# Third Normal Form (3NF)

**Track:** Normalization forms · **Priority:** `P0`

> **Core idea:** 3NF requires 2NF and excludes problematic transitive dependencies of non-prime attributes on keys. Formally, for every nontrivial X → A, X is a superkey or A is prime.


## Detailed theory

Formal definition: in 2NF (equivalently start from 1NF) and for every **nontrivial** functional dependency `X → A`, at least one holds: **X is a superkey**, or **A is a prime attribute** (part of some candidate key). A helpful beginner shorthand is “remove non-key attributes depending transitively on a key via another non-key attribute,” but the formal definition handles exceptions more accurately.

Before:
```text
Employees(emp_id PK, dept_id, dept_name)
emp_id → dept_id
 dept_id → dept_name
```
`dept_name` depends on `emp_id` via `dept_id`, which is not a superkey.

After:
```text
Employees(emp_id PK, dept_id FK)
Departments(dept_id PK, dept_name)
```

**Benefits:** Avoid changing a department name across employee rows and losing department details when the last employee leaves. **Trap:** splitting every repeated text value into its own table is not “normalization”; derive decisions from **functional dependencies** and business semantics.

**Interview prompt:** Explain a transitive dependency and an update anomaly. Can a table be in 3NF yet fail BCNF? Yes.

## Worked example — understand the *why*

```text
Bad: Employees(employee_id, department_id, department_name)
employee_id -> department_id -> department_name
Better: Employees(employee_id, department_id)
        Departments(department_id, department_name)
```
Now a department rename happens once. The common shorthand “no transitive dependencies” is useful for beginners but the formal 3NF definition has a prime-attribute exception.

## Possible interview questions (with answer guidance)

1. **What is a transitive dependency?**
   - *Answer guidance:* A key determines an attribute through another determinant, e.g., employee_id → department_id → name.
2. **How does 3NF differ from 2NF?**
   - *Answer guidance:* 2NF targets partial-key dependencies; 3NF also handles problematic transitive dependencies.
3. **What is a prime attribute?**
   - *Answer guidance:* An attribute that belongs to at least one candidate key.


---

