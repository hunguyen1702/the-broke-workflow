---
children_hash: a1981fa761cab832337176d6bcc8773b49665f2b135f76db3a084b2b92c483eb
compression_ratio: 0.11940158073014678
condensation_order: 1
covers: [bw_config_model_overrides.md, bw_config_module.md, bw_steps_module.md, bw_worktree_command.md, claude_code_work_adapter.md, codex_adapter.md, codex_adapter/_index.md, context.md, model_configuration_system.md, plan_cli_commands.md, product_cli_commands.md, product_flow_architecture.md, product_plan_workflow.md, project_config.md, step_cli_commands.md, task_cli_commands.md, task_frontmatter_fields.md, task_store_module.md, test_framework_configuration.md, the_broke_workflow_architecture.md, the_broke_workflow_project_config.md, triage_command.md, triage_command_integration.md, triage_flow.md, triager_agent.md, workflow_conventions.md]
covers_token_total: 10628
summary_level: d1
token_count: 1269
type: summary
---
<think>
This is a comprehensive collection of knowledge entries about "The Broke Workflow" project - a CLI-based workflow management system. I need to create a structural summary at level d1 that preserves key facts, architectural decisions, and relationships while compressing the content to ~20-30% of the original token count.

Let me organize the key information:

**Architecture Overview:**
- 9 core modules: config, frontmatter, lock, paths, slug, steps, task_store, templates, triage
- 10 CLI commands: config, doctor, init, install, plan, product, step, task, triage, worktree
- 10 agents: analysis, conductor, discovery, milestone-reviewer, milestone-splitter, plan-writer, product-conductor, splitter, triager, worker

**Two Workflow Flows:**
1. Plan Flow - 6 steps (requirements, discovery, analysis, write-plan, split-tasks, review)
2. Product Flow - 5 steps (requirements, summary, milestones, review, present)

**Model Configuration:**
- Model config in .bw/config.yaml
- Resolution: exact match → models.<tool>.default → tool natural default
- 9 agent model assignments: default(sonnet), conductor(opus), discovery(sonnet), analysis(sonnet), plan-writer(sonnet), splitter(sonnet), reviewer(sonnet), worker(sonnet), triager(haiku)

**Key CLI Commands:**
- bw plan: 7 subcommands (init, list, docs, read, finalize, remove, status)
- bw product: 9 subcommands (init, list, docs, read, finalize, plan, status, link, remove)
- bw task: 12 subcommands (add-dependency, claim, comment, comments, dag, deps, list, next, release, remove, show, status)
- bw step: 5 subcommands (list, show, agent, preamble, spawn)


- bw worktree: create/list/remove subcommands
- bw triage: classifies ideas as PLAN vs PRODUCT

**Triage System:**
- One-shot flow router for classifying user ideas
- Decision tree: Scope test → Knowledge test (for single) or Value-stream test (for multi)
- Outputs Agent(...) call that conductor executes

**Task Store:**
- Valid statuses: pending, in_progress, done
- Transitions: pending→in_progress, in_progress→done|pending, done is terminal
- Frontmatter fields: id, title, status, blocked_by, blocks, owner, claimed_at, effort

**Known Gaps:**
- Testing framework: No pytest or test dependencies configured
- Codex adapter: Deferred past MVP

**Project Config:**
- Python >=3.10
- Dependencies: click>=8.0, pyyaml>=6.0
- CLI entry: bw.cli:main
</think>

# Project: facts/project — The Broke Workflow

## Overview

The Broke Workflow is a CLI-based workflow management system with 9 core modules, 10 CLI commands, and 10 agents. It routes user ideas through either a PLAN or PRODUCT flow using a triage system.

## Architecture

**Core Modules (9):** config, frontmatter, lock, paths, slug, steps, task_store, templates, triage

**CLI Commands (10):** config, doctor, init, install, plan, product, step, task, triage, worktree

**Agents (10):** analysis, conductor, discovery, milestone-reviewer, milestone-splitter, plan-writer, product-conductor, splitter, triager, worker

## Two Workflow Flows

- **Plan Flow** (6 steps): requirements → discovery → analysis → write-plan → split-tasks → review
- **Product Flow** (5 steps): requirements → summary → milestones → review → present

Product flow uses Product Conductor agent; Plan flow uses standard Conductor.

## Model Configuration

Located in `.bw/config.yaml` with resolution order: `models.<tool>.<agent>` → `models.<tool>.default` → tool default. 9 agent assignments: conductor→opus, all others (discovery/analysis/plan-writer/splitter/reviewer/worker)→sonnet, triager→haiku.

## Key CLI Commands

- **bw plan** (7 subcommands): init, list, docs, read, finalize, remove, status
- **bw product** (9 subcommands): init, list, docs, read, finalize, plan, status, link, remove
- **bw task** (12 subcommands): add-dependency, claim, comment, comments, dag, deps, list, next, release, remove, show, status
- **bw step** (5 subcommands): list, show, agent, preamble, spawn
- **bw worktree** (3 subcommands): create, list, remove — stores under `.bw/worktrees/`, uses sparse-checkout
- **bw triage**: Classifies ideas as PLAN vs PRODUCT via decision tree

## Triage System

One-shot flow router using decision tree: **Scope test (A)** → determines single vs multi → **Knowledge test (B)** for single scope, **Value-stream test (C)** for multi. Outputs Agent(...) call for conductor to execute. Detects codebase via `.git/` + code files check.

## Task Store

Valid statuses: `{pending, in_progress, done}`. Transitions: `pending→in_progress`, `in_progress→done|pending`, done is terminal. Blocked state implicit via `blocked_by` field. Frontmatter fields: id, title, status, blocked_by, blocks, owner, claimed_at, effort.

## Known Gaps

- **Testing**: No pytest or test dependencies in pyproject.toml
- **Codex adapter**: Deferred past MVP

## Project Config

Python ≥3.10, click≥8.0, pyyaml≥6.0, CLI entry: `bw.cli:main`

---

**Drill-down entries:** See individual files in `facts/project/` for detailed CLI command specs, agent configurations, triage decision logic, and module documentation.