import os
import re
import argparse


def extract_markdown(input_path: str, output_dir: str = 'extracted_md_files') -> int:
    """Extract embedded markdown files from a chat log text file.

    Parameters
    ----------
    input_path: Path to the text file containing embedded markdown.
    output_dir: Directory where extracted .md files will be written.

    Returns
    -------
    int
        Number of markdown files extracted.
    """
    with open(input_path, 'r', encoding='utf-8', errors='ignore') as f:
        data = f.read()

    print("DEBUG first 200 chars:\n" + data[:200])

    pattern = r'([a-z0-9\-]+\.md)\s*\n(.*?)(?=\n[a-z0-9\-]+\.md\s*\n|\Z)'
    matches = re.finditer(pattern, data, flags=re.DOTALL | re.IGNORECASE)

    os.makedirs(output_dir, exist_ok=True)

    counts: dict[str, int] = {}
    extracted_files: list[str] = []
    duplicate_info: list[str] = []

    for match in matches:
        filename = match.group(1).lower()
        content = match.group(2)

        header_index = content.find('#')
        if header_index == -1:
            # Skip sections with no header
            continue
        content = content[header_index:].strip() + '\n'

        base_name, ext = os.path.splitext(filename)
        count = counts.get(filename, 0)
        if count:
            new_filename = f"{base_name}_v{count+1}{ext}"
            duplicate_info.append(f"{filename} -> {new_filename}")
        else:
            new_filename = filename
        counts[filename] = count + 1

        file_path = os.path.join(output_dir, new_filename)
        with open(file_path, 'w', encoding='utf-8') as out_file:
            out_file.write(content)
        extracted_files.append(new_filename)
        print(f"Extracted {new_filename}")

    report_path = os.path.join(output_dir, 'report.txt')
    with open(report_path, 'w', encoding='utf-8') as report:
        report.write('Extracted files:\n')
        report.write('\n'.join(extracted_files))
        report.write(f"\n\nTotal files: {len(extracted_files)}\n")
        if duplicate_info:
            report.write('\nDuplicates handled:\n')
            report.write('\n'.join(duplicate_info))

    print(f"\nTotal extracted: {len(extracted_files)}")
    if duplicate_info:
        print(f"Duplicates: {len(duplicate_info)}")
    print(f"Report written to {report_path}")
    return len(extracted_files)


def main() -> None:
    parser = argparse.ArgumentParser(description='Extract .md files from a text file.')
    parser.add_argument('input_file', nargs='?', default='300religions.txt',
                        help='Path to the input text file.')
    parser.add_argument('-o', '--output', default='extracted_md_files',
                        help='Output directory for extracted markdown files.')
    args = parser.parse_args()

    extract_markdown(args.input_file, args.output)


if __name__ == '__main__':
    main()

# Usage example:
# python extract_md_files.py 300religions.txt -o extracted_md_files
