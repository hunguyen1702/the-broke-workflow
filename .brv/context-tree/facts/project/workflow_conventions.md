---
title: Workflow Conventions
summary: 'Workflow conventions: task IDs, YAML frontmatter, status machine, sub-agent instructions, lean context principle'
tags: []
keywords: []
importance: 77
recency: 1
maturity: validated
accessCount: 9
createdAt: '2026-04-18T04:20:31.122Z'
updatedAt: '2026-04-18T04:20:31.122Z'
---
## Reason
Documenting workflow and coding conventions from task_store context

## Raw Concept
**Task:**
Document workflow and coding conventions used in the broke workflow

**Changes:**
- Curated from task_store context with conventions

**Files:**
- bw/core/task_store.py

**Timestamp:** 2026-04-18

## Narrative
### Structure
Conventions cover: coding style (Python snake_case), task ID format, YAML frontmatter schema, workflow status machine, sub-agent communication pattern

### Highlights
Sub-agents: give only slug, what to read, what to write, what to return. Fresh context = lean context.

### Rules
Rule 1: Use snake_case for Python functions and variables
Rule 2: Task IDs must follow {plan-slug}/{nnn}-{task-slug} format
Rule 3: YAML frontmatter must include: id, title, status, blocked_by, blocks, owner, effort
Rule 4: Status flow: pending → ready/in_progress → done, with blocked as intermediate state
Rule 5: Sub-agents receive minimal context (slug, read, write, return instructions only)

## Facts
- **naming_convention**: Python uses snake_case for functions and variables [convention]
- **task_id_format**: Task IDs use format {plan-slug}/{nnn}-{task-slug} (e.g., auth-feature-x7k2/001-add-user-model) [convention]
- **task_frontmatter_fields**: YAML frontmatter for tasks includes: id, title, status, blocked_by, blocks, owner, effort [convention]
- **workflow_statuses**: Workflow statuses: pending → ready/in_progress → done, with blocked as intermediate [convention]
- **sub_agent_instructions**: Sub-agents receive only slug, what to read, what to write, what to return [convention]
- **context_principle**: Fresh context = lean context - keep context minimal and focused [convention]
