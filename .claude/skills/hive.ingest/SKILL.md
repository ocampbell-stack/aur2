---
name: hive.ingest
description: Ingest documents or notes into the hive-mind knowledge base
disable-model-invocation: false
allowed-tools: Bash, Read, Write, Edit, Glob, Grep, WebFetch, WebSearch
---

# /hive.ingest - Update Mental Model

Ingest new documents, notes, or external context into the knowledge base.

**Bead prefix**: `Ingest:`

Follow `protocols/skill-lifecycle.md` for setup (mode, beads, complexity check, alignment) and closeout (verify, close and hand off). Then execute the skill-specific steps below.

## Alignment Focus

During preliminary alignment, pay attention to:
- Which KB section the source material belongs in
- Whether this creates new files or updates existing ones
- Overlap with or contradictions to current entries
- Structural decisions: which directory, file naming

## Core Work

1. **Read the provided document(s) or notes**
   - Accept input as: pasted text, file paths, URLs, or conversation context
   - Identify document type: meeting notes, strategic doc, project charter, status update, etc.

2. **Extract key information**
   - Facts and data points
   - Decisions made and their rationale
   - Relationships between people, projects, and workstreams
   - Open questions and unresolved items
   - Action items and deadlines

3. **Update or create KB files**
   - Place files in the appropriate subdirectory:
     - `strategic-context/` for role, priorities, OKRs
     - `projects/{project-name}/` for project-specific information
     - `team/` for professional team models (INTERNAL ONLY)
     - `workstreams/` for workstream status and tracking
   - If updating existing files, preserve existing content and annotate what changed
   - If creating new files, follow the section README.md for structure
   - Include YAML frontmatter per `protocols/quality.md`

4. **Update `knowledge-base/INDEX.md`**
   - Add new entries to the Quick Reference table
   - Update the By Section listing
   - Update the file count and last updated date

5. **Create follow-up beads** if verification is needed:
   `bd create "Verify ingestion of {source}" -t task`
