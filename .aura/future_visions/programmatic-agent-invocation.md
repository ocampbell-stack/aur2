# Programmatic Agent Invocation

## Vision
Aura can invoke Claude Code programmatically via `aura run`, enabling skills to be chained without interactive sessions. The user writes a vision, hands it off, and gets back a branch with commits.

## Key Ideas
- Use `claude -p <prompt> --output-format stream-json` to invoke Claude Code as a subprocess
- Parse JSONL output for session_id, is_error, total_cost_usd, duration
- Sanitized subprocess environment (only pass required env vars)
- Structured logging: prompts sent, raw output, execution logs per run
- Lives in `src/aura/` as a CLI command (not copied scripts) — single source of truth, upgradeable

## Interface
```
aura run <skill-name> [args...]
aura chain scope execute        # run scope, feed output to execute
```

## Depends On
- Scope and execute skills working reliably in interactive mode first
- Proven through manual dogfooding before automating

## Reference
- tac-4 ADWS `agent.py` for subprocess pattern and JSONL parsing
- tac-4 `data_types.py` for Pydantic models (AgentPromptRequest/Response)
