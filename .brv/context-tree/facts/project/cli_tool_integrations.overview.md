---
related: [facts/project/cli_tool_integrations.md, facts/project/task_store_module.overview.md, facts/project/workflow_conventions.overview.md, facts/project/codex_adapter.overview.md]
---
<think>
The user wants me to produce a structured overview of this knowledge document about CLI Tool Integrations. Let me analyze the document and extract the key information.

Key entities and facts:
- Claude Code adapters with slash-commands
- Codex adapter deferred past MVP
- Pure Python CLI with no external dependencies
- Adapter pattern used
- 5 slash-commands: plan, split, next, work, status
- AGENTS.md convention for Codex

Let me structure this properly:

1. Key points (3-7 bullet points)
2. Structure / sections summary
3. Notable entities, patterns, or decisions

I'll keep it under 1500 tokens and use markdown formatting.
</think>

# CLI Tool Integrations Overview

## Key Points

- **Pure Python CLI** with no external dependencies, APIs, databases, or auth providers
- **Adapter pattern** used for tool integrations: Claude Code uses skill/command format, Codex uses AGENTS.md convention
- **Claude Code** provides 5 slash-commands: `plan`, `split`, `next`, `work`, `status`
- **Codex adapter** is deferred past MVP — implementation depends on completing MVP first
- **AGENTS.md convention**: Codex agents defined in project root must reference prompts in `agents/` directory
- All adapters must be tool-agnostic (shell out to bw CLI)

## Structure / Sections

| Section | Summary |
|---------|---------|
| **Reason** | Documents tool integrations architecture for Claude Code and Codex adapters |
| **Raw Concept** | Created Claude Code adapters with slash-commands; Codex adapter planned but deferred past MVP |
| **Narrative** | Covers structure (adapter pattern), dependencies (MVP completion), highlights (pure Python, 5 commands), and rules (tool-agnostic, AGENTS.md reference, deployment flags) |
| **Facts** | Lists project metadata: tool type, external dependencies, adapter paths, command sets, status, convention, deployment commands |

## Notable Entities & Decisions

- **Adapter paths**: `adapters/claude-code/`, `adapters/codex/`
- **Codex deployment command**: `bw install --tool codex --scope project/global`
- **Rule 1**: All adapters must shell out to bw CLI (tool-agnostic)
- **Rule 2**: Codex AGENTS.md must reference prompts in `agents/` directory
- **Rule 3**: Deploy via `bw install` with `--tool` and `--scope` flags