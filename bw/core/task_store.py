"""Task file scanning and state management."""

from pathlib import Path
from typing import Iterator

from bw.core.frontmatter import read_file
from bw.core.paths import find_bw_root, plan_tasks_dir, tasks_dir


def scan_tasks(
    plan_slug: str | None = None,
    status_filter: str | None = None,
) -> Iterator[tuple[Path, dict]]:
    """Yield (filepath, meta) for tasks, optionally filtered.

    If plan_slug is given, only scan that plan's tasks.
    If status_filter is given, only yield tasks matching that status.
    """
    bw = find_bw_root()

    if plan_slug:
        # Scan a specific plan's task directory
        base = plan_tasks_dir(bw, plan_slug)
        if not base.is_dir():
            return
        for tf in base.glob("*.md"):
            if not tf.is_file():
                continue
            meta, _ = read_file(tf)
            tplan = plan_slug
            task_id = meta.get("id", f"{tplan}/{tf.stem}")
            meta["_path"] = tf
            meta["_plan_slug"] = tplan
            if status_filter is None or meta.get("status") == status_filter:
                yield tf, meta
    else:
        # Scan all plans
        base = tasks_dir(bw)
        if not base.is_dir():
            return
        for tdir in base.iterdir():
            if not tdir.is_dir():
                continue
            tplan = tdir.name
            for tf in tdir.glob("*.md"):
                meta, _ = read_file(tf)
                task_id = meta.get("id", f"{tplan}/{tf.stem}")
                meta["_path"] = tf
                meta["_plan_slug"] = tplan
                if status_filter is None or meta.get("status") == status_filter:
                    yield tf, meta


def get_task(task_id: str) -> tuple[Path, dict]:
    """Load a task by id (plan-slug/nnn-slug). Raises if not found."""
    bw = find_bw_root()
    parts = task_id.split("/", 1)
    if len(parts) != 2:
        raise ValueError(f"Invalid task id: {task_id} (expected plan/slug)")
    plan_slug, task_slug = parts
    tf = plan_tasks_dir(bw, plan_slug) / f"{task_slug}.md"
    if not tf.exists():
        raise FileNotFoundError(f"Task not found: {task_id}")
    meta, _ = read_file(tf)
    meta["_path"] = tf
    meta["_plan_slug"] = plan_slug
    return tf, meta


VALID_STATUSES = {"pending", "ready", "in_progress", "blocked", "done"}
STATUS_TRANSITIONS = {
    "pending": {"ready", "in_progress", "blocked"},
    "ready": {"in_progress", "pending"},
    "in_progress": {"done", "blocked", "pending"},
    "blocked": {"ready", "pending"},
    "done": set(),
}


def validate_transition(current: str, new: str) -> bool:
    """Check if a status transition is valid."""
    if current == new:
        return True
    return new in STATUS_TRANSITIONS.get(current, set())
