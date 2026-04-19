---
title: CLI Tool Integrations
summary: 'Claude Code adapters: plan, split, next, work, status (5) + product (1) = 6 total slash-commands'
tags: []
related: [facts/project/cli_tool_integrations.overview.md, facts/project/codex_adapter.md, facts/project/the_broke_workflow_architecture.md]
keywords: []
importance: 100
recency: 1
maturity: core
accessCount: 25
updateCount: 3
createdAt: '2026-04-18T04:25:49.854Z'
updatedAt: '2026-04-19T05:28:57.990Z'
---
## Reason
Updating CLI tool integrations to reflect 6 commands (added product)

## Raw Concept
**Task:**
Document Claude Code CLI tool integrations with 6 slash-commands

**Changes:**
- Created Claude Code adapters with slash-commands
- Planned Codex adapter but deferred past MVP
- Created Claude Code adapters with 6 slash-commands
- Added product command for 5-step product plan flow
- Added Claude Code product command (6th slash-command)
- Product command runs 5-step product plan flow
- Added product command to CLI integrations
- Total commands increased from 5 to 6

**Files:**
- adapters/claude-code/
- adapters/codex/README.md
- adapters/claude-code/plan.md
- adapters/claude-code/product.md
- adapters/claude-code/split.md
- adapters/claude-code/next.md
- adapters/claude-code/work.md
- adapters/claude-code/status.md

**Flow:**
CLI tool -> adapters/ -> Claude Code (slash-commands) / Codex (AGENTS.md)

**Timestamp:** 2026-04-19

**Author:** the-broke-workflow

## Narrative
### Structure
6 Claude Code slash-commands: plan (6-step implementation flow), product (5-step product flow), split, next, work, status

### Dependencies
Codex adapter implementation depends on completing MVP first

### Highlights
Plan runs 6-step flow, Product runs 5-step flow, Split breaks into tasks, Next shows next step, Work runs tasks, Status shows progress

### Rules
Rule 1: All adapters must be tool-agnostic (shell out to bw CLI)
Rule 2: Codex agents defined in AGENTS.md must reference prompts in agents/ directory
Rule 3: Deploy via bw install command with --tool and --scope flags

## Facts
- **cli_command_count**: Claude Code has 6 slash-commands [convention]
- **product_command**: Product command was added as the 6th command [convention]
