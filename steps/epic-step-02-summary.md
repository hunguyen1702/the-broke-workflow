# Step 2: Summary

**Progress: Step 2 of 5** — Next: Milestones

## Goal

Write a clean requirements document from the interview. Present it for user review and approval before proceeding to milestone breakdown.

## Rules

- This step is **interactive** — the conductor handles it directly.
- **HALTs** at the end for user review.
- After approval: calls `bw epic init "<title>"` and writes requirements into the plan file.

## Sequence

### 1. Write Requirements Summary

Synthesize everything from Step 1 into a structured summary. Use these sections:

```
## What We're Building

{One paragraph: what is this and why does it matter}

## Target Users

{Who is this for? What job are they hiring this epic to do?}

## Core Requirements

- {Requirement 1 — what must exist, not how to build it}
- {Requirement 2}
- ...

## Boundaries

### In Scope
- ...

### Out of Scope
- ...

## Constraints
{Only include if relevant — timeline, tech stack, resources, dependencies}
```

**Rules for writing:**
- Focus on WHAT, never HOW. "Users can sign in with email" not "Build a JWT auth system."
- Each requirement should be testable: you can look at the epic and say "yes this exists" or "no it doesn't."
- Keep it concise. If a section has nothing meaningful, omit it entirely.

### 2. Present for Review

> Here's the requirements summary for your epic plan:
>
> {formatted summary}
>
> Does this capture everything? Any changes before I proceed to milestone breakdown?

**HALTs** — wait for user review.

- If user approves: proceed to Step 3.
- If user adjusts: update and re-present.

### 3. Create Epic Plan

After approval, call:

```
bw epic init "<title>"
```

This creates `.bw/plans/<slug>/epic.md` with the requirements filled in.

Then write the approved requirements into the epic plan file at `.bw/plans/{slug}/epic.md`.

### 4. Auto-Proceed

Read `epic-step-03-milestones.md` and follow it.
