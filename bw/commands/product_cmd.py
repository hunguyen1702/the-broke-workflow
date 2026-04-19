"""bw product — product plan lifecycle commands."""

import json as json_mod
import re
import shutil
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
    "requirements": "product-plan.md",
    "milestones": "milestones.md",
}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

_MILESTONE_RE = re.compile(r"^## Milestone (\d+):\s*(.+)", re.MULTILINE)
_GOAL_RE = re.compile(r"\*\*Goal:\*\*\s*(.+)")


def _parse_milestones(milestones_path: Path) -> list[dict]:
    """Parse milestone headings from milestones.md.

    Returns list of {"number": int, "name": str, "goal": str}.
    """
    text = milestones_path.read_text()
    # Split into sections by milestone heading
    parts = _MILESTONE_RE.split(text)
    # parts: [preamble, num1, name1, body1, num2, name2, body2, ...]
    milestones = []
    for i in range(1, len(parts), 3):
        number = int(parts[i])
        name = parts[i + 1].strip()
        body = parts[i + 2] if i + 2 < len(parts) else ""
        goal_m = _GOAL_RE.search(body)
        goal = goal_m.group(1).strip() if goal_m else ""
        milestones.append({"number": number, "name": name, "goal": goal})
    return milestones


def _find_linked_plans(product_slug: str) -> dict[int, list[dict]]:
    """Scan all plans to find those linked to a product.

    Returns {milestone_number: [{"slug": ..., "status": ..., ...}]}.
    """
    bw = find_bw_root()
    pdir = plans_dir(bw)
    if not pdir.exists():
        return {}

    by_milestone: dict[int, list[dict]] = defaultdict(list)
    for slug_dir in sorted(pdir.iterdir()):
        if not slug_dir.is_dir():
            continue
        plan_file = slug_dir / "plan.md"
        if not plan_file.exists():
            continue
        meta, _ = read_file(plan_file)
        if meta.get("product") != product_slug:
            continue
        ms = meta.get("milestone")
        if ms is None:
            continue
        by_milestone[int(ms)].append({
            "slug": slug_dir.name,
            "status": meta.get("status", "unknown"),
            "summary": meta.get("summary", ""),
        })
    return dict(by_milestone)


def _task_counts(plan_slug: str) -> tuple[dict[str, int], list[dict]]:
    """Count tasks by status for a plan. Returns (counts_dict, task_list)."""
    counts: dict[str, int] = defaultdict(int)
    task_list = []
    for _, meta in scan_tasks(plan_slug=plan_slug):
        st = meta.get("status", "pending")
        counts[st] += 1
        task_list.append({
            "id": meta.get("id", f"{plan_slug}/{meta['_path'].stem}"),
            "name": meta.get("title", meta["_path"].stem),
            "status": st,
            "owner": meta.get("owner") or None,
        })
    return dict(counts), task_list


def _progress_bar(done: int, total: int, width: int = 12) -> str:
    """Render [████░░░░] style progress bar."""
    if total == 0:
        return f"[{'░' * width}] 0/0"
    filled = round(done / total * width)
    bar = "█" * filled + "░" * (width - filled)
    return f"[{bar}] {done}/{total}"


_STATUS_ICON = {
    "done": "✓",
    "in_progress": "●",
    "pending": "○",
}


@click.group()
def product():
    """Product plan lifecycle commands."""
    pass


@product.command("init")
@click.argument("title")
def product_init(title: str):
    """Create a new product plan from templates.

    TITLE is the product name (e.g. "my awesome app").
    """
    bw = find_bw_root()
    slug = slugify(title)
    pdir = plan_dir(bw, slug)

    if pdir.exists():
        click.echo(f"Plan directory already exists: {slug}", err=True)
        raise SystemExit(1)

    pdir.mkdir(parents=True)

    today = date.today().isoformat()

    for template_name, filename in [
        ("product-plan.md", "product-plan.md"),
        ("milestones.md", "milestones.md"),
    ]:
        content = get_template(template_name)
        content = content.replace("{slug}", slug)
        content = content.replace("{date}", today)
        content = content.replace("{title}", title)
        content = content.replace("{feature_name}", title)
        (pdir / filename).write_text(content)

    click.echo(f"Product plan created: {slug}")
    click.echo(f"  .bw/plans/{slug}/")
    for f in sorted(pdir.iterdir()):
        click.echo(f"    {f.name}")


