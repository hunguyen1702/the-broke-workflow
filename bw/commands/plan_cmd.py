"""bw plan — plan lifecycle commands."""

from datetime import date
from pathlib import Path

import click

from bw.core.frontmatter import read_file, update_meta
from bw.core.paths import find_bw_root, plan_dir, plans_dir
from bw.core.slug import slugify
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
