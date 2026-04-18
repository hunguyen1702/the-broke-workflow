"""Locate and copy template files."""

from pathlib import Path

# Templates ship alongside the package in the repo root templates/ dir.
# Resolve relative to this file: bw/core/templates.py -> ../../templates/
_TEMPLATES_DIR = Path(__file__).resolve().parent.parent.parent / "templates"


def templates_dir() -> Path:
    if not _TEMPLATES_DIR.is_dir():
        raise FileNotFoundError(
            f"Templates directory not found at {_TEMPLATES_DIR}. "
            "Ensure you're running from a proper bw installation."
        )
    return _TEMPLATES_DIR


def get_template(name: str) -> str:
    """Read a template file by name (e.g. 'plan.md')."""
    path = templates_dir() / name
    if not path.exists():
        raise FileNotFoundError(f"Template not found: {name}")
    return path.read_text()
