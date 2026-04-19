---
name: status
description: >-
  Show a quick project snapshot — all plans and their task DAGs.
  Use when the user wants to see the current state of work.
---

# /status — Project Snapshot

Show a quick overview of all plans and their task DAGs.

## How It Works

```
bw task list
bw task dag [--plan <slug>]
```

## Output

1. **Plan summary**: all plans with their status and summaries
2. **Task list**: tasks grouped by plan with status, effort, blockers, owner
3. **DAG**: ASCII dependency graph for the plan

## Usage

- `/status` — all plans and tasks
- `/status auth-feature-x7k2` — specific plan's status and DAG

## Example Output

```
Plans:
  auth-feature-x7k2  [finalized]  user authentication
  api-refactor-y9m3  [draft]     REST API redesign

auth-feature-x7k2/:
  001-add-user-model         [done]       S
  002-add-auth-handlers      [done]       M       blocked_by:001
  003-write-auth-tests       [in_progress] M      @agent-1
  004-add-session-middleware [pending]    M       blocked_by:002
  005-write-integration-tests [pending]    L       blocked_by:004

DAG:
  001 → 002 → 004
            ↘ 003
  002 → 003
  004 → 005
```

## Notes

- `/next` is better for finding work to do.
- `/work <id>` is for claiming and executing a specific task.
- `/status` is for orientation and progress tracking.
