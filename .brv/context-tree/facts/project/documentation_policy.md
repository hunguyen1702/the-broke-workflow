---
title: Documentation Policy
summary: README=overview, CLAUDE.md=canonical guide (CLI, epic hierarchy, data model, adapters, config, tests), AGENTS.md references CLAUDE.md
tags: []
related: []
keywords: []
createdAt: '2026-05-12T16:40:41.201Z'
updatedAt: '2026-05-12T16:40:41.201Z'
---
## Reason
Documenting updated single-source-of-truth policy for repository docs

## Raw Concept
**Task:**
Document repository documentation single-source-of-truth policy

**Changes:**
- README.md is now a short user-facing overview
- CLAUDE.md is the canonical detailed guide for CLI surface, epic hierarchy, data model, adapters, config, and tests
- AGENTS.md now references CLAUDE.md instead of duplicating command lists
- AGENTS.md keeps ByteRover runtime rules

**Files:**
- README.md
- CLAUDE.md
- AGENTS.md

**Timestamp:** 2026-05-12

## Narrative
### Structure
Three-tier documentation: README (overview), CLAUDE.md (detailed canonical guide), AGENTS.md (runtime rules + references CLAUDE.md)

### Highlights
Single-source-of-truth policy eliminates duplication between documentation files

## Facts
- **doc_source_of_truth**: CLAUDE.md is the canonical source for CLI commands, epic hierarchy, data model, adapters, config, and tests [convention]
- **readme_purpose**: README.md provides short user-facing overview only [convention]
- **agents_purpose**: AGENTS.md contains ByteRover runtime rules and references CLAUDE.md [convention]
