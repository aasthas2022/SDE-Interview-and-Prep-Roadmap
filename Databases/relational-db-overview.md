# Relational databases (SQL)

**Track:** Relational databases (SQL) · **Priority:** `P0`

> **Core idea:** Think of a relational database as named tables connected by explicit keys. A schema specifies allowed columns and constraints; SQL describes the data you want rather than the algorithm for retrieving it.


## Detailed theory

## What is a relational database?
A relational database stores structured information in **relations (tables)**. Each table has **columns (attributes)** and **rows (tuples)**. A **schema** describes the table's structure and constraints; an **instance** is the data at a particular moment. SQL is the declarative language used to define, query, and modify that data. SQL is standardized but implementations differ (PostgreSQL, MySQL, SQL Server, Oracle, SQLite).

Relational theory treats rows as unordered; SQL query results have **no guaranteed order without `ORDER BY`**. SQL also supports duplicate rows by default (bag semantics), whereas the mathematical relational model uses sets.

## Example schema
```sql
CREATE TABLE customers (
  customer_id BIGINT PRIMARY KEY,
  email VARCHAR(255) NOT NULL UNIQUE,
  name VARCHAR(100) NOT NULL
);
CREATE TABLE orders (
  order_id BIGINT PRIMARY KEY,
  customer_id BIGINT NOT NULL REFERENCES customers(customer_id),
  total DECIMAL(12,2) NOT NULL CHECK (total >= 0),
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```
**Entity:** customer. **Attribute:** email. **Primary key:** `customer_id`. **Foreign key:** `orders.customer_id`. **Relationship:** one customer can have many orders (one-to-many).

## Core vocabulary
| Term | Meaning | Watch out for |
|---|---|---|
| Database / schema | Collection of objects / logical namespace or structure (DBMS-dependent) | `schema` has two meanings |
| Table | Structured relation | Doesn't imply row ordering |
| Row | One record | May contain NULLs |
| Column | Named attribute with a type | Types and coercion differ by vendor |
| Candidate key | Minimal column set that uniquely identifies a row | May have multiple candidates |
| Primary key | Chosen candidate key; unique and non-NULL | One PK per table; it can be composite |
| Foreign key | Columns referencing eligible unique/primary columns | A nullable FK may be NULL |
| Surrogate key | Artificial ID | Doesn't replace domain uniqueness rules |
| Natural key | Meaningful business identifier | Could change over time |
| Index | Auxiliary structure speeding lookups | Costs writes and storage |
| View | Stored query definition | Usually not a physical copy |
| Materialized view | Persisted query result | Refresh and freshness vary |
| Transaction | Unit of work | Subject to isolation and rollback behavior |

## Relationship types
- **1:1**: put an FK with a `UNIQUE` constraint on one side; often separate sensitive/optional attributes.
- **1:N**: FK on the many side (`orders.customer_id`).
- **M:N**: bridge table with both FKs, often a composite primary key (`enrollments(student_id, course_id)`).

## SQL language categories
- **DDL:** `CREATE`, `ALTER`, `DROP` (and vendor-dependent `TRUNCATE`).
- **DML:** `INSERT`, `UPDATE`, `DELETE`, `MERGE` (often `SELECT` is considered DQL).
- **DQL:** `SELECT`, filtering, grouping, joins, windows.
- **DCL:** `GRANT`, `REVOKE`.
- **TCL:** `BEGIN`, `COMMIT`, `ROLLBACK`, `SAVEPOINT` (syntax varies).
These are learning categories, not fully consistent SQL standard classifications.

## SELECT processing — interview essential
Conceptual logical order (not necessarily execution plan):
1. `FROM` / `JOIN` and `ON`
2. `WHERE` — filters **rows**
3. `GROUP BY` — forms groups
4. `HAVING` — filters **groups**
5. `SELECT` — chooses/project expressions
6. `DISTINCT`
7. `ORDER BY`
8. `LIMIT` / `OFFSET` or `FETCH FIRST` (dialect-specific)

```sql
SELECT customer_id, COUNT(*) AS order_count,
       SUM(total) AS total_spend
FROM orders
WHERE created_at >= DATE '2026-01-01'
GROUP BY customer_id
HAVING COUNT(*) >= 2
ORDER BY total_spend DESC, customer_id
FETCH FIRST 10 ROWS ONLY;
```
This uses PostgreSQL-compatible syntax (other engines differ). Always include a tie-breaker for deterministic pagination.

