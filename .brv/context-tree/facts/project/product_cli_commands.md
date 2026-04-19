---
title: Product CLI Commands
summary: 'CLI commands: bw product init, list, docs, read, finalize for product plan lifecycle'
tags: []
related: [facts/project/product_plan_workflow.md, facts/project/cli_tool_integrations.md]
keywords: []
importance: 56
recency: 1
maturity: draft
accessCount: 2
createdAt: '2026-04-19T05:24:14.934Z'
updatedAt: '2026-04-19T05:24:14.934Z'
---
## Reason
Documenting bw product CLI commands for product plan management

## Raw Concept
**Task:**
Product CLI commands for product plan lifecycle management

**Files:**
- bw/commands/product_cmd.py

**Flow:**
init → list/docs/read → finalize

**Timestamp:** 2026-04-19

## Narrative
### Structure
Commands: init (create plan from templates), list (list all plans), docs (list documents in plan), read (print document), finalize (freeze plan)

### Dependencies
Uses bw.core.paths, bw.core.frontmatter, bw.core.slug, bw.core.templates

### Highlights
Short doc names: requirements→product-plan.md, milestones→milestones.md

### Rules
Rule 1: init requires unique title (fails if exists)
Rule 2: list shows slug, status, summary for each plan
Rule 3: docs maps friendly names to filenames
Rule 4: read accepts doc name or filename
Rule 5: finalize updates status to finalized with date

## Facts
- **cli_command**: bw product init creates new product plan [project]
- **cli_command**: bw product list shows all product plans [project]
- **cli_command**: bw product docs lists documents in a plan [project]
- **cli_command**: bw product read prints a product document [project]
- **cli_command**: bw product finalize freezes a product plan [project]
