---
children_hash: 5816b73f6c06d814b39c8c89d27cf58e06553bbdb196f1d7d817ebddc9f2bbd6
compression_ratio: 0.18161468437546635
condensation_order: 1
covers: [bw_config_model_overrides.md, cli_tool_integrations.md, codex_adapter.md, context.md, model_configuration_system.md, product_cli_commands.md, product_flow_architecture.md, product_plan_workflow.md, project_config.md, step_cli_commands.md, task_frontmatter_fields.md, task_store_module.md, test_framework_configuration.md, the_broke_workflow_architecture.md, the_broke_workflow_project_config.md, workflow_conventions.md]
covers_token_total: 6701
summary_level: d1
token_count: 1217
type: summary
---
<think>
The user wants me to create a structural summary of the provided knowledge entries at level d1 (domain level). I need to consolidate the information from these child entries into a concise overview that preserves key facts, architectural decisions, and relationships.

Let me analyze the entries:

1. **Architecture**: the_broke_workflow_architecture.md - CLI tool with core modules, commands, agents, adapters
2. **Config**: project_config.md, the_broke_workflow_project_config.md - Python >=3.10, click, pyyaml, no tests
3. **CLI Commands**: 
   - step_cli_commands.md - bw step CLI (list, show, agent, preamble, spawn)
   - product_cli_commands.md - bw product CLI (init, list, docs, read, finalize)
   - cli_tool_integrations.md - Claude Code adapters with 6 slash-commands
4. **Model Config**: bw_config_model_overrides.md, model_configuration_system.md - model overrides system
5. **Workflows**: 
   - product_flow_architecture.md - Two flows: plan (6 steps) and product (5 steps)
   - product_plan_workflow.md - 5-step CLI-guided product planning
   - workflow_conventions.md - task IDs, YAML frontmatter, status machine
6. **Tasks**: task_store_module.md, task_frontmatter_fields.md - task management
7. **Adapters**: codex_adapter.md - deferred past MVP
8. **Testing**: test_framework_configuration.md - known gap, no tests

Key relationships:
- Product flow uses bw product CLI commands
- Step flow uses bw step CLI commands
- Claude Code has 6 slash-commands
- Model config system provides per-tool per-agent overrides
- Task store handles task scanning and status validation

Let me create a clean structural summary.
</think>

# Domain: facts/project

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