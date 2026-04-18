# Step 3: Analysis

**Progress: Step 3 of 6** — Next: Write Plan

## Goal

Evaluate implementation approaches using either pattern-based selection or multi-approach scoring. Present all options as decision cards for the user to choose.

## Rules

- This step **auto-triggers** — proceed without waiting for user input.
- **Conductor** spawns an analysis sub-agent.
- Conductor presents **ALL approaches** as decision cards to the user.
- **HALTs** for user to pick before proceeding.

## Sequence

### 1. Spawn Analysis Sub-Agent

```
## Analysis: {feature_name}

Fill in the analysis report for plan {slug}.

## Your task

1. Read the discovery report:
   bw plan read {slug} discovery

2. Read the analysis report template:
   bw plan read {slug} analysis

3. Evaluate approaches:
   - PATH T (Trivial): if the change is trivially obvious (config tweak, 1-2 file edit)
   - PATH A (Pattern-Based): if a direct pattern match exists in the codebase
   - PATH B (Multi-Approach): otherwise — evaluate 3 distinct approaches

4. For each approach:
   - Describe implementation strategy
   - Score against 9 criteria (1-10 each)
   - Note effort/complexity (S/M/L)
   - Identify key risks and benefits

5. Rank and recommend:
   - Present comparison table
   - Mark the highest-scoring as recommended
   - Note trade-offs

6. Write the completed report to:
   .bw/plans/{slug}/analysis-report.md

## Return to conductor

Return your findings formatted EXACTLY as decision cards:

| # | Approach | Effort | Key Risk | Score |
|---|----------|--------|----------|-------|
| 1 | {name} ⭐ Recommended | M | {risk} | {score} |
| 2 | {name} | S | {risk} | {score} |
| 3 | {name} | L | {risk} | {score} |

**Why #N:** {rationale}
**Trade-off:** {what you give up}
```

### 2. Present Decision Cards

The conductor presents the decision cards from the sub-agent:

```
## Approach Evaluation

| # | Approach | Effort | Key Risk | Score |
|---|----------|--------|----------|-------|
| ...filled in from sub-agent...

**Why {recommended}:** {rationale}
**Trade-off:** {trade-off}
```

### 3. User Checkpoint

> **Pick an approach** — enter a number (1, 2, 3) to select, or describe adjustments you'd like to see.

**HALTs** — wait for user input.

- If user picks a number: use that approach, proceed.
- If user wants adjustments: update the approach and re-present.

### 4. Record Selection

After user picks, update the analysis report's selected approach field via the sub-agent, or directly:

```
bw plan read {slug} analysis
# Sub-agent or conductor updates the "Selected Approach" frontmatter
```

### 5. Auto-Proceed

Read `step-04-write-plan.md` and follow it.
