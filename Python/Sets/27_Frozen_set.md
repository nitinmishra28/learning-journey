# 🔷 Frozen Sets and Internal Working

This chapter covers the advanced concepts of Python sets that are useful for interviews, backend development, and DSA.

Topics covered:

* `frozenset`
* Hashability
* Internal Working
* Hash Table
* Time Complexity
* Performance
* DSA Patterns
* Best Practices

---

# What is a `frozenset`?

A **frozenset** is an immutable version of a set.

Just like:

* List → Tuple
* Set → FrozenSet

Once created, a frozenset **cannot be modified**.

---

# Creating a FrozenSet

## Syntax

```python
frozenset(iterable)
```

Example

```python
numbers = frozenset([1, 2, 3])

print(numbers)
```

Output

```
frozenset({1, 2, 3})
```

---

# Empty FrozenSet

```python
empty = frozenset()

print(empty)
```

Output

```
frozenset()
```

---

# Immutability

```python
numbers = frozenset([1, 2, 3])

numbers.add(4)
```

Output

```
AttributeError
```

A frozenset has no methods that modify it.

---

# Methods Not Available

These methods do **not** exist.

```python
add()

remove()

discard()

update()

clear()

pop()

difference_update()

intersection_update()

symmetric_difference_update()
```

Because the object is immutable.

---

# Operations That Still Work

Although immutable, frozensets still support mathematical operations.

```python
A = frozenset({1, 2})
B = frozenset({2, 3})

print(A | B)
```

Output

```
frozenset({1, 2, 3})
```

A **new** frozenset is returned.

---

Intersection

```python
print(A & B)
```

Output

```
frozenset({2})
```

---

Difference

```python
print(A - B)
```

Output

```
frozenset({1})
```

---

Symmetric Difference

```python
print(A ^ B)
```

Output

```
frozenset({1, 3})
```

---

# Membership

```python
numbers = frozenset({1, 2, 3})

print(2 in numbers)
```

Output

```
True
```

Average Complexity

```
O(1)
```

---

# Iteration

```python
for value in numbers:
    print(value)
```

Complexity

```
O(n)
```

---

# Why Do We Need FrozenSet?

A normal set is mutable.

Therefore

```python
data = {

    {1, 2}

}
```

Output

```
TypeError
```

Sets cannot be stored inside another set.

---

Using FrozenSet

```python
data = {

    frozenset({1, 2}),

    frozenset({3, 4})

}

print(data)
```

Output

```
{
 frozenset({1,2}),
 frozenset({3,4})
}
```

---

# FrozenSet as Dictionary Key

Valid

```python
graph = {

    frozenset({1,2}): "Edge"

}

print(graph)
```

Because a frozenset is hashable.

---

# Set vs FrozenSet

| Feature              | Set | FrozenSet |
| -------------------- | --- | --------- |
| Mutable              | ✅   | ❌         |
| Hashable             | ❌   | ✅         |
| Dictionary Key       | ❌   | ✅         |
| Can be Stored in Set | ❌   | ✅         |
| Supports add()       | ✅   | ❌         |
| Supports remove()    | ✅   | ❌         |

---

# Internal Working of Sets

Python sets are implemented using a **hash table**.

Conceptually

```
Element

↓

hash()

↓

Hash Value

↓

Internal Slot

↓

Store Element
```

This is the same fundamental idea used by dictionaries.

The main difference is:

Dictionary stores

```
Key → Value
```

Set stores only

```
Value
```

---

# Why Membership is Fast

Suppose

```python
numbers = {10, 20, 30}
```

Checking

```python
20 in numbers
```

Conceptually

```
20

↓

hash(20)

↓

Find Slot

↓

Found
```

Python does **not** normally scan every element.

Therefore average complexity is

```
O(1)
```

---

# Hashability

Everything stored inside a set must be hashable.

Valid

```python
10

"Python"

(1,2)

frozenset({1,2})

True
```

Invalid

```python
[1,2]

{1,2}

{"a":1}
```

---

# Why Lists Cannot Be Stored

Lists are mutable.

```python
numbers = [

    1,

    2

]
```

can later become

```python
[1,2,3]
```

If mutable objects were allowed in a hash table, lookups could become inconsistent after mutation.

