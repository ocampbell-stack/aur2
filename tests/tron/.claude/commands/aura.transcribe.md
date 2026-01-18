---
allowed-tools: Bash(python:*), Read
description: Transcribe audio file to text
argument-hint: <audio-file-path>
---

# Transcribe Audio

Transcribe the provided audio file using OpenAI Whisper API via the local transcription script.

## Prerequisites

- `OPENAI_API_KEY` environment variable must be set (in `.env` or exported)
- Dependencies installed: `pip install -r .aura/scripts/requirements.txt`
- Supported formats: mp3, m4a, wav, webm (max 25MB)

## Instructions

1. Verify the audio file exists:
   ```bash
   ls -la "$ARGUMENTS"
   ```

2. Transcribe using the local script:
   ```bash
   python .aura/scripts/transcribe.py "$ARGUMENTS"
   ```

3. Display the transcription result.

## Error Handling

If transcription fails:
- **"OPENAI_API_KEY not set"**: Create `.env` file with `OPENAI_API_KEY=sk-your-key`
- **"pydub not installed"**: Run `pip install -r .aura/scripts/requirements.txt`
- **"File too large"**: Compress with `ffmpeg -i input.m4a -vn -ac 1 -ar 16000 -b:a 48k output.m4a`

## After Transcription

You can:
- Summarize the content
- Extract action items or tasks
- Create meeting notes
- Answer questions about what was discussed
- Use `/aura.act` for full processing workflow
