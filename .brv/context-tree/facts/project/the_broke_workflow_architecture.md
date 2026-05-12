---
title: The Broke Workflow Architecture
summary: Python Click CLI for agent-coding with plan-flow (6-step) and epic-flow (5-step), triage routes to plan vs epic
tags: []
related: []
keywords: []
createdAt: '2026-04-18T04:19:02.579Z'
updatedAt: '2026-05-12T17:14:03.326Z'
---
## Reason
Update architecture to reflect current epic-based flow naming

## Raw Concept
**Task:**
Document the_broke_workflow architecture with current CLI commands and flows

**Changes:**
- Updated agents from 6 to 9 (added product-conductor, milestone-splitter, milestone-reviewer)
- Updated CLI commands from 6 to 9 (added product, step, worktree)
- Updated core modules from 6 to 9 (added config.py, steps.py)
- Added triage module (bw/core/triage.py)
- Added triage command
- Added triager agent
- Renamed product flow to epic flow
- Updated CLI commands from product to epic
- Triage now routes to plan-flow vs epic-flow (not PLAN vs PRODUCT)
- Removed product-conductor, added epic-conductor, milestone-splitter, milestone-reviewer

**Files:**
- bw/cli.py
- bw/commands/
- bw/core/
- agents/
- bw/core/triage.py
- bw/commands/triage_cmd.py
- agents/triager.md
- CLAUDE.md
- agents/epic-conductor.md

**Flow:**
triage (plan vs epic) -> requirements -> discovery/analysis -> plan/write/split -> review

**Timestamp:** 2026-05-12

## Narrative
### Structure
The broke workflow is a Python Click CLI with two flows: plan (6-step) for single features, epic (5-step) for multi-stream milestone planning. Triage classifies ideas as plan-flow or epic-flow.

### Dependencies
Requires Python >=3.10, click, pyyaml

### Highlights
CLI commands: bw plan init/read/finalize, bw epic init/read/finalize/plan/link, bw task list/next/claim, bw step show/spawn

## Facts
- **large_scope_flow**: The current large-scope flow is epic [convention]
- **triage_routing**: Triage routes to plan-flow vs epic-flow [convention]
- **cli_commands**: No bw product command exists [convention]
- **epic_flow_steps**: Epic flow has 5 steps: Requirements, Summary, Milestones, Review, Present [convention]
- **plan_flow_steps**: Plan flow has 6 steps: Requirements, Discovery, Analysis, Write Plan, Split Tasks, Review [convention]
- **work_hierarchy**: Canonical hierarchy is Epic -> Milestone -> Plan -> Task [convention]
