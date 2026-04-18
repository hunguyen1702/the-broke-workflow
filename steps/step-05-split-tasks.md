# Step 5: Split Tasks

**Progress: Step 5 of 6** — Next: Review

## Goal

Decompose the finalized plan into discrete, self-contained task files with explicit dependencies.

## Rules

- Uses the **splitter agent** (a fresh session — separate from the planner session).
- Invoked after `bw plan finalize {slug}`.
- Task descriptions must be **MAXIMALLY SPECIFIC** — exact file paths, function names, pattern references. Vague tasks are failures.
- Each task is self-contained: goal, AC, scope, contracts, boundaries.
- Tasks declare `blocked_by` and `blocks` for DAG integrity.

## Sequence

### 1. Invoke Splitter Agent

The conductor (or user via `/split {slug}`) launches the splitter agent:

```
## Splitter: {slug}

Create task files for plan {slug}.

## Context

Requirements summary:
{1-paragraph from Step 1}

Deliverables:
{bullet list from plan}

Selected approach:
{approach name from plan}

## Read the full plan and discovery

bw plan read {slug} plan
bw plan read {slug} discovery

## Template

Read the task template:
bw plan read tasks task  (or use the template: {plan-slug}/{nnn}-{task-slug}.md)

## Your task

1. Break the plan into 3-8 tasks. Each task must be:
   - Achievable in one session by a single agent
   - Self-contained: can be understood from the task file alone
   - Specific: exact file paths, function names, patterns from discovery

2. For each task:
   - Goal: what this task accomplishes
   - Acceptance Criteria: verifiable outcomes
   - Scope: Files to Read (with WHY), Files to Modify/Create (with WHAT)
   - Contracts: reference by name + location, NEVER paste code
   - Boundaries: what NOT to touch
   - blocked_by: task IDs that must complete first
   - effort: S / M / L

3. File naming: {plan-slug}/{nnn}-{task-slug}.md
   Example: auth-feature-x7k2/001-add-user-model.md
   Number tasks sequentially: 001, 002, 003...

4. Write each task to:
   .bw/tasks/{slug}/{nnn}-{task-slug}.md

## Return to user

Present:
- A summary: "Created {N} tasks for {slug}"
- The DAG: show task IDs, names, and dependencies
- A spot-check prompt: "Review the tasks above. Any missing, unclear, or badly-split?"
```

### 2. User Spot-Check

**HALTs** — wait for user to review the task list and DAG.

- If user approves: proceed to Step 6.
- If user wants changes: adjust task files and re-present.

### 3. Auto-Proceed

Read `step-06-review.md` and follow it.
