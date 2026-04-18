---
related: [facts/project/cli_tool_integrations.overview.md]
---
<think>
The user wants me to produce a structured overview of the knowledge document about "Workflow Conventions". Let me analyze the document and create a proper summary.

Key points from the document:
1. Python uses snake_case for functions and variables
2. Task IDs follow {plan-slug}/{nnn}-{task-slug} format
3. YAML frontmatter has specific required fields (id, title, status, blocked_by, blocks, owner, effort)
4. Workflow status machine: pending → ready/in_progress → done, with blocked as intermediate
5. Sub-agent communication pattern - minimal context (slug, read, write, return)
6. Lean context principle - keep context minimal and focused

The document covers:
- Coding style (Python snake_case)
- Task ID format
- YAML frontmatter schema
- Workflow status machine
- Sub-agent communication pattern

Notable entities:
- bw/core/task_store.py - the source file
- Task IDs format: {plan-slug}/{nnn}-{task-slug}
- YAML frontmatter fields: id, title, status, blocked_by, blocks, owner, effort
- Status flow: pending → ready/in_progress → done, with blocked as intermediate

Let me format this properly in markdown under 1500 tokens.
</think>

# Workflow Conventions

## Key Points

- **Naming**: Python uses snake_case for functions and variables
- **Task IDs**: Format follows `{plan-slug}/{nnn}-{task-slug}` (e.g., `auth-feature-x7k2/001-add-user-model`)
- **YAML Frontmatter**: Required fields are `id`, `title`, `status`, `blocked_by`, `blocks`, `owner`, `effort`
- **Status Machine**: Flow is `pending → ready/in_progress → done`, with `blocked` as an intermediate state
- **Sub-agent Pattern**: Give only slug, what to read, what to write, what to return — keep context lean and focused
- **Context Principle**: "Fresh context = lean context" — minimal, focused information only

## Structure / Sections Summary

The document is a conventions reference covering five main areas:

1. **Coding Style** — Python snake_case for functions/variables
2. **Task ID Format** — Structured `{plan-slug}/{nnn}-{task-slug}` pattern
3. **YAML Frontmatter Schema** — Task metadata fields (id, title, status, blocking relationships, owner, effort)
4. **Workflow Status Machine** — State transitions with blocked as intermediate
5. **Sub-agent Communication** — Minimal instruction pattern for delegation

## Notable Entities & Patterns

| Entity | Pattern |
|--------|---------|
| Source file | `bw/core/task_store.py` |
| Task ID example | `auth-feature-x7k2/001-add-user-model` |
| Status values | `pending`, `ready`, `in_progress`, `blocked`, `done` |
| Frontmatter fields | 7 required: id, title, status, blocked_by, blocks, owner, effort |

## Facts Summary

- **naming_convention**: Python uses snake_case [convention]
- **task_id_format**: `{plan-slug}/{nnn}-{task-slug}` [convention]
- **task_frontmatter_fields**: 7 required fields [convention]
- **workflow_statuses**: 5 states with defined transitions [convention]
- **sub_agent_instructions**: Minimal 4-part instruction pattern [convention]
- **context_principle**: Lean context for fresh assignments [convention]