---
title: BW Steps Module
summary: Step/agent file rendering with template variables for bw step CLI
tags: []
related: []
keywords: []
createdAt: '2026-05-11T02:12:49.444Z'
updatedAt: '2026-05-11T02:12:49.444Z'
---
## Reason
Document new steps.py module for step and agent rendering

## Raw Concept
**Task:**
Document bw/core/steps.py module

**Files:**
- bw/core/steps.py
- steps/step-01-requirements.md
- agents/conductor.md

**Flow:**
render_step -> render_agent -> render_spawn_call

## Narrative
### Structure
STEP_META (6 steps for plan), PRODUCT_STEP_META (5 steps for product), FLOW_META mapping flows to configs

### Dependencies
Uses frontmatter for reading plan metadata, paths for file resolution

### Highlights
Supports plan and product flows. Template vars: {slug}, {feature_name}. render_spawn_call generates Agent tool call with resolved model

## Facts
- **steps_module**: bw/core/steps.py loads step and agent markdown files for step CLI [project]
- **plan_steps**: STEP_META defines 6 steps: requirements, discovery, analysis, write-plan, split-tasks, review [project]
- **product_steps**: PRODUCT_STEP_META defines 5 steps: requirements, summary, milestones, review, present [project]
- **flow_meta**: FlowMeta maps plan and product flows with their step configurations [project]
- **step_spawn_command**: bw step spawn outputs Agent tool call for spawning sub-agents with model config [project]
- **step_show_command**: bw step show outputs conductor-level instructions for a step [project]
- **step_agent_command**: bw step agent outputs sub-agent instructions for self-bootstrap [project]
