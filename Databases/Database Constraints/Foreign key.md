# Foreign key

**Track:** Database Constraints · **Priority:** `P1`

> **Core idea:** A FOREIGN KEY requires referenced values to exist in a candidate key, usually a primary or unique key. It protects relationships from orphaned child records.


## Detailed theory

A foreign key enforces that a non-NULL referencing key matches an eligible referenced candidate/unique key (subject to database rules). It prevents orphaned relationships.

```sql
CREATE TABLE departments (id BIGINT PRIMARY KEY);
CREATE TABLE employees (
  id BIGINT PRIMARY KEY,
  department_id BIGINT NOT NULL,
  CONSTRAINT fk_department FOREIGN KEY (department_id)
    REFERENCES departments(id) ON DELETE RESTRICT
);
```

## Referential actions
- `RESTRICT` / `NO ACTION`: reject deletion/update that would break references (timing/deferrability may differ).
- `CASCADE`: delete/update dependent records appropriately.
- `SET NULL`: make referencing columns NULL (must permit NULL).
- `SET DEFAULT`: assign default values (must remain valid).

## Nuances
- FKs may be composite; match column order and types appropriately.
- A referencing column is not necessarily indexed automatically: add an index when joins/deletes warrant it.
- Circular relations and deferred constraints are database-specific.
- The referenced row must exist at enforcement time, subject to deferrable rules.

**Interview prompt:** Why does inserting an order with a nonexistent customer fail? When would `ON DELETE CASCADE` be dangerous?

## Worked example — understand the *why*

```sql
CREATE TABLE customers(id BIGINT PRIMARY KEY);
CREATE TABLE orders(
 id BIGINT PRIMARY KEY,
 customer_id BIGINT NOT NULL REFERENCES customers(id) ON DELETE RESTRICT
);
```
Deleting a parent can be `RESTRICT`/`NO ACTION`, `CASCADE`, `SET NULL`, etc. Exact differences between `NO ACTION` and `RESTRICT` can involve deferrable constraints.

## Possible interview questions (with answer guidance)

1. **What is a referential integrity violation?**
   - *Answer guidance:* Child row refers to an absent parent key.
2. **When should ON DELETE CASCADE be used?**
   - *Answer guidance:* For owned dependent rows where parent deletion should intentionally delete children; avoid surprise loss.
3. **Can a foreign key column contain NULL?**
   - *Answer guidance:* Yes unless NOT NULL is specified; NULL usually means no required reference.


---

