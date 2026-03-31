# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased] - 2026-03-31
### Added
- Initial CLAUDE.md file providing guidance for Claude Code usage in this repository
- Study tracker files in `course notes/` directory:
  - `study tracker.md` - logs study sessions with timestamps, elapsed time, areas studied, strong/weak points
  - `quiz tracker.md` - tracks quiz scores with timestamps, question counts, correct/incorrect answers, percentage scores, and focus areas
- Reference to the official exam guide in `references/` directory
- Created `.claude/skills/study.md` skill (originally `study-skill.md`) for exam preparation support
- Updated CLAUDE.md to document repository structure and usage instructions
- Flashcard study system with local web server:
  - `scripts/flashcard_server.py` - Python server that serves flashcards and logs to study tracker
  - `scripts/templates/flashcard.html` - Browser-based flashcard UI with timer
  - `flashcards/` directory with topic-specific flashcard sets:
    - `agentic-architecture-flashcards.md`
    - `tool-design-flashcards.md`
    - `claude-code-flashcards.md`
    - `prompt-engineering-flashcards.md`
    - `context-management-flashcards.md`
  - `.kilo/command/study-flashcards.md` - Kilo command for launching flashcards
  - `.claude/skills/flashcards/SKILL.md` - Claude Code skill for launching flashcards

### Changed
- Renamed study skill from `claude-certified-architect-study` to `study` for easier invocation (`/study <topic>`)
- Updated all references in CLAUDE.md to use the shortened `/study` command

### Fixed
- Windows compatibility: statusline configuration now uses PowerShell (`statusline-command.ps1`) instead of bash script
- Flashcard UI: fixed mirrored text on card flip using preserve-3d and backface-visibility

## [Initial Setup] - 2026-03-29
### Added
- Repository initialized with study materials:
  - `claude-study-pack.md` - main study guide with exam domains and practice templates
  - `study-skill.md` (later renamed to `study.md`) - reusable skill for generating quizzes, flashcards, and drills
  - `course notes/Claude Course notes.md` and `course notes/claude-101.md` - course reference materials
  - Directories: `certificates/`, `claude cert notes/`, `course notes/`, `references/`
