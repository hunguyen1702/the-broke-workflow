---
title: Project Config
summary: 'Project config: Python >=3.10, click & pyyaml deps, bw CLI, NO test framework (known gap)'
tags: []
keywords: []
importance: 86
recency: 1
maturity: core
accessCount: 7
updateCount: 3
createdAt: '2026-04-18T04:21:51.110Z'
updatedAt: '2026-04-18T04:24:04.003Z'
---
## Reason
Update project config with testing gap as known gap

## Raw Concept
**Task:**
Document project configuration including known gaps

**Changes:**
- Initial project configuration
- No test framework configured - known gap
- Added testing gap: No test framework configured
- Added testing gap as known gap - no test framework configured

**Files:**
- pyproject.toml

**Flow:**
pyproject.toml defines project metadata, dependencies, build system, and CLI entry point

**Timestamp:** 2026-04-18

## Narrative
### Structure
pyproject.toml defines project metadata, dependencies, and CLI entry point

### Dependencies
Python >=3.10 required

### Highlights
No test framework configured - known gap. Dependencies: click>=8.0, pyyaml>=6.0. CLI: bw.cli:main

### Rules
Testing gap: No test framework (pytest) configured in dependencies. No test files exist in the codebase.

## Facts
- **test_framework**: No test framework configured [project]
- **dependencies**: Dependencies: click>=8.0, pyyaml>=6.0 [project]
- **python_version**: Python >=3.10 required [project]
- **cli_entry**: CLI entry: bw.cli:main [project]
