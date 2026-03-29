anthropic.skilljar.com



🌟 Main Points from Getting Better Results
🧩 Common Challenges When Using Claude — and How to Fix Them
Claude’s responses can miss the mark for predictable reasons. The page outlines six common issues:

1. Responses feel too generic
●    Usually caused by missing context.
●    Fix: Add details about audience, constraints, tone, and situation.

2. Responses are too long or too short
●    Claude guesses length unless told otherwise.
●    Fix: Specify word count, number of paragraphs, or “length isn’t a concern.”

3. Claude doesn’t follow your desired format
●    Claude understood what you want, not how you want it.
●    Fix: Provide an example or explicitly describe the structure.

4. Confident but incorrect information
●    Large models can produce plausible but wrong details.
●    Fix: Verify facts, ask for citations, or enable web search for grounding.

5. Tone mismatch
●    Claude defaults to helpful/professional.
●    Fix: Describe the tone (“more conversational,” “authoritative,” etc.) or give a sample.

6. Iteration is essential
●    First drafts are starting points, not final outputs.
●    Fix:
○    Give specific revision instructions
○    Restart the chat when the thread drifts
○    Treat the process as collaborative refinement



🎓 AI Fluency & the 4D Framework
The lesson introduces AI Fluency as the skill of working effectively with AI tools. It highlights the 4D Framework:

Competency    What it Means
Delegation    Deciding what humans vs. AI should do
Description    Communicating clearly with AI (prompts, rules, examples)
Discernment    Evaluating AI outputs critically
Diligence    Using AI responsibly, ethically, transparently
These map directly to the prompting and troubleshooting techniques taught earlier.



🧪 Evaluating Claude for Your Workflows (Evals)
The page encourages lightweight, practical evaluation of Claude’s performance on your real tasks.

Why evals matter
●    Your workflows are unique.
●    Evals help you understand where Claude excels or needs more guidance.

A simple eval method
1.    Gather examples of your real work (5–10 samples).
2.    Write test prompts that mirror those tasks.
3.    Compare outputs to your originals.
4.    Refine prompts or add examples to improve results.

Example: Data analysis
●    Use a dataset you’ve analyzed manually.
●    Ask Claude to analyze it.
●    Compare patterns, accuracy, and reasoning.
●    Adjust prompts accordingly.



🪞 Reflection Questions
The lesson ends with prompts to help you internalize the material:

●    Which challenges have you already experienced?
●    What troubleshooting techniques will you try next?
●    Where could evals help you build confidence?
●    How might the 4D Framework shape your collaboration with Claude?

