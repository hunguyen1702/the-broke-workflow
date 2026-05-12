---
title: Task Store Module
summary: Task store module providing scan_tasks, get_task, validate_transition, and comment management for workflow tasks
tags: []
related: [facts/project/the_broke_workflow_project_config.md]
keywords: []
importance: 80
recency: 1
maturity: validated
accessCount: 5
updateCount: 3
createdAt: '2026-04-18T04:20:31.114Z'
updatedAt: '2026-04-19T15:49:31.975Z'
---
## Reason
Documenting task_store.py module for task scanning and state management

## Raw Concept
**Task:**
Document bw/core/task_store.py module

**Changes:**
- Curated from bw/core/task_store.py
- VALID_STATUSES simplified from {pending,ready,in_progress,blocked,done} to {pending,in_progress,done}
- STATUS_TRANSITIONS simplified: pending→{in_progress}, in_progress→{done,pending}, done→{}
- task_block command removed and replaced with task_add-dependency
- Added task_store.py with scan_tasks, get_task, validate_transition, add_comment, get_comments functions

**Files:**
- bw/core/task_store.py
- bw/commands/task_cmd.py

**Flow:**
task file read -> frontmatter parse -> status validation/comment update

**Timestamp:** 2026-04-19

**Patterns:**
- `^\{plan-slug\}/\{nnn\}-\{task-slug\}$` - Task ID format: plan-slug/nnn-task-slug

## Narrative
### Structure
Module at bw/core/task_store.py with functions: scan_tasks(plan_slug?, status_filter?) Iterator, get_task(task_id) tuple, validate_transition(current, new) bool, add_comment(task_id, text, author) dict, get_comments(task_id) list

### Dependencies
Depends on bw.core.frontmatter (read_file, write_file), bw.core.lock (acquire, release), bw.core.paths (find_bw_root, plan_tasks_dir, tasks_dir)

### Highlights
Valid statuses: pending, in_progress, done. Status transitions: pending→in_progress, in_progress→done|pending, done is terminal. Comments stored in task frontmatter with author, timestamp, text fields.

### Rules
Rule 1: Task ID format must be plan-slug/task-slug (e.g., "plan-001/my-task")
Rule 2: Status transitions validated before allowed
Rule 3: Comments require both non-empty text and author
Rule 4: Lock acquisition required for comment writes to prevent race conditions

### Examples
Example: validate_transition("pending", "in_progress") returns True
Example: scan_tasks(status_filter="pending") yields only pending tasks
