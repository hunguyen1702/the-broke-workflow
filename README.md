# the-broke-workflow

Personal agent-coding workflow toolkit. It provides:

- a 6-step implementation **plan** flow
- a 5-step milestone-oriented **epic** flow
- file-backed task tracking under `.bw/`
- adapters for agent tools, currently Claude Code commands plus deferred Codex notes

`CLAUDE.md` is the canonical repo guide. Keep detailed architecture and agent instructions there.

## Install

```bash
pip install -e .
bw init
```

## Main Flows

```bash
# Route a raw idea to the right flow
bw triage "Build a search platform with indexing and ranking" --tool claude-code

# Implementation plan flow
bw plan init "Search API"
bw step list
bw step show 1 <plan-slug>
bw plan status <plan-slug>

# Epic flow: Epic -> Milestone -> Plan -> Task
bw epic init "Search Platform"
bw step list --flow epic
bw step show 1 <epic-slug> --flow epic
bw epic plan <epic-slug> 1
bw epic status <epic-slug>
```

## Command Groups

```bash
bw plan      # plan docs: init/list/docs/read/finalize/status/remove
bw epic      # epic docs and milestone rollup: init/list/docs/read/finalize/plan/status/link/remove
bw task      # task list/next/show/claim/release/status/deps/dag/add-dependency/comment/comments/remove
bw step      # render flow instructions and sub-agent spawn calls
bw triage    # classify an idea as plan-flow vs epic-flow
bw worktree  # create/list/remove .bw/worktrees worktrees
bw install   # install adapters for claude-code or codex
bw config    # print .bw/config.yaml
bw doctor    # health check
```

## Repository Layout

```text
.bw/                 Runtime workspace: plans, tasks, archive, worktrees, config
adapters/            Tool adapters
agents/              Tool-agnostic agent prompts
bw/commands/         Click command groups
bw/core/             Frontmatter, paths, steps, config, task store, triage
steps/               Plan and epic flow instructions rendered by bw step
templates/           Markdown templates for plans, epics, milestones, tasks
tests/               CLI regression tests
```

## Verify

```bash
python -m unittest tests.test_epic_flow -v
python -m bw.cli doctor
```
