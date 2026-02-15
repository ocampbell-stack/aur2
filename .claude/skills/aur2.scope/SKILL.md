---
name: aur2.scope
description: Research the project and produce a scope file from a template
argument-hint: <vision description>
disable-model-invocation: false
allowed-tools: Bash, Read, Write, Edit, Glob, Grep, WebFetch, WebSearch
---

# Scope Task

Research the project against a user's vision, select a template, populate it, and write a scope file.

## Input

The argument is a vision description - what the user wants to achieve.

## Steps

1. **Discover templates** - List available templates:
   ```bash
   ls .claude/templates/
   ```
   Read each template to understand what sections it expects.

2. **Select template** - Choose the template that best fits the vision:
   - `feature.md` — Code feature: adding or changing functionality in a codebase
   - `bug.md` — Code bug: investigating and fixing a defect
   - `knowledge-project.md` — Knowledge work: KB restructures, multi-document ingestions, deliverable production, process improvements
   - `research.md` — Research/analysis: open-ended investigation, comparative analysis, information gathering

   **How to choose**: If the work primarily produces or modifies code, use `feature.md` or `bug.md`. If the work primarily produces or modifies markdown/documents in a knowledge base, use `knowledge-project.md`. If the work is investigative with no predetermined output structure, use `research.md`. Default to `knowledge-project.md` if in a hive-mind context (presence of `knowledge-base/` directory), or `feature.md` if in a codebase.

3. **Research the project** - Explore to understand what exists and what will change:

   **For codebases** (source code, application logic):
   - Existing architecture and patterns
   - Files that will be affected
   - Constraints and dependencies
   - How similar features are implemented

   **For knowledge bases** (markdown repos, hive-mind instances):
   - Read `knowledge-base/INDEX.md` to understand current coverage
   - Identify which KB sections are relevant to the vision
   - Check for existing entries that overlap with or relate to the work
   - Review protocols that govern the work (e.g., compound deliverable, privacy standards)
   - Identify gaps where new entries will be needed

   **For mixed contexts**: Do both. Some projects have code and knowledge base components.

4. **Populate template** - Fill in every section of the template with findings from research. Replace all `<placeholder>` markers with real content.

5. **Write scope file** - Save to `.aur2/plans/queue/<kebab-case-name>/scope.md`
   - Generate name from the vision (max 50 chars, lowercase, hyphens)
   - Create the subdirectory if needed

6. **Report** - Tell the user where the scope file was saved and suggest reviewing it before running `/aur2.execute`

## Task Format

The task list in the scope file MUST use the standard epic task format so it is compatible with `create_beads` parsing:

```
N. [ ] <Task title> - <Brief description>
N. [ ] <Task title> (depends on X, Y) - <Brief description>
```

Number tasks sequentially across phases. Dependencies reference task numbers.

## Guidelines

- Research thoroughly before writing - read relevant files, understand existing structure and patterns
- Tasks should be actionable and specific
- A task should do one thing: research, create/modify, or verify - not all three
- Each task should be completable in one work session
- Dependencies should form a DAG (no cycles)
- Keep phases to 3-5 tasks each
- Include a Dependencies section summarizing the dependency graph
