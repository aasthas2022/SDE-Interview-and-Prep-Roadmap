# Unique constraint

**Track:** Database Constraints · **Priority:** `P1`

> **Core idea:** UNIQUE prevents duplicate non-null key combinations according to database semantics. It is useful for usernames, emails, and idempotency keys.


## Detailed theory

`UNIQUE` prevents duplicate key combinations, usually allowing multiple NULLs under the default behavior of many DBMSs. **NULL treatment varies:** PostgreSQL has `NULLS NOT DISTINCT` option; SQL Server's standard unique-index behavior differs; verify your database.

```sql
CREATE TABLE users (
  user_id BIGINT PRIMARY KEY,
  email VARCHAR(255) NOT NULL UNIQUE,
  country_code CHAR(2),
  phone VARCHAR(30),
  UNIQUE (country_code, phone)
);
```

A composite unique constraint applies to the combination, **not** each column independently. Two rows with the same `country_code` but different `phone` are allowed. `UNIQUE` often uses an index internally, but implementation details vary.

**Pitfall:** Pre-checking for an email in application code does not prevent a race; enforce `UNIQUE` and handle conflict errors.

**Interview prompt:** How does UNIQUE compare with PK? What happens when multiple rows have NULL email values?

## Worked example — understand the *why*

```sql
CREATE TABLE requests (
 id BIGINT PRIMARY KEY,
 idempotency_key TEXT NOT NULL UNIQUE
);
```
A pre-insert `SELECT` is not race-safe by itself; two requests may both see no row. A UNIQUE constraint is the concurrency-safe guard.

## Possible interview questions (with answer guidance)

1. **What happens when two sessions insert the same unique value?**
   - *Answer guidance:* At most one succeeds under a correct unique enforcement mechanism; one may block then fail.
2. **Why is UNIQUE plus NOT NULL often used together?**
   - *Answer guidance:* To disallow both duplicates and absent values.
3. **How does a composite UNIQUE work?**
   - *Answer guidance:* It enforces uniqueness on the combination, not each column independently.


---

