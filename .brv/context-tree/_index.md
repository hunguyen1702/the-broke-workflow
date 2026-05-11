---
children_hash: e71cbb868529dc90b574ec09dc9db2a31e169e572c6cd78d2b78adb00c0fd7d3
compression_ratio: 0.9207920792079208
condensation_order: 3
covers: [facts/_index.md]
covers_token_total: 1111
summary_level: d3
token_count: 1023
type: summary
---
<think>
The user is asking me to create a structural summary at the domain level (d1) from the provided child entries. I need to synthesize the information from the child entries into a condensed, authoritative summary of the "The Broke Workflow Project" domain.

Let me analyze the child entries and create a summary:

**Key facts from the entries:**
- The broke workflow (bw) is a Python CLI tool for workflow and task management
- Has adapters for Claude Code and Codex AI assistants
- 9 core modules in bw/core/
- 9 CLI commands
- 9 agents
- 2 adapters (Claude Code with 6 slash-commands, Codex deferred)
- Plan flow: 6 steps
- Product flow: 5 steps
- Task status flow: pending → in_progress → done
- Task IDs: {plan-slug}/{nnn}-{task-slug}
- Configuration with model overrides
- Known gaps: no test framework, dead config key (reviewer)

The user wants me to output ONLY the summary text without using any tools. This appears to be a direct output request.
</think>

# Domain: The Broke Workflow Project

## Overview
The broke workflow (bw) is a Python CLI tool for workflow and task management, with adapters for Claude Code and Codex AI assistants.

## Architecture

**Core Components:**
- **9 Core Modules** in `bw/core/`: frontmatter, lock, paths, slug, task_store, templates, config, steps, paths
- **9 CLI Commands**: plan, task, doctor, init, install, config, product, step, worktree
- **9 Agents**: conductor, discovery, analysis, plan-writer, splitter, worker, product-conductor, milestone-splitter, milestone-reviewer
- **2 Adapters**: Claude Code (6 slash-commands), Codex (deferred past MVP)

**Details**: See `the_broke_workflow_architecture.md`, `the_broke_workflow_project_config.md`

## CLI Commands

### Task Commands (12 subcommands)
`add-dependency`, `claim`, `comment`, `comments`, `dag`, `deps`, `list`, `next`, `release`, `remove`, `show`, `status`

### Plan Commands (7 subcommands)
`init`, `list`, `docs`, `read`, `finalize`, `status`, `remove`

### Product Commands (9 subcommands)
`init`, `list`, `docs`, `read`, `finalize`, `plan`, `status`, `link`, `remove`

### Step Commands (5 subcommands)
`list`, `show`, `agent`, `preamble`, `spawn`

### Worktree Commands (3 subcommands)
`create`, `list`, `remove`

**Details**: See `task_cli_commands.md`, `plan_cli_commands.md`, `product_cli_commands.md`, `step_cli_commands.md`, `bw_worktree_command.md`

## Workflow Flows

**Plan Flow**: 6 steps (requirements → discovery → analysis → write-plan → split-tasks → review)

**Product Flow**: 5 steps (requirements → summary → milestones → review → present), managed by product-conductor agent with milestone-splitter and milestone-reviewer sub-agents

**Details**: See `product_flow_architecture.md`, `product_plan_workflow.md`

## Task Model

**Status Flow**: `pending → in_progress → done` (simplified from 5 to 3 statuses)
- Blocked state is implicit via `blocked_by` dependencies
- Task IDs: `{plan-slug}/{nnn}-{task-slug}`

**Details**: See `task_store_module.md`, `workflow_conventions.md`, `task_frontmatter_fields.md`

## Configuration

- **Model Config**: `.bw/config.yaml` with per-tool per-agent overrides
- **Resolution Order**: `models.<tool>.<agent>` → `models.<tool>.default` → tool default
- **Default Models**: opus for conductors, sonnet for workers, haiku for simple tasks
- **Config Module**: `bw/core/config.py` provides `load_config()`, `resolve_model()`

**Details**: See `bw_config_module.md`, `model_configuration_system.md`, `bw_config_model_overrides.md`

## Adapters

**Claude Code Adapter**: 6 slash-commands (`/next`, `/plan`, `/product`, `/split`, `/status`, `/work`)

**Codex Adapter**: Deferred past MVP

**Details**: See `cli_tool_integrations.md`, `codex_adapter.md`, `claude_code_work_adapter.md`

## Known Gaps

- **No test framework**: pyproject.toml lacks pytest/test dependencies, no test files exist
- **Dead code**: `reviewer` config key has no corresponding `agents/reviewer.md` file (only `milestone-reviewer.md` exists)

**Details**: See `project_config.md`, `test_framework_configuration.md`, `bw_config_model_overrides.md`