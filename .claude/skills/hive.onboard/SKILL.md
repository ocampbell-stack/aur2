---
name: hive.onboard
description: Build or update the user profile through structured conversation
disable-model-invocation: false
allowed-tools: Bash, Read, Write, Edit, Glob, Grep, WebFetch, WebSearch
---

# /hive.onboard - Build User Profile

Build or update the user's profile in the knowledge base. The user profile is foundational context that all other skills use to frame deliverables, recommendations, and ingestions from the user's perspective.

**Bead prefix**: `Onboard:`

Follow the skill lifecycle in `protocols/workflow.md` for setup (steps 1–4) and closeout (steps 7–9). Execute the skill-specific steps below during step 6.

## Alignment Focus

During preliminary alignment, determine:
- Does `knowledge-base/user/profile.md` already exist? (create vs. update flow)
- Did the user provide freeform input (notes about themselves, pasted context) or are they expecting a guided interview?
- If updating: what has changed since the last profile version?

## Core Work

### 1. Check for Existing Profile

Look for `knowledge-base/user/profile.md`:
- **If it exists**: This is an update flow. Read the current profile, present it to the user, and ask what has changed. Merge updates while preserving what hasn't changed.
- **If it doesn't exist**: This is initial setup. Proceed to step 2.

### 2. Gather Profile Information

**If the user provided freeform input** (skill argument, pasted text, notes, documents):
- Extract structured profile data from the input
- Identify gaps in the five profile sections (see step 3)
- Ask the user only about the gaps — don't re-ask for information already provided

**If no input was provided**, conduct a guided interview. Ask about each area:

1. **Identity**: What is your name and title? What organization or team are you part of?
2. **Expertise**: What are your primary technical or professional domains? What's your leadership scope? What are you strongest at?
3. **Goals**: What are your strategic goals? What are your immediate priorities?
4. **Working context**: How do you spend most of your time? Who are your key collaborators and stakeholders? What decisions are in your scope?
5. **Augmentation preferences**: How would the hive-mind be most useful to you? What types of deliverables do you need most often? What should agents proactively surface or help with?

Use `AskUserQuestion` for each area, or let the conversation flow naturally. Adapt based on what the user shares — if they give comprehensive answers, don't belabor the remaining questions.

### 3. Create or Update the Profile

Write `knowledge-base/user/profile.md` with this structure:

```yaml
---
source: "User-provided during onboarding"
ingested: YYYY-MM-DD
confidence: high
last_verified: YYYY-MM-DD
tags: [user-profile, identity]
---
```

**Sections**:

- **Identity** — Name, title/role, organization
- **Expertise** — Technical domains, leadership scope, strengths
- **Goals**
  - *Strategic Goals* — Long-term objectives
  - *Current Focus* — Active priorities, immediate objectives
- **Working Context** — How the user spends their time, key relationships, decision scope
- **Augmentation Preferences** — How the hive-mind should help: deliverable types, proactive support areas, communication style preferences

For any sections where information wasn't provided, include the section header with a note: `_To be enriched — run /hive.onboard to update._`

### 4. Create Supporting Files

If `knowledge-base/user/README.md` does not exist, create it:

```markdown
# User Profile

This section contains the user's identity, expertise, goals, and preferences for how the hive-mind should augment their work.

## Contents
- `profile.md` - Core user profile: identity, expertise, goals, working context, augmentation preferences

## Usage
Agents should consult the user profile when:
- Framing deliverables from the user's perspective
- Calibrating technical depth and communication style
- Grounding recommendations in the user's goals and role
- Understanding who the user works with and what they care about

## Getting Started
Run `/hive.onboard` to build your profile through a guided conversation, or `/hive.ingest` with notes about yourself to create it from existing context.
```

### 5. Update INDEX.md

Update `knowledge-base/INDEX.md`:
- Add `user/profile.md` to the Quick Reference table
- Add a `### user/` entry in the By Section listing
- Update the file count and last updated date
