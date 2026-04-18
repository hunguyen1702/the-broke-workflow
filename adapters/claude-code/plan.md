---
name: plan
description: >-
  Start the plan flow — interactive requirements, discovery, analysis,
  and plan writing. Use when the user wants to plan a new feature, create
  a structured implementation plan, or plan out work for a feature.
---

# /plan — Start the Plan Flow

Run the 6-step plan flow using CLI-guided instructions.

## When to Use

- User wants to plan a new feature or significant change
- User says "plan a feature", "let's plan this", "what's the approach"
- Any scenario requiring structured discovery and analysis

## How It Works

1. Run `bw step preamble {slug}` to load conductor rules
2. Run `bw step show 1 {slug}` through `bw step show 6 {slug}` in order
3. Each step output tells you exactly what to do — including when to HALT, when to spawn a sub-agent, and what the next command is
4. When a step says to spawn a sub-agent, give the sub-agent the exact bootstrap command shown in the output
5. After finalize, suggest `/split {slug}` or `/work`

## Before Step 1

If no slug exists yet (new plan), start with step 1 using a placeholder slug. After `bw plan init "<title>"` runs, use the real slug for subsequent steps.

## Sub-Agent Spawning

When a step output includes a "Spawn Sub-Agent" section, give the sub-agent the exact prompt shown. The sub-agent will run `bw step agent <N> {slug}` to self-bootstrap with its full instructions. You do NOT need to read the sub-agent's instructions yourself.

## Examples

- `/plan "add user authentication"` — start planning auth
- `/plan` — prompts for feature description
