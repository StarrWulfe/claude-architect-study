# Agentic Architecture & Orchestration Flashcards

### Front
What is the agentic loop?

### Back
The core cycle where the model iterates between `tool_use` (continue) and `end_turn` (stop), appending tool results to history for reasoning.

### Front
When should you use a hub-and-spoke coordinator pattern?

### Back
For complex delegation tasks where you need observability and error handling. The tradeoff is it creates a single failure point.

### Front
What is the key difference between subagents and prompts?

### Back
Subagents isolate work in a separate context so the main conversation stays focused. Subagents need explicit context passed to them—they don't inherit automatically.

### Front
Why avoid arbitrary loop caps (e.g., 10 iterations)?

### Back
It misses dynamic needs. Use `end_turn` + hooks instead for more reliable termination.

### Front
When is prompt chaining better than dynamic decomposition?

### Back
Prompt chaining is simpler and more deterministic for predictable sequential steps. Use when you know the exact order of operations.

### Front
What problem do hooks solve that prompts cannot?

### Back
Hooks provide guaranteed enforcement. A prompt can be ignored, but hooks run deterministic automation outside the model loop (e.g., blocking >$500 refunds).

### Front
When should a coordinator invoke subagents instead of doing everything itself?

### Back
When the task can be parallelized, requires specialized context, or would bloat the main conversation with irrelevant details.
