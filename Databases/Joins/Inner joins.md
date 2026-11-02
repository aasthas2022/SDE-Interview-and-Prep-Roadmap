# Inner joins

**Track:** Joins · **Priority:** `P0`

> **Core idea:** INNER JOIN keeps pairs of rows satisfying the join predicate; unmatched rows on either side disappear.


## Detailed theory

Keeps only pairings for which the join condition evaluates TRUE.

```sql
SELECT c.customer_id, c.name, o.order_id
FROM customers AS c
INNER JOIN orders AS o ON o.customer_id = c.customer_id;
```

For one customer with three orders, there are three output rows. If two rows on each side share a nonunique join key, that key can yield **4** paired rows. `JOIN` unqualified usually means `INNER JOIN`.

**Common mistakes:** joining `id = id` unqualified, assuming no duplicates, using an incorrect business key, and treating NULL = NULL as a match (it does not evaluate TRUE in ordinary equality).

**Interview prompt:** What is the resulting row count if customer 1 has three orders and customer 2 none? How do you show customer 2 as well?

## Worked example — understand the *why*

```sql
SELECT o.id, c.email
FROM orders o
INNER JOIN customers c ON c.id = o.customer_id;
```
If one customer has three orders, that customer’s attributes appear on three result rows. Use actual relationship cardinalities to reason about results.

## Possible interview questions (with answer guidance)

1. **Does INNER JOIN require a declared foreign key?**
   - *Answer guidance:* No; the predicate is enough, though declared keys improve integrity.
2. **What happens with NULL join keys on equality?**
   - *Answer guidance:* NULL = NULL is UNKNOWN, so they do not match in a normal equality join.
3. **How is INNER JOIN different from EXISTS?**
   - *Answer guidance:* EXISTS checks existence without multiplying each left row by the number of matches.


---

