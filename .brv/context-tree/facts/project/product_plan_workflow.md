---
title: Product Plan Workflow
summary: '5-step CLI-guided product planning with 9 subcommands: init, list, docs, read, finalize, plan, status, link, remove'
tags: []
related: [facts/project/workflow_conventions.md, facts/project/cli_tool_integrations.md, facts/project/cli_tool_integrations.md, facts/project/workflow_conventions.md]
keywords: []
importance: 67
recency: 1
maturity: validated
accessCount: 4
updateCount: 1
createdAt: '2026-04-19T05:24:14.931Z'
updatedAt: '2026-04-19T15:46:08.027Z'
---
## Reason
Update product plan workflow with new CLI commands: link, plan, status, remove

## Raw Concept
**Task:**
Document product plan workflow with CLI commands for product-level planning

**Changes:**
- Added Requirements step with JTBD interview framework
- Added Summary step with HALTs for user approval
- Added Milestones step spawning milestone-splitter sub-agent
- Added Review step spawning milestone-reviewer sub-agent
- Added Present step with finalize decision HALT
- Added bw product link command to link existing plan to a product milestone
- Added bw product plan command to create a plan linked to a milestone
- Added bw product status command for milestone rollup with task progress
- Added bw product remove command to remove product and linked plans
- Added helper functions: _parse_milestones, _find_linked_plans, _task_counts, _progress_bar

**Files:**
- steps/product-step-01-requirements.md
- agents/product-conductor.md
- bw/commands/product_cmd.py

**Flow:**
product init → product plan → product status (with progress tracking)

**Timestamp:** 2026-04-19

**Patterns:**
- `^## Milestone (\d+):\s*(.+)` (flags: M) - Match milestone headings in milestones.md
- `\*\*Goal:\*\*\s*(.+)` - Extract goal text from milestone sections

## Narrative
### Structure
bw/commands/product_cmd.py implements product plan lifecycle with Click CLI framework. Contains 9 subcommands grouped under "bw product" parent command.

### Dependencies
Depends on bw.core.frontmatter (read_file, update_meta), bw.core.paths (find_bw_root, plan_dir, plans_dir), bw.core.slug (slugify), bw.core.task_store (scan_tasks), bw.core.templates (get_template)

### Highlights
Product plans are stored in .bw/plans/{slug}/ directory. Each product has product-plan.md and milestones.md. Plans linked to milestones have product and milestone frontmatter fields. Status command shows task progress with visual progress bars.

### Rules
Rule 1: Milestone numbers in milestones.md must be sequential starting from 1
Rule 2: Product plan must exist before linking plans to it
Rule 3: Cannot remove product with linked plans unless --force is used
Rule 4: Plan status is tracked via task frontmatter (done, in_progress, pending)

### Examples
Example spawn for milestone-splitter: "Break the product plan {slug} into milestones. Read: bw product read {slug} requirements. Write: .bw/plans/{slug}/milestones.md. Return: number of milestones + one-line summary each"

## Facts
- **product_cli_command_count**: Product plan workflow has 9 CLI commands [project]
- **product_storage_path**: Products are stored in .bw/plans/{slug}/ [project]
- **plan_milestone_link**: Plans can be linked to product milestones via product/milestone frontmatter [project]
- **progress_tracking**: Status shows task counts with visual progress bars [project]
