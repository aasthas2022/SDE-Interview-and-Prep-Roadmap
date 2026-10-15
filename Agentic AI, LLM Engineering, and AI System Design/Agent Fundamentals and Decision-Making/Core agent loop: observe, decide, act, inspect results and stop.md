# Core Agent Loop: Observe, Decide, Act, Inspect, Stop

## 1. Mental model in 60 seconds

Core Agent Loop: Observe, Decide, Act, Inspect, Stop is best understood as a **system-design choice**, not a magic model feature. The LLM may propose interpretations and actions; the **application** owns permissions, control flow, durability, verified outcomes, and failure behavior. When interviewing, begin with the goal and risk, then show how the architecture enforces boundaries.

### Vocabulary to know

| Term | Meaning |
|---|---|
| **State and observations** | Maintain explicit task state with goal, evidence, actions taken, outstanding questions, and budgets. |
| **Decision stage** | Determine the next action from the current observation and goal, subject to allowed tools. |
| **Tool execution** | Execute validated tool requests with schema checks, authorization, and timeouts. |
| **Inspect results** | Check whether tool output proves progress; distinguish success, partial success, and error. |
| **Explicit stopping** | Stop when success is verified, a refusal is required, human input is needed, or budget expires. |
| **Error handling** | Separate transient failures, permanent failures, and unknown outcomes before deciding on retries. |
| **Idempotency** | Repeating a tool operation should not duplicate a business side effect when retries occur. |
| **Progress detection** | Track meaningful state changes and avoid repeated futile calls. |
| **Structured outputs** | Use typed actions and observations, not ambiguous strings, for control flow. |
| **Observability** | Record step traces, correlation IDs, durations, tokens, tool errors, and final outcome. |

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

### 3.1 State and observations

**What it means.** Maintain explicit task state with goal, evidence, actions taken, outstanding questions, and budgets.

**Concrete example.** A lookup step records that ERP returned no supplier match.

**Common mistake.** Letting conversational prose be the only source of truth.

**How to validate it.** Replay a run from the stored state.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.2 Decision stage

**What it means.** Determine the next action from the current observation and goal, subject to allowed tools.

**Concrete example.** After a product lookup, select validation rather than immediately updating.

**Common mistake.** Selecting actions from stale tool output.

**How to validate it.** Unit test decision branches using fixture observations.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.3 Tool execution

**What it means.** Execute validated tool requests with schema checks, authorization, and timeouts.

**Concrete example.** A read_material tool accepts one well-formed material ID.

**Common mistake.** Passing arbitrary model text into shell commands.

**How to validate it.** Fuzz arguments and assert invalid calls never execute.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.4 Inspect results

**What it means.** Check whether tool output proves progress; distinguish success, partial success, and error.

**Concrete example.** HTTP 200 with zero rows is not evidence that the desired record exists.

**Common mistake.** Treating any successful API response as task completion.

**How to validate it.** Use outcome assertions and business invariants.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.5 Explicit stopping

**What it means.** Stop when success is verified, a refusal is required, human input is needed, or budget expires.

**Concrete example.** Stop after verified mapping validation, not after the tenth identical search.

**Common mistake.** Infinite loops and premature final answers.

**How to validate it.** Simulate no-progress sequences and assert bounded termination.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.6 Error handling

**What it means.** Separate transient failures, permanent failures, and unknown outcomes before deciding on retries.

**Concrete example.** Retry a rate-limited GET with jitter; verify state before repeating a POST.

**Common mistake.** Blindly retrying a non-idempotent payment request.

**How to validate it.** Inject 429, timeout, and partial-write faults.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.7 Idempotency

**What it means.** Repeating a tool operation should not duplicate a business side effect when retries occur.

**Concrete example.** Use an idempotency key for purchase-order creation.

**Common mistake.** Assuming a network timeout means the server did nothing.

**How to validate it.** Call a command twice with the same key and compare results.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.8 Progress detection

**What it means.** Track meaningful state changes and avoid repeated futile calls.

**Concrete example.** Hash normalized retrieval results to detect no-new-information loops.

**Common mistake.** Repeatedly querying an empty index.

**How to validate it.** Test cycle detection and no-progress thresholds.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.9 Structured outputs

**What it means.** Use typed actions and observations, not ambiguous strings, for control flow.

**Concrete example.** Model emits {action: "lookup", material_id: "..."} against a JSON schema.

**Common mistake.** Parsing free-form model explanations with fragile regex.

**How to validate it.** Validate both happy and malformed responses.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.10 Observability

**What it means.** Record step traces, correlation IDs, durations, tokens, tool errors, and final outcome.

**Concrete example.** A trace identifies an approval wait as the latency bottleneck.

**Common mistake.** Keeping only final answers, making failures irreproducible.

