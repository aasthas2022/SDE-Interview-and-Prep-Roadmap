# Atomicity

**Track:** ACID properties · **Priority:** `P0`

> **Core idea:** Atomicity is an all-or-nothing property of one transaction. It does not mean an operation is individually fast or physically indivisible.


## Detailed theory

**Definition:** Every transaction commits all of its intended database changes or commits none of them. If a transaction fails before commit, its uncommitted database changes are undone (subject to DBMS-specific transactional features).

```sql
BEGIN;
INSERT INTO orders (order_id, customer_id, total) VALUES (9001, 42, 100);
INSERT INTO order_items (order_id, product_id, quantity) VALUES (9001, 7, 2);
COMMIT;
```
If the second statement fails and the transaction is rolled back, the order header should not be committed by itself. Some systems automatically mark a transaction failed; others require explicit rollback handling.

## How it works
Typical mechanisms include write-ahead logging (WAL), undo records, recovery processing, and transaction status tracking. The exact mechanics vary by engine. Savepoints enable *partial rollback within a transaction* without violating the final atomic commit unit.

```sql
BEGIN;
SAVEPOINT before_optional_step;
-- perform optional work
ROLLBACK TO SAVEPOINT before_optional_step;
COMMIT;
```

## Boundary and caveats
- A database transaction cannot automatically undo an external email, HTTP call, or third-party payment. Use **outbox**, idempotency, compensation/saga patterns where appropriate.
- DDL transaction behavior varies (PostgreSQL supports many transactional DDL statements; MySQL often implicitly commits DDL).
- Separate calls running in autocommit mode are not one transaction.


**Check:** What happens if a server crashes after the first SQL statement but before commit? Why can't an SQL rollback unsend an email?

## Worked example — understand the *why*

```sql
BEGIN;
INSERT INTO orders(order_id, customer_id, total) VALUES (101, 1, 200);
INSERT INTO order_items(order_id, sku, quantity) VALUES (101, 'SKU-A', 2);
-- If the second statement fails, roll back both statements.
ROLLBACK;
```
After the rollback, neither insert should remain committed. Real applications should ensure exceptions trigger rollback, including when connection pooling and timeouts occur.

## Possible interview questions (with answer guidance)

1. **What happens when statement 2 fails after statement 1 succeeds?**
   - *Answer guidance:* If both are in the same transaction, roll back; DBMS-specific transaction error handling matters.
2. **Why is atomicity important for order creation?**
   - *Answer guidance:* It prevents an order header existing without required items or vice versa.
3. **Can a distributed workflow across two databases rely on a local transaction?**
   - *Answer guidance:* No; consider distributed coordination, idempotency, or sagas and compensating actions.


---

