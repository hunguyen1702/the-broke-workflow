---
title: Epic Rename Product To Epic
summary: 'Canonical hierarchy: Epic -> Milestone -> Plan -> Task. CLI uses bw epic, --flow epic, epic: frontmatter. Tests verify legacy product flow is rejected.'
tags: []
related: []
keywords: []
createdAt: '2026-05-12T17:09:50.195Z'
updatedAt: '2026-05-12T17:09:50.195Z'
---
## Reason
Document the rename from product to epic workflow

## Raw Concept
**Task:**
Document the product-to-epic rename in the codebase

**Changes:**
- Renamed bw product to bw epic
- Renamed --flow product to --flow epic
- Renamed product-conductor to epic-conductor
- Renamed product: frontmatter to epic:
- Renamed product-plan.md to epic.md

**Files:**
- CLAUDE.md
- bw/commands/epic_cmd.py
- bw/core/steps.py
- agents/epic-conductor.md
- tests/test_epic_flow.py

**Flow:**
CLI -> epic command -> step flow -> milestone

**Timestamp:** 2025-05-12

## Narrative
### Structure
Canonical hierarchy: Epic -> Milestone -> Plan -> Task. Epic docs at .bw/plans/<slug>/epic.md, milestones at .bw/plans/<slug>/milestones.md. Plans link via epic: and milestone: frontmatter.

### Dependencies
Requires flow configuration in bw/core/steps.py with EPIC_STEP_META and EPIC_STEP_AGENTS

### Highlights
CLI commands: bw epic init/list/docs/read/finalize/plan/status/link/remove. Step flow: bw step list --flow epic. Tests verify: --help shows epic not product, legacy product flow rejected, epic plan links with epic: frontmatter.

### Rules
Rule 1: Use epic: not product: in frontmatter
Rule 2: Use --flow epic not --flow product
Rule 3: Use bw epic not bw product

### Examples
Example: bw epic init "New Feature"
Example: bw step list --flow epic
Example frontmatter: epic: new-feature, milestone: 1

## Facts
- **hierarchy**: Canonical hierarchy is Epic -> Milestone -> Plan -> Task [convention]
- **cli_command**: CLI command is bw epic [convention]
- **flow_flag**: Step flow flag is --flow epic [convention]
- **model_key**: Model key is epic-conductor [project]
- **test_coverage**: Tests verify legacy product flow is rejected [project]
