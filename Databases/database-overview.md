# Database Interview Prep Guide

## Overview

This guide is designed to be a practical, interview-focused database reference.
It covers both fundamentals and the kinds of tradeoffs interviewers expect you to understand in backend, full-stack, and system design interviews.

It is intentionally written in plain language first, then backed with technical detail.

---

## 1. What a Database Is

A database is an organized way to store, retrieve, update, and manage data.

In real systems, a database is usually paired with a DBMS:

- Database = the actual stored data
- DBMS = the software that manages the data

Examples of DBMSs:

- PostgreSQL
- MySQL
- SQLite
- MongoDB
- Redis
- DynamoDB
- Cassandra

Main things a database helps with:

- storing data safely
- finding data efficiently
- updating data consistently
- handling many users at once
- protecting data
- recovering from failures

---

## 2. Relational Databases vs NoSQL Databases

### Relational Databases

Relational databases store data in tables with rows and columns.

Examples:

- PostgreSQL
- MySQL
- SQL Server
- Oracle

Good for:

- structured data
- clear relationships
- transactions
- joins
- reporting
- strong consistency

Example:

- users
- orders
- payments
- invoices

These entities often relate tightly, which makes relational databases a strong fit.

### NoSQL Databases

NoSQL is a broad category. It includes:

- document databases
- key-value databases
- column-family databases
- graph databases

Examples:

- MongoDB
- Redis
- DynamoDB
- Cassandra
- Neo4j

Good for:

- flexible schemas
- very large scale
- simple access patterns
- specific workload shapes

### Interview Summary

Use relational databases when you need:

- transactions
- relationships
- reporting
- data integrity

Use NoSQL when you need:

- extreme scale
- schema flexibility
- simple key-based access
- special data models

Do not say one is always better.
Say the choice depends on:

- data shape
- consistency needs
- query patterns
- scale
- team familiarity

---

## 3. SQL Basics

SQL stands for Structured Query Language.

Common categories:

- DDL = Data Definition Language
- DML = Data Manipulation Language
- DCL = Data Control Language
- DQL = Data Query Language
- TCL = Transaction Control Language

### DDL

Used to define structure.

Examples:

- `CREATE`
- `ALTER`
- `DROP`
- `TRUNCATE`

### DML

Used to change data.

Examples:

- `SELECT` is often discussed separately under querying, but interview checklists sometimes still mention it alongside core SQL operations
- `INSERT`
- `UPDATE`
- `DELETE`
- `MERGE`
- `UPSERT`

### DQL

Used to query data.

Examples:

- `SELECT`
- filtering with `WHERE`
- sorting with `ORDER BY`
- grouping with `GROUP BY`
- aggregates like `COUNT`, `SUM`, `AVG`
- subqueries
- window functions

### DCL

Used to control access.

Examples:

- `GRANT`
- `REVOKE`

### TCL

Used to control transactions.

Examples:

- `BEGIN`
- `COMMIT`
- `ROLLBACK`

### Explicit vs Implicit Transactions

An explicit transaction is one you intentionally start and end yourself.

Example:

- `BEGIN`
- `UPDATE ...`
- `COMMIT`

An implicit transaction is started automatically by the database or client behavior.

Interview summary:

- explicit transactions give more control
- implicit transactions are simpler, but easier to overlook when debugging write behavior

### Control-of-Flow Language

Some SQL dialects and procedural SQL extensions support control flow like:

- `CASE`
- `IF`
- `IF-ELSE`

These are commonly used in:

- stored procedures
- functions
- complex data transformation logic

---

## 4. Schema Design

Schema design is how you organize your tables and relationships.

Key ideas:

- pick the right entities
- define relationships clearly
- avoid duplicated data unless there is a good reason
- choose correct data types
- enforce constraints where possible

Questions to ask:

- What are the core entities?
- How do they relate?
- Which fields are required?
- Which fields must be unique?
- Which queries will happen most often?

Example:

- `users`
- `orders`
- `order_items`
- `products`

This is a relational model because:

- one user can have many orders
- one order can have many items
- one product can appear in many orders

---

## 5. Keys and Constraints

### Primary Key

A primary key uniquely identifies a row.

Examples:

- `id`
- `user_id`
- UUID

Properties:

- unique
- not null

### Foreign Key

