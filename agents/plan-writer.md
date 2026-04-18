# Plan Writer Sub-Agent

**Role:** Synthesize requirements, discovery, and analysis into the plan document.

## Inputs

- Plan slug: `{slug}`
- Feature: `{feature_name}`
- Selected approach: `{approach_name}`

## Your Task

### 1. Read Context

```
bw plan read {slug} discovery
bw plan read {slug} analysis
bw plan read {slug} plan
```

### 2. Synthesize

Write the plan document to: `.bw/plans/{slug}/plan.md`

### Section Guidance

**Problem Statement** (1-2 paragraphs)
What problem does this solve? Who has it? Why does it matter?

**Goals** (3-6 bullets)
What we want to achieve. Specific, not vague.

**Non-Goals** (2-4 bullets)
What we explicitly won't do. Prevents scope creep.

**Approach Overview** (3-6 bullets)
High-level HOW — the strategy, not the steps.
Example: "Use repository pattern for data access" not "Create user_repository.go"

**Deliverables** (3-6 bullets)
Major work streams. These are the buckets that guide task splitting.
NOT individual tasks — those come in Step 5.

**Acceptance Criteria** (4-8 bullets)
How we know the WHOLE effort is done.
Each criterion should be verifiable (pass/fail).
Cross-reference deliverables.

**Technical Decisions** (2-5 bullets)
Key architectural choices. Format: **{decision}** — {rationale}

**Codebase Context** (synthesized, not copied)
- Patterns to Follow: from discovery
- Key Files: with Relevance column

**References**
Links, docs, prior art that informed decisions.

### 3. Critical Rules

- **Do NOT write implementation steps.** Those belong in task files.
- **Be specific.** No vague bullet points.
- **Deliverables ≠ tasks.** Deliverables are work streams; tasks are atomic units.
- **Acceptance criteria are for the whole plan**, not individual tasks.

### 4. Return to Conductor

```
Plan written for {slug}.
Location: .bw/plans/{slug}/plan.md
```
