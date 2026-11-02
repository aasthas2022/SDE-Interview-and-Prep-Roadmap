# CREATE statement

**Track:** SQL Data Definition Language (DDL) · **Priority:** `P0`

> **Core idea:** CREATE declares a new database object and its structure. Types, constraints, and indexes should reflect the expected workload.


## Detailed theory

`CREATE` defines a schema object, commonly a table, index or view. Design types, nullability, keys, default values, and constraints carefully.

```sql
CREATE TABLE shipments (
  shipment_id BIGINT PRIMARY KEY,
  tracking_code VARCHAR(80) NOT NULL UNIQUE,
  status VARCHAR(30) NOT NULL DEFAULT 'created',
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX idx_shipments_status_created
  ON shipments(status, created_at);
```

**Design questions:** Is the ID stable? Should the tracking code be unique across all carriers or only within one carrier? Is a composite key better? What is the expected query workload? Indexes improve lookup but have storage/write costs.

**Interview prompt:** Design an orders table with a customer FK, nonnegative total and a creation timestamp.

## Worked example — understand the *why*

```sql
CREATE TABLE accounts (
 account_id BIGINT PRIMARY KEY,
 email TEXT NOT NULL UNIQUE,
 balance NUMERIC(12,2) NOT NULL DEFAULT 0 CHECK (balance >= 0)
);
CREATE INDEX idx_accounts_email ON accounts(email);
```
Since UNIQUE usually creates an index in PostgreSQL, the separate email index shown here is redundant. Avoid duplicating indexes in real schemas.

## Possible interview questions (with answer guidance)

1. **Which columns should be indexed?**
   - *Answer guidance:* Columns used in selective filters, joins, and sorts, balanced against write cost.
2. **Is index creation free?**
   - *Answer guidance:* No; storage, build time, and write overhead.
3. **What is the role of constraints in CREATE TABLE?**
   - *Answer guidance:* Enforce identity, uniqueness, relationships, and valid values.


---

