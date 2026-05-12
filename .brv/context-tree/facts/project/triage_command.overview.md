- bw triage command classifies user ideas as plan-flow (single feature) or epic-flow (multi-stream)
- Uses decision tree logic: A) scope test (single vs multi), B) knowledge test (for single), C) value-stream test (for multi)
- Detects codebase presence via .git directory and code file extensions outside build/cache dirs
- Routing changed from PLAN vs PRODUCT to plan-flow vs epic-flow terminology
- Returns Agent(...) call with next command for tool execution
- Requires --tool option (claude-code or codex) per Rule 1
- Supports claude-code and codex tools for output

**Structure/Sections:**
- Reason (update triage command for plan-flow vs epic-flow routing)
- Raw Concept (changes, files, flow)
- Narrative (Structure, Dependencies, Highlights, Rules)
- Facts (triage_routing, decision_tree, codebase_detection conventions)

**Notable Entities:**
- Files: bw/core/triage.py, bw/commands/triage_cmd.py, agents/triager.md
- Functions: render_triage_call, _detect_codebase, read_agent_file
- Config: triager: haiku added to default_config
- Decision tree paths: A (scope), B (knowledge), C (value-stream)