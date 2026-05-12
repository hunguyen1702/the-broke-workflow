---
title: Epic Flow Architecture
summary: 'Epic flow replaces product flow: Epic -> Milestone -> Plan -> Task hierarchy with bw epic CLI, --flow epic, and epic-conductor model config'
tags: []
related: []
keywords: []
createdAt: '2026-05-12T16:20:32.312Z'
updatedAt: '2026-05-12T16:20:32.312Z'
---
## Reason
Documenting the renamed epic flow hierarchy and CLI changes

## Raw Concept
**Task:**
Document epic flow architecture after renaming from product flow

**Changes:**
- Hard-renamed product flow to epic flow
- Canonical hierarchy: Epic -> Milestone -> Plan -> Task
- CLI command: bw epic
- Step flow: --flow epic
- Implementation plan frontmatter: epic: and milestone: fields
- Epic documents: .bw/plans/<slug>/epic.md and milestones.md
- Model config key: epic-conductor
- Removed bw product command and --flow product support

**Files:**
- bw/cli.py
- bw/commands/epic_cmd.py
- bw/commands/plan_cmd.py
- bw/core/steps.py
- bw/commands/step_cmd.py
- templates/epic.md
- templates/plan.md
- tests/test_epic_flow.py

**Flow:**
bw epic -> step --flow epic -> generate epic.md + milestones.md -> implementation plans with epic: frontmatter

**Timestamp:** 2026-05-12

## Narrative
### Structure
The workflow hierarchy is now Epic (top) -> Milestone -> Plan -> Task. The epic-conductor model coordinates epic-level planning. Implementation plans use epic: and milestone: frontmatter fields to link to parent epic/milestone.

### Dependencies
Depends on step command infrastructure in bw/core/steps.py

### Highlights
CLI uses bw epic command, step flow uses --flow epic flag, model config uses epic-conductor key

## Facts
- **workflow_hierarchy**: Canonical hierarchy is Epic -> Milestone -> Plan -> Task [project]
- **cli_command**: CLI command is bw epic [project]
- **step_flow_flag**: Step flow flag is --flow epic [project]
- **model_config_key**: Model config key is epic-conductor [project]
