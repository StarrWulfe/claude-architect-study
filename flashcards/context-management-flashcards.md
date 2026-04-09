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

### Front
How should transactional facts be preserved in long support sessions?

### Back
Extract transactional facts (amounts, dates, order numbers) into a persistent "case facts" block included in each prompt, outside the summarized history.

### Front
What is the evaluator-optimizer pattern for response quality?

### Back
Add a self-critique step where the agent evaluates its draft response for completeness—ensuring it addresses the customer's concern, includes relevant context, and anticipates follow-up questions.

### Front
How do you mitigate the lost-in-the-middle effect in aggregated subagent outputs?

### Back
Place key findings summary at the beginning (primacy effect) and organize detailed results with explicit section headers for easier navigation.

### Front
What is the correct approach for handling conflicting sources in multi-agent systems?

### Back
Complete the analysis with both figures included, explicitly annotate the conflict with source attribution, and let the coordinator decide how to reconcile before synthesis.

### Front
When should a multi-agent system escalate to human judgment?

### Back
Escalate when there is a genuine policy gap—where company guidelines are silent on the specific situation and the agent cannot fabricate a policy.

### Front
What approach addresses multi-concern message decomposition without extra model calls?

### Back
Add few-shot examples demonstrating correct reasoning and tool sequencing for multi-concern requests. The agent already handles single concerns well at 94%.
