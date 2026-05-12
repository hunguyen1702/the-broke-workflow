---
title: Triage Command
summary: bw triage classifies ideas as plan-flow or epic-flow, not PLAN vs PRODUCT
tags: []
related: [facts/project/task_cli_commands.md]
keywords: []
createdAt: '2026-05-11T17:09:38.174Z'
updatedAt: '2026-05-12T17:14:03.335Z'
---
## Reason
Update triage command to reflect plan-flow vs epic-flow routing

## Raw Concept
**Task:**
Document the triage command that classifies user ideas

**Changes:**
- Added bw/core/triage.py with render_triage_call function
- Added bw/commands/triage_cmd.py with triage CLI command
- Added agents/triager.md with decision tree logic
- Extended AGENTS tuple with triager in config.py
- Added triager: haiku to default_config()
- Added read_agent_file helper in steps.py for cross-module agent file reads
- Added triage command to CLI
- Added codebase detection via _detect_codebase()
- Updated routing from PLAN vs PRODUCT to plan-flow vs epic-flow
- Now uses has_codebase detection

**Files:**
- bw/core/triage.py
- bw/commands/triage_cmd.py
- agents/triager.md
- bw/core/config.py
- bw/core/steps.py
- bw/cli.py

**Flow:**
idea -> scope test -> knowledge/value-stream test -> recommendation

**Timestamp:** 2026-05-12

## Narrative
### Structure
Triage command takes user idea and classifies as plan-flow (single feature) or epic-flow (multi-stream). Uses decision tree: scope test, then knowledge test (for single) or value-stream test (for multi).

### Dependencies
Detects codebase presence via .git directory and code file extensions

### Highlights
Supports claude-code and codex tools. Outputs Agent(...) call with next command.

### Rules
Rule 1: --tool option required, must be claude-code or codex
Rule 2: Returns Agent(...) call for triager sub-agent

### Examples
Example: "Add login" -> A:single -> B:unclear -> PLAN (analysis will be useful)
Example: "Build search platform with indexing, ranking, query API" -> A:multi -> C:multi-stream -> PRODUCT

## Facts
- **triage_routing**: Triage routes to plan-flow vs epic-flow [convention]
- **decision_tree**: Triager agent uses decision tree: A (scope), B (knowledge), C (value-stream) [convention]
- **codebase_detection**: Codebase detection checks for .git directory and code files outside build/cache dirs [project]
