---
related: [facts/project/project_config.overview.md]
---
<think>
The user wants me to produce a structured overview of the knowledge document about "The Broke Workflow Architecture". I need to:

1. Identify key points (3-7 bullet points)
2. Provide structure/sections summary
3. Note notable entities, patterns, or decisions
4. Keep under 1500 tokens
5. Use markdown formatting
6. Output only the overview - no preamble

Let me analyze the document:

- It's about documenting a CLI tool project called "the-broke-workflow"
- There are 4 main areas: core modules, commands, agents, adapters
- The flow is: CLI commands -> core modules -> agents -> adapters -> steps/templates
- There are 6 steps in the playbook
- Dependencies: Python CLI tool integrating with Claude Code and Codex adapters

Key entities:
- bw/core/ - core Python modules (frontmatter, lock, paths, slug, task_store, templates)
- bw/commands/ - CLI commands (plan, task, doctor, init, install, config)
- agents/ - agent definitions (conductor, discovery, analysis, plan-writer, splitter, worker)
- adapters/ - integration adapters (claude-code, codex)
- steps/ - 6-step playbook
- templates/ - templates (plan, discovery-report, analysis-report, task)

The 6-step playbook: requirements -> discovery -> analysis -> write plan -> split tasks -> review

Let me structure this properly.
</think>

# The Broke Workflow Architecture - Overview

## Key Points

- **CLI-based tool** built with Python that orchestrates a 6-step playbook workflow: requirements → discovery → analysis → write plan → split tasks → review
- **Four main architectural areas**: core modules (`bw/core/`), CLI commands (`bw/commands/`), agent definitions (`agents/`), and integration adapters (`adapters/`)
- **Integrates with external AI systems** via adapters for Claude Code and Codex
- **Template-driven output** with templates for plan, discovery-report, analysis-report, and task artifacts
- **Modular agent architecture** with 6 agent types: conductor, discovery, analysis, plan-writer, splitter, and worker

## Structure Summary

| Area | Location | Contents |
|------|----------|----------|
| Core Modules | `bw/core/` | frontmatter, lock, paths, slug, task_store, templates |
| CLI Commands | `bw/commands/` | plan, task, doctor, init, install, config |
| Agents | `agents/` | conductor, discovery, analysis, plan-writer, splitter, worker |
| Adapters | `adapters/` | claude-code, codex |
| Steps | `steps/` | 6-step playbook |
| Templates | `templates/` | plan, discovery-report, analysis-report, task |

## Notable Entities & Patterns

- **Flow Pattern**: CLI → Core Modules → Agents → Adapters → Steps/Templates
- **Agent Specialization**: Distinct agents for discovery, analysis, planning, task splitting, and execution
- **Command Set**: 8 CLI commands covering full lifecycle (plan, task, doctor, init, install, config)
- **Maturity Status**: Draft (recency: 1, importance: 50)