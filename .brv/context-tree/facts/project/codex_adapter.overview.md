---
related: [facts/project/cli_tool_integrations.overview.md]
---
<think>
The user wants me to produce a structured overview of a knowledge document about the "Codex Adapter". Let me analyze the document and extract the key information.

Key points from the document:
1. Codex adapter is deferred past MVP
2. It mirrors Claude Code adapter using AGENTS.md conventions
3. Located at adapters/codex/
4. Uses AGENTS.md for agent configuration instead of Claude Code skill/command format
5. Requires AGENTS.md implementation
6. Depends on adapters/claude-code/ as reference
7. Deployment via `bw install` command

Structure of the document:
- Reason: Documenting deferred implementation
- Raw Concept: Task, changes, files, flow, timestamp, author
- Narrative: Structure, Dependencies, Highlights, Rules, Examples
- Facts: key facts about the project

Notable entities:
- adapters/codex/
- adapters/claude-code/
- AGENTS.md
- bw CLI
- the-broke-workflow (author)
- MVP
- 0.1.0 (project version)

Patterns/decisions:
- Deferred past MVP
- Uses AGENTS.md conventions
- Mirrors Claude Code adapter structure
- Commands shell out to bw CLI

Let me format this properly in markdown under 1500 tokens.
</think>

# Codex Adapter Overview

## Key Points

- **Status: Deferred** — The Codex adapter is explicitly deferred past MVP (Minimum Viable Product)
- **Architecture mirrors Claude Code adapter** — Uses AGENTS.md conventions instead of Claude Code skill/command format
- **Location**: `adapters/codex/` with a README.md file
- **Dependency**: Requires AGENTS.md implementation and references `adapters/claude-code/` as a porting reference
- **Deployment**: Uses `bw install --tool codex --scope project/global` command
- **Project stage**: Version 0.1.0 (early stage) — no linting or testing configured yet
- **Rule constraint**: Only implement after MVP is complete

## Structure / Sections Summary

| Section | Content |
|---------|---------|
| **Reason** | Documents the deferred Codex adapter implementation |
| **Raw Concept** | Task definition, changes, files, flow, timestamp (2026-04-18), author |
| **Narrative** | Structure, dependencies, highlights, rules, examples |
| **Facts** | Project metadata: adapter status, version, code quality, convention |

## Notable Entities

- **Files/Paths**: `adapters/codex/README.md`, `agents.md`, `commands/` directory
- **Tools**: Claude Code adapter, bw CLI
- **Author**: the-broke-workflow
- **Reference**: `adapters/claude-code/` (porting reference)

## Rules / Decisions

1. Must mirror Claude Code adapter structure
2. Agents defined in AGENTS.md must reference `agents/` directory prompts
3. Commands must shell out to bw CLI
4. Only implement after MVP complete

## Patterns

- **Convention-driven**: Codex uses AGENTS.md files for agent configuration (different from Claude Code's skill/command format)
- **Deferred architecture**: Adapter designed but intentionally delayed until post-MVP
- **CLI-based deployment**: Follows `bw install` pattern for tool installation