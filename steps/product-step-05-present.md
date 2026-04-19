# Step 5: Present

**Progress: Step 5 of 5** — Complete

## Goal

Present the milestone breakdown and reviewer feedback to the user. User decides whether to accept, adjust, or redo.

## Rules

- This step is **interactive** — the conductor handles it directly.
- **HALTs** at the end for user decision.

## Sequence

### 1. Present Milestones

Show each milestone in a compact format:

```
## Milestone Breakdown

### Milestone 1: {name}
{goal}
- {included item 1}
- {included item 2}

### Milestone 2: {name}
{goal}
- {included item 1}
- {included item 2}

... (all milestones)
```

### 2. Present Review Feedback

Show the reviewer's findings:

```
## Review Feedback

**Verdict:** {GOOD / NEEDS WORK / RETHINK}

### Issues
- {issue → suggestion}

### Suggestions
- {suggestion}
```

If the verdict is GOOD with no issues, keep it brief:

> Review passed with no issues. {N} optional suggestions noted.

### 3. Ask for Decision

> **What would you like to do?**
>
> 1. **Accept** — finalize this product plan and milestone breakdown
> 2. **Adjust** — tell me specific changes and I'll update the milestones
> 3. **Redo** — go back to milestone splitting with different guidance

**HALTs** — wait for user decision.

- If **Accept**: call `bw product finalize {slug}` and complete the flow.
- If **Adjust**: update milestones directly based on user feedback, re-present.
- If **Redo**: go back to Step 3 with the user's additional guidance included in the splitter prompt.

### 4. Complete

After finalization:

> **Product plan finalized.**
>
> - Requirements: `bw product read {slug} requirements`
> - Milestones: `bw product read {slug} milestones`
>
> To start technical planning for a milestone, use:
> - `bw product plan {slug} 1` — creates a plan linked to Milestone 1
