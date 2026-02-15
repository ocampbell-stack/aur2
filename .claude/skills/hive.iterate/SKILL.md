---
name: hive.iterate
description: Address PR review feedback on an existing feature branch
argument-hint: <PR number or URL>
disable-model-invocation: false
allowed-tools: Bash, Read, Write, Edit, Glob, Grep, WebFetch, WebSearch
---

# /hive.iterate - Address PR Feedback

Iterate on an existing pull request based on review comments.

## Instructions

1. **Determine operating mode**
   - Read `protocols/autonomous-workflow.md` for mode detection
   - This skill is most commonly used in autonomous mode (agent worktrees)

2. **Beads setup**
   - Find the associated bead for this PR:
     ```bash
     bd search "PR:" | head -5
     bd list --status in_progress --assignee $(basename $(pwd) | sed 's/agent-//')
     ```
   - If found: `bd update <id> --status in_progress` (if not already)
   - If no bead exists: `bd create "Iterate: PR #<number> feedback" -t task`
   - Read bead context: `bd show <id>` to check description and comments

3. **Identify the PR**
   - If a PR number or URL was provided as input, use it directly
   - If no input, detect from current branch:
     ```bash
     gh pr list --head $(git branch --show-current) --json number,url
     ```
   - If no PR found, ask the user which PR to iterate on

4. **Ensure correct branch**
   - Verify you are on the feature branch associated with the PR
   - If not, check it out:
     ```bash
     git checkout <branch-name>
     ```

5. **Read review feedback**
   - Read `protocols/pr-feedback.md` for the full feedback protocol
   - Fetch PR details and comments:
     ```bash
     gh pr view <number> --comments
     gh api repos/{owner}/{repo}/pulls/<number>/reviews
     ```
   - Identify unresolved comments and requested changes

6. **Address each comment**
   - For each unresolved review comment:
     - Read the referenced file(s) and understand the requested change
     - Make the change
     - If the change affects KB content, update `knowledge-base/INDEX.md`

7. **Verify**
   - Re-run compound deliverable verification (fidelity, coherence, privacy, professionalism)
   - Ensure changes don't introduce new issues

8. **Commit, push, and notify**
   ```bash
   git add -A
   git commit -m "address review: <summary of changes>"
   git push
   gh pr comment <number> --body "Addressed feedback: <bullet list of changes>"
   ```

9. **Close and hand off**
   - Record what was done: `bd comments add <id> "Addressed PR #<number> feedback. Changes: <summary>. Unresolved: <any items needing clarification>"`
   - If all feedback is addressed and PR is ready for re-review: `bd close <id> --reason "PR feedback addressed" --suggest-next`
   - If some comments need user clarification, keep the bead open and note what's pending
   - Review `--suggest-next` output for newly unblocked work

10. **Report to user**
    - Summarize what changes were made
    - Note any comments that could not be addressed (need clarification, out of scope, etc.)
