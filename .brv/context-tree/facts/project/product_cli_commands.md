---
title: Product CLI Commands
summary: '9 product subcommands: init, list, docs, read, finalize, plan, status, link, remove'
tags: []
related: [facts/project/product_plan_workflow.md, facts/project/cli_tool_integrations.md, facts/project/product_plan_workflow.md, facts/project/cli_tool_integrations.md]
keywords: []
importance: 67
recency: 1
maturity: validated
accessCount: 4
updateCount: 1
createdAt: '2026-04-19T05:24:14.934Z'
updatedAt: '2026-04-19T15:46:08.040Z'
---
## Reason
Update product CLI commands with new link, plan, status, remove commands

## Raw Concept
**Task:**
Document all bw product CLI commands

**Changes:**
- Added link command: bw product link <plan_slug> <product_slug> <milestone_n>
- Added plan command: bw product plan <slug> <milestone_n>
- Added status command: bw product status <slug> with --json and --details flags
- Added remove command: bw product remove <slug> with --force flag

**Files:**
- bw/commands/product_cmd.py

**Flow:**
init → list/docs/read → plan/link → status → finalize/remove

**Timestamp:** 2026-04-19

## Narrative
### Structure
Click-based CLI with 9 subcommands. Each command validates inputs and provides helpful error messages.

### Dependencies
Uses bw.core.paths, bw.core.frontmatter, bw.core.slug, bw.core.templates

### Highlights
link: Links existing plan to milestone (3 args). plan: Creates new plan from milestone (2 args). status: Shows progress with optional JSON/detailed output. remove: Safety check prevents accidental deletion of linked plans.

### Rules
Rule 1: init requires unique title (fails if exists)
Rule 2: list shows slug, status, summary for each plan
Rule 3: docs maps friendly names to filenames
Rule 4: read accepts doc name or filename
Rule 5: finalize updates status to finalized with date

### Examples
Example: bw product link my-api-plan my-product 2 → Links my-api-plan to my-product milestone 2
Example: bw product status my-product --json → Outputs status as JSON for scripting
