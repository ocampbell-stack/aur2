---
name: hive.deliver
description: Produce external deliverables grounded in hive-mind context
disable-model-invocation: false
allowed-tools: Bash, Read, Write, Edit, Glob, Grep, WebFetch, WebSearch
---

# /hive.deliver - Produce External Deliverables

Generate stakeholder-facing outputs grounded in KB context.

## Instructions

0. **Determine operating mode**
   - Read `protocols/autonomous-workflow.md` for mode detection and git workflow
   - If in autonomous mode, follow the full lifecycle (sync, branch, work, commit, PR)

1. **Beads setup**
   - If triggered by an existing bead: `bd update <id> --claim` (or `--status in_progress` if already yours)
   - If triggered by user request with no bead: `bd create "Deliver: <brief description>" -t task`
   - Read bead context: `bd show <id>` to check description and comments from prior agents

2. **Complexity check**
   - If the request involves multiple deliverables or a large multi-section document, escalate to `/aur2.scope` to produce a scope PR for user review. Close this bead with a note pointing to the scope. Execution via `/aur2.execute` happens separately after the user approves the scope.
   - For a single focused deliverable, proceed directly

3. **Preliminary alignment**
   - Read `knowledge-base/INDEX.md` and identify KB sections relevant to the deliverable topic
   - Read those sections to understand what context is available
   - Assess: What is the audience, format, and purpose? Which KB sources will inform the deliverable? What structural or tone decisions need to be made?
   - Present to user: context found, proposed deliverable structure, KB sources to draw from, any questions about audience/format/scope
   - **Always pause** (use `AskUserQuestion`) when: the format or audience is unclear, multiple approaches are possible, or the deliverable will be externally visible
   - **State plan and proceed** when: the request specifies format, audience, and scope explicitly
   - When in doubt, pause — the cost of asking is always lower than the cost of rework

4. **Read the deliverable request**
   - Understand the audience, format, and purpose
   - Identify the type: document, code, plan, presentation, analysis, email, etc.

5. **Load relevant context from KB**
   - Consult `knowledge-base/INDEX.md` to identify all relevant files
   - Read project files, strategic context, and workstream status as needed
   - Read team models ONLY for informing approach (never for content)

6. **Draft the deliverable**
   - Match the requested format and tone
   - Ground all claims in KB content (cite internally which KB files informed each section)
   - Maintain appropriate level of detail for the audience

7. **Run compound deliverable verification**

   a. **Fidelity**: Does it match the assignment instructions?
      - Re-read the original request
      - Check every requirement is addressed
      - Verify scope is correct

   b. **Coherence**: Is it consistent with the KB?
      - Cross-reference facts, dates, and claims against KB files
      - Flag any information that couldn't be verified in KB

   c. **Privacy**: Does it contain NO internal team models or unnecessary personal info?
      - Search for team member names and verify no model content leaked
      - Check for internal-only assessments
      - Apply the leak test from privacy-standards.md

   d. **Professionalism**: Would this be appropriate if leaked?
      - Check tone and language
      - Verify formatting meets stakeholder expectations

8. **Update KB with learnings**
   - If the deliverable process revealed new information, ingest it
   - If existing KB content was found to be stale or wrong, flag for grooming

9. **Close and hand off**
   - If in autonomous mode, follow `protocols/autonomous-workflow.md` for commit, push, and PR creation
   - If in manual mode, follow the user's lead on committing and submission
   - Record what was done: `bd comments add <id> "Produced {deliverable type}. KB sources used: {list}. KB updates: {list or none}. PR: {url or N/A}"`
   - Close the bead: `bd close <id> --reason "Delivered {brief description}" --suggest-next`
   - Review `--suggest-next` output for newly unblocked work
