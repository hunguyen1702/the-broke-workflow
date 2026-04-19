<think>
The user wants me to produce a structured overview of the knowledge document about the Task Store Module. Let me analyze the document and extract the key information.

Key points to include:
1. Module location and purpose (bw/core/task_store.py)
2. Core functions: scan_tasks, get_task, validate_transition, add_comment, get_comments
3. Valid statuses simplified to {pending, in_progress, done}
4. Status transition rules
5. Task ID format pattern
6. Dependencies on other modules
7. Rules for task management

Structure/Sections:
- Reason: Documenting task_store.py
- Raw Concept: Changes and files
- Narrative: Structure, Dependencies, Highlights, Rules, Examples

Notable entities:
- Module: bw/core/task_store.py
- Commands: bw/commands/task_cmd.py
- Dependencies: bw.core.frontmatter, bw.core.lock, bw.core.paths
- Functions: scan_tasks, get_task, validate_transition, add_comment, get_comments
- Valid statuses: pending, in_progress, done
- Task ID format: {plan-slug}/{nnn}-{task-slug}

Let me format this as requested - under 1500 tokens, markdown only, no preamble.
</think>

# Task Store Module

## Key Points

- **Module location**: `bw/core/task_store.py` provides task scanning, retrieval, validation, and comment management for workflow tasks
- **Core functions**: `scan_tasks()`, `get_task()`, `validate_transition()`, `add_comment()`, `get_comments()`
- **Valid statuses simplified** to `pending`, `in_progress`, `done` (removed `ready`, `blocked`)
- **Status transitions**: `pending→in_progress`, `in_progress→{done,pending}`, `done` is terminal (no outgoing transitions)
- **Task ID format**: `{plan-slug}/{nnn}-{task-slug}` (e.g., "plan-001/my-task")
- **Locking required**: Comment writes must acquire locks to prevent race conditions

## Structure Summary

| Section | Content |
|---------|---------|
| **Reason** | Documenting task_store.py module |
| **Raw Concept** | Changes: status simplification, transition rules, task_block→task_add-dependency replacement |
| **Narrative** | Full module documentation with structure, dependencies, highlights, rules, examples |

## Dependencies

- `bw.core.frontmatter` — `read_file`, `write_file`
- `bw.core.lock` — `acquire`, `release`
- `bw.core.paths` — `find_bw_root`, `plan_tasks_dir`, `tasks_dir`

## Rules

1. **Task ID format**: Must be `plan-slug/task-slug`
2. **Status validation**: Transitions must pass `validate_transition()` before being allowed
3. **Comment requirements**: Both non-empty `text` and `author` required
4. **Concurrency**: Lock acquisition required for comment writes

## Examples

```
validate_transition("pending", "in_progress") → True
scan_tasks(status_filter="pending") → yields pending tasks only
```

## Related Files

- `bw/core/task_store.py` — main module
- `bw/commands/task_cmd.py` — command layer
- `facts/project/the_broke_workflow_project_config.md` — related config