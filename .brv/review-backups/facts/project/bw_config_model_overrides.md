---
title: BW Config Model Overrides
summary: 'Model overrides in .bw/config.yaml: default=sonnet, conductor=opus, other roles=sonnet. Product flow keys: product-conductor, milestone-splitter, milestone-reviewer. VERIFIED: reviewer key is DEAD - no corresponding agents/reviewer.md file exists.'
tags: []
related: []
keywords: []
createdAt: '2026-04-19T05:28:57.986Z'
updatedAt: '2026-05-11T02:06:53.104Z'
---
## Reason
Verified reviewer key is dead - no agents/reviewer.md file exists, only milestone-reviewer.md

## Raw Concept
**Task:**
Document .bw/config.yaml model overrides for bw CLI and verify reviewer key status

**Changes:**
- Added model overrides for claude-code tool
- Added product flow model override keys: product-conductor, milestone-splitter, milestone-reviewer
- Noted reviewer key anomaly: no corresponding agents/reviewer.md file exists
- Verified reviewer config key is dead code - no agents/reviewer.md exists
- Only milestone-reviewer.md exists under agents/

**Files:**
- .bw/config.yaml

**Flow:**
Config loaded by bw CLI on startup

**Timestamp:** 2026-05-11

## Narrative
### Structure
The .bw/config.yaml provides per-task model overrides. Default model is sonnet, conductor uses opus.

### Dependencies
Loaded by bw CLI core config module

### Highlights
Standard workflow keys: default, conductor, discovery, analysis, plan-writer, splitter, reviewer, worker. Product flow keys: product-conductor, milestone-splitter, milestone-reviewer. VERIFIED 2026-05-11: reviewer key has NO corresponding agents/reviewer.md file - only milestone-reviewer.md exists. The reviewer key in config is DEAD CODE and can be removed.
