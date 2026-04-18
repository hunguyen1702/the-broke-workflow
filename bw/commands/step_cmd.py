"""bw step — CLI-driven step and agent instructions."""

import click

from bw.core.steps import list_steps, render_agent, render_preamble, render_step


@click.group()
def step():
    """Step instructions for the plan flow."""
    pass


@step.command("list")
def step_list():
    """List all steps in the plan flow."""
    steps = list_steps()
    click.echo("Plan Flow Steps:\n")
    for num, name in steps:
        click.echo(f"  {num}. {name}")


@step.command("show")
@click.argument("step_num", type=click.IntRange(1, 6))
@click.argument("slug")
def step_show(step_num: int, slug: str):
    """Output conductor-level instructions for a step.

    STEP_NUM is the step number (1-6).
    SLUG is the plan slug.
    """
    try:
        output = render_step(step_num, slug)
    except (FileNotFoundError, ValueError) as e:
        click.echo(str(e), err=True)
        raise SystemExit(1)
    click.echo(output)


@step.command("agent")
@click.argument("step_num", type=click.IntRange(1, 6))
@click.argument("slug")
def step_agent(step_num: int, slug: str):
    """Output sub-agent instructions for a step.

    The sub-agent runs this command itself to self-bootstrap.
    STEP_NUM is the step number (1-6).
    SLUG is the plan slug.
    """
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
