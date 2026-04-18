# Codex Adapters

**Status:** Deferred past MVP

The Codex adapter will mirror the Claude Code adapters but use Codex's `AGENTS.md` conventions instead of Claude Code's skill/command format.

## Planned Files

- `agents.md` — Codex agents config referencing `agents/` directory
- `commands/` — Equivalent command wrappers for Codex

## Implementation Notes

Codex uses `AGENTS.md` files in the project root to define agents and commands. The bw adapter for Codex should:

1. Define agents in `AGENTS.md` that reference the tool-agnostic prompts in `agents/`
2. Define commands that shell out to `bw` CLI
3. Deploy via `bw install --tool codex --scope project/global`

See `adapters/claude-code/` for the equivalent implementation to port.
