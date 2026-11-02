# Joins

**Track:** Joins · **Priority:** `P0`

> **Core idea:** A JOIN combines rows based on a condition. The most important interview skill is predicting which rows survive and whether a one-to-many match multiplies rows.


## Detailed theory

Joins combine rows from two or more table sources using a predicate. Start by asking: **Which side's unmatched rows should appear?**

```sql
-- sample data
-- customers: (1, Ana), (2, Ben), (3, Cam)
-- orders:    (10, 1), (11, 1), (12, 2)
```

| Join | Returns | Sample rows count |
|---|---|---|
| `INNER JOIN` | Matching customers-orders only | 3 |
| `LEFT JOIN` | All customers, matched orders or NULL | 4 |
| `RIGHT JOIN` | All orders plus unmatched orders-side rows | 3 in this example |
| `FULL OUTER JOIN` | Matched + unmatched from both | 4 |
| `CROSS JOIN` | Every customer-order combination | 9 |

## Safe mental model
Join cardinality depends on key relationships: 1:N expands one left row to many; M:N may expand dramatically. Before choosing a join, identify the join key, uniqueness on each side, which unmatched records matter, and expected duplicates.

## Important outer-join pitfall
```sql
-- A: includes only customers with matched PAID orders (WHERE filters NULL-extended rows)
SELECT c.id, o.id FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id
WHERE o.status = 'PAID';

-- B: retains every customer, pairing only paid orders
SELECT c.id, o.id FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id AND o.status = 'PAID';
```
The predicates have different meanings. An `INNER JOIN` is not inherently faster or safer; the optimizer and problem determine cost.

## Interview must-knows
- INNER vs LEFT; `ON` vs `WHERE`; many-to-many multiplication.
- Find missing related records using `NOT EXISTS` or left anti-join.
- `NULL` equality and duplicate keys.
- CROSS JOIN dangers and supported uses.
- FULL OUTER JOIN availability (not native in some systems, e.g. MySQL).

Read the specific join files and sketch result sets manually before executing SQL.

## Worked example — understand the *why*

```sql
-- Customers without orders:
SELECT c.id
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id
WHERE o.id IS NULL;
```
Place right-side filtering conditions in the `ON` clause when you want to preserve unmatched left rows. Putting `o.status = 'paid'` in `WHERE` may turn a LEFT JOIN into an effective INNER JOIN.

## Possible interview questions (with answer guidance)

1. **How would you find records with no match in another table?**
   - *Answer guidance:* LEFT JOIN + IS NULL or NOT EXISTS.
2. **Why did my join return more rows than either source table?**
   - *Answer guidance:* One-to-many or many-to-many matches multiply rows.
3. **JOIN condition versus WHERE condition for LEFT JOIN?**
   - *Answer guidance:* ON controls match; WHERE filters resulting rows, possibly removing NULL-extended unmatched rows.


---

