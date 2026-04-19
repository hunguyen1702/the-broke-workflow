<think>
The user wants me to produce a structured overview of a knowledge document about "Product Flow Architecture" from The Broke Workflow. I need to:

1. Identify 3-7 key points
2. Provide a structure/sections summary
3. Note notable entities, patterns, or decisions
4. Keep under 1500 tokens
5. Use markdown formatting
6. Output only the overview - no preamble

Let me analyze the document:

**Key Points:**
- Two distinct workflow flows: Plan Flow (6 steps, 6 agents) and Product Flow (5 steps)
- Product Flow steps: requirements → summary → milestones → review → present
- Product Conductor agent manages product flow orchestration
- Sub-agents: milestone-splitter and milestone-reviewer
- HALTs at interactive checkpoints (summary approval, final presentation)
- Uses JTBD lens methodology in Step 1
- Rules about using CLI commands instead of file paths

**Structure:**
- Reason: Why this was updated
- Raw Concept: Task description and changes
- Narrative: Structure, Dependencies, Highlights, Rules, Examples
- Facts: Key facts/conventions

**Notable Entities:**
- Product Conductor agent
- milestone-splitter sub-agent
- milestone-reviewer sub-agent
- CLI commands (bw product read, bw product init, bw product finalize)
- HALTs (user input checkpoints)
- JTBD lens methodology
- Two flows: plan flow and product flow

**Decisions:**
- Product flow has 5 steps vs plan flow's 6 steps
- HALTs at interactive checkpoints for user input
- Sub-agents work in fresh context (keep context lean)
- Focus on WHAT not HOW

Let me format this properly in markdown.
</think>

# Product Flow Architecture — Overview

## Key Points

- **Two workflow flows exist**: Plan Flow (6 steps, 6 agents) for implementation planning, and Product Flow (5 steps) for product planning
- **Product Flow sequence**: requirements → summary → milestones → review → present
- **Product Conductor** is the main orchestrating agent for product flow; delegates to sub-agents **milestone-splitter** and **milestone-reviewer**
- **HALTs** pause the flow at interactive checkpoints (summary approval, final presentation) for user input; auto-proceeds when coverage is sufficient
- **Step 1 uses JTBD lens methodology** for requirements gathering
- **CLI-first rule**: All file operations use `bw` CLI commands (e.g., `bw product read {slug} requirements`), never raw file paths or shell commands
- **Context isolation**: Sub-agents operate in fresh context to keep things lean

## Structure / Sections Summary

| Section | Content |
|---------|---------|
| **Reason** | Update rationale — added new 5-step product flow alongside existing plan flow |
| **Raw Concept** | Task details, specific changes (agents, steps, HALTs), file references, flow diagram |
| **Narrative** | Core architecture explanation: dependencies (CLI commands), highlights (HALTs, auto-proceed), rules (5 governing principles), example spawn syntax |
| **Facts** | Canonical conventions: `workflow_flows`, `product_flow_steps`, `product_conductor_agent`, `sub_agents` |

## Notable Entities, Patterns & Decisions

- **Agents**: `product-conductor` (main), `milestone-splitter`, `milestone-reviewer` (sub-agents)
- **CLI Commands**: `bw product read {slug}`, `bw product init`, `bw product finalize`
- **Pattern**: HALTs at summary (Step 2) and present (Step 5) for user validation
- **Pattern**: JTBD lens applied to requirements step
- **Decision**: Product flow has 5 steps vs. Plan flow's 6 steps
- **Decision**: Sub-agents get fresh context (Rule 3)
- **Convention**: `facts/workflow_flows`, `facts/product_flow_steps` — structured as knowledge base conventions