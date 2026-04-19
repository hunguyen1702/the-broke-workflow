---
title: Step CLI Commands
summary: bw step CLI with list, show, agent, preamble, and spawn subcommands
tags: []
keywords: []
importance: 56
recency: 1
maturity: draft
accessCount: 2
createdAt: '2026-04-19T05:27:29.258Z'
updatedAt: '2026-04-19T05:27:29.258Z'
---
## Reason
Documenting bw step subcommands for plan flow execution

## Raw Concept
**Task:**
Document the step command system in bw/commands/step_cmd.py

**Changes:**
- Added step spawn command that outputs Agent() calls with model config

**Files:**
- bw/commands/step_cmd.py

**Flow:**
step command -> _resolve_step_num() -> render_* functions -> output

## Narrative
### Structure
The step command group provides CLI-driven step and agent instructions. Subcommands: list (show all steps), show (conductor-level instructions), agent (sub-agent instructions), preamble (conductor rules/setup), spawn (Agent tool call with model config).

### Dependencies
Uses bw.core.steps module: _get_flow, list_steps, render_agent, render_preamble, render_spawn_call, render_step

### Highlights
step_spawn requires --tool flag (claude-code or codex) to determine model config. Step resolution accepts both numbers (1-6) and slugs (discovery, analysis, milestones, etc.).
