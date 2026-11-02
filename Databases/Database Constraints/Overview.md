# Database Constraints

**Track:** Database Constraints · **Priority:** `P1`

> **Core idea:** Constraints are database-enforced rules. They provide a final line of defense even when application code, multiple services, or manual SQL writes bypass ordinary validation.


## Detailed theory

Constraints are schema-level rules that protect data integrity **regardless of which application writes**. Treat them as the database's last line of defense; also validate inputs in applications for good error messages.

| Constraint | Enforces | NULL behavior |
|---|---|---|
| `PRIMARY KEY` | Unique identity, non-NULL | NULL forbidden |
| `UNIQUE` | No duplicated constrained values | Multiple NULLs often allowed; varies by database |
| `FOREIGN KEY` | Referential integrity | NULL allowed unless `NOT NULL` |
| `CHECK` | Boolean rule per row | Usually UNKNOWN passes; add `NOT NULL` when necessary |
| `DEFAULT` | Value if expression omitted | Explicit NULL generally bypasses it |
| `NOT NULL` | Value must exist | NULL forbidden |

```sql
CREATE TABLE employees (
  employee_id BIGINT PRIMARY KEY,
  email VARCHAR(255) NOT NULL UNIQUE,
  department_id BIGINT REFERENCES departments(department_id),
  salary DECIMAL(12,2) NOT NULL CHECK (salary >= 0),
  active BOOLEAN NOT NULL DEFAULT TRUE
);
```

## Interview traps
- `UNIQUE` and `PRIMARY KEY` are not synonyms: a table can have several UNIQUE constraints but one PK.
- A foreign key doesn't automatically create an index on the **referencing** table in every DBMS (PostgreSQL, for example, does not automatically create that index).
- `CHECK (x > 0)` alone does not rule out NULL.
- A DB constraint can prevent violations under concurrency more reliably than “check first, then insert” without protection.
- Cascading FKs are powerful: `ON DELETE CASCADE` can remove dependent rows; understand data-loss implications.

See each dedicated file for syntax, tradeoffs, and interviewer follow-ups.

## Worked example — understand the *why*

```sql
CREATE TABLE products (
 product_id BIGINT PRIMARY KEY,
 sku TEXT NOT NULL UNIQUE,
 price NUMERIC(12,2) NOT NULL CHECK (price >= 0),
 status TEXT NOT NULL DEFAULT 'active'
);
```
All four constraints have distinct jobs: identity, uniqueness, validity, and omitted-value defaulting. None substitutes for the others.

## Possible interview questions (with answer guidance)

1. **Why enforce constraints in both application code and database?**
   - *Answer guidance:* Application validation offers friendly errors; database constraints enforce correctness across writers and races.
2. **Does UNIQUE always imply NOT NULL?**
   - *Answer guidance:* No. NULL treatment is database-dependent; many systems permit multiple NULLs.
3. **Can CHECK reject NULL?**
   - *Answer guidance:* SQL CHECK generally fails only when FALSE; UNKNOWN often passes, so add NOT NULL.


---

