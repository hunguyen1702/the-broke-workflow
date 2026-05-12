"""Read step and agent files, render template variables, and output instructions."""

from pathlib import Path
from typing import NamedTuple

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

EPIC_STEP_META = {
    1: {"file": "epic-step-01-requirements.md", "name": "Requirements", "slug": "requirements", "agent": None},
    2: {"file": "epic-step-02-summary.md", "name": "Summary", "slug": "summary", "agent": None},
    3: {"file": "epic-step-03-milestones.md", "name": "Milestones", "slug": "milestones", "agent": "milestone-splitter.md"},
    4: {"file": "epic-step-04-review.md", "name": "Review", "slug": "review", "agent": "milestone-reviewer.md"},
    5: {"file": "epic-step-05-present.md", "name": "Present", "slug": "present", "agent": None},
}

EPIC_STEP_AGENTS = {
    3: "milestone-splitter",
    4: "milestone-reviewer",
}


class FlowConfig(NamedTuple):
    """Configuration for a workflow flow."""

    step_meta: dict
    step_agents: dict
    conductor_file: str
    plan_doc: str


FLOW_META = {
    "plan": FlowConfig(STEP_META, STEP_AGENTS, "conductor.md", "plan.md"),
    "epic": FlowConfig(EPIC_STEP_META, EPIC_STEP_AGENTS, "epic-conductor.md", "epic.md"),
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


def read_agent_file(name: str) -> str:
    """Read raw agent markdown by filename (e.g. 'triager.md').

    Used by callers outside the step flow (e.g. triage) that need agent
    content without going through STEP_META.
    """
    return (_agents_dir() / name).read_text()


def _get_flow(flow: str) -> FlowConfig:
    """Return FlowConfig for the given flow. Raises ValueError if unknown."""
    if flow not in FLOW_META:
        raise ValueError(f"Unknown flow: '{flow}'. Valid: {', '.join(FLOW_META)}")
    return FLOW_META[flow]


def _require_agent(step_num: int, meta: dict) -> None:
    """Raise ValueError if the step has no sub-agent."""
    if not meta["agent"]:
        raise ValueError(
            f"Step {step_num} ({meta['name']}) has no sub-agent. "
            "The conductor handles this step directly."
        )


def _resolve_feature_name(slug: str, flow: str = "plan") -> str:
    """Try to read feature name from plan frontmatter, fall back to slug."""
    # find_bw_root failure is fatal — user is outside a bw project
    bw = find_bw_root()
    flow_cfg = _get_flow(flow)
    plan_path = plan_dir(bw, slug) / flow_cfg.plan_doc
    if plan_path.exists():
        meta, _ = read_frontmatter(plan_path)
        return meta.get("summary", slug) or slug
    return slug


def _render_vars(
    content: str,
    slug: str,
    feature_name: str | None = None,
    flow: str = "plan",
) -> str:
    """Replace template variables in content."""
    if feature_name is None:
        feature_name = _resolve_feature_name(slug, flow)
    content = content.replace("{slug}", slug)
    content = content.replace("{feature_name}", feature_name)
    return content


def _validate_step(step_num: int, flow: str = "plan") -> tuple[dict, FlowConfig]:
    """Return (step_meta_dict, flow_cfg) for the step number."""
    flow_cfg = _get_flow(flow)
    step_meta = flow_cfg.step_meta
    max_step = max(step_meta)
    if step_num not in step_meta:
        raise ValueError(f"Invalid step number: {step_num}. Must be 1-{max_step}.")
    return step_meta, flow_cfg


def list_steps(flow: str = "plan") -> list[tuple[int, str]]:
    """Return list of (step_number, slug) tuples."""
    flow_cfg = _get_flow(flow)
    return [(num, meta["slug"]) for num, meta in sorted(flow_cfg.step_meta.items())]


def render_step(
    step_num: int,
    slug: str,
    feature_name: str | None = None,
    flow: str = "plan",
) -> str:
    """Render conductor-level instructions for a step.

    Includes the pre-rendered sub-agent bootstrap command if this step
    has a sub-agent. Does NOT include the sub-agent's full instructions.
    """
    step_meta, flow_cfg = _validate_step(step_num, flow)
    meta = step_meta[step_num]
    step_path = _steps_dir() / meta["file"]
    content = step_path.read_text()
    content = _render_vars(content, slug, feature_name, flow)

    # Append sub-agent spawn call if applicable
    flow_flag = f" --flow {flow}" if flow != "plan" else ""
    if meta["agent"]:
        content += (
            "\n\n---\n\n"
            "## Spawn Sub-Agent\n\n"
            "Give the conductor this exact prompt to copy verbatim:\n\n"
            f"> `bw step spawn {step_num} {slug} --tool {{tool}}{flow_flag}`\n"
        )

    # Append auto-proceed hint for next step
    next_step = step_num + 1
    if next_step in step_meta:
        content += (
            f"\n\n## Next Step\n\n"
            f"Auto-proceed: run `bw step show {next_step} {slug}{flow_flag}`\n"
        )

    return content


def render_agent(
    step_num: int,
    slug: str,
    feature_name: str | None = None,
    flow: str = "plan",
) -> str:
    """Render sub-agent instructions for a step.

    The sub-agent runs this command itself to self-bootstrap.
    Raises ValueError if the step has no sub-agent.
    """
    step_meta, flow_cfg = _validate_step(step_num, flow)
    meta = step_meta[step_num]
    _require_agent(step_num, meta)
    agent_path = _agents_dir() / meta["agent"]
    content = agent_path.read_text()
    return _render_vars(content, slug, feature_name, flow)


def render_spawn_call(
    step_num: int,
    slug: str,
    tool: str,
    feature_name: str | None = None,
    flow: str = "plan",
) -> str:
    """Render the Agent tool call for spawning a sub-agent.

    Looks up the model from config for the given tool + step's agent.
    Returns the Agent(...) call that the conductor copies verbatim.
    Raises ValueError if the step has no sub-agent.
    """
    from bw.core.config import resolve_model

    step_meta, flow_cfg = _validate_step(step_num, flow)
    meta = step_meta[step_num]
    _require_agent(step_num, meta)

    agent_name = flow_cfg.step_agents[step_num]
    model = resolve_model(tool, agent_name)
    agent_md = _render_vars(
        (_agents_dir() / meta["agent"]).read_text(), slug, feature_name, flow
    )

    header = f"## Spawn {agent_name.title()} Agent\n\n```\nAgent(\n  subagent_type=\"{agent_name}\","
    if model:
        body = f'\n  model="{model}",\n  prompt="""\n{agent_md}\n""",'
    else:
        body = f'\n  prompt=""""\n{agent_md}\n""",'
    footer = "\n)```"
    return header + body + footer


def render_preamble(
    slug: str,
    feature_name: str | None = None,
    flow: str = "plan",
) -> str:
    """Render conductor preamble (rules and setup)."""
    flow_cfg = _get_flow(flow)
    conductor_path = _agents_dir() / flow_cfg.conductor_file
    content = conductor_path.read_text()
    return _render_vars(content, slug, feature_name, flow)
