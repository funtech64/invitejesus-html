import argparse
import hashlib
import os
import re
from typing import List, Tuple

CHUNK_SIZE = 8192  # 8KB


def md5sum(path: str) -> str:
    h = hashlib.md5()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()


def read_file(path: str) -> str:
    parts: List[str] = []
    with open(path, 'r', encoding='utf-8') as f:
        while True:
            chunk = f.read(CHUNK_SIZE)
            if not chunk:
                break
            parts.append(chunk)
    return ''.join(parts)


def slugify(title: str) -> str:
    slug = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
    return slug or 'untitled'


def extract_sections(text: str) -> List[Tuple[str, str]]:
    pattern = re.compile(r'([a-z0-9\-]+\.md)\s*\n(.*?)(?=\n[a-z0-9\-]+\.md\s*\n|\Z)', re.DOTALL | re.IGNORECASE)
    matches = pattern.finditer(text)
    results: List[Tuple[str, str]] = []
    for m in matches:
        fname = m.group(1).lower()
        content = m.group(2)
        header_match = re.search(r'#\s+.*', content)
        if not header_match:
            continue
        content = content[header_match.start():].strip()
        title = header_match.group(0)[2:].strip()
        slug = slugify(title)
        results.append((f"{slug}.md", content))
    return results


def write_files(sections: List[Tuple[str, str]], out_dir: str) -> Tuple[List[str], List[str]]:
    os.makedirs(out_dir, exist_ok=True)
    counts = {}
    written = []
    duplicates = []
    for fname, content in sections:
        base, ext = os.path.splitext(fname)
        count = counts.get(fname, 0)
        out_name = fname if count == 0 else f"{base}_v{count+1}{ext}"
        if count > 0:
            duplicates.append(out_name)
        counts[fname] = count + 1
        with open(os.path.join(out_dir, out_name), 'w', encoding='utf-8') as f:
            f.write(content.rstrip() + '\n')
        written.append(out_name)
    return written, duplicates


def main():
    parser = argparse.ArgumentParser(description='Extract markdown files from a chat log')
    parser.add_argument('input_file')
    parser.add_argument('-o', '--output', required=True)
    parser.add_argument('-b', '--backup', help='Path to backup file for md5 comparison')
    args = parser.parse_args()

    try:
        text = read_file(args.input_file)
    except FileNotFoundError:
        print(f"Input file not found: {args.input_file}")
        return

    print('First 200 chars of input:')
    print(text[:200])

    if args.backup and os.path.exists(args.backup):
        orig_md5 = md5sum(args.input_file)
        backup_md5 = md5sum(args.backup)
        if orig_md5 != backup_md5:
            print('Warning: md5 of input and backup differ before extraction')
    else:
        orig_md5 = md5sum(args.input_file)
        backup_md5 = None

    sections = extract_sections(text)
    print(f"Found {len(sections)} sections")

    written, duplicates = write_files(sections, args.output)
    with open(os.path.join(args.output, 'report.txt'), 'w', encoding='utf-8') as rep:
        rep.write('\n'.join(written) + '\n')
        rep.write(f"Total: {len(written)}\n")
        rep.write(f"Duplicates: {len(duplicates)}\n")

    after_md5 = md5sum(args.input_file)
    if after_md5 != orig_md5:
        print('Warning: input file md5 changed after extraction!')
    if backup_md5 and after_md5 != backup_md5:
        print('Warning: input file differs from backup after extraction')


if __name__ == '__main__':
    main()
