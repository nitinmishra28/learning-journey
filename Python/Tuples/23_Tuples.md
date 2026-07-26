# 🔷 Python Tuples

A **tuple** is an ordered, immutable collection of elements.

Once a tuple is created, its elements **cannot be modified**.

---

# Why Tuples?

Use tuples when:

- Data should not change.
- Multiple values need to be grouped together.
- The collection should be hashable (if all elements are hashable).
- Slightly better memory efficiency than lists is desired.

---

# Characteristics

| Property | Tuple |
|----------|--------|
| Ordered | ✅ Yes |
| Mutable | ❌ No |
| Allows Duplicates | ✅ Yes |
| Indexed | ✅ Yes |
| Hashable | ✅ If all elements are hashable |

---

# Creating Tuples

## Empty Tuple

```python
t = ()
```

---

## Multiple Elements

```python
t = (1, 2, 3)

print(t)
```

Output

```
(1, 2, 3)
```

---

## Without Parentheses

Parentheses are optional.

```python
t = 1, 2, 3

print(t)
```

Output

```
(1, 2, 3)
```

Python creates the tuple automatically.

---

# Single Element Tuple ⭐

One of the most common interview questions.

```python
t = (5)
```

Type

```python
print(type(t))
```

Output

```
<class 'int'>
```

Why?

Because parentheses alone do not create a tuple.

---

Correct

```python
t = (5,)
```

or

```python
t = 5,
```

Output

```
<class 'tuple'>
```

The comma creates the tuple.

---

# Mixed Data Types

```python
t = (1, "Python", True, 5.6)
```

Tuples can store different data types.

---

# Nested Tuples

```python
t = (
    (1, 2),
    (3, 4)
)

print(t)
```

Output

```
((1, 2), (3, 4))
```

---

# tuple() Constructor

Convert another iterable into a tuple.

```python
numbers = [1, 2, 3]

t = tuple(numbers)

print(t)
```

Output

```
(1, 2, 3)
```

Works with

- List
- String
- Set
- Range
- Dictionary

---

Example

```python
tuple("Python")
```

Output

```
('P', 'y', 't', 'h', 'o', 'n')
```

---

# Dictionary to Tuple

```python
student = {
    "name": "Nitin",
    "age": 23
}

print(tuple(student))
```

Output

```
('name', 'age')
```

Only dictionary keys are converted.

---

# Indexing

```python
t = (10, 20, 30)

print(t[0])
```

Output

```
10
```

---

Negative Indexing

```python
print(t[-1])
```

Output

```
30
```

---

# Slicing

```python
t = (10, 20, 30, 40, 50)

print(t[1:4])
```

Output

```
(20, 30, 40)
```

---

Reverse

```python
print(t[::-1])
```

Output

```
(50, 40, 30, 20, 10)
```

---

# Immutability ⭐⭐⭐

Tuples cannot be modified.

```python
t = (1, 2, 3)

t[0] = 100
```

Output

```
TypeError
```

---

Cannot

- Append
- Remove
- Insert
- Update

because tuples are immutable.

---

# Memory Representation

```
Tuple

↓

Fixed References

↓

Objects
```

The tuple structure cannot change after creation.

---

# Mutable Objects Inside Tuple ⭐

A tuple is immutable.

Its elements are not necessarily immutable.

Example

```python
t = (
    [1, 2],
    [3, 4]
)

t[0].append(100)

print(t)
```

Output

```
([1, 2, 100], [3, 4])
```

Why?

The tuple itself did not change.

The list inside it changed.

---

# Tuple Packing

```python
person = "Nitin", 23, "Python"
```

Python packs the values into a tuple.

---

# Tuple Unpacking

```python
name, age, skill = person

print(name)
print(age)
print(skill)
```

Output

```
Nitin

23

Python
```

---

# Extended Unpacking

```python
numbers = (1, 2, 3, 4, 5)

first, *middle, last = numbers

print(first)

print(middle)

print(last)
```

Output

```
1

[2, 3, 4]

5
```

Notice

```
middle
```

is a **list**, not a tuple.

---

# Swapping Variables

Python internally uses tuple packing/unpacking.

```python
a = 10
b = 20

a, b = b, a

print(a, b)
```

Output

```
20 10
```

---

# Membership

```python
t = (1, 2, 3)

print(2 in t)
```

Output

```
True
```

Complexity

```
O(n)
```

---

# Length

```python
len(t)
```

Complexity

```
O(1)
```

---

# Iteration

```python
for value in t:
    print(value)
```

Complexity

```
O(n)
```

---

# Tuple vs List

| Tuple | List |
|--------|------|
| Immutable | Mutable |
| Slightly More Memory Efficient | More Memory |
| Slightly Faster Iteration | Slightly Slower |
| Hashable (if elements are hashable) | Not Hashable |
| No append(), remove(), etc. | Supports modification |

---

# When Should You Use Tuples?

Use tuples when

- Data should never change.
- Returning multiple values from a function.
- Creating dictionary keys.
- Representing coordinates.
- Representing DP states.

Examples

```python
point = (10, 20)

state = (index, mask)

student = ("Nitin", 23)
```

---

# Common Mistakes

❌

```python
t = (5)
```

Not a tuple.

---

Correct

```python
t = (5,)
```

---

❌

Thinking tuple elements cannot change.

```python
([1,2],)
```

The list inside can still change.

---

❌

Using a list as a dictionary key.

```python
data = {
    [1,2]: 10
}
```

Use

```python
(1,2)
```

instead.

---

# DSA Applications

Tuples are frequently used for

- Coordinates

```python
(row, col)
```

- Graph edges

```python
(u, v)
```

- Heap elements

```python
(priority, node)
```

- Memoization

```python
(index, target)
```

- BFS queue

```python
(row, col)
```

---

# Interview Questions

1. Difference between tuple and list?
2. Why is `(5)` not a tuple?
3. Why is `(5,)` a tuple?
4. Can a tuple contain mutable objects?
5. Why can tuples be dictionary keys?
6. Why can't lists be dictionary keys?
7. What is tuple packing?
8. What is tuple unpacking?
9. Why are tuples used in heaps and graph problems?

---

# Quick Revision

✔ Tuples are immutable.

✔ Tuples are ordered.

✔ Tuples allow duplicates.

✔ The comma creates a tuple.

✔ `(5)` is an integer.

✔ `(5,)` is a tuple.

✔ Tuple slicing creates a new tuple.

✔ Mutable objects inside tuples can still change.

✔ Tuples are commonly used in DSA for coordinates, states, and heaps.