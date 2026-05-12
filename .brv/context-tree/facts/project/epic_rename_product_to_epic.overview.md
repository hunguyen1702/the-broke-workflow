- Canonical hierarchy: Epic -> Milestone -> Plan -> Task
- CLI renamed from `bw product` to `bw epic` (init/list/docs/read/finalize/plan/status/link/remove)
- Flow flag renamed from `--flow product` to `--flow epic`
- Frontmatter key renamed from `product:` to `epic:`
- Tests verify legacy product flow is rejected and epic features work correctly
- Model key is epic-conductor; requires EPIC_STEP_META and EPIC_STEP_AGENTS in bw/core/steps.py

**Structure:** Document has Reason, Raw Concept (Task/Changes/Files/Flow/Timestamp), Narrative (Structure/Dependencies/Highlights/Rules/Examples), and Facts sections.

**Notable:** Files modified include CLAUDE.md, bw/commands/epic_cmd.py, bw/core/steps.py, agents/epic-conductor.md, tests/test_epic_flow.py. Epic docs stored at .bw/plans/<slug>/epic.md.