---
title: Triage Flow
summary: Triage flow routes user ideas to PLAN or PRODUCT workflow via decision tree
tags: []
related: [facts/project/the_broke_workflow_architecture.md, facts/project/triage_command.md]
keywords: []
createdAt: '2026-05-12T14:52:16.820Z'
updatedAt: '2026-05-12T14:52:16.820Z'
---
## Reason
Document new triage flow (triage.py, triage_cmd.py, triager.md)

## Raw Concept
**Task:**
Document new triage flow for classifying user ideas

**Changes:**
- Added bw/core/triage.py - flow-router module with render_triage_call()
- Added bw/commands/triage_cmd.py - CLI command for triage
- Added agents/triager.md - triager sub-agent with decision tree

**Files:**
- bw/core/triage.py
- bw/commands/triage_cmd.py
- agents/triager.md

**Flow:**
user idea -> triage -> PLAN flow or PRODUCT flow

**Timestamp:** 2026-05-12

**Author:** the-broke-workflow

## Narrative
### Structure
Triage is a one-shot flow router. Unlike step spawn, it has no slug, no flow, and no plan/product context — only the raw user idea and a has_codebase flag. The triage command detects if running in a codebase (checks for .git + code files) and renders an Agent(...) call for the triager sub-agent.

### Dependencies
Uses bw.core.config.resolve_model for model lookup, bw.core.steps.read_agent_file for agent template

### Highlights
Decision tree: A (scope test) -> B (knowledge test for single) or C (value-stream test for multi). Signals: PLAN=fix,add,refactor; PRODUCT=MVP,launch,phase,platform. Output is Agent(...) call copied verbatim by conductor.

### Rules
Rule 1: One card only — no extra commentary
Rule 2: Ground the Why in signals from idea text
Rule 3: Never recommend both flows with equal weight
Rule 4: Default to PLAN if idea is too sparse

### Examples
Example 1: "Add login" → A:single → B:unclear → PLAN
Example 2: "Build search platform with indexing, ranking, query API" → A:multi → C:multi-stream → PRODUCT

## Facts
- **triage_flow_type**: Triage is a one-shot flow router [project]
- **triage_inputs**: Triage uses only idea and has_codebase flag as inputs [project]
- **codebase_detection**: has_codebase is true when .git dir exists AND code files present [project]
- **code_extensions**: Code extensions checked: .py, .ts, .tsx, .js, .jsx, .go, .rs, .java, .rb, .kt, .swift, .cpp, .c, .cs, .php [project]
- **skip_directories**: Skipped dirs: .git, .bw, .brv, node_modules, .venv, venv, __pycache__, dist, build [project]
