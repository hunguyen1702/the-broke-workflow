---
children_hash: 71058e31fb3cc9337e69e3c89b2fca4629b25cefb73abedec5f6d085b277d9e9
compression_ratio: 0.18777180864671272
condensation_order: 1
covers: [cli_tool_integrations.md, codex_adapter.md, context.md, project_config.md, task_frontmatter_fields.md, task_store_module.md, test_framework_configuration.md, the_broke_workflow_architecture.md, the_broke_workflow_project_config.md, workflow_conventions.md]
covers_token_total: 3909
summary_level: d1
token_count: 734
type: summary
---
<think>
The user wants me to create a structural summary at level d1 from the provided knowledge entries. Let me analyze these entries and create a concise summary that preserves key facts, architectural decisions, and relationships while referencing entry names for drill-down.

Key themes I see across these entries:
1. Project architecture - CLI tool with core modules, commands, agents, adapters
2. CLI tool integrations - Claude Code (slash-commands) and Codex (deferred)
3. Project configuration - Python >=3.10, click, pyyaml, known gap: no test framework
4. Task system - task_store module, frontmatter fields, status transitions
5. Workflow conventions - task IDs, status machine, sub-agent instructions

Let me create a structured summary that groups these logically and references the entry names.
</think>

# The Broke Workflow - Project Summary

## Overview
The broke workflow is a pure Python CLI tool (no external dependencies) that provides a 6-step playbook for planning and executing tasks. It integrates with Claude Code and Codex via adapter patterns.

## Architecture

The project has 4 main components:

- **Core** (`bw/core/`) - Python modules: frontmatter, lock, paths, slug, task_store, templates
- **Commands** (`bw/commands/`) - CLI commands: plan, task, doctor, init, install, config
- **Agents** (`agents/`) - 6 agents: conductor, discovery, analysis, plan-writer, splitter, worker
- **Adapters** (`adapters/`) - Claude Code and Codex integrations

The 6-step playbook: requirements → discovery → analysis → write plan → split tasks → review

## CLI Tool Integrations

See: `cli_tool_integrations.md`, `codex_adapter.md`

- **Claude Code**: Uses skill/command format with 5 slash-commands (plan, split, next, work, status) - implemented
- **Codex**: Uses AGENTS.md convention - deferred past MVP

Both adapters shell out to the `bw` CLI. Deployment: `bw install --tool <name> --scope project/global`

## Project Configuration

See: `project_config.md`, `the_broke_workflow_project_config.md`

- Python >=3.10, click >=8.0, pyyaml >=6.0
- Build: setuptools >=68.0 with setuptools-scm for versioning
- Entry: `bw = bw.cli:main`
- **KNOWN GAP**: No test framework configured (no pytest in dependencies, no test files)

## Task System

See: `task_store_module.md`, `task_frontmatter_fields.md`, `workflow_conventions.md`

**Task ID format**: `{plan-slug}/{nnn}-{task-slug}` (e.g., `auth-feature-x7k2/001-add-user-model`)

**Frontmatter fields**: id, title, status, blocked_by, blocks, owner, claimed_at, effort

**Status machine**: `pending → ready/in_progress → done`, with `blocked` as intermediate state

**Valid statuses**: pending, ready, in_progress, blocked, done (done is terminal)

## Workflow Conventions

See: `workflow_conventions.md`

- Python: snake_case naming
- Sub-agents: receive minimal context (slug, read, write, return instructions only)
- Context principle: fresh context = lean context