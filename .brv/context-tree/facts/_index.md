---
children_hash: 2bf1ca0e562c13390770e42a72c0a01ff7fd4e7e2295ccb9ac9389910b84f7a7
compression_ratio: 0.9427570093457944
condensation_order: 2
covers: [project/_index.md]
covers_token_total: 856
summary_level: d2
token_count: 807
type: summary
---
<think>
The user is asking me to create a structural summary at level d1 from the provided knowledge entries. Let me analyze these entries and create a concise summary that preserves key facts, architectural decisions, and relationships while referencing entry names for drill-down.

Looking at the context tree structure provided, I can see there are various entries about:
- CLI tool integrations
- Codex adapter
- Project config
- Task frontmatter fields
- Task store module
- Test framework configuration
- The broke workflow architecture
- Project config
- Workflow conventions

The user wants me to create a d1 level summary. Looking at the structure, d1 would be the domain level (like `facts/project/`). So I need to create a summary that groups these related entries together.

Let me craft a concise, well-structured summary that:
1. Has a brief overview
2. Groups related entries into logical sections
3. Preserves key facts
4. References entry names for drill-down
5. Uses proper formatting with headings and bullet points
</think>

# Project Knowledge Summary

## Overview

The broke workflow is a pure Python CLI tool providing a 6-step playbook for task planning and execution. It integrates with Claude Code and Codex via adapter patterns, with no external dependencies beyond Python's standard library.

## Architecture

**Core Components:**
- **CLI Commands** (`bw/commands/`) — plan, task, doctor, init, install, config
- **Core Modules** (`bw/core/`) — frontmatter, lock, paths, slug, steps, task_store, templates
- **Agents** (`agents/`) — 6 sub-agents: conductor, discovery, analysis, plan-writer, splitter, worker
- **Adapters** (`adapters/`) — Claude Code and Codex integrations

**6-Step Playbook:** requirements → discovery → analysis → write-plan → split-tasks → review

→ See: `the_broke_workflow_architecture.md`

## CLI Tool Integrations

- **Claude Code**: 5 slash-commands (plan, split, next, work, status) using skill/command format — implemented
- **Codex**: Uses AGENTS.md convention — deferred past MVP

Both shell out to `bw` CLI. Deployment: `bw install --tool <name> --scope project/global`

→ See: `cli_tool_integrations.md`, `codex_adapter.md`

## Project Configuration

- Python >=3.10, click >=8.0, pyyaml >=6.0
- Build: setuptools >=68.0 with setuptools-scm for versioning
- Entry: `bw = bw.cli:main`

→ See: `project_config.md`, `the_broke_workflow_project_config.md`

**Known Gap:** No test framework configured (no pytest in dependencies, no test files)

→ See: `test_framework_configuration.md`

## Task System

**Task ID Format:** `{plan-slug}/{nnn}-{task-slug}` (e.g., `auth-feature-x7k2/001-add-user-model`)

**Frontmatter Fields:** id, title, status, blocked_by, blocks, owner, claimed_at, effort

**Status Machine:** `pending → ready/in_progress → done`, with `blocked` as intermediate state

**Valid Statuses:** pending, ready, in_progress, blocked, done (terminal)

→ See: `task_store_module.md`, `task_frontmatter_fields.md`, `workflow_conventions.md`

## Workflow Conventions

- Python naming: snake_case
- Sub-agents: receive minimal context (slug, read, write, return instructions only)
- Context principle: fresh context = lean context

→ See: `workflow_conventions.md`