@product.command("list")
def product_list():
    """List all product plans."""
    bw = find_bw_root()
    pdir = plans_dir(bw)
    if not pdir.exists():
        click.echo("No plans found.")
        return

    found = False
    for slug_dir in sorted(pdir.iterdir()):
        if not slug_dir.is_dir():
            continue
        plan_file = slug_dir / "product-plan.md"
        if plan_file.exists():
            meta, _ = read_file(plan_file)
            status = meta.get("status", "unknown")
            summary = meta.get("summary", "")
            click.echo(f"  {slug_dir.name}  [{status}]  {summary}")
            found = True

    if not found:
        click.echo("No product plans found.")


@product.command("docs")
@click.argument("slug")
def product_docs(slug: str):
    """List documents in a product plan."""
    bw = find_bw_root()
    pdir = plan_dir(bw, slug)
    if not pdir.exists():
        click.echo(f"Plan not found: {slug}", err=True)
        raise SystemExit(1)

    files = sorted(f.name for f in pdir.iterdir() if f.is_file())
    click.echo(f"Documents in {slug}:")
    for f in files:
        friendly = next(
            (k for k, v in DOC_NAMES.items() if v == f), f
        )
        click.echo(f"  {friendly:20s} → {f}")


@product.command("read")
@click.argument("slug")
@click.argument("doc")
def product_read(slug: str, doc: str):
    """Print a product plan document.

    DOC is one of: requirements, milestones (or a filename).
    """
    bw = find_bw_root()
    filename = DOC_NAMES.get(doc, doc)
    filepath = plan_dir(bw, slug) / filename
    if not filepath.exists():
        click.echo(f"Document not found: {slug}/{filename}", err=True)
        raise SystemExit(1)

    try:
        click.echo(filepath.read_text())
    except OSError as e:
        click.echo(f"Could not read {slug}/{filename}: {e}", err=True)
        raise SystemExit(1)


@product.command("finalize")
@click.argument("slug")
def product_finalize(slug: str):
    """Freeze a product plan — mark status as finalized."""
    bw = find_bw_root()
    plan_file = plan_dir(bw, slug) / "product-plan.md"
    if not plan_file.exists():
        click.echo(f"Product plan not found: {slug}", err=True)
        raise SystemExit(1)

    meta, _ = read_file(plan_file)
    if meta.get("status") == "finalized":
        click.echo(f"Product plan {slug} is already finalized.")
        return

    try:
        update_meta(plan_file, status="finalized", finalized=date.today().isoformat())
    except OSError as e:
        click.echo(f"Could not finalize {slug}: {e}", err=True)
        raise SystemExit(1)

    click.echo(f"Product plan {slug} finalized.")


# ---------------------------------------------------------------------------
# product plan — create a plan linked to a milestone
# ---------------------------------------------------------------------------


