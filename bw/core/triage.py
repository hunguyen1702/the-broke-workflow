"""Render the Agent(...) call for the triager sub-agent.

Triage is a one-shot flow router. Unlike step spawn, it has no slug, no flow,
and no plan/epic context — only the raw user idea and a has_codebase flag.
"""

from bw.core.config import resolve_model
from bw.core.steps import read_agent_file


def render_triage_call(idea: str, tool: str, has_codebase: bool) -> str:
    """Render the Agent(...) call for spawning the triager sub-agent.

    Looks up the model from config for the given tool. Returns the
    Agent(...) call that the conductor copies verbatim.
    """
    agent_md = read_agent_file("triager.md")
    rendered = agent_md.replace("{idea}", idea).replace(
        "{has_codebase}", "true" if has_codebase else "false"
    )

    model = resolve_model(tool, "triager")

    header = '## Spawn Triager Agent\n\n```\nAgent(\n  subagent_type="triager",'
    model_line = f'\n  model="{model}",' if model else ""
    prompt_line = f'\n  prompt="""\n{rendered}\n""",'
    footer = "\n)```"
    return header + model_line + prompt_line + footer
