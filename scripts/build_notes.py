#!/usr/bin/env python3
"""
Usage: python3 scripts/build_notes.py <meta.json>

Copy each til note to content/<path>, replacing its '# Title' heading with Zola frontmatter,
and give every category dir a transparent section index so its notes list under /notes.
"""
import json
import sys
from pathlib import Path

SITE_ROOT = Path(__file__).resolve().parent.parent
TIL_DIR = SITE_ROOT / "til"
CONTENT_DIR = SITE_ROOT / "content"


def frontmatter(note: dict[str, str]) -> str:
    return (
        "+++\n"
        f'title = "{note["title"]}"\n'
        f'date = {note["added"]}\n'
        f'updated = {note["updated"]}\n'
        "[taxonomies]\n"
        f'tags = ["{note["category"]}"]\n'
        "+++\n\n"
    )


def section_frontmatter(category: str) -> str:
    # transparent hands the category's notes up to /notes, so they all list at the top level
    return f'+++\ntitle = "{category}"\ntransparent = true\nsort_by = "date"\n+++\n'


def drop_title_heading(body: str) -> str:
    first_line, _, rest = body.lstrip().partition("\n")
    return rest.lstrip("\n") if first_line.startswith("# ") else body


def main() -> None:
    notes: list[dict[str, str]] = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))

    for category_dir in sorted({Path(note["path"]).parent for note in notes}):
        (CONTENT_DIR / category_dir).mkdir(parents=True, exist_ok=True)
        (CONTENT_DIR / category_dir / "_index.md").write_text(
            section_frontmatter(category_dir.name), encoding="utf-8"
        )

    for note in notes:
        body = (TIL_DIR / note["path"]).read_text(encoding="utf-8")
        target = CONTENT_DIR / note["path"]
        target.write_text(frontmatter(note) + drop_title_heading(body), encoding="utf-8")

    print(f"generated {len(notes)} notes")


if __name__ == "__main__":
    main()
