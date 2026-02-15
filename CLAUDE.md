# Aur2 - Claude Code Agent Guide

This document provides context for Claude Code agents working on the Aur2 project itself (not repos wrapped by Aur2).

## Project Overview

Aur2 is agentic scaffolding for knowledge work. It wraps repositories with Claude Code skills, beads-based issue tracking, and vision capture (text + audio). Forked from [cdimoush/aura](https://github.com/cdimoush/aura) (coding-focused) and repurposed for general work tasks using markdown as the primary "language".

**Core Philosophy**: Remove friction between ideas and action.

## Architecture

### Project Structure

```
aur2/
├── .aur2/                   # Working copy (dogfood) AND template source
│   ├── .gitignore           # Ignores visions/*, .env
│   ├── .env.example         # Example environment file
│   ├── AUR2.md              # Context file (injected at session start)
│   ├── visions/
│   │   ├── queue/           # Text files OR audio+transcript dirs
│   │   ├── processed/       # Successfully processed
│   │   └── failed/          # Failed processing
│   ├── plans/
│   │   ├── queue/           # Scoped plans awaiting execution
│   │   └── processed/       # Executed/completed plans
│   └── scripts/
│       ├── record_memo.py   # Record → transcribe → title → queue
│       ├── transcribe.py    # OpenAI Whisper transcription
│       ├── generate_title.py # Intelligent title generation
│       └── requirements.txt  # Script dependencies
├── .claude/
│   ├── settings.json        # SessionStart hook configuration
│   ├── templates/           # Plan templates (feature, bug, knowledge-project, research)
│   └── skills/              # Working copy (dogfood) AND template source
│       ├── aur2.execute/
│       │   └── SKILL.md
│       ├── aur2.process_visions/
│       │   └── SKILL.md
│       ├── aur2.scope/
│       │   └── SKILL.md
│       ├── hive.advise/
│       │   └── SKILL.md
│       ├── hive.deliver/
│       │   └── SKILL.md
│       ├── hive.groom/
│       │   └── SKILL.md
│       ├── hive.ingest/
│       │   └── SKILL.md
│       └── hive.iterate/
│           └── SKILL.md
├── src/aur2/
│   ├── __init__.py          # Package init
│   ├── cli.py               # Click CLI entry point
│   ├── config.py            # Configuration constants
│   └── init.py              # Scaffolding logic
├── pyproject.toml           # Package metadata
└── README.md                # User documentation
```

**Key insight**: The `.aur2/`, `.claude/skills/`, and `.claude/templates/` at repo root serve dual purposes:
1. **Working copies** - Used when developing aur2 with Claude Code
2. **Template sources** - Copied to target repos by `aur2 init`

### Core Components

#### CLI (`src/aur2/cli.py`)

Entry point for `aur2 init`, `aur2 check`, and `aur2 remove` commands.

#### Init Logic (`src/aur2/init.py`)

Handles template file discovery, copying, and settings.json merging:

```python
def get_template_files() -> list[tuple[Path, Path]]:
    """Returns (src, dst) pairs for all template files."""

def merge_settings_json(target_path, force=False) -> dict:
    """Merge SessionStart hook into existing settings.json."""

def init_aur2(force=False, dry_run=False, skip_settings=False) -> dict:
    """Initialize aur2 in target directory."""
```

The init process:
1. Creates folder structure: `.aur2/visions/queue/`, `visions/processed/`, `visions/failed/`, `plans/queue/`, `plans/processed/`
2. Copies `.aur2/` files (scripts, AUR2.md, .gitignore, etc.)
3. Copies `.claude/templates/` files
4. Copies `.claude/skills/` subdirectories
5. Merges SessionStart hook into `.claude/settings.json` (unless `--skip-settings`)
6. Runs `bd init` if beads CLI available

#### Skills (Dogfooding)

**Skill directory** (`.claude/skills/` at repo root):
- Source for `.claude/skills/` in target repositories
- Each skill is a directory containing `SKILL.md`
- Skills are invoked via `/skill-name` in Claude Code
- Also used directly when developing aur2

**Available Skills**:
| Skill | Purpose |
|-------|---------|
| `aur2.process_visions` | Process all visions from queue (text + audio). Context-aware: modifies KB files in hive-mind, keeps output in vision dir for codebases |
| `aur2.scope` | Research the project and produce a scope file. Domain-aware: selects template based on context (code vs KB vs research) |
| `aur2.execute` | Create beads from a scope file and implement autonomously. Domain-aware implementation guidelines for code and KB contexts |
| `hive.ingest` | Ingest documents into the knowledge base (hive-mind) |
| `hive.groom` | Audit KB for staleness, inconsistencies, and gaps (hive-mind) |
| `hive.deliver` | Produce external deliverables grounded in KB context (hive-mind) |
| `hive.advise` | Analyze communications and recommend actions (hive-mind) |
| `hive.iterate` | Address PR review feedback on an existing feature branch (hive-mind) |

> `hive.*` skills are designed for the [hive-mind](https://github.com/ocampbell-stack/hive-mind) repo but are maintained here as the source of truth.

### Beads Integration Pattern

All `hive.*` skills follow a standard lifecycle defined in `protocols/skill-lifecycle.md` (deployed to target repos). When adding or modifying skills, maintain this pattern:

**Standard lifecycle** (referenced by every `hive.*` skill):

1. **Mode** → **Beads setup** → **Complexity check** → **Alignment** → [Skill-specific work] → **Verify** → **Close and hand off**

Each skill's SKILL.md references `protocols/skill-lifecycle.md` for the common steps, then provides only its unique "Alignment Focus" and "Core Work" sections. This avoids repeating the same beads/alignment/verification boilerplate in every skill.

**Key protocols** (deployed to target repos by `aur2 init`):
- `protocols/workflow.md` — mode detection, branching, PR lifecycle, feedback iteration
- `protocols/alignment.md` — context gathering, impact assessment, confirmation
- `protocols/quality.md` — compound deliverable, verification checklist, privacy standards
- `protocols/skill-lifecycle.md` — the common hive.* skill wrapper

**Design rationale**:
- Each skill invocation = one bead. Don't decompose single-session work into sub-beads (overhead exceeds benefit).
- Verification stays inline within the skill, not as a separate bead (avoids unnecessary context reload).
- Follow-up beads (remediation items, action items) are created during execution and feed `bd ready` for other agents.
- `bd comments add` is the primary inter-agent context-passing mechanism — always leave a useful comment before closing.

## Visions Pipeline

### Recording Audio Visions

Use `record_memo.py` to record, transcribe, and queue audio visions:

```bash
python .aur2/scripts/record_memo.py [--max-duration SECONDS]
```

The script:
1. Records audio via sox (press Ctrl+C to stop)
2. Transcribes via OpenAI Whisper
3. Generates a kebab-case title from the transcript
4. Saves to `.aur2/visions/queue/<title>/` with `audio.wav` and `transcript.txt`

If transcription fails, audio is preserved in `.aur2/visions/failed/` with a timestamp-based title.

### Text Visions

Place a `.txt` file directly in `.aur2/visions/queue/` to create a text vision.

### Skill Anatomy

Claude Code skills have this structure:

```
.claude/skills/<skill-name>/
└── SKILL.md
```

With frontmatter:

```markdown
---
name: skill.name
description: What the skill does
argument-hint: <optional input hint>
disable-model-invocation: false
allowed-tools: Bash, Read, Write, Edit, Glob, Grep, WebFetch, WebSearch
---

# Skill Title

Instructions for the agent...
```

### Frontmatter Conventions

All skills in this project follow these conventions:

| Field | Standard value | Rationale |
|-------|---------------|-----------|
| `name` | `namespace.skillname` | Required on all skills. `aur2.*` for general-purpose, `hive.*` for KB operations. |
| `description` | Unquoted string | What the skill does. Claude uses this to decide when to apply the skill. |
| `argument-hint` | Present only if skill takes input | Shown in autocomplete. |
| `disable-model-invocation` | `false` | All skills allow Claude to invoke them. This enables complexity escalation — `hive.*` skills can escalate to `/aur2.scope` autonomously when they detect multi-session work. |
| `allowed-tools` | `Bash, Read, Write, Edit, Glob, Grep` | Full tool access on all skills. Agents on worktree branches are isolated by git — the PR review process is the human-in-the-loop check, not per-tool permission prompts. |

**Why `disable-model-invocation: false` everywhere**: The escalation model requires it. When a `hive.*` skill detects multi-session complexity, it escalates to `/aur2.scope` to produce a scope PR for user review. If `/aur2.scope` had `disable-model-invocation: true`, the agent couldn't invoke it and escalation would be broken. `/aur2.execute` is invoked separately after the user approves the scope.

**Why uniform `allowed-tools`**: Agents working autonomously on feature branches need full tool access to make progress without blocking on permission prompts. Branch isolation + PR review is the safety mechanism, not tool restrictions.

## Development Workflow

### Dogfooding

Aur2 is developed using aur2. The skills and scripts at the repo root are the same ones copied to target repos.

**Workflow**:
1. Edit `.claude/skills/aur2.process_visions/SKILL.md`
2. Run `/aur2.process_visions` to test immediately
3. Fix issues, repeat

### Adding a New Skill

1. Create skill directory at repo root:
   ```bash
   mkdir -p .claude/skills/aur2.newskill
   touch .claude/skills/aur2.newskill/SKILL.md
   ```

2. Add frontmatter and instructions

3. Test immediately with `/aur2.newskill` in Claude Code

4. Update README.md skill reference

5. **Namespace convention**: Use `aur2.*` for general-purpose skills that work in any repo (code or knowledge work). Use `hive.*` for skills specific to hive-mind knowledge base operations. The `aur2.*` skills are domain-aware — they detect project context and adapt their behavior (template selection, research strategy, implementation guidelines) accordingly.

### Running Tests

```bash
# Test scripts directly from aur2 root
python .aur2/scripts/generate_title.py --text "test memo"

# Test init dry-run
uv run aur2 init --dry-run
```

## Key Files

| File | Purpose |
|------|---------|
| `src/aur2/cli.py` | CLI commands (`init`, `check`, `remove`) |
| `src/aur2/init.py` | Scaffolding logic |
| `src/aur2/config.py` | Configuration constants |
| `.claude/templates/*.md` | Plan templates (feature, bug, knowledge-project, research) |
| `.claude/skills/*/SKILL.md` | Skill sources (dogfood + template) |
| `.claude/settings.json` | SessionStart hook configuration |
| `.aur2/AUR2.md` | Context file (injected at session start) |
| `.aur2/scripts/*.py` | Portable Python scripts (dogfood + template) |

### Downstream Repos

This repo is the **source of truth** for skills deployed to [hive-mind](https://github.com/ocampbell-stack/hive-mind). Hive-mind gitignores `.claude/skills/` and `.claude/templates/` — they come from here via `aur2 init --force --skip-settings`. The `--skip-settings` flag preserves hive-mind's custom SessionStart hook (which extends the base hook with `bd prime` + KB INDEX.md loading).

## Troubleshooting

### Templates Not Copying

Check that files exist at repo root:
```bash
ls -la .aur2/scripts/
ls -la .claude/skills/
ls -la .claude/templates/
```

### Init Fails Silently

Run with verbose output:
```bash
uv run aur2 init --dry-run
```

### SessionStart Hook Not Working

Check settings.json has the hook:
```bash
cat .claude/settings.json
```

Should contain a `SessionStart` hook that cats `.aur2/AUR2.md` and runs `bd prime`.
