---
title: Triage Command
summary: bw triage command classifies ideas as PLAN vs PRODUCT flow
tags: []
related: [facts/project/task_cli_commands.md]
keywords: []
createdAt: '2026-05-11T17:09:38.174Z'
updatedAt: '2026-05-12T14:52:16.823Z'
---
## Reason
Update triage command with new files and codebase detection

## Raw Concept
**Task:**
Document bw triage command

**Changes:**
- Added bw/core/triage.py with render_triage_call function
- Added bw/commands/triage_cmd.py with triage CLI command
- Added agents/triager.md with decision tree logic
- Extended AGENTS tuple with triager in config.py
- Added triager: haiku to default_config()
- Added read_agent_file helper in steps.py for cross-module agent file reads
- Added triage command to CLI
- Added codebase detection via _detect_codebase()

**Files:**
- bw/core/triage.py
- bw/commands/triage_cmd.py
- agents/triager.md
- bw/core/config.py
- bw/core/steps.py
- bw/cli.py

**Flow:**
idea input -> detect codebase -> render triager agent call

**Timestamp:** 2026-05-12

## Narrative
### Structure
triage_cmd.py exposes `bw triage <idea> --tool <claude-codecodex>` CLI command. Uses click for CLI framework. The command renders Agent(...) call that conductor copies verbatim.

### Dependencies
Uses resolve_model from config.py to get model for the tool; uses read_agent_file from steps.py to read triager.md template

### Highlights
Codebase detection: .git/ directory must exist AND at least one source file outside build/cache dirs

### Rules
Rule 1: --tool option required, must be claude-code or codex
Rule 2: Returns Agent(...) call for triager sub-agent

### Examples
Example: "Add login" -> A:single -> B:unclear -> PLAN (analysis will be useful)
Example: "Build search platform with indexing, ranking, query API" -> A:multi -> C:multi-stream -> PRODUCT
