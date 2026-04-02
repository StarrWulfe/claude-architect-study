---
description: Generate a scenario-based multiple choice quiz for exam prep
argument-hint: topic (e.g., agentic-architecture, tool-design, prompt-engineering, context-management, all)
---

Generate a scenario-based multiple choice quiz for Claude Certified Architect exam.

## Quiz Rules

1. **10-15 questions** covering the topic
2. **Scenario-based** - real production situations, not definitions
3. **4 options per question** (A, B, C, D)
4. **RANDOMIZED correct answers** - distribute evenly across A/B/C/D (no more than 3-4 of any letter)
5. **One correct answer** per question
6. **Include explanation** for why correct answer is right and why distractors are wrong
7. **Tag each question** with domain and difficulty (easy/medium/hard)

## Question Flow

1. Show question with 4 options
2. Wait for user answer (A/B/C/D)
3. Show result with explanation
4. Continue to next question

## Available Topics

- `agentic-architecture`: Agentic Architecture & Orchestration
- `tool-design`: Tool Design & MCP Integration
- `claude-code`: Claude Code Configuration & Workflows
- `prompt-engineering`: Prompt Engineering & Structured Output
- `context-management`: Context Management & Reliability
- `all`: All topics combined

## Example Question Format

**Q1.** [Scenario description]

A) [Option A]  
B) [Option B]  
C) [Option C]  
D) [Option D]

---

**Answer:** [Letter] ✓ (or ✗)

**Explanation:** [Why correct answer is right]

**Why others wrong:** [Brief why each distractor is incorrect]

---

## Important: Randomization

When generating, ensure correct answers are distributed:
- ~25% correct answers should be A
- ~25% correct answers should be B
- ~25% correct answers should be C
- ~25% correct answers should be D

Avoid patterns like all answers being B or sequential patterns like A,B,C,D,A,B,C,D

After quiz, update `course notes/quiz tracker.md` with score and notes.
