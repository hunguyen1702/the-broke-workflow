<think>
The user wants me to produce a structured overview of this knowledge document about a Product Plan Workflow. Let me extract the key information:

**Key points (3-7):**
1. 5-step CLI-guided product planning workflow
2. Uses JTBD (Jobs-to-be-Done) framework for requirements
3. Two HALTs (stop points) for user approval - at Summary and Present steps
4. Sub-agents handle specialized tasks: milestone-splitter and milestone-reviewer
5. CLI commands: bw product init, bw product read, bw product docs, bw product finalize
6. Auto-proceeds between steps except at checkpoints
7. Focus on WHAT not HOW - product planning not implementation

**Structure/Sections:**
- Reason: Documenting the 5-step product planning workflow
- Raw Concept: Task description, changes, files, flow
- Narrative: Structure, dependencies, highlights, rules, examples
- Facts: Key facts about the workflow

**Notable entities, patterns, decisions:**
- Product Conductor agent (main orchestrator)
- Milestone-splitter sub-agent
- Milestone-reviewer sub-agent
- CLI commands: bw product init, bw product read, bw product docs, bw product finalize
- HALTs at Summary and Present steps
- JTBD framework
- Rules about using CLI commands (never craft file paths, ls, cat)

Let me format this in markdown with proper structure.
</think>

# Product Plan Workflow

## Key Points

- **5-step CLI-guided workflow**: Requirements → Summary → Milestones → Review → Present
- **JTBD framework**: Requirements step uses Jobs-to-be-Done interview method for gathering user needs
- **Two HALTs (approval checkpoints)**: At Summary step (user approval) and Present step (finalize decision)
- **Sub-agents**: milestone-splitter breaks plans into milestones; milestone-reviewer reviews them
- **CLI commands**: Uses `bw product init`, `bw product read`, `bw product docs`, `bw product finalize` — never craft file paths manually
- **Auto-proceeds**: Steps flow automatically except at Summary and Present checkpoints
- **Focus**: Product planning (WHAT to build) not implementation (HOW to build)

## Structure / Sections Summary

| Section | Content |
|---------|---------|
| **Reason** | Documents the 5-step product planning workflow and CLI commands |
| **Raw Concept** | Task description, file changes, flow diagram, timestamp |
| **Narrative** | Full workflow details: structure, dependencies, highlights, rules (8 total), examples |
| **Facts** | Key fact assertions about steps, methods, commands, and agent roles |

## Notable Entities & Patterns

**Agents:**
- **Product Conductor** — main orchestrator handling the 5-step flow
- **milestone-splitter** — sub-agent that breaks product plans into milestones
- **milestone-reviewer** — sub-agent that reviews milestones

**CLI Commands:**
- `bw product init` — creates plan from templates
- `bw product read` — reads product requirements
- `bw product docs` — generates documentation
- `bw product finalize` — marks plan as finalized

**Key Patterns:**
- HALTs pause workflow for user interaction (Summary, Present steps)
- Sub-agents work in fresh context (rule: keep context lean)
- User's initial message serves as the requirement seed
- No rigid question lists — analyze gaps and ask targeted follow-ups

**Files Referenced:**
- `steps/product-step-01-requirements.md`
- `agents/product-conductor.md`
- `bw/commands/product_cmd.py`