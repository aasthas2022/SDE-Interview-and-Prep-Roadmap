# Durability

**Track:** ACID properties · **Priority:** `P0`

> **Core idea:** Durability is about committed changes surviving crashes according to the database’s configured durability guarantees. It is different from availability and from keeping backups forever.


## Detailed theory

**Definition:** Once a transaction's commit has been acknowledged under the system's durability settings, its committed effects survive the failures covered by the DBMS's guarantees, typically a process or machine crash.

## Usual mechanisms
- **Write-ahead logging (WAL):** log sufficient information before declaring commit durable.
- **Flush/synchronization:** ensure required log data reaches suitably persistent storage.
- **Crash recovery:** replay committed operations / undo incomplete ones.
- **Backups, snapshots, and replication:** strengthen disaster recovery but are **not equivalent** to the definition of transaction durability.

## Real-world qualification
Durability depends on configuration (e.g., asynchronous commit), hardware, storage correctness, and failure model. A commit acknowledged on a primary does not automatically mean an asynchronous replica has applied the write. Multi-region availability and backups are separate architectural guarantees.


**Check:** Is an async replica guaranteed to contain the last committed write? Does a backup taken last night prevent loss of today's data?

## Worked example — understand the *why*

```sql
BEGIN;
UPDATE orders SET status = 'paid' WHERE order_id = 101;
COMMIT;
```
A DBMS typically uses a write-ahead log (WAL)/redo log so committed state can be recovered after process or system restart. Exact protection depends on logging, flush settings, and storage reliability.

## Possible interview questions (with answer guidance)

1. **How do WAL and crash recovery relate to durability?**
   - *Answer guidance:* Log records are persisted before data pages, enabling redo/recovery of committed changes.
2. **Are backups a substitute for durability?**
   - *Answer guidance:* No; backups support recovery, but a committed transaction must survive ordinary crashes under the DBMS guarantee.
3. **Can configuration weaken durability?**
   - *Answer guidance:* Yes; asynchronous commit or relaxed flush policies may risk very recent commits in some failures.


---

