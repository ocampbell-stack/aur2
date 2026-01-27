# Aura Context

Aura is a voice-driven development workflow. Voice memos are transcribed and turned into code.

## Available Skills

| Skill | Purpose |
|-------|---------|
| `/aura.process_memo` | Process all voice memos from queue |
| `/aura.epic <vision>` | Break a vision into an epic with tasks |
| `/aura.create_beads <epic>` | Convert epic tasks to beads tickets |
| `/aura.implement <epic or bead>` | Implement beads in dependency order |

## Recording Voice Memos

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

## Folder Structure

```
.aura/
├── memo/
│   ├── queue/           # Pending voice memos (<title>/audio.wav + transcript.txt)
│   ├── processed/       # Successfully processed (<title>_<timestamp>/)
│   └── failed/          # Failed processing (audio preserved)
├── epics/               # Epic planning documents
├── scripts/
│   ├── record_memo.py   # Record → transcribe → title → queue
│   ├── transcribe.py    # OpenAI Whisper transcription
│   └── generate_title.py # Intelligent title generation
└── aura.md              # This file (injected at session start)
```

## Workflow

1. **Record** - Run `python .aura/scripts/record_memo.py`
2. **Queue** - Memo saved to `.aura/memo/queue/<title>/` with audio and transcript
3. **Process** - `/aura.process_memo` acts on requests from memos
4. **Plan** - `/aura.epic` for larger features needing breakdown
5. **Track** - `/aura.create_beads` converts epic to trackable tickets
6. **Implement** - `/aura.implement` works through tickets in order

## Context Injection

This file is automatically injected via Claude Code's SessionStart hook.
No need to run `/prime` - context is loaded automatically.
