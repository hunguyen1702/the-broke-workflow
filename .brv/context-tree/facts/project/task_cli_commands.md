---
title: Task CLI Commands
summary: 'CLI commands for task lifecycle: list, next, show, claim, release, status, deps, dag, add-dependency, comment, comments, remove'
tags: []
keywords: []
importance: 50
recency: 1
maturity: draft
createdAt: '2026-04-19T15:47:25.576Z'
updatedAt: '2026-04-19T15:47:25.576Z'
---
## Reason
Curating bw task command implementation from task_cmd.py

## Raw Concept
**Task:**
Document bw task CLI commands implementation

**Changes:**
- Added bw task add-dependency command replacing old add-edge command
- Implements blocked_by dependency where child depends on parent

**Files:**
- bw/commands/task_cmd.py

**Flow:**
Click CLI commands delegate to task_store module functions

**Timestamp:** 2026-04-19

## Narrative
### Structure
Task CLI implemented as Click group with subcommands in bw/commands/task_cmd.py

### Dependencies
Depends on bw.core.frontmatter, bw.core.lock, bw.core.paths, bw.core.task_store

### Highlights
Commands: list (filter by plan/status), next (ready unclaimed tasks), show (print task), claim/release (atomic ownership), status (with transition validation), deps (show blockers/blocks), dag (ASCII render), add-dependency (child blocked_by parent), comment/comments (threaded comments), remove (delete task file)
