# CLAUDE.md

This is the canonical repo guide for agent work in `the-broke-workflow`. `AGENTS.md` intentionally points here instead of duplicating project instructions.

## Overview

`the-broke-workflow` is a Python Click CLI for agent-coding workflows. It stores workflow state in `.bw/` as markdown files with YAML frontmatter.

Current flows:

- **Plan flow**: 6-step implementation planning flow: Requirements -> Discovery -> Analysis -> Write Plan -> Split Tasks -> Review.
- **Epic flow**: 5-step milestone planning flow: Requirements -> Summary -> Milestones -> Review -> Present.

Canonical hierarchy for larger work:

```text
Epic -> Milestone -> Plan -> Task
```

There is no deprecated large-scope command or alternate flow alias. The current large-scope flow is `epic`.

## Setup

```bash
pip install -e .
bw init
python -m bw.cli doctor
```

Requirements:

- Python `>=3.10`
- `click`
- `pyyaml`

## CLI Surface

```bash
# Health/config/install
bw init
bw doctor
bw config
bw install --tool claude-code --scope project
bw install --tool claude-code --scope global
bw install --tool codex --scope project
bw install --tool codex --scope global

# Triage
bw triage "<idea>" --tool claude-code
bw triage "<idea>" --tool codex

# Step rendering
bw step list [--flow plan|epic]
bw step show <step-or-name> <slug> [--flow plan|epic]
bw step agent <step-or-name> <slug> [--flow plan|epic]
bw step preamble <slug> [--flow plan|epic]
bw step spawn <step-or-name> <slug> --tool <claude-code|codex> [--flow plan|epic]

# Plan lifecycle
bw plan init "<title>"
bw plan list
bw plan docs <slug>
bw plan read <slug> <plan|discovery|analysis|filename>
bw plan finalize <slug>
bw plan status <slug> [--json] [--details]
bw plan remove <slug> [--force]

# Epic lifecycle
bw epic init "<title>"
bw epic list
bw epic docs <slug>
bw epic read <slug> <requirements|milestones|filename>
bw epic finalize <slug>
bw epic plan <epic-slug> <milestone-number>
bw epic status <epic-slug> [--json] [--details]
bw epic link <plan-slug> <epic-slug> <milestone-number>
bw epic remove <epic-slug> [--force]

# Task lifecycle
bw task list [--plan <slug>] [--status <pending|in_progress|done>]
bw task next [--plan <slug>]
bw task show <plan-slug/task-slug>
bw task claim <plan-slug/task-slug> --owner <owner>
bw task release <plan-slug/task-slug>
bw task status <plan-slug/task-slug> <pending|in_progress|done>
bw task deps <plan-slug/task-slug>
bw task dag [--plan <slug>]
bw task add-dependency <child-id> <parent-id>
bw task comment <task-id> "<text>" [--author <name>]
bw task comments <task-id>
bw task remove <task-id> [--force]

# Worktrees
bw worktree create <name> [--branch <branch>] [--base <ref>]
bw worktree list
bw worktree remove <name> [--force]
```

## Data Model

```text
.bw/
  config.yaml
  plans/
    <plan-slug>/
      plan.md
      discovery-report.md
      analysis-report.md
    <epic-slug>/
      epic.md
      milestones.md
  tasks/
    <plan-slug>/
      001-<task>.md
      002-<task>.md
  archive/
  worktrees/
```

Important frontmatter:

- Plan docs use `plan.md`.
- Epic docs use `epic.md` and `milestones.md`.
- Plans linked to epics use `epic: <epic-slug>` and `milestone: <number>`.
- Task status values are `pending`, `in_progress`, and `done`.
- Blocked state is implicit through `blocked_by`; there is no separate `blocked` status.

## Source Layout

```text
adapters/
  claude-code/          # Slash-command adapter files: epic, next, plan, split, status, work
  codex/                # README only; implementation is deferred
agents/                 # Tool-agnostic prompts read by bw step/triage
bw/
  cli.py                # Top-level Click registration
  commands/             # config, doctor, epic, init, install, plan, step, task, triage, worktree
  core/                 # config, frontmatter, lock, paths, slug, steps, task_store, templates, triage
steps/                  # Plan and epic flow markdown instructions
templates/              # plan, epic, milestones, discovery, analysis, task templates
tests/                  # unittest CLI regression tests
```

## Flow Mechanics

Conductors should use the CLI as the source of instructions:

- Do not read `steps/` or `agents/` directly during normal flow execution.
- Use `bw step preamble` for conductor rules.
- Use `bw step show` for conductor-facing step instructions.
- Use `bw step spawn` to generate a tool-specific sub-agent call with model config applied.
- Sub-agents self-bootstrap from `bw step agent`.

Plan flow steps:

1. Requirements
2. Discovery
3. Analysis
4. Write Plan
5. Split Tasks
6. Review

Epic flow steps:

1. Requirements
2. Summary
3. Milestones
4. Review
5. Present

## Configuration

Model overrides are read from `.bw/config.yaml` as `models.<tool>.<agent>`, falling back to `models.<tool>.default`.

The current checked-in `.bw/config.yaml` has Claude Code overrides for:

```yaml
models:
  claude-code:
    default: sonnet
    conductor: opus
    discovery: sonnet
    analysis: sonnet
    plan-writer: sonnet
    splitter: sonnet
    reviewer: sonnet
    worker: sonnet
    triager: haiku
```

`bw.core.config.default_config()` also includes defaults for `epic-conductor`, `milestone-splitter`, and `milestone-reviewer`. Add those keys to `.bw/config.yaml` when you need explicit model routing for epic sub-agents.

## Adapters

Claude Code adapter files are active under `adapters/claude-code/`:

- `plan.md`
- `epic.md`
- `split.md`
- `next.md`
- `work.md`
- `status.md`

The Codex adapter currently has `adapters/codex/README.md` only and is documented as deferred.

## Testing

Current focused regression tests:

```bash
python -m unittest tests.test_epic_flow -v
```

Useful smoke checks:

```bash
python -m bw.cli --help
python -m bw.cli epic --help
python -m bw.cli step list --flow epic
python -m bw.cli step show 1 <slug> --flow epic
python -m bw.cli step spawn 3 <slug> --flow epic --tool claude-code
python -m bw.cli doctor
```

## Documentation Rule

Keep detailed repository behavior here in `CLAUDE.md`. `README.md` should stay short and user-facing. `AGENTS.md` should point to this file and only contain agent-runtime rules that must live there.
