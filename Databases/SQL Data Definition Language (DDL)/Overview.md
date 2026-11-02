# SQL Data Definition Language (DDL)

**Track:** SQL Data Definition Language (DDL) · **Priority:** `P0`

> **Core idea:** DDL defines database objects and schema: creating, changing, and removing tables, indexes, and other structures. DDL behavior inside transactions varies across vendors.


## Detailed theory

DDL defines and changes database structure: tables, constraints, indexes, views, and other schema objects. Core operations: `CREATE`, `ALTER`, `DROP`; many tutorials include `TRUNCATE` here, though terminology and transactional semantics differ.

## Lifecycle example
```sql
CREATE TABLE projects (
  project_id BIGINT PRIMARY KEY,
  name VARCHAR(120) NOT NULL,
  status VARCHAR(20) NOT NULL DEFAULT 'open',
  CONSTRAINT status_allowed CHECK (status IN ('open','closed'))
);

ALTER TABLE projects ADD COLUMN created_at TIMESTAMP;

DROP TABLE projects;
```

## DDL vs DML
- DDL changes schema or database object definitions.
- DML changes **rows**: `INSERT`, `UPDATE`, `DELETE`.
- Querying uses `SELECT` (often called DQL).
- DCL manages access.
- `TRUNCATE` removes table rows without individual `DELETE` operations; behavior varies in locking, identity reset, triggers, privileges, rollback, and referential integrity.

## Production schema migrations
1. Understand existing data volume, current indexes, consumers and constraints.
2. Prefer backward-compatible **expand → migrate/backfill → contract** changes for zero-downtime deployments.
3. Assess locks, table rewrites, long-running transactions, replication lag and rollback strategy.
4. Validate constraints and test migration on representative data.
5. Avoid assuming DDL is fully transactional across all databases; PostgreSQL supports many transactional DDL operations, while MySQL commonly uses implicit commits.

## Interview prompts
- What is the difference between `DELETE`, `TRUNCATE`, and `DROP`?
- Can `ALTER TABLE` lock production traffic?
- How would you add a NOT NULL column to a huge table safely?
- Do all DBMSs roll back DDL when a transaction fails? No.

## Worked example — understand the *why*

```sql
CREATE TABLE tasks (id BIGINT PRIMARY KEY, status TEXT NOT NULL);
ALTER TABLE tasks ADD COLUMN created_at TIMESTAMP;
DROP TABLE tasks;
```
In production, consider locks, migration duration, application compatibility, backups, and rollback strategy. Do not assume all DDL commands can be rolled back on every DBMS.

## Possible interview questions (with answer guidance)

1. **DDL vs DML?**
   - *Answer guidance:* DDL changes schema/objects; DML changes rows (though SELECT is often called DQL).
2. **Why are schema migrations risky in production?**
   - *Answer guidance:* Table locks, long rewrites, application version mismatch, and data loss.
3. **Is DDL automatically committed?**
   - *Answer guidance:* DBMS-specific; PostgreSQL generally supports transactional DDL, many MySQL operations implicitly commit.


---

