# Stop Conditions, Turn Budgets, Iteration Limits, and Fallback Paths

## 1. Mental model in 60 seconds

Stop Conditions, Turn Budgets, Iteration Limits, and Fallback Paths is best understood as a **system-design choice**, not a magic model feature. The LLM may propose interpretations and actions; the **application** owns permissions, control flow, durability, verified outcomes, and failure behavior. When interviewing, begin with the goal and risk, then show how the architecture enforces boundaries.

### Vocabulary to know

| Term | Meaning |
|---|---|
| **Success criteria** | Define independently verifiable completion conditions before running an agent. |
| **Turn budget** | Cap the number of model decision cycles to guarantee bounded execution. |
| **Tool budget** | Limit tool calls or quota consumption per run and sometimes per tool. |
| **Time budget** | Apply hard wall-clock deadlines and individual tool timeouts. |
| **Cost budget** | Cap expected model/API spending and adapt strategy near the limit. |
| **No-progress stopping** | End or change strategy if state/evidence stops improving. |
| **Risk stop** | Immediately stop on policy violations, unusual permissions, suspected injection, or dangerous ambiguity. |
| **Fallback ladder** | Define alternatives such as cached results, simpler workflow, human review, or partial output. |
| **Cancellation and cleanup** | Propagate cancellation to tools and release locks/resources safely. |
| **Final status taxonomy** | Report succeeded, partially completed, awaiting approval, blocked, failed, or cancelled with evidence. |

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

### 3.1 Success criteria

**What it means.** Define independently verifiable completion conditions before running an agent.

**Concrete example.** Task succeeds only when ERP and material mapping agree.

**Common mistake.** Stopping because model says done.

**How to validate it.** Evaluate business invariant on final state.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.2 Turn budget

**What it means.** Cap the number of model decision cycles to guarantee bounded execution.

**Concrete example.** Maximum eight decision steps for a diagnostic agent.

**Common mistake.** Using unlimited recursion for a low-value request.

**How to validate it.** Test adversarial no-progress inputs.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.3 Tool budget

**What it means.** Limit tool calls or quota consumption per run and sometimes per tool.

**Concrete example.** Maximum ten external searches and two writes.

**Common mistake.** One failed task exhausting shared API quota.

**How to validate it.** Simulate repeated 429 and budget exhaustion.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.4 Time budget

**What it means.** Apply hard wall-clock deadlines and individual tool timeouts.

**Concrete example.** Support request has a 20-second request deadline.

**Common mistake.** Having a turn cap but no hung-tool timeout.

**How to validate it.** Delay tool responses and assert termination.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.5 Cost budget

**What it means.** Cap expected model/API spending and adapt strategy near the limit.

**Concrete example.** Switch from large model to concise report after budget reached, without new risky actions.

**Common mistake.** Unexpected cost from repeated long-context calls.

**How to validate it.** Track billed usage per run.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.6 No-progress stopping

**What it means.** End or change strategy if state/evidence stops improving.

**Concrete example.** Three identical search results trigger an abstention.

**Common mistake.** Repeating the same query until loop limit.

**How to validate it.** Inject cyclical tool responses.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.7 Risk stop

**What it means.** Immediately stop on policy violations, unusual permissions, suspected injection, or dangerous ambiguity.

**Concrete example.** An unexpected instruction to exfiltrate records ends the run.

**Common mistake.** Treating security errors as transient failures.

**How to validate it.** Run adversarial policy tests.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.8 Fallback ladder

**What it means.** Define alternatives such as cached results, simpler workflow, human review, or partial output.

**Concrete example.** If ERP API is down, produce validation report flagged unverified.

**Common mistake.** Inventing missing ERP confirmation.

**How to validate it.** Simulate upstream outages.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.9 Cancellation and cleanup

**What it means.** Propagate cancellation to tools and release locks/resources safely.

**Concrete example.** Cancel pending external calls and clear a temporary reservation.

**Common mistake.** Leaving orphaned jobs after user cancel.

**How to validate it.** Test cancellation during each stage.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.10 Final status taxonomy

**What it means.** Report succeeded, partially completed, awaiting approval, blocked, failed, or cancelled with evidence.

**Concrete example.** Job report lists 399 rows, 231 not verified, and reason codes.

**Common mistake.** Collapsing every outcome into success/failure.

**How to validate it.** Validate outcome statuses against trace data.

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

### Q1. What is success criteria, and why does it matter?

