# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Common Development Tasks

### Studying for the Claude Certified Architect Exam
- Use the study skill: `/study <topic>` to get explanations, quizzes, or flashcards on exam topics
- Example: `/study MCP` for information about Model Context Protocol
- Example: `/study "Agentic Architecture"` for explanations about agent orchestration

### Generating Study Materials
- Create flashcards: `/study flashcards`
- Generate quiz questions: `/study quiz`
- Create targeted drills: `/study drill <weak areas>`

### Exam Preparation Workflow
1. Review core concepts using the claude-study-pack.md reference
2. Use the study skill for active recall and scenario-based practice
3. Focus on decision rules and anti-patterns for exam success
4. Practice with generated quizzes and flashcards

## Repository Structure
- `claude-study-pack.md`: Main study guide with exam domains, references, and practice templates
- `.claude/skills/study.md`: Reusable skill for generating study content (quizzes, flashcards, drills) - invoked via `/study <topic>`
- `study-skill.md`: Original skill file (kept for backward compatibility)
- `certificates/`: Directory for storing exam certificates (currently empty)
- `claude cert notes/`: Personal notes directory
- `course notes/`: Additional course materials directory
  - `Claude Course notes.md`: Notes from Claude courses
  - `claude-101.md`: Introductory Claude course notes
  - `study tracker.md`: Logs study sessions with timestamps, elapsed time, areas studied, strong/weak points
  - `quiz tracker.md`: Tracks quiz scores with timestamps, question counts, correct/incorrect answers, percentage scores, and focus areas
- `references/`: Course reference materials for studying
  - `Claude+Certified+Architect+–+Foundations+Certification+Exam+Guide.pdf`: Official exam guide

## Key Conventions from Study Materials
- Use `CLAUDE.md` for always-on project conventions and instructions
- Use Skills for reusable knowledge or workflow instructions (like this study skill)
- Use MCP for connecting to external services, tools, data, or actions
- Use Subagents for isolated analysis or parallel work
- Use Hooks for deterministic automation outside the model loop
- Use Structured Outputs when downstream systems need machine-readable data
- Use Prompt Engineering for instructions, examples, format, and task clarity
- Use Context Engineering when managing what should and should not stay in context

## Decision Rules for Claude Code Usage
- Prefer scenario-based reasoning over memorization
- Focus on production tradeoffs, reliability, context, tool boundaries, and workflow decisions
- Keep explanations concise, practical, and directly usable
- Always tie concepts to production use cases
- Note at least one wrong approach or anti-pattern when teaching concepts