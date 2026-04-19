# Step 4: Review

**Progress: Step 4 of 5** — Next: Present

## Goal

Adversarial review of the milestone breakdown. Catch gaps, bad ordering, scope creep, and sizing issues before presenting to the user.

## Rules

- The **conductor** spawns a milestone-reviewer sub-agent.
- Reviews both the requirements and the milestone breakdown.
- Identifies issues — not style preferences.

## Sequence

### 1. Spawn Reviewer Sub-Agent

```
## Review: {slug}

Review the milestone breakdown for product plan {slug}.

## Read everything

bw product read {slug} requirements
bw product read {slug} milestones

## Review checklist

For each item, answer YES / NO / PARTIAL:

1. Coverage
   - Does every core requirement appear in at least one milestone?
   - Are there milestones that include work not in the requirements? (scope creep)

2. Standalone Value
   - Can each milestone be shipped independently?
   - Does each milestone deliver something a user can actually use or see?

3. Ordering
   - Are dependencies ordered correctly? (milestone N shouldn't need milestone N+1)
   - Is the highest-value or highest-risk work front-loaded?

4. Sizing
   - Are any milestones too large (>2 weeks)? Suggest splitting.
   - Are any milestones too small (<1 day)? Suggest merging.
   - Are milestones roughly balanced in effort?

5. Gaps
   - Is anything missing that would prevent milestone 1 from being usable?
   - Are "not yet" items properly captured and assigned to later milestones?

## Return to conductor

Format findings as:

### Issues (should fix)
- {issue} → {suggestion}

### Suggestions (consider)
- {suggestion}

### Verdict
- {N} issues, {N} suggestions
- Overall assessment: GOOD / NEEDS WORK / RETHINK
```

### 2. Receive Review

The conductor receives the review findings from the sub-agent.

### 3. Auto-Proceed

Read `product-step-05-present.md` and follow it.
