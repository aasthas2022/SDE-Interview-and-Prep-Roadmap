# ACID properties

**Track:** ACID properties · **Priority:** `P0`

> **Core idea:** ACID describes transaction guarantees, not the four SQL command types. A transaction groups operations into one logical unit of work. The properties jointly protect invariants when requests fail or execute concurrently.


## Detailed theory

ACID describes four key properties of reliable database **transactions**: **Atomicity, Consistency, Isolation, Durability**. They are related but distinct. A transaction is a group of operations treated as a logical unit.

```sql
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE account_id = 1;
UPDATE accounts SET balance = balance + 100 WHERE account_id = 2;
COMMIT;
-- ROLLBACK instead of COMMIT if something fails
```
This example alone is not a complete safe money-transfer implementation: it also needs sufficient-funds checks, correct concurrency control, appropriate constraints, and error handling.

| Letter | Core question | Typical mechanism |
|---|---|---|
| A | All or nothing? | Undo/redo logging, rollback |
| C | Does valid data stay valid? | Constraints + correct transaction logic |
| I | How do concurrent transactions interact? | Locks, MVCC, isolation levels |
| D | Will committed data survive a crash? | Write-ahead log, durable storage, recovery |

**Memorable distinction:** Atomicity protects against *partial work*; isolation protects against *interference from other work*. Consistency requires the application to define and maintain meaningful invariants. Durability is about survival after **commit**, subject to configured durability guarantees.

Learn the four dedicated files and rehearse transfer, inventory reservation, and order-payment examples. Do not conflate ACID **Consistency** with the **C** in the distributed-systems CAP theorem.

## High-value discussion prompts
- Can a transaction be atomic yet run under weak isolation? **Yes.**
- Does ACID mean transactions can never deadlock? **No.**
- Does a successful commit mean every replica is caught up? **No.**
- Are all SQL engines configured for identical durability and isolation? **No.**

## Worked example — understand the *why*

```sql
BEGIN;
UPDATE accounts SET balance = balance - 50 WHERE account_id = 1;
UPDATE accounts SET balance = balance + 50 WHERE account_id = 2;
COMMIT;
-- On error: ROLLBACK instead of COMMIT.
```
A money transfer illustrates atomicity (both updates or neither), consistency (business invariants), isolation (concurrent transfers), and durability (committed updates survive a crash). A bare pair of updates without a transaction is vulnerable to partial completion.

## Possible interview questions (with answer guidance)

1. **Expand ACID with a one-sentence example of each property.**
   - *Answer guidance:* Atomicity: all-or-none; consistency: constraints/invariants; isolation: concurrency visibility; durability: committed work survives failure.
2. **Does ACID guarantee high availability?**
   - *Answer guidance:* No. ACID is about transaction correctness, not service uptime.
3. **Is ACID the same as serializability?**
   - *Answer guidance:* No. Serializable isolation is one possible isolation guarantee; ACID does not require every transaction to use it.


---

