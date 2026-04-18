# Step 2: Discovery

**Progress: Step 2 of 6** — Next: Analysis

## Goal

Conduct targeted codebase analysis to gather patterns, constraints, and references. Sub-agents do the heavy exploration; conductor receives a compact summary.

## Rules

- This step **auto-triggers** after Step 1 confirmation.
- The **conductor** spawns a discovery sub-agent with full requirements context.
- Sub-agents access document templates **exclusively** via `bw plan read {slug} discovery`.
- Conductor receives: **3-5 bullet summary** (NOT the full report).

## Sequence

### 1. Inform User

> Exploring the codebase for patterns, constraints, and references. Stand by while I compile findings.

### 2. Spawn Discovery Sub-Agent

The conductor spawns ONE discovery sub-agent with this prompt template:

```
## Discovery: {feature_name}

Fill in the discovery report for plan {slug}.
- Requirements summary: {Q1-Q5 from Step 1}
- Requirements: {Q2 outcome}

## Your task

1. Read the discovery report template:
   bw plan read {slug} discovery

2. Explore the codebase and populate the following sections:
   - Architecture Snapshot (modules relevant to this feature, with WHY)
   - File-Level Scope Map (files/dirs in play, with WHY)
   - Existing Patterns (similar implementations, naming conventions)
   - Reusable Utilities
   - Technical Constraints
   - Testing Context

3. Only spawn sub-sub-agents for: codebase analysis, constraints. Skip external docs unless this feature involves external libraries/APIs.

4. Write the completed report to:
   .bw/plans/{slug}/discovery-report.md

## Return to conductor

Return a 3-5 bullet summary of the most important findings, formatted as:
- Finding + implication for this feature
```

### 3. Receive Summary

The conductor receives the 3-5 bullet summary from the sub-agent. The full report lives in the artifact.

### 4. Present Summary

```
## Discovery Complete

{3-5 bullets from sub-agent}

Full report: `bw plan read {slug} discovery`
```

### 5. Auto-Proceed

Read `step-03-analysis.md` and follow it.
