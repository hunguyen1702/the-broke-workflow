---
title: Milestone Splitter Agent
summary: Milestone Splitter breaks epic requirements into 3-6 shippable milestones with ordering and scoping
tags: []
related: []
keywords: []
createdAt: '2026-05-12T17:15:47.011Z'
updatedAt: '2026-05-12T17:15:47.011Z'
---
## Reason
Document milestone-splitter agent for breaking epics into milestones

## Raw Concept
**Task:**
Document Milestone Splitter agent role and splitting principles

**Files:**
- agents/milestone-splitter.md

**Flow:**
read requirements -> analyze -> break into milestones -> write milestones.md -> return

**Timestamp:** 2026-05-12

## Narrative
### Structure
Input: plan slug + title. Output: .bw/plans/{slug}/milestones.md with milestone frontmatter and structure

### Dependencies
Writes to .bw/plans/{slug}/milestones.md

### Highlights
Milestone count: 3-6. Each must be shippable (standalone value), ordered (no later dependencies), scoped (clear include/exclude). Sizing: 3-7 days ideal, <1 day merge, >2 weeks split.

### Rules
Rule 1: Milestone count 3-6
Rule 2: Each milestone shippable standalone
Rule 3: Earlier milestones dont depend on later
Rule 4: Clear whats included and deferred
Rule 5: Order by dependency and priority
Rule 6: Front-load highest-value/risk items