A foreign key links one table to another.

Example:

- `orders.user_id -> users.id`

This enforces referential integrity.

### Unique Constraint

Ensures a value appears only once.

Examples:

- email
- username
- external payment reference
- idempotency key

### Check Constraint

Ensures data follows a rule.

Examples:

- amount > 0
- status in allowed values

### Default Constraint

Supplies a default value if one is not given.

Examples:

- created_at = current timestamp
- status = pending

### Interview Summary

Constraints are not just for correctness.
They also reduce bugs and make data harder to corrupt.

---

## 6. Relationships

### One-to-One

One row in one table matches one row in another.

Example:

- users and user_profiles

### One-to-Many

One row relates to many rows.

Example:

- one user has many orders

### Many-to-Many

Many rows in one table relate to many rows in another.

Example:

- students and courses

Usually modeled with a join table:

- `student_courses`

---

## 7. Normalization

Normalization is the process of organizing data to reduce redundancy and improve consistency.

### 1NF

First Normal Form means:

- each column holds atomic values
- no repeating groups

### 2NF

Second Normal Form means:

- already in 1NF
- non-key columns depend on the full primary key

### 3NF

Third Normal Form means:

- already in 2NF
- non-key columns depend only on the key, not on other non-key columns

### BCNF

Boyce-Codd Normal Form is a stricter version of 3NF.

### Why Normalization Matters

It helps reduce:

- duplicated data
- inconsistent updates
- insertion anomalies
- deletion anomalies

### When to Denormalize

Sometimes you deliberately duplicate some data for:

- performance
- simpler reads
- analytics
- caching-like access patterns

Interview answer:

Normalize first for correctness, denormalize deliberately for performance when needed.

---

## 8. Joins

Joins combine rows from multiple tables.

### Inner Join

Returns only matching rows from both tables.

### Left Join

Returns all rows from the left table and matching rows from the right.

### Right Join

Returns all rows from the right table and matching rows from the left.

### Full Join

Returns all rows from both tables, matched where possible.

### Cross Join

Returns the Cartesian product.
Usually dangerous unless intentional.

### Interview Tip

Know when joins are useful, but also know that too many large joins can become expensive.

### Quick Join Summary

- inner join = only matching rows
- left join = all rows from the left table plus matches from the right
- right join = all rows from the right table plus matches from the left
- full join = all rows from both tables
- cross join = every row paired with every other row

---

## 9. Transactions

A transaction is a unit of work that should succeed completely or fail completely.

Example:

- create order
- charge payment
- reduce inventory
- write audit log

If step 3 fails, you may want the earlier steps rolled back.

That is what transactions help with.

### Common Commands

- `BEGIN`
- `COMMIT`
- `ROLLBACK`

---

## 10. ACID Properties

### Atomicity

All or nothing.

### Consistency

The database remains valid before and after the transaction.

### Isolation

Concurrent transactions should not interfere incorrectly.

### Durability

Once committed, data should survive crashes.

### Interview Summary

ACID is especially important for:

- payments
- orders
- financial systems
- inventory
- workflow state transitions

---

## 11. Isolation Levels

Isolation levels control how transactions interact with each other.

### Read Uncommitted

Weakest level.
Can read uncommitted changes.

Problem:

- dirty reads

### Read Committed

Common default in many systems.
Only reads committed data.

Still possible:

- non-repeatable reads

### Repeatable Read

If you read the same row twice in one transaction, you get the same result.

Still possible:

- phantom reads depending on database behavior

### Serializable

Strongest level.
Transactions behave as if run one by one.

Tradeoff:

- lower concurrency
- more locking or retries

### Common Interview Anomalies

- dirty read
- non-repeatable read
- phantom read
- lost update

---

## 12. Indexing

Indexes make lookups faster.

Without an index, the database may scan many rows.

With an index, it can locate matching rows much faster.

### Common Index Types

- B-tree
- B+ tree
- bitmap index
- hash index

### B-tree

A B-tree index is the most common general-purpose index in relational databases.
It works well for:

- equality lookups
- range queries
- ordered scans

### B+ tree

A B+ tree is closely related to a B-tree and is often used internally by database engines because leaf nodes are especially good for sequential access.

### Bitmap Indexing

Bitmap indexes are useful when:

- a column has low cardinality
- large analytical scans are common

