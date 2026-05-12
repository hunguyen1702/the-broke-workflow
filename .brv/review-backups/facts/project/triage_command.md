---
title: Triage Command
summary: Triage command classifies ideas as plan-flow vs product-flow using 3-axis decision tree
tags: []
related: [facts/project/task_cli_commands.md, facts/project/cli_tool_integrations.md]
keywords: []
createdAt: '2026-05-11T17:09:38.174Z'
updatedAt: '2026-05-11T17:09:38.174Z'
---
## Reason
Documenting new triage flow-router command

## Raw Concept
**Task:**
Implement triage command as flow-router entrypoint

**Changes:**
- Added bw/core/triage.py with render_triage_call function
- Added bw/commands/triage_cmd.py with triage CLI command
- Added agents/triager.md with decision tree logic
- Extended AGENTS tuple with triager in config.py
- Added triager: haiku to default_config()
- Added read_agent_file helper in steps.py for cross-module agent file reads

**Files:**
- bw/core/triage.py
- bw/commands/triage_cmd.py
- agents/triager.md
- bw/core/config.py
- bw/core/steps.py
- bw/cli.py

**Flow:**
user idea -> triage command -> render Agent call -> conductor spawns triager -> decision card output

**Timestamp:** 2025-05-11

## Narrative
### Structure
Triage is an optional shortcut for users unsure whether to use plan flow (6-step, HOW-focused) or product flow (5-step, WHAT-focused). It does NOT init any folder — only prints an Agent(...) call.

### Dependencies
Uses resolve_model from config.py to get model for the tool; uses read_agent_file from steps.py to read triager.md template

### Highlights
Decision tree: A) Scope test (single vs multi), B) Knowledge test (clear vs unclear HOW), C) Value-stream test (multi-persona/subsystem/release-stage). Single feature + clear HOW -> PLAN. Multi-stream or >15 tasks -> PRODUCT.

### Rules
Rule 1: Triager outputs exactly one decision card with Recommendation, Why, Path, Next command, Alternative
Rule 2: Never recommend both flows with equal weight - pick one as primary
Rule 3: Default to PLAN if idea is too sparse to classify
Rule 4: CLI skips .bw, .brv, .git, node_modules, venv, dist, build directories when detecting codebase

### Examples
Example: "Add login" -> A:single -> B:unclear -> PLAN (analysis will be useful)
Example: "Build search platform with indexing, ranking, query API" -> A:multi -> C:multi-stream -> PRODUCT

## Facts
- **triage_command**: bw triage is a new command that classifies ideas as plan-flow or product-flow [project]
- **decision_tree**: Triage uses a 3-axis decision tree: scope test, knowledge test, value-stream test [project]
- **architecture_counts**: Architecture has 11 agents (added triager), 11 CLI commands (added triage), 11 core modules [project]
- **agents_tuple**: AGENTS tuple in config.py includes triager as the 11th agent [project]
- **triager_model**: Default config uses haiku model for triager under claude-code models [project]
- **codebase_detection**: CLI auto-detects has_codebase by checking .git dir + code files (py, ts, js, go, rs, etc.) [project]
- **codex_model_resolution**: Codex tool returns no model line when not configured in config [project]
- **resolve_model**: resolve_model returns None for missing config, which omits the model= line [project]
