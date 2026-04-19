"""bw worktree — manage git worktrees under .bw/worktrees/."""

import re
import shutil
import subprocess
from pathlib import Path

import click

from bw.core.paths import find_bw_root, worktrees_dir

_NAME_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")


def _git(*args: str, cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=cwd,
        capture_output=True,
        text=True,
    )


@click.group()
def worktree():
    """Manage git worktrees under .bw/worktrees/."""
    pass


@worktree.command("create")
@click.argument("name")
@click.option("--branch", "-b", default=None, help="Branch name (default: bw/<name>).")
@click.option("--base", default="HEAD", help="Base ref to branch from (default: HEAD).")
def worktree_create(name: str, branch: str | None, base: str):
    """Create a new worktree."""
    if not _NAME_RE.match(name):
        raise click.ClickException(
            f"Invalid name '{name}'. Use alphanumeric, hyphens, underscores, dots."
        )

    if shutil.which("git") is None:
        raise click.ClickException("git is not installed.")

    bw = find_bw_root()
    project_root = bw.parent
    wt_dir = worktrees_dir(bw)
    wt_path = wt_dir / name

    if wt_path.exists():
        raise click.ClickException(f"Worktree '{name}' already exists at {wt_path}")

    wt_dir.mkdir(exist_ok=True)

    branch_name = branch or f"bw/{name}"

    # Create the worktree
    result = _git(
        "worktree", "add", str(wt_path), "-b", branch_name, base,
        cwd=project_root,
    )
    if result.returncode != 0:
        raise click.ClickException(f"git worktree add failed:\n{result.stderr.strip()}")

    # Sparse-checkout to exclude .bw/ from the worktree
    result = _git("-C", str(wt_path), "sparse-checkout", "init", "--no-cone")
    if result.returncode != 0:
        raise click.ClickException(
            f"sparse-checkout init failed:\n{result.stderr.strip()}"
        )

    result = _git("-C", str(wt_path), "sparse-checkout", "set", "/*", "!/.bw")
    if result.returncode != 0:
        raise click.ClickException(
            f"sparse-checkout set failed:\n{result.stderr.strip()}"
        )

    click.echo(f"Created worktree '{name}' at {wt_path}")
    click.echo(f"  branch: {branch_name}")
    click.echo(f"  cd {wt_path}")


@worktree.command("list")
def worktree_list():
    """List worktrees managed by bw."""
    bw = find_bw_root()
    project_root = bw.parent
    wt_dir = worktrees_dir(bw)

    result = _git("worktree", "list", "--porcelain", cwd=project_root)
    if result.returncode != 0:
        raise click.ClickException(f"git worktree list failed:\n{result.stderr.strip()}")

    wt_prefix = str(wt_dir.resolve())
    entries = result.stdout.strip().split("\n\n")
    found = False

    for entry in entries:
        lines = entry.strip().splitlines()
        info = {}
        for line in lines:
            if line.startswith("worktree "):
                info["path"] = line[len("worktree "):]
            elif line.startswith("branch "):
                info["branch"] = line[len("branch "):]

        path = info.get("path", "")
        if not path.startswith(wt_prefix):
            continue

        found = True
        name = Path(path).name
        branch = info.get("branch", "").replace("refs/heads/", "")
        click.echo(f"  {name:20s} {branch:30s} {path}")

    if not found:
        click.echo("No worktrees.")


@worktree.command("remove")
@click.argument("name")
@click.option("--force", is_flag=True, help="Force removal even with uncommitted changes.")
def worktree_remove(name: str, force: bool):
    """Remove a worktree."""
    bw = find_bw_root()
    project_root = bw.parent
    wt_path = worktrees_dir(bw) / name

    if not wt_path.exists():
        raise click.ClickException(f"Worktree '{name}' not found at {wt_path}")

    # Check for uncommitted changes (dirty state)
    status_result = _git("status", "--porcelain", cwd=wt_path)
    if status_result.stdout.strip():
        lines = status_result.stdout.strip().splitlines()
        click.echo(f"Worktree '{name}' has uncommitted changes:")
        for line in lines:
            click.echo(f"  {line}")
        click.echo()
        click.echo("Use --force to remove the worktree and discard all changes.")
        raise SystemExit(1)

    args = ["worktree", "remove", str(wt_path)]
    if force:
        args.append("--force")

    result = _git(*args, cwd=project_root)
    if result.returncode != 0:
        raise click.ClickException(f"git worktree remove failed:\n{result.stderr.strip()}")

    click.echo(f"Removed worktree '{name}'.")
