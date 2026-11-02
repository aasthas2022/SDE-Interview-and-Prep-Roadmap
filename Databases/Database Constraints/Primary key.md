# Primary key

**Track:** Database Constraints · **Priority:** `P1`

> **Core idea:** A PRIMARY KEY is the table’s chosen unique non-null identifier. It may consist of one column or multiple columns.


## Detailed theory

The primary key is the **chosen unique non-NULL identifier** of rows. Exactly one PK constraint per table, but it may span multiple columns.

```sql
CREATE TABLE enrollments (
  student_id BIGINT NOT NULL REFERENCES students(id),
  course_id BIGINT NOT NULL REFERENCES courses(id),
  enrolled_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (student_id, course_id)
);
```

**Natural key** uses meaningful domain fields; **surrogate key** is generated or assigned solely for identity. Surrogate keys simplify reference stability but may need additional `UNIQUE` domain constraints.

**Common trap:** A PK is not guaranteed to dictate physical row storage order. Index/cluster details are vendor-specific. A PK does not imply a column is an integer or auto-incrementing.

**Interview prompt:** How would you represent one student's enrollment in one course at most once? Would you still need uniqueness with a surrogate enrollment ID?

## Worked example — understand the *why*

```sql
CREATE TABLE enrollment (
 student_id BIGINT NOT NULL,
 course_id BIGINT NOT NULL,
 enrolled_at TIMESTAMP NOT NULL,
 PRIMARY KEY(student_id, course_id)
);
```
A composite key makes a pair unique. A surrogate id is convenient, but a separate UNIQUE constraint may still be needed for a natural business key.

## Possible interview questions (with answer guidance)

1. **Can a table have two primary keys?**
   - *Answer guidance:* No, one primary-key constraint, which may contain multiple columns.
2. **Primary key versus unique constraint?**
   - *Answer guidance:* Primary key is designated non-null row identity; UNIQUE enforces an alternate candidate key with DB-specific NULL behavior.
3. **Surrogate versus natural key?**
   - *Answer guidance:* Surrogate is generated/stable identity; natural key reflects business meaning but may change.


---

