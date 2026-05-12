---
title: Epic Flow Architecture
summary: '5-step milestone planning flow: Requirements -> Summary -> Milestones -> Review -> Present'
tags: []
related: [facts/project/triage_command.md, facts/project/triager_agent.md]
keywords: []
createdAt: '2026-05-12T16:20:32.312Z'
updatedAt: '2026-05-12T17:14:03.342Z'
---
## Reason
Create/update epic flow architecture replacing old product flow

## Raw Concept
**Task:**
Document the epic flow architecture for multi-stream milestone planning

**Changes:**
- Hard-renamed product flow to epic flow
- Canonical hierarchy: Epic -> Milestone -> Plan -> Task
- CLI command: bw epic
- Step flow: --flow epic
- Implementation plan frontmatter: epic: and milestone: fields
- Epic documents: .bw/plans/<slug>/epic.md and milestones.md
- Model config key: epic-conductor
- Removed bw product command and --flow product support
- Renamed from product_flow_architecture to epic_flow_architecture
- Updated terminology from product to epic throughout

**Files:**
- bw/cli.py
- bw/commands/epic_cmd.py
- bw/commands/plan_cmd.py
- bw/core/steps.py
- bw/commands/step_cmd.py
- templates/epic.md
- templates/plan.md
- tests/test_epic_flow.py
- agents/epic-conductor.md
- CLAUDE.md

**Flow:**
requirements -> summary -> milestones -> review -> present -> finalize

**Timestamp:** 2026-05-12

## Narrative
### Structure
Epic flow is a 5-step milestone planning flow managed by epic-conductor agent. Steps: Requirements (JTBD), Summary (user review, HALTs), Milestones (spawns milestone-splitter), Review (spawns milestone-reviewer), Present (HALTs for decision).

### Dependencies
Uses bw epic CLI commands: init, read, finalize, plan, link

### Highlights
Sub-agents: milestone-splitter (breaks into shippable phases), milestone-reviewer (reviews milestone plans). Document access via bw epic read {slug} requirements|milestones.

## Facts
- **epic_flow_steps**: Epic flow has 5 steps: Requirements, Summary, Milestones, Review, Present [convention]
- **sub_agents**: Epic-conductor delegates to milestone-splitter and milestone-reviewer sub-agents [convention]
- **document_access**: Document access: bw epic read {slug} requirements or milestones [convention]
