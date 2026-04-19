# Step 1: Requirements

**Progress: Step 1 of 5** — Next: Summary

## Goal

Understand what the user wants to build. Clarify gray areas through a focused interview. The user has already done their research — this step captures and sharpens their intent, not re-discovers it.

## Rules

- This step is **interactive** — the conductor handles it directly.
- The user's initial message IS the requirement seed. Don't ask them to repeat it.
- **No rigid question list.** Analyze what was said, identify gaps, ask targeted follow-ups.
- Use brainstorming techniques to surface blind spots — but keep it conversational, not mechanical.
- **Auto-proceeds** to Step 2 when coverage is sufficient.

## Sequence

### 1. Accept Initial Input

The user has already described what they want to build. Acknowledge it and move straight into analysis.

### 2. JTBD Lens

Rephrase the user's intent as a Jobs-to-be-Done statement:

> "When [situation], I want to [motivation], so I can [outcome]."

Present this back and ask if it captures the core job. This forces clarity on WHO needs it, WHAT they need, and WHY.

If the user's intent is already crystal clear, skip this — don't be formulaic.

### 3. Clarify Gray Areas

Mentally map the input against these dimensions:

| Dimension | What it covers | When to ask |
|-----------|---------------|-------------|
| **What** | Product/feature being built | Already stated — just confirm understanding |
| **Why** | Motivation, who it's for | Ask if not obvious from context |
| **Boundaries** | What's in/out of scope | Ask if the request is ambiguous or broad |
| **Constraints** | Timeline, tech, resources | Ask only if the user signals these exist |

For each gap, use the **Five Whys** technique lightly: if something is unclear, ask "why is that important?" or "why is that a problem?" 1-2 levels deep to find the real intent. Don't mechanically ask "why" five times.

### 4. Targeted Follow-Ups

If gaps exist, ask 1-2 focused questions per round. Keep them conversational:

- "Is this just the backend API, or does it include the UI?"
- "When you say 'simple auth', do you mean email/password only, or social login too?"
- "Any existing tools or libs you're already committed to using?"

After each round, present a running summary:

> Here's what I have so far:
>
> {summary}
>
> Anything to add or clarify?

The user controls the depth. Simple products may need zero follow-ups.

### 5. Auto-Proceed

Once coverage is sufficient (all non-trivial dimensions addressed), auto-proceed to Step 2. Don't ask for explicit "ready?" confirmation — the summary in Step 2 serves as the review checkpoint.
