---
title: Task Store Module
summary: Python module for task file scanning, state management, and status transition validation with VALID_STATUSES and STATUS_TRANSITIONS
tags: []
related: [facts/project/the_broke_workflow_project_config.md]
keywords: []
importance: 56
recency: 1
maturity: draft
accessCount: 2
createdAt: '2026-04-18T04:20:31.114Z'
updatedAt: '2026-04-18T04:20:31.114Z'
---
## Reason
Documenting task_store.py with status management and transition validation

## Raw Concept
**Task:**
Document task_store.py - task file scanning and state management module

**Changes:**
- Curated from bw/core/task_store.py

**Files:**
- bw/core/task_store.py

**Flow:**
scan_tasks yields task metadata -> get_task loads by ID -> validate_transition checks status changes

**Timestamp:** 2026-04-18

**Patterns:**
- `^\{plan-slug\}/\{nnn\}-\{task-slug\}$` - Task ID format: plan-slug/nnn-task-slug

## Narrative
### Structure
Module provides scan_tasks() iterator for scanning task files, get_task() for loading by ID, VALID_STATUSES set, STATUS_TRANSITIONS dict, and validate_transition() function

### Dependencies
Depends on bw.core.frontmatter, bw.core.paths (find_bw_root, plan_tasks_dir, tasks_dir)

### Highlights
VALID_STATUSES: pending, ready, in_progress, blocked, done. STATUS_TRANSITIONS defines valid state machine transitions.

### Rules
Rule 1: Task ID must be format plan/slug (e.g., auth-feature-x7k2/001-add-user-model)
Rule 2: Status transitions must be validated via validate_transition()
Rule 3: done status has no outgoing transitions (terminal state)

### Examples
Example: validate_transition("pending", "in_progress") returns True
Example: scan_tasks(status_filter="pending") yields only pending tasks

## Facts
- **task_id_format**: Task IDs use format {plan-slug}/{nnn}-{task-slug} [convention]
- **task_frontmatter_fields**: YAML frontmatter fields: id, title, status, blocked_by, blocks, owner, effort [convention]
- **workflow_statuses**: Workflow statuses: pending → ready/in_progress → done, with blocked as intermediate [convention]
- **naming_convention**: Python uses snake_case for functions and variables [convention]
