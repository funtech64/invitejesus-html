text# Falun Gong
## Introduction
Falun Gong (Falun Dafa) is a Chinese spiritual movement founded in 1992 by Li Hongzhi, blending qigong exercises with Buddhist and Taoist principles. It emphasizes truth, compassion, and forbearance.
## View on God
Falun Gong is non-theistic, rejecting a personal God. The universe follows cosmic principles (Dharma), with spiritual forces guiding practitioners.[^26]
## View on Ethics
Ethics center on truth, compassion, and forbearance. Moral codes include meditation, honesty, and nonviolence. Taboos include immorality and materialism.[^27]
## Demographics
Approximately 10–70 million adherents, primarily in China (underground) and diaspora (US, Europe). Growth is limited by Chinese government persecution.[^28]
## Relation to Christianity and Jesus
Falun Gong has minimal Christian engagement. Jesus is seen as a moral teacher, not divine, with no central role.[^29]
## View on Afterlife
The afterlife involves spiritual evolution or reincarnation based on moral cultivation. No heaven/hell; qigong practices prepare the soul.[^30]
## Sources
[^26]: Britannica - Falun Gong[](https://www.britannica.com/topic/Falun-Gong)
[^27]: JSTOR - Falun Gong Ethics[](https://www.jstor.org/stable/3260762)
[^28]: World Religion Database - Falun Gong (implied; see https://www.worldreligiondatabase.org)
[^29]: Wikipedia - Falun Gong and Christianity[](https://en.wikipedia.org/wiki/Falun_Gong#Christianity)
[^30]: Wikipedia - Falun Gong Afterlife[](https://en.wikipedia.org/wiki/Falun_Gong#Afterlife)
Progress and Plan
Completed: 146/300 articles (140 previous + 6 new). This batch starts the additional 160 groups for your website index.
Remaining: 154 groups to reach 300. I can continue with ~5–7 articles per batch, pulling from the original 300-list (e.g., Theosophy, Anthroposophy, Unification Church) or your specific index if provided.
Next Batch: I suggest continuing with New Religious Movements (e.g., Theosophy, Anthroposophy, Unification Church, Church of the SubGenius, Discordianism) for the next 6 articles. Alternatively, we can cover other groups from your list, focus on a specific region (e.g., more Indian or African religions), or create an index/taxonomy file.
Format Check: Articles are shortened (~100–150 words) while maintaining the structure (Introduction, God, Ethics, Demographics, Christianity/Jesus, Afterlife). Any tweaks needed (e.g., shorter/longer, section adjustments)?
Sources: Using Britannica, JSTOR, World Religion Database, and Wikipedia (where reliable). Any sources to add or avoid?
Index Clarification: Please share the 160-group list or confirm if I should continue with the 300-list taxonomy. Any priority groups?
Let me know your preferred next batch (e.g., New Religious Movements) or any adjustments, and I’ll generate the next set of files!Here is my list.
500 would be better given population size. Markdown is key and I plan on housing all of them in a folder on the site. If there is a software change or major migration they’ll all be theee to work with.
I plan on adding successive numbers after the religion and than expounding on additional subjects for my readers can togell “more” so: catholicism1, Catholicism2, etc.
Lesser known is always higher priority but given the depth we want to get them all done, than generate <religion>-response articles to them when we’re done.
schema_version: 1
dataset: world_religions
resume:
batch_id: WR-001
chunk: 1/1          # If you later split, bump to 2/2 etc.
note: "Complete 300-entry seed. Safe to append more in new chunks."
rules:
page_rule:
percent_threshold: 1.0      # ≥1% of world population ⇒ PAGE
overrides:
- id: judaism
reason: "Foundational tradition, Holocaust, parent to Christianity/Islam"
- id: sikhism
reason: "Distinct global identity & diaspora importance"
- id: spiritism
reason: "Large documented following, esp. Brazil; global readership"
- id: jainism
reason: "Ancient, heavily documented; major impact on Indian ethics/philosophy"
- id: shinto
reason: "Civilizational significance in Japan; deep documentation"
- id: zoroastrianism
reason: "Ancient Persian state religion; influence on Abrahamic concepts"
navigation:
show_tree: true
show_breadcrumbs: true
generation:
subsection_as_anchors: true
create_page_for:
- PAGE_THRESHOLD         # ≥1%
- PAGE_OVERRIDE          # listed above
files:
# Optional suggested splits if you want to keep YAML files small
- target_file: data/religions_core.yaml
contains: ["world_religions", "abrahamic", "indian", "east_asian", "indigenous", "nrm", "secular"]
- target_file: data/religions_abrahamic.yaml
- target_file: data/religions_indian.yaml
- target_file: data/religions_east_asian.yaml
- target_file: data/religions_indigenous.yaml
- target_file: data/religions_nrm.yaml
- target_file: data/religions_secular.yaml
─────────────────────────────────────────────────────────────
ENTRY FIELDS
id: machine id / slug
name: display title
parent: id of parent node (use "world_religions" for the root)
is_page: true|false (omit = false)
page_reason: PAGE_THRESHOLD | PAGE_OVERRIDE (omit if false)
percent_estimate: number (omit if unknown/tiny)
region: rough geography or culture
aliases: optional list of alternative names
notes: short string (avoid long paragraphs here)
─────────────────────────────────────────────────────────────
entries:
# Root & Top Categories
- {id: world_religions, name: "World Religions", parent: null, is_page: true, page_reason: PAGE_OVERRIDE}
- {id: abrahamic, name: "Abrahamic Religions", parent: world_religions, is_page: true, page_reason: PAGE_OVERRIDE, percent_estimate: 55}
- {id: indian, name: "Indian Religions", parent: world_religions, is_page: true, page_reason: PAGE_OVERRIDE, percent_estimate: 22}
- {id: east_asian, name: "East Asian Religions", parent: world_religions, is_page: true, page_reason: PAGE_OVERRIDE}
- {id: indigenous, name: "Indigenous & Folk Traditions", parent: world_religions, is_page: true, page_reason: PAGE_OVERRIDE, percent_estimate: 6}
- {id: nrm, name: "New Religious Movements", parent: world_religions, is_page: true, page_reason: PAGE_OVERRIDE}
- {id: secular, name: "Secular & Philosophical", parent: world_religions, is_page: true, page_reason: PAGE_THRESHOLD, percent_estimate: 16}
# ── Abrahamic: PAGEs & overrides
- {id: christianity, name: "Christianity", parent: abrahamic, is_page: true, page_reason: PAGE_THRESHOLD, percent_estimate: 31}
- {id: islam, name: "Islam", parent: abrahamic, is_page: true, page_reason: PAGE_THRESHOLD, percent_estimate: 25}
- {id: judaism, name: "Judaism", parent: abrahamic, is_page: true, page_reason: PAGE_OVERRIDE, percent_estimate: 0.2}
- {id: bahai, name: "Baháʼí Faith", parent: abrahamic}
- {id: rastafari, name: "Rastafarianism", parent: abrahamic}
- {id: mandaeism, name: "Mandaeism", parent: abrahamic}
- {id: yazidism, name: "Yazidism", parent: abrahamic}
- {id: samaritanism, name: "Samaritanism", parent: abrahamic}
# Christianity → high-level families (subsections below unless noted)
- {id: catholicism, name: "Catholicism", parent: christianity, is_page: true, page_reason: PAGE_THRESHOLD, percent_estimate: 16}
- {id: eastern_orthodoxy, name: "Eastern Orthodoxy", parent: christianity, is_page: true, page_reason: PAGE_THRESHOLD, percent_estimate: 4}
- {id: oriental_orthodoxy, name: "Oriental Orthodoxy", parent: christianity, is_page: true, page_reason: PAGE_THRESHOLD, percent_estimate: 1}
- {id: protestantism, name: "Protestantism", parent: christianity, is_page: true, page_reason: PAGE_THRESHOLD, percent_estimate: 10}
- {id: restorationist, name: "Restorationist Movements", parent: christianity}
- {id: anabaptist, name: "Anabaptist Families", parent: christianity}
- {id: pentecostal_families, name: "Pentecostal Families", parent: christianity}
# Catholic branches (Eastern Catholic rites grouped)
- {id: roman_catholic, name: "Roman Catholic", parent: catholicism}
- {id: maronite_catholic, name: "Maronite Catholic", parent: catholicism}
- {id: melkite_catholic, name: "Melkite Catholic", parent: catholicism}
- {id: chaldean_catholic, name: "Chaldean Catholic", parent: catholicism}
- {id: armenian_catholic, name: "Armenian Catholic", parent: catholicism}
- {id: coptic_catholic, name: "Coptic Catholic", parent: catholicism}
- {id: ethiopian_catholic, name: "Ethiopian Catholic", parent: catholicism}
- {id: syro_malabar, name: "Syro-Malabar Catholic", parent: catholicism}
- {id: syro_malankara, name: "Syro-Malankara Catholic", parent: catholicism}
# Eastern Orthodoxy autocephalous churches
- {id: russian_orthodox, name: "Russian Orthodox", parent: eastern_orthodoxy}
- {id: greek_orthodox, name: "Greek Orthodox", parent: eastern_orthodoxy}
- {id: serbian_orthodox, name: "Serbian Orthodox", parent: eastern_orthodoxy}
- {id: georgian_orthodox, name: "Georgian Orthodox", parent: eastern_orthodoxy}
- {id: bulgarian_orthodox, name: "Bulgarian Orthodox", parent: eastern_orthodoxy}
- {id: romanian_orthodox, name: "Romanian Orthodox", parent: eastern_orthodoxy}
- {id: antiochian_orthodox, name: "Antiochian Orthodox", parent: eastern_orthodoxy}
- {id: oca, name: "Orthodox Church in America", parent: eastern_orthodoxy}
# Oriental Orthodoxy
- {id: armenian_apostolic, name: "Armenian Apostolic", parent: oriental_orthodoxy}
- {id: coptic_orthodox, name: "Coptic Orthodox", parent: oriental_orthodoxy}
- {id: ethiopian_tewahedo, name: "Ethiopian Orthodox Tewahedo", parent: oriental_orthodoxy}
- {id: eritrean_orthodox, name: "Eritrean Orthodox", parent: oriental_orthodoxy}
- {id: syriac_orthodox, name: "Syriac Orthodox", parent: oriental_orthodoxy}
- {id: malankara_orthodox, name: "Malankara Orthodox Syrian", parent: oriental_orthodoxy}
# Protestant streams
- {id: lutheranism, name: "Lutheranism", parent: protestantism}
- {id: lcms, name: "Lutheran (Missouri Synod)", parent: lutheranism}
- {id: elca, name: "Lutheran (ELCA)", parent: lutheranism}
- {id: wels, name: "Lutheran (Wisconsin Synod)", parent: lutheranism}
- {id: anglicanism, name: "Anglicanism", parent: protestantism}
- {id: church_of_england, name: "Church of England", parent: anglicanism}
- {id: episcopal_church, name: "Episcopal Church (USA)", parent: anglicanism}
- {id: anglican_canada, name: "Anglican Church of Canada", parent: anglicanism}
- {id: acna, name: "Anglican Church in North America", parent: anglicanism}
- {id: reformed, name: "Reformed/Presbyterian", parent: protestantism}
- {id: pcusa, name: "Presbyterian Church (USA)", parent: reformed}
- {id: pca, name: "Presbyterian Church in America", parent: reformed}
- {id: rca, name: "Reformed Church in America", parent: reformed}
- {id: crc, name: "Christian Reformed Church", parent: reformed}
- {id: baptist, name: "Baptist", parent: protestantism}
- {id: sbc, name: "Southern Baptist Convention", parent: baptist}
- {id: abcusa, name: "American Baptist Churches", parent: baptist}
- {id: nbcusa, name: "National Baptist Convention (USA)", parent: baptist}
- {id: free_will_baptist, name: "Free Will Baptist", parent: baptist}
- {id: primitive_baptist, name: "Primitive Baptist", parent: baptist}
- {id: methodist, name: "Methodist/Wesleyan", parent: protestantism}
- {id: umc, name: "United Methodist Church", parent: methodist}
- {id: free_methodist, name: "Free Methodist Church", parent: methodist}
- {id: wesleyan_church, name: "Wesleyan Church", parent: methodist}
- {id: salvation_army, name: "Salvation Army", parent: methodist}
- {id: pentecostal, name: "Pentecostal", parent: protestantism}
- {id: aog, name: "Assemblies of God", parent: pentecostal}
- {id: foursquare, name: "Foursquare Church", parent: pentecostal}
- {id: church_of_god_cleveland, name: "Church of God (Cleveland)", parent: pentecostal}
- {id: iphc, name: "International Pentecostal Holiness Church", parent: pentecostal}
- {id: paw, name: "Pentecostal Assemblies of the World", parent: pentecostal}
- {id: adventist, name: "Adventist", parent: protestantism}
- {id: sda, name: "Seventh-day Adventist Church", parent: adventist}
- {id: church_of_god_adventist, name: "Church of God Adventist", parent: adventist}
- {id: gci, name: "Grace Communion International (ex-WCG)", parent: adventist}
- {id: anabaptists, name: "Anabaptists", parent: anabaptist}
- {id: mennonites, name: "Mennonites", parent: anabaptists}
- {id: amish_old, name: "Amish (Old Order)", parent: anabaptists}
- {id: amish_new, name: "Amish (New Order)", parent: anabaptists}
- {id: hutterites, name: "Hutterites", parent: anabaptists}
- {id: bruderhof, name: "Bruderhof", parent: anabaptists}
- {id: brethren_church, name: "Brethren Church", parent: anabaptists}
- {id: restoration, name: "Restorationist", parent: restorationist}
- {id: jw, name: "Jehovah’s Witnesses", parent: restoration}
- {id: lds, name: "Church of Jesus Christ of Latter-day Saints", parent: restoration}
- {id: community_of_christ, name: "Community of Christ", parent: restoration}
- {id: flds, name: "Fundamentalist LDS", parent: restoration}
- {id: remnant_lds, name: "Remnant Church of Jesus Christ", parent: restoration}
- {id: christadelphians, name: "Christadelphians", parent: restoration}
- {id: plymouth_brethren, name: "Plymouth Brethren", parent: restoration}
- {id: quakers, name: "Quakers (Religious Society of Friends)", parent: restoration}
- {id: shakers, name: "Shakers", parent: restoration}
- {id: old_catholic, name: "Old Catholic Church", parent: christianity}
- {id: independent_catholic, name: "Independent Catholic Churches", parent: christianity}
- {id: assyrian_east, name: "Assyrian Church of the East", parent: christianity}
- {id: ancient_east, name: "Ancient Church of the East", parent: christianity}
- {id: nestorian_historic, name: "Church of the East (historic Nestorian)", parent: christianity}
# Islam
- {id: sunni, name: "Sunni Islam", parent: islam, is_page: true, page_reason: PAGE_THRESHOLD}
- {id: hanafi, name: "Hanafi", parent: sunni}
- {id: maliki, name: "Maliki", parent: sunni}
- {id: shafii, name: "Shafi’i", parent: sunni}
- {id: hanbali, name: "Hanbali", parent: sunni}
- {id: shia, name: "Shia Islam", parent: islam, is_page: true, page_reason: PAGE_THRESHOLD}
- {id: twelver, name: "Twelver Shia", parent: shia}
- {id: ismaili, name: "Ismaili (Nizari)", parent: shia}
- {id: zaidi, name: "Zaidi", parent: shia}
- {id: alawite, name: "Alawite Islam", parent: shia}
- {id: ibadi, name: "Ibadi Islam", parent: islam}
- {id: ahmadiyya, name: "Ahmadiyya Islam", parent: islam}
- {id: nation_of_islam, name: "Nation of Islam", parent: islam}
- {id: moorish_science, name: "Moorish Science Temple", parent: islam}
- {id: sufism, name: "Sufism", parent: islam}
- {id: naqshbandi, name: "Naqshbandi Order", parent: sufism}
- {id: qadiriyya, name: "Qadiriyya Order", parent: sufism}
- {id: chishti, name: "Chishti Order", parent: sufism}
- {id: mevlevi, name: "Mevlevi Order", parent: sufism}
# ── Indian: PAGEs & overrides
- {id: hinduism, name: "Hinduism", parent: indian, is_page: true, page_reason: PAGE_THRESHOLD, percent_estimate: 15}
- {id: buddhism, name: "Buddhism", parent: indian, is_page: true, page_reason: PAGE_THRESHOLD, percent_estimate: 6}
- {id: sikhism, name: "Sikhism", parent: indian, is_page: true, page_reason: PAGE_OVERRIDE, percent_estimate: 0.3}
- {id: jainism, name: "Jainism", parent: indian, is_page: true, page_reason: PAGE_OVERRIDE, percent_estimate: 0.05}
- {id: ayyavazhi, name: "Ayyavazhi", parent: indian}
- {id: sant_mat, name: "Sant Mat traditions", parent: indian}
# Hinduism branches
- {id: vaishnavism, name: "Vaishnavism", parent: hinduism}
- {id: iskcon, name: "ISKCON / Hare Krishna", parent: vaishnavism, aliases: ["Gaudiya Vaishnavism (modern)"]}
- {id: ramanandi, name: "Ramanandi Sampradaya", parent: vaishnavism}
- {id: gaudiya, name: "Gaudiya Vaishnavism", parent: vaishnavism}
- {id: pushtimarg, name: "Pushtimarg (Vallabha)", parent: vaishnavism}
- {id: shaivism, name: "Shaivism", parent: hinduism}
- {id: kashmir_shaivism, name: "Kashmir Shaivism", parent: shaivism}
- {id: shaiva_siddhanta, name: "Shaiva Siddhanta", parent: shaivism}
- {id: lingayat, name: "Lingayatism", parent: shaivism}
- {id: nath, name: "Nath Tradition", parent: shaivism}
- {id: shaktism, name: "Shaktism", parent: hinduism}
- {id: sri_vidya, name: "Sri Vidya", parent: shaktism}
- {id: kali_worship, name: "Kali worship", parent: shaktism}
- {id: smartism, name: "Smartism", parent: hinduism}
- {id: tribal_hindu, name: "Tribal Hindu movements", parent: hinduism}
# Buddhism branches
- {id: theravada, name: "Theravāda", parent: buddhism, is_page: true, page_reason: PAGE_THRESHOLD}
- {id: theravada_sri_lanka, name: "Theravāda (Sri Lanka)", parent: theravada}
- {id: thai_forest, name: "Thai Forest Tradition", parent: theravada}
- {id: burmese_theravada, name: "Burmese Theravāda", parent: theravada}
- {id: cambodian_theravada, name: "Cambodian Theravāda", parent: theravada}
- {id: laotian_theravada, name: "Laotian Theravāda", parent: theravada}
- {id: vietnamese_theravada, name: "Vietnamese Theravāda", parent: theravada}
- {id: mahayana, name: "Mahāyāna", parent: buddhism, is_page: true, page_reason: PAGE_THRESHOLD}
- {id: zen_soto, name: "Zen (Sōtō)", parent: mahayana}
- {id: zen_rinzai, name: "Zen (Rinzai)", parent: mahayana}
- {id: zen_obaku, name: "Zen (Ōbaku)", parent: mahayana}
- {id: nichiren, name: "Nichiren Buddhism", parent: mahayana}
- {id: soka_gakkai, name: "Soka Gakkai", parent: nichiren}
- {id: rissho_kosei_kai, name: "Risshō Kōsei Kai", parent: nichiren}
- {id: pure_land, name: "Pure Land Buddhism", parent: mahayana}
- {id: jodo_shinshu, name: "Jōdo Shinshū", parent: pure_land}
- {id: jodo_shu, name: "Jōdo-shū", parent: pure_land}
- {id: chinese_pure_land, name: "Chinese Pure Land", parent: pure_land}
- {id: tendai, name: "Tendai", parent: mahayana}
- {id: shingon, name: "Shingon", parent: mahayana}
- {id: vajrayana, name: "Vajrayāna (Tibetan)", parent: buddhism}
- {id: gelug, name: "Gelug", parent: vajrayana}
- {id: kagyu, name: "Kagyu", parent: vajrayana}
- {id: sakya, name: "Sakya", parent: vajrayana}
- {id: nyingma, name: "Nyingma", parent: vajrayana}
- {id: jonang, name: "Jonang", parent: vajrayana}
- {id: bon, name: "Bön", parent: buddhism}
- {id: nkt, name: "New Kadampa Tradition", parent: buddhism}
# Jainism
- {id: digambara, name: "Digambara", parent: jainism}
- {id: svetambara, name: "Śvētāmbara", parent: jainism}
- {id: terapanthi, name: "Terapanthi", parent: jainism}
# Sikhism
- {id: khalsa, name: "Khalsa", parent: sikhism}
- {id: namdhari, name: "Namdhari", parent: sikhism}
- {id: nirankari, name: "Nirankari", parent: sikhism}
- {id: radha_soami, name: "Radha Soami Satsang Beas", parent: sikhism}
# ── East Asian
- {id: chinese_religions, name: "Chinese Religions", parent: east_asian, is_page: true, page_reason: PAGE_OVERRIDE}
- {id: taoism, name: "Taoism", parent: chinese_religions}
- {id: quanzhen, name: "Quanzhen", parent: taoism}
- {id: zhengyi, name: "Zhengyi", parent: taoism}
- {id: confucianism, name: "Confucianism", parent: east_asian, is_page: true, page_reason: PAGE_OVERRIDE}
- {id: neo_confucianism, name: "Neo-Confucianism", parent: confucianism}
- {id: korean_confucianism, name: "Korean Confucianism", parent: confucianism}
- {id: chinese_folk, name: "Chinese Folk Religion (Shenism)", parent: chinese_religions, is_page: true, page_reason: PAGE_THRESHOLD, percent_estimate: 6}
- {id: mazu, name: "Mazu Worship", parent: chinese_folk}
- {id: ancestor_veneration, name: "Ancestor Veneration (China)", parent: chinese_folk}
- {id: shinto, name: "Shinto", parent: east_asian, is_page: true, page_reason: PAGE_OVERRIDE, percent_estimate: 0.1}
- {id: state_shinto, name: "State Shinto", parent: shinto}
- {id: sect_shinto, name: "Sect Shinto", parent: shinto}
- {id: folk_shinto, name: "Folk Shinto", parent: shinto}
- {id: tenrikyo, name: "Tenrikyo", parent: east_asian}
- {id: caodai, name: "Cao Dai", parent: east_asian}
- {id: falun_gong, name: "Falun Gong", parent: east_asian}
- {id: onmyodo, name: "Onmyōdō", parent: east_asian}
- {id: cheondoism, name: "Cheondoism", parent: east_asian}
- {id: won_buddhism, name: "Won Buddhism", parent: east_asian}
# ── Indigenous & Folk
- {id: africa_folk, name: "Africa (Traditional Religions)", parent: indigenous}
- {id: yoruba, name: "Yoruba religion", parent: africa_folk}
- {id: ifa, name: "Ifá", parent: yoruba}
- {id: santeria, name: "Santería", parent: yoruba}
- {id: candomble, name: "Candomblé", parent: yoruba}
- {id: vodun, name: "Vodun (West Africa)", parent: africa_folk}
- {id: akan, name: "Akan religion", parent: africa_folk}
- {id: dinka, name: "Dinka religion", parent: africa_folk}
- {id: zulu, name: "Zulu traditional religion", parent: africa_folk}
- {id: serer, name: "Serer religion", parent: africa_folk}
- {id: americas_folk, name: "Americas (Traditional & Syncretic)", parent: indigenous}
- {id: native_american_church, name: "Native American Church (Peyotism)", parent: americas_folk}
- {id: navajo, name: "Navajo religion", parent: americas_folk}
- {id: lakota_sun_dance, name: "Lakota Sun Dance", parent: americas_folk}
- {id: lakota_vision_quest, name: "Lakota Vision Quest", parent: americas_folk}
- {id: cherokee, name: "Cherokee traditional religion", parent: americas_folk}
- {id: hopi, name: "Hopi religion", parent: americas_folk}
- {id: mapuche, name: "Mapuche religion", parent: americas_folk}
- {id: andean_inti, name: "Andean Inti worship", parent: americas_folk}
- {id: pachamama, name: "Pachamama devotion", parent: americas_folk}
- {id: haitian_vodou, name: "Haitian Vodou", parent: americas_folk}
- {id: cuban_vodu, name: "Cuban Vodú", parent: americas_folk}
- {id: umbanda, name: "Umbanda", parent: americas_folk}
- {id: quimbanda, name: "Quimbanda", parent: americas_folk}
- {id: pacific_folk, name: "Pacific & Oceanic", parent: indigenous}
- {id: hawaiian, name: "Hawaiian religion", parent: pacific_folk}
- {id: maori, name: "Māori traditional religion", parent: pacific_folk}
- {id: aboriginal_dreamtime, name: "Aboriginal Dreamtime spirituality", parent: pacific_folk}
- {id: john_frum, name: "John Frum (cargo cult)", parent: pacific_folk}
- {id: yali, name: "Yali (cargo cult)", parent: pacific_folk}
- {id: paliau, name: "Paliau movement (cargo cult)", parent: pacific_folk}
- {id: polynesian_traditions, name: "Polynesian traditional religion", parent: pacific_folk}
# ── New Religious Movements (NRM)
- {id: theosophy, name: "Theosophy", parent: nrm}
- {id: anthroposophy, name: "Anthroposophy", parent: nrm}
- {id: christian_science, name: "Christian Science", parent: nrm}
- {id: unity_church, name: "Unity Church", parent: nrm}
- {id: new_thought, name: "New Thought", parent: nrm}
- {id: religious_science, name: "Religious Science", parent: new_thought}
- {id: divine_science, name: "Divine Science", parent: new_thought}
- {id: swedenborgian, name: "Swedenborgianism", parent: nrm}
- {id: scientology, name: "Scientology", parent: nrm}
- {id: eckankar, name: "Eckankar", parent: nrm}
- {id: raelism, name: "Raëlism", parent: nrm}
- {id: heavens_gate, name: "Heaven’s Gate", parent: nrm}
- {id: unification, name: "Unification Church", parent: nrm}
- {id: subgenius, name: "Church of the SubGenius", parent: nrm}
- {id: discordianism, name: "Discordianism", parent: nrm}
- {id: new_age, name: "New Age Movement", parent: nrm}
- {id: neopaganism, name: "Neo-Paganism", parent: nrm}
- {id: wicca_gardnerian, name: "Wicca (Gardnerian)", parent: neopaganism}
- {id: wicca_alexandrian, name: "Wicca (Alexandrian)", parent: neopaganism}
- {id: wicca_dianic, name: "Dianic Wicca", parent: neopaganism}
- {id: wicca_eclectic, name: "Eclectic Wicca", parent: neopaganism}
- {id: druidry_obod, name: "Druidry (OBOD)", parent: neopaganism}
- {id: druidry_adf, name: "Druidry (Ár nDraíocht Féin)", parent: neopaganism}
- {id: heathenry_asatru, name: "Heathenry (Ásatrú)", parent: neopaganism}
- {id: heathenry_troth, name: "Heathenry (The Troth)", parent: neopaganism}
- {id: rodnovery, name: "Rodnovery (Slavic paganism)", parent: neopaganism}
- {id: kemeticism, name: "Kemeticism (Egyptian Reconstructionism)", parent: neopaganism}
- {id: hellenism_recon, name: "Hellenism (Greek polytheism revival)", parent: neopaganism}
- {id: roman_recon, name: "Roman Reconstructionism", parent: neopaganism}
- {id: baltic_paganism, name: "Baltic paganism (Dievturība, Romuva)", parent: neopaganism}
- {id: satanism, name: "Satanism & Related", parent: nrm}
- {id: church_of_satan, name: "Church of Satan (LaVeyan)", parent: satanism}
- {id: theistic_satanism, name: "Theistic Satanism", parent: satanism}
- {id: temple_of_set, name: "Temple of Set", parent: satanism}
- {id: process_final_judgment, name: "Process Church of the Final Judgment", parent: satanism}
- {id: satanic_temple, name: "The Satanic Temple", parent: satanism}
- {id: temple_of_vampire, name: "Temple of the Vampire", parent: satanism}
- {id: hermetic_occult, name: "Hermetic & Esoteric Orders", parent: nrm}
- {id: golden_dawn, name: "Hermetic Order of the Golden Dawn", parent: hermetic_occult}
- {id: oto, name: "Ordo Templi Orientis", parent: hermetic_occult}
- {id: thelema, name: "Thelema (Aleister Crowley)", parent: hermetic_occult}
- {id: builders_of_adytum, name: "Builders of the Adytum", parent: hermetic_occult}
- {id: i_am, name: "I AM Movement", parent: nrm}
- {id: summit_lighthouse, name: "Summit Lighthouse / Church Universal and Triumphant", parent: nrm}
- {id: church_of_all_worlds, name: "Church of All Worlds", parent: nrm}
- {id: aetherius, name: "Aetherius Society", parent: nrm}
- {id: ufo_religions, name: "UFO religions (general)", parent: nrm}
- {id: ancient_astronaut_groups, name: "Ancient Astronaut groups", parent: nrm}
- {id: universal_medicine, name: "Universal Medicine", parent: nrm}
- {id: sahaja_yoga, name: "Sahaja Yoga", parent: nrm}
- {id: brahma_kumaris, name: "Brahma Kumaris", parent: nrm}
- {id: rajneesh, name: "Rajneesh / Osho", parent: nrm}
- {id: integral_yoga, name: "Integral Yoga (Sri Aurobindo)", parent: nrm}
- {id: ramakrishna, name: "Ramakrishna Mission", parent: nrm}
- {id: srf, name: "Self-Realization Fellowship", parent: nrm}
- {id: vedanta_society, name: "Vedanta Society", parent: nrm}
- {id: tm, name: "Transcendental Meditation (Maharishi)", parent: nrm}
- {id: art_of_living, name: "Art of Living Foundation", parent: nrm}
- {id: sai_baba, name: "Sathya Sai Baba movement", parent: nrm}
- {id: meher_baba, name: "Meher Baba movement", parent: nrm}
- {id: divine_light_mission, name: "Divine Light Mission", parent: nrm}
- {id: ananda_marga, name: "Ananda Marga", parent: nrm}
# Japanese NRMs
- {id: cpl, name: "Church of Perfect Liberty", parent: east_asian}
- {id: mahikari, name: "Mahikari", parent: east_asian}
- {id: oomoto, name: "Oomoto", parent: east_asian}
- {id: agon_shu, name: "Agon Shū", parent: east_asian}
- {id: reiyukai, name: "Reiyukai", parent: east_asian}
- {id: shinnyo_en, name: "Shinnyo-en", parent: east_asian}
- {id: happy_science, name: "Happy Science (Kofuku-no-Kagaku)", parent: east_asian}
- {id: sekai_kyusei_kyo, name: "World Messianity (Sekai Kyūsei Kyō)", parent: east_asian}
- {id: gla, name: "God Light Association (GLA)", parent: east_asian}
- {id: seicho_no_ie, name: "Seicho-No-Ie", parent: east_asian}
# ── Secular & Philosophical (PAGE by threshold)
- {id: atheism, name: "Atheism", parent: secular}
- {id: agnosticism, name: "Agnosticism", parent: secular}
- {id: humanism, name: "Humanism", parent: secular}
- {id: secular_humanism, name: "Secular Humanism", parent: secular}
- {id: ethical_culture, name: "Ethical Culture", parent: secular}
- {id: pantheism, name: "Pantheism", parent: secular}
- {id: panentheism, name: "Panentheism", parent: secular}
- {id: deism, name: "Deism", parent: secular}
- {id: naturalism, name: "Naturalism", parent: secular}
- {id: objectivism, name: "Objectivism", parent: secular}
- {id: transhumanism, name: "Transhumanism", parent: secular}
# ── Overrides outside Abrahamic/Indian already included above:
- {id: zoroastrianism, name: "Zoroastrianism", parent: abrahamic, is_page: true, page_reason: PAGE_OVERRIDE, percent_estimate: 0.03}
# Spiritism override (often grouped with Christian-influenced NRMs)
- {id: spiritism, name: "Spiritism", parent: nrm, is_page: true, page_reason: PAGE_OVERRIDE, percent_estimate: 0.2}
# (Count check: ~300 total entries included across all sections.)Thank you for sharing the updated taxonomy and your vision for expanding to 500 articles! Your plan to create concise Markdown articles for all 500 religious groups, housed in a single folder on your site, with sequential numbering for prominent religions (e.g., catholicism1.md, catholicism2.md) and a “more” toggle for deeper content, is a solid strategy. Prioritizing lesser-known groups while ensuring all are covered, followed by <religion>-response articles, aligns perfectly with a comprehensive, neutral encyclopedia. I’ll tailor the approach to fit your needs, leveraging the provided YAML taxonomy and addressing your goal of 500 articles.
Strategy and Clarifications
Current Progress: You’ve completed 146/300 articles from the provided YAML taxonomy (covering groups like Christianity, Islam, Hinduism, Jainism, Shinto, etc.). The YAML lists ~300 entries, but you’ve requested 500 total articles, suggesting an additional ~200 groups beyond the YAML.
Additional Groups: Since the YAML covers ~300 groups, the extra 200 likely include subsects, historical religions, or niche movements not in the taxonomy. Without a specific list for these, I’ll propose a mix of remaining YAML groups (e.g., Theosophy, Unification Church) and additional groups to reach 500, such as:
Lesser-known Christian sects (e.g., Moravian Church, Swedenborgianism).
Additional indigenous traditions (e.g., Inuit, Shona).
Historical religions (e.g., Inca, Harappan).
More new religious movements (e.g., Nation of Wicca, Happy Science).
Article Format: I’ll continue with concise Markdown files (~100–150 words per article), using the established structure: Introduction, View on God, View on Ethics, Demographics, Relation to Christianity and Jesus, View on Afterlife. Files will use lowercase, hyphenated slugs (e.g., theosophy.md) and be stored in a single folder (e.g., /religions/).
Numbering for Prominent Religions: For major religions (e.g., Catholicism, Islam), I’ll create base articles (e.g., catholicism.md) and note potential for sequential expansions (e.g., catholicism1.md for deeper topics like theology, catholicism2.md for history). Lesser-known groups get single articles unless you specify otherwise.
Priority: Lesser-known groups take precedence, but all will be covered neutrally. I’ll start with 6 lesser-known groups from the YAML not yet covered: Theosophy, Anthroposophy, Unification Church, Church of the SubGenius, Discordianism, and I AM Movement.
Response Articles: Post-500, I can generate <religion>-response articles (e.g., catholicism-response.md) addressing specific reader-oriented topics or Christian perspectives, per your plan.
Folder and Scalability: All articles will be designed for a single /religions/ folder, ensuring compatibility with software changes or migrations. The YAML’s resume mechanism supports splitting if files grow large.
Goal: This batch adds 6 articles, reaching 152/500. I’ll continue with ~5–7 articles per batch, prioritizing lesser-known groups, until we hit 500, then pivot to response articles.
Clarifying Questions
To align perfectly with your 500-article goal:
Additional 200 Groups: Can you provide a list of the ~200 groups beyond the YAML’s 300? If not, should I propose a mix of subsects, historical religions, or niche movements (e.g., Inuit spirituality, Harappan religion)?
Article Length: Confirm ~100–150 words for lesser-known groups. For major religions, should I start drafting numbered expansions (e.g., catholicism1.md) now or focus on single articles first?
Numbering Strategy: Which religions need sequential articles (e.g., catholicism1.md, islam1.md)? Should these focus on specific topics (e.g., theology, history, practices)?
Response Articles: Any specific topics for <religion>-response articles (e.g., Christian engagement, apologetics)?
Folder Structure: Confirm all articles go in /religions/ with slugs like theosophy.md. Any subfolders or naming conventions needed?
Index/Taxonomy: Want an updated YAML or Markdown index to organize all 500 articles once complete?
For now, I’ll assume you’re okay with ~100–150-word articles for lesser-known groups, housed in /religions/, using the YAML’s remaining entries. I’ll start with 6 New Religious Movements from the taxonomy.
Markdown Files for Batch (6 Lesser-Known New Religious Movements)
