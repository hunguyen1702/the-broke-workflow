---
title: Epic Conductor Agent
summary: 'Epic Conductor orchestrates epic plan flow with 5 steps: requirements, summary, milestones, review, present'
tags: []
related: []
keywords: []
createdAt: '2026-05-12T17:15:47.003Z'
updatedAt: '2026-05-12T17:15:47.003Z'
---
## Reason
Document epic-conductor agent for epic plan flow orchestration

## Raw Concept
**Task:**
Document Epic Conductor agent role and responsibilities

**Files:**
- agents/epic-conductor.md

**Flow:**
requirements -> summary -> milestones -> review -> present -> finalize

**Timestamp:** 2026-05-12

## Narrative
### Structure
5-step flow: Step 1 (requirements - JTBD lens, follow-up questions), Step 2 (write requirements, halt for approval), Step 3 (spawn milestone-splitter), Step 4 (spawn milestone-reviewer), Step 5 (present, halt for decision, finalize)

### Dependencies
Spawns milestone-splitter and milestone-reviewer as sub-agents

### Highlights
Core rules: never craft file paths (use CLI), never craft ls/cat commands, keep context lean, HALTs at checkpoints, focus on WHAT not HOW

### Rules
Rule 1: Never craft file paths — use `bw epic read {slug} <doc>`
Rule 2: Never craft ls or cat — use CLI
Rule 3: Keep context lean — sub-agents get fresh context
Rule 4: HALTs at interactive checkpoints
Rule 5: Focus on WHAT, not HOW
