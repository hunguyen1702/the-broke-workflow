---
children_hash: 55e142bba86df086e61a85f5a910a153d4b7a59e515297e16c94796f81ea6b01
compression_ratio: 0.15037396667104055
condensation_order: 1
covers: [bw_config_model_overrides.md, claude_code_work_adapter.md, cli_tool_integrations.md, codex_adapter.md, context.md, model_configuration_system.md, product_cli_commands.md, product_flow_architecture.md, product_plan_workflow.md, project_config.md, step_cli_commands.md, task_cli_commands.md, task_frontmatter_fields.md, task_store_module.md, test_framework_configuration.md, the_broke_workflow_architecture.md, the_broke_workflow_project_config.md, workflow_conventions.md]
covers_token_total: 7621
summary_level: d1
token_count: 1146
type: summary
---
<think>
The user wants me to create a structural summary at level d1 from the provided knowledge entries. This is a summarization task - I need to condense the child entries into a structural overview while preserving key facts, relationships, and patterns.

Let me analyze the child entries:

1. **bw_config_model_overrides.md** - Model overrides in config.yaml (sonnet default, opus for conductor)
2. **claude_code_work_adapter.md** - Work adapter for task execution with 5 key rules
3. **cli_tool_integrations.md** - 6 Claude Code slash-commands
4. **codex_adapter.md** - Deferred past MVP
5. **context.md** - Topic overview for project
6. **model_configuration_system.md** - Per-tool per-agent model overrides
7. **product_cli_commands.md** - 9 product subcommands
8. **product_flow_architecture.md** - Two workflow flows (plan: 6 steps, product: 5 steps)
9. **product_plan_workflow.md** - CLI-guided product planning
10. **project_config.md** - Python >=3.10, click, pyyaml, NO test framework
11. **step_cli_commands.md** - bw step CLI with list, show, agent, preamble, spawn
12. **task_cli_commands.md** - Task lifecycle commands
13. **task_frontmatter_fields.md** - Task template fields
14. **task_store_module.md** - Task scanning and state management
15. **test_framework_configuration.md** - Known gap: no test framework
16. **the_broke_workflow_architecture.md** - CLI tool with core modules, commands, agents, adapters
17. **the_broke_workflow_project_config.md** - Project config with known gap
18. **workflow_conventions.md** - Status flow: pending → in_progress → done


19. **bw_config_model_overrides.md** - Model overrides in config.yaml (sonnet default, opus for conductor)

Now I can structure this into a coherent summary covering the architecture, CLI integrations, task management, product workflow, and configuration system.
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
- `claude_code_work_adapter.md` → links to cli_tool_integrations, task_store_module