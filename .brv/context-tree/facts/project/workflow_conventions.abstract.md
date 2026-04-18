<think>
The user wants a one-line summary (max 80 tokens) of this workflow conventions document. The key points are:

1. Task ID format: {plan-slug}/{nnn}-{task-slug}
2. YAML frontmatter fields: id, title, status, blocked_by, blocks, owner, effort
3. Status machine: pending → ready/in_progress → done, with blocked as intermediate
4. Sub-agent instructions: give only slug, what to read, what to write, what to return
5. Python naming: snake_case
6. Lean context principle

The core topic is workflow conventions for a task management system. The key insight seems to be about standardization - standardizing task IDs, YAML frontmatter,