@product.command("plan")
@click.argument("slug")
@click.argument("milestone_n", type=int)
def product_plan(slug: str, milestone_n: int):
    """Create a plan linked to a product milestone.

    SLUG is the product plan slug.
    MILESTONE_N is the milestone number (e.g. 1, 2, 3).
    """
    bw = find_bw_root()
    pdir = plan_dir(bw, slug)
    milestones_file = pdir / "milestones.md"

    if not pdir.exists():
        click.echo(f"Product plan not found: {slug}", err=True)
        raise SystemExit(1)
    if not milestones_file.exists():
        click.echo(f"No milestones.md found for {slug}", err=True)
        raise SystemExit(1)

    milestones = _parse_milestones(milestones_file)
    target = next((m for m in milestones if m["number"] == milestone_n), None)
    if not target:
        nums = ", ".join(str(m["number"]) for m in milestones)
        click.echo(
            f"Milestone {milestone_n} not found in {slug}. Available: {nums}",
            err=True,
        )
        raise SystemExit(1)

    # Create the plan
    plan_title = f"Milestone {milestone_n}: {target['name']}"
    plan_slug = slugify(target["name"])
    new_pdir = plan_dir(bw, plan_slug)

    if new_pdir.exists():
        click.echo(f"Plan directory already exists: {plan_slug}", err=True)
        raise SystemExit(1)

    new_pdir.mkdir(parents=True)
    today = date.today().isoformat()

    for template_name, filename in [
        ("plan.md", "plan.md"),
        ("discovery-report.md", "discovery-report.md"),
        ("analysis-report.md", "analysis-report.md"),
    ]:
        content = get_template(template_name)
        content = content.replace("{slug}", plan_slug)
        content = content.replace("{date}", today)
        content = content.replace("{title}", plan_title)
        content = content.replace("{feature_name}", plan_title)
        (new_pdir / filename).write_text(content)

    # Set product/milestone link and summary
    plan_file = new_pdir / "plan.md"
    summary = target["goal"] or target["name"]
    update_meta(plan_file, product=slug, milestone=milestone_n, summary=summary)

    click.echo(f"Plan created: {plan_slug}")
    click.echo(f"  Linked to: {slug} → Milestone {milestone_n}: {target['name']}")
    click.echo(f"  .bw/plans/{plan_slug}/")
    for f in sorted(new_pdir.iterdir()):
        click.echo(f"    {f.name}")


# ---------------------------------------------------------------------------
# product status — milestone rollup with progress
# ---------------------------------------------------------------------------


@product.command("status")
@click.argument("slug")
@click.option("--json", "as_json", is_flag=True, help="Output as JSON for agent use.")
@click.option("--details", is_flag=True, help="Show full hierarchy with task names.")
def product_status(slug: str, as_json: bool, details: bool):
    """Show product status with milestone progress.

    SLUG is the product plan slug.
    """
    bw = find_bw_root()
    pdir = plan_dir(bw, slug)
    product_file = pdir / "product-plan.md"
    milestones_file = pdir / "milestones.md"

    if not product_file.exists():
        click.echo(f"Product plan not found: {slug}", err=True)
        raise SystemExit(1)

    prod_meta, _ = read_file(product_file)
    milestones = _parse_milestones(milestones_file) if milestones_file.exists() else []
    linked = _find_linked_plans(slug)

    # Build data structure
    total_tasks = 0
    total_done = 0
    milestones_started = 0
    milestone_data = []

    for ms in milestones:
        plans_for_ms = linked.get(ms["number"], [])
        ms_entry: dict = {
            "number": ms["number"],
            "name": ms["name"],
            "goal": ms["goal"],
            "plans": [],
        }

        if plans_for_ms:
            milestones_started += 1

        for p in plans_for_ms:
            counts, task_list = _task_counts(p["slug"])
            t = sum(counts.values())
            d = counts.get("done", 0)
            total_tasks += t
            total_done += d
            ms_entry["plans"].append({
                "slug": p["slug"],
                "status": p["status"],
                "tasks": {"total": t, "done": d, **counts},
                "task_list": task_list,
            })

        milestone_data.append(ms_entry)

    # --- JSON output ---
    if as_json:
        out = {
            "slug": slug,
            "status": prod_meta.get("status", "unknown"),
            "summary": prod_meta.get("summary", ""),
            "milestones": milestone_data,
            "totals": {
                "tasks": total_tasks,
                "done": total_done,
                "milestones": len(milestones),
                "milestones_started": milestones_started,
            },
        }
        click.echo(json_mod.dumps(out, indent=2))
        return

    # --- Human-readable output ---
    status = prod_meta.get("status", "unknown")
    click.echo(f"Product: {slug} [{status}]")
    summary = prod_meta.get("summary", "")
    if summary:
        click.echo(f"Summary: {summary}")
    click.echo()

    for ms in milestone_data:
        plans_for_ms = ms["plans"]
        if not plans_for_ms:
            click.echo(f"  Milestone {ms['number']}: {ms['name']}  ○ no plan yet")
            continue

        if details:
            click.echo(f"  Milestone {ms['number']}: {ms['name']}")

        for p in plans_for_ms:
            t = p["tasks"].get("total", 0)
            d = p["tasks"].get("done", 0)
            bar = _progress_bar(d, t)

            if details:
                click.echo(f"    Plan: {p['slug']} [{p['status']}]")
                for task in p["task_list"]:
                    icon = _STATUS_ICON.get(task["status"], "?")
                    owner = f" @{task['owner']}" if task.get("owner") else ""
                    click.echo(f"      {icon} {task['id']} [{task['status']}]{owner}")
            else:
                click.echo(
                    f"  Milestone {ms['number']}: {ms['name']}  {bar}"
                )
                click.echo(f"    Plan: {p['slug']}  {d}/{t} tasks done")

    click.echo()
    bar = _progress_bar(total_done, total_tasks)
    click.echo(
        f"  Overall: {bar} ({milestones_started}/{len(milestones)} milestones started)"
    )


