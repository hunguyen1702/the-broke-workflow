---
title: project_config
summary: Project config with pyproject.toml, data model, CLI commands, and unittest-based CLI regression tests
tags: []
related: [facts/project/test_framework_configuration.md]
keywords: []
createdAt: '2026-04-18T04:21:51.110Z'
updatedAt: '2026-05-12T17:15:36.663Z'
---
## Reason
Update project_config to fix outdated rule about test files

## Raw Concept
**Task:**
Document project configuration and testing infrastructure

**Changes:**
- Initial project configuration
- No test framework configured - known gap
- Added testing gap: No test framework configured
- Added testing gap as known gap - no test framework configured
- Updated to reflect unittest-based tests exist in tests/test_epic_flow.py
- No pytest dependency - tests use Python stdlib unittest
- Added tests/test_epic_flow.py with unittest-based CLI regression tests
- Updated CLAUDE.md to document testing commands
- pyproject.toml has no pytest dependency (optional gap)

**Files:**
- pyproject.toml
- tests/test_epic_flow.py
- CLAUDE.md

**Flow:**
CLI tests use Click CliRunner for integration testing

**Timestamp:** 2026-05-12

## Narrative
### Structure
Project config includes: pyproject.toml dependencies, .bw/ data model, CLI commands, source layout, and testing

### Dependencies
Python >=3.10, click, pyyaml

### Highlights
CLI regression tests in tests/test_epic_flow.py cover epic flow, step flow, plan status, and task tracking

### Rules
Testing gap: No pytest dependency in pyproject.toml - tests use Python stdlib unittest. Tests run with: python -m unittest tests.test_epic_flow -v

## Facts
- **test_files**: tests/test_epic_flow.py exists and provides unittest-based CLI regression coverage [project]
- **test_framework**: pyproject.toml has no pytest dependency - uses unittest from stdlib [project]
- **test_command**: Run tests with: python -m unittest tests.test_epic_flow -v [convention]