Therefore Python only allows hashable objects.

---

# Duplicate Removal

When inserting

```python
numbers = {

    1,

    2,

    2,

    3

}
```

Python computes the hash.

If an equal element already exists, it is **not inserted again**.

Output

```
{1,2,3}
```

---

# Hash Collisions

Different objects can produce conflicting positions in a hash table.

Conceptually

```
Element A

↓

Slot 5


Element B

↓

Slot 5
```

Python internally resolves these collisions.

This process is automatic.

---

# Average Complexity

| Operation            | Complexity  |
| -------------------- | ----------- |
| Add                  | O(1)        |
| Remove               | O(1)        |
| Membership           | O(1)        |
| Discard              | O(1)        |
| Pop                  | O(1)        |
| Union                | O(n+m)      |
| Intersection         | O(min(n,m)) |
| Difference           | O(n)        |
| Symmetric Difference | O(n+m)      |
| Iteration            | O(n)        |

These are **average-case** complexities.

---

# Set Comprehension

Example

```python
squares = {

    x * x

    for x in range(6)

}

print(squares)
```

Output

```
{0,1,4,9,16,25}
```

---

Conditional

```python
evens = {

    x

    for x in range(10)

    if x % 2 == 0

}
```

---

# Performance Notes

Sets are generally

* Faster than lists for membership testing.
* Slightly more memory-intensive than lists because they maintain a hash table.
* Ideal for uniqueness checks.

Do **not** use a set when element order matters.

---

# DSA Patterns

## Duplicate Detection

```python
seen = set()
```

---

## Visited Nodes

```python
visited = set()
```

Graph

DFS

BFS

---

## Sliding Window

```python
window = set()
```

Useful when elements in the current window must remain unique.

---

## Remove Duplicates

```python
unique = set(arr)
```

---

## Fast Lookup

```python
if value in seen:
```

Average

```
O(1)
```

---

## Common Elements

```python
common = A & B
```

---

## Unique Elements

```python
unique = A ^ B
```

---

# Set vs Dictionary

| Set                 | Dictionary         |
| ------------------- | ------------------ |
| Stores Values       | Stores Key → Value |
| Uses Hash Table     | Uses Hash Table    |
| Unique Values       | Unique Keys        |
| Membership by Value | Membership by Key  |

---

# Common Mistakes

❌

Thinking

```python
{}
```

creates an empty set.

It creates a dictionary.

---

❌

Trying

```python
my_set[0]
```

Sets are not indexed.

---

❌

Using mutable objects.

```python
{[1,2]}
```

Invalid.

---

❌

Using

```python
remove()
```

when the element may not exist.

Use

```python
discard()
```

instead.

---

❌

Assuming

```python
list(set(arr))
```

preserves the original order.

A set does not guarantee insertion order as part of its API. If your algorithm depends on order, do not rely on converting through a set.

---

❌

Trying

```python
frozenset.add()
```

FrozenSet is immutable.

---

# Best Practices

✅ Use a set for fast membership testing.

✅ Use a set for duplicate removal.

✅ Use `discard()` when an element may not exist.

✅ Use `frozenset` when an immutable set is required.

✅ Prefer set operations (`&`, `|`, `-`, `^`) instead of manual loops when appropriate.

---

# Interview Questions

1. Difference between set and frozenset?
2. Why are sets implemented using hash tables?
3. Why is membership testing fast?
4. Why can't lists be stored inside a set?
5. Can a set contain another set?
6. Why can a frozenset be stored inside a set?
7. Difference between remove() and discard()?
8. Difference between set and dictionary?
9. Why is duplicate removal using sets efficient?
10. When should you use a set instead of a list?

---

# Quick Revision

✔ Sets store unique hashable elements.

✔ Sets are mutable.

✔ FrozenSets are immutable.

✔ FrozenSets are hashable.

✔ Sets use hash tables internally.

✔ Membership testing is average `O(1)`.

✔ Sets cannot contain mutable objects.

✔ Sets are ideal for duplicate removal and fast lookup.

✔ FrozenSets can be dictionary keys and elements of other sets.

✔ Sets are widely used in graphs, BFS, DFS, sliding window, and duplicate detection.
