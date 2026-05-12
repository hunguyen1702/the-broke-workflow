---
title: Claude Code Work Adapter
summary: 'Work adapter handles task execution: claim → read task → execute → verify ACs. bw task block removed - use verbal explanation instead.'
tags: []
related: [facts/project/cli_tool_integrations.md, facts/project/task_store_module.md]
keywords: []
importance: 50
recency: 1
maturity: draft
createdAt: '2026-04-19T15:44:13.246Z'
updatedAt: '2026-04-19T15:44:13.246Z'
---
## Reason
Documenting Claude Code work adapter for task execution - updating blocked command convention

## Raw Concept
**Task:**
Document Claude Code work adapter for task claiming and execution

**Changes:**
- Updated blocked command: bw task block removed, use verbal explanation to user instead
- Updated task release: now reverts in_progress → pending (not → ready)

**Files:**
- adapters/claude-code/work.md

**Flow:**
claim task -> read task file -> read scope files -> execute work -> verify ACs -> mark done

**Timestamp:** 2026-04-19

## Narrative
### Structure
The work adapter (/work) handles atomic task claiming and execution. Task file is primary brief, plan is fallback for additional context.

### Dependencies
Requires task to be claimed first via bw task claim

### Highlights
5 key rules: (1) Task file first, (2) Respect boundaries, (3) Log gaps, (4) Verify ACs, (5) Claim before starting

### Rules
Rule 1: Task file first - don't read plan unless you must
Rule 2: Respect boundaries - don't touch files not in scope
Rule 3: Log gaps - if something was unclear, say so
Rule 4: Verify ACs - each acceptance criterion is a checkpoint
Rule 5: Claim before starting - never work unclaimed

### Examples
Usage: /work <task-id>
Example: /work auth-feature-x7k2/001-add-user-model
If stuck: Explain to the user what is blocking you and why (do NOT use bw task block)

## Facts
- **task_block_command**: The bw task block command was removed - use verbal explanation instead [convention]
- **task_block_pattern**: If stuck on a task, explain to the user what is blocking and why (do not use bw task block) [convention]
- **task_release_behavior**: bw task release now reverts in_progress status to pending (not to ready) [convention]
- **work_adapter_purpose**: The work.md adapter documents task claiming and execution flow [project]
- **work_adapter_steps**: Key steps: claim task, read task file, read scope files, execute work, verify ACs [project]
