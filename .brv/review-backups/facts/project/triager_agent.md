---
title: Triager Agent
summary: Triager agent classifies ideas using scope/knowledge/value-stream tests
tags: []
related: []
keywords: []
createdAt: '2026-05-12T14:52:16.827Z'
updatedAt: '2026-05-12T14:52:16.827Z'
---
## Reason
Document new triager sub-agent with decision tree logic

## Raw Concept
**Task:**
Document triager sub-agent for idea classification

**Changes:**
- Created triager.md agent with decision tree

**Files:**
- agents/triager.md

**Flow:**
idea + has_codebase -> decision tree -> PLAN/PRODUCT recommendation

**Timestamp:** 2026-05-12

## Narrative
### Structure
Triager agent uses 3-step decision tree: A (scope test) determines single vs multi, B (knowledge test) for single scope, C (value-stream test) for multi scope. Outputs decision card with Why, Path, Next command.

### Highlights
Decision paths: A:single→B:clear/unclear→PLAN; A:multi→C:single-stream→size proxy→PLAN/PRODUCT; A:multi→C:multi-stream→PRODUCT

### Rules
Rule 1: Output exactly one decision card
Rule 2: Never recommend both flows equally
Rule 3: Default to PLAN if idea too sparse
Rule 4: Ground Why in concrete signals from idea text

### Examples
PLAN: "Add login" (single feature, unclear HOW)
PRODUCT: "Build search platform with indexing, ranking, query API" (3 subsystems)
