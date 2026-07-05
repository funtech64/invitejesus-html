#!/usr/bin/env python3
"""Phase 1: copy legacy content and migrate encyclopedia markdown."""

from __future__ import annotations

import re
import shutil
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC_MD = ROOT / "md_religions"
DEST_ENC = ROOT / "src" / "content" / "encyclopedia"
LEGACY_ROOT = ROOT / "legacy"
REPORT_PATH = ROOT / "MIGRATION_PHASE_1_REPORT.md"

LEGACY_DIRS = [
    ("md_religions", ROOT / "md_religions"),
    ("md_worldviews", ROOT / "md_worldviews"),
    ("data", ROOT / "data"),
    ("religions", ROOT / "religions"),
    ("assets", ROOT / "assets"),
    ("build", ROOT / "build"),
]

EMPTY_DIRS = [
    ROOT / "src" / "layouts",
    ROOT / "src" / "components",
    ROOT / "src" / "pages" / "encyclopedia",
    ROOT / "src" / "data",
    ROOT / "src" / "styles",
    ROOT / "scripts",
]

SKIP_NAMES = {"README.md", "report.txt"}
V2_SUFFIX = "_v2.md"
FILENAME_RE = re.compile(r"^[a-z0-9][a-z0-9-]*\.md$")


def is_v2(name: str) -> bool:
    return name.endswith(V2_SUFFIX)


def base_slug(name: str) -> str:
    if is_v2(name):
        return name[: -len(V2_SUFFIX)]
    return name[: -len(".md")]


def copy_tree(src: Path, dest: Path) -> None:
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(src, dest)


def ensure_dirs() -> None:
    DEST_ENC.mkdir(parents=True, exist_ok=True)
    for d in EMPTY_DIRS:
        d.mkdir(parents=True, exist_ok=True)
        gitkeep = d / ".gitkeep"
        if not gitkeep.exists():
            gitkeep.write_text("", encoding="utf-8")


def collect_source_files() -> tuple[list[Path], int]:
    md_files = sorted(SRC_MD.glob("*.md"))
    total_entries = len(list(SRC_MD.iterdir()))
    return md_files, total_entries


def choose_canonical(files: list[Path], total_dir_entries: int) -> tuple:
    """Return canonical map, v2_replacements, skipped, filename_problems, stats."""
    by_base: dict[str, dict[str, Path]] = defaultdict(dict)
    skipped: list[str] = []
    filename_problems: list[str] = []

    if (SRC_MD / "report.txt").exists():
        skipped.append("report.txt")

    for path in files:
        name = path.name
        if name in SKIP_NAMES:
            skipped.append(name)
            continue

        slug = base_slug(name)
        dest_name = f"{slug}.md"
        if not FILENAME_RE.match(dest_name):
            filename_problems.append(
                f"{name} → {dest_name} (invalid slug after normalization)"
            )

        if is_v2(name):
            by_base[slug]["v2"] = path
        else:
            by_base[slug]["base"] = path

    canonical: dict[str, Path] = {}
    v2_replacements: list[str] = []

    for slug in sorted(by_base.keys()):
        entry = by_base[slug]
        base_path = entry.get("base")
        v2_path = entry.get("v2")

        if v2_path and base_path:
            canonical[slug] = v2_path
            v2_replacements.append(f"{base_path.name} → {slug}.md (canonical: {v2_path.name})")
        elif v2_path:
            canonical[slug] = v2_path
            v2_replacements.append(f"(no base) → {slug}.md (canonical: {v2_path.name})")
        elif base_path:
            canonical[slug] = base_path
        else:
            filename_problems.append(f"{slug}: no source file resolved")

    base_only = sum(1 for slug in by_base if "base" in by_base[slug] and "v2" not in by_base[slug])
    v2_only = sum(1 for slug in by_base if "v2" in by_base[slug] and "base" not in by_base[slug])
    both = sum(1 for slug in by_base if "base" in by_base[slug] and "v2" in by_base[slug])

    stats = {
        "total_files_found": total_dir_entries,
        "markdown_files": len(files),
        "base_articles": base_only + both,
        "v2_articles": v2_only + both,
        "canonical_copied": len(canonical),
        "base_only": base_only,
        "v2_only": v2_only,
        "both_versions": both,
    }

    return canonical, v2_replacements, skipped, filename_problems, stats


