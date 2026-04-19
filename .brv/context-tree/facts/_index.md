---
children_hash: 1c9647b7bc56d359af86609a4499ac1469a6fda5524116b22194a406800b09e5
compression_ratio: 0.8282608695652174
condensation_order: 2
covers: [project/_index.md]
covers_token_total: 1380
summary_level: d2
token_count: 1143
type: summary
---
<think>
The user has provided a structured overview of the "facts/project" domain and wants me to output only the summary text without using any tools. Let me review the key information they've provided:

1. **Overview**: The Broke Workflow (TBW) is a CLI tool for AI-augmented product and implementation planning with two workflow flows.

2. **Core Architecture**: 
   - `bw/core/` - Python modules
   - `bw/commands/` - CLI commands
   - `agents/` - Agent definitions
   - `adapters/` - Tool integrations

3. **Configuration**: Python >= 3.10, click >= 8.0, pyyaml >= 6.0. No test framework.

4. **CLI Command Systems**:
   - Product CLI: bw product init | list | docs | read | finalize
   - Step CLI: bw step list | show | agent | preamble | spawn
   - Claude Code Integration: 6 slash-commands

5. **Workflow Flows**:
   - Plan Flow: 6 steps
   - Product Flow: 5 steps with HALTs

6. **Model Configuration**: Resolution order system with overrides

7. **Task Management**: Task store module and frontmatter fields

8. **Key Relationships**: Various connections between components

9. **Known Gaps**: No testing, Codex adapter deferred

I need to output this as a clean, consolidated summary. The user wants ONLY the summary text, no tools, no code blocks, no markdown formatting unless appropriate for the text itself.
</think>

# Domain: facts/project — Structural Summary

## Overview
The Broke Workflow (TBW) is a CLI tool for AI-augmented product and implementation planning. It provides two distinct workflow flows managed through a modular architecture of core Python modules, CLI commands, agent definitions, and tool adapters.

## Core Architecture

**Project Structure** (see `the_broke_workflow_architecture.md`):
- `bw/core/` — Python modules: frontmatter, lock, paths, slug, task_store, templates
- `bw/commands/` — CLI commands: plan, task, step, product, doctor, init, install, config
- `agents/` — Agent definitions: conductor, discovery, analysis, plan-writer, splitter, reviewer, worker, product-conductor, milestone-splitter, milestone-reviewer
- `adapters/` — Tool integrations: claude-code (6 slash-commands), codex (deferred)

**Configuration** (see `the_broke_workflow_project_config.md`):
- Python >= 3.10, click >= 8.0, pyyaml >= 6.0
- CLI entry: `bw.cli:main`
- **KNOWN GAP**: No test framework configured

## CLI Command Systems

**Product CLI** (`product_cli_commands.md`): `bw product init | list | docs | read | finalize`
- Manages product plan lifecycle (create, query, freeze)
- Short doc names: requirements → product-plan.md, milestones → milestones.md

**Step CLI** (`step_cli_commands.md`): `bw step list | show | agent | preamble | spawn`
- Drives 6-step plan flow execution
- spawn outputs Agent() calls with model config

**Claude Code Integration** (`cli_tool_integrations.md`): 6 slash-commands
- plan (6-step implementation flow)
- product (5-step product flow)
- split, next, work, status

## Workflow Flows

**Plan Flow** (`product_flow_architecture.md`): 6 steps, 6 agents
- requirements → discovery → analysis → write plan → split tasks → review

**Product Flow** (`product_plan_workflow.md`): 5 steps
- requirements (JTBD interview) → summary (HALT) → milestones (sub-agent) → review (sub-agent) → present (HALT)
- Orchestrated by Product Conductor; sub-agents: milestone-splitter, milestone-reviewer
- Uses HALTs at interactive checkpoints for user approval

## Model Configuration

**System** (`model_configuration_system.md`): Resolution order
1. Exact match: `models.<tool>.<agent>`
2. Tool default: `models.<tool>.default`
3. Natural default

**Overrides** (`bw_config_model_overrides.md`):
- default: claude-sonnet-4-20250514
- conductor: opus
- all others: sonnet

## Task Management

**Task Store** (`task_store_module.md`): Python module for scanning and state management
- Statuses: pending → ready/in_progress → done (blocked is intermediate)
- Task ID format: `{plan-slug}/{nnn}-{task-slug}`

**Frontmatter Fields** (`task_frontmatter_fields.md`):
- id, title, status, blocked_by, blocks, owner, claimed_at, effort

## Key Relationships

- Product flow ↔ Product CLI commands (init, read, finalize)
- Step flow ↔ Step CLI commands (spawn with model config)
- Claude Code adapter ↔ 6 slash-commands in adapters/claude-code/
- Codex adapter (deferred) ↔ relies on claude-code as reference
- Model config ↔ bw step spawn (outputs Agent() with correct model)

## Known Gaps

- **Testing**: No pytest or test dependencies in pyproject.toml; no test files exist
- **Codex Adapter**: Deferred past MVP (version 0.1.0)