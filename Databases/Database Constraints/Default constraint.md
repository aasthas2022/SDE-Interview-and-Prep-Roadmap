# Default constraint

**Track:** Database Constraints · **Priority:** `P1`

> **Core idea:** DEFAULT supplies a value when a column is omitted or the DEFAULT keyword is used. It does not override an explicit NULL.


## Detailed theory

A `DEFAULT` supplies a column value when an `INSERT` omits it or explicitly requests `DEFAULT` (syntax varies). It does not usually replace an explicitly supplied `NULL`.

```sql
CREATE TABLE jobs (
  id BIGINT PRIMARY KEY,
  status VARCHAR(20) NOT NULL DEFAULT 'pending',
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO jobs (id) VALUES (10);
```

**Uses:** creation timestamps, booleans, initial workflow states. A DEFAULT is not the same as a CHECK: it provides a value but does not restrict future updates. Default functions, time zones, and row-generation mechanics differ by engine.

**Trap:** `INSERT INTO jobs (id, status) VALUES (11, NULL)` usually fails due to `NOT NULL` rather than getting `'pending'`.

**Interview prompt:** How does `DEFAULT` differ from `NOT NULL` and from a database trigger?

## Worked example — understand the *why*

```sql
CREATE TABLE jobs (
 id BIGINT PRIMARY KEY,
 state TEXT NOT NULL DEFAULT 'queued',
 created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO jobs(id) VALUES (1);  -- state becomes queued
```
Use database-generated timestamps thoughtfully; time zone types, evaluation semantics, and function portability differ by DBMS.

## Possible interview questions (with answer guidance)

1. **Does DEFAULT apply to an explicit NULL?**
   - *Answer guidance:* Normally no; explicit NULL is still NULL and may violate NOT NULL.
2. **Should every nullable column have a DEFAULT?**
   - *Answer guidance:* No; distinguish unknown from an intentional default.
3. **What is the risk of adding a new NOT NULL column?**
   - *Answer guidance:* Existing rows must be populated; large-table migrations may need staged rollout.


---