Examples:

- status
- boolean flags
- small fixed categories

### Practical Examples

Good candidates for indexes:

- primary keys
- foreign keys
- email
- username
- created_at if often sorted
- status if heavily filtered

### Tradeoffs

Indexes improve:

- reads
- search
- filtering
- sorting

Indexes hurt:

- writes
- insert/update/delete speed
- storage usage

### Interview Summary

Do not say “index everything.”
Say:

- index the columns you query often
- avoid unnecessary indexes
- balance read and write costs

---

## 13. Query Optimization and Tuning

Slow queries often come from:

- missing indexes
- selecting too many columns
- too many joins
- unbounded scans
- bad filtering order
- N+1 query patterns

### Common improvements

- add the right index
- avoid `SELECT *`
- reduce result size with `LIMIT`
- paginate
- rewrite joins
- inspect query plans
- precompute expensive views where needed

### What to Know

- `EXPLAIN`
- query plan basics
- scan vs index lookup
- sort cost
- join cost

### Subqueries

A subquery is a query inside another query.

Common uses:

- filtering using values from another result set
- comparing against aggregate values
- correlated row-by-row checks

Interview note:

- know when a join is clearer than a subquery
- know that correlated subqueries can become expensive

### Aggregate Functions

Common aggregate functions include:

- `COUNT`
- `SUM`
- `AVG`
- `MIN`
- `MAX`

### GROUP BY and HAVING

`GROUP BY` is used to group rows before aggregation.

`HAVING` is used to filter grouped results after aggregation.

Simple distinction:

- `WHERE` filters rows before grouping
- `HAVING` filters groups after grouping

---

## 14. Views and Materialized Views

### View

A stored query that behaves like a virtual table.

Good for:

- simplifying repeated queries
- exposing restricted data shapes

### Materialized View

Stores the computed result physically.

Good for:

- expensive read-heavy reporting

Tradeoff:

- must be refreshed

### Advantages and Use Cases

#### Regular Views

Good for:

- simplifying repeated queries
- exposing a restricted subset of data
- making complex joins reusable

#### Materialized Views

Good for:

- dashboards
- reports
- precomputed aggregations
- expensive read-heavy queries

---

## 15. Stored Procedures, Functions, and Triggers

### Stored Procedures

Procedures stored in the database and executed there.

Key things to know:

- creation
- execution
- parameters

### Functions

Reusable logic that returns a value or set of values.

Key things to know:

- creation
- execution
- parameters
- return values

### Triggers

Logic that runs automatically:

- before insert
- after insert
- before update
- after delete

### Types of Triggers

Common trigger types include:

- `BEFORE`
- `AFTER`

These often apply to:

- `INSERT`
- `UPDATE`
- `DELETE`

### Trigger Execution Order

Interview answer:

- trigger execution order depends on the database engine
- if multiple triggers exist for the same event, the engine may define ordering rules
- avoid hiding too much business logic inside triggers

### Interview Guidance

Know what they are, but avoid saying everything belongs in the database.

Good answer:

- use them when they simplify consistency or audit behavior
- do not overuse them to hide too much business logic

---

## 16. SQL Query Topics to Know

### Core Query Skills

- filtering with `WHERE`
- sorting with `ORDER BY`
- grouping with `GROUP BY`
- filtering groups with `HAVING`
- subqueries
- CTEs
- window functions
- aggregates

### Window Functions

Important for advanced interview questions.

Examples:

- `ROW_NUMBER()`
- `RANK()`
- `DENSE_RANK()`
- running totals

### Upsert

Insert if not exists, otherwise update.

Very useful in:

- sync systems
- idempotent writes
- background jobs

---

## 17. NoSQL Types

### Document Databases

Store JSON-like documents.

Example:

- MongoDB

Good for:

- flexible schemas
- document-shaped data

### Key-Value Databases

Store values by key.

Examples:

- Redis
- DynamoDB

Good for:

- fast lookups
- sessions
- caches
- simple access patterns

### Column-Family Databases

Examples:

- Cassandra
- HBase

Good for:

- very large distributed workloads

### Graph Databases

Example:

- Neo4j

Good for:

- highly connected data
- relationship-heavy queries

### Examples

- document-based: MongoDB
- key-value: Redis, DynamoDB
- column-family: Cassandra, HBase
- graph: Neo4j

