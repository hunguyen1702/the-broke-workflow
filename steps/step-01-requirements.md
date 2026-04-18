# Step 1: Requirements

**Progress: Step 1 of 6** — Next: Discovery

## Goal

Understand what the user wants to build. Establish shared understanding before any analysis begins.

## Rules

- This step is **interactive** — the conductor handles it directly.
- The user's initial message IS the requirement seed. Don't ask them to repeat it.
- **No rigid question list.** Analyze what was said, identify gaps, ask targeted follow-ups.
- **HALTs** at the end to confirm scope before proceeding.
- After confirmation: calls `bw plan init "<title>"` to create the plan folder.

## Sequence

### 1. Accept Initial Input

The user has already described what they want (their first message). Acknowledge it and move straight into analysis — no scripted greeting, no "let me ask you a few questions" preamble.

### 2. Analyze Coverage

Mentally map the user's input against these dimensions:

| Dimension | What it covers | When to ask |
|-----------|---------------|-------------|
| **What** | Feature or change being built | Always required — but the user likely already said this |
| **Why** | Motivation, problem being solved | Ask if the intent is unclear from context |
| **Boundaries** | What's in/out of scope | Ask if the request is ambiguous or could be interpreted broadly |
| **Constraints** | Tech restrictions, known blockers | Ask only if there are signals (e.g. mentions of legacy code, deadlines) |

Skip dimensions that are obvious from context or not relevant to the task.

### 3. Ask Targeted Follow-Ups

If there are gaps, ask 1–2 focused questions. Keep them conversational — no formal "Q1", "Q2" labels. Examples:

- "Are you thinking just the API, or the UI as well?"
- "Should this work with the existing auth, or is that getting replaced too?"
- "Any parts of the codebase you already know are involved?"

After each round of follow-ups, present a running summary and ask:

> Here's what I have so far:
>
> {summary}
>
> Ready to proceed with discovery, or want to clarify anything else?

The user controls the depth. Simple tasks may need zero follow-ups. Complex ones may need several rounds.

### 4. Confirm

Once the user says they're ready, present the final summary:

```
## Scope Confirmed

**Feature:** {what's being built}
**Why:** {motivation — omit if obvious}
**Scope:** {boundaries as bullet list — omit if straightforward}
**Constraints:** {only if relevant}
```

Only include dimensions that were actually discussed. No "none stated" fillers.

**HALTs** — wait for final confirmation.

- If user confirms: proceed to Step 2.
- If user adjusts: update summary and re-present.

### 5. Create Plan

After confirmation, call:

```
bw plan init "<feature title>"
```

This creates `.bw/plans/<slug>/` with plan.md, discovery-report.md, and analysis-report.md templates copied in.
