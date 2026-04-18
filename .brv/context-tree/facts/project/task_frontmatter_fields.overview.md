---
related: [facts/project/task_store_module.overview.md]
---
<think>
The user wants me to produce a structured overview of this knowledge document about Task Frontmatter Fields. Let me analyze the document and create the required output.

Key points from the document:
1. Task template frontmatter fields: id, title, status, blocked_by, blocks, owner, claimed_at, effort
2. The document mentions newly added claimed_at field
3. The fields are defined in templates/task.md
4. ID format is {plan-slug}/{nnn}-{task-slug}
5. Status defaults to pending
6. claimed_at is empty until task is claimed
7. Effort values are S, M, L, XL

Structure/Sections:
- Reason: Documenting task template frontmatter fields including newly added claimed_at
- Raw Concept: Task details about documenting the fields
- Narrative: Structure, Highlights, and Rules sections

Notable entities:
- templates/task.md (file)
- claimed_at (new field)
- Fields: id, title, status, blocked_by, blocks, owner, claimed_at, effort
- Rules about field formats

Now I'll format this as requested - under 1500 tokens, markdown only, no preamble.
</think>

# Task Frontmatter Fields

## Key Points

- **Frontmatter fields**: id, title, status, blocked_by, blocks, owner, claimed_at, effort
- **New field added**: `claimed_at` tracks when a task is claimed by an owner (empty until claimed)
- **ID format**: `{plan-slug}/{nnn}-{task-slug}` (e.g., `proj/001-setup`)
- **Default status**: `pending`
- **Effort values**: S, M, L, XL
- **Source file**: `templates/task.md`

## Structure / Sections Summary

| Section | Content |
|---------|---------|
| **Reason** | Documents task template frontmatter fields including newly added `claimed_at` |
| **Raw Concept** | Overview of the task: document fields, changes made (added `claimed_at`), file location, and flow |
| **Narrative** | Three sub-sections: Structure (field list), Highlights (usage notes), Rules (field constraints) |

## Notable Entities & Decisions

- **Field**: `claimed_at` — newly introduced to track claim timestamp
- **File**: `templates/task.md` — central template for all tasks
- **Rule 1**: ID follows `{plan-slug}/{nnn}-{task-slug}` pattern
- **Rule 2**: Status defaults to `pending`
- **Rule 3**: `claimed_at` remains empty until task is claimed
- **Rule 4**: Effort must be one of S, M, L, XL