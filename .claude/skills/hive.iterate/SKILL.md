---
name: hive.iterate
description: Address PR review feedback on an existing feature branch
argument-hint: <PR number or URL>
disable-model-invocation: false
allowed-tools: Bash, Read, Write, Edit, Glob, Grep, WebFetch, WebSearch
---

# /hive.iterate - Address PR Feedback

Iterate on an existing pull request based on review comments.

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

## Core Work

3. **Identify the PR** — from input (PR number or URL). If not provided, attempt detection from current branch:
   ```bash
   gh pr list --head $(git branch --show-current) --json number,url
   ```

4. **Check out the PR's branch**:
   ```bash
   PR_BRANCH=$(gh pr view <number> --json headRefName -q .headRefName)
   CURRENT=$(git branch --show-current)
   if [ "$CURRENT" != "$PR_BRANCH" ]; then
     git fetch origin
     git checkout "$PR_BRANCH"
   fi
   ```
   If checkout fails because the branch is checked out in another worktree, tell the user to run `./scripts/cleanup.sh {agent}` from the Command Post to free it.

5. **Read feedback**:
   ```bash
   gh pr view <number> --comments
   gh api repos/{owner}/{repo}/pulls/<number>/reviews
   ```

6. **Address each unresolved comment**:
   - Read the referenced file(s) and understand the requested change
   - Make the change
   - If the change affects KB content, update `knowledge-base/INDEX.md`

## Closeout

7. **Verify** — run quality checks per `protocols/quality.md` (light task weight is fine for iteration rounds).

8. **Commit, push, and notify**:
   ```bash
   git add -A
   git commit -m "address review: <summary>"
   git push
   # Session and context capture (see protocols/workflow.md Step 8.3)
   CLAUDE_SESSION=$(/bin/ls -1t ~/.claude/projects/$(echo "$PWD" | tr '/' '-')/*.jsonl 2>/dev/null | head -1 | sed 's/.*\///' | sed 's/\.jsonl$//')
   AGENT_NAME=$(basename "$PWD" | sed 's/^agent-//')
   gh pr comment <number> --body "Addressed feedback: <bullet list>

   ---
   Agent: \`$AGENT_NAME\` · Session: \`$CLAUDE_SESSION\` · Resume: \`cd $PWD && claude --resume $CLAUDE_SESSION\`"
   ```

9. **Update beads**: `bd comments add <id> "Addressed PR #<number> feedback. Changes: <summary>"`

10. **Close or keep open**:
    - All feedback addressed → `bd close <id> --reason "PR feedback addressed" --suggest-next`
    - Some comments need clarification → keep bead open, note what's pending

11. **Report** — summarize changes made and any unresolved items.
