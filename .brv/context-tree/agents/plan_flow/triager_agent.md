---
title: Triager Agent
summary: Triager classifies user ideas into PLAN (single feature) or EPIC (multi-stream/milestone) flow using decision tree
tags: []
related: []
keywords: []
createdAt: '2026-05-12T17:15:47.016Z'
updatedAt: '2026-05-12T17:15:47.016Z'
---
## Reason
Document triager agent for classifying ideas as PLAN or EPIC flow

## Raw Concept
**Task:**
Document Triager agent decision logic for PLAN vs EPIC classification

**Files:**
- agents/triager.md

**Flow:**
receive idea + has_codebase -> scope test -> knowledge test (if single) -> value-stream test (if multi) -> output decision card

**Timestamp:** 2026-05-12

## Narrative
### Structure
Decision tree: A (scope test single/multi) -> B (knowledge test clear/unclear, only if single) -> C (value-stream test multi/single-stream, only if multi)

### Dependencies
Uses has_codebase flag to determine if in real repo or greenfield

### Highlights
PLAN signals: fix, add, refactor, file/module names. EPIC signals: MVP, launch, phase, roadmap, platform, multiple subsystems. Output: strict decision card format with Why, Path, Next command.

### Rules
Rule 1: One card only — no preamble or closing
Rule 2: Ground Why in signals — quote/paraphrase idea text
Rule 3: Never recommend both flows with equal weight
Rule 4: Dont ask clarifying questions — work with what given
Rule 5: Default to PLAN if idea genuinely empty
