---
title: Product Plan Workflow
summary: '5-step CLI-guided product planning: Requirements (JTBD interview) → Summary (approval HALT) → Milestones (sub-agent) → Review (sub-agent) → Present (finalize HALT)'
tags: []
related: [facts/project/workflow_conventions.md, facts/project/cli_tool_integrations.md]
keywords: []
importance: 62
recency: 1
maturity: draft
accessCount: 4
createdAt: '2026-04-19T05:24:14.931Z'
updatedAt: '2026-04-19T05:24:14.931Z'
---
## Reason
Documenting the 5-step product planning workflow and CLI commands

## Raw Concept
**Task:**
Product plan flow - 5-step CLI-guided workflow for product-level planning (WHAT to build)

**Changes:**
- Added Requirements step with JTBD interview framework
- Added Summary step with HALTs for user approval
- Added Milestones step spawning milestone-splitter sub-agent
- Added Review step spawning milestone-reviewer sub-agent
- Added Present step with finalize decision HALT

**Files:**
- steps/product-step-01-requirements.md
- agents/product-conductor.md
- bw/commands/product_cmd.py

**Flow:**
Requirements (JTBD interview) → Summary (approval HALT) → Milestones (spawn sub-agent) → Review (spawn sub-agent) → Present (finalize HALT)

**Timestamp:** 2026-04-19

## Narrative
### Structure
5-step CLI-guided product planning workflow. Step 1: Requirements (interactive JTBD, auto-proceeds). Step 2: Summary (write requirements, HALT for approval, bw product init). Step 3: Milestones (spawn milestone-splitter). Step 4: Review (spawn milestone-reviewer). Step 5: Present (present milestones, HALT for decision, bw product finalize).

### Dependencies
Requires CLI commands: bw product init, bw product read, bw product docs, bw product finalize

### Highlights
Uses Jobs-to-be-Done (JTBD) framework for requirements gathering. Auto-proceeds between steps except at Summary and Present checkpoints. Sub-agents (milestone-splitter, milestone-reviewer) handle specialized tasks.

### Rules
Rule 1: Never craft file paths - use CLI commands
Rule 2: Never craft ls or cat commands - use CLI
Rule 3: Keep context lean - sub-agents work in fresh context
Rule 4: HALTs at interactive checkpoints (Summary, Present)
Rule 5: Focus on WHAT not HOW - product planning not implementation
Rule 6: User initial message is the requirement seed
Rule 7: Auto-proceeds to Step 2 when coverage is sufficient
Rule 8: No rigid question list - analyze gaps and ask targeted follow-ups

### Examples
Example spawn for milestone-splitter: "Break the product plan {slug} into milestones. Read: bw product read {slug} requirements. Write: .bw/plans/{slug}/milestones.md. Return: number of milestones + one-line summary each"

## Facts
- **product_plan_steps**: Product plan flow has 5 steps [project]
- **requirements_method**: Requirements step uses JTBD framework [project]
- **cli_command**: bw product init creates plan from templates [project]
- **cli_command**: bw product finalize marks plan as finalized [project]
- **agent_role**: Product Conductor is the main orchestrator agent [project]
- **agent_role**: Milestone-splitter is a sub-agent for breaking plans [project]
- **agent_role**: Milestone-reviewer is a sub-agent for reviewing milestones [project]
