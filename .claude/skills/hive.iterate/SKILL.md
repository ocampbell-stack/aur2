---
name: hive.iterate
description: Iterate on prior work — address PR feedback or follow up on closed/merged PRs
argument-hint: <PR number or URL> [follow-up instructions]
disable-model-invocation: false
allowed-tools: Bash, Read, Write, Edit, Glob, Grep, WebFetch, WebSearch
---

# /hive.iterate - Iterate on Prior Work

Iterate on an existing pull request — either address review comments on an open PR, or follow up on a closed/merged PR with new direction provided in the user's prompt.

This skill has a lighter lifecycle than other hive.* skills — it skips the complexity check and uses an abbreviated alignment step since the PR context is already established.

## Setup

1. **Determine operating mode** — read `protocols/workflow.md` for mode detection.

2. **Beads setup**
   - Find the associated bead:
     ```bash
     bd search "PR:"
     bd list --status in_progress --assignee $(basename $(pwd) | sed 's/agent-//')
     ```
   - If found: `bd update <id> --status in_progress`
   - If none: `bd create "Iterate: PR #<number> feedback" -t task`

3. **Identify the PR** — from input (PR number or URL). If not provided, attempt detection from current branch:
   ```bash
   gh pr list --head $(git branch --show-current) --json number,url
   ```

4. **Check PR state**:
   ```bash
   PR_STATE=$(gh pr view <number> --json state -q .state)
   ```
   - If `OPEN` → follow **Open PR Flow** below
   - If `CLOSED` or `MERGED` → follow **Closed/Merged PR Flow** below

---

## Open PR Flow

Address review comments on the existing branch and push updates to the open PR.

1. **Check out the PR's branch**:
   ```bash
   PR_BRANCH=$(gh pr view <number> --json headRefName -q .headRefName)
   CURRENT=$(git branch --show-current)
   if [ "$CURRENT" != "$PR_BRANCH" ]; then
     git fetch origin
     git checkout "$PR_BRANCH"
   fi
   ```
   If checkout fails because the branch is checked out in another worktree, tell the user to run `./scripts/cleanup.sh {agent}` from the Command Post to free it.

2. **Read feedback**:
   ```bash
   gh pr view <number> --comments
   gh api repos/{owner}/{repo}/pulls/<number>/reviews
   ```

3. **Address each unresolved comment**:
   - Read the referenced file(s) and understand the requested change
   - Make the change
   - If the change affects KB content, update `knowledge-base/INDEX.md`

4. **Verify** — run quality checks per `protocols/quality.md` (light task weight).

5. **Commit, push, and notify**:
   ```bash
   git add -A
   git commit -m "address review: <summary>"
   git push
   # Session and context capture (see protocols/workflow.md Step 8.3)
   CLAUDE_SESSION=$(/bin/ls -1t ~/.claude/projects/$(echo "$PWD" | tr '/' '-')/*.jsonl 2>/dev/null | head -1 | sed 's/.*\///' | sed 's/\.jsonl$//')
   AGENT_NAME=$(basename "$PWD" | sed 's/^agent-//')
   CURRENT_BRANCH=$(git branch --show-current)
   gh pr comment <number> --body "Addressed feedback: <bullet list>

   ---
   - Agent: \`$AGENT_NAME\`
   - Branch: \`$CURRENT_BRANCH\`
   - Hash: \`$CLAUDE_SESSION\`
   - Resume: \`cd $PWD && claude --resume $CLAUDE_SESSION\`"
   ```

6. **Update beads**: `bd comments add <id> "Addressed PR #<number> feedback. Changes: <summary>"`

7. **Close or keep open**:
   - All feedback addressed → `bd close <id> --reason "PR feedback addressed" --suggest-next`
   - Some comments need clarification → keep bead open, note what's pending

8. **Report** — summarize changes made and any unresolved items.

---

## Closed/Merged PR Flow

The PR is no longer open. The user's prompt accompanying this skill invocation is the new feedback or direction. Treat this as a follow-up to the original task.

1. **Gather original context**:
   ```bash
   gh pr view <number>
   gh pr view <number> --comments
   gh pr diff <number>
   ```
   Understand the original PR's purpose, what was changed, and any review discussion.

2. **Interpret user feedback** — the text accompanying the `/hive.iterate` invocation IS the new direction. Parse it as requirements for this iteration.

3. **Load KB context**:
   - Read `knowledge-base/INDEX.md` and relevant KB files referenced by or affected by the original PR
   - Read `knowledge-base/user/profile.md` if it exists
   - Understand the current state of the content that was modified in the original PR

4. **Alignment** — follow `protocols/alignment.md`:
   - Assess what needs to change given the new feedback
   - Identify any overlap or contradiction with content that landed from the original PR (or elsewhere since)
   - Confirm approach with the user per the standard confidence thresholds

5. **Sync and branch** (autonomous only):
   ```bash
   git fetch origin
   git rebase origin/main
   git checkout -b feat/{agent-name}/{description}
   ```

6. **Make changes** — implement the requested modifications. If changes affect KB content, update `knowledge-base/INDEX.md`.

7. **Verify** — run quality checks per `protocols/quality.md` (task weight based on scope of changes).

8. **Commit, push, and create PR** — follow `protocols/workflow.md` steps 8.1–8.4 for the full commit/push/PR flow. Reference the original PR:
   - Title: concise description of the follow-up work
   - Body: include `Follow-up to #<original-PR-number>` at the top of the Summary section, then the standard PR format

9. **Update beads**: `bd comments add <id> "Follow-up to PR #<original>. New PR: <url>. Changes: <summary>"`

10. **Close bead**: `bd close <id> --reason "Follow-up PR submitted" --suggest-next`

11. **Report** — output the new PR URL, summarize what changed from the original, and note the relationship to the prior PR.
