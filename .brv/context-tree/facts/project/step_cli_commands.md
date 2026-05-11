---
title: Step CLI Commands
summary: 'Step CLI: list, show, agent, preamble, spawn commands'
tags: []
related: []
keywords: []
createdAt: '2026-04-19T05:27:29.258Z'
updatedAt: '2026-05-11T02:12:49.449Z'
---
## Reason
Document bw step CLI subcommands

## Raw Concept
**Task:**
Document bw/commands/step_cmd.py CLI commands

**Changes:**
- Added step spawn command that outputs Agent() calls with model config

**Files:**
- bw/commands/step_cmd.py

**Flow:**
_resolve_step_num -> render_* -> click.echo

## Narrative
### Structure
5 subcommands: list (show all steps), show (conductor instructions), agent (sub-agent instructions), preamble (conductor rules), spawn (Agent tool call)

### Dependencies
Depends on bw.core.steps for rendering functions

### Highlights
Accepts step as number or slug (e.g., "2" or "discovery"). --flow flag selects plan or product flow. --tool flag required for spawn to determine model config

## Facts
- **step_spawn_command**: bw step spawn outputs Agent tool call for spawning sub-agents with model config [project]
- **step_show_command**: bw step show outputs conductor-level instructions for a step [project]
- **step_agent_command**: bw step agent outputs sub-agent instructions for self-bootstrap [project]
