# Flashcards

This directory contains topic-specific flashcard sets for the Claude Certified Architect exam.

## Available Topics

| Topic | File | Description |
|-------|------|-------------|
| Agentic Architecture | `agentic-architecture-flashcards.md` | Agent loops, multi-agent orchestration, hooks |
| Tool Design | `tool-design-flashcards.md` | MCP integration, tool descriptions, error handling |
| Claude Code | `claude-code-flashcards.md` | CLAUDE.md, skills, hooks, workflows |
| Prompt Engineering | `prompt-engineering-flashcards.md` | Structured outputs, precision, examples |
| Context Management | `context-management-flashcards.md` | Lost-in-middle, escalation, context bloat |

## Adding New Flashcards

Add flashcards in this format:

```markdown
### Front
Your question here

### Back
Your answer here (1-3 sentences)
```

## Running Flashcards

Using the Python server (recommended):
```bash
python3 scripts/flashcard_server.py --topic <topic>
```

Using static HTML:
```bash
python3 scripts/flashcard_server.py --static --topic <topic>
# Then open flashcards.html in browser
```

Available topics: `agentic-architecture`, `tool-design`, `claude-code`, `prompt-engineering`, `context-management`, `all`
