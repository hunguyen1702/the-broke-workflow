---
title: The Broke Workflow Architecture
summary: 'The Broke Workflow: 9 core modules, 10 CLI commands, 10 agents'
tags: []
related: []
keywords: []
createdAt: '2026-04-18T04:19:02.579Z'
updatedAt: '2026-05-12T14:52:23.496Z'
---
## Reason
Update architecture with new triage components (9 modules, 10 commands, 10 agents)

## Raw Concept
**Task:**
Document the_broke_workflow architecture with updated counts

**Changes:**
- Updated agents from 6 to 9 (added product-conductor, milestone-splitter, milestone-reviewer)
- Updated CLI commands from 6 to 9 (added product, step, worktree)
- Updated core modules from 6 to 9 (added config.py, steps.py)
- Added triage module (bw/core/triage.py)
- Added triage command
- Added triager agent

**Files:**
- bw/cli.py
- bw/commands/
- bw/core/
- agents/
- bw/core/triage.py
- bw/commands/triage_cmd.py
- agents/triager.md

**Flow:**
idea -> triage -> plan/product flow

**Timestamp:** 2026-05-12

## Narrative
### Structure
9 core modules: config, frontmatter, lock, paths, slug, steps, task_store, templates, triage. 10 CLI commands: config, doctor, init, install, plan, product, step, task, triage, worktree. 10 agents: analysis, conductor, discovery, milestone-reviewer, milestone-splitter, plan-writer, product-conductor, splitter, triager, worker.

### Dependencies
CLI tool using Python, integrates with Claude Code and Codex adapters

### Highlights
Triage is the new flow router - one-shot classifier for PLAN vs PRODUCT workflow
