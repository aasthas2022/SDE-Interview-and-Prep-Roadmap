# DROP statement

**Track:** SQL Data Definition Language (DDL) · **Priority:** `P0`

> **Core idea:** DROP removes a database object. Treat it as destructive and distinct from deleting rows.


## Detailed theory

`DROP` removes a database **object** (such as a table or view), not merely its rows. It can permanently remove schema and data, and may affect dependent objects.

```sql
DROP TABLE old_events;
-- Optional syntax and dependency handling vary:
DROP TABLE IF EXISTS old_events;
```

**Distinguish clearly:**
- `DELETE FROM t WHERE ...`: removes selected rows; may fire row triggers.
- `DELETE FROM t`: removes all rows, retains table definition.
- `TRUNCATE TABLE t`: fast bulk row removal in many systems, with different locks/identity/trigger/transaction behavior.
- `DROP TABLE t`: removes the table object itself.

**Safety:** Check dependencies, backups, retention, permissions and migration order. `CASCADE` (where available) can drop dependent objects too. Vendor behavior for transactional rollback varies.

**Interview prompt:** What happens to indexes and foreign keys when a table is dropped? What is different from TRUNCATE?

## Worked example — understand the *why*

```sql
DROP TABLE IF EXISTS temp_import;
-- In PostgreSQL: DROP TABLE customers CASCADE; may remove dependent objects.
```
`DROP TABLE` removes the table definition and its data. `DELETE FROM table` removes selected/all rows but leaves the table. `TRUNCATE` removes all rows efficiently in many DBMSs, with different transactional/identity behavior.

## Possible interview questions (with answer guidance)

1. **DROP vs DELETE vs TRUNCATE?**
   - *Answer guidance:* DROP removes an object; DELETE removes rows optionally with WHERE; TRUNCATE removes all rows, implementation differs.
2. **What is the danger of CASCADE?**
   - *Answer guidance:* It can drop dependent objects you did not intend to remove.
3. **How should a production column be retired?**
   - *Answer guidance:* Stop reading/writing, deploy compatible code, verify, then drop in a later migration.


---

