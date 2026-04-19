---
children_hash: 63f8cb8adc87b56a76056e52fb0b8ee1e60849604899c08f41e17df85987b399
compression_ratio: 0.4767827529021559
condensation_order: 3
covers: [facts/_index.md]
covers_token_total: 1206
summary_level: d3
token_count: 575
type: summary
---
<think>
The user has asked me to review what I've learned and provide a summary. Looking at the context:

1. The system has provided me with a detailed overview of the "facts/project" domain
2. It contains information about The Broke Workflow (TBW) architecture, CLI commands, workflow flows, model configuration, and task management
3. I need to output ONLY the summary text without using any tools

The user explicitly states this is my "FINAL ITERATION" and wants me to "Summarize your findings and give the best answer you can with the information gathered."

Based on the context provided, I should output a clean summary of the facts/project domain. However, I notice there's a "FINAL ITERATION" note which suggests this might be a test or evaluation scenario.

Looking at the content provided in the context, it appears to be a comprehensive overview of the domain. Let me provide a clean summary as requested.
</think>

# Facts/Project Domain — Summary

## The Broke Workflow (TBW)

A CLI tool for AI-augmented product and implementation planning with two distinct workflow flows.

### Core Architecture

- **bw/core/** — Python modules: frontmatter, lock, paths, slug, task_store, templates
- **bw/commands/** — CLI commands: plan, task, step, product, doctor, init, install, config
- **agents/** — Agent definitions for orchestration and task execution
- **adapters/** — Tool integrations for Claude Code and Codex

### CLI Command Systems

- **Product CLI**: `bw product init | list | docs | read | finalize` — manages product plan lifecycle
- **Step CLI**: `bw step list | show | agent | preamble | spawn` — drives 6-step plan flow
- **Claude Code**: 6 slash-commands (plan, product, split, next, work, status)

### Workflow Flows

- **Plan Flow** (6 steps): requirements → discovery → analysis → write plan → split tasks → review
- **Product Flow** (5 steps): requirements → summary → milestones → review → present (with HALTs for user approval)

### Configuration & Model System

- Python >= 3.10, click >= 8.0, pyyaml >= 6.0
- Model configuration with resolution order: exact match → tool default → natural default
- Default override: opus for conductor, sonnet for all others

### Known Gaps

- No test framework configured (no pytest dependencies)
- Codex adapter deferred past MVP