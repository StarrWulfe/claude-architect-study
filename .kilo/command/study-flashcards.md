---
description: Study flashcards for a specific topic
subtask: true
---

Study flashcards by starting a local flashcard server.

Available topics:
- agentic-architecture: Agentic Architecture & Orchestration
- tool-design: Tool Design & MCP Integration  
- claude-code: Claude Code Configuration & Workflows
- prompt-engineering: Prompt Engineering & Structured Output
- context-management: Context Management & Reliability
- all: All topics

Run the flashcard server with the topic argument:
```
python3 scripts/flashcard_server.py --topic $1
```

If flashcards don't exist for the topic yet, generate them first using the study skill, then save to flashcards/ directory before running the server.
