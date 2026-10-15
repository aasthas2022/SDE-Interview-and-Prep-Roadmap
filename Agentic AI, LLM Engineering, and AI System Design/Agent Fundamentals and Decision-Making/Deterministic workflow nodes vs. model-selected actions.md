# Deterministic Workflow Nodes vs. Model-Selected Actions

## 1. Mental model in 60 seconds

Deterministic Workflow Nodes vs. Model-Selected Actions is best understood as a **system-design choice**, not a magic model feature. The LLM may propose interpretations and actions; the **application** owns permissions, control flow, durability, verified outcomes, and failure behavior. When interviewing, begin with the goal and risk, then show how the architecture enforces boundaries.

### Vocabulary to know

| Term | Meaning |
|---|---|
| **Fixed nodes** | A fixed node runs known code with predictable branching rules. |
| **Model-selected tools** | The model chooses among authorized tools based on ambiguous semantics or incomplete information. |
| **Conditional edges** | Deterministic edges use explicit predicates to route state through a graph. |
| **Semantic routing** | A classifier or LLM may map a request to a specialist when the meaning is uncertain. |
| **Contracts** | Define input/output schemas and pre/postconditions for every node. |
| **Hybrid orchestration** | Use code to enforce topology and gates, with models handling only flexible decisions. |
| **Parallel branches** | Independent deterministic or model calls can run concurrently, then join before synthesis. |
| **Retry boundaries** | Retry individual idempotent nodes rather than replaying a complete workflow with side effects. |
| **Versioning** | Version workflow definitions, prompts, and tool schemas for reproducible deployments. |
| **Evaluation split** | Measure rule correctness, routing quality, and end-to-end business success separately. |

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

### 3.1 Fixed nodes

**What it means.** A fixed node runs known code with predictable branching rules.

**Concrete example.** Validate CSV columns before any LLM reasoning.

**Common mistake.** Spending LLM tokens on syntax checks.

**How to validate it.** Test nodes with standard unit tests.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.2 Model-selected tools

**What it means.** The model chooses among authorized tools based on ambiguous semantics or incomplete information.

**Concrete example.** Choose whether to inspect PIM metadata or supplier data next.

**Common mistake.** Letting model invent new tool names.

**How to validate it.** Assert the selected tool belongs to the allowlist.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.3 Conditional edges

**What it means.** Deterministic edges use explicit predicates to route state through a graph.

**Concrete example.** If validation_errors>0, route to review.

**Common mistake.** Encoding policy in natural-language instructions only.

**How to validate it.** Exercise boundary cases for each predicate.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.4 Semantic routing

**What it means.** A classifier or LLM may map a request to a specialist when the meaning is uncertain.

**Concrete example.** Classify inquiry as shipment tracking, billing, or account support.

**Common mistake.** Using open-ended planning for a simple three-class routing problem.

**How to validate it.** Evaluate confusion matrix and fallback rate.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.5 Contracts

**What it means.** Define input/output schemas and pre/postconditions for every node.

**Concrete example.** A supplier lookup returns supplier_id, source, timestamp, status.

**Common mistake.** Returning untyped free text from business-critical nodes.

**How to validate it.** Run schema and invariant checks in CI.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.6 Hybrid orchestration

**What it means.** Use code to enforce topology and gates, with models handling only flexible decisions.

**Concrete example.** Rule-based compliance checks surround an LLM explanation step.

**Common mistake.** Assuming autonomy must apply to every node.

**How to validate it.** Measure error rates separately for rules and model judgments.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.7 Parallel branches

**What it means.** Independent deterministic or model calls can run concurrently, then join before synthesis.

**Concrete example.** Check ERP presence and PIM attributes in parallel.

**Common mistake.** Parallelizing steps with a hidden dependency.

**How to validate it.** Verify join completeness and timeout behavior.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.8 Retry boundaries

**What it means.** Retry individual idempotent nodes rather than replaying a complete workflow with side effects.

**Concrete example.** Retry a failed metadata fetch without recreating a material.

**Common mistake.** Restarting an entire purchase-order pipeline on one timeout.

**How to validate it.** Fault-inject at each node boundary.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.9 Versioning

**What it means.** Version workflow definitions, prompts, and tool schemas for reproducible deployments.

**Concrete example.** A trace references workflow v3 and parser schema v2.

**Common mistake.** Changing routing logic without recording its version.

**How to validate it.** Replay prior fixtures against new versions.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.10 Evaluation split

**What it means.** Measure rule correctness, routing quality, and end-to-end business success separately.

**Concrete example.** Track validator false negatives and model router misclassification.

**Common mistake.** Using a single subjective quality score.

