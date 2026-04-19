---
title: Model Configuration System
summary: 'Model config in .bw/config.yaml with resolution: exact match -> models.<tool>.default -> tool natural default'
tags: []
keywords: []
importance: 50
recency: 1
maturity: draft
createdAt: '2026-04-19T05:27:29.255Z'
updatedAt: '2026-04-19T05:27:29.255Z'
---
## Reason
Documenting the bw model config system with per-tool per-agent overrides and resolution order

## Raw Concept
**Task:**
Document model configuration system for agent tool selection

**Files:**
- .bw/config.yaml
- bw/commands/step_cmd.py

**Flow:**
config.yaml -> resolution order -> Agent() call with correct model

## Narrative
### Structure
The model config system allows per-tool per-agent model overrides. Resolution order: models.<tool>.<agent> exact match -> models.<tool>.default -> tool natural default. The bw step spawn command uses this to output Agent(...) calls with the correct model.

### Highlights
Claude-code tool uses sonnet by default, conductor agent overrides to opus. Supported agents: conductor, discovery, analysis, plan-writer, splitter, reviewer, worker.
