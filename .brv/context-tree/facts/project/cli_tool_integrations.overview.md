<think>
The user wants me to produce a structured overview of this knowledge document about CLI Tool Integrations. Let me analyze the document and create a concise overview with the required elements:

1. Key points (3-7 bullet points)
2. Structure/sections summary
3. Notable entities, patterns, or decisions

The document is about Claude Code CLI tool integrations with slash-commands. Let me extract the key information:

**Key Points:**
- Claude Code has 6 slash-commands (plan, split, next, work, status, product)
- Product command was added as the 6th command
- Plan runs 6-step implementation flow, Product runs 5-step product flow
- Codex adapter was deferred past MVP
- All adapters must be tool-agnostic (shell out to bw CLI)
- Deploy via bw install command with --tool and --scope flags

**Structure:**
- Reason (why the update was made)
- Raw Concept (task, changes, files, flow, timestamp, author)
- Narrative (structure, dependencies, highlights, rules)
- Facts (cli_command_count, product_command)

**Notable entities:**
- 6 slash-commands: plan, split, next, work, status, product
- Files in adapters/claude-code/
- adapters/codex/README.md (deferred)
- bw CLI
- AGENTS.md for Codex agents

**Patterns/Decisions:**
- Deferred Codex adapter until after MVP
- Tool-agnostic approach (shell out to bw CLI)
- 6 total commands now (was 5 before adding product)

Let me format this as markdown without preamble.
</think>

## CLI Tool Integrations — Overview

### Key Points

- **6 Claude Code slash-commands** added: `plan`, `split`, `next`, `work`, `status`, `product` (the 6th command)
- **Product command** runs a 5-step product plan flow; **Plan command** runs a 6-step implementation flow
- **Codex adapter deferred** past MVP — not currently implemented
- **All adapters must be tool-agnostic** — shell out to `bw` CLI
- Deployment uses `bw install` with `--tool` and `--scope` flags

### Structure Summary

| Section | Content |
|---------|---------|
| **Reason** | Updating CLI integrations to reflect 6 commands (added `product`) |
| **Raw Concept** | Task description, file list (8 adapter files), command flow diagram |
| **Narrative** | Command breakdown, dependencies, highlights, deployment rules |
| **Facts** | `cli_command_count: 6`, `product_command` convention |

### Notable Entities & Decisions

- **Commands:** `plan` (6-step), `product` (5-step), `split`, `next`, `work`, `status`
- **Files:** `adapters/claude-code/` (6 .md files), `adapters/codex/README.md` (deferred)
- **Architecture:** CLI → `adapters/` → Claude Code (slash-commands) / Codex (AGENTS.md)
- **Rule 2:** Codex agents in AGENTS.md must reference prompts in `agents/` directory
- **Decision:** Product command added to expand from 5 → 6 slash-commands