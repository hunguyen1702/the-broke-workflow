# Step 3: Milestones

**Progress: Step 3 of 5** — Next: Review

## Goal

Break the approved requirements into phased milestones. Each milestone is a shippable increment that delivers standalone value.

## Rules

- The **conductor** spawns a milestone-splitter sub-agent.
- The sub-agent reads the requirements and produces a milestone breakdown.
- Milestones focus on WHAT to deliver in each phase, not HOW to implement.

## Sequence

### 1. Inform User

> Breaking your requirements into milestones. Each milestone will be a shippable phase that delivers standalone value.

### 2. Spawn Milestone Splitter Sub-Agent

The conductor spawns ONE milestone-splitter sub-agent with this prompt:

```
## Milestones: {slug}

Break the epic plan for {slug} into phased milestones.

## Read the requirements

bw epic read {slug} requirements

## Your task

1. Analyze the requirements and break them into 3-6 milestones.

2. Each milestone must be:
   - A shippable increment — delivers standalone value even if later milestones are never built
   - Ordered by dependency and priority — earlier milestones unlock later ones
   - Scoped clearly — what's IN this milestone and what's deferred

3. For each milestone, write:

   ## Milestone {N}: {name}

   **Goal:** {1-2 sentence description of what this phase delivers}

   **Includes:**
   - {requirement or capability delivered}
   - {requirement or capability delivered}

   **Not yet (deferred to later milestones):**
   - {item explicitly excluded from this phase}

4. Write the milestone breakdown to:
   .bw/plans/{slug}/milestones.md

   Preserve the frontmatter from the template. Add each milestone as a section.

## Milestone sizing guidelines

- Too small: a milestone that takes less than a day is probably a task, not a milestone
- Too big: a milestone that takes more than 2 weeks should be split
- Just right: a milestone that takes 3-7 days of focused work

## Return to conductor

Return:
- Number of milestones created
- One-line summary of each milestone
```

### 3. Receive Summary

The conductor receives the milestone summary from the sub-agent.

### 4. Auto-Proceed

Read `epic-step-04-review.md` and follow it.
