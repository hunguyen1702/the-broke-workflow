# Step 6: Review

**Progress: Step 6 of 6** — Complete

## Goal

Adversarial review of the plan document, task files, and DAG integrity. Catch gaps, inconsistencies, and false assumptions before execution begins.

## Rules

- The **conductor** spawns a reviewer sub-agent.
- Reviews both the plan and all task files.
- Identifies critical issues — not style preferences.
- Applies fixes only for critical correctness issues.

## Sequence

### 1. Spawn Reviewer Sub-Agent

```
## Review: {slug}

Adversarial review of the plan and all task files for {slug}.

## Read everything

bw plan read {slug} plan
bw plan read {slug} discovery
bw plan read {slug} analysis

List all task files:
bw task list --plan {slug}

For each task:
bw task show {plan-slug}/{nnn}-{task-slug}

## Review checklist

For each item, answer YES / NO / PARTIAL and note the finding:

1. Plan Completeness
   - Does the plan cover all stated goals?
   - Are non-goals clearly delineated?
   - Are acceptance criteria verifiable?

2. Task Decomposition
   - Is each task achievable in one session?
   - Are tasks too coarse (>1 day of work) or too fine (trivial)?
   - Are task scopes specific enough (file paths, function names)?
   - Do task ACs map to plan acceptance criteria?

3. DAG Integrity
   - Are all blocked_by dependencies correct?
   - Are there cycles in the DAG?
   - Are all blocks references reciprocated in blocked_by?

4. Contract Clarity
   - Do tasks reference contracts by name + location?
   - Are boundaries clearly stated?

5. Redundancy Check
   - Is any work described in multiple tasks?
   - Are deliverables uniquely owned by one task?

6. Verification
   - Can a worker complete each task from the task file alone?
   - Are there gaps where plan context would be required?

## Return to conductor

Format findings as:

### Critical Issues (fix before execution)
- {issue} → {suggestion}

### Suggestions (consider, may skip)
- {suggestion}

### Summary
- {N} critical, {N} suggestions
```

### 2. Present Findings

The conductor presents the review findings.

### 3. Apply Fixes

Critical issues are fixed by the conductor or re-delegated to sub-agents. Suggestions are noted but execution may proceed.

### 4. Complete

> **Review complete.** The plan is ready for execution.
>
> Next steps:
> - `bw task next` — see ready tasks
> - `/work <task-id>` — claim and execute a task
> - `bw task dag --plan {slug}` — view the full DAG
