# Flashcard Scripts

## flashcard_server.py

Serves a flashcard study app with timer. Extracts cards from `flashcards/` directory.

### Usage

```bash
# Study specific topic (opens browser automatically)
python3 scripts/flashcard_server.py --topic agentic-architecture

# Study all topics
python3 scripts/flashcard_server.py --topic all

# Don't open browser automatically
python3 scripts/flashcard_server.py --topic agentic-architecture --no-open

# Use custom port
python3 scripts/flashcard_server.py --topic agentic-architecture --port 9000

# Generate static HTML instead of running server
python3 scripts/flashcard_server.py --static --topic agentic-architecture
```

### Available Topics

- `agentic-architecture` - Agent loops, orchestration, hooks
- `tool-design` - MCP, tool descriptions, error handling
- `claude-code` - CLAUDE.md, skills, workflows
- `prompt-engineering` - Structured outputs, precision
- `context-management` - Context bloat, escalation
- `all` - All topics combined
