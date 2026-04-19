# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

**the-broke-workflow** is a personal agent-coding workflow toolkit. It supports two flows:
- **Plan flow** (6 steps): Requirements → Discovery → Analysis → Write Plan → Split Tasks → Review
- **Product flow** (5 steps): Requirements → Summary → Milestones → Review → Present

Both use a conductor that delegates heavy work to fresh sub-agents. Plans and tasks are stored as markdown files in `.bw/`.

## Requirements

- Python `>=3.10`
- `pip install -e .` to install

## CLI Commands

```bash
# Setup
pip install -e .

# Step flow (conductor uses these to navigate the plan flow)
bw step list                  # List all 6 steps
bw step show <N> <slug>       # Output conductor instructions for step N
bw step agent <N> <slug>      # Output sub-agent instructions (sub-agent self-bootstraps)
bw step preamble <slug>       # Output conductor rules

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

# Step flow (conductor uses these to navigate the plan flow)
bw step list                  # List all steps as slug names
bw step show <step> <slug>     # Output conductor instructions (step: number or name)
bw step agent <step> <slug>    # Output sub-agent instructions
bw step spawn <step> <slug> --tool <tool>  # Output Agent(...) call with model
bw step preamble <slug>       # Output conductor rules
# All step commands accept --flow (plan|product) to switch flows (default: plan)

# Product plan lifecycle (5-step flow: requirements → summary → milestones → review → present)
bw product init "<title>"     # Create a new product plan from templates
bw product list               # List all product plans
bw product docs <slug>        # List documents in a product plan
bw product read <slug> <doc>  # Print a document (requirements|milestones)
bw product finalize <slug>   # Freeze product plan status
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

steps/                        # Conductor playbook (content source, read by CLI)
  step-01-requirements.md     # Plan flow: 6 steps
  step-02-discovery.md
  step-03-analysis.md
  step-04-write-plan.md
  step-05-split-tasks.md
  step-06-review.md
  product-step-01-requirements.md  # Product flow: 5 steps
  product-step-02-summary.md
  product-step-03-milestones.md
  product-step-04-review.md
  product-step-05-present.md

agents/                       # Sub-agent definitions (content source, read by CLI)
  conductor.md                # Plan conductor preamble (rules, setup)
  product-conductor.md        # Product conductor preamble
  discovery.md                # Codebase exploration sub-agent
  analysis.md                 # Approach scoring sub-agent
  plan-writer.md              # Plan synthesis sub-agent
  splitter.md                 # Task decomposition sub-agent
  milestone-splitter.md       # Milestone decomposition sub-agent
  milestone-reviewer.md       # Milestone review sub-agent
  worker.md                   # Task execution sub-agent

adapters/
  claude-code/                # Claude Code /slash-command integrations
    plan.md  split.md  next.md  work.md  status.md  product.md
  codex/                      # Codex MCP integration

bw/
  core/                       # frontmatter, lock, paths, slug, steps, task_store, templates
  commands/                   # plan_cmd, product_cmd, step_cmd, task_cmd, config/doctor/init/install

templates/                    # Shared document templates
  plan.md  discovery-report.md  analysis-report.md  task.md
```

## Key Patterns

**CLI-driven conductor:**
- The conductor navigates the plan flow by running `bw step show <N> <slug>` for each step
- Each step output tells the conductor what to do, when to HALT, and what command to run next
- Sub-agents self-bootstrap by running `bw step agent <N> <slug>`
- The conductor never reads step or agent files directly — only via CLI commands

**Lean context:**
- `bw step show` outputs only conductor-level instructions (no sub-agent details)
- Sub-agent bootstrap commands are pre-rendered in the output — conductor copies verbatim
- Sub-agents get their full instructions by running `bw step agent` themselves

**Plan document access:**
```
bw plan read {slug} plan       → .bw/plans/{slug}/plan.md
bw plan read {slug} discovery  → .bw/plans/{slug}/discovery-report.md
bw plan read {slug} analysis   → .bw/plans/{slug}/analysis-report.md
```

**Task IDs:** `{plan-slug}/{nnn}-{task-slug}` (e.g. `auth-feature-x7k2/001-add-user-model`)

**Workflow statuses:** `pending` → `in_progress` → `done`, with `blocked` and `ready` as intermediate states.

## Conductor Behavior

The conductor runs a 6-step flow guided by `bw step show` commands and **HALTs** at these checkpoints:
- **Step 1** — After gathering requirements, HALTs for user confirmation before creating the plan
- **Step 3** — After presenting decision cards, HALTs for user to pick an approach
- **Step 4** — After presenting the written plan, HALTs for user review before finalizing
- **Step 5** — After presenting the task list + DAG, HALTs for user spot-check before closing

Between HALTs, the conductor auto-proceeds by running the next `bw step show` command. "HALTs" = wait for explicit user input; do not proceed automatically.

## Adapter Pattern

Adapters in `adapters/<name>/` provide `/slash-command` integrations for specific agent tools. Each adapter is a thin wrapper that tells the conductor which `bw step` commands to run.

## Model Configuration

Models per agent are configured in `.bw/config.yaml`:

```yaml
models:
  claude-code:
    default: opus
    conductor: opus
    discovery: sonnet
    analysis: sonnet
    plan-writer: sonnet
    splitter: sonnet
    reviewer: sonnet
    worker: haiku
    product-conductor: opus
    milestone-splitter: sonnet
    milestone-reviewer: sonnet

  codex:
    default: gpt-5.4
    discovery: gpt-5.4-mini
    analysis: gpt-5.4-mini
    plan-writer: gpt-5.4
    splitter: gpt-5.4-mini
    reviewer: gpt-5.4-mini
    worker: gpt-5.3-codex-spark
    product-conductor: gpt-5.4
    milestone-splitter: gpt-5.4-mini
    milestone-reviewer: gpt-5.4-mini
```

**Resolution:** `models.<tool>.<agent>` → exact match. No match → `models.<tool>.default`. No default → no model override (uses tool's natural default).

**`bw step spawn`** outputs the `Agent(...)` call with the correct model for the tool + step. The conductor copies it verbatim.
