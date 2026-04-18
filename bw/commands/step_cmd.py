"""bw step — CLI-driven step and agent instructions."""

import click

from bw.core.steps import (
    STEP_META,
    list_steps,
    render_agent,
    render_preamble,
    render_spawn_call,
    render_step,
)


def _resolve_step_num(step: str) -> int:
    """Convert a step name (slug) or number to a step number.

    Accepts '2', 'discovery', 'DISCOVERY', 'write-plan', 'Write-Plan', etc.
    Raises ValueError for invalid numbers, KeyError for unknown names.
    """
    try:
        return int(step)
    except ValueError:
        pass
    # Try as step slug
    name_map = {meta["slug"]: num for num, meta in STEP_META.items()}
    key = step.lower()
    if key not in name_map:
        valid = ", ".join(sorted(m["slug"] for m in STEP_META.values()))
        raise KeyError(f"Unknown step: '{step}'. Valid: {valid}")
    return name_map[key]


@click.group()
def step():
    """Step instructions for the plan flow."""
    pass


@step.command("list")
def step_list():
    """List all steps in the plan flow."""
    steps = list_steps()
    click.echo(" ".join(name.lower().replace(" ", "-") for _, name in steps))


@step.command("show")
@click.argument("step")
@click.argument("slug")
def step_show(step: str, slug: str):
    """Output conductor-level instructions for a step.

    STEP is the step number (1-6) or step name (e.g. discovery, analysis).
    SLUG is the plan slug.
    """
    try:
        step_num = _resolve_step_num(step)
    except (ValueError, KeyError) as e:
        click.echo(str(e), err=True)
        raise SystemExit(1)
    try:
        output = render_step(step_num, slug)
    except (FileNotFoundError, ValueError) as e:
        click.echo(str(e), err=True)
        raise SystemExit(1)
    click.echo(output)


@step.command("agent")
@click.argument("step")
@click.argument("slug")
def step_agent(step: str, slug: str):
    """Output sub-agent instructions for a step.

    The sub-agent runs this command itself to self-bootstrap.
    STEP is the step number (1-6) or step name (e.g. discovery, analysis).
    SLUG is the plan slug.
    """
    try:
        step_num = _resolve_step_num(step)
    except (ValueError, KeyError) as e:
        click.echo(str(e), err=True)
        raise SystemExit(1)
    try:
        output = render_agent(step_num, slug)
    except (FileNotFoundError, ValueError) as e:
        click.echo(str(e), err=True)
        raise SystemExit(1)
    click.echo(output)


@step.command("preamble")
@click.argument("slug")
def step_preamble(slug: str):
    """Output conductor preamble (rules and setup).

    SLUG is the plan slug.
    """
    try:
        output = render_preamble(slug)
    except FileNotFoundError as e:
        click.echo(str(e), err=True)
        raise SystemExit(1)
    click.echo(output)


@step.command("spawn")
@click.argument("step")
@click.argument("slug")
@click.option(
    "--tool",
    required=True,
    type=click.Choice(["claude-code", "codex"]),
    help="Agent tool to spawn for (determines model config).",
)
def step_spawn(step: str, slug: str, tool: str):
    """Output the Agent tool call for spawning a sub-agent.

    STEP is the step number (1-6) or step name (e.g. discovery, analysis).
    SLUG is the plan slug.
    """
    try:
        step_num = _resolve_step_num(step)
    except (ValueError, KeyError) as e:
        click.echo(str(e), err=True)
        raise SystemExit(1)
    try:
        output = render_spawn_call(step_num, slug, tool)
    except (FileNotFoundError, ValueError) as e:
        click.echo(str(e), err=True)
        raise SystemExit(1)
    click.echo(output)
