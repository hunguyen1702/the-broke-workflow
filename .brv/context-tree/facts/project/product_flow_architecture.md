---
title: Product Flow Architecture
summary: 'Two workflow flows: plan flow (6 steps, 6 agents) and product flow (5 steps: requirements, summary, milestones, review, present; agents: product-conductor, milestone-splitter, milestone-reviewer)'
tags: []
related: [facts/project/the_broke_workflow_architecture.md]
keywords: []
importance: 76
recency: 1
maturity: validated
accessCount: 7
updateCount: 1
createdAt: '2026-04-19T05:24:21.534Z'
updatedAt: '2026-04-19T05:25:24.617Z'
---
## Reason
Update product flow architecture with new 5-step product flow

## Raw Concept
**Task:**
Document the two workflow flows in The Broke Workflow

**Changes:**
- Added product flow (5 steps) alongside existing plan flow
- Product flow agents: product-conductor, milestone-splitter, milestone-reviewer
- Step 1 uses JTBD lens methodology
- Step 2 and Step 5 HALT for user input
- Added product flow as distinct from plan flow
- Product flow has 5 steps instead of 6
- Product Conductor agent handles product flow orchestration
- Milestone-splitter and milestone-reviewer are sub-agents

**Files:**
- steps/product-step-01-requirements.md
- agents/product-conductor.md
- templates/milestones.md

**Flow:**
requirements -> summary -> milestones -> review -> present

**Timestamp:** 2026-04-19

## Narrative
### Structure
The Broke Workflow now has two distinct flows: (1) Plan Flow - 6 steps with 6 agents for implementation planning, (2) Product Flow - 5 steps for product planning. Product flow managed by Product Conductor agent which handles interactive steps directly and delegates to milestone-splitter and milestone-reviewer sub-agents.

### Dependencies
Requires bw CLI for document access: bw product read {slug} requirements/milestones, bw product init, bw product finalize

### Highlights
Product flow uses HALTs at interactive checkpoints (summary approval, final presentation). Steps auto-proceed when coverage is sufficient except at review points.

### Rules
Rule 1: Never craft file paths - use CLI commands
Rule 2: Never craft ls or cat commands - use CLI
Rule 3: Keep context lean - sub-agents work in fresh context
Rule 4: HALTs at interactive checkpoints
Rule 5: Focus on WHAT not HOW

### Examples
Example spawn: "Break the product plan {slug} into milestones. Read: bw product read {slug} requirements. Write: .bw/plans/{slug}/milestones.md"

## Facts
- **workflow_flows**: Two workflow flows exist: plan flow (6 steps) and product flow (5 steps) [convention]
- **product_flow_steps**: Product flow steps: requirements, summary, milestones, review, present [convention]
- **product_conductor_agent**: Product Conductor is the main agent for product flow [project]
- **sub_agents**: Sub-agents: milestone-splitter and milestone-reviewer [project]
