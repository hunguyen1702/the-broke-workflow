"""bw product — product plan lifecycle commands."""

from datetime import date
from pathlib import Path

import click

from bw.core.frontmatter import read_file, update_meta
from bw.core.paths import find_bw_root, plan_dir, plans_dir
from bw.core.slug import slugify
from bw.core.templates import get_template

# Map short doc names to filenames
DOC_NAMES = {
    "requirements": "product-plan.md",
    "milestones": "milestones.md",
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
