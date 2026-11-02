# Check constraint

**Track:** Database Constraints · **Priority:** `P1`

> **Core idea:** CHECK limits allowed values according to a Boolean expression. It is designed for row-level validity rules, not arbitrary cross-table checks.


## Detailed theory

A `CHECK` requires its expression not to be **FALSE** for inserted/updated rows. In many SQL engines, TRUE *or UNKNOWN* passes; therefore make a field `NOT NULL` if null is invalid.

```sql
CREATE TABLE products (
  id BIGINT PRIMARY KEY,
  price NUMERIC(10,2) NOT NULL CHECK (price >= 0),
  discount NUMERIC(5,2) DEFAULT 0,
  CHECK (discount BETWEEN 0 AND 100)
);
```

**Uses:** numeric ranges, status enumerations, ordering of two same-row dates (`end_date >= start_date`). Some systems limit expressions to the current row and prohibit subqueries / volatile expressions. Cross-row uniqueness is for `UNIQUE`, not CHECK.

**Trap:** `CHECK (price > 0)` generally allows `price = NULL`; `NOT NULL` prevents that. Also note named constraints and syntax vary across engines.

**Interview prompt:** How would you ensure a product can't have a negative price, including when two services write concurrently?

## Worked example — understand the *why*

```sql
CREATE TABLE invoices (
 id BIGINT PRIMARY KEY,
 amount NUMERIC(12,2) NOT NULL CHECK (amount >= 0),
 state TEXT NOT NULL CHECK (state IN ('draft', 'sent', 'paid'))
);
```
`CHECK (amount > 0)` alone does not reject `NULL`; combine with `NOT NULL` when required.

## Possible interview questions (with answer guidance)

1. **Why can NULL pass a CHECK constraint?**
   - *Answer guidance:* Because UNKNOWN is not FALSE under SQL CHECK semantics.
2. **How would you restrict a status to known values?**
   - *Answer guidance:* CHECK IN, lookup table plus foreign key, or DB-specific enum.
3. **When is a foreign key better than CHECK?**
   - *Answer guidance:* When legal values live in a separate maintained table.


---

