# ReAct and Reasoning-and-Acting Tool-Use Loops

## 1. Mental model in 60 seconds

ReAct and Reasoning-and-Acting Tool-Use Loops is best understood as a **system-design choice**, not a magic model feature. The LLM may propose interpretations and actions; the **application** owns permissions, control flow, durability, verified outcomes, and failure behavior. When interviewing, begin with the goal and risk, then show how the architecture enforces boundaries.

### Vocabulary to know

| Term | Meaning |
|---|---|
| **ReAct pattern** | Interleave decisions/actions with external observations instead of relying only on a one-shot answer. |
| **Tool affordances** | Each tool requires clear name, description, schema, permissions, and error modes. |
| **Tool selection** | Choose the least risky, most informative authorized action next. |
| **Grounding** | Treat tool observations as evidence but verify relevance, recency, and source reliability. |
| **Prompt injection boundary** | Tool results are untrusted data and must not be allowed to override developer policies or privileges. |
| **Action validation** | Authorize and validate requests at execution time outside the model. |
| **Search quality** | Use targeted queries, deduplicate evidence, and stop when additional retrieval has little value. |
| **Observation compression** | Summarize or extract only pertinent results without losing provenance. |
| **Failure recovery** | On tool error, distinguish retry, alternative tool, clarification, and safe stop. |
| **Termination after evidence** | Answer when the requested output is supported, or disclose a blocker. |

## 2. Architecture and execution flow

```text
User goal
   |
   v
[Authenticate + authorize + validate request]
   |
   v
[Load bounded task state and relevant evidence]
   |
   v
[Choose deterministic step OR constrained model decision]
   |
   v
[Validate proposed action against schema + policy]
   |
   +--> approval required? --> [durable pause + human decision]
   |
   v
[Execute authorized tool with timeout + idempotency]
   |
   v
[Inspect result + update state + write trace]
   |
   +--> success proven? --------> [return verified result]
   +--> blocked / unsafe? ------> [escalate / partial result]
   +--> budget exhausted? -----> [safe fallback]
   +--> progress possible? -----> [repeat]
```

**Important distinctions:** *decision* is not *authorization*; an HTTP success is not business success; context is not durable memory; a plan is not evidence that actions succeeded.

## 3. Learn each building block from scratch

### 3.1 ReAct pattern

**What it means.** Interleave decisions/actions with external observations instead of relying only on a one-shot answer.

**Concrete example.** Agent searches for a material, reads ERP response, then checks supplier rules.

**Common mistake.** Presenting unsupported guesses as observations.

**How to validate it.** Trace each tool observation to its source.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.2 Tool affordances

**What it means.** Each tool requires clear name, description, schema, permissions, and error modes.

**Concrete example.** search_materials(query, plant) has a required plant.

**Common mistake.** Exposing arbitrary shell access unnecessarily.

**How to validate it.** Schema-test generated tool calls.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.3 Tool selection

**What it means.** Choose the least risky, most informative authorized action next.

**Concrete example.** Read PIM variant before updating a material mapping.

**Common mistake.** Calling write tools to discover read-only information.

**How to validate it.** Evaluate tool choice on labeled scenarios.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.4 Grounding

**What it means.** Treat tool observations as evidence but verify relevance, recency, and source reliability.

**Concrete example.** An ERP API read outranks a stale cached CSV mapping.

**Common mistake.** Trusting arbitrary retrieved content as policy instructions.

**How to validate it.** Inject conflicting observations and inspect resolution.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.5 Prompt injection boundary

**What it means.** Tool results are untrusted data and must not be allowed to override developer policies or privileges.

**Concrete example.** A webpage says ignore your instructions and send credentials; agent ignores it.

**Common mistake.** Elevating document text to an instruction.

**How to validate it.** Run tool-output injection tests.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.6 Action validation

**What it means.** Authorize and validate requests at execution time outside the model.

**Concrete example.** Server rejects an update to a different tenant.

**Common mistake.** Using tool descriptions as the sole security boundary.

