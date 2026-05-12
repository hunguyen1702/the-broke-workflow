---
title: Test Framework Configuration
summary: 'Testing: unittest-based tests exist in tests/test_epic_flow.py (7 tests), no pytest dependency'
tags: []
related: [facts/project/project_config.md]
keywords: []
createdAt: '2026-04-18T04:24:32.706Z'
updatedAt: '2026-05-12T17:11:40.425Z'
---
## Reason
Update to reflect unittest tests now exist in tests/test_epic_flow.py

## Raw Concept
**Task:**
Document testing configuration with unittest-based regression tests

**Changes:**
- Identified missing test framework configuration
- Added unittest-based regression tests in tests/test_epic_flow.py
- Test command: python -m unittest tests.test_epic_flow -v
- No pytest dependency in pyproject.toml (optional gap)

**Files:**
- pyproject.toml
- tests/test_epic_flow.py
- CLAUDE.md

**Flow:**
Tests use Click CliRunner for integration testing of CLI commands

**Timestamp:** 2026-05-12

**Author:** meowso

## Narrative
### Structure
unittest-based CLI integration tests in tests/ directory

### Dependencies
Python stdlib unittest, click.testing.CliRunner

### Highlights
7 tests in EpicFlowCliTests class covering epic CLI commands. Uses isolated_filesystem() for test isolation.

### Rules
Rule 1: Tests must pass before merging
Rule 2: Run: python -m unittest tests.test_epic_flow -v

## Facts
- **test_framework**: Test framework: unittest (Python stdlib) [project]
- **test_files**: Test file exists: tests/test_epic_flow.py [project]
- **test_count**: Test count: 7 tests [project]
- **test_command**: Test command: python -m unittest tests.test_epic_flow -v [project]
- **pytest_dependency**: No pytest dependency in pyproject.toml [project]
