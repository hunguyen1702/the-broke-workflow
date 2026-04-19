<think>
The document is about model overrides in .bw/config.yaml for the bw CLI tool. The key points are:
- It's a configuration file for model overrides
- Default model is sonnet
- Conductor uses opus
- Other roles (discovery, analysis, plan-writer, splitter, reviewer, worker) use sonnet
- It's used by the bw CLI on startup

I need to create a ONE-LINE summary (max 80 tokens) that captures the core topic and key insight.

Let me draft:
"The .bw/config.yaml file enables per-task model overrides in bw CLI, defaulting to sonnet while conductor uses opus for orchestration and other roles use sonnet."

That's about 26 tokens, well under 80.