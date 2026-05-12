---
title: Triager Agent
summary: Triager agent classifies ideas as PLAN flow or EPIC flow with decision tree logic
tags: []
related: []
keywords: []
createdAt: '2026-05-12T14:52:16.827Z'
updatedAt: '2026-05-12T17:14:03.338Z'
---
## Reason
Update triager agent to output plan vs epic flow recommendation

## Raw Concept
**Task:**
Document the triager agent prompt for classifying work scope

**Changes:**
- Created triager.md agent with decision tree
- Updated recommendation from PRODUCT to EPIC
- Updated output format to show plan vs epic commands

**Files:**
- agents/triager.md

**Flow:**
idea + has_codebase -> decision tree -> recommendation card

**Timestamp:** 2026-05-12

## Narrative
### Structure
Triager reads user idea and classifies as PLAN flow (single feature) or EPIC flow (multi-stream, milestone-focused). Decision tree: A) Scope test (single vs multi), B) Knowledge test (for single), C) Value-stream test (for multi).

### Dependencies
Input: idea text, has_codebase boolean

### Highlights
Output format: Recommendation: PLAN/EPIC flow, Why (grounded in signals), Path (decision tree path), Next command (bw plan init or bw epic init)

### Rules
Rule 1: Output exactly one decision card
Rule 2: Never recommend both flows equally
Rule 3: Default to PLAN if idea too sparse
Rule 4: Ground Why in concrete signals from idea text

### Examples
PLAN: "Add login" (single feature, unclear HOW)
PRODUCT: "Build search platform with indexing, ranking, query API" (3 subsystems)

## Facts
- **plan_signals**: Plan signals: fix, add, refactor, file/module names, existing codebase references [convention]
- **epic_signals**: Epic signals: MVP, launch, phase, roadmap, platform, multiple subsystems/personas [convention]
- **epic_threshold**: EPIC flow recommended for multi-stream (>=2 independent value streams) [convention]
