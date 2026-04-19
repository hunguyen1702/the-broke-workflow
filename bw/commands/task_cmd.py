"""bw task — task lifecycle commands."""

import subprocess
from datetime import datetime
from pathlib import Path

import click

from bw.core.frontmatter import read_file, write_file
from bw.core.lock import acquire, release
from bw.core.paths import find_bw_root, plan_dir, plan_tasks_dir
from bw.core.task_store import (
    VALID_STATUSES,
    add_comment,
    get_comments,
    get_task,
    scan_tasks,
    validate_transition,
)


@click.group()
def task():
    """Task lifecycle commands."""
    pass


@task.command("list")
@click.option("--plan", "plan_slug", help="Filter by plan slug")
@click.option("--status", "status_filter", help="Filter by status")
def task_list(plan_slug: str | None, status_filter: str | None):
    """List tasks, optionally filtered."""
    results = list(scan_tasks(plan_slug, status_filter))

    if not results:
        if plan_slug:
            click.echo(f"No tasks found for plan: {plan_slug}")
        elif status_filter:
            click.echo(f"No tasks with status: {status_filter}")
        else:
            click.echo("No tasks found.")
        return

    # Group by plan
    by_plan: dict[str, list] = {}
    for tf, meta in results:
        ps = meta["_plan_slug"]
        by_plan.setdefault(ps, []).append((tf, meta))

    for ps, items in by_plan.items():
        click.echo(f"{ps}/")
        for tf, meta in sorted(items, key=lambda x: x[0].stem):
            tid = f"{ps}/{tf.stem}"
            status = meta.get("status", "unknown")
            owner = meta.get("owner", "")
            effort = meta.get("effort", "?")
            blocked_by = meta.get("blocked_by", [])
            blocked_str = f" blocked_by:{','.join(str(b) for b in blocked_by)}" if blocked_by else ""
            owner_str = f" @{owner}" if owner else ""
            click.echo(
                f"  {tf.stem:40s} [{status:12s}] {effort}{blocked_str}{owner_str}"
            )


@task.command("next")
@click.option("--plan", "plan_slug", help="Only from this plan")
def task_next(plan_slug: str | None):
    """Show ready tasks (unblocked, unclaimed)."""
    bw = find_bw_root()

    for tf, meta in scan_tasks(plan_slug, status_filter=None):
        status = meta.get("status", "pending")
        owner = meta.get("owner")
        blocked_by = meta.get("blocked_by", [])

        # Only ready: status=ready, or pending with no blockers
        is_ready = status == "pending" and not blocked_by
        if not is_ready:
            continue

        ps = meta["_plan_slug"]
        tid = f"{ps}/{tf.stem}"

        if owner:
            continue  # claimed

        click.echo(f"{tid}: {meta.get('status','?')} effort:{meta.get('effort','?')}")


@task.command("show")
@click.argument("task_id")
def task_show(task_id: str):
    """Print a task file."""
    try:
        tf, meta = get_task(task_id)
    except (FileNotFoundError, ValueError) as e:
        click.echo(str(e), err=True)
        raise SystemExit(1)

    # Print full file content
    click.echo(tf.read_text())


@task.command("claim")
@click.argument("task_id")
@click.option("--owner", default="", help="Owner identifier (agent name, etc.)")
def task_claim(task_id: str, owner: str):
    """Atomically claim a task."""
    if not owner:
        owner = "unknown"

    try:
        tf, meta = get_task(task_id)
    except (FileNotFoundError, ValueError) as e:
        click.echo(str(e), err=True)
        raise SystemExit(1)

    current_owner = meta.get("owner", "")
    if current_owner:
        click.echo(f"Task already claimed by: {current_owner}")
        raise SystemExit(1)

    if not acquire(f"task:{task_id}", owner):
        click.echo(f"Could not acquire lock for {task_id}. Try again.")
        raise SystemExit(1)

    try:
        new_meta, body = read_file(tf)
        new_meta["owner"] = owner
        new_meta["claimed_at"] = datetime.now().isoformat()
        if new_meta.get("status") in ("pending", ""):
            new_meta["status"] = "in_progress"
        write_file(tf, new_meta, body)
    finally:
        release(f"task:{task_id}")

    click.echo(f"Claimed: {task_id} by {owner}")


@task.command("release")
@click.argument("task_id")
def task_release(task_id: str):
    """Drop claim on a task."""
    try:
        tf, meta = get_task(task_id)
    except (FileNotFoundError, ValueError) as e:
        click.echo(str(e), err=True)
        raise SystemExit(1)

    if not meta.get("owner"):
        click.echo(f"Task {task_id} is not claimed.")
        return

    new_meta, body = read_file(tf)
    new_meta["owner"] = ""
    new_meta["claimed_at"] = ""
    if new_meta.get("status") == "in_progress":
        new_meta["status"] = "pending"
    write_file(tf, new_meta, body)
    click.echo(f"Released: {task_id}")


