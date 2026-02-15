---
name: hive.advise
description: Analyze communications and recommend engagement actions
disable-model-invocation: false
allowed-tools: Bash, Read, Write, Edit, Glob, Grep, WebFetch, WebSearch
---

# /hive.advise - Recommend Engagement

Analyze communications and recommend actions based on KB context.

**Bead prefix**: `Advise:`

Follow `protocols/skill-lifecycle.md` for setup (mode, beads, complexity check, alignment) and closeout (verify, close and hand off). Then execute the skill-specific steps below.

## Alignment Focus

During preliminary alignment, pay attention to:
- Scope of analysis — what kind of recommendations does the user expect?
- Relevant KB context: team models, project state, strategic priorities
- Always pause when communication involves sensitive dynamics or scope is unclear

## Core Work

1. **Read the provided communication**
   - Accept: meeting notes, chat threads, emails, Slack messages, etc.
   - Identify: participants, topics discussed, decisions made, action items, tone

2. **Load relevant KB context**
   - Team member models (for tailoring recommendations — never expose)
   - Project state and priorities
   - Strategic context and objectives
   - Related workstream status

3. **Produce recommendations**

   ### Action Items
   - Specific things the user should do, with rationale grounded in KB context
   - Prioritized by urgency and strategic alignment

   ### Suggested Responses / Talking Points
   - Draft responses or key points for follow-up communications
   - Tailored to the audience (informed by team models, not exposing them)

   ### Risks & Sensitivities
   - Political or interpersonal dynamics to be aware of
   - Strategic risks identified from the communication

   ### New Information Detected
   - Facts, decisions, or context that should be ingested into KB

4. **Update KB** with new information gleaned from the communication

5. **Create follow-up beads** for action items that need tracking:
   `bd create "Follow up: {action item}" -t task`