### MongoDB Interview Questions

Common MongoDB interview questions include:

- When would you choose MongoDB over PostgreSQL?
- What makes the document model useful?
- What are collections and documents?
- How does indexing work in MongoDB?
- What are the tradeoffs of schema flexibility?
- When are embedded documents better than references?

### Redis Interview Questions

Common Redis interview questions include:

- What type of database is Redis?
- When would you use Redis instead of PostgreSQL?
- What data structures does Redis support?
- How is Redis used for caching?
- How is Redis used for queues, pub-sub, or rate limiting?
- What are the risks of putting too much critical state only in cache?

---

## 18. CAP, BASE, and Eventual Consistency

### CAP Theorem

In a distributed system, you usually reason about:

- Consistency
- Availability
- Partition tolerance

You cannot fully optimize all three in the presence of network partitions.

### BASE

- Basically Available
- Soft state
- Eventual consistency

BASE systems often trade strict consistency for availability and scale.

### Eventual Consistency

Reads may temporarily lag behind writes, but the system converges over time.

Interview note:

Eventual consistency can be acceptable for:

- feeds
- analytics
- replicated read models

It is less acceptable for:

- payments
- balance updates
- critical workflow states

---

## 19. Replication

Replication means keeping copies of data on multiple machines.

### Why use it

- better read scaling
- redundancy
- failover

### Primary/Replica Pattern

- primary handles writes
- replicas often serve reads

### Tradeoff

- replicas can lag
- recent writes may not appear immediately

Interview answer:

Use replicas when read traffic is high, but understand replication lag.

---

## 20. Partitioning and Sharding

### Partitioning

Splitting data into smaller parts for manageability or performance.

### Sharding

Distributing data across multiple database instances.

### Why do it

- scale beyond one machine
- reduce hot spots
- improve throughput

### Problems

- cross-shard joins become hard
- rebalancing is hard
- operational complexity increases

Interview guidance:

Do not propose sharding too early unless the scale really demands it.

## 20A. Database Design and Optimization

Database design and optimization usually includes:

- schema design
- normalization and denormalization
- indexing
- query tuning
- partitioning
- materialized views
- choosing the right constraints
- choosing the right database for the workload

Interview summary:

- correct design comes first
- optimization follows real workload patterns

---

## 21. Relational vs NoSQL Decision-Making

This is a very common interview question.

### Choose SQL when:

- schema is structured
- transactions matter
- consistency matters
- joins matter
- reporting matters

### Choose NoSQL when:

- schema changes often
- scale is very large
- access patterns are simple and known
- denormalization is acceptable
- low-latency key access matters

### Good Interview Language

Do not answer with preference alone.
Say:

- "I would choose based on access patterns, consistency needs, schema shape, and operational complexity."

---

## 22. PostgreSQL vs DynamoDB

This is a useful practical comparison.

### PostgreSQL

Best for:

- relational workflows
- transactions
- joins
- reporting
- constraints
- flexible querying

### DynamoDB

Best for:

- very large scale
- simple, predictable access patterns
- key-based lookups
- serverless-friendly architectures

### Why PostgreSQL Often Wins Early

- easier to reason about
- easier to query
- better for changing product requirements
- stronger default for operational systems

### Why DynamoDB Can Win

- huge scale
- simple workload
- low operational overhead if modeled well

### Interview Summary

Use PostgreSQL for:

- product systems
- admin dashboards
- workflow engines
- reporting

Use DynamoDB for:

- access-pattern-first workloads
- extreme scale
- key-value heavy systems

---

## 23. Primary Keys, Unique Constraints, Idempotency, and Retries

This is very important for backend interviews.

### Primary Keys

Used to uniquely identify rows.

### Unique Constraints

Used to prevent duplicates.

Very useful for:

- emails
- usernames
- external references
- idempotency keys

### Idempotency

If a request is retried, it should not accidentally create duplicate side effects.

Examples:

- payment creation
- order creation
- webhook processing

### Database Support for Idempotency

You often use:

- a unique constraint
- an idempotency key table
- transaction-safe lookup and insert logic

### Why Retries Need Idempotency

Because distributed systems retry on:

- timeout
- temporary failure
- unknown response state

Without idempotency:

