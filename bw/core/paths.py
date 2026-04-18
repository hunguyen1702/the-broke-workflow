"""Resolve .bw/ directory and artifact paths."""

from pathlib import Path


def find_bw_root(start: Path | None = None) -> Path:
    """Walk up from start (default cwd) to find a directory containing .bw/."""
    current = (start or Path.cwd()).resolve()
    while True:
        candidate = current / ".bw"
        if candidate.is_dir():
            return candidate
        if current.parent == current:
            raise FileNotFoundError(
                "Not inside a bw project. Run `bw init` first."
            )
        current = current.parent


def plans_dir(bw: Path) -> Path:
    return bw / "plans"


def tasks_dir(bw: Path) -> Path:
    return bw / "tasks"


def archive_dir(bw: Path) -> Path:
    return bw / "archive"


def plan_dir(bw: Path, slug: str) -> Path:
    return plans_dir(bw) / slug


def plan_tasks_dir(bw: Path, slug: str) -> Path:
    return tasks_dir(bw) / slug
