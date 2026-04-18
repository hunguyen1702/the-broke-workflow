---
accessCount: 10
createdAt: '2026-04-18T04:25:49.854Z'
importance: 80
keywords: []
maturity: validated
recency: 1
related: [facts/project/cli_tool_integrations.overview.md]
summary: Pure Python CLI with Claude Code slash-commands, Codex deferred past MVP using AGENTS.md convention
tags: []
title: CLI Tool Integrations
updatedAt: '2026-04-18T04:25:49.854Z'
---
## Reason
Documenting tool integrations architecture - Claude Code and Codex adapters

## Raw Concept
**Task:**
Document CLI tool integrations architecture

**Changes:**
- Created Claude Code adapters with slash-commands
- Planned Codex adapter but deferred past MVP

**Files:**
- adapters/claude-code/
- adapters/codex/README.md

**Flow:**
CLI tool -> adapters/ -> Claude Code (slash-commands) / Codex (AGENTS.md)

## Narrative
### Structure
Tool integrations follow adapter pattern: Claude Code uses skill/command format, Codex uses AGENTS.md convention

### Dependencies
Codex adapter implementation depends on completing MVP first

### Highlights
Pure Python CLI with no external dependencies. Claude Code provides 5 slash-commands. Codex deferred until after MVP.

### Rules
Rule 1: All adapters must be tool-agnostic (shell out to bw CLI)
Rule 2: Codex agents defined in AGENTS.md must reference prompts in agents/ directory
Rule 3: Deploy via bw install command with --tool and --scope flags

## Facts
- **tool_type**: The tool is a pure Python CLI with no external services [project]
- **external_dependencies**: No external APIs, databases, or auth providers are used [project]
- **claude_code_adapter_path**: Claude Code adapters are in adapters/claude-code/ [project]
- **claude_code_commands**: Claude Code provides slash-commands: plan, split, next, work, status [project]
- **codex_adapter_path**: Codex adapter is in adapters/codex/ [project]
- **codex_status**: Codex adapter is deferred past MVP [project]
- **codex_convention**: Codex uses AGENTS.md files in project root to define agents and commands [project]
- **codex_deployment**: Codex deployment uses: bw install --tool codex --scope project/global [project]
