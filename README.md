# Aur2

Agentic scaffolding for knowledge work. Skills, issue tracking, and vision capture — wired together.

> Forked from [cdimoush/aura](https://github.com/cdimoush/aura) (coding-focused). Aur2 applies the same agentic scaffolding concept to general work tasks, using markdown as the primary "language" in a version-controlled knowledge base.

## What is Aur2?

Aur2 wraps your repository with Claude Code skills and beads-based issue tracking to support both agents and human operators. It provides the scaffolding layer for [hive-mind](https://github.com/ocampbell-stack/hive-mind) — a template for building persistent, version-controlled knowledge bases managed by parallel AI agents.

**Key Features:**
- **Beads integration** — dependency-aware issue tracking via `bd` CLI
- **Scope planning** — break visions into phased, dependency-mapped tasks
- **Multi-agent ready** — beads carry context between agents via comments and dependency graphs
- **Vision capture** — queue text ideas or record audio via OpenAI Whisper
- **Automatic context injection** — SessionStart hook loads project context + `bd prime`

## Installation

### Prerequisites

- **uv**: Python package manager - [Install uv](https://docs.astral.sh/uv/getting-started/installation/)
- **git**: Version control
- **Claude Code**: [Install Claude Code](https://claude.ai/claude-code)
- **beads**: Issue tracking CLI (required) - [GitHub](https://github.com/steveyegge/beads)
  ```bash
  brew tap steveyegge/beads && brew install beads
  ```
- **sox**: Audio recording
  - macOS: `brew install sox`
  - Ubuntu: `sudo apt-get install sox`
- **ffmpeg**: Audio processing (for transcription)
  - macOS: `brew install ffmpeg`
  - Ubuntu: `sudo apt-get install ffmpeg`

### Install Aur2

```bash
git clone https://github.com/ocampbell-stack/aur2.git
cd aur2
uv venv && source .venv/bin/activate
uv pip install -e . -r .aur2/scripts/requirements.txt
aur2 --version  # Verify installation
```

## Quick Start

### 1. Initialize Aur2 in Your Project

```bash
cd your-project
aur2 init
```

This creates:
- `.aur2/` - Configuration, scripts, visions and plans directories
- `.claude/skills/` - Slash command skills for Claude Code
- `.claude/templates/` - Plan templates (feature, bug)
- `.claude/settings.json` - SessionStart hook for automatic context
- `.beads/` - Task tracking (if beads CLI available)

### 2. Set Up Environment

```bash
# Copy the example env file
cp .aur2/.env.example .aur2/.env

# Add your OpenAI API key (edit the file with your key)
echo "OPENAI_API_KEY=sk-your-key" >> .aur2/.env

# Create a virtual environment for aur2 scripts
uv venv .aur2/.venv
source .aur2/.venv/bin/activate

# Install script dependencies
uv pip install -r .aur2/scripts/requirements.txt
```

### 3. Verify Setup

```bash
# Check aur2 installation
aur2 check

# Start Claude Code - context auto-loads via SessionStart hook
```

### 4. Capture and Process Visions

```bash
# Option A: Text vision — just drop a file
echo "Add user authentication with OAuth" > .aur2/visions/queue/add-auth.txt

# Option B: Audio vision — record and transcribe
source .aur2/.venv/bin/activate
python .aur2/scripts/record_memo.py
# Press Ctrl+C to stop recording

# In Claude Code session:
/aur2.process_visions   # Process all queued visions
```

## Skills Reference

Aur2 provides skills across two namespaces:

**`aur2.*` — General-purpose** (work in any aur2-initialized repo):

| Skill | Description | Example |
|-------|-------------|---------|
| `/aur2.process_visions` | Process all visions from queue (text + audio) | `/aur2.process_visions` |
| `/aur2.scope` | Research codebase and produce a scope file | `/aur2.scope "user authentication system"` |
| `/aur2.execute` | Create beads from scope and implement autonomously | `/aur2.execute .aur2/plans/queue/user-auth/scope.md` |

**`hive.*` — Knowledge base operations** (designed for [hive-mind](https://github.com/ocampbell-stack/hive-mind)):

| Skill | Description |
|-------|-------------|
| `/hive.ingest` | Ingest documents into the knowledge base |
| `/hive.groom` | Audit KB for staleness, inconsistencies, and gaps |
| `/hive.deliver` | Produce external deliverables grounded in KB context |
| `/hive.advise` | Analyze communications and recommend actions |
| `/hive.maintain` | Plan and execute maintenance or improvements to tooling |
| `/hive.iterate` | Address PR review feedback on an existing feature branch |

### Context Injection

Aur2 automatically injects context at session start via Claude Code's hook system. No need to run a prime command - the aur2 context loads automatically when you start a session.

## Using with Hive-Mind

This repo is the **source of truth** for all skills used in [hive-mind](https://github.com/ocampbell-stack/hive-mind). The hive-mind repo gitignores `.claude/skills/` and `.claude/templates/` — they are deployed from here.

**Updating skills in hive-mind:**

```bash
cd ~/path/to/your/hive-mind
aur2 init --force --skip-settings
```

The `--skip-settings` flag preserves the hive-mind repo's custom SessionStart hook (which adds `bd prime` + KB INDEX.md loading on top of the base AUR2.md injection).

`--force` overwrites skill files and templates but preserves `.aur2/visions/` and `.aur2/plans/` content.

## Directory Structure

After `aur2 init`:

```
your-project/
├── .aur2/
│   ├── AUR2.md              # Context file (auto-injected at session start)
│   ├── .gitignore            # Ignores visions contents, .env, .venv/
│   ├── .venv/                # Virtual environment for scripts
│   ├── visions/
│   │   ├── queue/            # Text files or audio dirs waiting to be processed
│   │   ├── processed/        # Successfully processed visions
│   │   └── failed/           # Failed processing attempts
│   ├── plans/
│   │   ├── queue/            # Scoped plans awaiting execution
│   │   └── processed/        # Completed plans
│   └── scripts/
│       ├── record_memo.py    # Record → transcribe → title → queue
│       ├── transcribe.py     # OpenAI Whisper transcription
│       ├── generate_title.py # Intelligent title generation
│       └── requirements.txt  # Script dependencies
├── .beads/                   # Task tracking (if beads available)
└── .claude/
    ├── settings.json         # SessionStart hook configuration
    ├── templates/            # Plan templates (feature.md, bug.md)
    └── skills/
        ├── aur2.execute/
        │   └── SKILL.md
        ├── aur2.process_visions/
        │   └── SKILL.md
        ├── aur2.scope/
        │   └── SKILL.md
        ├── hive.advise/
        │   └── SKILL.md
        ├── hive.deliver/
        │   └── SKILL.md
        ├── hive.groom/
        │   └── SKILL.md
        ├── hive.ingest/
        │   └── SKILL.md
        ├── hive.iterate/
        │   └── SKILL.md
        └── hive.maintain/
            └── SKILL.md
```

## Configuration

### Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `OPENAI_API_KEY` | Yes | API key for transcription and title generation |

## Workflow Examples

### Example 1: Vision to Action

```bash
# Option A: Text vision
echo "Prepare Q1 status update for leadership" > .aur2/visions/queue/q1-status.txt

# Option B: Audio vision
source .aur2/.venv/bin/activate
python .aur2/scripts/record_memo.py
# Press Ctrl+C when done speaking

# In Claude Code session:
/aur2.process_visions
# → Reads vision content
# → Acts on your request
# → Moves to .aur2/visions/processed/
```

### Example 2: Scope and Execute

```bash
# Create a structured scope from a vision
/aur2.scope "Restructure knowledge base for Q2 priorities"
# → Creates .aur2/plans/queue/restructure-kb-q2/scope.md

# Execute the scope (creates beads and implements)
/aur2.execute .aur2/plans/queue/restructure-kb-q2/scope.md
# → Creates beads tasks with dependencies
# → Works through tasks respecting dependencies
```

## Verification

After installation, verify everything works:

```bash
# Quick verification
mkdir /tmp/aur2-test && cd /tmp/aur2-test
git init
aur2 init
aur2 check
```

## Troubleshooting

### "OPENAI_API_KEY not set"

Create a `.env` file in the `.aur2/` directory:
```bash
echo "OPENAI_API_KEY=sk-your-key" > .aur2/.env
```

### "pydub/openai not installed"

Install script dependencies in a virtual environment:
```bash
uv venv .aur2/.venv
source .aur2/.venv/bin/activate
uv pip install -r .aur2/scripts/requirements.txt
```

### Skills not appearing in Claude Code

Ensure you're in a directory with `.claude/skills/`:
```bash
ls .claude/skills/*/SKILL.md
```

If missing, run `aur2 init`.

## Development

Aur2 uses itself for development. The `.aur2/`, `.claude/skills/`, and `.claude/templates/` at the repo root are:

1. **Working copies** - Used when developing aur2 with Claude Code
2. **Template sources** - Copied to target repos by `aur2 init`

This means changes to skills are immediately testable without running init.

```bash
# Edit a skill
vim .claude/skills/aur2.process_visions/SKILL.md

# Test immediately in Claude Code
/aur2.process_visions
```

## Design Decisions

### Why Beads?

Beads provides dependency-aware issue tracking that agents can navigate autonomously. An agent runs `bd ready`, picks a bead, reads comments left by prior agents, does the work, and closes it — unlocking downstream beads. No orchestrator needed.

### Why SessionStart Hook?

Automatic context injection means no manual priming. Every Claude Code session starts with project context (`.aur2/AUR2.md`) and beads workflow guidance (`bd prime`) loaded automatically. Configured in `.claude/settings.json` and merged with existing user settings by `aur2 init`.

### How is this different from the original Aura?

The original [aura](https://github.com/cdimoush/aura) by Connor is agentic scaffolding for **coding** — helping agents plan and write code. Aur2 carries forward the scaffolding concept but applies it to **general knowledge work**: maintaining context repositories, producing stakeholder deliverables, analyzing communications, and grooming knowledge bases. The primary "language" is markdown, not code.

## License

MIT License - see LICENSE file for details.

---

*Built with Claude Code*
