"""bw install — deploy adapters and commands to agent-coding tools."""

import shutil
from pathlib import Path

import click

from bw.core.paths import find_bw_root

# Source of truth for adapters is the repo's adapters/ dir
_ADAPTERS_DIR = Path(__file__).resolve().parent.parent.parent / "adapters"


@click.command("install")
@click.option("--tool", required=True, type=click.Choice(["claude-code", "codex"]))
@click.option(
    "--scope",
    required=True,
    type=click.Choice(["project", "global"]),
    help="'project' installs to .claude/ in current dir; 'global' to ~/.claude/",
)
def install(tool: str, scope: str):
    """Deploy bw adapters and commands to an agent-coding tool.

    Examples:
      bw install --tool claude-code --scope project
      bw install --tool claude-code --scope global
    """
    # Resolve destination
    if scope == "global":
        home = Path.home()
        if tool == "claude-code":
            dest = home / ".claude"
        elif tool == "codex":
            dest = home / ".codex"
        else:
            dest = home / f".{tool}"
    else:
        # project scope — ensure we're in a project
        bw = find_bw_root()
        if tool == "claude-code":
            dest = bw.parent / ".claude"
        elif tool == "codex":
            dest = bw.parent / ".codex"
        else:
            dest = bw.parent / f".{tool}"

    src_tool_dir = _ADAPTERS_DIR / tool
    if not src_tool_dir.is_dir():
        click.echo(f"No adapters found for tool: {tool}", err=True)
        raise SystemExit(1)

    dest.mkdir(parents=True, exist_ok=True)

    # Copy each adapter file
    for src in sorted(src_tool_dir.iterdir()):
        if src.is_file():
            dest_file = dest / src.name
            shutil.copy2(src, dest_file)
            click.echo(f"  {dest_file.relative_to(dest.parent if scope == 'project' else dest.parent)}")

    click.echo(f"\nInstalled {tool} adapters ({scope} scope) to {dest}")
    click.echo("  Note: Claude Code skills need to be placed in .claude/commands/")
    click.echo("  Move them manually if needed for your tool version.")
