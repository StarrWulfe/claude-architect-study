---
name: flashcards
description: Study flashcards for the Claude Certified Architect exam
argument-hint: topic to study (e.g., agentic-architecture, tool-design, claude-code, prompt-engineering, context-management, all)
---

# Flashcards Skill

Use this skill to study flashcards for the Claude Certified Architect exam.

## Available Topics

- `agentic-architecture`: Agentic Architecture & Orchestration
- `tool-design`: Tool Design & MCP Integration
- `claude-code`: Claude Code Configuration & Workflows
- `prompt-engineering`: Prompt Engineering & Structured Output
- `context-management`: Context Management & Reliability
- `all`: All topics combined

## How to Use

1. Run the flashcard server:
   ```
   python3 scripts/flashcard_server.py --topic <topic>
   ```

2. The server will open automatically in your browser

3. Study with keyboard controls:
   - Space: Flip card
   - Enter: Mark as "Got It"
   - Backspace: Mark as "Needs Work"
   - h/j/k/l or arrows: Navigate Previous/Next

4. Progress is saved locally in your browser

## Adding New Flashcards

Add new flashcards to `flashcards/<topic>-flashcards.md`:

```markdown
### Front
Your question here

### Back
Your answer here (1-3 sentences)
```

Then regenerate with: `python3 scripts/flashcard_server.py --static --topic <topic>`

## Cross-Platform Note

This works with Kilo, Claude Code, and OpenCode. Run the same Python script regardless of which AI app you're using.
