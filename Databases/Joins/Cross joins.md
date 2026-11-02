# Cross joins

**Track:** Joins · **Priority:** `P0`

> **Core idea:** CROSS JOIN returns every pair of rows. If A has m rows and B has n rows, the result has m × n rows before later filtering.


## Detailed theory

Produces the **Cartesian product**: every row from A paired with every row from B. If A has `m` rows and B has `n`, the result has **m × n rows** (before filtering). This can be intentional or accidental.

```sql
SELECT s.size, c.color FROM sizes s CROSS JOIN colors c;
-- 3 sizes × 4 colors = 12 combinations
```

**Useful:** constructing combinations, test matrices, calendars, and exhaustive product options. **Risk:** huge intermediate results and latency. An omitted join predicate in old comma-join syntax can inadvertently create a cross join.

**Interview prompt:** How many rows result from tables with 8 and 12 rows? How would you generate every day–region pair?

## Worked example — understand the *why*

```sql
SELECT s.size, c.color
FROM sizes s
CROSS JOIN colors c;
```
With sizes `{S,M}` and colors `{red,blue}`, output contains four combinations. An accidental missing join condition can create a costly Cartesian product.

## Possible interview questions (with answer guidance)

1. **When is CROSS JOIN useful?**
   - *Answer guidance:* Generating combinations, date grids, scenarios, and parameter matrices.
2. **How many rows from 7 CROSS JOIN 4?**
   - *Answer guidance:* 28 unless further predicates filter them.
3. **How can a CROSS JOIN happen accidentally?**
   - *Answer guidance:* Leaving out a join predicate or using an unqualified comma join.


---

