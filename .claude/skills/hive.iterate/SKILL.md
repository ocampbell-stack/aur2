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

3. **Identify the PR** — from input, or detect from branch:
   ```bash
   gh pr list --head $(git branch --show-current) --json number,url
   ```

4. **Ensure correct branch** — check out the feature branch if needed.

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
   CLAUDE_SESSION=$(/bin/ls -1t ~/.claude/projects/$(echo "$PWD" | tr '/' '-')/*.jsonl 2>/dev/null | head -1 | sed 's/.*\///' | sed 's/\.jsonl$//')
   gh pr comment <number> --body "Addressed feedback: <bullet list>

   ---
   Session: \`$CLAUDE_SESSION\` · Resume: \`claude --resume $CLAUDE_SESSION\`"
   ```

9. **Update beads**: `bd comments add <id> "Addressed PR #<number> feedback. Changes: <summary>"`

10. **Close or keep open**:
    - All feedback addressed → `bd close <id> --reason "PR feedback addressed" --suggest-next`
    - Some comments need clarification → keep bead open, note what's pending

11. **Report** — summarize changes made and any unresolved items.
