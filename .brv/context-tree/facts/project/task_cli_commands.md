---
title: Task CLI Commands
summary: 'bw task subcommands: add-dependency, claim, comment, comments, dag, deps, list, next, release, remove, show, status'
tags: []
related: []
keywords: []
createdAt: '2026-04-19T15:47:25.576Z'
updatedAt: '2026-05-11T02:07:38.753Z'
---
## Reason
Update task CLI commands with corrected subcommand count (12, not 13)

## Raw Concept
**Task:**
Document bw task CLI subcommands with corrected count

**Changes:**
- Added bw task add-dependency command replacing old add-edge command
- Implements blocked_by dependency where child depends on parent
- Corrected subcommand count from 13 to 12
- Verified list: add-dependency, claim, comment, comments, dag, deps, list, next, release, remove, show, status

**Files:**
- bw/commands/task_cmd.py

**Flow:**
Click group with 12 subcommands: list, next, show, claim, release, status, deps, dag, add-dependency, comment, comments, remove

**Timestamp:** 2026-05-11

## Narrative
### Structure
The bw task command is a Click group with 12 subcommands for task lifecycle management

### Dependencies
Uses bw.core.frontmatter, bw.core.lock, bw.core.paths, bw.core.task_store modules

### Highlights
12 subcommands: add-dependency (add blocker), claim (assign owner), comment/comments (add/list comments), dag (show dependency graph), deps (show blockers/blocks), list (list tasks), next (show ready tasks), release (drop claim), remove (delete task), show (print task), status (update status)

### Rules
Rule 1: Status transitions must be validated via validate_transition()
Rule 2: All modifications require acquiring lock via acquire()
Rule 3: Owner defaults to "unknown" if not specified

## Facts
- **task_cli_subcommand_count**: The bw task command has exactly 12 subcommands [project]
- **task_subcommand_list**: Task subcommands are: add-dependency, claim, comment, comments, dag, deps, list, next, release, remove, show, status [project]