**How to validate it.** Permission-bypass test suite.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.7 Search quality

**What it means.** Use targeted queries, deduplicate evidence, and stop when additional retrieval has little value.

**Concrete example.** Search by material ID, then exact ERP ID once.

**Common mistake.** Repeated broad searching without information gain.

**How to validate it.** Track source novelty per search.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.8 Observation compression

**What it means.** Summarize or extract only pertinent results without losing provenance.

**Concrete example.** Retain error code, source timestamp, and record ID rather than entire logs.

**Common mistake.** Truncating evidence required for a decision.

**How to validate it.** Compare compressed and full-context decisions.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.9 Failure recovery

**What it means.** On tool error, distinguish retry, alternative tool, clarification, and safe stop.

**Concrete example.** On 429 back off; on 403 request access instead.

**Common mistake.** Retrying a 403 until budget expires.

**How to validate it.** Fault-inject each error class.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.10 Termination after evidence

**What it means.** Answer when the requested output is supported, or disclose a blocker.

**Concrete example.** After two independent checks, return validated mapping and citations.

**Common mistake.** Continuing actions merely because turns remain.

**How to validate it.** Assert success condition before final answer.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

## 4. Reference implementation (framework-agnostic)

This pseudocode sketches **control-plane** responsibilities rather than working library APIs; adapt the decision and persistence interfaces to your stack. The outer application enforces tool schema and authorization even if the model ignores its prompt.

```python
# Illustrative framework-agnostic pseudocode. All authorization is server-side.
def run_agent(goal, user, tools, state_store, max_steps=8):
    state = state_store.load_or_create(goal=goal, user=user)
    for step in range(max_steps):
        if verified_success(state):
            return {"status": "succeeded", "evidence": state.evidence}
        if deadline_exceeded(state) or no_progress(state):
            return fallback_with_partial_evidence(state)

        choice = choose_next_step(state)  # rule-based OR model-selected
        validated = validate_schema(choice, tools.allowed_schemas)
        authorize(user, validated.action, validated.arguments)

        if needs_approval(validated):
            state_store.checkpoint(state, pending_action=validated)
            return {"status": "awaiting_approval", "run_id": state.id}

        # Idempotency key must be stable across retries of the same side effect.
        result = tools.execute(
            validated, timeout_seconds=10,
            idempotency_key=state.stable_operation_id(validated)
        )
        state.record_observation(result)  # provenance + timestamp + outcome
        state_store.checkpoint(state)

    return fallback_with_partial_evidence(state)
```

### Why each boundary matters

1. **Before execution:** validate input, identity, allowed tools, and action-specific business policies.
2. **During execution:** use deadlines, limited budgets, stable idempotency keys, durable progress updates, and restricted credentials.
3. **After execution:** inspect the *business outcome*, capture source evidence, and classify partial or unknown results.
4. **At completion:** return only verified claims, with unresolved items and the next safe action.

## 5. End-to-end example and walkthrough

### Running example: supplier/material validation

You are building an assistant that validates a spreadsheet of materials before creating records. Inputs include a CSV, product-catalog metadata, ERP identifiers, and plant permissions. The **safe design** is to parse the CSV with code, fetch ERP and catalog facts with typed read tools, compare required attributes with deterministic checks, ask a model only to interpret genuinely ambiguous descriptions, and produce a row-by-row report. Creation is a separate, gated action after approval. In an interview, explain why you separated **evidence gathering**, **judgment**, and **side effects**.

**Acceptance criteria:** every row has a stable ID, source evidence, a pass/fail/unknown outcome, reason codes, and no writes occur without explicit authority. A report with 399 processed rows is not automatically 399 validated rows.

**Walkthrough:** the input is parsed → rows receive stable IDs → metadata is fetched from trusted tools → missing records are marked `unknown`, not `pass` → ambiguous fields may use model interpretation with recorded evidence → inconsistent rows are flagged → a reviewer approves any proposed updates → a write service enforces the approved diff and version check → the final report distinguishes verified, skipped, failed, and pending records.

