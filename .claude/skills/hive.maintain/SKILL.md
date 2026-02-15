---
name: hive.maintain
description: Plan and execute maintenance or improvements to the hive-mind system
disable-model-invocation: false
allowed-tools: Bash, Read, Write, Edit, Glob, Grep, WebFetch, WebSearch
---

# /hive.maintain - Maintain the Fleet

Improve tooling, scripts, and infrastructure for the hive-mind system.

## Instructions

0. **Determine operating mode**
   - Read `protocols/autonomous-workflow.md` for mode detection and git workflow
   - If in autonomous mode, follow the full lifecycle (sync, branch, work, commit, PR)

1. **Beads setup**
   - If triggered by an existing bead: `bd update <id> --claim` (or `--status in_progress` if already yours)
   - If triggered by user request with no bead: `bd create "Maintain: <brief description>" -t task`
   - Read bead context: `bd show <id>` to check description and comments from prior agents

2. **Read the maintenance request** or identify improvement opportunity
   - Types: bug fix, script improvement, new automation, protocol update, skill refinement

3. **Consult existing infrastructure**
   - Review relevant scripts in `scripts/`
   - Review CLAUDE.md and `protocols/` for agent behavior docs
   - Review skill definitions in `.claude/skills/`
   - Check `.claude/settings.json` for hook configuration

4. **Scope the change**
   - If the change is complex, use `/aur2.scope` for task decomposition, then `/aur2.execute`
   - If simple, proceed directly

5. **Implement**
   - Make changes
   - Test changes:
     - Verify hooks fire correctly (check `.claude/settings.json`)
     - Verify skills load (check SKILL.md frontmatter)
     - Verify beads commands work (`bd ready`, `bd list`)
     - Verify scripts execute without errors

6. **Update documentation**
   - Update CLAUDE.md if agent behavior should change
   - Update protocols if verification or process standards change
   - **Skills note**: Skills (`.claude/skills/`) are gitignored in hive-mind and deployed from [aur2](https://github.com/ocampbell-stack/aur2). Do NOT edit skills in this repo — changes are lost on the next `aur2 init --force`. If skill changes are needed, create a follow-up bead: `bd create "Aur2: update {skill} - {what needs changing}" -t task`

7. **Update KB**
   - Document the change in appropriate KB section
   - Update INDEX.md

8. **Close and hand off**
   - Record what was done: `bd comments add <id> "Maintained {component}. Changes: {summary}. Test results: {pass/fail details}"`
   - Close the bead: `bd close <id> --reason "Maintenance complete: {brief summary}" --suggest-next`
   - If in autonomous mode, follow `protocols/autonomous-workflow.md` for commit, push, PR
   - Review `--suggest-next` output for newly unblocked work

## Common Maintenance Tasks
- Update SessionStart hook for new context sources
- Refine skill instructions based on usage patterns
- Add new fleet scripts for common operations
- Update protocols based on lessons learned
- Fix issues with worktree or beads configuration
