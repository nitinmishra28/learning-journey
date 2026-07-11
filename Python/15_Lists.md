# 📋 Python Lists

> Lists are one of the most powerful and frequently used data structures in Python. They are mutable, ordered, dynamically sized collections capable of storing heterogeneous objects.

---

# 📚 Table of Contents

- What is a List?
- Why Lists?
- Internal Working
- Dynamic Arrays
- Memory Allocation
- Creating Lists
- Characteristics
- Accessing Elements
- Indexing
- Negative Indexing
- Updating Elements
- List Length
- Membership Operator
- Iteration
- Internal Memory Model
- Time Complexity
- Best Practices
- Common Mistakes
- Interview Questions
- Quick Revision

---

# 📖 What is a List?

A list is an **ordered**, **mutable** collection of objects.

Unlike arrays in C/C++,

Python lists

- grow dynamically
- store different data types
- automatically manage memory

Example

```python
numbers = [10, 20, 30]
```

A list can store different types simultaneously.

```python
data = [10, "Python", 3.14, True, [1,2]]
```

---

# Why Use Lists?

Lists are useful because they

✅ Preserve insertion order

✅ Can grow and shrink dynamically

✅ Allow duplicate values

✅ Support random indexing

✅ Store any Python object

Lists are used everywhere in DSA.

Examples

- Arrays
- Stacks
- Queues (although deque is preferred)
- Graph adjacency lists
- Dynamic Programming
- Sliding Window
- Backtracking

---

# Characteristics of Lists

| Property | Value |
|----------|-------|
| Ordered | ✅ |
| Mutable | ✅ |
| Duplicates Allowed | ✅ |
| Dynamic Size | ✅ |
| Indexed | ✅ |
| Heterogeneous | ✅ |

---

# Internal Working ⭐

One of the most important interview topics.

Python Lists are **Dynamic Arrays**.

They are **NOT Linked Lists.**

Internally

```
List Object

↓

Pointer Array

↓

Object References
```

Example

```python
numbers = [10,20,30]
```

Internally

```
numbers

↓

+---------+
|   *-----|------> Integer Object (10)
|   *-----|------> Integer Object (20)
|   *-----|------> Integer Object (30)
+---------+
```

Notice

The list stores **references**, not actual objects.

Exactly like variables.

---

# Dynamic Array

Unlike C arrays,

Python lists automatically resize.

Suppose

```python
arr = [1,2,3]
```

Memory

```
Capacity = 4

Used = 3
```

Append

```python
arr.append(4)
```

Still enough memory.

```
Capacity = 4

Used = 4
```

Append again

```python
arr.append(5)
```

Now

Python allocates a larger array.

Copies references.

Deletes old array.

```
Capacity

↓

8
```

This is why

append()

is usually

```
O(1)
```

but occasionally

```
O(n)
```

---

# Memory Growth

Python overallocates memory.

Instead of increasing by one element every time,

it reserves extra capacity.

Benefits

✅ Fewer reallocations

✅ Faster append()

This technique is called

```
Overallocation
```

---

# Creating Lists

Empty

```python
arr = []
```

---

Using list()

```python
arr = list()
```

---

Using iterable

```python
arr = list("Python")
```

Output

```
['P','y','t','h','o','n']
```

---

Using range

```python
arr = list(range(5))
```

Output

```
[0,1,2,3,4]
```

---

Nested List

```python
matrix = [

    [1,2],

    [3,4]
]
```

---

# Accessing Elements

```python
arr = [10,20,30]
```

First

```python
print(arr[0])
```

Output

```
10
```

---

Second

```python
print(arr[1])
```

Output

```
20
```

---

Last

```python
print(arr[2])
```

Output

```
30
```

Complexity

```
O(1)
```

Because Python directly calculates

```
Base Address

+

Index × Pointer Size
```

---

# Negative Indexing

```python
arr = [10,20,30,40]
```

```
10 20 30 40

-4 -3 -2 -1
```

Example

```python
print(arr[-1])
```

Output

```
40
```

---

# Updating Elements

Lists are mutable.

```python
arr = [1,2,3]

arr[1] = 100

print(arr)
```

Output

```
[1,100,3]
```

Complexity

```
O(1)
```

---

# Length

```python
len(arr)
```

Returns

```
Number of elements
```

Complexity

```
O(1)
```

Why?

Python stores the length inside the list object.

It does not count elements every time.

---

# Membership

```python
3 in arr
```

Returns

```
True
```

Complexity

```
O(n)
```

Python checks elements one by one.

---

# Iterating

Using element

```python
for x in arr:
    print(x)
```

---

Using index

```python
for i in range(len(arr)):
    print(arr[i])
```

---

Using enumerate()

```python
for index,value in enumerate(arr):
    print(index,value)
```

Interview Tip

Prefer

```python
enumerate()
```

when both index and value are required.

---

# Internal Memory Representation

```
Variable

↓

List Object

↓

Reference Array

↓

Actual Objects
```

Remember

Python Lists

store

```
References

NOT

Objects
```

---

# Complexity Table

| Operation | Complexity |
|-----------|------------|
| Index | O(1) |
| Update | O(1) |
| len() | O(1) |
| Membership | O(n) |
| Iteration | O(n) |
| Append | O(1) Amortized |

---

# Best Practices

✅ Use lists when frequent appending is needed.

✅ Prefer enumerate() over range(len()) when both index and value are required.

✅ Remember lists store references.

---

# Common Mistakes

❌ Thinking lists store actual values.

They store references.

---

❌ Assuming append() is always O(1).

Occasionally,

resizing makes it O(n).

---

❌ Confusing Python Lists with Linked Lists.

Python Lists are dynamic arrays.

---

# DSA Tips

Lists are ideal for

- Sliding Window

- Prefix Sum

- Sorting

- Binary Search

- Dynamic Programming

- Graph Representation

Understand list internals before solving DSA because almost every Python DSA solution relies on them.

---

# Interview Questions

1. Are Python Lists arrays or linked lists?

2. Why is append() amortized O(1)?

3. Why is indexing O(1)?

4. Why is membership O(n)?

5. Do Python Lists store values or references?

6. Why is len() O(1)?

---

# Quick Revision

✔ Lists are mutable.

✔ Lists are dynamic arrays.

✔ Lists store references.

✔ Lists support random access.

✔ append() is amortized O(1).

✔ Membership is O(n).

✔ Indexing is O(1).

✔ len() is O(1).