# Second Normal Form (2NF)

**Track:** Normalization forms · **Priority:** `P0`

> **Core idea:** 2NF requires 1NF and no non-prime attribute depending on a proper subset of any candidate key. Partial dependencies matter when candidate keys have multiple attributes.


## Detailed theory

A relation is in **2NF** if it is in 1NF and **every non-prime attribute is fully functionally dependent on every candidate key** (no partial dependency on a proper subset of a candidate key).

Example with composite candidate key `(student_id, course_id)`:
```text
Enrollment(student_id, course_id, student_name, course_title, grade)
```
- `student_id → student_name` (partial dependency)
- `course_id → course_title` (partial dependency)
- `(student_id, course_id) → grade` (full dependency)

Decompose to `Students(student_id, student_name)`, `Courses(course_id, course_title)`, `Enrollments(student_id, course_id, grade)`.

**Important nuance:** A relation with only one **single-column** candidate key cannot have a partial-key dependency on that key, but still can violate 3NF due to transitive dependencies. Also, a 2NF relation can have multiple candidate keys.

**Interview prompt:** What is a partial functional dependency? Why is a composite key a common teaching example for 2NF?

## Worked example — understand the *why*

```text
Bad: Enrollment(student_id, course_id, student_name, grade)
Key: (student_id, course_id)
student_id -> student_name  [partial dependency]
Better: Students(student_id, student_name)
        Enrollment(student_id, course_id, grade)
```
`grade` depends on the whole enrollment key, while `student_name` depends on only student_id.

## Possible interview questions (with answer guidance)

1. **Why is a single-column candidate key table usually already in 2NF if 1NF?**
   - *Answer guidance:* No proper nonempty subset of a single-attribute key can determine a non-prime attribute.
2. **Give a partial dependency example.**
   - *Answer guidance:* (student_id, course_id) → grade, but student_id → student_name.
3. **What issue does 2NF fix?**
   - *Answer guidance:* Redundant non-key facts tied to part of a composite key.


---