------------

 **Claude Desktop App: Chat, Cowork, Code**   [anthropic.skilljar.com](https://anthropic.skilljar.com/claude-101/440908).
---

# 🖥️ Claude Desktop App — Key Notes

## 🎯 What this lesson teaches
- The Claude desktop app has **three modes**: **Chat**, **Cowork**, **Code**.
- Each mode is optimized for a different type of work.
- You learn how to choose the right mode and what features are unique to each.

---

# 🔱 The Three Modes

## 💬 1. Chat — Fast, lightweight interaction
**Best for:** questions, brainstorming, drafting, back‑and‑forth problem solving.
**Key features (desktop‑only):**
- **Quick Entry:** Double‑tap Option (Mac) to summon Claude over any app.
- **Screenshots / window sharing:** Show Claude exactly what you see.
- **Dictation (Mac):** Talk instead of type.
- **Desktop connectors:** Let Claude read from local apps (e.g., Notes).

**Use cases:**
- Interpreting dashboards
- Talking through ideas between meetings
- Pulling together scattered notes

---

## 🤝 2. Cowork — Deep research & multi‑step work
**Best for:** complex tasks requiring analysis, synthesis, or multi‑source input.
**Core capabilities:**
- **Multitasking + sub‑agents:** Works on multiple parts of a project in parallel.
- **Folder access:** Reads/writes files in shared folders.
- **Scheduled tasks:** Automate recurring workflows (daily briefings, inbox triage).
- **Browser integration:** Navigate websites, extract data, interact with pages.
- **Plugins:** Extend capabilities (financial data, internal KB search, compliance tools).
- **Protected environment:** Only accesses folders you explicitly share.

**Use cases:**
- Market research, competitor analysis
- Cross‑document review (contracts, reports, transcripts)
- Automated recurring workflows
- Querying all your tools like a unified database

---

## 🧑‍💻 3. Code — Full development environment
**Best for:** writing, modifying, testing, and deploying software.
**Two environments:**
- **Local:** Works directly in your filesystem; can run dev servers.
- **Remote:** Works in a cloud environment tied to a GitHub repo; persists even if you close the app.

**Interaction modes:**
- **Ask:** Claude proposes changes; you approve via visual diffs.
- **Code:** Claude applies file changes automatically; asks before running commands.
- **Plan:** Claude outlines its full strategy before touching anything.

**Other features:**
- Visual diffs
- Built‑in terminal
- Git versioning
- Multiple sessions across projects

---

# 🆚 Quick Comparison Table

| Mode | Optimized For | Key Features |
|------|---------------|--------------|
| **Chat** | Quick exchanges, drafting, Q&A | Quick entry, dictation, screenshots, connectors |
| **Cowork** | Complex/sustained work | Folder access, plugins, scheduled tasks, browser use, sub‑agents |
| **Code** | Software development | Ask/Code/Plan modes, diffs, terminal, git, local/remote environments |

---

# 🪞 Reflection prompts (from the lesson)
- Which mode fits your most common tasks?
- How would Cowork have changed a recent multi‑source project?
- What workflows could you automate with scheduled tasks?

---

# 📁 Claude Projects

## 🎯 What are Claude Projects?
Projects are self-contained workspaces with their own memory, chat histories, knowledge bases, and customized instructions. Think of them as dedicated environments for specific work streams.

## 🔑 Key Features of Projects

### Project Knowledge
Project knowledge enhances Claude's understanding by letting you upload relevant documents that Claude references across all chats within that project. No more re-uploading the same files each time.

### Project Instructions
Project instructions guide Claude's behavior—you can specify tone, expertise level, response style, and more. These instructions apply to every conversation within the project.

### Automatic Scaling with RAG
Projects automatically scale to handle large amounts through a feature called Retrieval Augmented Generation (RAG).

"When your project knowledge approaches the context window limit, Claude seamlessly enables RAG mode. Instead of loading all project content into memory at once, Claude intelligently searches and retrieves only the most relevant information needed to answer your questions. This expands your project's capacity by up to 10x while maintaining response quality."

### Collaboration (Claude for Work)
For Claude for Work users, projects enable collaboration. Share projects with teammates so everyone benefits from the same context, instructions, and accumulated knowledge.

---

# 🛠️ Claude Skills

## 🎯 What are Claude Skills?
Skills are specialized capabilities and domain knowledge that extend Claude's functionality. When users reference a "slash command" or "/<something>" (e.g., "/commit", "/review-pr"), they are referring to a skill.

## 🔧 Types of Skills

### Built-in Skills (User-Invocable)
These skills can be executed directly using the Skill tool:
- **update-config**: Configure the Claude Code harness via settings.json
- **keybindings-help**: Customize keyboard shortcuts and keybindings.json
- **simplify**: Review changed code for reuse, quality, and efficiency
- **loop**: Run prompts or slash commands on recurring intervals
- **schedule**: Create, update, list, or run scheduled remote agents (triggers)
- **claude-api**: Build apps with the Claude API or Anthropic SDK

### Agent Skills (Subagent Types)
These are used with the Agent tool for specialized tasks:
- **general-purpose**: Research complex questions, search for code, execute multi-step tasks
- **Explore**: Fast agent for exploring codebases (quick/medium/very thorough)
- **Plan**: Software architect agent for designing implementation plans
- **statusline-setup**: Configure Claude Code status line settings
- **claude-code-guide**: Answer questions about Claude Code, Agent SDK, or Claude API

## ⚙️ How to Enable and Use Skills

### Using Built-in Skills
Invoke skills using the Skill tool:
```
skill: "skill-name", args: "optional arguments"
```
Examples:
- `skill: "commit", args: "-m 'Fix bug'"`
- `skill: "simplify"` (to review recent changes)
- `skill: "schedule", args: "list"` (to see scheduled triggers)

### Using Agent Skills
Launch specialized agents using the Agent tool:
```
Agent: {
  description: "Task summary",
  prompt: "Detailed task description",
  subagent_type: "explore",
  run_in_background: true
}
```

### Skill Execution Rules
- Skills are blocking requirements: invoke the relevant Skill tool BEFORE generating any other response about the task
- Never mention a skill without actually calling the Skill tool
- Do not invoke a skill that is already running
- Skills require clear, detailed prompts to work autonomously

## 💡 Practical Applications

### Development Workflow
- Use `simplify` skill to review code changes for quality
- Use `schedule` skill to automate recurring tasks (daily checks, deployments)
- Use `claude-api` skill when building applications with Claude API

### Codebase Exploration
- Use Explore agent (`subagent_type: "explore"`) for finding files or patterns
- Use Plan agent (`subagent_type: "plan"`) to design implementation strategies
- Use general-purpose agent for complex research tasks

### Customization
- Use `keybindings-help` to customize keyboard shortcuts
- Use `update-config` to modify settings.json for automated behaviors
- Create custom scheduled agents with the `schedule` skill

## 🪞 Skill-Related Reflection
- Which built-in skills would improve your current workflow?
- How could scheduled skills automate repetitive tasks in your projects?
- When would you use different agent types (Explore vs Plan vs general-purpose)?

---

# 🔌 Claude Connectors

## 🎯 What are Claude Connectors?
Connectors transform Claude from an assistant into an informed collaborator by giving Claude access to the same tools, data, and context that you use every day. Instead of starting every conversation from scratch, Claude can work directly with your actual information.

## 🔑 Key Features of Connectors

### Capabilities
Connectors allow Claude to read information and perform actions on your behalf. Depending on the connector and permissions you grant, Claude can search your files, retrieve documents, analyze data, create new content, update records, and execute tasks across your connected applications—all from within your conversation.

### Model Context Protocol (MCP)
The Model Context Protocol (MCP) powers connectors. Think of MCP like USB-C for AI—a universal standard that allows Claude to connect to many different applications through a single, consistent interface. This open standard means developers can build connectors for any tool, and those connectors work seamlessly with Claude.

### Connector Types
There are two types of connectors:
- **Web connectors**: Link Claude to cloud services like Google Drive, Notion, Slack, and Asana
- **Desktop extensions**: Run locally on your computer through the Claude Desktop app, giving Claude access to local files and native applications

### Finding and Connecting Tools
Anthropic maintains a directory of recommended connectors at claude.ai/directory. The directory is organized into two tabs:
- **Web**: Cloud services and applications (Gmail, Notion, Slack, Asana, Linear, Stripe, and many more)
- **Desktop extensions**: Local tools that run on your computer through the Claude Desktop app

To browse available connectors, you can also click the "Search and tools" button in the lower left of the chat window, then select "Add connectors."

---

# �ina Research Mode

## 🎯 What is Research Mode?
Research transforms how Claude finds and analyzes information, moving beyond simple searches to comprehensive, agentic investigations.

## 🔑 Key Features of Research Mode

### Agentic Research Process
Instead of a single search, Claude operates agentically—conducting multiple searches that build on each other while determining exactly what to investigate next. It explores different angles of your question automatically and works through open questions systematically.

### Time Efficiency
Research delivers comprehensive answers in minutes. Most reports complete in 5 to 15 minutes, though more complex investigations may take up to 45 minutes—work that would typically require hours of manual research.

### Extended Thinking
Extended thinking is automatically enabled with Research. This powerful combination lets Claude both plan its approach thoughtfully and gather comprehensive information, breaking complex requests into manageable pieces.

### Verification & Citations
Citations make verification easy. Research delivers thorough answers complete with easy-to-check citations, so you can trust Claude's findings and quickly verify sources yourself.

---

