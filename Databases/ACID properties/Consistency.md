# Consistency

**Track:** ACID properties · **Priority:** `P0`

> **Core idea:** Consistency means a successful transaction takes the database from one valid state to another with respect to enforced constraints and application invariants. It does not mean every replica immediately has identical data.


## Detailed theory

**Definition:** A transaction must take the database from one state satisfying its declared invariants to another state satisfying those invariants, assuming the application performs valid operations. The database enforces **some** invariants through keys and checks; complex business rules may need transactional application logic and concurrency controls.

## Examples of invariants
- `orders.customer_id` references an existing customer (FK).
- Account balances cannot be negative (`CHECK (balance >= 0)` if appropriate).
- An order's line-item totals match its declared order total (often maintained by transactional logic, not a simple check).

```sql
CREATE TABLE inventory (
  sku TEXT PRIMARY KEY,
  available INTEGER NOT NULL CHECK (available >= 0)
);
UPDATE inventory
SET available = available - 1
WHERE sku = 'A' AND available > 0;
-- Check affected row count to know if reservation succeeded.
```

**Pitfall:** “Consistency” does **not** mean every concurrent read is the newest. That is a separate question involving isolation, replication, and read routing. Nor does the DB automatically know every business rule.


**Check:** Can an individually valid pair of updates violate a cross-table invariant? Why is an FK not enough to enforce total account balance?

## Worked example — understand the *why*

```sql
CREATE TABLE inventory (
 sku TEXT PRIMARY KEY,
 available INTEGER NOT NULL CHECK (available >= 0)
);
UPDATE inventory SET available = available - 1
WHERE sku = 'SKU-A' AND available > 0;
```
The `CHECK` constraint prevents negative stock; the predicate prevents an invalid decrement. Business rules spread across multiple tables may need application logic and suitable isolation.

## Possible interview questions (with answer guidance)

1. **What does ACID consistency actually guarantee?**
   - *Answer guidance:* Preservation of database-enforced invariants and any correctly implemented business rules.
2. **Why does CHECK (quantity >= 0) not fully prevent overselling?**
   - *Answer guidance:* It blocks negative stored values but cannot by itself coordinate reservations across other tables or concurrent workflows.
3. **Is ACID consistency the C in CAP?**
   - *Answer guidance:* No. CAP consistency concerns a distributed read/write model, a different use of the word.


---

