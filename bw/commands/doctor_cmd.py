"""bw doctor — health check for bw installation."""

import shutil
import sys
from pathlib import Path

import yaml

from bw.core import frontmatter, lock, paths, slug, task_store, templates

import click


@click.command("doctor")
def doctor():
    """Run health checks on the bw installation."""
    errors = 0

    def check(name: str, ok: bool, detail: str = ""):
        nonlocal errors
        prefix = "  PASS" if ok else "  FAIL"
        msg = f"{prefix}  {name}"
        if detail:
            msg += f": {detail}"
        click.echo(msg)
        if not ok:
            errors += 1

    click.echo("bw doctor — health check")
    click.echo("=" * 40)

    # Python version
    check("Python >= 3.10", sys.version_info >= (3, 10), sys.version)

    # Dependencies
    try:
        import click as _click
        check("click installed", True, _click.__version__)
    except ImportError:
        check("click installed", False)

    try:
        import yaml as _yaml
        check("pyyaml installed", True, _yaml.__version__)
    except ImportError:
        check("pyyaml installed", False)

    # Templates
    try:
        tdir = templates.templates_dir()
        check("templates/ found", tdir.is_dir(), str(tdir))
        for t in ["plan.md", "epic.md", "milestones.md", "task.md", "discovery-report.md", "analysis-report.md"]:
            check(f"  template: {t}", (tdir / t).exists())
    except FileNotFoundError as e:
        check("templates/ found", False, str(e))

    # bw root
    try:
        bw_root = paths.find_bw_root()
        check(".bw/ found", True, str(bw_root))
    except FileNotFoundError:
        check(".bw/ found", False, "Run `bw init` first")

    # Directories
    for d in ["plans", "tasks", "archive"]:
        try:
            bw_root = paths.find_bw_root()
            check(f"  .bw/{d}/", (bw_root / d).is_dir(), str(bw_root / d))
        except FileNotFoundError:
            check(f"  .bw/{d}/", False)

    # bw executable
    bw_path = shutil.which("bw")
    check("bw in PATH", bw_path is not None, bw_path or "not found")

    click.echo("=" * 40)
    if errors:
        click.echo(f"  {errors} issue(s) found.")
    else:
        click.echo("  All checks passed.")

    raise SystemExit(errors)
