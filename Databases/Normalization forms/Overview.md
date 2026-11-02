# Normalization forms

**Track:** Normalization forms · **Priority:** `P0`

> **Core idea:** Normalization organizes tables around functional dependencies to reduce update, insert, and delete anomalies. Learn what each normal form *prevents*, not only its slogan.


## Detailed theory

Normalization systematically structures relational tables to reduce redundancy and **update, insert, delete anomalies**, guided by **functional dependencies (FDs)**.

An FD `X → Y` means that for any two rows agreeing on X, their Y values must agree (under the intended semantics). A **superkey** uniquely identifies all columns; a **candidate key** is a minimal superkey. A **prime attribute** belongs to some candidate key.

## Running example
Bad design: `Enrollments(student_id, student_name, course_id, course_title, instructor_id, instructor_name, grade)` with key `(student_id, course_id)`.
- `student_id → student_name`
- `course_id → course_title, instructor_id`
- `instructor_id → instructor_name`
- `(student_id, course_id) → grade`
Student name and course title repeat. Changing an instructor name requires many updates; deleting the final enrollment could discard course information.

Better decomposition:
```text
Students(student_id PK, student_name)
Instructors(instructor_id PK, instructor_name)
Courses(course_id PK, course_title, instructor_id FK)
Enrollments(student_id FK, course_id FK, grade,
            PK(student_id, course_id))
```

## Normal forms (informal ladder)
1. **1NF:** each field holds one value from its domain; no repeating groups.
2. **2NF:** in 1NF, non-prime attributes have no dependency on a proper subset of any candidate key.
3. **3NF:** for every nontrivial FD `X → A`, X is a superkey **or** A is prime.
4. **BCNF:** for every nontrivial FD `X → Y`, X is a superkey. Stronger than 3NF.

## Tradeoffs
Normalization increases data integrity, clarity, and flexibility; it can require more joins. Denormalization may speed read-heavy workloads but increases synchronization obligations. Normalization is not an automatic replacement for thoughtful indexing or workload-specific design.

## Two formal goals of decomposition
- **Lossless join:** recombining the decomposed relations does not create spurious rows or lose information.
- **Dependency preservation:** original constraints can be enforced on individual resulting relations without joins; a BCNF decomposition may fail to preserve every FD, motivating 3NF in some designs.

**Interview prompt:** Demonstrate one update anomaly and decompose a table to 3NF. Why might BCNF sacrifice dependency preservation?

## Worked example — understand the *why*

```text
Bad: order_id | customer_name | customer_email | product_id | product_name
Better:
Customers(customer_id, customer_name, customer_email)
Products(product_id, product_name)
Orders(order_id, customer_id)
OrderItems(order_id, product_id, quantity)
```
Repeated customer/product facts risk contradictory updates. Normalization has trade-offs: additional joins may be needed. Denormalize deliberately when justified by measured access patterns.

## Possible interview questions (with answer guidance)

1. **What are update, insert, and delete anomalies?**
   - *Answer guidance:* Inconsistent duplicate facts; unable to add an independent fact; deleting one row accidentally loses another fact.
2. **Do normalized schemas always run faster?**
   - *Answer guidance:* No; they generally improve integrity and maintainability, but joins and access patterns matter.
3. **What is a functional dependency X → Y?**
   - *Answer guidance:* Every pair of rows with the same X must have the same Y.


---

