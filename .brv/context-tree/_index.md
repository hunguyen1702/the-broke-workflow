---
children_hash: 878ca5402981729a969989b475205a464e4f6b32c2002f56c1d089d7713d25c4
compression_ratio: 0.9987951807228915
condensation_order: 3
covers: [facts/_index.md]
covers_token_total: 830
summary_level: d3
token_count: 829
type: summary
---
## facts/_index.md
---
children_hash: adbc842128bcf90fca8ed3506304075577feae4266796a7a98552dcba1012a0e
compression_ratio: 0.5551523947750363
condensation_order: 2
covers: [context.md, project/_index.md]
covers_token_total: 1378
summary_level: d2
token_count: 765
type: summary
---
<think>
The user wants me to create a structural summary at level d1 from the provided knowledge entries. This is a summarization task - I need to condense the child entries into a structural overview while preserving key facts, relationships, and patterns.

Let me analyze the child entries and create a coherent summary.
</think>

# Project: The Broke Workflow - Structural Summary

The Broke Workflow is a Python CLI tool for structured project planning and task execution, featuring two distinct workflows (plan flow and product flow) with Claude Code and Codex adapters.

## Architecture Overview

The project consists of four main areas:
- **Core modules** (`bw/core/`): frontmatter, lock, paths, slug, task_store, templates
- **CLI commands** (`bw/commands/`): plan, task, product, step, config, doctor, init, install
- **Agents** (`agents/`): conductor, discovery, analysis, plan-writer, splitter, reviewer, worker, plus product-conductor, milestone-splitter, milestone-reviewer
- **Adapters** (`adapters/`): Claude Code (6 slash-commands) and Codex (deferred past MVP)

**Entry point**: `bw = bw.cli:main` | **Python**: >=3.10 | **Deps**: click>=8.0, pyyaml>=6.0 | **Build**: setuptools with setuptools-scm

**Known Gap**: No test framework configured (no pytest in dependencies)

## CLI Commands

### Task Commands
13 subcommands: list, next, show, claim, release, status, deps, dag, add-dependency, comment, comments, remove

### Product Commands
9 subcommands: init, list, docs, read, finalize, plan, status, link, remove

### Step Commands
5 subcommands: list, show, agent, preamble, spawn

### Claude Code Integration
6 slash-commands: `/plan` (6-step), `/product` (5-step), `/split`, `/next`, `/work`, `/status`

## Task Model

**Status Flow**: `pending → in_progress → done` (simplified from 5 to 3 statuses)

**Valid Transitions**: pending→in_progress, in_progress→{done,pending}, done is terminal

**Blocked state** is implicit via `blocked_by` dependencies, not an explicit status

**Frontmatter fields**: id, status, owner, blocked_by, blocks, claimed_at, effort

**Task ID format**: `{plan-slug}/{nnn}-{task-slug}`

## Workflows

### Plan Flow (6 steps)
Requirements → Discovery → Analysis → Write Plan → Split Tasks → Review

### Product Flow (5 steps)
Requirements → Summary → Milestones → Review → Present

Product flow managed by Product Conductor agent, with milestone-splitter and milestone-reviewer as sub-agents.

## Model Configuration

Located in `.bw/config.yaml` with resolution order:
1. Exact match: `models.<tool>.<agent>`
2. Default: `models.<tool>.default`
3. Tool natural default

Default: sonnet | Conductor: opus | All others: sonnet

## Key Relationships

- `cli_tool_integrations.md` → links to codex_adapter, workflow_architecture
- `product_flow_architecture.md` → links to workflow_architecture
- `product_cli_commands.md` → links to product_plan_workflow, cli_tool_integrations
- `task_store_module.md` → links to project_config
- `claude_co
[summary compaction; truncated from 830 tokens]