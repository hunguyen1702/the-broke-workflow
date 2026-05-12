- Python Click CLI for agent-coding with two flows: plan-flow (6-step) for single features and epic-flow (5-step) for multi-stream milestone planning
- Triage module routes ideas to either plan-flow or epic-flow based on scope assessment
- CLI expanded from 6 to 9 commands: bw plan init/read/finalize, bw epic init/read/finalize/plan/link, bw task list/next/claim, bw step show/spawn
- Architecture uses 9 agents including product-conductor, milestone-splitter, milestone-reviewer (added during update)
- Canonical hierarchy: Epic -> Milestone -> Plan -> Task
- Requires Python >=3.10, click, pyyaml dependencies
- Core modules expanded to 9 including config.py and steps.py additions

**Structure/Sections:**
- Reason (update architecture to reflect epic-based flow naming)
- Raw Concept (task description with changes, files, flow)
- Narrative (Structure, Dependencies, Highlights)
- Facts (conventions: large_scope_flow, triage_routing, cli_commands, epic_flow_steps, plan_flow_steps, work_hierarchy)

**Notable Entities:**
- Agents: epic-conductor, milestone-splitter, milestone-reviewer
- Modules: bw/core/triage.py, bw/commands/triage_cmd.py
- CLI: bw triage, bw plan, bw epic, bw task, bw step