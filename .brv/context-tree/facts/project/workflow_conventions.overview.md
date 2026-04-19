<think>
The user wants me to produce a structured overview of the provided knowledge document about workflow conventions. Let me analyze the document and create a concise overview with:

1. Key points (3-7 bullet points)
2. Structure/sections summary
3. Notable entities, patterns, or decisions

The document is about fixing Rule 4 in workflow conventions to reflect a corrected status model. Let me extract the key information:

**Key Points:**
- Simplified status model from 5 to 3 statuses (pending, in_progress, done)
- Corrected Rule 4: Status flow is pending → in_progress → done
- Blocked state is now implicit via blocked_by dependencies
- Removed ready and blocked as explicit statuses
- VALID_STATUSES defined in task_store.py
- STATUS_TRANSITIONS defined in task_store.py

**Structure:**
- Reason section explaining the fix
- Raw Concept with task details
- Narrative with Structure, Dependencies, Highlights, and Rules sections

**Notable entities:**
- Files: bw/core/task_store.py, bw/commands/task_cmd.py
- VALID_STATUSES: {pending, in_progress, done}
- STATUS_TRANSITIONS: pending→{in_progress}, in_progress→{done,pending}, done→{}
- blocked_by field in task frontmatter
- Rule 4

Let me format this properly in markdown under 1500 tokens.
</think>

## Workflow Conventions — Overview

### Key Points

- **Simplified status model**: Reduced from 5 to 3 statuses — `pending`, `in_progress`, `done`
- **Corrected Rule 4**: Status flow is now `pending → in_progress → done`
- **Blocked state is implicit**: No explicit `blocked` or `ready` status; blockers tracked via `blocked_by` dependencies in task frontmatter
- **Valid statuses defined in `task_store.py`**: `VALID_STATUSES = {pending, in_progress, done}`
- **Status transitions**: `pending → {in_progress}`, `in_progress → {done, pending}`, `done → {}` (terminal)
- **Files modified**: `bw/core/task_store.py` and `bw/commands/task_cmd.py`

### Structure Summary

The document contains four main sections:

1. **Reason** — Explains the purpose: fixing Rule 4 to match the corrected status model
2. **Raw Concept** — Lists the task, changes made, affected files, and the new flow
3. **Narrative** — Structured into:
   - **Structure**: Location of status model definitions
   - **Dependencies**: How blocking is handled
   - **Highlights**: Valid statuses and transition rules
   - **Rules**: Specific wording for Rule 4

### Notable Entities & Decisions

| Entity | Detail |
|--------|--------|
| **Rule 4** | Status flow: pending → in_progress → done; blocked state implicit via `blocked_by` |
| **VALID_STATUSES** | `pending`, `in_progress`, `done` |
| **STATUS_TRANSITIONS** | Defined per status; `done` is terminal (no outgoing transitions) |
| **blocked_by** | Field in task frontmatter replacing explicit `blocked` status |
| **Files** | `bw/core/task_store.py`, `bw/commands/task_cmd.py` |
| **Timestamps** | Created 2026-04-18, Updated 2026-04-19 |