# SE Toolkit Bot — Development Plan

## Overview
Build a Telegram bot that integrates with the LMS backend and LLM API.
The bot is structured around testable handlers — plain functions that take
input and return text, with no Telegram dependency.

## Architecture
- `bot.py` — entry point; routes `--test` CLI mode or starts Telegram polling
- `handlers/` — pure functions per command, independently testable
- `services/` — HTTP clients for LMS API and LLM API
- `config.py` — loads environment variables from `.env.bot.secret`

## Tasks

### Task 1: Scaffold
Create project structure, pyproject.toml, handler stubs, and --test mode.
Verify all commands exit 0 with output.

### Task 2: Backend Integration
Implement `/health` (GET /health), `/scores <lab>`, `/labs` using httpx.
Read LMS_API_URL and LMS_API_KEY from config.

### Task 3: LLM / Intent Routing
Route free-text messages (e.g. "what labs are available") to LLM API.
Use LLM_API_KEY. Parse intent and dispatch to correct handler.

### Task 4: Deployment
Run bot via `nohup` on VM. Ensure `.env.bot.secret` is present.
Verify via `--test` and live Telegram interaction.

## Testing Strategy
Every handler is tested via `--test` flag before deploying to Telegram.
This decouples logic verification from Telegram connectivity.