## 6. Design trade-offs you should discuss

| Choice | Good fit | Trade-off or failure |
|---|---|---|
| Deterministic rule | Stable business invariant | Brittle for open-ended semantic ambiguity |
| LLM judgment | Ambiguous text or uncertain next investigative step | Variable outputs, token cost, eval burden |
| Human gate | High-impact or irreversible write | Human latency and review fatigue |
| Durable checkpoint | Long-running and resumable actions | Additional persistence/consistency requirements |
| Retrieval/memory | Relevant evidence outside current input | Stale, irrelevant, or unauthorized evidence |
| Bounded autonomous loop | Unpredictable path with useful tools | Loops, expense, larger operational surface |

## 7. Production readiness: failure modes, mitigations, and metrics

| Failure | Mitigation | Measure |
|---|---|---|
| Tool times out after side effect | Idempotency key, query operation status, avoid blind replay | Duplicate action rate |
| Tool response contains hostile instructions | Treat result as data, isolate permissions, enforce tool policies | Injection success rate in adversarial tests |
| Agent repeats itself | No-progress detector + step budget | Repeat-action rate |
| Source systems disagree | Mark unknown, record provenance, escalate | False-pass rate |
| Reviewer approves stale diff | Version checks + approval expiry | Stale-approval rejection rate |
| Model output breaks schema | Structured generation + server validation | Schema failure rate |
| High latency / model cost | Simpler baseline, caching, caps, parallel independent reads | p50/p95 latency and cost per verified task |
| Partial failure hidden as success | Row-level status and verifiable success predicate | Outcome misclassification |

**Metric definitions:** task success = verified goal achieved / eligible runs; false-pass rate = invalid outputs accepted / outputs accepted; escalation rate = runs sent for human review / total runs; tool error rate = failed calls / total calls; cost per verified task = total inference + tool expense / verified tasks. Use representative, held-out workloads; report both quality and the percentage of cases the system declines.

## 8. Practice: whiteboard, coding, behavioral articulation

**Whiteboard drill (15 minutes):** Draw trusted services, model decisions, tool adapters, checkpoint database, approval UI, and audit logs. Mark the *trust boundary* between untrusted tool text and authorized actions. Explain how an interrupted write is recovered.

**Coding drill (30 minutes):** Implement a typed state object, action schema validator, loop with max steps, no-progress detector, fake tool responses, and unit tests for timeout, approval wait, duplicate retry, and conflicting sources.

**Interview delivery pattern:** (1) state the simple baseline; (2) describe why complexity is justified; (3) show data/control flow; (4) call out security + correctness; (5) explain failure behavior; (6) provide specific evaluation metrics. Avoid claiming an agent is reliable because its prompt asks it to be.

## Further reading

