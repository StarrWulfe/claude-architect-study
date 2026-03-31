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
