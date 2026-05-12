---
title: BW Config Model Overrides
summary: 'Claude Code model overrides: reviewer now sonnet (was dead 2026-05-11), triager added as haiku, 9 total agent model assignments'
tags: []
related: []
keywords: []
createdAt: '2026-04-19T05:28:57.986Z'
updatedAt: '2026-05-12T14:56:08.628Z'
---
## Reason
Refresh config model overrides with current .bw/config.yaml - confirmed reviewer alive (sonnet), added triager (haiku)

## Raw Concept
**Task:**
Refresh bw_config_model_overrides with current .bw/config.yaml

**Changes:**
- Added model overrides for claude-code tool
- Added product flow model override keys: product-conductor, milestone-splitter, milestone-reviewer
- Noted reviewer key anomaly: no corresponding agents/reviewer.md file exists
- Verified reviewer config key is dead code - no agents/reviewer.md exists
- Only milestone-reviewer.md exists under agents/
- Confirmed reviewer key alive - now set to sonnet (was flagged dead 2026-05-11)
- Added triager key with haiku model - new agent role

**Files:**
- .bw/config.yaml

**Flow:**
Config YAML loaded -> Model overrides extracted -> Knowledge updated

**Timestamp:** 2026-05-12

## Narrative
### Structure
Model overrides defined under models.claude-code in .bw/config.yaml

### Dependencies
Used by bw config module to resolve per-agent model selection

### Highlights
9 agent model assignments: default(sonnet), conductor(opus), discovery(sonnet), analysis(sonnet), plan-writer(sonnet), splitter(sonnet), reviewer(sonnet), worker(sonnet), triager(haiku)

## Facts
- **reviewer_model**: Reviewer model is sonnet [project]
- **triager_model**: Triager model is haiku [project]
- **model_override_count**: Total agent model overrides: 9 [project]
