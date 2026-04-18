---
related: [facts/project/the_broke_workflow_architecture.overview.md]
---
<think>
The user wants me to produce a structured overview of the provided knowledge document about Project Config. Let me analyze the document and create a concise markdown overview with:

1. Key points (3-7 bullet points)
2. Structure/sections summary
3. Notable entities, patterns, or decisions

The document is about a Python project configuration with:
- Python >=3.10 requirement
- Dependencies: click>=8.0, pyyaml>=6.0
- CLI entry: bw.cli:main
- No test framework (known gap)
- Files involved: pyproject.toml

Let me create the structured overview following the guidelines.
</think>

# Project Config — Structured Overview

## Key Points
- **Python Version**: Requires Python >=3.10
- **Dependencies**: `click>=8.0`, `pyyaml>=6.0`
- **CLI Entry Point**: `bw.cli:main` (bw CLI tool)
- **Build System**: Configured in `pyproject.toml`
- **Known Gap**: No test framework (pytest) configured — no test files exist
- **Maturity**: Validated (update count: 3)

## Structure / Sections Summary

| Section | Content |
|---------|---------|
| **Files** | `pyproject.toml` — defines metadata, deps, build system, CLI entry |
| **Dependencies** | click (CLI framework), pyyaml (YAML parsing) |
| **Rules** | Testing gap: no pytest in dependencies, no test files in codebase |
| **Facts** | Captured as key-value pairs (test_framework, dependencies, python_version, cli_entry) |

## Notable Entities, Patterns, Decisions

- **Entity**: `bw.cli:main` — CLI entry point using Click
- **Pattern**: Configuration-driven project setup via `pyproject.toml` (PEP 517/518 style)
- **Decision**: Explicitly documenting testing gap as a known limitation rather than ignoring it
- **Tagging**: No tags assigned; importance rated 65; recency 1 (current)