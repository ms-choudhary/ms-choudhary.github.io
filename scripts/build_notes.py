#!/usr/bin/env python3
"""
Usage: python3 scripts/build_notes.py <meta.json>

Copy each til note to content/<path>, replacing its '# Title' heading with Zola frontmatter,
and give every category dir a transparent section index so its notes list under /notes.

Cross-note links are turned into Zola internal links, which Zola resolves and validates:
    /notes/git/oh-shit-git.md  ->  @/notes/git/oh-shit-git.md
"""
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

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


def anchor_slug(text: str) -> str:
    """The notes writes anchors as prose; Zola's heading ids are slugified."""
    return re.sub(r"[^a-z0-9]+", "-", unquote(text).lower()).strip("-")


def link_to_internal(body: str) -> str:
    def to_internal(match: re.Match[str]) -> str:
        path, anchor = match.group(1), match.group(2)
        return f"](@{path}#{anchor_slug(anchor)}" if anchor else f"](@{path}"

    # an anchor may contain balanced parens, as in #KASLR%20(Kernel%20Address%20Space...)
    fragment = r"(?:[^()\s]|\([^()\s]*\))*"
    return re.sub(rf"\]\((/notes/[^)\s#]+\.md)(?:#({fragment}))?", to_internal, body)


def main() -> None:
    notes: list[dict[str, str]] = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))

    for category_dir in sorted({Path(note["path"]).parent for note in notes}):
        (CONTENT_DIR / category_dir).mkdir(parents=True, exist_ok=True)
        (CONTENT_DIR / category_dir / "_index.md").write_text(
            section_frontmatter(category_dir.name), encoding="utf-8"
        )

    for note in notes:
        body = (TIL_DIR / note["path"]).read_text(encoding="utf-8")
        body = link_to_internal(drop_title_heading(body))
        target = CONTENT_DIR / note["path"]
        target.write_text(frontmatter(note) + body, encoding="utf-8")

    print(f"generated {len(notes)} notes")


if __name__ == "__main__":
    main()