- duplicate charges
- duplicate orders
- duplicate webhooks

Interview summary:

- retries should be paired with idempotency
- databases often help enforce that through unique constraints

---

## 24. ACID and Consistency in Real Backend Systems

Example:

Creating an order may require:

- insert order row
- reserve inventory
- insert payment record
- insert audit log

Why ACID matters:

- if one step fails, state should not become corrupted

### Practical consistency questions

Ask:

- does this need to be strongly consistent?
- can this be eventually consistent?
- can I use a transaction?
- do I need an outbox/event pattern?

---

## 25. Database Security Basics

Know these for interviews:

- least privilege
- `GRANT` / `REVOKE`
- credential management
- secret rotation
- encryption at rest
- encryption in transit
- SQL injection prevention
- parameterized queries
- audit logging

Never store secrets directly in source code.

---

## 26. Backup, Recovery, and Durability

Databases must survive failures.

Important ideas:

- backups
- replication
- snapshots
- point-in-time recovery
- write-ahead logging

Questions interviewers may ask:

- how would you recover from accidental deletion?
- how do you protect against disk failure?
- how do you plan disaster recovery?

---

## 27. Common Database Interview Questions

### Fundamentals

- What is a database?
- What is a DBMS?
- Difference between SQL and NoSQL?
- What is normalization?
- What is denormalization?
- Difference between primary key and unique key?
- What is a foreign key?

### SQL

- Difference between `WHERE` and `HAVING`?
- Difference between inner join and left join?
- What are window functions?
- What is an index?
- Why can too many indexes be bad?

### Transactions

- What is ACID?
- What is a transaction?
- What is an isolation level?
- What are dirty reads and phantom reads?

### Systems

- When would you use PostgreSQL vs DynamoDB?
- What is replication?
- What is sharding?
- What is eventual consistency?
- How do retries and idempotency work together?

---

## 28. How to Answer Database Questions Well

Strong answers usually include:

- definition
- why it matters
- tradeoffs
- real example

Example:

"An index speeds up reads by allowing the database to locate rows more efficiently, but it increases write cost and storage usage, so I add indexes based on real query patterns rather than by default."

That is much better than:

"An index makes queries faster."

---

## 29. Recommended Study Path

### Phase 1

- what a database is
- DBMS
- SQL basics
- schema design
- keys and constraints
- normalization
- joins

### Phase 2

- transactions
- ACID
- isolation levels
- indexing
- query optimization
- views
- triggers and procedures

### Phase 3

- NoSQL types
- CAP / BASE
- replication
- partitioning
- PostgreSQL vs DynamoDB
- idempotency and retries
- backup and recovery

### Phase 4

- solve interview questions
- write SQL queries
- explain tradeoffs out loud
- connect database decisions to backend/system design

---

## 30. Recommended Book and Resource

### Best Core Book

**Database System Concepts** by Abraham Silberschatz, Henry F. Korth, and S. Sudarshan

Why it is a strong choice:

- foundational
- respected textbook
- covers relational databases, transactions, indexing, query processing, storage, concurrency, and recovery
- broad enough for both interviews and long-term understanding

Recommended repo-friendly way to add it:

- add the title and an official publisher or catalog link
- do not upload a copyrighted PDF into the repository unless you have permission

### Free Legal Companion Resource

**Readings in Database Systems** by Joseph M. Hellerstein and Michael Stonebraker

Why it is useful:

- strong for deeper database systems thinking
- great once you move past basics
- useful for distributed data systems and internals

---

## 31. Suggested Resource Section for the Repository

You can add something like this:

```md
## Recommended Database Resources

- **Database System Concepts** by Abraham Silberschatz, Henry F. Korth, and S. Sudarshan
  - Strong foundational database textbook covering relational design, SQL, transactions, indexing, query processing, concurrency, and recovery.

- **Readings in Database Systems**
  - Great follow-up resource for deeper database systems thinking and modern database architecture concepts.
```

---

## 32. Final Interview Advice

For interviews, do not study databases as just SQL syntax.

Study them as:

- data modeling
- consistency
- performance
- concurrency
- scalability
- reliability
- tradeoffs

If you can explain:

- why one schema is better than another
- why one database fits a use case better than another
- why retries need idempotency
- why indexes help but also cost something

then you will sound much stronger than someone who only memorized commands.
