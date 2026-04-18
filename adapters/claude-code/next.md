---
name: next
description: >-
  Show ready tasks — unblocked, unclaimed tasks available to work on.
  Use when the user wants to see what work is available.
---

# /next — Show Ready Tasks

List tasks that are ready to work on: unblocked and unclaimed.

## How It Works

```
bw task next [--plan <slug>]
```

Shows all tasks with `status: ready` (or `pending` with no blockers).

## Usage

- `/next` — show all ready tasks across all plans
- `/next auth-feature-x7k2` — show ready tasks for a specific plan

## Output

Each ready task shown as:
```
{plan-slug}/{task-slug}: {status} effort:{S|M|L}
```

## Notes

- Claimed (owned) tasks are filtered out.
- Blocked tasks are filtered out.
- After seeing ready tasks, use `/work <task-id>` to claim one.
