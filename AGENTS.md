# AGENTS.md

This file provides guidance for agentic coding agents working in this repository.

## Repository Purpose

This is a study repository for preparing for the **Claude Certified Architect Exam**. The repository contains:
- Study guides and flashcards in markdown files
- Course notes in `course notes/`
- References in `references/`
- Claude Code skills in `.claude/skills/`

## No Build/Test Commands

This is not a code project. There are no build, lint, or test commands. All content is markdown-based study materials. Agents should focus on generating, organizing, and improving study content.

## Agent Workflow Guidelines

### Study Session Assistance
When asked to help study, agents should:
1. Use the study skill (`/study <topic>`) for explanations, quizzes, or flashcards
2. Generate scenario-based questions focusing on production decisions
3. Create flashcards with clear questions and concise answers (1-3 sentences)
4. Include tradeoffs and anti-patterns when teaching concepts

### Content Generation
- Generate quizzes: 10-15 scenario-based questions covering exam domains
- Generate flashcards: 20-40 cards focusing on decision rules
- Generate drills: Targeted practice on weak areas identified in trackers

### Tracking Progress
- Update `course notes/study tracker.md` after study sessions
- Update `course notes/quiz tracker.md` after taking quizzes
- Note strong areas, weak areas, and areas needing review

## Code Style Guidelines

### General Conventions
- Use clear, concise language in all markdown files
- Prefer scenario-based content over definitions
- Include tradeoffs and anti-patterns when explaining concepts
- Keep explanations practical and directly usable

### Markdown Formatting
- Use ATX-style headers (`#`, `##`, `###`)
- Use fenced code blocks with language hints for any code examples
- Use bullet points for lists, not numbered steps unless sequence matters
- Use tables for structured data (flashcards, quiz questions)
- Limit line length to 100 characters where practical

### File Naming
- Use lowercase with hyphens: `study-tracker.md`, not `studyTracker.md`
- Use descriptive names: `claude-101.md`, not `notes.md`
- Prefix files with category where ambiguous: `course notes/claude-course.md`

### Content Organization
- Each concept file should cover one topic
- Include: key idea, tradeoff, anti-pattern, production scenario
- Use consistent section headers across files
- Cross-reference related concepts with links

## Study Content Conventions

### Flashcards
- Front: One clear question
- Back: Concise answer (1-3 sentences)
- Focus on production decisions, not definitions

### Quiz Questions
- Scenario-based, not definition-only
- Four options, one correct answer
- Include explanation and why distractors are wrong
- Tag with domain and difficulty (easy/medium/hard)

### Decision Rules
- Always provide decision rules for tool selection
- Include anti-patterns for common mistakes
- Tie concepts to production use cases

## Key Patterns (from Study Materials)

### When to Use Each Extension
- `CLAUDE.md`: Always-on project conventions and instructions
- Skill: Reusable knowledge or workflow instructions
- MCP: External services, data, or actions
- Subagent: Isolation or parallel work
- Hook: Deterministic automation outside model loop
- Structured output: Machine-readable data for consumers

### Anti-Patterns to Avoid
- Overloading prompts with everything
- Using MCP when a skill would suffice
- Using hooks when reasoning is needed
- Carrying noisy or stale context
- Writing vague success criteria
- Skipping schema design for parsed outputs

## Exam Domains

Agents should be familiar with these domains for generating relevant study content:
1. Agentic Architecture & Orchestration
2. Tool Design & MCP Integration
3. Claude Code Configuration & Workflows
4. Prompt Engineering & Structured Output
5. Context Management & Reliability

## Adding Content

### New Study Materials
1. Add to appropriate directory (`course notes/`, root, or `.claude/skills/`)
2. Follow markdown formatting conventions
3. Include decision rules and anti-patterns
4. Update `claude-study-pack.md` if adding new domains

### Updating Trackers
- `course notes/study tracker.md`: Log study sessions with timestamp, elapsed time, topics
- `course notes/quiz tracker.md`: Log quiz scores with timestamp, question count, correct/total

## Important Files

- `claude-study-pack.md`: Main study guide with exam domains and decision rules
- `CLAUDE.md`: Project conventions for Claude Code
- `.claude/skills/study.md`: Reusable skill for generating study content
- `study-skill.md`: Original skill file (kept for compatibility)

## Git Workflow

- Commit meaningful changes with descriptive messages
- Keep commits focused on single topics
- Do not commit generated PDFs or large binaries