**Answer:** Define independently verifiable completion conditions before running an agent. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q2. Give a practical example of success criteria.

**Answer:** Task succeeds only when ERP and material mapping agree. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q3. What can go wrong when implementing success criteria?

**Answer:** Stopping because model says done. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q4. How would you test or measure success criteria?

**Answer:** Evaluate business invariant on final state. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q5. What is turn budget, and why does it matter?

**Answer:** Cap the number of model decision cycles to guarantee bounded execution. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q6. Give a practical example of turn budget.

**Answer:** Maximum eight decision steps for a diagnostic agent. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q7. What can go wrong when implementing turn budget?

**Answer:** Using unlimited recursion for a low-value request. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q8. How would you test or measure turn budget?

**Answer:** Test adversarial no-progress inputs. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q9. What is tool budget, and why does it matter?

**Answer:** Limit tool calls or quota consumption per run and sometimes per tool. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q10. Give a practical example of tool budget.

**Answer:** Maximum ten external searches and two writes. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q11. What can go wrong when implementing tool budget?

**Answer:** One failed task exhausting shared API quota. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q12. How would you test or measure tool budget?

**Answer:** Simulate repeated 429 and budget exhaustion. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q13. What is time budget, and why does it matter?

**Answer:** Apply hard wall-clock deadlines and individual tool timeouts. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q14. Give a practical example of time budget.

**Answer:** Support request has a 20-second request deadline. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q15. What can go wrong when implementing time budget?

**Answer:** Having a turn cap but no hung-tool timeout. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q16. How would you test or measure time budget?

**Answer:** Delay tool responses and assert termination. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q17. What is cost budget, and why does it matter?

**Answer:** Cap expected model/API spending and adapt strategy near the limit. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q18. Give a practical example of cost budget.

**Answer:** Switch from large model to concise report after budget reached, without new risky actions. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q19. What can go wrong when implementing cost budget?

**Answer:** Unexpected cost from repeated long-context calls. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q20. How would you test or measure cost budget?

**Answer:** Track billed usage per run. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q21. What is no-progress stopping, and why does it matter?

**Answer:** End or change strategy if state/evidence stops improving. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q22. Give a practical example of no-progress stopping.

**Answer:** Three identical search results trigger an abstention. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q23. What can go wrong when implementing no-progress stopping?

**Answer:** Repeating the same query until loop limit. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q24. How would you test or measure no-progress stopping?

**Answer:** Inject cyclical tool responses. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q25. What is risk stop, and why does it matter?

**Answer:** Immediately stop on policy violations, unusual permissions, suspected injection, or dangerous ambiguity. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q26. Give a practical example of risk stop.

**Answer:** An unexpected instruction to exfiltrate records ends the run. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q27. What can go wrong when implementing risk stop?

**Answer:** Treating security errors as transient failures. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q28. How would you test or measure risk stop?

**Answer:** Run adversarial policy tests. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q29. What is fallback ladder, and why does it matter?

**Answer:** Define alternatives such as cached results, simpler workflow, human review, or partial output. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q30. Give a practical example of fallback ladder.

**Answer:** If ERP API is down, produce validation report flagged unverified. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q31. What can go wrong when implementing fallback ladder?

**Answer:** Inventing missing ERP confirmation. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q32. How would you test or measure fallback ladder?

**Answer:** Simulate upstream outages. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q33. What is cancellation and cleanup, and why does it matter?

**Answer:** Propagate cancellation to tools and release locks/resources safely. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q34. Give a practical example of cancellation and cleanup.

**Answer:** Cancel pending external calls and clear a temporary reservation. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q35. What can go wrong when implementing cancellation and cleanup?

**Answer:** Leaving orphaned jobs after user cancel. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q36. How would you test or measure cancellation and cleanup?

**Answer:** Test cancellation during each stage. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q37. What is final status taxonomy, and why does it matter?

**Answer:** Report succeeded, partially completed, awaiting approval, blocked, failed, or cancelled with evidence. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q38. Give a practical example of final status taxonomy.

**Answer:** Job report lists 399 rows, 231 not verified, and reason codes. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q39. What can go wrong when implementing final status taxonomy?

**Answer:** Collapsing every outcome into success/failure. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q40. How would you test or measure final status taxonomy?

**Answer:** Validate outcome statuses against trace data. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

---

**Final self-check:** Can you explain this topic without relying on a framework name? Can you name the control-plane owner, the most serious failure, a safe fallback, and one metric proving it works?
