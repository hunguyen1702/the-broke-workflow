- Epic flow is 5-step milestone planning: Requirements -> Summary -> Milestones -> Review -> Present -> finalize
- Managed by epic-conductor agent, delegates to milestone-splitter and milestone-reviewer sub-agents
- Hard-renamed from product flow to epic flow throughout codebase
- CLI: bw epic init/read/finalize/plan/link commands
- Canonical hierarchy: Epic -> Milestone -> Plan -> Task
- Document storage: .bw/plans/<slug>/epic.md and milestones.md
- Milestone-splitter breaks work into shippable phases; milestone-reviewer reviews milestone plans
- Step flow parameter: --flow epic (not product)

**Structure/Sections:**
- Reason (create/update epic flow architecture replacing old product flow)
- Raw Concept (changes, files, flow)
- Narrative (Structure, Dependencies, Highlights)
- Facts (epic_flow_steps, sub_agents, document_access conventions)

**Notable Entities:**
- Sub-agents: milestone-splitter, milestone-reviewer, epic-conductor
- Files: bw/commands/epic_cmd.py, templates/epic.md, agents/epic-conductor.md
- Steps: Requirements (JTBD), Summary (user review/HALTs), Milestones, Review, Present
- Document access: bw epic read {slug} requirements|milestones