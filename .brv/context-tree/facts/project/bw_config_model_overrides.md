---
title: BW Config Model Overrides
summary: 'Model overrides in .bw/config.yaml: default=sonnet, conductor=opus, discovery/analysis/plan-writer/splitter/reviewer/worker=sonnet'
tags: []
keywords: []
importance: 50
recency: 1
maturity: draft
createdAt: '2026-04-19T05:28:57.986Z'
updatedAt: '2026-04-19T05:28:57.986Z'
---
## Reason
Adding .bw/config.yaml model overrides for Claude Code commands

## Raw Concept
**Task:**
Document .bw/config.yaml model overrides for bw CLI

**Changes:**
- Added model overrides for claude-code tool

**Files:**
- .bw/config.yaml

**Flow:**
config loaded by bw CLI on startup

**Timestamp:** 2026-04-19

## Narrative
### Structure
The .bw/config.yaml provides per-task model overrides. Default model is sonnet, but conductor uses opus for more capable orchestration.

### Dependencies
Loaded by bw CLI core config module

### Highlights
Model override keys: default, conductor, discovery, analysis, plan-writer, splitter, reviewer, worker

## Facts
- **default_model**: Default model is claude-sonnet-4-20250514 [project]
- **conductor_model**: Conductor uses opus model [project]
- **role_models**: All other roles use sonnet model [project]
