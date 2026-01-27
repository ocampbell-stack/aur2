---
name: aura.process_memo
description: Process all voice memos from queue - transcribe and act on requests
disable-model-invocation: true
allowed-tools: Bash(python *), Bash(mv *), Read, Write, Glob, Grep, Edit
---

# Process Voice Memos

Process all voice memos in the queue sequentially.

## Directory Structure

Memos are stored in `.aura/memo/` with the following structure:
- `queue/<title>/` - Ready for processing (has audio.wav + transcript.txt)
- `processed/<title>_<timestamp>/` - Successfully processed
- `failed/<title>/` - Failed (may be missing transcript.txt)

Each memo directory contains:
- `audio.wav` - Original recording
- `transcript.txt` - Whisper transcript (may be missing if transcription failed)

## Steps

1. **List queue** - Find all memo directories:
   ```bash
   ls -1 .aura/memo/queue/
   ```

2. **For each memo directory**, process sequentially:

   a. **Check for transcript** - If `transcript.txt` doesn't exist, transcribe first:
      ```bash
      python .aura/scripts/transcribe.py ".aura/memo/queue/<title>/audio.wav" > ".aura/memo/queue/<title>/transcript.txt"
      ```

   b. **Read transcript** - Use Read tool on `.aura/memo/queue/<title>/transcript.txt`

   c. **Act on request** - Execute what the user asked for in the memo

   d. **On success** - Move to processed with timestamp:
      ```bash
      mv ".aura/memo/queue/<title>" ".aura/memo/processed/<title>_$(date +%Y%m%d_%H%M%S)"
      ```

   e. **On failure** - Move to failed with timestamp:
      ```bash
      mv ".aura/memo/queue/<title>" ".aura/memo/failed/<title>_$(date +%Y%m%d_%H%M%S)"
      ```

3. **Continue** - Process next memo without user confirmation

## Recording New Memos

Use the record_memo.py script to record new voice memos:
```bash
python .aura/scripts/record_memo.py
```

This will:
1. Record audio via sox (press Ctrl+C to stop)
2. Transcribe via OpenAI Whisper
3. Generate a title from the transcript
4. Save to `.aura/memo/queue/<title>/`

If transcription fails, audio is preserved in `.aura/memo/failed/`.

## Retrying Failed Memos

To retry a failed memo:
1. Move it from `failed/` to `queue/`:
   ```bash
   mv ".aura/memo/failed/<title>" ".aura/memo/queue/<title>"
   ```
2. Run `/aura.process_memo` - it will attempt to re-transcribe if needed

## Empty Queue

If `.aura/memo/queue/` is empty or contains only `.gitkeep`, report:
"No memos in queue. Record a new memo with: python .aura/scripts/record_memo.py"

## Error Handling

- If transcription fails, move memo to failed/
- If acting on request fails, move memo to failed/
- Always continue to next memo after handling current one
