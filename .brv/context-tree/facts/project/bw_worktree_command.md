---
title: bw Worktree Command
summary: bw worktree CLI with create/list/remove subcommands, stores worktrees under .bw/worktrees/, uses git worktree with sparse-checkout
tags: []
related: []
keywords: []
createdAt: '2026-05-11T02:10:41.944Z'
updatedAt: '2026-05-11T02:10:41.944Z'
---
## Reason
Documenting new bw worktree command group

## Raw Concept
**Task:**
Implement bw worktree command for managing git worktrees

**Changes:**
- Added worktree command group with create, list, remove subcommands
- Implemented sparse-checkout to exclude .bw/ from worktrees

**Files:**
- bw/commands/worktree_cmd.py
- bw/core/paths.py
- bw/cli.py

**Flow:**
find_bw_root -> worktrees_dir -> git worktree add/list/remove -> sparse-checkout

**Timestamp:** 2026-05-11

## Narrative
### Structure
worktree_cmd.py defines Click group with 3 commands. paths.py provides worktrees_dir() function. cli.py registers the command.

### Dependencies
Requires git installed, uses subprocess to shell out to git commands

### Highlights
Name validation via regex ^[A-Za-z0-9][A-Za-z0-9._-]*$, default branch is bw/<name>, sparse-checkout excludes .bw/ directory

## Facts
- **worktree_storage_path**: Worktrees are stored under .bw/worktrees/ [project]
- **worktree_subcommands**: The worktree command has 3 subcommands: create, list, remove [project]
- **worktree_name_regex**: Name validation regex is ^[A-Za-z0-9][A-Za-z0-9._-]*$ [project]
- **worktree_default_branch**: Default branch name is bw/<name> [project]
- **worktree_sparse_checkout**: Sparse-checkout excludes .bw/ from worktree [project]
