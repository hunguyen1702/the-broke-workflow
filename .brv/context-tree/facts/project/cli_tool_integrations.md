---
title: cli_tool_integrations
summary: 'Claude Code adapter has 6 slash-commands: next, plan, product, split, status, work. Step and worktree are bw CLI commands, not Claude Code commands.'
tags: []
related: [facts/project/codex_adapter.md, facts/project/the_broke_workflow_architecture.md, facts/project/claude_code_work_adapter.md, facts/project/cli_tool_integrations.md]
keywords: []
createdAt: '2026-04-18T04:25:49.854Z'
updatedAt: '2026-05-11T02:13:37.496Z'
---
## Reason
Correcting Claude Code adapter slash-command count from 9 to 6

## Raw Concept
**Task:**
Document Claude Code adapter slash-commands (CORRECTED to 6 commands)

**Changes:**
- Created Claude Code adapters with slash-commands
- Planned Codex adapter but deferred past MVP
- Created Claude Code adapters with 6 slash-commands
- Added product command for 5-step product plan flow
- Added Claude Code product command (6th slash-command)
- Product command runs 5-step product plan flow
- Added product command to CLI integrations
- Total commands increased from 5 to 6
- Added product command (5-step product plan flow)
- Added step command (step execution)
- Added worktree command (worktree management)
- Total commands increased from 6 to 9
- Corrected slash-command count from 9 to 6
- Verified adapters/claude-code/ contains: next.md, plan.md, product.md, split.md, status.md, work.md
- Clarified step and worktree are bw CLI commands (bw/commands/), not Claude Code slash-commands

**Files:**
- adapters/claude-code/
- adapters/codex/README.md
- adapters/claude-code/plan.md
- adapters/claude-code/product.md
- adapters/claude-code/split.md
- adapters/claude-code/next.md
- adapters/claude-code/work.md
- adapters/claude-code/status.md
- bw/cli.py

**Flow:**
User invokes slash-command -> Claude Code adapter parses -> bw CLI command execution -> output formatting

**Timestamp:** 2026-05-11

**Author:** the-broke-workflow

## Narrative
### Structure
Claude Code adapter in adapters/claude-code/ provides 6 slash-commands that map to bw CLI commands. Each slash-command has a corresponding .md file with name, description, and detailed usage instructions.

### Dependencies
Depends on bw CLI commands (bw task, bw step, bw plan, bw product). The step and worktree commands are bw CLI native commands located in bw/commands/, not Claude Code adapter commands.

### Highlights
6 slash-commands: /next (ready tasks), /plan (6-step plan flow), /product (5-step product flow), /split (split finalized plan), /status (project snapshot), /work (claim and execute task)

### Rules
Rule 1: All adapters must be tool-agnostic (shell out to bw CLI)
Rule 2: Codex agents defined in AGENTS.md must reference prompts in agents/ directory
Rule 3: Deploy via bw install command with --tool and --scope flags

## Facts
- **claude_code_command_count**: Claude Code adapter has exactly 6 slash-commands [project]
- **command_source_distinction**: Step and worktree are bw CLI commands, not Claude Code adapter commands [project]
- **adapter_location**: Adapter files are in adapters/claude-code/ directory [project]
