- 10 CLI commands: config, doctor, init, install, plan, product, step, task, triage, worktree
- Two workflow flows: Plan flow (6 steps) using discovery/analysis/plan-writer/splitter agents, Product flow (5 steps) using milestone-splitter/milestone-reviewer agents
- Task dependency DAG with claim/release mechanism for atomic task ownership
- Task statuses: pending, in_progress, done
- Product-to-milestone linking with product finalize setting status=finalized
- Worktree uses sparse checkout excluding .bw directory
- Codex adapter deferred past MVP

**Structure:**
- Reason: Documents CLI features from RLM context
- Raw Concept: Task description with changes and file list
- Narrative: Structure (Click CLI), Dependencies (git, Click), Highlights (DAG, claims, worktrees), Rules (3 rules), Examples
- Facts: Structured key-value facts

**Notable entities/patterns:**
- Agents: discovery, analysis, plan-writer, splitter, milestone-splitter, milestone-reviewer
- CLI subcommands: config, doctor, init, install, plan, product, step, task, triage, worktree
- Flow pattern: triage -> (PLAN: step1-6) OR (PRODUCT: step1-5)
- Rule 1: Task claim is atomic
- Rule 2: Product finalize sets status=finalized
- Rule 3: Worktree uses sparse checkout excluding .bw