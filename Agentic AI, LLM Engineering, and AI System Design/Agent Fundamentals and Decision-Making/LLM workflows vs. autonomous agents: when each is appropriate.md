# LLM Workflows vs. Autonomous Agents

## 1. Mental model in 60 seconds

LLM Workflows vs. Autonomous Agents is best understood as a **system-design choice**, not a magic model feature. The LLM may propose interpretations and actions; the **application** owns permissions, control flow, durability, verified outcomes, and failure behavior. When interviewing, begin with the goal and risk, then show how the architecture enforces boundaries.

### Vocabulary to know

| Term | Meaning |
|---|---|
| **Workflow definition** | A workflow has an application-defined path even if individual steps use an LLM. |
| **Agent definition** | An agent dynamically chooses next steps and tools to pursue a goal within constraints. |
| **Prompt-response baseline** | A single model call is often the cheapest viable solution. |
| **Prompt chaining** | Break a fixed task into sequenced transformations when stages need separate checks. |
| **Routing workflow** | Map inputs to specialist handlers with rules or a classification model. |
| **Parallelization** | Run independent subtasks simultaneously and aggregate the results. |
| **Evaluator-optimizer** | Iteratively improve an artifact with a separate evaluator and bounded revisions. |
| **Dynamic uncertainty** | Agents pay off when the sequence of investigation cannot be known beforehand. |
| **Trade-off matrix** | Compare predictability, latency, cost, observability, flexibility, and blast radius. |
| **Graduated architecture** | Start with a fixed workflow, add model judgment only where failure evidence warrants it. |

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

### 3.1 Workflow definition

**What it means.** A workflow has an application-defined path even if individual steps use an LLM.

**Concrete example.** Extract invoice fields, validate, request approval, then write.

**Common mistake.** Calling any chain of LLM prompts an autonomous agent.

**How to validate it.** Diagram which component controls each transition.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.2 Agent definition

**What it means.** An agent dynamically chooses next steps and tools to pursue a goal within constraints.

**Concrete example.** Investigate an unknown supply-chain mismatch using several read tools.

**Common mistake.** Assuming an agent always needs multiple models.

**How to validate it.** Test behavior under varied unexpected observations.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.3 Prompt-response baseline

**What it means.** A single model call is often the cheapest viable solution.

**Concrete example.** Summarize a short support ticket.

**Common mistake.** Creating a planner and memory store for trivial summarization.

**How to validate it.** Compare quality and latency to more complex designs.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.4 Prompt chaining

**What it means.** Break a fixed task into sequenced transformations when stages need separate checks.

**Concrete example.** Extract requirements, classify, then generate a formatted report.

**Common mistake.** Splitting a simple task into redundant calls.

**How to validate it.** Check step-wise failure propagation.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.5 Routing workflow

**What it means.** Map inputs to specialist handlers with rules or a classification model.

**Concrete example.** Route password reset to deterministic backend service.

**Common mistake.** Building an open-ended agent to select among two fixed handlers.

**How to validate it.** Measure routing precision and fallback frequency.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.6 Parallelization

**What it means.** Run independent subtasks simultaneously and aggregate the results.

**Concrete example.** Check tax code and supplier metadata concurrently.

**Common mistake.** Parallelize dependent state changes that require ordering.

**How to validate it.** Validate consistency and p95 latency.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.7 Evaluator-optimizer

**What it means.** Iteratively improve an artifact with a separate evaluator and bounded revisions.

**Concrete example.** Draft a SQL query, run syntax check, repair once.

**Common mistake.** Using an untrusted self-grade as proof of correctness.

**How to validate it.** Test improvement on external gold-standard cases.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.8 Dynamic uncertainty

**What it means.** Agents pay off when the sequence of investigation cannot be known beforehand.

**Concrete example.** Diagnose an intermittent production incident from logs and metrics.

**Common mistake.** Forcing fixed branches for every possible unknown anomaly.

**How to validate it.** Use scenario diversity tests and compare coverage.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.9 Trade-off matrix

**What it means.** Compare predictability, latency, cost, observability, flexibility, and blast radius.

**Concrete example.** Choose a workflow for regulated approvals and an agent for exploratory diagnosis.

**Common mistake.** Selecting based on marketing terminology.

**How to validate it.** Build a decision table for each use case.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.10 Graduated architecture

**What it means.** Start with a fixed workflow, add model judgment only where failure evidence warrants it.

**Concrete example.** Introduce adaptive retrieval only after fixed search misses documented cases.

**Common mistake.** Starting with a multi-agent hierarchy without baseline metrics.

**How to validate it.** A/B test added autonomy against a simpler baseline.

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

### Q1. What is workflow definition, and why does it matter?

