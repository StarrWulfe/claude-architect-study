# Tool Design & MCP Integration Flashcards

### Front
When should you use MCP instead of a skill?

### Back
Use MCP when Claude needs to connect to external services, tools, data, or actions that require the Model Context Protocol.

### Front
What makes an MCP error response useful to an agent?

### Back
Structured error codes, retry hints, and context about what failed so the agent can recover intelligently.

### Front
Why should agents have fewer, more specialized tools?

### Back
Too many tools causes misrouting and increases the chance the agent picks the wrong one. Specialized tools with clear descriptions perform better.

### Front
When should a built-in tool be preferred over a custom integration?

### Back
When the built-in tool already solves the problem reliably. Custom integrations add complexity and maintenance overhead.

### Front
How should a tool description be written to avoid misrouting?

### Back
Be specific about what the tool does, its inputs, and when to use it. Avoid vague names or overlapping functionality with other tools.

### Front
What anti-pattern should you avoid with MCP?

### Back
Using MCP for something that should be a simple skill or prompt. MCP is for external system integration, not every small task.

### Front
When should few-shot examples be used for tool selection?

### Back
Use few-shot examples for ambiguous scenarios where simple descriptions aren't enough. Include 4-6 examples showing reasoning for why one tool was chosen over plausible alternatives.

### Front
Why are few-shot examples more effective than declarative rules for tool selection?

### Back
Worked examples demonstrate the actual decision process in context. Declarative rules ("use when"/"do not use when") are less effective for nuanced edge-case reasoning.

### Front
What is the recommended approach for enforcing tool calling order?

### Back
Add programmatic prerequisites that block downstream tool calls until required upstream tools return verified data. Don't rely on prompt instructions alone.

### Front
How should Claude Code CLI enforce structured output for automated pipelines?

### Back
Use `--output-format json` with `--json-schema` flags to guarantee well-formed JSON at the CLI level, not prompt-based formatting that may be inconsistent.

### Front
What is the principle of least privilege for tool distribution?

### Back
Give agents only the tools they need for their specific task. Replace general-purpose tools with specialized ones that constrain capability at the interface level.

### Front
Why is multi-instance verification more effective than extended thinking for code review?

### Back
A second independent Claude instance without access to the generator's reasoning eliminates confirmation bias. Extended thinking doesn't help when the model has already rationalized its decisions.

### Front
What approach helps Claude Code batch multiple tool requests in a single turn?

### Back
Prompt Claude explicitly to batch related tool requests per turn and return all results together before the next API call. Claude already supports multiple tools per turn.
