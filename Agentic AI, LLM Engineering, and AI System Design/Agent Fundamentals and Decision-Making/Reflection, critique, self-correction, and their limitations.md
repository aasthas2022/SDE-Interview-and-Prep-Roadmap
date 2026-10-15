# Reflection, Critique, Self-Correction, and Limitations

## 1. Mental model in 60 seconds

Reflection, Critique, Self-Correction, and Limitations is best understood as a **system-design choice**, not a magic model feature. The LLM may propose interpretations and actions; the **application** owns permissions, control flow, durability, verified outcomes, and failure behavior. When interviewing, begin with the goal and risk, then show how the architecture enforces boundaries.

### Vocabulary to know

| Term | Meaning |
|---|---|
| **Reflection definition** | A model reviews an intermediate answer or plan and proposes improvements. |
| **Independent evaluator** | Use a distinct rubric, tool, or model to check output rather than unstructured self-praise. |
| **Critique rubric** | Define concrete criteria such as correctness, completeness, groundedness, constraints, and security. |
| **External feedback** | Prefer executable tests, source checks, and user feedback over self-critique. |
| **Bounded correction** | Limit revision attempts and stop when no measurable progress occurs. |
| **Error amplification** | A critic sharing the same misconceptions may confidently reinforce an error. |
| **Regression checking** | A revision can fix one aspect while breaking another. |
| **When not to reflect** | For simple, deterministic tasks, an extra critique call adds latency and cost without value. |
| **Evaluator gaming** | If the generator optimizes against a flawed grader, scores can rise while real quality falls. |
| **Decision record** | Retain what was changed, why, and which test justified accepting the revision. |

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

### 3.1 Reflection definition

**What it means.** A model reviews an intermediate answer or plan and proposes improvements.

**Concrete example.** A drafting agent notices its response omitted a required field.

**Common mistake.** Assuming reflection necessarily improves factual accuracy.

**How to validate it.** Compare with an objective validation set.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.2 Independent evaluator

**What it means.** Use a distinct rubric, tool, or model to check output rather than unstructured self-praise.

**Concrete example.** SQL parser validates a generated query.

**Common mistake.** Trusting model saying looks correct.

**How to validate it.** Measure evaluator precision and recall.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.3 Critique rubric

**What it means.** Define concrete criteria such as correctness, completeness, groundedness, constraints, and security.

**Concrete example.** Require every material validation row to include source evidence.

**Common mistake.** Generic instruction to improve your answer.

**How to validate it.** Score on labeled rubric items.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.4 External feedback

**What it means.** Prefer executable tests, source checks, and user feedback over self-critique.

**Concrete example.** Run a generated SQL query in read-only staging.

**Common mistake.** Confusing fluent explanation with verified execution.

**How to validate it.** Measure factual error before and after external feedback.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.5 Bounded correction

**What it means.** Limit revision attempts and stop when no measurable progress occurs.

**Concrete example.** Allow at most two repairs to a malformed JSON payload.

**Common mistake.** Infinite critique-rewrite loops.

**How to validate it.** Inject unsatisfiable constraints and assert exit.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.6 Error amplification

**What it means.** A critic sharing the same misconceptions may confidently reinforce an error.

**Concrete example.** Two prompts hallucinate the same nonexistent API property.

**Common mistake.** Treating repeated agreement as independent proof.

**How to validate it.** Use disjoint data, tools, or human labels.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.7 Regression checking

**What it means.** A revision can fix one aspect while breaking another.

**Concrete example.** A code patch fixes a test but violates authorization.

**Common mistake.** Accepting a patch without rerunning the entire suite.

**How to validate it.** Run full invariant and regression tests.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.8 When not to reflect

**What it means.** For simple, deterministic tasks, an extra critique call adds latency and cost without value.

**Concrete example.** No LLM critique needed for a regex format check.

**Common mistake.** Applying expensive reflection to all requests.

**How to validate it.** Measure net benefit by task category.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.9 Evaluator gaming

**What it means.** If the generator optimizes against a flawed grader, scores can rise while real quality falls.

**Concrete example.** Answers learn to mention keywords rather than solve problems.

**Common mistake.** Using only model-graded scores.

**How to validate it.** Hold out human-reviewed cases.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.10 Decision record

**What it means.** Retain what was changed, why, and which test justified accepting the revision.

**Concrete example.** Trace shows original output, failed constraint, corrected result.

**Common mistake.** Deleting failed attempts from audit history.

**How to validate it.** Audit an end-to-end correction trace.

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

