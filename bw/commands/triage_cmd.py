"""`bw triage` — classify an idea as plan-flow vs epic-flow."""

from pathlib import Path

import click

from bw.core.triage import render_triage_call

_CODE_EXTS = {".py", ".ts", ".tsx", ".js", ".jsx", ".go", ".rs", ".java", ".rb", ".kt", ".swift", ".cpp", ".c", ".cs", ".php"}
_SKIP_DIRS = {".git", ".bw", ".brv", "node_modules", ".venv", "venv", "__pycache__", "dist", "build"}


def _has_code_file(root: Path) -> bool:
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        # Skip any path inside a hidden/build directory
        if any(part in _SKIP_DIRS for part in path.relative_to(root).parts):
            continue
        if path.suffix in _CODE_EXTS:
            return True
    return False


def _detect_codebase() -> bool:
    """Return True if cwd looks like a real code repository.

    Heuristic: a `.git/` directory exists AND at least one source file with a
    known code extension is present outside common build/cache directories.
    """
    cwd = Path.cwd()
    if not (cwd / ".git").is_dir():
        return False
    return _has_code_file(cwd)


@click.command("triage")
@click.argument("idea")
@click.option(
    "--tool",
    required=True,
    type=click.Choice(["claude-code", "codex"]),
    help="Agent tool to spawn for (determines model config).",
)
def triage(idea: str, tool: str):
    """Classify an idea as plan-flow vs epic-flow.

    IDEA is a free-text description of what the user wants to build.
    Output is an Agent(...) call that the conductor copies verbatim.
    """
    has_codebase = _detect_codebase()
    output = render_triage_call(idea, tool, has_codebase)
    click.echo(output)
