---
title: The Broke Workflow CLI Features
summary: '10 CLI commands: config, doctor, init, install, plan, product, step, task, triage, worktree. Plan flow: 6 steps, Product flow: 5 steps.'
tags: []
related: []
keywords: []
createdAt: '2026-05-12T15:18:15.346Z'
updatedAt: '2026-05-12T15:18:39.771Z'
---
## Reason
Documenting CLI features from RLM context

## Raw Concept
**Task:**
Document CLI commands, workflows, and adapters for the-broke-workflow project

**Changes:**
- Added complete CLI command inventory
- Documented plan/product flows
- Listed task and product subcommands
- Curated CLI feature documentation
- Documented plan and product flows
- Captured task and product subcommands

**Files:**
- bw/cli.py
- bw/core/steps.py
- bw/commands/task_cmd.py
- bw/commands/product_cmd.py
- steps/
- agents/
- adapters/
- adapters/claude-code/
- adapters/codex/

**Flow:**
triage -> (PLAN: step1-6) OR (PRODUCT: step1-5)

**Timestamp:** 2026-05-12

## Narrative
### Structure
Python Click CLI with 10 subcommands. Plan flow uses agents: discovery, analysis, plan-writer, splitter. Product flow uses milestone-splitter, milestone-reviewer.

### Dependencies
Requires git for worktree management, Click for CLI

### Highlights
Task dependency DAG, claim/release mechanism, product-to-milestone linking, sparse checkout worktrees, Agent(...) prompt for triage

### Rules
Rule 1: Task claim is atomic
Rule 2: Product finalize sets status=finalized
Rule 3: Worktree uses sparse checkout excluding .bw

### Examples
Example: bw task claim TASK_ID --owner NAME
Example: bw product plan SLUG MILESTONE_N
Example: bw triage renders Agent(...) prompt

## Facts
- **cli_commands**: 10 CLI commands: config, doctor, init, install, plan, product, step, task, triage, worktree [project]
- **plan_flow**: Plan flow has 6 steps [project]
- **product_flow**: Product flow has 5 steps [project]
- **task_statuses**: Task statuses: pending, in_progress, done [project]
- **codex_adapter**: Codex adapter is deferred past MVP [project]
- **worktree**: Worktree uses sparse checkout excluding .bw [project]
