---
title: The Broke Workflow Architecture
summary: CLI tool with 9 core modules, 9 CLI commands, 9 agents, adapters, steps playbook, and templates
tags: []
related: []
keywords: []
createdAt: '2026-04-18T04:19:02.579Z'
updatedAt: '2026-05-11T02:05:03.531Z'
---
## Reason
Updating architecture to reflect 9 agents, 9 commands, 9 core modules

## Raw Concept
**Task:**
Document project architecture for the-broke-workflow with updated counts

**Changes:**
- Updated agents from 6 to 9 (added product-conductor, milestone-splitter, milestone-reviewer)
- Updated CLI commands from 6 to 9 (added product, step, worktree)
- Updated core modules from 6 to 9 (added config.py, steps.py)

**Files:**
- bw/cli.py
- bw/commands/
- bw/core/
- agents/

**Flow:**
CLI commands -> core modules -> agents -> adapters -> steps/templates

**Timestamp:** 2026-05-11

## Narrative
### Structure
Project has 4 main areas: (1) bw/core/ - core Python modules (frontmatter, lock, paths, slug, task_store, templates, config, steps); (2) bw/commands/ - CLI commands (plan, task, doctor, init, install, config, product, step, worktree); (3) agents/ - agent definitions (conductor, discovery, analysis, plan-writer, splitter, worker, product-conductor, milestone-splitter, milestone-reviewer); (4) adapters/ - integration adapters (claude-code, codex)

### Dependencies
CLI tool using Python, integrates with Claude Code and Codex adapters

### Highlights
Uses 6-step playbook (requirements -> discovery -> analysis -> write plan -> split tasks -> review), includes template system (plan, discovery-report, analysis-report, task), 5-step product flow (requirements -> summary -> milestones -> review -> present)

## Facts
- **core_modules_count**: Core modules count is 9 [project]
- **cli_commands_count**: CLI commands count is 9 [project]
- **agents_count**: Agents count is 9 [project]
- **core_modules_path**: Core modules are in bw/core/ [project]
- **commands_path**: CLI commands are in bw/commands/ [project]
- **agents_path**: Agents are defined in agents/ [project]
