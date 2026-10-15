# Planning: Task Breakdown, Dependency Graphs, and Replanning

## 1. Mental model in 60 seconds

Planning: Task Breakdown, Dependency Graphs, and Replanning is best understood as a **system-design choice**, not a magic model feature. The LLM may propose interpretations and actions; the **application** owns permissions, control flow, durability, verified outcomes, and failure behavior. When interviewing, begin with the goal and risk, then show how the architecture enforces boundaries.

### Vocabulary to know

| Term | Meaning |
|---|---|
| **Goal decomposition** | Translate vague goals into observable deliverables and subgoals. |
| **Task dependencies** | Represent required-before relationships as a directed acyclic graph where possible. |
| **Critical path** | The longest dependency chain sets a lower bound on completion time. |
| **Resource constraints** | Plan for tool quotas, rate limits, token budget, and concurrency limits. |
| **Plan granularity** | Keep steps actionable without over-fragmenting a straightforward task. |
| **Replanning triggers** | Replan on a material new observation, failure, changed objective, or invalidated assumption. |
| **Plan validation** | Check preconditions, forbidden actions, missing information, and dependency consistency before execution. |
| **Partial completion** | Report completed items and blocked branches honestly instead of inventing completion. |
| **Branching and joins** | Use explicit gates when parallel branches feed downstream actions. |
| **Plan versus execution state** | Preserve both intended tasks and observed results to detect divergence. |

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

### 3.1 Goal decomposition

**What it means.** Translate vague goals into observable deliverables and subgoals.

**Concrete example.** Replace improve supplier data with inspect, validate, propose corrections, approve.

**Common mistake.** Creating steps whose completion cannot be verified.

**How to validate it.** Require acceptance criteria for every subgoal.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.2 Task dependencies

**What it means.** Represent required-before relationships as a directed acyclic graph where possible.

**Concrete example.** Validate ERP ID before creating its mapping.

**Common mistake.** Executing dependent writes in parallel.

**How to validate it.** Topologically sort and reject dependency cycles.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.3 Critical path

**What it means.** The longest dependency chain sets a lower bound on completion time.

**Concrete example.** ERP lookup and PIM lookup are parallel, but approval waits for both.

**Common mistake.** Optimizing a non-critical task while bottleneck remains.

**How to validate it.** Estimate path durations and measure actual bottleneck.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.4 Resource constraints

**What it means.** Plan for tool quotas, rate limits, token budget, and concurrency limits.

**Concrete example.** Only five ERP API calls can be in flight at once.

**Common mistake.** Assuming unlimited parallel tool execution.

**How to validate it.** Load test under realistic quotas.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.5 Plan granularity

**What it means.** Keep steps actionable without over-fragmenting a straightforward task.

**Concrete example.** One validate CSV node rather than a step per cell.

**Common mistake.** Generating 100 microsteps that consume the whole context.

**How to validate it.** Compare plan overhead and execution outcome.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.6 Replanning triggers

**What it means.** Replan on a material new observation, failure, changed objective, or invalidated assumption.

**Concrete example.** Supplier lookup returns merged accounts so switch mapping strategy.

**Common mistake.** Replanning after every harmless token or never replanning.

**How to validate it.** Test decision to replan on changed versus unchanged evidence.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.7 Plan validation

**What it means.** Check preconditions, forbidden actions, missing information, and dependency consistency before execution.

**Concrete example.** Reject a plan that deletes records before backup.

**Common mistake.** Treating the model-generated plan as policy authority.

**How to validate it.** Static check plans against tool permissions.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.8 Partial completion

**What it means.** Report completed items and blocked branches honestly instead of inventing completion.

**Concrete example.** Return 90 verified rows and 10 unresolved ERP IDs.

**Common mistake.** Marking task successful because most steps ran.

**How to validate it.** Check that outputs retain per-item statuses.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.9 Branching and joins

**What it means.** Use explicit gates when parallel branches feed downstream actions.

**Concrete example.** Material creation waits for compliance and ERP checks.

**Common mistake.** Consuming one branch result before the other finishes.

**How to validate it.** Simulate delayed branches and check join logic.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.10 Plan versus execution state

**What it means.** Preserve both intended tasks and observed results to detect divergence.

**Concrete example.** Plan says create mapping; execution records conflict and skip.

**Common mistake.** Mutating the plan to hide execution errors.

**How to validate it.** Compare planned and executed steps in trace reports.

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

### Q1. What is goal decomposition, and why does it matter?

