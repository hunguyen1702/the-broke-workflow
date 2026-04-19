---
title: Workflow Conventions
summary: Workflow conventions with corrected Rule 4 status flow (pending → in_progress → done)
tags: []
keywords: []
importance: 100
recency: 1
maturity: core
accessCount: 14
updateCount: 2
createdAt: '2026-04-18T04:20:31.122Z'
updatedAt: '2026-04-19T15:49:31.986Z'
---
## Reason
Fixing Rule 4 to reflect corrected status model from task_store.py

## Raw Concept
**Task:**
Update workflow_conventions Rule 4

**Changes:**
- Curated from task_store context with conventions
- Simplified status model from 5 to 3 statuses
- Removed ready and blocked as explicit statuses
- Blocked state now implicit via blocked_by dependencies
- Corrected Rule 4: Status flow is pending → in_progress → done. Blocked state is implicit via blocked_by deps, no explicit blocked/ready status.

**Files:**
- bw/core/task_store.py
- bw/commands/task_cmd.py

**Flow:**
pending → in_progress → done

**Timestamp:** 2026-04-19

## Narrative
### Structure
Task status model defined in bw/core/task_store.py with VALID_STATUSES and STATUS_TRANSITIONS

### Dependencies
blocked_by field in task frontmatter tracks blockers instead of explicit status

### Highlights
VALID_STATUSES: {pending, in_progress, done}; STATUS_TRANSITIONS: pending→{in_progress}, in_progress→{done,pending}, done→{}

### Rules
Rule 4: Status flow: pending → in_progress → done. Blocked state is implicit via blocked_by deps, no explicit blocked/ready status.
