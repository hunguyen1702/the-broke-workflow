# Step 4: Write Plan

**Progress: Step 4 of 6** — Next: Split Tasks

## Goal

Synthesize requirements, discovery findings, and selected approach into a structured plan document.

## Rules

- The **conductor** spawns a plan writer sub-agent.
- The plan document covers WHAT and WHY — NOT implementation steps.
- Implementation steps belong in task files (Step 5).
- **HALTs** after sub-agent completes for user review.

## Sequence

### 1. Spawn Plan Writer Sub-Agent

```
## Write Plan: {feature_name}

Fill in the plan document for plan {slug}.

## Selected approach: {name}
Selected by user. See: bw plan read {slug} analysis

## Your task

1. Read context:
   bw plan read {slug} discovery
   bw plan read {slug} analysis
   bw plan read {slug} plan

2. Synthesize into plan.md covering:
   - Problem Statement (what problem does this solve?)
   - Goals (what we want to achieve)
   - Non-Goals (what we explicitly won't do)
   - Approach Overview (high-level HOW, not steps)
   - Deliverables (major work streams, NOT individual tasks)
   - Acceptance Criteria (how we know the whole effort is done)
   - Technical Decisions (key choices with rationale)
   - Codebase Context (synthesized from discovery)
   - References

3. IMPORTANT:
   - Do NOT write implementation steps. Those go in task files.
   - Deliverables should be high-level work streams.
   - Be specific — no vague bullet points.

4. Write the completed plan to:
   .bw/plans/{slug}/plan.md

## Return to conductor

Return a one-line confirmation: "Plan written for {slug}"
```

### 2. Present for Review

After the sub-agent completes:

> **Plan written.** Review it now, or let me know what to adjust.

Display the plan:

```
bw plan read {slug} plan
```

### 3. User Review

> Any adjustments before I finalize?

**HALTs** — wait for user input.

- If user approves: call `bw plan finalize {slug}`.
- If user adjusts: apply changes and re-present.

### 4. Finalize

After user approval:

```
bw plan finalize {slug}
```

This marks the plan as finalized and creates `.bw/tasks/{slug}/` for task files.

### 5. Auto-Proceed

Read `step-05-split-tasks.md` and follow it.
