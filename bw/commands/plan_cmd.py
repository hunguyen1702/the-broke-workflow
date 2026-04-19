"""bw plan — plan lifecycle commands."""

import json as json_mod
from collections import defaultdict
from datetime import date
from pathlib import Path

import click

from bw.core.frontmatter import read_file, update_meta
from bw.core.paths import find_bw_root, plan_dir, plans_dir
from bw.core.slug import slugify
from bw.core.task_store import scan_tasks
from bw.core.templates import get_template

# Map short doc names to filenames
DOC_NAMES = {
    "plan": "plan.md",
    "discovery": "discovery-report.md",
    "analysis": "analysis-report.md",
}


@click.group()
def plan():
    """Plan lifecycle commands."""
    pass


@plan.command("init")
@click.argument("title")
def plan_init(title: str):
    """Create a new plan from templates.

    TITLE is the feature name (e.g. "user authentication").
    """
    bw = find_bw_root()
    slug = slugify(title)
    pdir = plan_dir(bw, slug)

    if pdir.exists():
        click.echo(f"Plan directory already exists: {slug}", err=True)
        raise SystemExit(1)

    pdir.mkdir(parents=True)

    today = date.today().isoformat()

    # Copy and fill basic placeholders in templates
    for template_name, filename in [
        ("plan.md", "plan.md"),
        ("discovery-report.md", "discovery-report.md"),
        ("analysis-report.md", "analysis-report.md"),
    ]:
        content = get_template(template_name)
        content = content.replace("{slug}", slug)
        content = content.replace("{date}", today)
        content = content.replace("{title}", title)
        content = content.replace("{feature_name}", title)
        (pdir / filename).write_text(content)

    click.echo(f"Plan created: {slug}")
    click.echo(f"  .bw/plans/{slug}/")
    for f in sorted(pdir.iterdir()):
        click.echo(f"    {f.name}")


@plan.command("list")
def plan_list():
    """List all plans."""
    bw = find_bw_root()
    pdir = plans_dir(bw)
    if not pdir.exists():
        click.echo("No plans found.")
        return

    plans = sorted(d.name for d in pdir.iterdir() if d.is_dir())
    if not plans:
        click.echo("No plans found.")
        return

    for slug in plans:
        plan_file = pdir / slug / "plan.md"
        if plan_file.exists():
            meta, _ = read_file(plan_file)
            status = meta.get("status", "unknown")
            summary = meta.get("summary", "")
            click.echo(f"  {slug}  [{status}]  {summary}")
        else:
            click.echo(f"  {slug}  [no plan.md]")


@plan.command("docs")
@click.argument("slug")
def plan_docs(slug: str):
    """List documents in a plan."""
    bw = find_bw_root()
    pdir = plan_dir(bw, slug)
    if not pdir.exists():
        click.echo(f"Plan not found: {slug}", err=True)
        raise SystemExit(1)

    files = sorted(f.name for f in pdir.iterdir() if f.is_file())
    click.echo(f"Documents in {slug}:")
    for f in files:
        # Show friendly name if known
        friendly = next(
            (k for k, v in DOC_NAMES.items() if v == f), f
        )
        click.echo(f"  {friendly:20s} → {f}")


@plan.command("read")
@click.argument("slug")
@click.argument("doc")
def plan_read(slug: str, doc: str):
    """Print a plan document.

    DOC is one of: plan, discovery, analysis (or a filename).
    """
    bw = find_bw_root()
    filename = DOC_NAMES.get(doc, doc)
    filepath = plan_dir(bw, slug) / filename
    if not filepath.exists():
        click.echo(f"Document not found: {slug}/{filename}", err=True)
        raise SystemExit(1)

    click.echo(filepath.read_text())


@plan.command("finalize")
@click.argument("slug")
def plan_finalize(slug: str):
    """Freeze a plan — mark status as finalized."""
    bw = find_bw_root()
    plan_file = plan_dir(bw, slug) / "plan.md"
    if not plan_file.exists():
        click.echo(f"Plan not found: {slug}", err=True)
        raise SystemExit(1)

    meta, _ = read_file(plan_file)
    if meta.get("status") == "finalized":
        click.echo(f"Plan {slug} is already finalized.")
        return

    update_meta(plan_file, status="finalized", finalized=date.today().isoformat())

    # Create tasks directory for this plan
    tdir = find_bw_root() / "tasks" / slug
    tdir.mkdir(parents=True, exist_ok=True)

    click.echo(f"Plan {slug} finalized.")
    click.echo(f"  Task directory ready: .bw/tasks/{slug}/")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

_STATUS_ICON = {
    "done": "✓",
    "in_progress": "●",
    "ready": "◐",
    "blocked": "✗",
    "pending": "○",
}


def _progress_bar(done: int, total: int, width: int = 12) -> str:
    """Render [████░░░░] style progress bar."""
    if total == 0:
        return f"[{'░' * width}] 0/0"
    filled = round(done / total * width)
    bar = "█" * filled + "░" * (width - filled)
    return f"[{bar}] {done}/{total}"


# ---------------------------------------------------------------------------
# plan status — task progress for a single plan
# ---------------------------------------------------------------------------


@plan.command("status")
@click.argument("slug")
@click.option("--json", "as_json", is_flag=True, help="Output as JSON for agent use.")
@click.option("--details", is_flag=True, help="Show task list with status icons.")
def plan_status(slug: str, as_json: bool, details: bool):
    """Show plan status with task progress.

    SLUG is the plan slug.
    """
    bw = find_bw_root()
    plan_file = plan_dir(bw, slug) / "plan.md"
    if not plan_file.exists():
        click.echo(f"Plan not found: {slug}", err=True)
        raise SystemExit(1)

    meta, _ = read_file(plan_file)
    counts: dict[str, int] = defaultdict(int)
    task_list = []

    for _, tmeta in scan_tasks(plan_slug=slug):
        st = tmeta.get("status", "pending")
        counts[st] += 1
        task_list.append({
            "id": tmeta.get("id", f"{slug}/{tmeta['_path'].stem}"),
            "name": tmeta.get("title", tmeta["_path"].stem),
            "status": st,
            "owner": tmeta.get("owner") or None,
        })

    total = sum(counts.values())
    done = counts.get("done", 0)

    # --- JSON output ---
    if as_json:
        out = {
            "slug": slug,
            "status": meta.get("status", "unknown"),
            "summary": meta.get("summary", ""),
            "product": meta.get("product") or None,
            "milestone": meta.get("milestone") or None,
            "tasks": {"total": total, "done": done, **dict(counts)},
            "task_list": task_list,
        }
        click.echo(json_mod.dumps(out, indent=2))
        return

    # --- Human-readable output ---
    click.echo(f"Plan: {slug} [{meta.get('status', 'unknown')}]")
    summary = meta.get("summary", "")
    if summary:
        click.echo(f"Summary: {summary}")
    prod = meta.get("product")
    ms = meta.get("milestone")
    if prod:
        link = f"Product: {prod}"
        if ms:
            link += f" → Milestone {ms}"
        click.echo(link)
    click.echo()

    bar = _progress_bar(done, total)
    click.echo(f"  Tasks: {bar} done")
    if total > 0:
        parts = [f"{k}: {v}" for k, v in sorted(counts.items())]
        click.echo(f"    {', '.join(parts)}")

    if details and task_list:
        click.echo()
        for task in task_list:
            icon = _STATUS_ICON.get(task["status"], "?")
            owner = f" @{task['owner']}" if task.get("owner") else ""
            click.echo(f"    {icon} {task['id']} [{task['status']}]{owner}")
