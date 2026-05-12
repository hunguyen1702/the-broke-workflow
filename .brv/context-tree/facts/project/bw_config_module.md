---
title: BW Config Module
summary: Config module with agent names (epic-conductor, milestone-splitter, milestone-reviewer, triager) and model resolution
tags: []
related: []
keywords: []
createdAt: '2026-05-11T02:12:49.440Z'
updatedAt: '2026-05-12T17:15:46.995Z'
---
## Reason
Update bw/core/config.py knowledge with current agent names

## Raw Concept
**Task:**
Document bw/core/config.py module with current agent configuration

**Changes:**
- Updated agent names to epic-conductor, milestone-splitter, milestone-reviewer, triager
- Removed product-conductor from current agents

**Files:**
- bw/core/config.py

**Flow:**
load_config -> resolve_model -> is_configured

**Timestamp:** 2026-05-12

## Narrative
### Structure
AGENTS tuple defines 11 agents: conductor, discovery, analysis, plan-writer, splitter, reviewer, worker, epic-conductor, milestone-splitter, milestone-reviewer, triager. resolve_model() supports tool+agent model override with fallback chain.

### Dependencies
Uses yaml and bw.core.paths.find_bw_root

### Highlights
Model resolution order: models.<tool>.<agent> -> models.<tool>.default -> None. default_config() provides Anthropic model defaults (opus, sonnet, haiku).