**Answer:** Translate vague goals into observable deliverables and subgoals. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q2. Give a practical example of goal decomposition.

**Answer:** Replace improve supplier data with inspect, validate, propose corrections, approve. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q3. What can go wrong when implementing goal decomposition?

**Answer:** Creating steps whose completion cannot be verified. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q4. How would you test or measure goal decomposition?

**Answer:** Require acceptance criteria for every subgoal. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q5. What is task dependencies, and why does it matter?

**Answer:** Represent required-before relationships as a directed acyclic graph where possible. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q6. Give a practical example of task dependencies.

**Answer:** Validate ERP ID before creating its mapping. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q7. What can go wrong when implementing task dependencies?

**Answer:** Executing dependent writes in parallel. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q8. How would you test or measure task dependencies?

**Answer:** Topologically sort and reject dependency cycles. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q9. What is critical path, and why does it matter?

**Answer:** The longest dependency chain sets a lower bound on completion time. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q10. Give a practical example of critical path.

**Answer:** ERP lookup and PIM lookup are parallel, but approval waits for both. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q11. What can go wrong when implementing critical path?

**Answer:** Optimizing a non-critical task while bottleneck remains. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q12. How would you test or measure critical path?

**Answer:** Estimate path durations and measure actual bottleneck. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q13. What is resource constraints, and why does it matter?

**Answer:** Plan for tool quotas, rate limits, token budget, and concurrency limits. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q14. Give a practical example of resource constraints.

**Answer:** Only five ERP API calls can be in flight at once. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q15. What can go wrong when implementing resource constraints?

**Answer:** Assuming unlimited parallel tool execution. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q16. How would you test or measure resource constraints?

**Answer:** Load test under realistic quotas. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q17. What is plan granularity, and why does it matter?

**Answer:** Keep steps actionable without over-fragmenting a straightforward task. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q18. Give a practical example of plan granularity.

**Answer:** One validate CSV node rather than a step per cell. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q19. What can go wrong when implementing plan granularity?

**Answer:** Generating 100 microsteps that consume the whole context. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q20. How would you test or measure plan granularity?

**Answer:** Compare plan overhead and execution outcome. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q21. What is replanning triggers, and why does it matter?

**Answer:** Replan on a material new observation, failure, changed objective, or invalidated assumption. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q22. Give a practical example of replanning triggers.

**Answer:** Supplier lookup returns merged accounts so switch mapping strategy. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q23. What can go wrong when implementing replanning triggers?

**Answer:** Replanning after every harmless token or never replanning. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q24. How would you test or measure replanning triggers?

**Answer:** Test decision to replan on changed versus unchanged evidence. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q25. What is plan validation, and why does it matter?

**Answer:** Check preconditions, forbidden actions, missing information, and dependency consistency before execution. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q26. Give a practical example of plan validation.

**Answer:** Reject a plan that deletes records before backup. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q27. What can go wrong when implementing plan validation?

**Answer:** Treating the model-generated plan as policy authority. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q28. How would you test or measure plan validation?

**Answer:** Static check plans against tool permissions. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q29. What is partial completion, and why does it matter?

**Answer:** Report completed items and blocked branches honestly instead of inventing completion. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q30. Give a practical example of partial completion.

**Answer:** Return 90 verified rows and 10 unresolved ERP IDs. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q31. What can go wrong when implementing partial completion?

**Answer:** Marking task successful because most steps ran. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q32. How would you test or measure partial completion?

**Answer:** Check that outputs retain per-item statuses. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q33. What is branching and joins, and why does it matter?

**Answer:** Use explicit gates when parallel branches feed downstream actions. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q34. Give a practical example of branching and joins.

**Answer:** Material creation waits for compliance and ERP checks. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q35. What can go wrong when implementing branching and joins?

**Answer:** Consuming one branch result before the other finishes. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q36. How would you test or measure branching and joins?

**Answer:** Simulate delayed branches and check join logic. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q37. What is plan versus execution state, and why does it matter?

**Answer:** Preserve both intended tasks and observed results to detect divergence. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q38. Give a practical example of plan versus execution state.

**Answer:** Plan says create mapping; execution records conflict and skip. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q39. What can go wrong when implementing plan versus execution state?

**Answer:** Mutating the plan to hide execution errors. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q40. How would you test or measure plan versus execution state?

**Answer:** Compare planned and executed steps in trace reports. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

---

**Final self-check:** Can you explain this topic without relying on a framework name? Can you name the control-plane owner, the most serious failure, a safe fallback, and one metric proving it works?
