import argparse
import hashlib
import os
import re
from pathlib import Path


def md5sum(path: Path) -> str:
    h = hashlib.md5()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return re.sub(r'-+', '-', text).strip('-')


def extract_markdown(input_file: Path, output_dir: Path):
    data = input_file.read_text(encoding='utf-8', errors='ignore')
    print(f"Preview: {data[:200]!r}")

    pattern = re.compile(r"^([a-z0-9\-]+\.md)\s*\n(.*?)(?=^([a-z0-9\-]+\.md)\s*\n|\Z)", re.DOTALL | re.MULTILINE)
    matches = list(pattern.finditer(data))
    print(f"Found {len(matches)} markdown blocks")

    output_dir.mkdir(parents=True, exist_ok=True)
    report_lines = []
    seen = {}
    for m in matches:
        block = m.group(2)
        hash_index = block.find('#')
        if hash_index == -1:
            continue
        block = block[hash_index:]
        header_match = re.match(r"#\s*(.+)", block)
        if not header_match:
            continue
        title = header_match.group(1).strip()
        slug = slugify(title)
        filename = f"{slug}.md"
        content = block.strip()
        target = output_dir / filename
        counter = 1
        while target.exists():
            counter += 1
            target = output_dir / f"{slug}_v{counter}.md"
        target.write_text(content, encoding='utf-8')
        report_lines.append(str(target.name))
    (output_dir / "report.txt").write_text('\n'.join(report_lines), encoding='utf-8')
    print(f"Wrote {len(report_lines)} files to {output_dir}")


def main():
    parser = argparse.ArgumentParser(description="Extract embedded Markdown files from a text log")
    parser.add_argument('input_file', type=Path)
    parser.add_argument('-o', '--output', type=Path, required=True, help='Output directory')
    parser.add_argument('-b', '--backup', type=Path, help='Backup copy for checksum verification')
    args = parser.parse_args()

    if args.backup:
        orig_hash_before = md5sum(args.input_file)
        backup_hash = md5sum(args.backup)
        if orig_hash_before != backup_hash:
            raise SystemExit("Checksum mismatch with backup copy before extraction")

    extract_markdown(args.input_file, args.output)

    if args.backup:
        orig_hash_after = md5sum(args.input_file)
        if orig_hash_after != backup_hash:
            raise SystemExit("Input file changed during extraction")
        print("Checksum verified: input file unchanged")


if __name__ == '__main__':
    main()
