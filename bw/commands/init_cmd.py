"""bw init — scaffold .bw/ directory."""

from pathlib import Path

import click


@click.command("init")
def init():
    """Initialize a .bw/ project in the current directory."""
    bw = Path.cwd() / ".bw"
    if bw.exists():
        click.echo(".bw/ already exists. Nothing to do.")
        return

    # Create directory structure
    for d in ["plans", "tasks", "archive"]:
        (bw / d).mkdir(parents=True)

    # Config placeholder
    (bw / "config.yaml").write_text(
        "# bw configuration\n# See: https://github.com/user/the-broke-workflow\n"
    )

    # Gitignore worktrees and lock files
    gitignore = bw / ".gitignore"
    gitignore.write_text("worktrees/\n.locks/\n")

    click.echo("Initialized .bw/ project.")
    click.echo("  .bw/plans/    — plan documents")
    click.echo("  .bw/tasks/    — task files")
    click.echo("  .bw/archive/  — completed plans")
