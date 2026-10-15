# Human-in-the-Loop Reviews, Approvals, and Escalation

## 1. Mental model in 60 seconds

Human-in-the-Loop Reviews, Approvals, and Escalation is best understood as a **system-design choice**, not a magic model feature. The LLM may propose interpretations and actions; the **application** owns permissions, control flow, durability, verified outcomes, and failure behavior. When interviewing, begin with the goal and risk, then show how the architecture enforces boundaries.

### Vocabulary to know

| Term | Meaning |
|---|---|
| **Approval gates** | Pause before specified side effects and request explicit human authorization. |
| **Review payload** | Give reviewers enough context: proposed action, rationale, evidence, impact, and alternatives. |
| **Escalation rules** | Escalate ambiguity, policy conflicts, high impact, repeated failures, and insufficient evidence. |
| **Resume semantics** | Save a durable checkpoint so an interrupted run can resume safely. |
| **Authorization** | Approval identity and authority must be verified independently of the model. |
| **Time-to-live** | Approvals should expire when context or business state becomes stale. |
| **Optimistic locking** | Re-check state/version at execution to avoid time-of-check/time-of-use races. |
| **Audit trail** | Persist initiator, reviewer, timestamps, diff, policy decision, and execution outcome. |
| **Review burden** | Too many gates cause rubber-stamping; reserve human review for meaningful decisions. |
| **Fallback ownership** | Define who takes responsibility when approval is rejected, unavailable, or times out. |

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

### 3.1 Approval gates

**What it means.** Pause before specified side effects and request explicit human authorization.

**Concrete example.** An agent proposes a supplier update and shows an exact diff before save.

**Common mistake.** Executing first and asking permission afterward.

**How to validate it.** Verify pending operations cannot execute before approval.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.2 Review payload

**What it means.** Give reviewers enough context: proposed action, rationale, evidence, impact, and alternatives.

**Concrete example.** Show old/new material mapping plus source-system checks.

**Common mistake.** Asking reviewers to approve opaque model reasoning.

**How to validate it.** Test whether reviewers can spot seeded errors.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.3 Escalation rules

**What it means.** Escalate ambiguity, policy conflicts, high impact, repeated failures, and insufficient evidence.

**Concrete example.** An unknown ERP mapping is routed to a domain owner.

**Common mistake.** Silently guessing when authoritative sources conflict.

**How to validate it.** Measure recall on known escalation scenarios.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.4 Resume semantics

**What it means.** Save a durable checkpoint so an interrupted run can resume safely.

**Concrete example.** An agent waits overnight for an inventory-manager sign-off.

**Common mistake.** Keeping pending approval solely in RAM.

**How to validate it.** Restart worker processes while approvals remain pending.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.5 Authorization

**What it means.** Approval identity and authority must be verified independently of the model.

**Concrete example.** Only finance approvers can authorize a large refund.

**Common mistake.** Treating any reply of yes as sufficient authorization.

**How to validate it.** Test role and tenant boundary violations.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.6 Time-to-live

**What it means.** Approvals should expire when context or business state becomes stale.

**Concrete example.** Reject a pricing change approved after underlying price updates.

**Common mistake.** Applying an old approval to a new record version.

**How to validate it.** Modify the target record before approving and verify rejection.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.7 Optimistic locking

**What it means.** Re-check state/version at execution to avoid time-of-check/time-of-use races.

**Concrete example.** Require matching row version when writing approved stock adjustments.

**Common mistake.** Trusting an unchanged world between draft and approval.

**How to validate it.** Simulate concurrent edits and assert conflicts.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.8 Audit trail

**What it means.** Persist initiator, reviewer, timestamps, diff, policy decision, and execution outcome.

**Concrete example.** An audit log records the approving manager for a material delete.

**Common mistake.** Saving only the final updated value.

**How to validate it.** Reconstruct who approved what and when.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.9 Review burden

**What it means.** Too many gates cause rubber-stamping; reserve human review for meaningful decisions.

**Concrete example.** Automatically process low-risk reads, batch similar exceptions for review.

**Common mistake.** Requiring approval for every harmless search.

**How to validate it.** Track reviewer workload, turnaround, and error catches.

**Senior-level reasoning:** Ask what changes if this component is wrong, slow, unavailable, stale, or malicious. Define the invariant that must hold despite that failure. Name the owner of any side effect and decide whether to stop, retry, degrade, or escalate.

### 3.10 Fallback ownership

**What it means.** Define who takes responsibility when approval is rejected, unavailable, or times out.

**Concrete example.** Route a declined migration proposal to a manual operations queue.

**Common mistake.** Blocking business processes indefinitely.

**How to validate it.** Test reject, timeout, delegation, and cancellation paths.

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

### Q1. What is approval gates, and why does it matter?

**Answer:** Pause before specified side effects and request explicit human authorization. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q2. Give a practical example of approval gates.

