- Triager agent classifies ideas using decision tree: A (scope test) -> B (knowledge test for single) or C (value-stream test for multi)
- Outputs recommendation as PLAN flow or EPIC flow with grounded reasoning
- EPIC flow recommended when >=2 independent value streams detected
- Plan signals: fix, add, refactor, file/module names, existing codebase references
- Epic signals: MVP, launch, phase, roadmap, platform, multiple subsystems/personas
- Output format: Recommendation, Why (grounded in signals), Path (decision tree path), Next command (bw plan init or bw epic init)
- Rule: Default to PLAN if idea is too sparse

**Structure/Sections:**
- Reason (update triager agent for plan vs epic flow recommendation)
- Raw Concept (task, changes, files, flow)
- Narrative (Structure, Dependencies, Highlights, Rules, Examples)
- Facts (plan_signals, epic_signals, epic_threshold conventions)

**Notable Entities:**
- Decision tree: A (single/multi scope) -> B (knowledge check) or C (value-stream check)
- Output format: Recommendation card with Why, Path, Next command
- Examples: "Add login" -> PLAN, "Build search platform..." -> EPIC