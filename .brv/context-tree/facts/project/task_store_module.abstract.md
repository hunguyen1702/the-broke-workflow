<think>
The document describes a Task Store Module in bw/core/task_store.py that provides task scanning, retrieval, status transition validation, and comment management for workflow tasks.

Key points:
- Location: bw/core/task_store.py
- Functions: scan_tasks, get_task, validate_transition, add_comment, get_comments
- Valid statuses: pending, in_progress, done
- Status transitions: pending→in_progress, in_progress→done|pending, done is terminal
- Task ID format: plan-slug/nnn-task-slug
- Depends on frontmatter, lock, and paths modules

I need to create a ONE-LINE summary (max 80 tokens) that captures the core topic and key insight.

Let me craft this