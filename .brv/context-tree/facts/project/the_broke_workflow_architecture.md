---
title: The Broke Workflow Architecture
summary: CLI tool with core modules, commands, agents, adapters, steps playbook, and templates
tags: []
keywords: []
importance: 86
recency: 1
maturity: core
accessCount: 12
createdAt: '2026-04-18T04:19:02.579Z'
updatedAt: '2026-04-18T04:19:02.579Z'
---
## Reason
Documenting the-broke-workflow project structure

## Raw Concept
**Task:**
Document project architecture for the-broke-workflow

**Flow:**
CLI commands -> core modules -> agents -> adapters -> steps/templates

## Narrative
### Structure
Project has 4 main areas: (1) bw/core/ - core Python modules (frontmatter, lock, paths, slug, task_store, templates); (2) bw/commands/ - CLI commands (plan, task, doctor, init, install, config); (3) agents/ - agent definitions (conductor, discovery, analysis, plan-writer, splitter, worker); (4) adapters/ - integration adapters (claude-code, codex)

### Dependencies
CLI tool using Python, integrates with Claude Code and Codex adapters

### Highlights
Uses 6-step playbook (requirements -> discovery -> analysis -> write plan -> split tasks -> review), includes template system (plan, discovery-report, analysis-report, task)

## Facts
- **core_modules_path**: Core modules are in bw/core/ [project]
- **commands_path**: CLI commands are in bw/commands/ [project]
- **agents_path**: Agents are defined in agents/ [project]
- **adapters_path**: Adapters for Claude Code and Codex in adapters/ [project]
- **steps_path**: 6-step playbook in steps/ [project]
- **templates_path**: Templates in templates/ [project]