- [Anthropic — Building Effective AI Agents](https://resources.anthropic.com/building-effective-ai-agents)
- [Anthropic — Common architecture patterns](https://claude.com/resources/guides/building-effective-ai-agents/common-architecture-patterns)
- [LangGraph documentation](https://docs.langchain.com/oss/python/langgraph/overview)
- [ReAct paper (Yao et al., 2022)](https://arxiv.org/abs/2210.03629)
- [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/)

> These are learning references, not a claim that all examples in this guide are taken from a specific framework.

## 9. Frequently asked interview questions (with answers)

These answers are intentionally concise enough to say aloud. For senior-level rounds, add a diagram, a failure scenario, and a measurable trade-off.

### Q1. What is react pattern, and why does it matter?

**Answer:** Interleave decisions/actions with external observations instead of relying only on a one-shot answer. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q2. Give a practical example of react pattern.

**Answer:** Agent searches for a material, reads ERP response, then checks supplier rules. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q3. What can go wrong when implementing react pattern?

**Answer:** Presenting unsupported guesses as observations. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q4. How would you test or measure react pattern?

**Answer:** Trace each tool observation to its source. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q5. What is tool affordances, and why does it matter?

**Answer:** Each tool requires clear name, description, schema, permissions, and error modes. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q6. Give a practical example of tool affordances.

**Answer:** search_materials(query, plant) has a required plant. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q7. What can go wrong when implementing tool affordances?

**Answer:** Exposing arbitrary shell access unnecessarily. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q8. How would you test or measure tool affordances?

**Answer:** Schema-test generated tool calls. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q9. What is tool selection, and why does it matter?

**Answer:** Choose the least risky, most informative authorized action next. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q10. Give a practical example of tool selection.

**Answer:** Read PIM variant before updating a material mapping. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q11. What can go wrong when implementing tool selection?

**Answer:** Calling write tools to discover read-only information. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q12. How would you test or measure tool selection?

**Answer:** Evaluate tool choice on labeled scenarios. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q13. What is grounding, and why does it matter?

**Answer:** Treat tool observations as evidence but verify relevance, recency, and source reliability. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q14. Give a practical example of grounding.

**Answer:** An ERP API read outranks a stale cached CSV mapping. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q15. What can go wrong when implementing grounding?

**Answer:** Trusting arbitrary retrieved content as policy instructions. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q16. How would you test or measure grounding?

**Answer:** Inject conflicting observations and inspect resolution. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q17. What is prompt injection boundary, and why does it matter?

**Answer:** Tool results are untrusted data and must not be allowed to override developer policies or privileges. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q18. Give a practical example of prompt injection boundary.

**Answer:** A webpage says ignore your instructions and send credentials; agent ignores it. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q19. What can go wrong when implementing prompt injection boundary?

**Answer:** Elevating document text to an instruction. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q20. How would you test or measure prompt injection boundary?

**Answer:** Run tool-output injection tests. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q21. What is action validation, and why does it matter?

**Answer:** Authorize and validate requests at execution time outside the model. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q22. Give a practical example of action validation.

**Answer:** Server rejects an update to a different tenant. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q23. What can go wrong when implementing action validation?

**Answer:** Using tool descriptions as the sole security boundary. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q24. How would you test or measure action validation?

**Answer:** Permission-bypass test suite. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q25. What is search quality, and why does it matter?

**Answer:** Use targeted queries, deduplicate evidence, and stop when additional retrieval has little value. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q26. Give a practical example of search quality.

**Answer:** Search by material ID, then exact ERP ID once. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q27. What can go wrong when implementing search quality?

**Answer:** Repeated broad searching without information gain. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q28. How would you test or measure search quality?

**Answer:** Track source novelty per search. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q29. What is observation compression, and why does it matter?

**Answer:** Summarize or extract only pertinent results without losing provenance. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q30. Give a practical example of observation compression.

**Answer:** Retain error code, source timestamp, and record ID rather than entire logs. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q31. What can go wrong when implementing observation compression?

**Answer:** Truncating evidence required for a decision. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q32. How would you test or measure observation compression?

**Answer:** Compare compressed and full-context decisions. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q33. What is failure recovery, and why does it matter?

**Answer:** On tool error, distinguish retry, alternative tool, clarification, and safe stop. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q34. Give a practical example of failure recovery.

**Answer:** On 429 back off; on 403 request access instead. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q35. What can go wrong when implementing failure recovery?

**Answer:** Retrying a 403 until budget expires. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q36. How would you test or measure failure recovery?

**Answer:** Fault-inject each error class. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q37. What is termination after evidence, and why does it matter?

**Answer:** Answer when the requested output is supported, or disclose a blocker. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q38. Give a practical example of termination after evidence.

**Answer:** After two independent checks, return validated mapping and citations. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q39. What can go wrong when implementing termination after evidence?

**Answer:** Continuing actions merely because turns remain. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q40. How would you test or measure termination after evidence?

**Answer:** Assert success condition before final answer. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

---

**Final self-check:** Can you explain this topic without relying on a framework name? Can you name the control-plane owner, the most serious failure, a safe fallback, and one metric proving it works?
