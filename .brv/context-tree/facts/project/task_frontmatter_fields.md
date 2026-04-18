---
title: Task Frontmatter Fields
summary: 'Task template frontmatter fields: id, title, status, blocked_by, blocks, owner, claimed_at, effort'
tags: []
keywords: []
importance: 50
recency: 1
maturity: draft
createdAt: '2026-04-18T07:23:51.360Z'
updatedAt: '2026-04-18T07:23:51.360Z'
---
## Reason
Documenting task template frontmatter fields including newly added claimed_at

## Raw Concept
**Task:**
Document task template frontmatter fields

**Changes:**
- Added claimed_at field to task frontmatter

**Files:**
- templates/task.md

**Flow:**
Task created with frontmatter -> claimed_at populated when task is claimed

**Timestamp:** 2026-04-18

## Narrative
### Structure
Task frontmatter YAML at top of templates/task.md with fields: id, status, owner, blocked_by, blocks, claimed_at, effort

### Highlights
All task templates use this frontmatter. claimed_at field tracks when a task was claimed by an owner.

### Rules
Rule 1: id format is {plan-slug}/{nnn}-{task-slug}
Rule 2: status defaults to pending
Rule 3: claimed_at is empty until task is claimed
Rule 4: effort values are S, M, L, XL
