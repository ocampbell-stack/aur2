---
name: aur2.process_visions
description: Process all visions from queue - text files and audio memos
disable-model-invocation: false
allowed-tools: Bash, Read, Write, Edit, Glob, Grep
---

# Process Visions

Process all visions in the queue sequentially.

## Directory Structure

Visions are stored in `.aur2/visions/` with the following structure:
- `queue/` - Ready for processing
  - `<title>.txt` - Text vision (plain text file)
  - `<title>/` - Audio vision directory (has audio.wav + transcript.txt)
- `processed/<title>_<timestamp>/` - Successfully processed
- `failed/<title>/` - Failed (may be missing transcript.txt)

## Steps

1. **List queue** - Find all vision items:
   ```bash
   ls -1 .aur2/visions/queue/
   ```

2. **For each item**, process sequentially:

   ### Text vision (`.txt` file)

   a. **Read text** - Use Read tool on `.aur2/visions/queue/<title>.txt`

   b. **Act on request** - Execute what the user asked for

   c. **On success** - Move to processed:
      ```bash
      mv ".aur2/visions/queue/<title>.txt" ".aur2/visions/processed/<title>_$(date +%Y%m%d_%H%M%S).txt"
      ```

   ### Audio vision (directory with audio.wav + transcript.txt)

   a. **Check for transcript** - If `transcript.txt` doesn't exist, transcribe first:
      ```bash
      python .aur2/scripts/transcribe.py ".aur2/visions/queue/<title>/audio.wav" > ".aur2/visions/queue/<title>/transcript.txt"
      ```

   b. **Read transcript** - Use Read tool on `.aur2/visions/queue/<title>/transcript.txt`

   c. **Act on request** - Execute what the user asked for in the memo

   d. **On success** - Move to processed with timestamp:
      ```bash
      mv ".aur2/visions/queue/<title>" ".aur2/visions/processed/<title>_$(date +%Y%m%d_%H%M%S)"
      ```

   e. **On failure** - Move to failed with timestamp:
      ```bash
      mv ".aur2/visions/queue/<title>" ".aur2/visions/failed/<title>_$(date +%Y%m%d_%H%M%S)"
      ```

3. **Continue** - Process next vision without user confirmation

## Acting on Request

- Read the content and determine what the user is asking for
- You can search and read any file in the project for context
- Determine the appropriate response based on project context:
  - **In a knowledge base** (hive-mind): Visions may require creating or updating KB entries, generating deliverables, updating INDEX.md, or creating beads for follow-up work. Modify project files as needed.
  - **In a codebase**: Prefer keeping research output (summaries, notes, analysis) in the vision's directory. Make code changes only if the vision explicitly requests them.
  - **For complex, multi-session work**: Escalate to `/aur2.scope` to decompose the vision into a phased plan, then `/aur2.execute` to implement it.
- Common requests: create a summary, research a topic, draft a plan, ingest documents, produce a deliverable

## Empty Queue

If `.aur2/visions/queue/` is empty or contains only `.gitkeep`, report:
"No visions in queue. Record a new memo with: python .aur2/scripts/record_memo.py"

## Error Handling

- If transcription fails, move memo to failed/
- If acting on request fails, move item to failed/
- Always continue to next vision after handling current one
