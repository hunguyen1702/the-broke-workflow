<think>
The user wants me to produce a structured overview of this knowledge document about "Step CLI Commands" in what appears to be a CLI tool called "bw". Let me analyze the document and extract the key information.

Key points to extract:
1. The step command group provides CLI-driven step and agent instructions with subcommands: list, show, agent, preamble, spawn
2. step_spawn requires --tool flag (claude-code or codex) to determine model config
3. Step resolution accepts both numbers (1-6) and slugs (discovery, analysis, milestones, etc.)
4. Uses bw.core.steps module with functions like _get_flow, list_steps, render_agent, render_preamble, render_spawn_call, render_step
5. The command flow is: step command -> _resolve_step_num() -> render_* functions -> output
6. step spawn command outputs Agent() calls with model config
7. step show provides conductor-level instructions, step agent provides sub-agent instructions

Notable entities:
- bw/commands/step_cmd.py - the main file
- bw.core.steps module
- _resolve_step_num() function
- render_* functions
- --tool flag
- claude-code and codex as tool options

Let me structure this properly in markdown under 1500 tokens.
</think>

# Step CLI Commands

## Key Points

- **Step command group** provides CLI-driven step and agent instructions with five subcommands: `list`, `show`, `agent`, `preamble`, and `spawn`
- **step_spawn** requires a `--tool` flag (values: `claude-code` or `codex`) to determine the model configuration for Agent() calls
- **Step resolution** accepts both numeric indices (1-6) and slugs (`discovery`, `analysis`, `milestones`, etc.)
- **Command flow**: `step command` → `_resolve_step_num()` → `render_* functions` → output
- **step show** outputs conductor-level instructions, while **step agent** provides sub-agent instructions
- Uses **bw.core.steps** module with functions: `_get_flow`, `list_steps`, `render_agent`, `render_preamble`, `render_spawn_call`, `render_step`
- **step spawn** outputs Agent() calls with model config (newly added)

## Structure Summary

- **Reason**: Documenting bw step subcommands for plan flow execution
- **Files**: `bw/commands/step_cmd.py`
- **Dependencies**: `bw.core.steps` module
- **Subcommands**:
  - `list` — show all steps
  - `show` — conductor-level instructions
  - `agent` — sub-agent instructions
  - `preamble` — conductor rules/setup
  - `spawn` — Agent tool call with model config (outputs Agent() calls)

## Notable Entities

| Entity | Type | Description |
|--------|------|-------------|
| `bw/commands/step_cmd.py` | File | Main step command implementation |
| `bw.core.steps` | Module | Core steps functionality |
| `_resolve_step_num()` | Function | Resolves step input (numbers/slugs) to step data |
| `render_*` functions | Functions | Render different step outputs |
| `--tool` flag | Flag | Required for spawn; values: `claude-code`, `codex` |
| Step slugs | Values | `discovery`, `analysis`, `milestones`, etc. |