---
title: The Broke Workflow Project Config
summary: 'Python >=3.10, click CLI, pyyaml, setuptools-scm, bw CLI entry. KNOWN GAP: No test framework configured'
tags: []
keywords: []
importance: 100
recency: 1
maturity: core
accessCount: 24
updateCount: 1
createdAt: '2026-04-18T03:42:57.802Z'
updatedAt: '2026-04-18T04:24:30.700Z'
---
## Reason
Adding testing gap - no test framework configured

## Raw Concept
**Task:**
Document project configuration for the-broke-workflow

**Changes:**
- Initial project configuration
- Added testing gap - no test framework configured

**Files:**
- pyproject.toml

**Flow:**
pyproject.toml defines project metadata, dependencies, build system, and CLI entry point

**Timestamp:** 2026-04-18

## Narrative
### Structure
Project uses setuptools with setuptools-scm for automatic versioning. Package includes bw* modules.

### Dependencies
Python >= 3.10 required. Uses click for CLI and pyyaml for config parsing.

### Highlights
CLI entry point bw invokes bw.cli:main. Version managed by setuptools-scm from git tags.

### Rules
KNOWN GAP: No test framework configured. pyproject.toml has no pytest or test dependencies. No test files found in codebase.

## Facts
- **project_name**: Project name is the-broke-workflow [project]
- **version**: Project version is 0.1.0 [project]
- **python_version**: Python requirement is >= 3.10 [project]
- **cli_framework**: CLI framework is click >= 8.0 [project]
- **yaml_library**: YAML library is pyyaml >= 6.0 [project]
- **build_system**: Build system uses setuptools >= 68.0 [project]
- **version_management**: Version management uses setuptools-scm >= 8.0 [project]
- **entry_point**: CLI entry point is bw = bw.cli:main [project]
- **test_framework**: No test framework configured (known gap) [project]
