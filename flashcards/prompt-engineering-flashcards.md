# Prompt Engineering & Structured Output Flashcards

### Front
Why use structured outputs?

### Back
To make the model return reliable machine-readable data that matches a schema. Freeform text has ~20% hallucination rate and breaks automated parsing.

### Front
What makes a prompt precise instead of vague?

### Back
Clear success criteria, specific examples, defined output format, and explicit constraints.

### Front
When should few-shot examples be added?

### Back
When the model consistently misunderstands the format or produces inconsistent outputs. Avoid overloading with too many examples.

### Front
When does retry-with-feedback help extraction?

### Back
When the initial extraction fails, providing specific feedback about what's wrong often leads to correct output on the second attempt.

### Front
What is the anti-pattern of overloading prompts?

### Back
Putting everything in one prompt—context, instructions, examples, constraints. This causes noise and the model loses focus on what matters most.

### Front
Why skip schema design for outputs that need to be parsed?

### Back
Without a schema, you get inconsistent structure. Structured outputs guarantee the format, making downstream automation reliable.
