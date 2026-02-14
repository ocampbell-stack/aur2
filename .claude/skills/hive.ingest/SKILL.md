---
description: "Ingest documents or notes into the hive-mind knowledge base"
disable-model-invocation: false
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
   - If the request involves multiple documents or will require more than one session, use `/aur2.scope` to decompose into a phased plan, then `/aur2.execute` to implement
   - For a single document or focused ingestion, proceed directly

3. **Read the provided document(s) or notes**
   - Accept input as: pasted text, file paths, URLs, or conversation context
   - Identify the document type: meeting notes, strategic doc, project charter, status update, etc.

4. **Consult `knowledge-base/INDEX.md`**
   - Find relevant existing KB sections
   - Determine if this is a new topic or an update to existing content

5. **Extract key information**
   - Facts and data points
   - Decisions made and their rationale
   - Relationships between people, projects, and workstreams
   - Open questions and unresolved items
   - Action items and deadlines

6. **Update or create KB files**
   - Place files in the appropriate subdirectory:
     - `strategic-context/` for role, priorities, OKRs
     - `projects/{project-name}/` for project-specific information
     - `team/` for professional team models (INTERNAL ONLY)
     - `workstreams/` for workstream status and tracking
   - If updating existing files, preserve existing content and annotate what changed
   - If creating new files, follow the section README.md for structure

7. **Include YAML frontmatter on all KB files**
   ```yaml
   ---
   source: "Description of the source document"
   ingested: YYYY-MM-DD
   confidence: high|medium|low
   last_verified: YYYY-MM-DD
   tags: [relevant, tags]
   ---
   ```

8. **Update `knowledge-base/INDEX.md`**
   - Add new entries to the Quick Reference table
   - Update the By Section listing
   - Update the file count and last updated date

9. **Verify**
   - Run the compound deliverable verification (fidelity, coherence, privacy, professionalism)
   - Create a beads task if follow-up verification is needed: `bd create "Verify ingestion of {source}" -t task`

10. **Close and hand off**
    - Record what was done: `bd comments add <id> "Ingested {source}. Files created/modified: {list}. Key decisions: {notes}"`
    - Close the bead: `bd close <id> --reason "Ingested {source} into KB" --suggest-next`
    - If in autonomous mode, follow `protocols/autonomous-workflow.md` for commit, push, PR
    - Review `--suggest-next` output for newly unblocked work

## Confidence Levels
- **high**: Primary source document, official record, direct from stakeholder
- **medium**: Second-hand account, meeting notes from attendee, summary document
- **low**: Inference, hearsay, outdated document being ingested for reference
