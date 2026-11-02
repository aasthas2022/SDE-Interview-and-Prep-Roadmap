# ALTER statement

**Track:** SQL Data Definition Language (DDL) · **Priority:** `P0`

> **Core idea:** ALTER changes existing objects. Prefer backward-compatible expansions before removing old columns or constraints.


## Detailed theory

`ALTER` modifies an existing object: add/drop/rename columns, change types, add/drop constraints, and more. Syntax varies significantly by database and release.

```sql
ALTER TABLE shipments ADD COLUMN delivered_at TIMESTAMP;
ALTER TABLE shipments ADD CONSTRAINT delivered_after_creation
  CHECK (delivered_at IS NULL OR delivered_at >= created_at);
```

**Production traps:** A seemingly small ALTER can lock a table, rewrite data, block writes or fail due to existing rows. Adding `NOT NULL` without backfilling old records may fail. Changing a type can cause truncation or errors. Some engines offer online/concurrent alternatives; know your vendor.

**Migration approach:** introduce nullable field → deploy writers → backfill safely → validate → enforce NOT NULL → remove obsolete field after consumers migrate.

**Interview prompt:** How would you add a required column to a large live table without breaking old application versions?

## Worked example — understand the *why*

```sql
-- Phase 1: add nullable field
ALTER TABLE customers ADD COLUMN preferred_name TEXT;
-- Phase 2: deploy writers/readers, backfill existing rows
-- Phase 3: enforce NOT NULL if the business rules require it
```
Safe migrations may use expand → backfill → switch application → contract. Database version, table size, and lock types matter.

## Possible interview questions (with answer guidance)

1. **How do you add a NOT NULL column to a large populated table safely?**
   - *Answer guidance:* Use staged add/default/backfill/validation, considering engine-specific lock behavior.
2. **What is an expand-and-contract migration?**
   - *Answer guidance:* Add new schema while maintaining compatibility; migrate users/data; remove old schema later.
3. **Why might ALTER TABLE block requests?**
   - *Answer guidance:* DDL may acquire locks or rewrite data, depending on the operation and engine.


---

