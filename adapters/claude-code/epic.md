---
name: epic
description: >-
  Start the epic plan flow — interview to capture requirements,
  break into phased milestones, review, and finalize. Use when the user
  wants to plan WHAT to build before diving into implementation.
---

# /epic — Start the Epic Plan Flow

Run the 5-step epic plan flow using CLI-guided instructions.

## When to Use

- User wants to plan an epic or feature at the "what to build" level
- User says "epic plan", "what should I build", "break this into milestones"
- User has already researched and just needs to structure their intent into phases

## How It Works

1. Run `bw step preamble {slug} --flow epic` to load epic conductor rules
2. Run `bw step show 1 {slug} --flow epic` through `bw step show 5 {slug} --flow epic` in order
3. Each step output tells you exactly what to do — including when to HALT, when to spawn a sub-agent, and what the next command is
4. When a step says to spawn a sub-agent, use the bootstrap command shown in the output
5. After finalize, suggest using `/plan` to start technical planning for individual milestones

## Before Step 1

If no slug exists yet (new epic plan), start with step 1 using a placeholder slug. After `bw epic init "<title>"` runs, use the real slug for subsequent steps.

## Sub-Agent Spawning

When a step output includes a "Spawn Sub-Agent" section, give the sub-agent the exact prompt shown. The sub-agent will run `bw step agent <N> {slug} --flow epic` to self-bootstrap.

## Flow Summary

| Step | What | HALT? |
|------|------|-------|
| 1 | Interview — clarify what to build | No |
| 2 | Write requirements summary | Yes — user reviews |
| 3 | Break into milestones (sub-agent) | No |
| 4 | Review milestones (sub-agent) | No |
| 5 | Present results + review feedback | Yes — user decides |

## Examples

- `/epic "my awesome app"` — start epic planning
- `/epic` — prompts for epic description
