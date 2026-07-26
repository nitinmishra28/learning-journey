# 🔷 Python Set Operations

Python sets support mathematical set operations such as:

* Union
* Intersection
* Difference
* Symmetric Difference
* Subset
* Superset
* Disjoint Set

These operations are one of the biggest reasons to use sets.

---

# Overview

| Operation            | Symbol | Method                   |
| -------------------- | ------ | ------------------------ |
| Union                | `\|`   | `union()`                |
| Intersection         | `&`    | `intersection()`         |
| Difference           | `-`    | `difference()`           |
| Symmetric Difference | `^`    | `symmetric_difference()` |

---

# Union

A union contains **all unique elements** from both sets.

Example

```python
A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)
```

Output

```
{1, 2, 3, 4, 5}
```

Duplicates appear only once.

---

## Using `union()`

```python
A = {1, 2}
B = {3, 4}

print(A.union(B))
```

Output

```
{1, 2, 3, 4}
```

---

## Multiple Sets

```python
A = {1}
B = {2}
C = {3}

print(A.union(B, C))
```

Output

```
{1, 2, 3}
```

---

## Complexity

```
Time : O(len(A) + len(B))

Space : O(len(A) + len(B))
```

---

# Intersection

Returns elements present in **both** sets.

```python
A = {1, 2, 3}
B = {2, 3, 4}

print(A & B)
```

Output

```
{2, 3}
```

---

## Using `intersection()`

```python
print(A.intersection(B))
```

Output

```
{2, 3}
```

---

## Multiple Sets

```python
A = {1,2,3}
B = {2,3,4}
C = {3,4,5}

print(A.intersection(B,C))
```

Output

```
{3}
```

---

## Complexity

```
Average O(min(len(A), len(B)))
```

Python generally iterates over the smaller set for efficiency.

---

# Difference

Returns elements present in the first set but **not** in the second.

```python
A = {1,2,3}
B = {2,3,4}

print(A - B)
```

Output

```
{1}
```

---

```python
print(B - A)
```

Output

```
{4}
```

Difference is **not symmetric**.

---

## Using `difference()`

```python
print(A.difference(B))
```

---

## Complexity

```
Average O(len(A))
```

---

# Symmetric Difference

Returns elements that appear in **exactly one** of the sets.

```python
A = {1,2,3}
B = {2,3,4}

print(A ^ B)
```

Output

```
{1,4}
```

Common elements are removed.

---

## Using `symmetric_difference()`

```python
print(A.symmetric_difference(B))
```

---

## Complexity

```
Average O(len(A) + len(B))
```

---

# Subset

A subset means **every element** of one set exists in another.

```python
A = {1,2}
B = {1,2,3}

print(A <= B)
```

Output

```
True
```

---

## Using `issubset()`

```python
print(A.issubset(B))
```

Output

```
True
```

---

## Proper Subset

```python
print(A < B)
```

Output

```
True
```

Proper subset means

* A is a subset of B
* A and B are **not equal**

---

# Superset

A superset contains every element of another set.

```python
A = {1,2,3}
B = {1,2}

print(A >= B)
```

Output

```
True
```

---

## Using `issuperset()`

```python
print(A.issuperset(B))
```

---

## Proper Superset

```python
print(A > B)
```

Returns `True` only if A has additional elements.

---

# Disjoint Sets

Two sets are disjoint if they have **no common elements**.

```python
A = {1,2}
B = {3,4}

print(A.isdisjoint(B))
```

Output

```
True
```

---

Example

```python
A = {1,2}
B = {2,3}

print(A.isdisjoint(B))
```

Output

```
False
```

---

# In-place Operations

These modify the original set.

---

## `update()`

Equivalent to

```python
A |= B
```

Example

```python
A = {1,2}
B = {2,3}

A.update(B)

print(A)
```

Output

```
{1,2,3}
```

---

## `intersection_update()`

Equivalent to

```python
A &= B
```

Example

```python
A = {1,2,3}
B = {2,3,4}

A.intersection_update(B)

print(A)
```

Output

```
{2,3}
```

---

## `difference_update()`

Equivalent to

```python
A -= B
```

Example

```python
A = {1,2,3}
B = {2}

A.difference_update(B)

print(A)
```

Output

```
{1,3}
```

---

## `symmetric_difference_update()`

Equivalent to

```python
A ^= B
```

Example

```python
A = {1,2,3}
B = {2,3,4}

A.symmetric_difference_update(B)

print(A)
```

Output

```
{1,4}
```

---

# New Set vs In-place

```python
A | B
```

Returns a **new** set.

Original sets remain unchanged.

---

```python
A |= B
```

Updates the original set.

---

| Operation     | New Set | Modify Original |   |
| ------------- | ------- | --------------- | - |
| `A \| B`      | ✅       | ❌               |   |
| `A.union(B)`  | ✅       | ❌               |   |
| `A            | = B`    | ❌               | ✅ |
| `A.update(B)` | ❌       | ✅               |   |

---

# Operator Summary

| Operator | Meaning              |
| -------- | -------------------- |
| `\|`     | Union                |
| `&`      | Intersection         |
| `-`      | Difference           |
| `^`      | Symmetric Difference |
| `<=`     | Subset               |
| `<`      | Proper Subset        |
| `>=`     | Superset             |
| `>`      | Proper Superset      |

---

# DSA Applications

## Union

Merge two unique collections.

```python
users = active | premium
```

---

## Intersection

Find common elements.

Examples

* Common friends
* Common skills
* Common characters

```python
common = A & B
```

---

## Difference

Find missing elements.

```python
missing = expected - received
```

---

## Symmetric Difference

Find elements that differ.

```python
changed = old ^ new
```

---

## Subset

Permission checking

```python
required <= user_permissions
```

---

## Disjoint

Check if two groups overlap.

```python
admins.isdisjoint(banned)
```

---

# Common Mistakes

❌

Thinking

```python
A - B
```

is the same as

```python
B - A
```

Difference depends on order.

---

❌

Using

```python
A |= B
```

when a new set is needed.

It modifies `A`.

---

❌

Confusing

```python
^
```

with exponentiation.

For sets,

```python
^
```

means **Symmetric Difference**.

---

❌

Thinking subset means equal size.

```python
{1,2} <= {1,2}
```

is `True`.

Use `<` for a proper subset.

---

# Interview Questions

1. Difference between union and update?
2. Difference between intersection and intersection_update()?
3. Difference between subset and proper subset?
4. Difference between superset and proper superset?
5. Difference between `-` and `^`?
6. What does `isdisjoint()` do?
7. Which operation finds common elements?
8. Which operation removes common elements?
9. Why are set operations useful in DSA?

---

# Quick Revision

✔ Union combines unique elements.

✔ Intersection returns common elements.

✔ Difference removes elements from the first set.

✔ Symmetric Difference keeps only different elements.

✔ Subset means every element exists in another set.

✔ Superset contains another set completely.

✔ Disjoint sets have no common elements.

✔ Operators like `|=`, `&=`, `-=`, `^=` modify the original set.

✔ Operators like `|`, `&`, `-`, `^` return new sets.
