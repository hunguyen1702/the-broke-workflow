"""Read step and agent files, render template variables, and output instructions."""

from pathlib import Path

from bw.core.frontmatter import read_file as read_frontmatter
from bw.core.paths import find_bw_root, plan_dir

# Resolve relative to this file: bw/core/steps.py -> ../../steps/
_STEPS_DIR = Path(__file__).resolve().parent.parent.parent / "steps"
_AGENTS_DIR = Path(__file__).resolve().parent.parent.parent / "agents"

STEP_META = {
    1: {"file": "step-01-requirements.md", "name": "Requirements", "slug": "requirements", "agent": None},
    2: {"file": "step-02-discovery.md", "name": "Discovery", "slug": "discovery", "agent": "discovery.md"},
    3: {"file": "step-03-analysis.md", "name": "Analysis", "slug": "analysis", "agent": "analysis.md"},
    4: {"file": "step-04-write-plan.md", "name": "Write Plan", "slug": "write-plan", "agent": "plan-writer.md"},
    5: {"file": "step-05-split-tasks.md", "name": "Split Tasks", "slug": "split-tasks", "agent": "splitter.md"},
    6: {"file": "step-06-review.md", "name": "Review", "slug": "review", "agent": None},
}

# Maps step number to agent name (used for config lookup)
STEP_AGENTS = {
    2: "discovery",
    3: "analysis",
    4: "plan-writer",
    5: "splitter",
    6: "reviewer",
}


def _steps_dir() -> Path:
    if not _STEPS_DIR.is_dir():
        raise FileNotFoundError(
            f"Steps directory not found at {_STEPS_DIR}. "
            "Ensure you're running from a proper bw installation."
        )
    return _STEPS_DIR


def _agents_dir() -> Path:
    if not _AGENTS_DIR.is_dir():
        raise FileNotFoundError(
            f"Agents directory not found at {_AGENTS_DIR}. "
            "Ensure you're running from a proper bw installation."
        )
    return _AGENTS_DIR


def _resolve_feature_name(slug: str) -> str:
    """Try to read feature name from plan frontmatter, fall back to slug."""
    try:
        bw = find_bw_root()
        plan_path = plan_dir(bw, slug) / "plan.md"
        if plan_path.exists():
            meta, _ = read_frontmatter(plan_path)
            return meta.get("summary", slug) or slug
    except FileNotFoundError:
        pass
    return slug


def _render_vars(content: str, slug: str, feature_name: str | None = None) -> str:
    """Replace template variables in content."""
    if feature_name is None:
        feature_name = _resolve_feature_name(slug)
    content = content.replace("{slug}", slug)
    content = content.replace("{feature_name}", feature_name)
    return content


def _validate_step(step_num: int) -> dict:
    if step_num not in STEP_META:
        raise ValueError(f"Invalid step number: {step_num}. Must be 1-6.")
    return STEP_META[step_num]


def list_steps() -> list[tuple[int, str]]:
    """Return list of (step_number, slug) tuples."""
    return [(num, meta["slug"]) for num, meta in sorted(STEP_META.items())]


def render_step(step_num: int, slug: str, feature_name: str | None = None) -> str:
    """Render conductor-level instructions for a step.

    Includes the pre-rendered sub-agent bootstrap command if this step
    has a sub-agent. Does NOT include the sub-agent's full instructions.
    """
    meta = _validate_step(step_num)
    step_path = _steps_dir() / meta["file"]
    content = step_path.read_text()
    content = _render_vars(content, slug, feature_name)

    # Append sub-agent spawn call if applicable
    if meta["agent"]:
        content += (
            "\n\n---\n\n"
            "## Spawn Sub-Agent\n\n"
            "Give the conductor this exact prompt to copy verbatim:\n\n"
            f"> `bw step spawn {step_num} {slug} --tool {{tool}}`\n"
        )

    # Append auto-proceed hint for next step
    next_step = step_num + 1
    if next_step in STEP_META:
        content += (
            f"\n\n## Next Step\n\n"
            f"Auto-proceed: run `bw step show {next_step} {slug}`\n"
        )

    return content


def render_agent(step_num: int, slug: str, feature_name: str | None = None) -> str:
    """Render sub-agent instructions for a step.

    The sub-agent runs this command itself to self-bootstrap.
    Raises ValueError if the step has no sub-agent.
    """
    meta = _validate_step(step_num)
    if not meta["agent"]:
        raise ValueError(
            f"Step {step_num} ({meta['name']}) has no sub-agent. "
            "The conductor handles this step directly."
        )
    agent_path = _agents_dir() / meta["agent"]
    content = agent_path.read_text()
    return _render_vars(content, slug, feature_name)


def render_spawn_call(
    step_num: int,
    slug: str,
    tool: str,
    feature_name: str | None = None,
) -> str:
    """Render the Agent tool call for spawning a sub-agent.

    Looks up the model from config for the given tool + step's agent.
    Returns the Agent(...) call that the conductor copies verbatim.
    Raises ValueError if the step has no sub-agent.
    """
    from bw.core.config import resolve_model

    meta = _validate_step(step_num)
    if not meta["agent"]:
        raise ValueError(
            f"Step {step_num} ({meta['name']}) has no sub-agent. "
            "The conductor handles this step directly."
        )

    agent_name = STEP_AGENTS[step_num]
    model = resolve_model(tool, agent_name)
    agent_md = _render_vars(
        (_agents_dir() / meta["agent"]).read_text(), slug, feature_name
    )

    header = f"## Spawn {agent_name.title()} Agent\n\n```\nAgent(\n  subagent_type=\"{agent_name}\","
    if model:
        body = f'\n  model="{model}",\n  prompt="""\n{agent_md}\n""",'
    else:
        body = f'\n  prompt=""""\n{agent_md}\n""",'
    footer = "\n)```"
    return header + body + footer


def render_preamble(slug: str, feature_name: str | None = None) -> str:
    """Render conductor preamble (rules and setup) from agents/conductor.md."""
    conductor_path = _agents_dir() / "conductor.md"
    content = conductor_path.read_text()
    return _render_vars(content, slug, feature_name)
