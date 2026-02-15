---
name: hive.groom
description: Audit knowledge base for staleness, inconsistencies, and gaps
disable-model-invocation: false
allowed-tools: Bash, Read, Write, Edit, Glob, Grep, WebFetch, WebSearch
---

# /hive.groom - Groom Mental Model

Proactively audit the KB for staleness, inconsistencies, and gaps.

## Instructions

0. **Determine operating mode**
   - Read `protocols/autonomous-workflow.md` for mode detection and git workflow
   - If in autonomous mode, follow the full lifecycle (sync, branch, work, commit, PR)

1. **Beads setup**
   - If triggered by an existing bead: `bd update <id> --claim` (or `--status in_progress` if already yours)
   - If triggered by user request with no bead: `bd create "Groom: <target section or full KB>" -t task`
   - Read bead context: `bd show <id>` to check description and comments from prior agents

2. **Complexity check**
   - If grooming the full KB and it contains many files, consider using `/aur2.scope` to break the audit into section-by-section beads, then `/aur2.execute`
   - For a targeted section or small KB, proceed directly

3. **Determine scope**
   - If a target section is specified, scope to that section
   - If no target specified, audit the full KB
   - Read `knowledge-base/INDEX.md` to get the file listing

4. **For each file in scope, check:**

   a. **Staleness** - Is `last_verified` in frontmatter older than 30 days?
      - Flag as stale with recommended action (re-verify, update, or archive)

   b. **Contradictions** - Cross-reference with related files:
      - Do dates, facts, or decisions conflict between files?
      - Are team assignments consistent across project and workstream files?
      - Do priorities in strategic-context match what's reflected in projects?

   c. **Gaps** - Are there referenced topics without KB entries?
      - Topics mentioned in one file but not documented elsewhere
      - Team members referenced but without team model files
      - Projects mentioned but without project directories

   d. **Structural issues**
      - Files missing required YAML frontmatter
      - Files not listed in INDEX.md
      - Empty or placeholder files that were never populated

5. **Produce a grooming report**
   Output a structured report with:
   - **Stale items**: File path, last verified date, recommended action
   - **Contradictions**: File paths, conflicting statements, which is likely authoritative
   - **Gaps**: Topic, where it's referenced, suggested KB location
   - **Structural issues**: What's wrong and how to fix it
   - **Questions for user**: Things that cannot be resolved autonomously

6. **Update INDEX.md** if structure changed during grooming

7. **Create follow-up beads** for each remediation item that requires action:
   - `bd create "KB: Update stale entry {file}" -t task`
   - `bd create "KB: Resolve contradiction between {file1} and {file2}" -t task`
   - `bd create "KB: Fill gap - document {topic}" -t task`

8. **Close and hand off**
   - Record what was done: `bd comments add <id> "Groomed {scope}. Found: {N} stale, {N} contradictions, {N} gaps. Created {N} follow-up beads."`
   - Close the bead: `bd close <id> --reason "KB grooming complete for {scope}" --suggest-next`
   - If in autonomous mode, follow `protocols/autonomous-workflow.md` for commit, push, PR
   - Review `--suggest-next` output — follow-up beads created above may now be ready

## Grooming Frequency
- Full KB groom: weekly or when explicitly requested
- Section groom: after any major ingestion into that section
- Quick check: before any deliverable that relies on KB context
