<think>
The user wants me to produce a structured overview of the knowledge document about Product CLI Commands. Let me analyze the document and extract the key information.

Key points from the document:
1. Five CLI commands: init, list, docs, read, finalize
2. Lifecycle flow: init → list/docs/read → finalize
3. Dependencies on bw.core modules
4. Rules for each command
5. Document naming conventions
6. Related files and workflows

Let me structure this into a clear markdown overview.
</think>

# Product CLI Commands Overview

## Key Points

- **Five CLI commands** manage the product plan lifecycle: `bw product init`, `list`, `docs`, `read`, and `finalize`
- **Lifecycle flow**: init → list/docs/read → finalize
- **Init command**: Creates product plans from templates; requires unique title (fails if duplicate)
- **List command**: Displays all plans with slug, status, and summary
- **Finalize command**: Freezes a product plan and records the finalization date
- **Document mapping**: Friendly names map to filenames (e.g., `requirements` → `product-plan.md`, `milestones` → `milestones.md`)
- **Core dependencies**: Uses `bw.core.paths`, `bw.core.frontmatter`, `bw.core.slug`, and `bw.core.templates`

## Structure / Sections Summary

| Section | Content |
|---------|---------|
| **Reason** | Documents CLI commands for product plan management |
| **Flow** | init → list/docs/read → finalize |
| **Commands** | init (create), list (show all), docs (list docs), read (print doc), finalize (freeze) |
| **Dependencies** | Core modules: paths, frontmatter, slug, templates |
| **Rules** | Five rules governing command behavior (unique titles, output format, name resolution) |
| **Facts** | Five fact statements defining each CLI command |

## Notable Entities, Patterns, Decisions

- **Files**: `bw/commands/product_cmd.py` (implementation location)
- **Related documents**: `facts/project/product_plan_workflow.md`, `facts/project/cli_tool_integrations.md`
- **Status tracking**: Plans have a status field that updates to "finalized" upon completion
- **Slug-based identification**: Plans identified by slug rather than title
- **Flexible document access**: `read` accepts both friendly names and filenames
- **Template-based creation**: `init` uses templates from `bw.core.templates`