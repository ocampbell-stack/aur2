---
name: hive.iterate
description: Address PR review feedback on an existing feature branch
argument-hint: <PR number or URL>
disable-model-invocation: false
---

# /hive.iterate - Address PR Feedback

Iterate on an existing pull request based on review comments.

## Instructions

1. **Determine operating mode**
   - Read `protocols/autonomous-workflow.md` for mode detection
   - This skill is most commonly used in autonomous mode (agent worktrees)

2. **Identify the PR**
   - If a PR number or URL was provided as input, use it directly
   - If no input, detect from current branch:
     ```bash
     gh pr list --head $(git branch --show-current) --json number,url
     ```
   - If no PR found, ask the user which PR to iterate on

3. **Ensure correct branch**
   - Verify you are on the feature branch associated with the PR
   - If not, check it out:
     ```bash
     git checkout <branch-name>
     ```

4. **Read review feedback**
   - Read `protocols/pr-feedback.md` for the full feedback protocol
   - Fetch PR details and comments:
     ```bash
     gh pr view <number> --comments
     gh api repos/{owner}/{repo}/pulls/<number>/reviews
     ```
   - Identify unresolved comments and requested changes

5. **Address each comment**
   - For each unresolved review comment:
     - Read the referenced file(s) and understand the requested change
     - Make the change
     - If the change affects KB content, update `knowledge-base/INDEX.md`

6. **Verify**
   - Re-run compound deliverable verification (fidelity, coherence, privacy, professionalism)
   - Ensure changes don't introduce new issues

7. **Commit, push, and notify**
   ```bash
   git add -A
   git commit -m "address review: <summary of changes>"
   git push
   gh pr comment <number> --body "Addressed feedback: <bullet list of changes>"
   ```

8. **Update beads**
   - Find the associated bead (search for one with the PR URL in comments)
   - Add a note: `bd comments add <id> "Review feedback addressed"`

9. **Report to user**
   - Summarize what changes were made
   - Note any comments that could not be addressed (need clarification, out of scope, etc.)
