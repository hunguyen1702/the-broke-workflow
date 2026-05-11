---
title: plan_cli_commands
summary: 'bw plan has 7 subcommands: init, list, docs, read, finalize, remove, status. Lifecycle: init -> read/docs -> finalize -> remove. status command shows task progress with JSON output.'
tags: []
related: [facts/project/task_cli_commands.md, facts/project/product_cli_commands.md]
keywords: []
createdAt: '2026-05-11T02:11:44.838Z'
updatedAt: '2026-05-11T02:12:11.982Z'
---
## Reason
Updating plan CLI commands with new status and remove subcommands

## Raw Concept
**Task:**
Document bw plan CLI commands with 7 subcommands

**Changes:**
- Added 2 new commands: status and remove
- Now has 7 subcommands total vs 5 previously documented in CLAUDE.md
- Added status command to show task progress with --json and --details options
- Added remove command to delete plans with --force flag

**Files:**
- bw/commands/plan_cmd.py

**Flow:**
plan init -> plan read/docs -> plan finalize -> plan status -> plan remove

**Timestamp:** 2026-05-11

## Narrative
### Structure
bw/commands/plan_cmd.py defines 7 subcommands under the plan group. DOC_NAMES maps short names (plan/discovery/analysis) to filenames.

### Dependencies
Uses bw.core.frontmatter for read_file/update_meta, bw.core.paths for directory functions, bw.core.task_store.scan_tasks for status

### Highlights
status command shows task progress with progress bar and optional --json output for agents. remove command checks for task dependencies and requires --force to override.

### Rules
Rule 1: plan init requires unique title (slug)
Rule 2: plan finalize creates .bw/tasks/{slug}/ directory
Rule 3: plan remove requires --force if plan has tasks
Rule 4: plan status --json outputs structured data for programmatic use

## Facts
- **plan_subcommands**: bw plan has 7 subcommands [project]
- **plan_status_json**: plan status command shows task progress with optional JSON output [project]
- **plan_remove_force**: plan remove command requires --force to delete plan with tasks [project]
- **plan_lifecycle**: Plan lifecycle is: init -> read/docs -> finalize -> remove [convention]
