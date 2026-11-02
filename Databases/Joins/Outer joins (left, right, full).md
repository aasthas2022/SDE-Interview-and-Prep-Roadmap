# Outer joins (left, right, full)

**Track:** Joins · **Priority:** `P0`

> **Core idea:** Outer joins preserve rows without matches by filling columns from the missing side with NULL. LEFT preserves left; RIGHT preserves right; FULL preserves both.


## Detailed theory

- **LEFT:** all rows from left source; unmatched right-side columns become NULL.
- **RIGHT:** all rows from right source; unmatched left-side columns become NULL; often expressible by swapping sides of a LEFT JOIN.
- **FULL OUTER:** matched rows plus unmatched rows from **either** source; availability differs by DBMS.

```sql
-- All customers, including those with no orders
SELECT c.customer_id, o.order_id
FROM customers c LEFT JOIN orders o ON o.customer_id = c.customer_id;

-- Customers with no orders (left anti-join)
SELECT c.customer_id
FROM customers c LEFT JOIN orders o ON o.customer_id = c.customer_id
WHERE o.order_id IS NULL;

-- Portable, often clearer anti-join
SELECT c.customer_id FROM customers c
WHERE NOT EXISTS (
  SELECT 1 FROM orders o WHERE o.customer_id = c.customer_id
);

-- All unmatched and matched IDs from either side
SELECT c.customer_id, o.order_id
FROM customers c FULL OUTER JOIN orders o
  ON o.customer_id = c.customer_id;
```

**Trap:** `WHERE o.status = 'paid'` after LEFT JOIN drops unmatched customers because NULL does not satisfy it; putting the restriction in `ON` preserves them.

**Trap:** `COUNT(*)` on a LEFT JOIN can be 1 for a customer with no orders; use `COUNT(o.order_id)` when counting actual matches.

**Interview prompt:** Find users without orders. Explain the difference between filtering a right-side column in `ON` vs `WHERE`.

## Worked example — understand the *why*

```sql
-- Return every customer, even without an order:
SELECT c.id, o.id AS order_id
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id;
-- Return unmatched rows from both sides (PostgreSQL):
SELECT a.id AS a_id, b.id AS b_id
FROM a FULL OUTER JOIN b ON a.id = b.id;
```
RIGHT JOIN is usually rewritable as LEFT JOIN by swapping table order. FULL OUTER JOIN availability differs across SQL engines.

## Possible interview questions (with answer guidance)

1. **INNER vs LEFT vs FULL OUTER JOIN?**
   - *Answer guidance:* Matching only; all left plus matching right; all rows from both with NULLs where absent.
2. **Find customers who never ordered.**
   - *Answer guidance:* LEFT JOIN orders then WHERE orders.id IS NULL, or NOT EXISTS.
3. **What happens if WHERE filters a nullable right-side column after LEFT JOIN?**
   - *Answer guidance:* Unmatched left rows may be removed.
4. **Is FULL OUTER JOIN supported in MySQL?**
   - *Answer guidance:* Not natively in commonly used MySQL versions; emulate when required.


---

