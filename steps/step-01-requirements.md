# Step 1: Requirements

**Progress: Step 1 of 6** — Next: Discovery

## Goal

Gather goals, outcomes, deliverables, and scope from the user. Establish shared understanding before any analysis begins.

## Rules

- This step is **interactive** — the conductor (main agent) handles it directly.
- **HALTs** at the end to confirm scope with the user before proceeding.
- After confirmation: calls `bw plan init "<title>"` to create the plan folder.

## Sequence

### 1. Opening

Greet the user and explain what happens next:

> I'll ask you a few questions to understand what you want to build, then I'll explore the codebase, evaluate options, and create a structured plan. Each step will be handed off to a fresh sub-agent to keep context lean.

### 2. Gather Requirements

Ask the following in order. Keep each question focused — no compound questions.

**Q1 — What are you building?**

> What feature or change are you working on? Describe it in one or two sentences as if explaining to a colleague.

**Q2 — What does success look like?**

> When this is done, what will be different? What specific outcomes or behaviors will exist?

**Q3 — What are the deliverables?**

> What are the major work streams or end products? Think: APIs, UIs, scripts, configs, migrations. Not implementation steps — outputs.

**Q4 — What is out of scope?**

> What should this explicitly NOT include? What would be a reasonable scope creep that you want to avoid?

**Q5 — Any constraints?**

> Are there deadlines, team considerations, technology restrictions, or known obstacles?

### 3. Summarize

Present a brief summary:

```
## Scope Confirmed

**Feature:** {Q1 answer}
**Success:** {Q2 answer}
**Deliverables:** {Q3 as bullet list}
**Out of scope:** {Q4 as bullet list}
**Constraints:** {Q5 or "none stated"}
```

### 4. Confirm

> Does this look right? I'll proceed with discovery — analyzing the codebase and gathering patterns before we evaluate approaches.

**HALTs** — wait for confirmation.

- If user confirms: proceed to Step 2.
- If user adjusts: update summary and re-present.

### 5. Create Plan

After confirmation, call:

```
bw plan init "<Q1 title>"
```

This creates `.bw/plans/<slug>/` with plan.md, discovery-report.md, and analysis-report.md templates copied in.
