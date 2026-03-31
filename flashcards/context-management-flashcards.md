# Context Management & Reliability Flashcards

### Front
What is the lost-in-the-middle effect?

### Back
Information in the middle of long contexts gets less attention than information at the ends. Important details can get overlooked.

### Front
When should the system escalate instead of keep trying?

### Back
After 2-3 failed attempts with different approaches, or when confidence is below threshold. Don't let the agent spin endlessly.

### Front
What facts should always be preserved in long support sessions?

### Back
User identity, the original problem statement, key constraints, and any confirmed facts. These prevent the conversation from drifting.

### Front
Why is self-confidence not enough to judge correctness?

### Back
Large models can produce confident but wrong answers. Always verify facts, ask for citations, or enable web search for grounding.

### Front
When is context summarization better than session resumption?

### Back
When the valuable context is spread throughout and can be condensed into a focused summary that preserves key facts.

### Front
What causes noisy or stale context?

### Back
Including irrelevant details, outdated information, or conversation history that no longer relates to the current task.