@product.command("link")
@click.argument("plan_slug")
@click.argument("product_slug")
@click.argument("milestone_n", type=int)
def product_link(plan_slug: str, product_slug: str, milestone_n: int):
    """Link an existing plan to a product milestone.

    PLAN_SLUG is the plan to link.
    PRODUCT_SLUG is the product plan slug.
    MILESTONE_N is the milestone number to link to (e.g. 1, 2, 3).
    """
    bw = find_bw_root()

    # Validate product exists
    pdir = plan_dir(bw, product_slug)
    product_file = pdir / "product-plan.md"
    milestones_file = pdir / "milestones.md"
    if not product_file.exists():
        click.echo(f"Product plan not found: {product_slug}", err=True)
        raise SystemExit(1)

    # Validate milestone exists
    if not milestones_file.exists():
        click.echo(f"No milestones.md found for {product_slug}", err=True)
        raise SystemExit(1)

    milestones = _parse_milestones(milestones_file)
    target = next((m for m in milestones if m["number"] == milestone_n), None)
    if not target:
        nums = ", ".join(str(m["number"]) for m in milestones)
        click.echo(
            f"Milestone {milestone_n} not found in {product_slug}. Available: {nums}",
            err=True,
        )
        raise SystemExit(1)

    # Validate plan exists
    plan_dir_path = plan_dir(bw, plan_slug)
    plan_file = plan_dir_path / "plan.md"
    if not plan_file.exists():
        click.echo(f"Plan not found: {plan_slug}", err=True)
        raise SystemExit(1)

    # Write the link
    summary = target["goal"] or target["name"]
    update_meta(plan_file, product=product_slug, milestone=milestone_n, summary=summary)

    click.echo(f"Plan '{plan_slug}' linked to {product_slug} → Milestone {milestone_n}: {target['name']}")


@product.command("remove")
@click.argument("slug")
@click.option("--force", is_flag=True, help="Remove product plan and all linked plans.")
def product_remove(slug: str, force: bool):
    """Remove a product plan and all linked plans."""
    bw = find_bw_root()
    pdir = plan_dir(bw, slug)
    product_file = pdir / "product-plan.md"

    if not product_file.exists():
        click.echo(f"Product plan not found: {slug}", err=True)
        raise SystemExit(1)

    # Check for linked plans (dependencies)
    by_milestone = _find_linked_plans(slug)
    if by_milestone:
        click.echo(f"Product plan '{slug}' is linked to plans:")
        click.echo()
        for ms_num in sorted(by_milestone):
            plans = by_milestone[ms_num]
            click.echo(f"  Milestone {ms_num} ({len(plans)} plan(s)):")
            for p in plans:
                click.echo(f"    - {p['slug']} [{p['status']}]")
        click.echo()
        click.echo("Use --force to remove the product and all linked plans.")
        raise SystemExit(1)

    try:
        shutil.rmtree(pdir)
    except OSError as e:
        click.echo(f"Could not remove product directory: {e}", err=True)
        raise SystemExit(1)

    click.echo(f"Removed product plan: {slug}")
