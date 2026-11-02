# REVOKE statement

**Track:** SQL Data Control Language (DCL) · **Priority:** `P0`

> **Core idea:** REVOKE removes a previously granted privilege, but effective access can remain through other roles or PUBLIC grants.


## Detailed theory

`REVOKE` withdraws previously granted privileges. Effective access can remain through other roles, `PUBLIC`, ownership, higher privileges, or database-specific rules.

```sql
-- PostgreSQL-style
REVOKE INSERT, UPDATE, DELETE ON public.orders FROM reporting_reader;
REVOKE SELECT ON public.orders FROM reporting_reader;
```

**Trap:** Revoking access from a directly named user does not necessarily block it if the user belongs to another role that still has access. Some databases support grant options and cascade/restrict semantics for dependent grants.

**Interview prompt:** You revoked `SELECT` but a user can still read the table. What would you investigate? Answer: inherited roles, PUBLIC, ownership, alternative granted paths, connection identity.

## Worked example — understand the *why*

```sql
REVOKE UPDATE ON TABLE orders FROM reporting_reader;
REVOKE SELECT ON TABLE orders FROM PUBLIC;
```
Always audit inherited permissions and default grants. Some DBMSs support grant options and cascading effects; syntax varies.

## Possible interview questions (with answer guidance)

1. **Does REVOKE guarantee the user loses all access?**
   - *Answer guidance:* No; other inherited or public permissions may still grant it.
2. **What is PUBLIC in PostgreSQL grants?**
   - *Answer guidance:* A special pseudo-role representing all roles.
3. **What should be checked after revoking access?**
   - *Answer guidance:* Effective permissions via group roles, ownership, public grants, and future defaults.


---

