"""bw CLI — the broke workflow toolkit."""

import click

from bw.commands.config_cmd import config
from bw.commands.doctor_cmd import doctor
from bw.commands.init_cmd import init
from bw.commands.install_cmd import install
from bw.commands.plan_cmd import plan
from bw.commands.epic_cmd import epic
from bw.commands.step_cmd import step
from bw.commands.task_cmd import task
from bw.commands.triage_cmd import triage
from bw.commands.worktree_cmd import worktree


@click.group()
@click.version_option(version="0.1.0", prog_name="bw")
def main():
    """The Broke Workflow — agent-coding toolkit."""
    pass


main.add_command(config)
main.add_command(doctor)
main.add_command(init)
main.add_command(install)
main.add_command(plan)
main.add_command(epic)
main.add_command(step)
main.add_command(task)
main.add_command(triage)
main.add_command(worktree)


if __name__ == "__main__":
    main()
