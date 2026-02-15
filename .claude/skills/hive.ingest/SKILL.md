---
name: hive.ingest
description: Ingest documents or notes into the hive-mind knowledge base
disable-model-invocation: false
allowed-tools: Bash, Read, Write, Edit, Glob, Grep, WebFetch, WebSearch
---

# /hive.ingest - Update Mental Model

Ingest new documents, notes, or external context into the knowledge base.

## Instructions

0. **Determine operating mode**
   - Read `protocols/autonomous-workflow.md` for mode detection and git workflow
   - If in autonomous mode, follow the full lifecycle (sync, branch, work, commit, PR)

1. **Beads setup**
   - If triggered by an existing bead: `bd update <id> --claim` (or `--status in_progress` if already yours)
   - If triggered by user request with no bead: `bd create "Ingest: <brief description>" -t task`
   - Read bead context: `bd show <id>` to check description and comments from prior agents

2. **Complexity check**
   - If the request involves multiple documents or will require more than one session, escalate to `/aur2.scope` to produce a scope PR for user review. Close this bead with a note pointing to the scope. Execution via `/aur2.execute` happens separately after the user approves the scope.
   - For a single document or focused ingestion, proceed directly

3. **Preliminary alignment**
   - Read `knowledge-base/INDEX.md` and identify KB sections relevant to the source material
   - Read those sections to understand what already exists
   - Assess: Will this create new files or update existing ones? Does it overlap with or contradict current entries? What structural decisions need to be made (which directory, naming)?
   - Present to user: context found, proposed placement, any questions about scope or interpretation
   - **Always pause** (use `AskUserQuestion`) when: creating new files, reorganizing existing structure, request is ambiguous, or you are making assumptions
   - **State plan and proceed** when: updating a single existing file with clear factual changes, or following explicit detailed instructions
   - When in doubt, pause — the cost of asking is always lower than the cost of rework

4. **Read the provided document(s) or notes**
   - Accept input as: pasted text, file paths, URLs, or conversation context
   - Identify the document type: meeting notes, strategic doc, project charter, status update, etc.

5. **Consult `knowledge-base/INDEX.md`**
   - Find relevant existing KB sections
   - Determine if this is a new topic or an update to existing content

6. **Extract key information**
   - Facts and data points
   - Decisions made and their rationale
   - Relationships between people, projects, and workstreams
   - Open questions and unresolved items
   - Action items and deadlines

7. **Update or create KB files**
   - Place files in the appropriate subdirectory:
     - `strategic-context/` for role, priorities, OKRs
     - `projects/{project-name}/` for project-specific information
     - `team/` for professional team models (INTERNAL ONLY)
     - `workstreams/` for workstream status and tracking
   - If updating existing files, preserve existing content and annotate what changed
   - If creating new files, follow the section README.md for structure

8. **Include YAML frontmatter on all KB files**
   ```yaml
   ---
   source: "Description of the source document"
   ingested: YYYY-MM-DD
   confidence: high|medium|low
   last_verified: YYYY-MM-DD
   tags: [relevant, tags]
   ---
   ```

9. **Update `knowledge-base/INDEX.md`**
   - Add new entries to the Quick Reference table
   - Update the By Section listing
   - Update the file count and last updated date

10. **Verify**
   - Run the compound deliverable verification (fidelity, coherence, privacy, professionalism)
   - Create a beads task if follow-up verification is needed: `bd create "Verify ingestion of {source}" -t task`

11. **Close and hand off**
    - If in autonomous mode, follow `protocols/autonomous-workflow.md` for commit, push, and PR creation
    - Record what was done: `bd comments add <id> "Ingested {source}. Files created/modified: {list}. Key decisions: {notes}. PR: {url or N/A}"`
    - Close the bead: `bd close <id> --reason "Ingested {source} into KB" --suggest-next`
    - Review `--suggest-next` output for newly unblocked work

## Confidence Levels
- **high**: Primary source document, official record, direct from stakeholder
- **medium**: Second-hand account, meeting notes from attendee, summary document
- **low**: Inference, hearsay, outdated document being ingested for reference