def copy_canonical(canonical: dict[str, Path]) -> None:
    if DEST_ENC.exists():
        for child in DEST_ENC.iterdir():
            if child.is_file():
                child.unlink()
    DEST_ENC.mkdir(parents=True, exist_ok=True)

    for slug, src in sorted(canonical.items()):
        dest = DEST_ENC / f"{slug}.md"
        shutil.copy2(src, dest)


def write_report(
    stats: dict,
    v2_replacements: list[str],
    skipped: list[str],
    filename_problems: list[str],
) -> None:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        "# Migration Phase 1 Report",
        "",
        f"Generated: {now}",
        "",
        "## Summary",
        "",
        f"- **Total files found in `md_religions/`:** {stats['total_files_found']} (including `report.txt`)",
        f"- **Markdown files in `md_religions/`:** {stats['markdown_files']}",
        f"- **Total base articles** (`.md` without `_v2`, excluding skipped): {stats['base_articles']}",
        f"- **Total `_v2` articles:** {stats['v2_articles']}",
        f"- **Total canonical articles copied to `src/content/encyclopedia/`:** {stats['canonical_copied']}",
        "",
        "### Version breakdown",
        "",
        f"- Base only (no `_v2` sibling): {stats['base_only']}",
        f"- `_v2` only (no base sibling): {stats['v2_only']}",
        f"- Both base and `_v2` present: {stats['both_versions']}",
        "",
        "## `_v2` replaced base version",
        "",
    ]

    if v2_replacements:
        for item in v2_replacements:
            lines.append(f"- `{item}`")
    else:
        lines.append("- _(none)_")

    lines.extend(["", "## Skipped files", ""])
    if skipped:
        for item in skipped:
            lines.append(f"- `{item}`")
    else:
        lines.append("- _(none)_")

    # Also note base files superseded by v2 are not copied separately
    superseded = stats["both_versions"]
    if superseded:
        lines.extend(
            [
                "",
                f"Additionally, **{superseded}** base `.md` files were not copied separately because their `_v2` sibling was used as canonical.",
            ]
        )

    lines.extend(["", "## Filename problems", ""])
    if filename_problems:
        for item in filename_problems:
            lines.append(f"- {item}")
    else:
        lines.append("- _(none detected)_")

    lines.extend(
        [
            "",
            "## Legacy preservation",
            "",
            "The following source folders were **copied** (not moved) into `legacy/`:",
            "",
            "- `legacy/md_religions/`",
            "- `legacy/md_worldviews/`",
            "- `legacy/data/`",
            "- `legacy/religions/`",
            "- `legacy/assets/`",
            "- `legacy/build/`",
            "",
            "**Confirmation:** Original top-level folders (`md_religions/`, `md_worldviews/`, `data/`, `religions/`, `assets/`, `build/`) were left intact. No legacy content was deleted.",
            "",
            "## Not migrated in Phase 1",
            "",
            "- `md_worldviews/` — no article markdown files present (README only)",
            "- Argument position pages — not generated",
            "- Astro layouts, components, and page routes — folders created only",
            "",
            "## Destination",
            "",
            "Canonical encyclopedia articles: `src/content/encyclopedia/`",
            "",
        ]
    )

    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    ensure_dirs()

    for name, src in LEGACY_DIRS:
        if not src.exists():
            raise SystemExit(f"Missing source directory: {src}")
        copy_tree(src, LEGACY_ROOT / name)

    files, total_entries = collect_source_files()
    canonical, v2_replacements, skipped, filename_problems, stats = choose_canonical(
        files, total_entries
    )
    copy_canonical(canonical)
    write_report(stats, v2_replacements, skipped, filename_problems)

    print(f"Legacy copied to {LEGACY_ROOT}")
    print(f"Canonical articles copied: {stats['canonical_copied']}")
    print(f"Report written: {REPORT_PATH}")


if __name__ == "__main__":
    main()
