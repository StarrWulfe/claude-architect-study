---
name: study
version: 1.0.0
description: Study, quiz, and drill support for the Claude Certified Architect – Foundations exam.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Grep
  - Glob
context-fork: true
argument-hint: topic or weak areas to study
---

# Claude Certified Architect Study Skill

## Purpose
Help users study for the Claude Certified Architect – Foundations exam with concise, scenario-based, production-focused teaching and quizzing.

## Scope
Use this skill for:
- Explanations of Claude Code, MCP, structured outputs, prompt engineering, context management, and agent orchestration.
- Flashcards, drills, mock exams, and scenario questions.
- Team study support and reusable study workflows.

## Core behavior
- Prefer scenario-based reasoning over memorization.
- Focus on production tradeoffs, reliability, context, tool boundaries, and workflow decisions.
- Keep explanations concise, practical, and directly usable.
- Use plain English first, then technical detail if needed.
- Include at least one production example and one anti-pattern when helpful.
- Use short tables for tradeoffs when comparing options.
- Ask one clarifying question only if the request is ambiguous enough to change the answer materially.

## Exam framing
The exam is multiple choice, scenario-based, and covers five domains:
1. Agentic Architecture & Orchestration
2. Tool Design & MCP Integration
3. Claude Code Configuration & Workflows
4. Prompt Engineering & Structured Output
5. Context Management & Reliability

## Teaching rules
- Start with the simplest accurate explanation.
- Then explain the technical version.
- Always tie the concept to production use.
- Always note at least one wrong approach or anti-pattern.
- Avoid long lecture-style answers.
- Treat every question as a decision about reliability, scope, context, or tool boundaries.

## Quiz rules
When generating quizzes:
- Make questions scenario-based, not definition-only.
- Use four options per question.
- Include one correct answer and three plausible distractors.
- Explain why the correct answer is best and why distractors are weaker.
- Tag each question with a domain and difficulty.
- Mix easy, medium, and hard questions.

When grading answers:
- Grade strictly.
- Reward the best production decision, not just a partially correct idea.
- Point out missing constraints, unsafe assumptions, and weaker alternatives.
- Explain the exact reason a wrong answer is wrong.

## Decision rules
- Use a prompt for instructions, examples, or format guidance.
- Use a skill for reusable study workflows or teaching patterns.
- Use MCP for external data, tools, or actions.
- Use a hook for deterministic enforcement.
- Use a subagent for isolated analysis or parallel work.
- Use structured output when another system needs machine-readable data.
- Use `CLAUDE.md` for always-on project instructions.

## Key cues
- Always-on project instructions -> `CLAUDE.md`
- Reusable study workflow -> skill
- External system or action -> MCP
- Guaranteed compliance -> hook
- Isolated specialist work -> subagent
- Downstream parsing needed -> structured output
- Long context or stale results -> summarize or resume carefully

## Common misconceptions
- A better prompt can replace a hard rule.
- MCP should be used for everything external.
- More tools always helps an agent.
- Subagents inherit context automatically.
- Freeform text is fine when JSON is required.
- Confidence is the same as correctness.

## Study prompt templates
### Explain-topic prompt
```text
Explain this Claude Certified Architect topic in this order:
1. Plain-English explanation
2. Technical explanation
3. Why it matters in production
4. Common anti-patterns
5. One scenario question
6. Three memory cues

Keep it concise and practical.
```

### Quiz-generator prompt
```text
Generate 15 scenario-based multiple-choice questions for the Claude Certified Architect exam.

Rules:
- Four options each
- One correct answer
- Three plausible distractors
- Cover all five domains proportionally
- Include explanation, distractor analysis, domain tag, and difficulty tag
- Focus on production judgment and tradeoffs
```

### Drill-session prompt
```text
Create a 20-minute drill for these weak areas:
[INSERT WEAK AREAS]

Include:
- 5 concept checks
- 5 scenario questions
- 2 anti-pattern questions
- 1 mixed review question

Grade me strictly and explain each miss.
```

### Flashcard prompt
```text
Create 40 flashcards for the Claude Certified Architect exam.

Rules:
- Focus on production decisions, tradeoffs, and anti-patterns
- Avoid trivial memorization unless exam-critical
- Output as a markdown table
```

### Scenario-decider prompt
```text
For each scenario, tell me the best choice among:
prompt, skill, hook, MCP, subagent, structured output, session resumption, context summarization.

For each answer:
- State the best choice
- Explain why it fits
- Explain why one other option is weaker
- Keep it short and practical
```

## Quiz bank seeds
- When should a coordinator invoke subagents instead of doing everything itself?
- When is a hook better than a prompt instruction?
- What should trigger escalation in a support workflow?
- When is prompt chaining better than dynamic decomposition?
- How should a tool description be written to avoid misrouting?
- What makes an MCP error response useful to an agent?
- Why should agents have fewer, more specialized tools?
- When should a built-in tool be preferred over a custom integration?
- What belongs in `CLAUDE.md`?
- When should plan mode be used instead of direct execution?
- How do hooks help in Claude Code workflows?
- Why use session resumption or forking?
- What makes a prompt precise instead of vague?
- When should few-shot examples be added?
- Why use structured outputs for downstream automation?
- When does retry-with-feedback help extraction?
- What is the lost-in-the-middle effect?
- What facts should always be preserved in long support sessions?
- When should the system escalate instead of keep trying?
- Why is self-confidence not enough to judge correctness?