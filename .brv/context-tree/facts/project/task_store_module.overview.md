---
related: [facts/project/cli_tool_integrations.overview.md, facts/project/task_frontmatter_fields.overview.md]
---
<think>
The user wants me to produce a structured overview of this knowledge document about the Task Store Module. Let me analyze the document and extract the key information.

Key entities and concepts:
- Module: task_store.py in bw/core/
- Functions: scan_tasks(), get_task(), validate_transition()
- Constants: VALID_STATUSES, STATUS_TRANSITIONS
- Dependencies: bw.core.frontmatter, bw.core.paths (find_bw_root, plan_tasks_dir, tasks_dir)
- Task ID format: {plan-slug}/{nnn}-{task-slug}
- Frontmatter fields: id, title, status, blocked_by, blocks, owner, effort

Status flow:
- pending → ready/in_progress → done
- blocked is intermediate
- done is terminal (no outgoing transitions)

Valid statuses: pending, ready, in_progress, blocked, done

Rules:
1. Task ID format: plan/slug
2. Status transitions must use validate_transition()
3. done is terminal

Let me structure this properly in markdown with:
- Key points (3-7 bullets)
- Structure/sections summary
- Notable entities, patterns, decisions
</think>

# Task Store Module Overview

## Key Points

- **Module**: `bw/core/task_store.py` — handles task file scanning, state management, and status transition validation
- **Core Functions**: `scan_tasks()` (iterator), `get_task()` (load by ID), `validate_transition()` (transition validation)
- **Valid Statuses**: `pending`, `ready`, `in_progress`, `blocked`, `done`
- **Task ID Format**: `{plan-slug}/{nnn}-{task-slug}` (e.g., `auth-feature-x7k2/001-add-user-model`)
- **Terminal State**: `done` has no outgoing transitions (workflow terminates)
- **Frontmatter Fields**: id, title, status, blocked_by, blocks, owner, effort

## Structure / Sections Summary

| Section | Content |
|---------|---------|
| **Reason** | Documenting task_store.py with status management and transition validation |
| **Raw Concept** | Flow: scan_tasks → get_task → validate_transition |
| **Narrative** | Module structure, dependencies, valid statuses, rules, examples |
| **Facts** | Task ID format, frontmatter fields, workflow statuses, naming conventions |

## Notable Entities & Patterns

**Functions**
- `scan_tasks(status_filter=None)` — yields task metadata from task files
- `get_task(task_id)` — loads single task by ID
- `validate_transition(from_status, to_status)` — validates state machine transitions

**Constants**
- `VALID_STATUSES` — set of allowed status strings
- `STATUS_TRANSITIONS` — dict defining valid from→to status pairs

**Dependencies**
- `bw.core.frontmatter`
- `bw.core.paths` (find_bw_root, plan_tasks_dir, tasks_dir)

**Rules Enforced**
1. Task IDs must match `{plan-slug}/{nnn}-{task-slug}` pattern
2. All status changes must pass through `validate_transition()`
3. `done` is a terminal state — no transitions out allowed

**Workflow Pattern**
```
pending → ready/in_progress → done
   ↓         ↓
  blocked ←─────
```