### Q1. What is reflection definition, and why does it matter?

**Answer:** A model reviews an intermediate answer or plan and proposes improvements. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q2. Give a practical example of reflection definition.

**Answer:** A drafting agent notices its response omitted a required field. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q3. What can go wrong when implementing reflection definition?

**Answer:** Assuming reflection necessarily improves factual accuracy. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q4. How would you test or measure reflection definition?

**Answer:** Compare with an objective validation set. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q5. What is independent evaluator, and why does it matter?

**Answer:** Use a distinct rubric, tool, or model to check output rather than unstructured self-praise. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q6. Give a practical example of independent evaluator.

**Answer:** SQL parser validates a generated query. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q7. What can go wrong when implementing independent evaluator?

**Answer:** Trusting model saying looks correct. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q8. How would you test or measure independent evaluator?

**Answer:** Measure evaluator precision and recall. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q9. What is critique rubric, and why does it matter?

**Answer:** Define concrete criteria such as correctness, completeness, groundedness, constraints, and security. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q10. Give a practical example of critique rubric.

**Answer:** Require every material validation row to include source evidence. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q11. What can go wrong when implementing critique rubric?

**Answer:** Generic instruction to improve your answer. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q12. How would you test or measure critique rubric?

**Answer:** Score on labeled rubric items. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q13. What is external feedback, and why does it matter?

**Answer:** Prefer executable tests, source checks, and user feedback over self-critique. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q14. Give a practical example of external feedback.

**Answer:** Run a generated SQL query in read-only staging. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q15. What can go wrong when implementing external feedback?

**Answer:** Confusing fluent explanation with verified execution. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q16. How would you test or measure external feedback?

**Answer:** Measure factual error before and after external feedback. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q17. What is bounded correction, and why does it matter?

**Answer:** Limit revision attempts and stop when no measurable progress occurs. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q18. Give a practical example of bounded correction.

**Answer:** Allow at most two repairs to a malformed JSON payload. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q19. What can go wrong when implementing bounded correction?

**Answer:** Infinite critique-rewrite loops. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q20. How would you test or measure bounded correction?

**Answer:** Inject unsatisfiable constraints and assert exit. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q21. What is error amplification, and why does it matter?

**Answer:** A critic sharing the same misconceptions may confidently reinforce an error. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q22. Give a practical example of error amplification.

**Answer:** Two prompts hallucinate the same nonexistent API property. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q23. What can go wrong when implementing error amplification?

**Answer:** Treating repeated agreement as independent proof. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q24. How would you test or measure error amplification?

**Answer:** Use disjoint data, tools, or human labels. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q25. What is regression checking, and why does it matter?

**Answer:** A revision can fix one aspect while breaking another. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q26. Give a practical example of regression checking.

**Answer:** A code patch fixes a test but violates authorization. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q27. What can go wrong when implementing regression checking?

**Answer:** Accepting a patch without rerunning the entire suite. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q28. How would you test or measure regression checking?

**Answer:** Run full invariant and regression tests. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q29. What is when not to reflect, and why does it matter?

**Answer:** For simple, deterministic tasks, an extra critique call adds latency and cost without value. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q30. Give a practical example of when not to reflect.

**Answer:** No LLM critique needed for a regex format check. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q31. What can go wrong when implementing when not to reflect?

**Answer:** Applying expensive reflection to all requests. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q32. How would you test or measure when not to reflect?

**Answer:** Measure net benefit by task category. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q33. What is evaluator gaming, and why does it matter?

**Answer:** If the generator optimizes against a flawed grader, scores can rise while real quality falls. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q34. Give a practical example of evaluator gaming.

**Answer:** Answers learn to mention keywords rather than solve problems. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q35. What can go wrong when implementing evaluator gaming?

**Answer:** Using only model-graded scores. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q36. How would you test or measure evaluator gaming?

**Answer:** Hold out human-reviewed cases. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q37. What is decision record, and why does it matter?

**Answer:** Retain what was changed, why, and which test justified accepting the revision. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q38. Give a practical example of decision record.

**Answer:** Trace shows original output, failed constraint, corrected result. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q39. What can go wrong when implementing decision record?

**Answer:** Deleting failed attempts from audit history. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q40. How would you test or measure decision record?

**Answer:** Audit an end-to-end correction trace. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

---

**Final self-check:** Can you explain this topic without relying on a framework name? Can you name the control-plane owner, the most serious failure, a safe fallback, and one metric proving it works?
