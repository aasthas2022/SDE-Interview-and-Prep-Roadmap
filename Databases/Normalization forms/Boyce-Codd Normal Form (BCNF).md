# Boyce-Codd Normal Form (BCNF)

**Track:** Normalization forms · **Priority:** `P0`

> **Core idea:** BCNF is stronger than 3NF: for every nontrivial functional dependency X → Y, X must be a superkey. It removes certain anomalies 3NF can permit.


## Detailed theory

A relation is in **BCNF** if for **every nontrivial functional dependency** `X → Y`, the determinant X is a **superkey**. This is stricter than 3NF, which permits some dependencies with a prime attribute on the right.

## Classic 3NF-but-not-BCNF example
Consider `Teaching(student, course, instructor)` under assumptions:
1. A student may take a course with one instructor: `(student, course) → instructor`.
2. Each instructor teaches exactly one course: `instructor → course`.
Candidate keys are `(student, course)` and `(student, instructor)`; every attribute is prime. Therefore 3NF holds, but `instructor → course` violates BCNF because instructor alone is not a superkey.

Decompose into:
- `InstructorCourse(instructor, course)`
- `StudentInstructor(student, instructor)`
The decomposition is lossless under these dependencies, but `(student, course) → instructor` may not be enforceable using constraints on individual decomposed relations (dependency-preservation issue).

**Tradeoff:** BCNF reduces FD-driven redundancy; 3NF is sometimes chosen because a dependency-preserving, lossless decomposition is desired.

**Interview prompt:** What does BCNF add beyond 3NF? Give an example where 3NF allows a dependency whose determinant is not a key.

## Worked example — understand the *why*

```text
Relation: Teaching(student, course, instructor)
Assume each instructor teaches exactly one course:
instructor -> course
Assume a student can take the course with one instructor:
(student, course) -> instructor
The determinant instructor need not be a superkey -> BCNF violation.
Possible split: InstructorCourse(instructor, course)
                StudentInstructor(student, instructor)
```
A BCNF decomposition can sacrifice dependency preservation. Carefully state assumptions: normalization is based on *business rules*, not just current sample data.

## Possible interview questions (with answer guidance)

1. **BCNF vs 3NF?**
   - *Answer guidance:* BCNF requires every nontrivial FD determinant to be a superkey; 3NF has a prime-attribute exception.
2. **Can BCNF decomposition lose dependency preservation?**
   - *Answer guidance:* Yes, although a lossless decomposition can still exist.
3. **Why must you establish candidate keys first?**
   - *Answer guidance:* Normal-form classification depends on the implied functional dependencies and keys.


---

