# SQL Data Control Language (DCL)

**Track:** SQL Data Control Language (DCL) · **Priority:** `P0`

> **Core idea:** DCL manages database permissions. In practice, enforce least privilege: give services only the table/schema actions they require, not administrative rights.


## Detailed theory

DCL determines **who can do what** with database objects. Core statements: `GRANT` and `REVOKE`. Privileges commonly include `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `REFERENCES`, `USAGE`, `EXECUTE`, or object-level actions depending on the DBMS.

## Principle of least privilege
Create roles aligned to responsibility (read-only analyst, app writer, schema migrator). Grant only necessary permissions, preferably via roles rather than individually to each user. Separate application and migration accounts. Treat credentials and privileged actions as security-sensitive.

```sql
-- PostgreSQL-style example (syntax varies)
CREATE ROLE reporting_reader;
GRANT USAGE ON SCHEMA public TO reporting_reader;
GRANT SELECT ON TABLE public.orders TO reporting_reader;
GRANT reporting_reader TO analyst_user;
```

## Security details to understand
- Users vs roles (whether interchangeable depends on database).
- Object ownership, inherited membership and effective privileges.
- Object grants versus row-level security (RLS) / column-specific privileges.
- Default privileges for future tables can differ from existing-object grants.
- `REVOKE` may not remove access inherited through another role or `PUBLIC`.
- Parameterized queries prevent SQL injection; DCL is **not** a substitute.

**Interview prompt:** A service only needs to read orders. Why should it not use the admin account? What would you inspect if REVOKE seems ineffective?

## Worked example — understand the *why*

```sql
CREATE ROLE reporting_reader;
GRANT SELECT ON TABLE orders TO reporting_reader;
REVOKE SELECT ON TABLE orders FROM reporting_reader;
```
Role-management syntax and permission inheritance differ by engine; these examples follow PostgreSQL style.

## Possible interview questions (with answer guidance)

1. **Why use roles rather than individually assigning every permission?**
   - *Answer guidance:* Simpler auditing, onboarding, and consistent least-privilege enforcement.
2. **What is least privilege?**
   - *Answer guidance:* Only permissions necessary for a workload and no broader.
3. **How is database authorization different from application authentication?**
   - *Answer guidance:* Authentication verifies identity; authorization decides permitted operations.


---