**Answer:** A workflow has an application-defined path even if individual steps use an LLM. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q2. Give a practical example of workflow definition.

**Answer:** Extract invoice fields, validate, request approval, then write. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q3. What can go wrong when implementing workflow definition?

**Answer:** Calling any chain of LLM prompts an autonomous agent. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q4. How would you test or measure workflow definition?

**Answer:** Diagram which component controls each transition. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q5. What is agent definition, and why does it matter?

**Answer:** An agent dynamically chooses next steps and tools to pursue a goal within constraints. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q6. Give a practical example of agent definition.

**Answer:** Investigate an unknown supply-chain mismatch using several read tools. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q7. What can go wrong when implementing agent definition?

**Answer:** Assuming an agent always needs multiple models. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q8. How would you test or measure agent definition?

**Answer:** Test behavior under varied unexpected observations. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q9. What is prompt-response baseline, and why does it matter?

**Answer:** A single model call is often the cheapest viable solution. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q10. Give a practical example of prompt-response baseline.

**Answer:** Summarize a short support ticket. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q11. What can go wrong when implementing prompt-response baseline?

**Answer:** Creating a planner and memory store for trivial summarization. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q12. How would you test or measure prompt-response baseline?

**Answer:** Compare quality and latency to more complex designs. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q13. What is prompt chaining, and why does it matter?

**Answer:** Break a fixed task into sequenced transformations when stages need separate checks. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q14. Give a practical example of prompt chaining.

**Answer:** Extract requirements, classify, then generate a formatted report. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q15. What can go wrong when implementing prompt chaining?

**Answer:** Splitting a simple task into redundant calls. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q16. How would you test or measure prompt chaining?

**Answer:** Check step-wise failure propagation. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q17. What is routing workflow, and why does it matter?

**Answer:** Map inputs to specialist handlers with rules or a classification model. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q18. Give a practical example of routing workflow.

**Answer:** Route password reset to deterministic backend service. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q19. What can go wrong when implementing routing workflow?

**Answer:** Building an open-ended agent to select among two fixed handlers. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q20. How would you test or measure routing workflow?

**Answer:** Measure routing precision and fallback frequency. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q21. What is parallelization, and why does it matter?

**Answer:** Run independent subtasks simultaneously and aggregate the results. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q22. Give a practical example of parallelization.

**Answer:** Check tax code and supplier metadata concurrently. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q23. What can go wrong when implementing parallelization?

**Answer:** Parallelize dependent state changes that require ordering. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q24. How would you test or measure parallelization?

**Answer:** Validate consistency and p95 latency. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q25. What is evaluator-optimizer, and why does it matter?

**Answer:** Iteratively improve an artifact with a separate evaluator and bounded revisions. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q26. Give a practical example of evaluator-optimizer.

**Answer:** Draft a SQL query, run syntax check, repair once. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q27. What can go wrong when implementing evaluator-optimizer?

**Answer:** Using an untrusted self-grade as proof of correctness. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q28. How would you test or measure evaluator-optimizer?

**Answer:** Test improvement on external gold-standard cases. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q29. What is dynamic uncertainty, and why does it matter?

**Answer:** Agents pay off when the sequence of investigation cannot be known beforehand. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q30. Give a practical example of dynamic uncertainty.

**Answer:** Diagnose an intermittent production incident from logs and metrics. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q31. What can go wrong when implementing dynamic uncertainty?

**Answer:** Forcing fixed branches for every possible unknown anomaly. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q32. How would you test or measure dynamic uncertainty?

**Answer:** Use scenario diversity tests and compare coverage. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q33. What is trade-off matrix, and why does it matter?

**Answer:** Compare predictability, latency, cost, observability, flexibility, and blast radius. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q34. Give a practical example of trade-off matrix.

**Answer:** Choose a workflow for regulated approvals and an agent for exploratory diagnosis. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q35. What can go wrong when implementing trade-off matrix?

**Answer:** Selecting based on marketing terminology. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q36. How would you test or measure trade-off matrix?

**Answer:** Build a decision table for each use case. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q37. What is graduated architecture, and why does it matter?

**Answer:** Start with a fixed workflow, add model judgment only where failure evidence warrants it. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q38. Give a practical example of graduated architecture.

**Answer:** Introduce adaptive retrieval only after fixed search misses documented cases. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q39. What can go wrong when implementing graduated architecture?

**Answer:** Starting with a multi-agent hierarchy without baseline metrics. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q40. How would you test or measure graduated architecture?

**Answer:** A/B test added autonomy against a simpler baseline. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

---

**Final self-check:** Can you explain this topic without relying on a framework name? Can you name the control-plane owner, the most serious failure, a safe fallback, and one metric proving it works?
