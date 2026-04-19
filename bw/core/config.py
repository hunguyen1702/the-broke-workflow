"""Read/write bw config and resolve model names per tool and agent."""

from pathlib import Path

import yaml

from bw.core.paths import find_bw_root

# Agent names that correspond to each step (must match STEP_META in steps.py)
AGENTS = (
    "conductor",
    "discovery",
    "analysis",
    "plan-writer",
    "splitter",
    "reviewer",
    "worker",
    "product-conductor",
    "milestone-splitter",
    "milestone-reviewer",
)


def _config_path() -> Path:
    bw = find_bw_root()
    return bw / "config.yaml"


def load_config() -> dict:
    """Return the full config dict from .bw/config.yaml, or empty dict."""
    try:
        cfg = _config_path()
    except FileNotFoundError:
        return {}
    if not cfg.exists():
        return {}
    return yaml.safe_load(cfg.read_text()) or {}


def save_config(data: dict) -> None:
    """Write a config dict to .bw/config.yaml."""
    cfg = _config_path()
    cfg.write_text(yaml.dump(data, default_flow_style=False, sort_keys=False))


def resolve_model(tool: str, agent: str) -> str | None:
    """Return the model name for a tool+agent, or None if not configured.

    Resolution order:
      1. models.<tool>.<agent>          — explicit override
      2. models.<tool>.default          — tool-level fallback
      3. (nothing)                      — return None (no override)
    """
    config = load_config()
    models = config.get("models", {})
    tool_config = models.get(tool, {})

    # Exact agent match
    if agent in tool_config and agent != "default":
        return tool_config[agent]

    # Default fallback
    if "default" in tool_config:
        return tool_config["default"]

    return None


def is_configured(tool: str) -> bool:
    """Return True if the tool has any model config."""
    config = load_config()
    return tool in config.get("models", {})


def default_config() -> dict:
    """Return a minimal starter config with Anthropic model names."""
    return {
        "models": {
            "claude-code": {
                "default": "opus",
                "conductor": "opus",
                "discovery": "sonnet",
                "analysis": "sonnet",
                "plan-writer": "sonnet",
                "splitter": "sonnet",
                "reviewer": "sonnet",
                "worker": "haiku",
                "product-conductor": "opus",
                "milestone-splitter": "sonnet",
                "milestone-reviewer": "sonnet",
            },
        },
    }
