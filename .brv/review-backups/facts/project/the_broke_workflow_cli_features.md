---
title: The Broke Workflow CLI Features
summary: 'Complete bw CLI feature inventory: 10 commands, 2 workflows (6-step plan, 5-step product), task management, adapters'
tags: []
related: []
keywords: []
createdAt: '2026-05-12T15:18:15.346Z'
updatedAt: '2026-05-12T15:18:15.346Z'
---
## Reason
Documenting bw CLI commands, workflows, and adapters

## Raw Concept
**Task:**
Document the-broke-workflow CLI features and architecture

**Changes:**
- Added complete CLI command inventory
- Documented plan/product flows
- Listed task and product subcommands

**Files:**
- bw/cli.py
- bw/core/steps.py
- bw/commands/task_cmd.py
- bw/commands/product_cmd.py
- steps/
- agents/
- adapters/

**Flow:**
triage -> (PLAN: 6 steps) or (PRODUCT: 5 steps)

**Timestamp:** 2026-05-12

## Narrative
### Structure
CLI package with 10 commands. Plan flow: 6 steps (requirements->discovery->analysis->write-plan->split-tasks->review). Product flow: 5 steps (requirements->summary->milestones->review->present).

### Dependencies
Uses Click for CLI, git worktrees under .bw/worktrees/, sparse checkout for .bw exclusion

### Highlights
Task statuses: pending/in_progress/done. Task subcommands: list/next/show/claim/release/status/deps/dag/add-dependency/comment/comments/remove. Product subcommands: init/list/docs/read/finalize/plan/status/link/remove. Claude Code adapter implemented, Codex adapter deferred.

### Rules
Rule 1: Task claim is atomic
Rule 2: Product finalize sets status=finalized
Rule 3: Worktree uses sparse checkout excluding .bw

### Examples
Example: bw task claim TASK_ID --owner NAME
Example: bw product plan SLUG MILESTONE_N
Example: bw triage renders Agent(...) prompt

## Facts
- **cli_commands**: bw CLI has 10 commands: config, doctor, init, install, plan, product, step, task, triage, worktree [project]
- **plan_flow_steps**: Plan flow has 6 steps [project]
- **product_flow_steps**: Product flow has 5 steps [project]
- **task_statuses**: Task statuses are pending, in_progress, done [project]
- **codex_adapter_status**: Codex adapter is deferred past MVP [project]
- **worktree_location**: Worktrees managed under .bw/worktrees/ [project]
