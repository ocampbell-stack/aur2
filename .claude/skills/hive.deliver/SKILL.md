---
name: hive.deliver
description: Produce external deliverables grounded in hive-mind context
disable-model-invocation: false
allowed-tools: Bash, Read, Write, Edit, Glob, Grep, WebFetch, WebSearch
---

# /hive.deliver - Produce External Deliverables

Generate stakeholder-facing outputs grounded in KB context.

**Bead prefix**: `Deliver:`

Follow the skill lifecycle in `protocols/workflow.md` for setup (steps 1–4) and closeout (steps 7–9). Execute the skill-specific steps below during step 6.

## Alignment Focus

During preliminary alignment, pay attention to:
- Audience, format, and purpose of the deliverable
- Which KB sources will inform the output
- Tone and structural decisions
- Always pause when format or audience is unclear, or deliverable will be externally visible

## Core Work

1. **Read the deliverable request**
   - Understand audience, format, and purpose
   - Identify type: document, plan, analysis, email, presentation, etc.

2. **Load relevant context from KB**
   - Consult `knowledge-base/INDEX.md` to identify all relevant files
   - Read project files, strategic context, and workstream status as needed
   - Read team models ONLY for informing approach (never for content)

3. **Draft the deliverable**
   - Match the requested format and tone
   - Ground all claims in KB content
   - Maintain appropriate detail level for the audience

4. **Update KB with learnings**
   - If the deliverable process revealed new information, ingest it
   - If existing KB content was found stale or wrong, flag for grooming
