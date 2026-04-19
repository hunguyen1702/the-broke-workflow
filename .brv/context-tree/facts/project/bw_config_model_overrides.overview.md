<think>
The user wants me to produce a structured overview of this knowledge document about BW Config Model Overrides. Let me analyze the content and create a concise summary with the required elements:

1. Key points (3-7 bullet points)
2. Structure/sections summary
3. Notable entities, patterns, or decisions

The document is about .bw/config.yaml model overrides for Claude Code commands in the bw CLI.

Key information:
- File: .bw/config.yaml
- Purpose: Per-task model overrides for bw CLI
- Default model: sonnet
- Conductor model: opus
- Other roles: sonnet (discovery, analysis, plan-writer, splitter, reviewer, worker)
- Config loaded by bw CLI on startup
- Default model is claude-sonnet-4-20250514
- Conductor uses opus model
- All other roles use sonnet model

Let me format this properly in markdown under 1500 tokens.
</think>

## BW Config Model Overrides - Overview

### Key Points
- **.bw/config.yaml** defines per-task model overrides for the bw CLI
- **Default model**: `claude-sonnet-4-20250514` (Sonnet 4)
- **Conductor model**: Uses Opus for more capable orchestration
- **All other roles** (discovery, analysis, plan-writer, splitter, reviewer, worker) use Sonnet
- Config loads on bw CLI startup via core config module
- Model override keys: `default`, `conductor`, `discovery`, `analysis`, `plan-writer`, `splitter`, `reviewer`, `worker`

### Structure / Sections
- **Reason**: Documents the purpose (adding model overrides for Claude Code commands)
- **Raw Concept**: Task description, changes made, files involved, flow explanation
- **Narrative**: Explains the structure, dependencies, and highlights the model override keys
- **Facts**: Explicit fact statements about default, conductor, and role models

### Notable Entities & Decisions
| Entity | Value |
|--------|-------|
| Config file | `.bw/config.yaml` |
| Default model | `claude-sonnet-4-20250514` |
| Conductor model | `opus` |
| Role models | All use `sonnet` |
| Loader | bw CLI core config module |

**Pattern**: Two-tier model hierarchy — Opus for high-level orchestration (conductor), Sonnet for task execution roles.