# Claude Certified Architect Study Repository

This repository is designed to support preparation for the **Claude Certified Architect – Foundations** exam. It provides study materials, tracking tools, and a reusable skill for generating quizzes, flashcards, and targeted drills.

## 📁 Project Structure

```
.
├── .claude/
│   └── skills/
│       └── study.md          # Reusable skill for exam preparation (invoked via `/study`)
├── certificates/             # Directory for storing exam certificates (empty initially)
├── claude cert notes/        # Personal notes directory
├── course notes/             # Additional course materials and tracking logs
│   ├── Claude Course notes.md      # Notes from Claude courses
│   ├── claude-101.md               # Introductory Claude course notes
│   ├── study tracker.md            # Logs study sessions (date/time, elapsed time, areas studied, strong/weak points)
│   └── quiz tracker.md             # Tracks quiz scores (date/time, question count, correct/incorrect, percentage, focus areas)
├── references/               # Official reference materials for studying
│   └── Claude+Certified+Architect+–+Foundations+Certification+Exam+Guide.pdf
├── claude-study-pack.md      # Main study guide: exam domains, core references, study goals, daily template, decision rules, anti-patterns, flashcards, scenario drills, review checklist, and prompts for quiz/flashcard/drill generation
├── study-skill.md            # Original skill file (kept for backward compatibility; the active skill is in .claude/skills/study.md)
├── CLAUDE.md                 # Guidance for Claude Code when working in this repository (commands, structure, conventions, decision rules)
├── CHANGELOG.md              # Running log of changes made to this project
└── README.md                 # This file
```

## 📖 Key Files Explained

### `claude-study-pack.md`
The primary study guide containing:
- **Exam domains**: Agentic Architecture & Orchestration, Tool Design & MCP Integration, Claude Code Configuration & Workflows, Prompt Engineering & Structured Output, Context Management & Reliability
- **Core references**: Official documentation links
- **Study goals & daily template**: Structured approach to studying (Read, Extract, Practice, Review)
- **Decision rules**: When to use CLAUDE.md, Skills, MCP, Subagents, Hooks, Structured Outputs, Prompt Engineering
- **Anti-patterns**: Common mistakes to avoid
- **Flashcards & scenario drills**: Pre-made study aids
- **Review checklist & prompts**: Tools for self-assessment and generating custom quizzes/flashcards/drills

### `.claude/skills/study.md` (the active study skill)
A reusable skill that enables:
- **Explanations**: `/study <topic>` → Get plain-English and technical explanations of exam topics with production relevance and anti-patterns
- **Quiz generation**: `/study quiz` → Create 15 scenario-based multiple-choice questions covering all five domains, with explanations and difficulty tags
- **Flashcards**: `/study flashcards` → Generate 40 flashcards focused on production decisions, tradeoffs, and anti-patterns
- **Targeted drills**: `/study drill <weak areas>` → Build a 20-minute drill session with concept checks, scenario questions, anti-pattern questions, and mixed review

> 💡 **Note**: The skill was renamed from `study-skill.md` to `study.md` and moved to `.claude/skills/` to enable the shortened `/study` command. The original `study-skill.md` remains in the root for backward compatibility.

### Tracking Files (`course notes/`)
- **`study tracker.md`**: Use to log each study session. Include:
  - Date/time started & ended
  - Elapsed time
  - Areas studied
  - Strong points (what you understood well)
  - Weak points (needing improvement)
  - Optional notes
- **`quiz tracker.md`**: Use to record quiz results. Include:
  - Date/time started & ended
  - Elapsed time
  - Number of questions
  - Answers correct/incorrect
  - Score percentage
  - Areas to focus on (based on missed questions)
  - Optional notes

### `references/`
Contains official study materials, such as the **Claude Certified Architect – Foundations Certification Exam Guide PDF**.

### `CLAUDE.md`
Provides instructions for Claude Code (or any agentic AI) on how to assist effectively in this repository, including:
- Common development tasks (studying, generating materials)
- Repository structure overview
- Key conventions from the study materials (when to use each extension mechanism)
- Decision rules for Claude Code usage

### `CHANGELOG.md`
A running log of all changes made to the project, updated with each significant modification.

## 🚀 How to Use With Claude Code or Other Agentic AI

### With Claude Code
1. **Invoke the study skill**: Type `/study <topic>` to get an explanation (e.g., `/study MCP`).
2. **Generate study aids**:
   - `/study quiz` → New quiz
   - `/study flashcards` → New flashcard set
   - `/study drill Agentic Architecture, MCP` → Targeted drill on weak areas
3. **Refer to CLAUDE.md** for guidance on how Claude should assist you in this repo.
4. **Update the tracker files** after each study session or quiz to monitor progress.

### With Other Agentic AIs
Even if you're not using Claude Code, you can still leverage this repository:
- Read `claude-study-pack.md` for structured study content.
- Use the prompts in the study pack (e.g., "Explain-topic prompt", "Quiz-generator prompt") manually with your preferred AI.
- Manually update the tracker files in `course notes/` to log your progress.
- Refer to `references/` for official exam materials.
- Follow the conventions in `CLAUDE.md` to understand how to organize your study workflow.

## 📝 Recommended Workflow
1. **Start**: Review `claude-study-pack.md` to understand the exam structure.
2. **Study a topic**: Use `/study <topic>` or manual prompts to learn.
3. **Practice**: Generate a quiz with `/study quiz` or create flashcards.
4. **Track**: Log your session in `study tracker.md` and quiz results in `quiz tracker.md`.
5. **Review**: Identify weak points from trackers and create targeted drills with `/study drill <weak areas>`.
6. **Iterate**: Repeat until you consistently score well on generated quizzes.

## 🔧 Customization
- Add your own notes to `claude cert notes/` or `course notes/`.
- Extend the study skill by editing `.claude/skills/study.md`.
- Update `CHANGELOG.md` with any modifications you make.

---

Happy studying, and best of luck on your Claude Certified Architect exam! 🎯