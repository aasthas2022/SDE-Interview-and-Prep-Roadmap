# GRANT statement

**Track:** SQL Data Control Language (DCL) · **Priority:** `P0`

> **Core idea:** GRANT assigns a privilege to a user or role. Its exact privilege types and grantable objects depend on the DBMS.


## Detailed theory

`GRANT` gives specified privileges to a role or user on database objects. The exact permissions, syntax, and role model vary by DBMS.

```sql
-- PostgreSQL examples
GRANT SELECT ON public.orders TO reporting_reader;
GRANT INSERT, UPDATE ON public.orders TO order_service;
GRANT USAGE ON SCHEMA public TO reporting_reader;
GRANT EXECUTE ON FUNCTION calculate_tax(numeric) TO order_service;
```

**Privileges are scoped:** reading a table is not modifying it; accessing the schema may require separate privileges. Granting on today's table does **not** necessarily apply to new tables created tomorrow; learn your database's default-privilege facilities.

**Interview prompt:** How would you give a dashboard read-only access to a specific reporting schema while preventing writes?

## Worked example — understand the *why*

```sql
GRANT USAGE ON SCHEMA public TO reporting_reader;
GRANT SELECT ON TABLE orders TO reporting_reader;
-- PostgreSQL: access to a schema and a table are distinct.
```
Be precise about schema USAGE, table SELECT, sequence permissions, and default privileges for newly created objects.

## Possible interview questions (with answer guidance)

1. **Is GRANT SELECT enough if schema access is absent?**
   - *Answer guidance:* Not necessarily; PostgreSQL also needs USAGE on the schema.
2. **Why avoid GRANT ALL?**
   - *Answer guidance:* It grants more power than typical applications need.
3. **How would you create a read-only analytics role?**
   - *Answer guidance:* Grant schema access and SELECT only on required tables/views, then test access.


---