@task.command("status")
@click.argument("task_id")
@click.argument("new_status")
def task_status(task_id: str, new_status: str):
    """Update a task's status."""
    if new_status not in VALID_STATUSES:
        click.echo(
            f"Invalid status: {new_status}. Valid: {', '.join(sorted(VALID_STATUSES))}",
            err=True,
        )
        raise SystemExit(1)

    try:
        tf, meta = get_task(task_id)
    except (FileNotFoundError, ValueError) as e:
        click.echo(str(e), err=True)
        raise SystemExit(1)

    current = meta.get("status", "pending")
    if not validate_transition(current, new_status):
        click.echo(
            f"Invalid transition: {current} -> {new_status}",
            err=True,
        )
        raise SystemExit(1)

    new_meta, body = read_file(tf)
    new_meta["status"] = new_status
    write_file(tf, new_meta, body)
    click.echo(f"{task_id}: {current} -> {new_status}")




@task.command("deps")
@click.argument("task_id")
def task_deps(task_id: str):
    """Show blockers and blocks for a task."""
    try:
        _, meta = get_task(task_id)
    except (FileNotFoundError, ValueError) as e:
        click.echo(str(e), err=True)
        raise SystemExit(1)

    blockers = meta.get("blocked_by", [])
    blocks = meta.get("blocks", [])

    click.echo(f"Task: {task_id}")
    if blockers:
        click.echo(f"  blocked_by: {', '.join(blockers)}")
    else:
        click.echo("  blocked_by: (none)")

    if blocks:
        click.echo(f"  blocks: {', '.join(blocks)}")
    else:
        click.echo("  blocks: (none)")


@task.command("dag")
@click.option("--plan", "plan_slug", help="Only show tasks from this plan")
def task_dag(plan_slug: str | None):
    """Render the task DAG as ASCII."""
    bw = find_bw_root()

    # Collect all tasks
    tasks: dict[str, dict] = {}
    for tf, meta in scan_tasks(plan_slug):
        tid = f"{meta['_plan_slug']}/{tf.stem}"
        tasks[tid] = {
            "status": meta.get("status", "unknown"),
            "blocked_by": meta.get("blocked_by", []),
            "blocks": meta.get("blocks", []),
            "owner": meta.get("owner", ""),
        }

    if not tasks:
        click.echo("No tasks.")
        return

    # Simple ASCII DAG: list tasks with their dependencies
    # Find roots (no blockers) and draw down
    done = set()
    for tid, info in tasks.items():
        if info["status"] == "done":
            done.add(tid)

    # Show blocked-by chain
    click.echo("Task DAG:")
    click.echo("=" * 60)
    for tid, info in sorted(tasks.items()):
        status = info["status"]
        owner = f" @{info['owner']}" if info["owner"] else ""
        blockers = info["blocked_by"]
        if blockers:
            click.echo(f"  {tid} [{status}]{owner}")
            for b in blockers:
                click.echo(f"    └─ {b}")
        else:
            click.echo(f"  {tid} [{status}]{owner}")


@task.command("add-dependency")
@click.argument("child_id")
@click.argument("parent_id")
def task_add_dependency(child_id: str, parent_id: str):
    """Add a dependency: child depends on parent (parent must complete first)."""
    try:
        tf, meta = get_task(child_id)
    except (FileNotFoundError, ValueError) as e:
        click.echo(str(e), err=True)
        raise SystemExit(1)

    new_meta, body = read_file(tf)
    blocked_by = new_meta.get("blocked_by", [])
    if parent_id not in blocked_by:
        blocked_by.append(parent_id)
        new_meta["blocked_by"] = blocked_by
        write_file(tf, new_meta, body)
        click.echo(f"Added: {child_id} blocked_by {parent_id}")
    else:
        click.echo(f"Already exists: {child_id} blocked_by {parent_id}")


@task.command("comment")
@click.argument("task_id")
@click.argument("text")
@click.option("--author", default="", help="Comment author (defaults to git user)")
def task_comment(task_id: str, text: str, author: str):
    """Add a comment to a task."""
    if not author:
        try:
            author = (
                subprocess.check_output(["git", "config", "user.name"], text=True)
                .strip()
            )
        except (subprocess.CalledProcessError, FileNotFoundError):
            click.echo("Warning: could not determine git user.name, using 'unknown'", err=True)
            author = "unknown"

    try:
        comment = add_comment(task_id, text, author)
        click.echo(f"Comment added to {task_id} by {comment['author']} at {comment['timestamp']}")
    except (FileNotFoundError, ValueError) as e:
        click.echo(str(e), err=True)
        raise SystemExit(1)
    except Exception as e:
        click.echo(f"Failed to add comment: {e}", err=True)
        raise SystemExit(1)


@task.command("comments")
@click.argument("task_id")
def task_comments(task_id: str):
    """List comments on a task."""
    try:
        comments = get_comments(task_id)
    except (FileNotFoundError, ValueError) as e:
        click.echo(str(e), err=True)
        raise SystemExit(1)

    if not comments:
        click.echo(f"No comments on {task_id}.")
        return

    for c in comments:
        click.echo(f"[{c['timestamp']}] {c['author']}: {c['text']}")


@task.command("remove")
@click.argument("task_id")
@click.option("--force", is_flag=True, help="Remove without confirmation.")
def task_remove(task_id: str, force: bool):
    """Remove a task file."""
    try:
        tf, _ = get_task(task_id)
    except (FileNotFoundError, ValueError) as e:
        click.echo(str(e), err=True)
        raise SystemExit(1)

    if not force:
        click.confirm(f"Remove task {task_id}?", abort=True)

    try:
        tf.unlink()
    except OSError as e:
        click.echo(f"Could not remove task file: {e}", err=True)
        raise SystemExit(1)

    click.echo(f"Removed: {task_id}")
