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

0. **Determine operating mode**
   - Read `protocols/autonomous-workflow.md` for mode detection and git workflow
   - If in autonomous mode:
     - Sync workspace: `git fetch origin && git rebase origin/main`
     - Create feature branch: `git checkout -b feat/{agent-name}/scope-{vision-name}`
   - If in manual mode, skip branching — follow the user's lead

1. **Beads setup**
   - If triggered by an existing bead: `bd update <id> --claim` (or `--status in_progress` if already yours)
   - If triggered by user request with no bead: `bd create "Scope: <brief description>" -t task`
   - Read bead context: `bd show <id>` to check description and comments from prior agents

2. **Discover templates** - List available templates:
   ```bash
   ls .claude/templates/
   ```
   Read each template to understand what sections it expects.

3. **Select template** - Choose the template that best fits the vision:
   - `feature.md` — Code feature: adding or changing functionality in a codebase
   - `bug.md` — Code bug: investigating and fixing a defect
   - `knowledge-project.md` — Knowledge work: KB restructures, multi-document ingestions, deliverable production, process improvements
   - `research.md` — Research/analysis: open-ended investigation, comparative analysis, information gathering

   **How to choose**: If the work primarily produces or modifies code, use `feature.md` or `bug.md`. If the work primarily produces or modifies markdown/documents in a knowledge base, use `knowledge-project.md`. If the work is investigative with no predetermined output structure, use `research.md`. Default to `knowledge-project.md` if in a hive-mind context (presence of `knowledge-base/` directory), or `feature.md` if in a codebase.

4. **Research the project** - Explore to understand what exists and what will change:

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

5. **Populate template** - Fill in every section of the template with findings from research. Replace all `<placeholder>` markers with real content.

6. **Write scope file** - Save to `.aur2/plans/queue/<kebab-case-name>/scope.md`
   - Generate name from the vision (max 50 chars, lowercase, hyphens)
   - Create the subdirectory if needed

7. **Submit and hand off**
   - If in autonomous mode:
     - Commit the scope file and push: follow `protocols/autonomous-workflow.md`
     - Create PR with a description noting this is a **scope for review** — include the task breakdown summary and the exact next-step command: `/aur2.execute <full-path-to-scope-file>`
     - Record PR in bead: `bd comments add <id> "Scope PR: {url}. Awaiting user review before execution."`
     - Close the bead: `bd close <id> --reason "Scope produced and submitted for review" --suggest-next`
   - If in manual mode:
     - Tell the user where the scope file was saved
     - Suggest reviewing it before running `/aur2.execute <path>` themselves

   > **Important**: `/aur2.execute` is always a **separate invocation** — never chain to it automatically. The scope must be reviewed and approved by the user before execution begins.

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
