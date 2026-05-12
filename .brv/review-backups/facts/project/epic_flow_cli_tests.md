---
title: Epic Flow CLI Tests
summary: 7 unittest-based CLI integration tests in tests/test_epic_flow.py covering epic commands
tags: []
related: [facts/project/test_framework_configuration.md]
keywords: []
createdAt: '2026-05-12T17:11:40.446Z'
updatedAt: '2026-05-12T17:11:40.446Z'
---
## Reason
Document the unittest-based CLI regression tests for epic flow

## Raw Concept
**Task:**
Document epic flow CLI integration tests

**Changes:**
- Created tests/test_epic_flow.py with 7 unittest tests
- Tests cover: epic init, epic plan, epic status, plan status, step flow

**Files:**
- tests/test_epic_flow.py
- CLAUDE.md

**Flow:**
Tests use Click CliRunner to invoke CLI commands and assert outputs

**Timestamp:** 2026-05-12

**Author:** meowso

## Narrative
### Structure
tests/test_epic_flow.py contains EpicFlowCliTests class with 7 test methods

### Dependencies
unittest (Python stdlib), click.testing.CliRunner

### Highlights
7 tests pass. Tests use isolated_filesystem() for test isolation. Helper functions: _init_project, _write_milestones, _only_plan_dir.

### Rules
Run: python -m unittest tests.test_epic_flow -v

## Facts
- **test_file**: Test file: tests/test_epic_flow.py [project]
- **test_class**: Test class: EpicFlowCliTests [project]
- **test_count**: Number of tests: 7 [project]
- **test_framework**: Test framework: unittest [project]
- **test_status**: All tests pass [project]
