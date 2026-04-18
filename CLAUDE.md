# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

**the-broke-workflow** is a personal agent-coding workflow toolkit. It runs a 6-step planning process (Requirements → Discovery → Analysis → Write Plan → Split Tasks → Review), using a conductor that delegates heavy work to fresh sub-agents. Plans and tasks are stored as markdown files in `.bw/`.

## Requirements

- Python `>=3.10`
- `pip install -e .` to install

## CLI Commands

```bash
# Setup
pip install -e .

# Plan lifecycle
bw plan init "<title>"        # Create new plan from templates
bw plan list                  # List all plans
bw plan read <slug> <doc>     # Print a document (plan|discovery|analysis)
bw plan docs <slug>           # List documents in a plan
bw plan finalize <slug>       # Freeze plan and create tasks/ directory

# Task lifecycle
bw task list                  # List all tasks (--plan, --status filters)
bw task next                  # Show ready tasks (unblocked, unclaimed)
bw task show <id>             # Print a task file
bw task claim <id> --owner X  # Atomically claim a task
bw task status <id> <status>   # Update status (pending|in_progress|done|blocked|ready)
bw task dag                   # Render task DAG as ASCII (--plan filter)
bw task deps <id>             # Show blockers and blocks for a task
bw task release <id>          # Drop claim on a task

# Other commands
bw doctor                     # Check installation
bw init                       # Initialize .bw structure
bw install <agent-type>       # Install adapter
bw config                     # Configure settings
```

## Architecture

```
.bw/                          # Workflow data root (created by bw init)
  plans/<slug>/               # Per-plan documents
    plan.md
    discovery-report.md
    analysis-report.md
  tasks/<slug>/               # Task files (created by bw plan finalize)
    001-<task>.md
    002-<task>.md
  archive/                    # Completed plans archived here

steps/                        # 6-step conductor playbook
  step-01-requirements.md
  step-02-discovery.md
  step-03-analysis.md
  step-04-write-plan.md
  step-05-split-tasks.md
  step-06-review.md

agents/                       # Sub-agent definitions
  conductor.md                # Main orchestrator — reads steps/, delegates
  discovery.md                # Codebase exploration sub-agent
  analysis.md                 # Approach scoring sub-agent
  plan-writer.md              # Plan synthesis sub-agent
  splitter.md                 # Task decomposition sub-agent
  worker.md                  # Task execution sub-agent

adapters/
  claude-code/                # Claude Code /slash-command integrations
    plan.md  split.md  next.md  work.md  status.md
  codex/                      # Codex MCP integration

bw/
  core/                       # frontmatter, lock, paths, slug, task_store, templates
  commands/                    # plan_cmd, task_cmd, config/doctor/init/install

templates/                    # Shared document templates
  plan.md  discovery-report.md  analysis-report.md  task.md
```

## Key Patterns

**Conductor rules:**
- Never craft file paths — use `bw plan read {slug} <doc>` exclusively
- Never craft `ls` or `cat` — use the CLI
- HALTs at interactive checkpoints (Step 1 confirmation, Step 3 approach pick, Step 4 review, Step 5 spot-check)
- Auto-proceeds between steps after showing results
- Keep sub-agent context lean — give only what they need to act

**Plan document access:**
```
bw plan read {slug} plan       → .bw/plans/{slug}/plan.md
bw plan read {slug} discovery  → .bw/plans/{slug}/discovery-report.md
bw plan read {slug} analysis   → .bw/plans/{slug}/analysis-report.md
```

**Task IDs:** `{plan-slug}/{nnn}-{task-slug}` (e.g. `auth-feature-x7k2/001-add-user-model`)

**Sub-agent spawning:** Give each sub-agent: the slug, what to read, what to write, what to return. Fresh context = lean context.

**Workflow statuses:** `pending` → `in_progress` → `done`, with `blocked` and `ready` as intermediate states.

## Conductor Behavior

The conductor runs a 6-step flow and **HALTs** at these checkpoints:
- **Step 1** — After gathering requirements, HALTs for user confirmation before creating the plan
- **Step 3** — After presenting decision cards, HALTs for user to pick an approach
- **Step 4** — After presenting the written plan, HALTs for user review before finalizing
- **Step 5** — After presenting the task list + DAG, HALTs for user spot-check before closing

Between HALTs, the conductor auto-proceeds. "HALTs" = wait for explicit user input; do not proceed automatically.

## Adapter Pattern

Adapters in `adapters/<name>/` provide `/slash-command` integrations for specific agent tools. Each adapter has its own markdown files (like `plan.md`, `work.md`) that define the agent's behavior when that command is invoked.
