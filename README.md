# the-broke-workflow

Personal agent-coding workflow toolkit. Runs a 6-step planning process (Requirements, Discovery, Analysis, Write Plan, Split Tasks, Review) using a conductor that delegates heavy work to fresh sub-agents.

## Quick Start

```bash
pip install -e .
bw init
bw plan init "My Project"
```

## Core Commands

```bash
# Step flow
bw step list                  # List all 6 steps
bw step show <N> <slug>       # Conductor instructions for step N
bw step agent <N> <slug>      # Sub-agent bootstrap instructions
bw step spawn <N> <slug>      # Output Agent(...) call with configured model

# Plan lifecycle
bw plan init "<title>"        # Create new plan from templates
bw plan list                  # List all plans
bw plan read <slug> <doc>     # Print a document (plan|discovery|analysis)
bw plan finalize <slug>       # Freeze plan and create tasks/

# Task lifecycle
bw task list                  # List all tasks (--plan, --status filters)
bw task next                  # Show ready tasks (unblocked, unclaimed)
bw task show <id>             # Print a task file
bw task claim <id> --owner X  # Claim a task
bw task status <id> <status>  # Update status
bw task dag                   # Render task DAG as ASCII

# Other
bw doctor                     # Check installation
bw config                     # Configure settings
```

## 6-Step Flow

1. **Requirements** — Gather user needs (adaptive, not rigid Q&A)
2. **Discovery** — Explore codebase and gather context
3. **Analysis** — Score and present approach options
4. **Write Plan** — Synthesize findings into a concrete plan
5. **Split Tasks** — Decompose plan into executable tasks with DAG
6. **Review** — Final human review before task execution

The conductor navigates the flow via `bw step show` commands and HALTs at key checkpoints for human input.

## Architecture

```
.bw/              # Workflow data root
  plans/<slug>/   # Plan documents (plan.md, discovery-report.md, analysis-report.md)
  tasks/<slug>/   # Task files (001-task.md, ...)

steps/            # 6-step conductor playbook
agents/           # Sub-agent definitions (conductor, discovery, analysis, ...)
adapters/         # Tool integrations (claude-code, codex)
templates/        # Shared document templates
```

## Configuration

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
```

See `CLAUDE.md` for full architecture details.
