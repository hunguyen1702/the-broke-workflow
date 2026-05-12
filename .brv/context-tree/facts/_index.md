---
children_hash: 225bcb1fcd06905e954c711370387d82ceef93cc66066056d74e5f5b9f6ee55b
compression_ratio: 0.5904082955281919
condensation_order: 2
covers: [context.md, project/_index.md]
covers_token_total: 1543
summary_level: d2
token_count: 911
type: summary
---
<think>
The user wants me to create a structural summary at level d1 (domain level) for "facts/project". I need to preserve key facts, architectural decisions, and relationships while compressing the content significantly (to ~20-30% of the original token count).

Looking at the context, this is a "curate" command where I'm creating or updating a summary file. The summary should:
1. Be at the domain level (facts/project)
2. Preserve key facts
3. Be compressed (~20-30% of original)
4. Include architectural decisions and relationships

I need to output this as a JSON tool call for a UPSERT operation.

Let me construct the summary based on the comprehensive information provided in the context. This is level d1 (domain summary), so I should reference child entries but not duplicate their content.

The key information to preserve:
- 9 core modules, 10 CLI commands, 10 agents
- Two workflow flows (Plan and Product)
- Model configuration system
- Key CLI commands (plan, product, task, step, worktree, triage)
- Triage system (decision tree)
- Task store (statuses, transitions, frontmatter)
- Known gaps (testing, codex adapter)
- Project config (Python ≥3.10, click≥8.0, pyyaml≥6.0)

This needs to be a compact but comprehensive summary that captures the essence of the entire project.
</think>


[TOOL_CALL]
{tool => "code_exec", args => {
  --code "// Curate facts/project domain summary at d1 level\n(async () => {\n  const result = await tools.curate([{\n    type: 'UPSERT',\n    path: 'facts/project',\n    title: 'The Broke Workflow',\n    reason: 'Creating domain-level summary for project facts',\n    summary: 'CLI workflow manager with 9 modules, 10 commands, 10 agents. PLAN (6 steps) and PRODUCT (5 steps) flows, triage router, task store.',\n    content: {\n      rawConcept: {\n        task: 'Domain summary for The Broke Workflow project',\n        flow: 'triage → PLAN/PRODUCT → agents → steps → tasks',\n        files: ['.bw/config.yaml', 'pyproject.toml', 'bw/cli.py', 'bw/core/*.py'],\n        timestamp: '2025-05-12',\n        author: 'Hung Nguyen'\n      },\n      narrative: {\n        structure: '9 core modules (config, frontmatter, lock, paths, slug, steps, task_store, templates, triage) + 10 CLI commands + 10 agents',\n        highlights: 'Two flows: Plan (requirements→discovery→analysis→write-plan→split→review) and Product (requirements→summary→milestones→review→present)',\n        dependencies: 'Python ≥3.10, click≥8.0, pyyaml≥6.0',\n        rules: 'Triage: one-shot router (scope test → knowledge/value-stream test) → Agent() call for conductor. Task states: pending→in_progress→done (terminal)'\n      },\n      relations: [\n        'facts/project/bw_config_module.md',\n        'facts/project/task_store_module.md',\n        'facts/project/triage_command.md',\n        'facts/project/plan_cli_commands.md',\n        'facts/project/product_cli_commands.md',\n        'facts/project/task_cli_commands.md',\n        'facts/project/step_cli_commands.md',\n        'facts/project/triager_agent.md',\n        'facts/project/the_broke_workflow_architecture.md'\n      ]\n    },\n    domainContext: {\n      purpose: 'Project-specific facts: configuration, CLI commands, agents, workflows, and technical decisions',\n      scope: {\n        included: ['CLI commands and subcommands', 'Agent configurations', 'Workflow flows', 'Module architecture', 'Task store schema', 'Triage decision logic', 'Project dependencies'],\n        excluded: ['User-specific preferences', 'External integrations beyond adapters']\n      }\n    }\n  }]);\n  console.log(JSON.stringify(result, null, 2));\n})()"
}}
[/TOOL_CALL]