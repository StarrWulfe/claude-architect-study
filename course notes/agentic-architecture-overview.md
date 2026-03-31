# Agentic Architecture Overview

**Agentic Architecture** (Domain 1, 27%) covers designing reliable agent loops, multi-agent orchestration, hooks, and workflows for production autonomy. Questions emphasize tradeoffs like deterministic hooks vs prompts. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_6f3f62d1-8a3e-4e91-97d2-e725079adfb5/3dedf7f4-d23a-40ab-b464-053bf3df58b4/Claude-Certified-Architect-Foundations-Certification-Exam-Guide.pdf)

## Core Concepts

- Agentic loop: Iterate on `tool_use` (continue) vs `end_turn` (stop); append tool results to history for reasoning. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_6f3f62d1-8a3e-4e91-97d2-e725079adfb5/3dedf7f4-d23a-40ab-b464-053bf3df58b4/Claude-Certified-Architect-Foundations-Certification-Exam-Guide.pdf)
- Multi-agent: Coordinator delegates via Task tool; subagents get explicit context (no auto-inherit). [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_6f3f62d1-8a3e-4e91-97d2-e725079adfb5/3dedf7f4-d23a-40ab-b464-053bf3df58b4/Claude-Certified-Architect-Foundations-Certification-Exam-Guide.pdf)
- Hooks: Intercept calls (e.g., block high refunds) or normalize results (e.g., timestamps). [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_6f3f62d1-8a3e-4e91-97d2-e725079adfb5/3dedf7f4-d23a-40ab-b464-053bf3df58b4/Claude-Certified-Architect-Foundations-Certification-Exam-Guide.pdf)

## Key Tradeoffs

| Pattern | Pro | Con | Use When |
|---------|-----|-----|----------|
| Hub-and-spoke coordinator | Observability, error handling | Single failure point | Complex delegation  [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_6f3f62d1-8a3e-4e91-97d2-e725079adfb5/3dedf7f4-d23a-40ab-b464-053bf3df58b4/Claude-Certified-Architect-Foundations-Certification-Exam-Guide.pdf) |
| Prompt chaining | Simple seq | Non-deterministic | Predictable steps  [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_6f3f62d1-8a3e-4e91-97d2-e725079adfb5/3dedf7f4-d23a-40ab-b464-053bf3df58b4/Claude-Certified-Architect-Foundations-Certification-Exam-Guide.pdf) |
| Hooks | Guaranteed | Code overhead | Compliance rules  [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_6f3f62d1-8a3e-4e91-97d2-e725079adfb5/3dedf7f4-d23a-40ab-b464-053bf3df58b4/Claude-Certified-Architect-Foundations-Certification-Exam-Guide.pdf) |

## Production Example

**Customer support (Scenario 1):** Coordinator decomposes query ("billing dispute + return"), parallel-subagents call `getcustomer`/`lookuporder`, aggregate for refund. Hooks block >$500. Achieves 80% first-contact resolution. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_6f3f62d1-8a3e-4e91-97d2-e725079adfb5/3dedf7f4-d23a-40ab-b464-053bf3df58b4/Claude-Certified-Architect-Foundations-Certification-Exam-Guide.pdf)

**Anti-Pattern:** Arbitrary loop caps (e.g., 10 iters)—misses dynamic needs; parse NL for "done" (unreliable ~20% hallucination). Use `end_turn` + hooks. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_6f3f62d1-8a3e-4e91-97d2-e725079adfb5/3dedf7f4-d23a-40ab-b464-053bf3df58b4/Claude-Certified-Architect-Foundations-Certification-Exam-Guide.pdf)

## Practice Quiz

**Scenario:** Research system; coordinator delegates web/search subagent, but it inherits full history, bloating context.

**Question:** Fix invocation?  
A. Auto-inherit via SDK.  
B. Pass explicit structured summary in Task prompt.  
C. Resume shared session.  
D. Global memory file.  

**Answer: B** Subagents need explicit context; summaries preserve key facts/metadata without dilution. A/C/D leak irrelevant history. [ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_6f3f62d1-8a3e-4e91-97d2-e725079adfb5/3dedf7f4-d23a-40ab-b464-053bf3df58b4/Claude-Certified-Architect-Foundations-Certification-Exam-Guide.pdf)