**Answer:** An agent proposes a supplier update and shows an exact diff before save. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q3. What can go wrong when implementing approval gates?

**Answer:** Executing first and asking permission afterward. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q4. How would you test or measure approval gates?

**Answer:** Verify pending operations cannot execute before approval. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q5. What is review payload, and why does it matter?

**Answer:** Give reviewers enough context: proposed action, rationale, evidence, impact, and alternatives. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q6. Give a practical example of review payload.

**Answer:** Show old/new material mapping plus source-system checks. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q7. What can go wrong when implementing review payload?

**Answer:** Asking reviewers to approve opaque model reasoning. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q8. How would you test or measure review payload?

**Answer:** Test whether reviewers can spot seeded errors. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q9. What is escalation rules, and why does it matter?

**Answer:** Escalate ambiguity, policy conflicts, high impact, repeated failures, and insufficient evidence. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q10. Give a practical example of escalation rules.

**Answer:** An unknown ERP mapping is routed to a domain owner. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q11. What can go wrong when implementing escalation rules?

**Answer:** Silently guessing when authoritative sources conflict. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q12. How would you test or measure escalation rules?

**Answer:** Measure recall on known escalation scenarios. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q13. What is resume semantics, and why does it matter?

**Answer:** Save a durable checkpoint so an interrupted run can resume safely. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q14. Give a practical example of resume semantics.

**Answer:** An agent waits overnight for an inventory-manager sign-off. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q15. What can go wrong when implementing resume semantics?

**Answer:** Keeping pending approval solely in RAM. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q16. How would you test or measure resume semantics?

**Answer:** Restart worker processes while approvals remain pending. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q17. What is authorization, and why does it matter?

**Answer:** Approval identity and authority must be verified independently of the model. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q18. Give a practical example of authorization.

**Answer:** Only finance approvers can authorize a large refund. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q19. What can go wrong when implementing authorization?

**Answer:** Treating any reply of yes as sufficient authorization. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q20. How would you test or measure authorization?

**Answer:** Test role and tenant boundary violations. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q21. What is time-to-live, and why does it matter?

**Answer:** Approvals should expire when context or business state becomes stale. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q22. Give a practical example of time-to-live.

**Answer:** Reject a pricing change approved after underlying price updates. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q23. What can go wrong when implementing time-to-live?

**Answer:** Applying an old approval to a new record version. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q24. How would you test or measure time-to-live?

**Answer:** Modify the target record before approving and verify rejection. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q25. What is optimistic locking, and why does it matter?

**Answer:** Re-check state/version at execution to avoid time-of-check/time-of-use races. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q26. Give a practical example of optimistic locking.

**Answer:** Require matching row version when writing approved stock adjustments. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q27. What can go wrong when implementing optimistic locking?

**Answer:** Trusting an unchanged world between draft and approval. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q28. How would you test or measure optimistic locking?

**Answer:** Simulate concurrent edits and assert conflicts. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q29. What is audit trail, and why does it matter?

**Answer:** Persist initiator, reviewer, timestamps, diff, policy decision, and execution outcome. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q30. Give a practical example of audit trail.

**Answer:** An audit log records the approving manager for a material delete. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q31. What can go wrong when implementing audit trail?

**Answer:** Saving only the final updated value. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q32. How would you test or measure audit trail?

**Answer:** Reconstruct who approved what and when. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q33. What is review burden, and why does it matter?

**Answer:** Too many gates cause rubber-stamping; reserve human review for meaningful decisions. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q34. Give a practical example of review burden.

**Answer:** Automatically process low-risk reads, batch similar exceptions for review. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q35. What can go wrong when implementing review burden?

**Answer:** Requiring approval for every harmless search. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q36. How would you test or measure review burden?

**Answer:** Track reviewer workload, turnaround, and error catches. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

### Q37. What is fallback ownership, and why does it matter?

**Answer:** Define who takes responsibility when approval is rejected, unavailable, or times out. In production, this determines what the application must enforce rather than merely ask the model to do.

### Q38. Give a practical example of fallback ownership.

**Answer:** Route a declined migration proposal to a manual operations queue. I would explicitly separate observations from authorized side effects and keep evidence for review.

### Q39. What can go wrong when implementing fallback ownership?

**Answer:** Blocking business processes indefinitely. The consequence is usually worse reliability, weaker auditability, or unnecessary risk. Design a bounded failure path rather than assuming the model will recover.

### Q40. How would you test or measure fallback ownership?

**Answer:** Test reject, timeout, delegation, and cancellation paths. Include success and failure fixtures, report the baseline, and check end-to-end impact instead of relying on subjective model ratings.

---

**Final self-check:** Can you explain this topic without relying on a framework name? Can you name the control-plane owner, the most serious failure, a safe fallback, and one metric proving it works?
