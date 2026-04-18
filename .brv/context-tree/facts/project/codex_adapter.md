---
title: Codex Adapter
summary: Codex adapter deferred past MVP, mirrors Claude Code adapter using AGENTS.md conventions
tags: []
related: [facts/project/cli_tool_integrations.md]
keywords: []
importance: 68
recency: 1
maturity: validated
accessCount: 6
createdAt: '2026-04-18T04:28:44.769Z'
updatedAt: '2026-04-18T04:28:44.769Z'
---
## Reason
Documenting the deferred Codex adapter implementation

## Raw Concept
**Task:**
Document Codex adapter architecture and implementation status

**Changes:**
- Codex adapter status set to deferred past MVP

**Files:**
- adapters/codex/README.md

**Flow:**
Define agents in AGENTS.md -> Reference agents/ prompts -> Define commands -> Deploy via bw install

**Timestamp:** 2026-04-18

**Author:** the-broke-workflow

## Narrative
### Structure
Codex adapter at adapters/codex/ with README.md. Uses AGENTS.md conventions instead of Claude Code skill/command format.

### Dependencies
Requires AGENTS.md implementation, depends on adapters/claude-code/ as reference implementation

### Highlights
Status: Deferred past MVP. Planned files: agents.md (Codex agents config), commands/ (command wrappers). Deployment: bw install --tool codex --scope project/global.

### Rules
Rule 1: Must mirror Claude Code adapter structure
Rule 2: Agents defined in AGENTS.md must reference agents/ directory prompts
Rule 3: Commands must shell out to bw CLI
Rule 4: Only implement after MVP complete

### Examples
Example deployment: bw install --tool codex --scope project
Example agent reference in AGENTS.md: See adapters/claude-code/ for porting reference

## Facts
- **codex_adapter_status**: Codex adapter is deferred past MVP [project]
- **project_version**: Project version is 0.1.0 (early stage) [project]
- **code_quality_gap**: No linting or testing configured [project]
- **codex_convention**: Codex uses AGENTS.md files for agent configuration [project]
