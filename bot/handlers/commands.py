def handle_start() -> str:
    return (
        "👋 Welcome to SE Toolkit Bot!\n"
        "Use /help to see available commands."
    )

def handle_help() -> str:
    return (
        "Available commands:\n"
        "/start — welcome message\n"
        "/help — this help\n"
        "/health — check backend status\n"
        "/scores <lab> — get scores for a lab\n"
        "/labs — list available labs"
    )

def handle_health() -> str:
    return "⚙️ Health check: not implemented yet (placeholder)"

def handle_scores(args: str) -> str:
    return f"📊 Scores for '{args}': not implemented yet (placeholder)"

def handle_labs() -> str:
    return "📚 Labs list: not implemented yet (placeholder)"

def handle_unknown(text: str) -> str:
    return f"❓ Unknown command or message: '{text}'"