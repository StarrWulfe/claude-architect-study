# Claude Certified Architect Study Pack

## Exam domains
- Agentic Architecture & Orchestration
- Tool Design & MCP Integration
- Claude Code Configuration & Workflows
- Prompt Engineering & Structured Output
- Context Management & Reliability

## Core references
- Claude Code docs: extensions, CLAUDE.md, Skills, MCP, Subagents, Hooks.
- Claude prompt engineering overview: clarity, examples, XML, thinking, chaining.
- Claude structured outputs docs: schema-constrained output.
- MCP docs: tools, resources, prompts, and external system integration.
- Anthropic context engineering article: managing full inference context.

## My study goals
- Understand the exam domains and what kinds of decisions they test.
- Recognize when to use prompt-only, skill, MCP, hook, or subagent.
- Write better prompts with clearer success criteria and structure.
- Design reliable, low-noise context and tool systems.
- Answer scenario questions by choosing the best architecture, not just the most advanced one.

## My weak areas
- [ ]
- [ ]
- [ ]
- [ ]

## Daily study template
### Read
- One official doc section.
- One community guide or video summary.

### Extract
- 5 key ideas.
- 3 tradeoffs.
- 3 anti-patterns.
- 1 production scenario.

### Practice
- 10 flashcards.
- 5 scenario questions.
- 1 written explanation in plain English.

### Review
- What did I confuse?
- What rule should I remember next time?
- What would I change in a real project?

## Decision rules
- Use `CLAUDE.md` for always-on project conventions.
- Use a Skill for reusable knowledge or workflow instructions.
- Use MCP for external services, data, or actions.
- Use a Subagent when I need isolation or parallel work.
- Use a Hook for deterministic automation outside the model loop.
- Use structured outputs when the consumer needs reliable machine-readable data.
- Use prompt engineering for instructions, examples, format, and task clarity.
- Use context engineering when the problem is really about what should and should not stay in context.

## Anti-patterns
- Overloading the prompt with everything.
- Using MCP for something that should be a simple skill or prompt.
- Using a hook when the task needs reasoning.
- Letting the model carry noisy or stale context.
- Writing vague success criteria.
- Skipping schema design for outputs that need to be parsed.

## Flashcards
### Front
What is `CLAUDE.md` best for?

### Back
Always-on project conventions and instructions that Claude should see every session.

### Front
When should I use MCP instead of a skill?

### Back
Use MCP when Claude needs to connect to external services, tools, data, or actions.

### Front
What problem do subagents solve?

### Back
They isolate work in a separate context so the main conversation stays focused.

### Front
What do hooks do?

### Back
They run deterministic automation outside the model loop.

### Front
Why use structured outputs?

### Back
To make the model return reliable machine-readable data that matches a schema.

## Scenario drills
### Scenario 1
A task needs database lookup and Slack notification.
- Decide: MCP, hook, skill, or prompt?
- Why?

### Scenario 2
A project has strict conventions every response must follow.
- Decide: CLAUDE.md, skill, or prompt?
- Why?

### Scenario 3
You need three independent reviewers checking different risks.
- Decide: subagent, skill, or hook?
- Why?

### Scenario 4
You need consistent JSON for downstream automation.
- Decide: structured output or freeform?
- Why?

### Scenario 5
A prompt is too long and full of irrelevant references.
- Decide: prompt fix or context engineering change?
- Why?

## Final review checklist
- Can I explain each domain in one sentence?
- Can I choose the right extension mechanism quickly?
- Can I identify the anti-pattern in a scenario?
- Can I explain prompt vs context vs tool design?
- Can I justify why the wrong answer is wrong?

## Quiz generator prompt
Generate 15 Claude Certified Architect exam questions.

Rules:
- Scenario-based, not definition-only.
- Four options each.
- One correct answer.
- Cover all 5 domains.
- Include explanation and why distractors are wrong.
- Tag each question with domain and difficulty.


## Weak-area drill prompt
I am weak in: [insert topics]

Create a 20-minute drill with:
- 5 concept checks
- 5 scenario questions
- 2 anti-pattern questions
- 1 final mixed review

Grade me strictly and explain each mistake.

## Flashcard maker prompt
Create 40 flashcards for the Claude Certified Architect exam.

Rules:
- Focus on production decisions.
- Include tradeoffs and anti-patterns.
- Avoid trivial memorization.
- Output as a markdown table.
