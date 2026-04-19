<think>
The user wants me to produce a structured overview of the provided knowledge document about the Model Configuration System. Let me analyze the document and create the requested output.

Key points from the document:
1. Model config is in .bw/config.yaml
2. Resolution order: exact match -> models.<tool>.default -> tool natural default
3. Per-tool per-agent model overrides supported
4. bw step spawn command uses this system
5. Claude-code tool uses sonnet by default
6. Conductor agent overrides to opus
7. Supported agents: conductor, discovery, analysis, plan-writer, splitter, reviewer, worker

Structure:
- Reason: Documenting the bw model config system
- Raw Concept: Task, Files, Flow
- Narrative: Structure and Highlights

Notable entities:
- .bw/config.yaml
- bw/commands/step_cmd.py
- Claude-code tool (sonnet default, opus for conductor)
- Agents: conductor, discovery, analysis, plan-writer, splitter, reviewer, worker

I need to output only the overview with no preamble, using markdown formatting, under 1500 tokens.
</think>

# Model Configuration System

## Key Points

- Model configuration is defined in `.bw/config.yaml`
- Resolution order: **exact match** (`models.<tool>.<agent>`) → **tool default** (`models.<tool>.default`) → **tool natural default**
- Supports per-tool per-agent model overrides
- `bw/commands/step_cmd.py` handles the resolution and spawns `Agent()` calls with the correct model
- **Claude-code** tool defaults to **sonnet** model
- **Conductor** agent overrides Claude-code to use **opus** model

## Structure / Sections Summary

| Section | Content |
|---------|---------|
| **Reason** | Documents the bw model config system with per-tool per-agent overrides and resolution order |
| **Raw Concept** | Outlines task, relevant files (`.bw/config.yaml`, `bw/commands/step_cmd.py`), and flow from config to Agent() call |
| **Narrative** | Details resolution hierarchy and highlights key tool/agent model assignments |

## Notable Entities

- **Files:** `.bw/config.yaml`, `bw/commands/step_cmd.py`
- **Tool:** Claude-code (default: sonnet)
- **Agents:** conductor, discovery, analysis, plan-writer, splitter, reviewer, worker
- **Model Override:** conductor → opus (for Claude-code)

## Patterns / Decisions

- Explicit agent-level overrides take precedence over tool defaults
- Tool natural defaults serve as fallback when no explicit config exists
- Configuration resolution happens at runtime when spawning agent commands