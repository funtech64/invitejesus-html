require 'yaml'
require 'json'
require 'fileutils'

DATA_GLOB = 'data/religions*.yaml'
OUTPUT_ROOT = 'world-religions'
BUILD_DIR = 'build'

files = Dir.glob(DATA_GLOB).sort
by_id = {}
source_file = {}
overwritten = []
chunks_seen = []
rules = {}

files.each do |file|
  data = YAML.load_file(file)
  resume = data['resume']
  chunks_seen << resume['chunk'] if resume && resume['chunk']
  rules = data['rules'] if data['rules']
  (data['entries'] || []).each do |entry|
    next unless entry['id'] && entry['name']
    id_orig = entry['id']
    slug = id_orig.downcase.gsub(' ', '-')
    entry['id'] = slug
    if by_id.key?(slug)
      overwritten << {'id'=>slug, 'from_file'=>source_file[slug], 'to_file'=>File.basename(file)}
    end
    by_id[slug] = entry
    source_file[slug] = File.basename(file)
  end
end

page_rule = rules['page_rule'] || {}
threshold = page_rule['percent_threshold'] || 1.0
overrides = (page_rule['overrides'] || []).map{|h| h['id']}

children = Hash.new{|h,k| h[k]=[]}
orphans = []
by_id.each do |id, entry|
  parent = entry['parent']
  next if parent.nil?
  unless by_id.key?(parent)
    orphans << id
    parent = 'world_religions'
    entry['parent'] = parent
  end
  children[parent] << id
end

by_id.each do |id, entry|
  percent = entry['percent_estimate']
  is_override = overrides.include?(id) || entry['page_reason'] == 'PAGE_OVERRIDE'
  meets = percent && percent.to_f >= threshold
  is_page = entry['is_page'] == true
  if is_override || meets || is_page
    entry['is_page_final'] = true
    if is_override
      entry['page_reason_final'] = 'PAGE_OVERRIDE'
    elsif meets || entry['page_reason'] == 'PAGE_THRESHOLD'
      entry['page_reason_final'] = 'PAGE_THRESHOLD'
    else
      entry['page_reason_final'] = 'PAGE_OVERRIDE'
    end
  else
    entry['is_page_final'] = false
    entry['page_reason_final'] = nil
  end
end

# compute urls
compute_url = lambda do |id|
  parts = []
  cur = by_id[id]
  while cur['parent']
    parts << cur['id']
    cur = by_id[cur['parent']]
  end
  parts.reverse!
  url = '/world-religions'
  parts.each { |p| url += "/#{p}" }
  url + '/index.html'
end

by_id.each { |id, entry| entry['url'] = compute_url.call(id) }

# breadcrumbs helper
breadcrumbs = lambda do |id|
  parts = []
  cur = by_id[id]
  while cur
    parts << cur['id']
    parent = cur['parent']
    break if parent.nil?
    cur = by_id[parent]
  end
  parts.reverse.map { |pid| e = by_id[pid]; {'id'=>pid, 'name'=>e['name'], 'url'=>e['url']} }
end

# render tree
render_tree = lambda do |id|
  e = by_id[id]
  kids = children[id] || []
  html = '<li>'
  if e['is_page_final']
    html += "<a href=\"#{e['url']}\">#{e['name']}</a>"
    if e['page_reason_final'] == 'PAGE_OVERRIDE'
      html += ' <span class="tag">PAGE (override)</span>'
    elsif e['page_reason_final'] == 'PAGE_THRESHOLD'
      html += " <span class=\"tag\">PAGE (≥#{threshold}%\)</span>"
    end
  else
    html += "<span>#{e['name']}</span> <span class=\"tag\">SUBSECTION</span>"
  end
  if kids.any?
    html += '<ul>'
    kids.each { |cid| html += render_tree.call(cid) }
    html += '</ul>'
  end
  html += '</li>'
  html
end

page_tree_html = "<nav class=\"page-tree\" aria-label=\"World Religions Tree\"><ul>"
page_tree_html += render_tree.call('world_religions')
page_tree_html += '</ul></nav>'

FileUtils.mkdir_p(OUTPUT_ROOT)

by_id.each do |id, entry|
  next unless entry['is_page_final']
  crumbs = breadcrumbs.call(id)
  breadcrumb_html = crumbs.each_with_index.map do |c,i|
    if i == crumbs.length - 1
      "<span>#{c['name']}</span>"
    else
      "<a href=\"#{c['url']}\">#{c['name']}</a> › "
    end
  end.join

  subsections_html = ''
  (children[id] || []).each do |cid|
    child = by_id[cid]
    if child['is_page_final']
      subsections_html += "<h3><a href=\"#{child['url']}\">#{child['name']}</a></h3>"
    else
      subsections_html += "<h3 id=\"#{child['id']}\">#{child['name']}</h3>"
      gkids = children[child['id']] || []
      if gkids.any?
        subsections_html += '<ul>'
        gkids.each do |gid|
          gc = by_id[gid]
          if gc['is_page_final']
            subsections_html += "<li><a href=\"#{gc['url']}\">#{gc['name']}</a></li>"
          else
            subsections_html += "<li><a href=\"##{gc['id']}\">#{gc['name']}</a></li>"
          end
        end
        subsections_html += '</ul>'
      else
        subsections_html += '<p>Details forthcoming.</p>'
      end
    end
  end

  lede = entry['percent_estimate'] ? "<p class=\"lede\">~#{entry['percent_estimate']}% of world population.</p>" : ''

  html = <<~HTML
  <!doctype html>
  <html lang=\"en\">
  <head>
    <meta charset=\"utf-8\"/>
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"/>
    <title>#{entry['name']} — InviteJesus</title>
    <link rel=\"stylesheet\" href=\"/assets/css/base.css\"/>
    <link rel=\"stylesheet\" href=\"/assets/css/page-tree.css\"/>
  </head>
  <body>
    <header class=\"site-header\">
      <a class=\"logo\" href=\"/\">InviteJesus</a>
    </header>
    #{page_tree_html}
    <nav class=\"breadcrumb\" aria-label=\"Breadcrumb\">#{breadcrumb_html}</nav>
    <main>
      <h1>#{entry['name']}</h1>
      #{lede}
      <section><h2>Overview</h2></section>
      <section><h2>History</h2></section>
      <section><h2>Core Beliefs</h2></section>
      <section><h2>Practices</h2></section>
      <section><h2>Demographics</h2></section>
      <section>
        <h2>Subsections</h2>
        #{subsections_html}
      </section>
    </main>
  </body>
  </html>
  HTML

  file_path = entry['url'][1..-1]
  FileUtils.mkdir_p(File.dirname(file_path))
  File.write(file_path, html)
end

report = {
  'counts'=>{
    'total'=>by_id.length,
    'pages_total'=>by_id.values.count{|e| e['is_page_final']},
    'pages_by_reason'=>{
      'threshold'=>by_id.values.count{|e| e['page_reason_final']=='PAGE_THRESHOLD'},
      'override'=>by_id.values.count{|e| e['page_reason_final']=='PAGE_OVERRIDE'}
    },
    'subsections_total'=>by_id.values.count{|e| !e['is_page_final']}
  },
  'chunks_seen'=>chunks_seen,
  'overwritten_ids'=>overwritten,
  'orphans_attached_to_root'=>orphans,
  'promotions'=>[],
  'demotions'=>[]
}

FileUtils.mkdir_p(BUILD_DIR)
File.write(File.join(BUILD_DIR, 'religions-report.json'), JSON.pretty_generate(report))
