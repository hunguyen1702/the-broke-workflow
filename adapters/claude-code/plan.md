---
name: plan
description: >-
  Start the plan flow — interactive requirements, discovery, analysis,
  and plan writing. Use when the user wants to plan a new feature, create
  a structured implementation plan, or plan out work for a feature.
---

# /plan — Start the Plan Flow

Launch the conductor agent to guide through the 4-step plan creation flow:
requirements → discovery → analysis → write plan.

## When to Use

- User wants to plan a new feature or significant change
- User says "plan a feature", "let's plan this", "what's the approach"
- User wants to evaluate implementation options before starting
- Any scenario requiring structured discovery and analysis

## How It Works

1. This command launches the **conductor agent** with the full plan flow.
2. The conductor reads `steps/step-01-requirements.md` and begins interactive requirements gathering.
3. The conductor spawns sub-agents for discovery and analysis.
4. Decision cards are presented for the user to pick an approach.
5. A plan document is written and reviewed.
6. After finalize, `/split {slug}` is suggested.

## Conductor Prompt

The conductor agent should:

1. **Read step definition**: Read `steps/step-01-requirements.md`
2. **Follow the step-by-step flow** in that file
3. **Spawn sub-agents** (discovery, analysis, plan-writer) as specified in `steps/step-02-*.md`, `step-03-*.md`, `step-04-*.md`
4. **Use the agent prompts** from `agents/conductor.md` for orchestration
5. **Use `bw` CLI** for all document access and state management

## Key Agent Files

| File | Role |
|------|------|
| `steps/step-01-requirements.md` | Interactive requirements gathering |
| `steps/step-02-discovery.md` | Discovery flow |
| `steps/step-03-analysis.md` | Analysis with decision cards |
| `steps/step-04-write-plan.md` | Plan document writing |
| `agents/conductor.md` | Conductor agent definition |
| `agents/discovery.md` | Discovery sub-agent |
| `agents/analysis.md` | Analysis sub-agent |
| `agents/plan-writer.md` | Plan writer sub-agent |

## Examples

- `/plan "add user authentication"` — start planning auth
- `/plan "fix memory leak in worker pool"` — start planning the fix
- `/plan` — prompts for feature description

## Notes

- The conductor handles all document creation via `bw plan init/read/finalize`.
- Sub-agents return summaries, not full reports — conductor maintains lean context.
- After the plan is finalized, suggest: `/split {slug}`
