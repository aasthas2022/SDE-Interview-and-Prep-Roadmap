# Isolation

**Track:** ACID properties · **Priority:** `P0`

> **Core idea:** Isolation determines which effects of concurrently executing transactions can be observed. Think in timelines, not merely in definitions.


## Detailed theory

**Definition:** Isolation governs what one transaction can observe of concurrent transactions and which concurrency anomalies are possible. Stronger isolation usually reduces anomalies but can increase blocking, conflicts, retries, or costs.

## Common anomalies
| Anomaly | Example |
|---|---|
| Dirty read | T2 reads T1's uncommitted change; T1 rolls back |
| Nonrepeatable read | T1 reads a row twice and sees different committed values |
| Phantom read | T1 reruns a predicate query and sees a changed set of matching rows |
| Lost update | Two writers both read an old value; a write overwrites the other's change |
| Write skew | Two transactions modify different rows after checking a shared rule, jointly violating the rule |

## ANSI isolation names and common expectations
| Isolation level | General intent | Caveat |
|---|---|---|
| READ UNCOMMITTED | Weakest; dirty reads may be allowed | Some DBMSs treat it as stronger |
| READ COMMITTED | No dirty reads; each statement sees committed data | Nonrepeatable/phantom reads may occur |
| REPEATABLE READ | Prevent nonrepeatable reads as classically defined | Actual MVCC behavior and phantom handling are vendor-specific |
| SERIALIZABLE | Effect equivalent to some serial transaction order | May produce serialization failures requiring retry |

**Important nuance:** The SQL standard's isolation-level phenomena don't exhaust practical anomalies. Snapshot isolation is *not automatically serializable*, and write skew may still occur under snapshot isolation. MySQL InnoDB, PostgreSQL and SQL Server differ; always discuss the database/version.

## Practical defenses
- Atomic conditional `UPDATE` (check affected row count).
- `SELECT ... FOR UPDATE` locking where supported and appropriate.
- Optimistic concurrency with `version` column in the `WHERE` clause.
- SERIALIZABLE with whole-transaction retry handling.
- Unique constraints as final protection for race-prone uniqueness.

```sql
-- Optimistic concurrency: succeeds only if version is unchanged
UPDATE inventory
SET available = available - 1, version = version + 1
WHERE sku = 'A' AND available > 0 AND version = 7;
```

## Deadlocks and retries
Locks can form cycles; databases usually detect deadlocks and abort one transaction. Transactions should be short; retry carefully for deadlocks/serialization failures, ideally with bounded backoff and idempotent business operations.


**Check:** Explain a dirty read vs phantom. Give a write-skew example. Why is snapshot isolation not always serializable?

## Worked example — understand the *why*

```text
T1: read seats_available = 1
T2: read seats_available = 1
T1: reserve seat
T2: reserve seat    <- danger if both act on stale state
```
Prefer a single conditional update and check affected rows, or use appropriate row locking. Higher isolation can reduce anomalies but may cause retries or blocking. Different database engines implement named levels differently.

## Possible interview questions (with answer guidance)

1. **Dirty vs nonrepeatable vs phantom read?**
   - *Answer guidance:* Dirty: see uncommitted data; nonrepeatable: the same row changes between reads; phantom: predicate returns a changed set.
2. **Is REPEATABLE READ always serializable?**
   - *Answer guidance:* No; its exact semantics vary by database and can permit anomalies.
3. **What is write skew?**
   - *Answer guidance:* Two transactions read a common condition then change different rows, violating a shared invariant.
4. **How do you prevent lost updates?**
   - *Answer guidance:* Atomic UPDATE, version checks, locking, or serializable transactions with retries.


---

