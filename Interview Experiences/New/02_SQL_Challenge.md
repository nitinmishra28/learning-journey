# Elastiq.ai - Python Developer Assessment

## Question 2: MySQL Challenge - Vendor Information

**Company:** Elastiq.ai  
**Role:** Python Developer  
**Assessment Type:** Quick Online Assessment  
**Category:** SQL / MySQL  

---

## Problem Statement

Write a MySQL query that combines vendor information with values from:

```text
cb_vendorinformation
```

The two tables should be combined based on the:

```text
GroupID
```

column.

The final result should display only:

```text
GroupID
CompanyName
Count
```

Where:

- `GroupID` represents the vendor group.
- `CompanyName` represents the corresponding company.
- `Count` represents the total number of rows grouped under each company.

The count column must be named:

```sql
Count
```

---

## Sorting Requirements

The final output should first be sorted by:

```text
Count
```

with higher values appearing first.

If multiple rows have the same count, sort them by:

```text
GroupID
```

with the higher `GroupID` appearing first.

Conceptually:

```sql
ORDER BY Count DESC, GroupID DESC
```

---

## Concepts Used

```text
JOIN
GROUP BY
COUNT()
ORDER BY
Aliases
```

---

## Query Flow

The expected approach is:

```text
Table 1
    +
cb_vendorinformation
    |
    | JOIN using GroupID
    ↓
Combined Data
    |
    | GROUP BY GroupID and CompanyName
    ↓
Count Rows
    |
    | ORDER BY Count DESC
    | ORDER BY GroupID DESC
    ↓
Final Result
```

---

## Expected Output Columns

```text
+---------+-------------+-------+
| GroupID | CompanyName | Count |
+---------+-------------+-------+
|   ...   |     ...     |  ...  |
+---------+-------------+-------+
```

---

## Important SQL Concepts

### JOIN

Used to combine the two tables based on:

```sql
GroupID
```

### GROUP BY

Used to group records belonging to the same company.

### COUNT()

Used to calculate how many records belong to each group.

### ORDER BY

Used to sort the final result by:

1. Count descending
2. GroupID descending

---

## Pattern

```text
JOIN + GROUP BY + Aggregation + Multi-Column Sorting
```

---

## Key Takeaways

- Identify the common column between the tables.
- Use the correct JOIN based on the expected output.
- Use `COUNT()` with `GROUP BY` for aggregated results.
- Alias the aggregate column as `Count`.
- Apply multiple sorting conditions in the required priority order.