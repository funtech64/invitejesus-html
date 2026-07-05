import re
import os

# Load the chat log from /data
input_file = 'data/philosophical_worldview_450_Output.txt'
with open(input_file, 'r', encoding='utf-8', errors='ignore') as f:
    data = f.read()

# Step 1: Clean - remove blank lines and normalize
cleaned_lines = [line.strip() for line in data.splitlines() if line.strip()]
cleaned_data = '\n'.join(cleaned_lines)

# Step 2: Extract MD blocks
pattern = r'([a-z0-9\-]+\.md)\s*text\s*(.*?)(?=\n[a-z0-9\-]+\.md\s*text\s*|\Z)'
matches = re.finditer(pattern, cleaned_data, flags=re.DOTALL | re.IGNORECASE)

# Output directory
output_dir = 'md_worldviews'
os.makedirs(output_dir, exist_ok=True)
extracted_files = []
counts = {}

for match in matches:
    filename = match.group(1).lower()
    content = match.group(2).strip()
    if content:
        # Handle tier in filename if present (e.g., -medium, -large)
        if '-medium' in filename or '-large' in filename:
            filename = filename  # Keep as-is
        else:
            # Check for tier hint in content (e.g., "Low Tier - Basic ~300 words")
            tier_match = re.search(r'(Low|High) Tier - Basic ~(\d+) words|Medium ~(\d+) words|Large ~(\d+) words', content)
            if tier_match:
                tier_type = tier_match.group(1) if tier_match.group(1) else 'medium' if tier_match.group(3) else 'large' if tier_match.group(4) else 'basic'
                word_count = tier_match.group(2) or tier_match.group(3) or tier_match.group(4) or '300'
                filename = f"{os.path.splitext(filename)[0]}-{tier_type}-{word_count}.md"
            else:
                filename = f"{os.path.splitext(filename)[0]}-basic-300.md"

        # Handle duplicates
        count = counts.get(filename, 0)
        if count:
            base, ext = os.path.splitext(filename)
            filename = f"{base}_v{count+1}{ext}"
        counts[filename] = count + 1

        # Write file
        file_path = os.path.join(output_dir, filename)
        with open(file_path, 'w', encoding='utf-8') as out:
            out.write(content + '\n')
        extracted_files.append(filename)

# Report
report = f"Extracted files:\n{'\n'.join(extracted_files)}\n\nTotal: {len(extracted_files)}"
with open(os.path.join(output_dir, 'report.txt'), 'w') as rep:
    rep.write(report)

print("Extraction complete! Check 'md_worldviews' folder.")
print(report)