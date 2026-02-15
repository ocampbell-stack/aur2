---
name: hive.groom
description: Audit knowledge base for staleness, inconsistencies, and gaps
disable-model-invocation: false
allowed-tools: Bash, Read, Write, Edit, Glob, Grep, WebFetch, WebSearch
---

# /hive.groom - Groom Mental Model

Proactively audit the KB for staleness, inconsistencies, and gaps.

**Bead prefix**: `Groom:`

Follow `protocols/skill-lifecycle.md` for setup (mode, beads, complexity check, alignment) and closeout (verify, close and hand off). Then execute the skill-specific steps below.

## Alignment Focus

During preliminary alignment, pay attention to:
- KB size — is this a full audit or targeted section?
- Remediation approach — auto-fix simple issues vs. create follow-up beads for substantive changes?
- Always pause for full-KB grooming or when remediation approach is unclear

## Core Work

1. **Determine scope**
   - If a target section is specified, scope to that section
   - If no target, audit the full KB
   - Read `knowledge-base/INDEX.md` to get the file listing

2. **For each file in scope, check:**

   a. **Staleness** — Is `last_verified` in frontmatter older than 30 days?
      - Flag as stale with recommended action (re-verify, update, or archive)

   b. **Contradictions** — Cross-reference with related files:
      - Do dates, facts, or decisions conflict between files?
      - Are team assignments consistent across project and workstream files?
      - Do priorities in strategic-context match what's reflected in projects?

   c. **Gaps** — Are there referenced topics without KB entries?
      - Topics mentioned in one file but not documented elsewhere
      - Team members referenced but without team model files
      - Projects mentioned but without project directories

   d. **Structural issues**
      - Files missing required YAML frontmatter
      - Files not listed in INDEX.md
      - Empty or placeholder files that were never populated

3. **Produce a grooming report**
   - **Stale items**: File path, last verified date, recommended action
   - **Contradictions**: File paths, conflicting statements, which is likely authoritative
   - **Gaps**: Topic, where it's referenced, suggested KB location
   - **Structural issues**: What's wrong and how to fix it
   - **Questions for user**: Things that cannot be resolved autonomously

4. **Update INDEX.md** if structure changed during grooming

5. **Create follow-up beads** for each remediation item:
   - `bd create "KB: Update stale entry {file}" -t task`
   - `bd create "KB: Resolve contradiction between {file1} and {file2}" -t task`
   - `bd create "KB: Fill gap - document {topic}" -t task`

## Grooming Frequency
- Full KB groom: weekly or when explicitly requested
- Section groom: after any major ingestion into that section
- Quick check: before any deliverable that relies on KB context
