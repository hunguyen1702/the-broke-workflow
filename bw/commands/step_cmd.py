"""bw step — CLI-driven step and agent instructions."""

import click

from bw.core.steps import (
    _get_flow,
    list_steps,
    render_agent,
    render_preamble,
    render_spawn_call,
    render_step,
)


def _resolve_step_num(step: str, flow: str = "plan") -> int:
    """Convert a step name (slug) or number to a step number.

    Accepts '2', 'discovery', 'DISCOVERY', 'write-plan', 'Write-Plan', etc.
    Raises ValueError for invalid numbers, KeyError for unknown names.
    """
    try:
        return int(step)
    except ValueError:
        pass
    # Try as step slug — uses _get_flow so invalid flow raises ValueError
    flow_cfg = _get_flow(flow)
    name_map = {meta["slug"]: num for num, meta in flow_cfg.step_meta.items()}
    key = step.lower()
    if key not in name_map:
        valid = ", ".join(sorted(m["slug"] for m in flow_cfg.step_meta.values()))
        raise KeyError(f"Unknown step: '{step}'. Valid: {valid}")
    return name_map[key]


@click.group()
def step():
    """Step instructions for the plan flow."""
    pass


_flow_option = click.option(
    "--flow",
    default="plan",
    type=click.Choice(["plan", "epic"]),
    help="Flow type (default: plan).",
)


@step.command("list")
@_flow_option
def step_list(flow: str):
    """List all steps in the flow."""
    steps = list_steps(flow)
    click.echo(" ".join(name.lower().replace(" ", "-") for _, name in steps))


@step.command("show")
@click.argument("step")
@click.argument("slug")
@_flow_option
def step_show(step: str, slug: str, flow: str):
    """Output conductor-level instructions for a step.

    STEP is the step number or step name (e.g. discovery, milestones).
    SLUG is the plan slug.
    """
    try:
        step_num = _resolve_step_num(step, flow)
    except (ValueError, KeyError) as e:
        click.echo(str(e), err=True)
        raise SystemExit(1)
    try:
        output = render_step(step_num, slug, flow=flow)
    except (FileNotFoundError, ValueError) as e:
        click.echo(str(e), err=True)
        raise SystemExit(1)
    click.echo(output)


@step.command("agent")
@click.argument("step")
@click.argument("slug")
@_flow_option
def step_agent(step: str, slug: str, flow: str):
    """Output sub-agent instructions for a step.

    The sub-agent runs this command itself to self-bootstrap.
    STEP is the step number or step name (e.g. discovery, milestones).
    SLUG is the plan slug.
    """
    try:
        step_num = _resolve_step_num(step, flow)
    except (ValueError, KeyError) as e:
        click.echo(str(e), err=True)
        raise SystemExit(1)
    try:
        output = render_agent(step_num, slug, flow=flow)
    except (FileNotFoundError, ValueError) as e:
        click.echo(str(e), err=True)
        raise SystemExit(1)
    click.echo(output)


@step.command("preamble")
@click.argument("slug")
@_flow_option
def step_preamble(slug: str, flow: str):
    """Output conductor preamble (rules and setup).

    SLUG is the plan slug.
    """
    try:
        output = render_preamble(slug, flow=flow)
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
@_flow_option
def step_spawn(step: str, slug: str, tool: str, flow: str):
    """Output the Agent tool call for spawning a sub-agent.

    STEP is the step number or step name (e.g. discovery, milestones).
    SLUG is the plan slug.
    """
    try:
        step_num = _resolve_step_num(step, flow)
    except (ValueError, KeyError) as e:
        click.echo(str(e), err=True)
        raise SystemExit(1)
    try:
        output = render_spawn_call(step_num, slug, tool, flow=flow)
    except (FileNotFoundError, ValueError) as e:
        click.echo(str(e), err=True)
        raise SystemExit(1)
    click.echo(output)
