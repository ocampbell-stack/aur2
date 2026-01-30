# Epic: Scope and Execute Skills

## Overview

Create two new skills (`aura.scope` and `aura.execute`) and a feature template in `.aura/templates/`.

### Why

Today the workflow for going from idea to code is three manual steps: `/aura.epic` → `/aura.create_beads` → `/aura.implement`. The user has to review and invoke each one. The epic skill produces multi-phase plans even for single features, which is overkill for most work. We want to collapse this to two steps: `/aura.scope` (plan, user reviews) → `/aura.execute` (autonomous). Templates make scope output predictable and consistent — a "feature" always produces scope/plan/implement/test stages without the agent reinventing structure each time.

### What stays

Existing `aura.epic`, `aura.create_beads`, and `aura.implement` skills are untouched. The new skills sit alongside them.

### Target folder structure

```
.aura/
├── templates/
│   └── feature.md                    # Feature work template (scope/plan/implement/test)
└── epics/
    └── <kebab-name>/
        └── scope.md                  # Output of /aura.scope (same format as epic.md)

.claude/skills/
├── aura.scope/
│   └── SKILL.md                      # Template-driven scoping skill
├── aura.execute/
│   ├── SKILL.md                      # Orchestrator: create graph then implement graph
│   ├── create-graph.md               # Reference: how to create beads from a scope file
│   └── implement-graph.md            # Reference: how to work beads in dependency order
├── aura.epic/                        # Unchanged
├── aura.create_beads/                # Unchanged
└── aura.implement/                   # Unchanged
```

### How implementation should work

**`.aura/templates/feature.md`** — A markdown file defining four stages (scope, plan, implement, test). Each stage has a title pattern (`"Scope: {{title}}"`), a description of what work that stage involves, and which prior stage it depends on. This is plain markdown the agent reads and follows, not a programmatic template engine.

**`aura.scope/SKILL.md`** — Uses `!`command`` to inject available template names from `.aura/templates/` at invocation time. Reads the feature template, takes the user's vision, and writes a scope file to `.aura/epics/<name>/scope.md`. The scope file uses the exact same task format as existing epics (`N. [ ] <Title> (depends on X) - <Description>`) so it's compatible with `create_beads` parsing.

**`aura.execute/SKILL.md`** — Takes a scope/epic path. Instructs the agent to do two things in sequence: first read `create-graph.md` and follow its instructions to create beads, then read `implement-graph.md` and follow its instructions to work the beads. These supporting files are copies of the `create_beads` and `implement` skill content (without frontmatter) so the execute skill is self-contained.

**`create-graph.md`** — Body content from `aura.create_beads/SKILL.md`. Describes how to parse task lines, create beads with `bd create`, and wire dependencies with `bd dep add`.

**`implement-graph.md`** — Body content from `aura.implement/SKILL.md`. Describes how to find ready beads with `bd ready`, implement each one, close with `bd close`, and repeat until done.

## Tasks

### Phase 1: Foundation

1. [ ] Create `.aura/templates/` directory and `feature.md` template - Define the feature template with four stages (scope, plan, implement, test), each with a title pattern, description of work, and dependency on the prior stage
2. [ ] Create `aura.scope` skill - New skill at `.claude/skills/aura.scope/SKILL.md` that uses `!`command`` to discover templates from `.aura/templates/`, reads the selected template, applies it to the user's vision, and writes a scope file to `.aura/epics/<name>/scope.md` in the existing epic task format

### Phase 2: Execute Skill

3. [ ] Create `create-graph.md` supporting file for execute skill (depends on 1) - Copy of `aura.create_beads/SKILL.md` content (without frontmatter) into `.claude/skills/aura.execute/create-graph.md` as a reference doc the execute skill points to
4. [ ] Create `implement-graph.md` supporting file for execute skill - Copy of `aura.implement/SKILL.md` content (without frontmatter) into `.claude/skills/aura.execute/implement-graph.md` as a reference doc the execute skill points to
5. [ ] Create `aura.execute` skill (depends on 3, 4) - New skill at `.claude/skills/aura.execute/SKILL.md` that takes a scope/epic path, instructs the agent to first follow `create-graph.md` to create beads, then follow `implement-graph.md` to implement them

### Phase 3: Verify

6. [ ] Test scope skill with a sample vision (depends on 2) - Run `/aura.scope` with a test vision, verify it reads the feature template, produces a correctly formatted scope file in `.aura/epics/`, and tasks match the template stages
7. [ ] Test execute skill end-to-end (depends on 5, 6) - Run `/aura.execute` against the test scope file, verify it creates beads with correct dependencies and then works through them in order

## Dependencies

- Task 3 blocked by: 1
- Task 5 blocked by: 3, 4
- Task 6 blocked by: 2
- Task 7 blocked by: 5, 6

## Success Criteria

- [ ] `.aura/templates/feature.md` exists with four stages
- [ ] `/aura.scope <vision>` produces a scope file using the feature template
- [ ] `/aura.execute <path>` creates beads then implements them in one invocation
- [ ] Existing `epic`, `create_beads`, and `implement` skills are unchanged
- [ ] Scope file format is compatible with existing `create_beads` parsing rules
