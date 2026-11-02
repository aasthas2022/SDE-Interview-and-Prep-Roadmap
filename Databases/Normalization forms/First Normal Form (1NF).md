# First Normal Form (1NF)

**Track:** Normalization forms · **Priority:** `P0`

> **Core idea:** 1NF requires attributes to hold single values from their domains rather than repeating lists or groups. Avoid comma-separated arrays of relational entities.


## Detailed theory

A table is in **1NF** when attributes take single values from their defined domains rather than holding repeating groups (e.g. `phone1`, `phone2`, `phone3`) or lists of independent values in a cell. In the formal relational model, values are atomic relative to the domain: whether a string/JSON value is “atomic” depends on its intended use.

Bad:
```text
customers(id, name, phone_numbers='555-1000,555-2000')
```
Better:
```text
customers(id PK, name)
customer_phones(customer_id FK, phone, PK(customer_id, phone))
```

**Caveat:** SQL tables generally require typed scalar columns, but storing CSV data inside a text field can still violate good 1NF modeling when each entry is logically a separate phone number. Modern JSON arrays can be valid engineering choices for some access patterns; assess query/integrity needs.

**Interview prompt:** Why does a comma-delimited tags column make filtering and FK enforcement harder?

## Worked example — understand the *why*

```text
Bad: customer_id | phone_numbers
     1           | 555-1000,555-2000
Better: CustomerPhones(customer_id, phone_number)
        (1,555-1000), (1,555-2000)
```
A JSON or array column can be valid in real systems, but storing searchable relational members in a separate table usually makes constraints and queries cleaner.

## Possible interview questions (with answer guidance)

1. **Does 1NF automatically remove duplicate rows?**
   - *Answer guidance:* The relational model uses unique tuples; in SQL explicitly enforce keys to avoid duplicates.
2. **Why are comma-separated IDs a problem?**
   - *Answer guidance:* Hard to enforce foreign keys, update one member, or index membership efficiently.
3. **Does 1NF mean every table needs an auto-increment ID?**
   - *Answer guidance:* No; a natural or composite key may identify rows.


---

