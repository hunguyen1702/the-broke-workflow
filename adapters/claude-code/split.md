---
name: split
description: >-
  Split a finalized plan into task files with dependencies.
  Use after /plan has been finalized.
---

# /split — Split Plan into Tasks

Run `bw step show 5 {slug}` and follow the instructions to decompose a finalized plan into task files.

## When to Use

- After `/plan` has been finalized (`bw plan finalize {slug}`)
- User says "split this plan", "break down tasks", "create tasks"

## How It Works

1. Run `bw step show 5 {slug}` — this outputs conductor instructions
2. The output includes a sub-agent bootstrap command — spawn a sub-agent with it
3. The sub-agent runs `bw step agent 5 {slug}` to get its full splitter instructions
4. Review the task list and DAG when the sub-agent returns

## Usage

- `/split auth-feature-x7k2` — split a specific plan
- `/split` — list plans and ask user to pick

## After Splitting

- `bw task dag --plan {slug}` — view the full DAG
- `/next` — see ready tasks
- `/work <task-id>` — claim and execute a task
