---
title: Triage Command Integration
summary: bw triage is a CLI command that outputs an Agent(...) call for the conductor to execute. It does NOT halt for confirmation - the conductor receives and runs the triager agent which recommends PLAN or PRODUCT flow.
tags: []
related: []
keywords: []
createdAt: '2026-05-12T14:55:32.004Z'
updatedAt: '2026-05-12T14:55:32.004Z'
---
## Reason
Documenting how bw triage integrates with the conductor

## Raw Concept
**Task:**
Document bw triage integration with conductor

**Changes:**
- Documented triage_cmd.py CLI structure
- Documented core/triage.py rendering
- Documented triager.md agent decision tree

**Files:**
- bw/commands/triage_cmd.py
- bw/core/triage.py
- agents/triager.md

**Flow:**
User runs `bw triage <idea> --tool <tool>` → CLI detects codebase → render_triage_call() → outputs Agent(...) for conductor

**Timestamp:** 2026-05-12

## Narrative
### Structure
triage_cmd.py is the CLI entry point. core/triage.py renders the Agent(...) call by substituting {idea} and {has_codebase} into triager.md template. The triager agent executes the decision tree and outputs recommendation.

### Dependencies
Requires .brv/context-tree/facts/project/triager_agent.md for triager agent knowledge

### Highlights
Triage does NOT halt for user confirmation. It outputs Agent(...) call that conductor copies verbatim. The triager recommends PLAN (single feature) or PRODUCT (multi-stream) flow.

### Rules
Rule 1: triage outputs Agent(...) call, not the recommendation directly
Rule 2: Conductor executes the Agent call to get recommendation
Rule 3: No user confirmation - fully automated flow

## Facts
- **triage_invocation**: bw triage is invoked via CLI with `bw triage <idea> --tool <claude-code.codex>` [project]
- **codebase_detection**: triage detects codebase using _detect_codebase() - checks for .git/ and code files [project]
- **conductor_integration**: triage outputs an Agent(...) call that the conductor copies verbatim [project]
- **user_confirmation**: triage does NOT halt for user confirmation - it outputs the Agent call and exits [project]
- **flow_recommendation**: The triager agent recommends PLAN flow or PRODUCT flow based on decision tree [project]
- **decision_tree**: Decision tree: Scope test (single vs multi) → Knowledge test (for single) → Value-stream test (for multi) [project]
- **flow_definitions**: PLAN flow: single feature, implementation-focused. PRODUCT flow: multi-stream, milestone-focused [project]
- **component_relationship**: triage_cmd.py, core/triage.py, and agents/triager.md work together: CLI → renderer → agent logic [project]
