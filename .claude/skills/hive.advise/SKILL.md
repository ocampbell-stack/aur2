---
name: hive.advise
description: Analyze communications and recommend engagement actions
disable-model-invocation: false
allowed-tools: Bash, Read, Write, Edit, Glob, Grep
---

# /hive.advise - Recommend Engagement

Analyze communications and recommend actions based on KB context.

## Instructions

0. **Determine operating mode**
   - Read `protocols/autonomous-workflow.md` for mode detection and git workflow
   - If in autonomous mode, follow the full lifecycle (sync, branch, work, commit, PR)

1. **Beads setup**
   - If triggered by an existing bead: `bd update <id> --claim` (or `--status in_progress` if already yours)
   - If triggered by user request with no bead: `bd create "Advise: <brief description>" -t task`
   - Read bead context: `bd show <id>` to check description and comments from prior agents

2. **Complexity check**
   - If the request involves analyzing multiple communications or producing advice across several topics, use `/aur2.scope` to decompose, then `/aur2.execute`
   - For a single communication or focused advisory, proceed directly

3. **Read the provided communication**
   - Accept: meeting notes, chat threads, emails, Slack messages, etc.
   - Identify: participants, topics discussed, decisions made, action items, tone

4. **Load relevant KB context**
   - Consult `knowledge-base/INDEX.md` for:
     - Team member models (if applicable, for tailoring recommendations)
     - Project state and priorities
     - Strategic context and objectives
     - Related workstream status

5. **Produce recommendations**
   Structure your output as:

   ### Action Items
   - Specific things the user should do, with rationale grounded in KB context
   - Prioritized by urgency and strategic alignment

   ### Suggested Responses / Talking Points
   - Draft responses or key points for follow-up communications
   - Tailored to the audience (informed by team models, not exposing them)

   ### Risks & Sensitivities
   - Political or interpersonal dynamics to be aware of
   - Strategic risks identified from the communication
   - Topics that need careful handling

   ### New Information Detected
   - Facts, decisions, or context from the communication that should be ingested into KB

6. **Privacy gate**
   - Ensure recommendations don't expose internal team models
   - Frame advice in terms of "what to do" not "why based on person X's model"
   - If the user asks for an external-facing response, run the full privacy check

7. **Update KB**
   - Ingest new information gleaned from the communication
   - Update relevant project, workstream, or team files
   - Update INDEX.md

8. **Create follow-up beads** for action items that need tracking:
   - `bd create "Follow up: {action item description}" -t task`

9. **Close and hand off**
   - Record what was done: `bd comments add <id> "Analyzed {communication type}. Key findings: {summary}. Created {N} follow-up beads. KB files updated: {list or none}"`
   - Close the bead: `bd close <id> --reason "Advisory complete for {brief description}" --suggest-next`
   - If in autonomous mode, follow `protocols/autonomous-workflow.md` for commit, push, PR
   - Review `--suggest-next` output for newly unblocked work