**How to validate it.** Reconstruct a sampled production run from its trace.

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

### Q1. What is state and observations, and why does it matter?

**Answer:** Maintain explicit task state with goal, evidence, actions taken, outstanding questions, and budgets. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q2. Give a practical example of state and observations.

**Answer:** A lookup step records that ERP returned no supplier match. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q3. What can go wrong when implementing state and observations?

**Answer:** Letting conversational prose be the only source of truth. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q4. How would you test or measure state and observations?

**Answer:** Replay a run from the stored state. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q5. What is decision stage, and why does it matter?

**Answer:** Determine the next action from the current observation and goal, subject to allowed tools. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q6. Give a practical example of decision stage.

**Answer:** After a product lookup, select validation rather than immediately updating. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q7. What can go wrong when implementing decision stage?

**Answer:** Selecting actions from stale tool output. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q8. How would you test or measure decision stage?

**Answer:** Unit test decision branches using fixture observations. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q9. What is tool execution, and why does it matter?

**Answer:** Execute validated tool requests with schema checks, authorization, and timeouts. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q10. Give a practical example of tool execution.

**Answer:** A read_material tool accepts one well-formed material ID. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q11. What can go wrong when implementing tool execution?

**Answer:** Passing arbitrary model text into shell commands. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q12. How would you test or measure tool execution?

**Answer:** Fuzz arguments and assert invalid calls never execute. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q13. What is inspect results, and why does it matter?

**Answer:** Check whether tool output proves progress; distinguish success, partial success, and error. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q14. Give a practical example of inspect results.

**Answer:** HTTP 200 with zero rows is not evidence that the desired record exists. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q15. What can go wrong when implementing inspect results?

**Answer:** Treating any successful API response as task completion. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q16. How would you test or measure inspect results?

**Answer:** Use outcome assertions and business invariants. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q17. What is explicit stopping, and why does it matter?

**Answer:** Stop when success is verified, a refusal is required, human input is needed, or budget expires. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q18. Give a practical example of explicit stopping.

**Answer:** Stop after verified mapping validation, not after the tenth identical search. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q19. What can go wrong when implementing explicit stopping?

**Answer:** Infinite loops and premature final answers. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q20. How would you test or measure explicit stopping?

**Answer:** Simulate no-progress sequences and assert bounded termination. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q21. What is error handling, and why does it matter?

**Answer:** Separate transient failures, permanent failures, and unknown outcomes before deciding on retries. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q22. Give a practical example of error handling.

**Answer:** Retry a rate-limited GET with jitter; verify state before repeating a POST. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q23. What can go wrong when implementing error handling?

**Answer:** Blindly retrying a non-idempotent payment request. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q24. How would you test or measure error handling?

**Answer:** Inject 429, timeout, and partial-write faults. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q25. What is idempotency, and why does it matter?

**Answer:** Repeating a tool operation should not duplicate a business side effect when retries occur. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q26. Give a practical example of idempotency.

**Answer:** Use an idempotency key for purchase-order creation. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q27. What can go wrong when implementing idempotency?

**Answer:** Assuming a network timeout means the server did nothing. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q28. How would you test or measure idempotency?

**Answer:** Call a command twice with the same key and compare results. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q29. What is progress detection, and why does it matter?

**Answer:** Track meaningful state changes and avoid repeated futile calls. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q30. Give a practical example of progress detection.

**Answer:** Hash normalized retrieval results to detect no-new-information loops. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q31. What can go wrong when implementing progress detection?

**Answer:** Repeatedly querying an empty index. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q32. How would you test or measure progress detection?

**Answer:** Test cycle detection and no-progress thresholds. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q33. What is structured outputs, and why does it matter?

**Answer:** Use typed actions and observations, not ambiguous strings, for control flow. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q34. Give a practical example of structured outputs.

**Answer:** Model emits {action: "lookup", material_id: "..."} against a JSON schema. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q35. What can go wrong when implementing structured outputs?

**Answer:** Parsing free-form model explanations with fragile regex. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q36. How would you test or measure structured outputs?

**Answer:** Validate both happy and malformed responses. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q37. What is observability, and why does it matter?

**Answer:** Record step traces, correlation IDs, durations, tokens, tool errors, and final outcome. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q38. Give a practical example of observability.

**Answer:** A trace identifies an approval wait as the latency bottleneck. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q39. What can go wrong when implementing observability?

**Answer:** Keeping only final answers, making failures irreproducible. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q40. How would you test or measure observability?

**Answer:** Reconstruct a sampled production run from its trace. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

---

**Final self-check:** Can you explain this topic without relying on a framework name? Can you name the control-plane owner, the most serious failure, a safe fallback, and one metric proving it works?
