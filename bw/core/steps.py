"""Read step and agent files, render template variables, and output instructions."""

from pathlib import Path

from bw.core.frontmatter import read_file as read_frontmatter
from bw.core.paths import find_bw_root, plan_dir

# Resolve relative to this file: bw/core/steps.py -> ../../steps/
_STEPS_DIR = Path(__file__).resolve().parent.parent.parent / "steps"
_AGENTS_DIR = Path(__file__).resolve().parent.parent.parent / "agents"

STEP_META = {
    1: {"file": "step-01-requirements.md", "name": "Requirements", "agent": None},
    2: {"file": "step-02-discovery.md", "name": "Discovery", "agent": "discovery.md"},
    3: {"file": "step-03-analysis.md", "name": "Analysis", "agent": "analysis.md"},
    4: {"file": "step-04-write-plan.md", "name": "Write Plan", "agent": "plan-writer.md"},
    5: {"file": "step-05-split-tasks.md", "name": "Split Tasks", "agent": "splitter.md"},
    6: {"file": "step-06-review.md", "name": "Review", "agent": None},
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
    """Return list of (step_number, name) tuples."""
    return [(num, meta["name"]) for num, meta in sorted(STEP_META.items())]


def render_step(step_num: int, slug: str, feature_name: str | None = None) -> str:
    """Render conductor-level instructions for a step.

    Includes the pre-rendered sub-agent bootstrap command if this step
    has a sub-agent. Does NOT include the sub-agent's full instructions.
    """
    meta = _validate_step(step_num)
    step_path = _steps_dir() / meta["file"]
    content = step_path.read_text()
    content = _render_vars(content, slug, feature_name)

    # Append sub-agent bootstrap command if applicable
    if meta["agent"]:
        content += (
            "\n\n---\n\n"
            "## Spawn Sub-Agent\n\n"
            "Give the sub-agent this exact prompt:\n\n"
            f"> Run `bw step agent {step_num} {slug}` and follow the instructions.\n"
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


def render_preamble(slug: str, feature_name: str | None = None) -> str:
    """Render conductor preamble (rules and setup) from agents/conductor.md."""
    conductor_path = _agents_dir() / "conductor.md"
    content = conductor_path.read_text()
    return _render_vars(content, slug, feature_name)
