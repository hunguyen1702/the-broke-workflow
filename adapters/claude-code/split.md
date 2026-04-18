---
name: split
description: >-
  Split a finalized plan into task files with dependencies.
  Use after /plan has been finalized.
---

# /split — Split Plan into Tasks

Launch the splitter agent to decompose a finalized plan into discrete, self-contained task files with DAG dependencies.

## When to Use

- After `/plan` has been finalized (`bw plan finalize {slug}`)
- User says "split this plan", "break down tasks", "create tasks"
- User wants to see what work items exist for a feature

## How It Works

1. The splitter agent reads the plan document and discovery report.
2. It decomposes deliverables into 3-8 task files.
3. Tasks are maximally specific: exact file paths, function names, patterns.
4. DAG dependencies are declared via `blocked_by`.
5. A task list and DAG are presented for user spot-check.

## Usage

```
/split <plan-slug>
```

Example: `/split auth-feature-x7k2`

If no slug given, list plans and ask the user to pick.

## Key Agent Files

| File | Role |
|------|------|
| `agents/splitter.md` | Splitter agent definition |
| `steps/step-05-split-tasks.md` | Step 5 flow |

## Key Rules

- **Maximally specific.** "Add user model" is bad. "Add `User` struct to `src/auth/models/user.py`" is good.
- **Self-contained.** Each task can be understood from its file alone.
- **Explicit DAG.** Every dependency is declared in `blocked_by`.
- **Contracts over code.** Reference by name + location, never paste code.

## After Splitting

- Run `bw task dag --plan {slug}` to see the full DAG
- Run `/next` to see ready tasks
- Run `/work <task-id>` to claim and execute a task
