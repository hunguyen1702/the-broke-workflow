"""Parse and update YAML frontmatter in markdown files."""

import re
from pathlib import Path

import yaml

_FM_RE = re.compile(r"\A---\n(.*?)\n---\n?(.*)", re.DOTALL)


def parse(text: str) -> tuple[dict, str]:
    """Return (metadata_dict, body_text). Empty dict if no frontmatter."""
    m = _FM_RE.match(text)
    if not m:
        return {}, text
    meta = yaml.safe_load(m.group(1)) or {}
    return meta, m.group(2)


def dump(meta: dict, body: str) -> str:
    """Serialize metadata + body back to frontmatter markdown."""
    fm = yaml.dump(meta, default_flow_style=False, sort_keys=False).rstrip("\n")
    return f"---\n{fm}\n---\n{body}"


def read_file(path: Path) -> tuple[dict, str]:
    """Read a markdown file and return (meta, body)."""
    return parse(path.read_text())


def write_file(path: Path, meta: dict, body: str) -> None:
    """Write metadata + body to a markdown file."""
    path.write_text(dump(meta, body))


def update_meta(path: Path, **updates) -> dict:
    """Update specific frontmatter keys in-place. Returns updated meta."""
    meta, body = read_file(path)
    meta.update(updates)
    write_file(path, meta, body)
    return meta
