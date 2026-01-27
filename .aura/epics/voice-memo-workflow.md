# Epic: Voice Memo Workflow

## Overview

Create a unified voice memo recording workflow with a single script that chains recording, transcription, and title generation. Handle failures gracefully by maintaining consistent directory structure across queue/, processed/, and failed/. The goal is a frictionless "record and forget" experience where the user runs one command and gets a properly organized, titled memo.

## Current State

- `transcribe.py` - Transcribes audio via OpenAI Whisper
- `generate_title.py` - Generates kebab-case title from transcript
- No recording script (was removed in redesign)
- `aura.process_memo` skill expects memos in queue with transcript.txt

## Target State

- `record_memo.py` - Single script that records → transcribes → titles → organizes
- Consistent directory structure: `<title>/audio.wav` + `<title>/transcript.txt`
- Graceful failure handling: audio preserved even if transcription fails
- Updated skill and documentation

## Tasks

### Phase 1: Script Foundation

1. [ ] Create record_memo.py with sox recording - Record audio via sox, save to temp location, handle Ctrl+C gracefully

2. [ ] Add transcription integration to record_memo.py - After recording, call transcription logic, handle API errors

3. [ ] Add title generation to record_memo.py - Generate title from transcript, create final directory structure

4. [ ] Add failure handling to record_memo.py (depends on 1, 2, 3) - If transcription fails, save to failed/ with timestamp-based name, preserve audio

### Phase 2: Directory Structure

5. [ ] Define consistent directory structure (depends on 4) - Document and implement: `<location>/<title>/audio.wav` + `transcript.txt` across queue/, processed/, failed/

6. [ ] Update aura.process_memo skill (depends on 5) - Adjust to work with new structure, handle memos without transcript (re-transcribe)

### Phase 3: Documentation

7. [ ] Update README.md (depends on 6) - Document new recording workflow and script usage

8. [ ] Update CLAUDE.md (depends on 6) - Update developer documentation for new structure

9. [ ] Update .aura/aura.md (depends on 6) - Update context file with new workflow

## Dependencies

- Task 4 blocked by: 1, 2, 3
- Task 5 blocked by: 4
- Task 6 blocked by: 5
- Task 7 blocked by: 6
- Task 8 blocked by: 6
- Task 9 blocked by: 6

## Directory Structure Spec

```
.aura/memo/
├── queue/                    # Ready for processing
│   └── <title>/
│       ├── audio.wav         # Original recording
│       └── transcript.txt    # Whisper transcript
├── processed/                # Successfully processed by aura.process_memo
│   └── <title>_<timestamp>/
│       ├── audio.wav
│       └── transcript.txt
└── failed/                   # Recording succeeded, transcription failed
    └── <title-or-timestamp>/
        ├── audio.wav         # Always preserved
        └── transcript.txt    # May be missing if transcription failed
```

## Script Behavior Spec

### record_memo.py

```
Usage: python .aura/scripts/record_memo.py [--max-duration SECONDS]

1. Check sox is available
2. Start recording (sox rec)
3. User presses Ctrl+C to stop
4. Transcribe audio (OpenAI Whisper)
5. Generate title from transcript
6. Create directory: .aura/memo/queue/<title>/
7. Move audio.wav and save transcript.txt

On transcription failure:
- Generate fallback title: memo-YYYYMMDD-HHMMSS
- Create directory: .aura/memo/failed/<fallback-title>/
- Save audio.wav (preserve user's recording)
- Print error message with instructions to retry
```

### Exit Codes

- 0: Success (audio recorded, transcribed, titled, saved to queue/)
- 1: Recording failed (sox error, no audio)
- 2: Transcription failed (audio saved to failed/)

## Success Criteria

- [ ] Single command `python .aura/scripts/record_memo.py` records and processes memo
- [ ] Audio is never lost - saved to failed/ if transcription fails
- [ ] Consistent directory structure across queue/, processed/, failed/
- [ ] `aura.process_memo` handles both transcribed and untranscribed memos
- [ ] Documentation updated to reflect new workflow
