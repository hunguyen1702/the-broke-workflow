---
name: work
description: >-
  Claim and execute a single task. Reads the task file, executes the work,
  and marks the task done. Primary brief is the task file; plan is fallback.
---

# /work — Execute a Task

Claim a task atomically and execute it using the task file as the primary brief.

## When to Use

- User says "work on task", "do task", "claim task"
- User has picked a task from `/next` and wants to execute it

## How It Works

1. **Claim** the task: `bw task claim {id} --owner {agent}`
2. **Read** the task file: `bw task show {id}`
3. **Read** referenced files (scope section of task file)
4. **Execute** — work through acceptance criteria
5. **If blocked**: `bw task block {id} --reason "..."`
6. **If done**: `bw task status {id} done`

## Usage

```
/work <task-id>
```

Example: `/work auth-feature-x7k2/001-add-user-model`

## Key Rules

1. **Task file first.** Don't read the plan unless you must.
2. **Respect boundaries.** Don't touch files not in scope.
3. **Log gaps.** If something was unclear, say so.
4. **Verify ACs.** Each acceptance criterion is a checkpoint.
5. **Claim before starting.** Never work unclaimed.

## Fallback: Plan Context

If the task file doesn't contain enough context:
```
bw plan read {slug} plan
```

If you needed plan context, log the gap:
```
Warning: Needed plan context: {what was missing from task file}
```

## If Blocked

If you encounter an obstacle requiring decisions outside your scope:
```
bw task block {task-id} --reason "..."
```
Then explain to the user what blocked you.