## NULL and three-valued logic
`NULL` means unknown/missing/inapplicable, **not zero, empty string, or false**. Comparisons with NULL generally produce **UNKNOWN**, not TRUE. Use `IS NULL` / `IS NOT NULL`, not `= NULL`. `WHERE` preserves rows only when the predicate is TRUE.
```sql
SELECT * FROM orders WHERE customer_id IS NULL;
SELECT COALESCE(NULL, 0); -- 0
```
`COUNT(*)` counts rows; `COUNT(col)` counts non-NULL values; `COUNT(DISTINCT col)` counts distinct non-NULL values.

## Common data types
- Integers: `SMALLINT`, `INTEGER`, `BIGINT`.
- Exact numeric: `DECIMAL(p,s)` / `NUMERIC`; prefer for money; avoid floating-point for exact currencies.
- Approximate numeric: `REAL`, `DOUBLE PRECISION`.
- Character: `CHAR`, `VARCHAR`, `TEXT` (availability varies).
- Temporal: `DATE`, `TIME`, `TIMESTAMP` and time-zone-aware variants; time zone behavior varies widely.
- Boolean, binary, JSON/JSONB and UUID support are database-specific.

## Execution and performance intuition
SQL is **declarative**: specify *what* you want; the optimizer chooses *how*. Know table scans vs index scans, indexes (often B-trees), selectivity, cardinality, join algorithms (nested loop, hash, merge), and `EXPLAIN` plans. An index is not automatically useful for every query. Composite index ordering matters, and predicates/functions may impact index usability. Avoid `SELECT *` in production paths where an explicit projection is suitable.

## Transactions and concurrency
A transaction can read and write multiple tables as one unit. Isolation affects which concurrent changes are visible; atomicity controls whether partial effects are committed. A DBMS commonly uses locks and/or MVCC (multi-version concurrency control). A `COMMIT` is not the same as replication to every replica.

## Common interview questions
1. DBMS vs RDBMS? What does SQL actually guarantee?
2. Primary vs candidate vs unique vs foreign key?
3. `WHERE` vs `HAVING`? `COUNT(*)` vs `COUNT(column)`?
4. What is NULL and why does `NOT IN` sometimes surprise people?
5. Why does a query without `ORDER BY` produce unpredictable row order?
6. What is a composite index and when can it help?
7. How do you model many-to-many relationships?
8. When would denormalization help, and what does it cost?

## Quick review
- Can you draw a 1:N and M:N schema?
- Can you explain a SELECT query's conceptual stages?
- Can you reason about NULL and counts?
- Can you separate data correctness (constraints) from performance (indexes)?

## Worked example — understand the *why*

```sql
CREATE TABLE customers (
  customer_id BIGINT PRIMARY KEY,
  email TEXT NOT NULL UNIQUE
);
CREATE TABLE orders (
  order_id BIGINT PRIMARY KEY,
  customer_id BIGINT NOT NULL REFERENCES customers(customer_id),
  total NUMERIC(12,2) NOT NULL CHECK (total >= 0)
);
-- Return orders, including the customer email:
SELECT o.order_id, c.email, o.total
FROM orders AS o
JOIN customers AS c ON c.customer_id = o.customer_id
WHERE o.total >= 100
ORDER BY o.total DESC
LIMIT 10;
```
The foreign key makes the relationship explicit. The `JOIN` combines matching rows; `WHERE` removes unwanted matches; `ORDER BY` sorts; `LIMIT` truncates the result. In standard SQL, a table is unordered; rows have no guaranteed order without `ORDER BY`.

## Possible interview questions (with answer guidance)

1. **What distinguishes a primary key from a foreign key?**
   - *Answer guidance:* A primary key identifies a row in its own table; a foreign key references a key in another or the same table.
2. **What is the difference between a database and a schema?**
   - *Answer guidance:* A database stores related objects/data; a schema is a namespace/structural definition, with terminology varying by DBMS.
3. **Why might SELECT * be undesirable?**
   - *Answer guidance:* It fetches unnecessary columns, creates brittle dependencies on schema changes, and can increase I/O.
4. **What is NULL and why does = NULL not work?**
   - *Answer guidance:* NULL represents missing/unknown; comparisons yield UNKNOWN; use IS NULL.
5. **Explain logical SQL query processing order.**
   - *Answer guidance:* FROM/JOIN, WHERE, GROUP BY, HAVING, SELECT, DISTINCT, ORDER BY, LIMIT/OFFSET conceptually.


---

