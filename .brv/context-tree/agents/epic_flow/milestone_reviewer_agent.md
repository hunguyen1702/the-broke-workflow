---
title: Milestone Reviewer Agent
summary: Milestone Reviewer performs adversarial review covering coverage, standalone value, ordering, sizing, and gaps
tags: []
related: []
keywords: []
createdAt: '2026-05-12T17:15:47.014Z'
updatedAt: '2026-05-12T17:15:47.014Z'
---
## Reason
Document milestone-reviewer agent for adversarial milestone review

## Raw Concept
**Task:**
Document Milestone Reviewer agent role and checklist

**Files:**
- agents/milestone-reviewer.md

**Flow:**
read requirements + milestones -> review checklist -> return findings

**Timestamp:** 2026-05-12

## Narrative
### Structure
5-category checklist: Coverage, Standalone Value, Ordering, Sizing, Gaps. Each item rated YES/NO/PARTIAL.

### Highlights
Verdict categories: GOOD / NEEDS WORK / RETHINK. Critical: constructiveness (every issue = suggestion), focus on substance, think like solo developer.

### Rules
Rule 1: Be constructive — every issue needs a suggestion
Rule 2: Focus on substance — dont nitpick wording
Rule 3: Think like solo developer
Rule 4: Check not yet lists — deferred items must appear in later milestones
