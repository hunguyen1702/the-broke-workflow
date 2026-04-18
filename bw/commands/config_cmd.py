"""bw config — show/edit bw configuration."""

import subprocess
from pathlib import Path

import click

from bw.core.paths import find_bw_root


@click.command("config")
def config():
    """Show (and optionally edit) bw configuration."""
    bw = find_bw_root()
    cfg = bw / "config.yaml"
    if not cfg.exists():
        click.echo("# No config.yaml found.")
        click.echo("# Create .bw/config.yaml to override defaults.")
        return

    click.echo(cfg.read_text())

    click.echo("\n# To edit: open .bw/config.yaml in your editor.")
