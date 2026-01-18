---
allowed-tools: Bash(sox:*), Bash(rec:*), Bash(ls:*), Bash(mkdir:*), Bash(date:*), Glob
description: Record voice memo to queue
argument-hint: [duration_in_seconds]
---

# Record Voice Memo

Record audio from your microphone and save to `.aura/queue/` for transcription.

## Prerequisites

- `sox` must be installed
  - macOS: `brew install sox`
  - Ubuntu: `sudo apt-get install sox libsox-fmt-all`

## Instructions

1. Create the queue directory if it doesn't exist:
   ```bash
   mkdir -p .aura/queue
   ```

2. Generate filename with timestamp:
   ```bash
   FILENAME=".aura/queue/memo_$(date +%Y%m%d_%H%M%S).wav"
   ```

3. Start recording:
   ```bash
   # Default: record until Ctrl+C
   rec "$FILENAME"

   # Or with duration limit (if $ARGUMENTS provided):
   rec "$FILENAME" trim 0 $ARGUMENTS
   ```

4. After recording completes, show the user:
   - File location and size: `ls -lh "$FILENAME"`
   - Next steps: `/aura.transcribe` or `/aura.act`

## Tips

- **Stop early**: Press Ctrl+C to stop before max duration
- **Custom duration**: `/aura.record 60` for 60-second max
- **Batch process**: Record multiple memos, then process with `/aura.act`

## Error Handling

If sox is not installed:
```
sox/rec command not found.
Install with:
  macOS: brew install sox
  Ubuntu: sudo apt-get install sox libsox-fmt-all
```

If recording fails, check:
- Microphone permissions (macOS: System Settings > Privacy & Security > Microphone)
- Audio device availability: `sox --help-device`