**How to validate it.** Create component-level and integration-level tests.

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

### Q1. What is fixed nodes, and why does it matter?

**Answer:** A fixed node runs known code with predictable branching rules. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q2. Give a practical example of fixed nodes.

**Answer:** Validate CSV columns before any LLM reasoning. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q3. What can go wrong when implementing fixed nodes?

**Answer:** Spending LLM tokens on syntax checks. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q4. How would you test or measure fixed nodes?

**Answer:** Test nodes with standard unit tests. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q5. What is model-selected tools, and why does it matter?

**Answer:** The model chooses among authorized tools based on ambiguous semantics or incomplete information. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q6. Give a practical example of model-selected tools.

**Answer:** Choose whether to inspect PIM metadata or supplier data next. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q7. What can go wrong when implementing model-selected tools?

**Answer:** Letting model invent new tool names. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q8. How would you test or measure model-selected tools?

**Answer:** Assert the selected tool belongs to the allowlist. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q9. What is conditional edges, and why does it matter?

**Answer:** Deterministic edges use explicit predicates to route state through a graph. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q10. Give a practical example of conditional edges.

**Answer:** If validation_errors>0, route to review. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q11. What can go wrong when implementing conditional edges?

**Answer:** Encoding policy in natural-language instructions only. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q12. How would you test or measure conditional edges?

**Answer:** Exercise boundary cases for each predicate. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q13. What is semantic routing, and why does it matter?

**Answer:** A classifier or LLM may map a request to a specialist when the meaning is uncertain. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q14. Give a practical example of semantic routing.

**Answer:** Classify inquiry as shipment tracking, billing, or account support. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q15. What can go wrong when implementing semantic routing?

**Answer:** Using open-ended planning for a simple three-class routing problem. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q16. How would you test or measure semantic routing?

**Answer:** Evaluate confusion matrix and fallback rate. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q17. What is contracts, and why does it matter?

**Answer:** Define input/output schemas and pre/postconditions for every node. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q18. Give a practical example of contracts.

**Answer:** A supplier lookup returns supplier_id, source, timestamp, status. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q19. What can go wrong when implementing contracts?

**Answer:** Returning untyped free text from business-critical nodes. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q20. How would you test or measure contracts?

**Answer:** Run schema and invariant checks in CI. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q21. What is hybrid orchestration, and why does it matter?

**Answer:** Use code to enforce topology and gates, with models handling only flexible decisions. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q22. Give a practical example of hybrid orchestration.

**Answer:** Rule-based compliance checks surround an LLM explanation step. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q23. What can go wrong when implementing hybrid orchestration?

**Answer:** Assuming autonomy must apply to every node. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q24. How would you test or measure hybrid orchestration?

**Answer:** Measure error rates separately for rules and model judgments. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q25. What is parallel branches, and why does it matter?

**Answer:** Independent deterministic or model calls can run concurrently, then join before synthesis. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q26. Give a practical example of parallel branches.

**Answer:** Check ERP presence and PIM attributes in parallel. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q27. What can go wrong when implementing parallel branches?

**Answer:** Parallelizing steps with a hidden dependency. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q28. How would you test or measure parallel branches?

**Answer:** Verify join completeness and timeout behavior. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q29. What is retry boundaries, and why does it matter?

**Answer:** Retry individual idempotent nodes rather than replaying a complete workflow with side effects. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q30. Give a practical example of retry boundaries.

**Answer:** Retry a failed metadata fetch without recreating a material. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q31. What can go wrong when implementing retry boundaries?

**Answer:** Restarting an entire purchase-order pipeline on one timeout. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q32. How would you test or measure retry boundaries?

**Answer:** Fault-inject at each node boundary. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q33. What is versioning, and why does it matter?

**Answer:** Version workflow definitions, prompts, and tool schemas for reproducible deployments. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q34. Give a practical example of versioning.

**Answer:** A trace references workflow v3 and parser schema v2. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q35. What can go wrong when implementing versioning?

**Answer:** Changing routing logic without recording its version. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q36. How would you test or measure versioning?

**Answer:** Replay prior fixtures against new versions. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q37. What is evaluation split, and why does it matter?

**Answer:** Measure rule correctness, routing quality, and end-to-end business success separately. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q38. Give a practical example of evaluation split.

**Answer:** Track validator false negatives and model router misclassification. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q39. What can go wrong when implementing evaluation split?

**Answer:** Using a single subjective quality score. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q40. How would you test or measure evaluation split?

**Answer:** Create component-level and integration-level tests. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

---

**Final self-check:** Can you explain this topic without relying on a framework name? Can you name the control-plane owner, the most serious failure, a safe fallback, and one metric proving it works?
