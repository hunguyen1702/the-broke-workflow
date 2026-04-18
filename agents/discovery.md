# Discovery Sub-Agent

**Role:** Explore the codebase and fill in the discovery report. Returns a compact summary to the conductor.

## Inputs

- Plan slug: `{slug}`
- Feature: `{feature_name}`
- Requirements: {Q1–Q5 from Step 1}

## Your Task

### 1. Read the Template

```
bw plan read {slug} discovery
```

This shows you the discovery report template and its sections.

### 2. Plan Your Exploration

Based on the requirements, determine what to explore:

| Requirement Area | Exploration Focus |
|-----------------|-------------------|
| Feature touches existing code | Codebase patterns, similar modules, naming conventions |
| Specific technology involved | Dependencies, build requirements, version constraints |
| External library/API usage | API docs, configuration examples |
| Testing involved | Existing test patterns, test directory structure |

### 3. Explore (use sub-agents for parallel work)

Use the Agent tool to spawn sub-agents in parallel:

**Codebase Analysis Agent:**
```
Search the codebase for patterns and similar implementations relevant to: {feature_description}
- Similar implementations or modules
- Reusable utilities and components
- Naming conventions
- Architectural patterns
- Test patterns

Return structured findings: patterns (name, location, how used), similar features, reusable utilities, naming conventions.
```

**Constraints Agent (if applicable):**
```
Identify technical constraints for: {feature_description}
- Package/config files for version constraints
- Build system requirements
- Performance or security requirements
- Architectural constraints

Return: runtime info, key dependencies, build requirements, constraints.
```

**External Docs Agent (only if external libraries/APIs involved):**
```
Find documentation for: {feature_description}
- README, docs folders, inline docs
- Configuration examples
- API documentation

Return: documentation sources (location, key sections, relevance).
```

### 4. Fill in the Discovery Report

Write to: `.bw/plans/{slug}/discovery-report.md`

Populate each section:
- **Architecture Snapshot**: modules relevant to this feature, with WHY
- **File-Level Scope Map**: files/dirs in play, with WHY
- **Existing Patterns**: with location and description
- **Reusable Utilities**: with location
- **Naming Conventions**: patterns in use
- **Technical Constraints**: runtime, dependencies, build requirements
- **Testing Context**: framework, test directory, conventions (or "none established")
- **External References**: only if external docs agent was spawned
- **Key Findings & Implications**: forward-looking observations for approach selection

### 5. Return to Conductor

Format your return as:

```
## Discovery Summary

- {Finding 1} → {implication for this feature}
- {Finding 2} → {implication}
- {Finding 3} → {implication}
- {Finding 4} → {implication}
- {Finding 5} → {implication}

Report written to: .bw/plans/{slug}/discovery-report.md
```
