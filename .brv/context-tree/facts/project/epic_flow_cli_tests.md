---
title: epic_flow_cli_tests
summary: Epic flow CLI tests using unittest and Click CliRunner for integration testing
tags: []
related: [facts/project/test_framework_configuration.md]
keywords: []
createdAt: '2026-05-12T17:11:40.446Z'
updatedAt: '2026-05-12T17:15:16.614Z'
---
## Reason
Document the epic flow CLI tests that provide regression coverage

## Raw Concept
**Task:**
Document epic flow CLI tests

**Changes:**
- Created tests/test_epic_flow.py with 7 unittest tests
- Tests cover: epic init, epic plan, epic status, plan status, step flow
- Created EpicFlowCliTests class with 7 test methods
- Tests verify: top-level help, epic subcommands, step flow, epic init, epic plan linking, epic status JSON, plan status JSON

**Files:**
- tests/test_epic_flow.py
- CLAUDE.md

**Flow:**
Tests use Click CliRunner.invoke() to test CLI commands end-to-end

**Timestamp:** 2026-05-12

**Author:** meowso

## Narrative
### Structure
EpicFlowCliTests class with 7 test methods covering epic lifecycle, plan linking, and status commands

### Dependencies
click.testing.CliRunner, unittest, json, pathlib

### Highlights
Tests verify that epic command replaces legacy product command, and that plan status uses epic key not product key

### Rules
Run: python -m unittest tests.test_epic_flow -v
