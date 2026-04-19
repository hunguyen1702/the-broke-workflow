<think>
The user wants me to produce a structured overview of this knowledge document about Claude Code Work Adapter. Let me analyze the document and extract the key points, structure, and notable entities/patterns/decisions.

Key points to extract:
1. Work adapter handles task execution flow: claim → read task → execute → verify ACs
2. The "bw task block" command was removed - now use verbal explanation instead
3. Task release now reverts in_progress → pending (not → ready)
4. Five key rules for task execution
5. Dependencies: task must be claimed first via "bw task claim"
6. Flow steps: claim task → read task file → read scope files → execute work → verify ACs → mark done

Structure:
- Reason: Documenting Claude Code work adapter
- Raw Concept: Task description and changes
- Narrative: Structure, Dependencies, Highlights, Rules, Examples
- Facts: Various conventions and patterns

Notable entities:
- work adapter (/work)
- bw task block command (now removed)
- task release behavior
- 5 key rules

Let me format this as a concise markdown overview under 1500 tokens.
</think>

# Claude Code Work Adapter - Overview

## Key Points

- **Task execution flow**: claim → read task file → read scope files → execute work → verify ACs → mark done
- **Blocked command change**: `bw task block` removed — use verbal explanation to user instead when stuck
- **Task release behavior**: `bw task release` now reverts status from `in_progress` → `pending` (previously → `ready`)
- **Five key rules**: (1) Task file first, (2) Respect boundaries, (3) Log gaps, (4) Verify ACs, (5) Claim before starting
- **Dependency**: Task must be claimed first via `bw task claim` before execution
- **Primary brief**: Task file is the primary brief; plan is fallback for additional context only

## Structure / Sections Summary

| Section | Content |
|---------|---------|
| **Reason** | Documenting Claude Code work adapter - updating blocked command convention |
| **Raw Concept** | Task details, file changes, execution flow, timestamp |
| **Narrative** | Structure description, dependencies, highlights, 5 rules, usage examples |
| **Facts** | Conventions and patterns (task_block, task_release, work_adapter) |

## Notable Entities & Decisions

| Entity/Decision | Description |
|-----------------|-------------|
| **work adapter** (`/work`) | Handles atomic task claiming and execution |
| **`bw task block`** | Command removed — replaced with verbal explanation convention |
| **`bw task release`** | Behavior changed: `in_progress` → `pending` (not → `ready`) |
| **Task file** | Primary brief; plan is fallback context only |
| **Scope boundaries** | Don't touch files outside task scope |
| **AC verification** | Each acceptance criterion is a checkpoint |
| **Files** | `adapters/claude-code/work.md` |

## Conventions

- **Stuck on task**: Explain to user what is blocking and why (no `bw task block`)
- **Claim before starting**: Never work on unclaimed tasks
- **Log gaps**: If something is unclear, explicitly say so