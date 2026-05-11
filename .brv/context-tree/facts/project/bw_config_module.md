---
title: BW Config Module
summary: Model resolution from .bw/config.yaml with tool+agent override hierarchy
tags: []
related: []
keywords: []
createdAt: '2026-05-11T02:12:49.440Z'
updatedAt: '2026-05-11T02:12:49.440Z'
---
## Reason
Document new config.py module for model resolution

## Raw Concept
**Task:**
Document bw/core/config.py module

**Files:**
- bw/core/config.py

**Flow:**
load_config -> resolve_model -> return model name

## Narrative
### Structure
Module provides load_config(), save_config(), resolve_model(), is_configured(), default_config() functions

### Dependencies
Uses yaml for config parsing, bw.core.paths for finding .bw root

### Highlights
Supports tool-specific model overrides with agent-level fallback. Default config tiers: opus for conductors, sonnet for workers, haiku for simple tasks

## Facts
- **config_module**: bw/core/config.py loads .bw/config.yaml and resolves model overrides for tool+agent combinations [project]
- **model_resolution**: Model resolution order: models.<tool>.<agent> -> models.<tool>.default -> None [project]
- **default_model_config**: Default config uses opus for conductor, product-conductor; sonnet for discovery/analysis/plan-writer/splitter/reviewer; haiku for worker [project]
