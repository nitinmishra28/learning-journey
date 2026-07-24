# 🔷 Python Tuple Methods and Internal Working

Unlike lists, tuples have very few built-in methods because they are immutable.

Python tuples provide only **two methods**:

* `count()`
* `index()`

Most tuple operations are performed using built-in functions rather than tuple methods.

# 📚 Built-in Methods

| Method    | Purpose                           |
| --------- | --------------------------------- |
| `count()` | Counts occurrences of a value     |
| `index()` | Returns index of first occurrence |

---

# `count()`

Returns the number of occurrences of a value.

## Syntax

```python
tuple.count(value)
```

Example

```python
numbers = (1, 2, 2, 3, 2)

print(numbers.count(2))
```

Output

```
3
```

---

If the value does not exist

```python
numbers = (1, 2, 3)

print(numbers.count(10))
```

Output

```
0
```

---

## Complexity

```
Time : O(n)

Space : O(1)
```

Why?

Python must scan the entire tuple to count occurrences.

---

# `index()`

Returns the index of the first occurrence.

## Syntax

```python
tuple.index(value)
```

Example

```python
numbers = (10, 20, 30)

print(numbers.index(20))
```

Output

```
1
```

---

Duplicate Values

```python
numbers = (5, 2, 5, 5)

print(numbers.index(5))
```

Output

```
0
```

Only the first occurrence is returned.

---

## Value Not Present

```python
numbers.index(100)
```

Output

```
ValueError
```

Unlike

```python
dictionary.get()
```

there is no default value parameter.

---

## Search in a Range

Syntax

```python
tuple.index(value, start, end)
```

Example

```python
numbers = (1, 2, 3, 2, 5)

print(numbers.index(2, 2))
```

Output

```
3
```

Search begins from index `2`.

---

## Complexity

```
Time : O(n)

Space : O(1)
```

---

# Built-in Functions

Most tuple operations use Python's built-in functions.

## `len()`

```python
t = (10, 20, 30)

print(len(t))
```

Output

```
3
```

Complexity

```
O(1)
```

---

## `max()`

```python
numbers = (3, 9, 5)

print(max(numbers))
```

Output

```
9
```

Complexity

```
O(n)
```

---

## `min()`

```python
print(min(numbers))
```

Output

```
3
```

---

## `sum()`

```python
numbers = (1, 2, 3)

print(sum(numbers))
```

Output

```
6
```

---

## `sorted()`

```python
numbers = (5, 2, 9)

print(sorted(numbers))
```

Output

```
[2, 5, 9]
```

Notice

`sorted()` returns a **list**, not a tuple.

---

## Convert Back

```python
tuple(sorted(numbers))
```

---

# Concatenation

```python
a = (1, 2)

b = (3, 4)

print(a + b)
```

Output

```
(1, 2, 3, 4)
```

A new tuple is created.

The original tuples remain unchanged.

---

## Complexity

```
Time : O(n + m)

Space : O(n + m)
```

---

# Repetition

```python
t = (1, 2)

print(t * 3)
```

Output

```
(1, 2, 1, 2, 1, 2)
```

A new tuple is created.

---

# Tuple Comparison ⭐⭐⭐

One of the most important interview topics.

Python compares tuples **lexicographically**.

Example

```python
print((1, 2) < (1, 5))
```

Output

```
True
```

Comparison happens element by element.

```
1 == 1

↓

Compare Next

↓

2 < 5

↓

True
```

---

Another Example

```python
print((2, 1) < (1, 100))
```

Output

```
False
```

The first element already determines the answer.

Python never compares the remaining elements.

---

# Different Lengths

```python
print((1, 2) < (1, 2, 3))
```

Output

```
True
```

The shorter tuple is considered smaller when all compared elements are equal.

---

# Why Tuple Comparison Is Useful

Heap

```python
(priority, node)
```

Sorting

```python
(age, name)
```

Coordinates

```python
(row, col)
```

Python automatically compares tuples correctly.

---

# Sorting Tuples

Example

```python
students = [

    ("Bob", 24),

    ("Alice", 20),

    ("Charlie", 22)

]

print(sorted(students))
```

Output

```
[
 ('Alice',20),
 ('Bob',24),
 ('Charlie',22)
]
```

Sorting occurs using the first element.

---

Sort by Second Element

```python
students = [

    ("Bob", 24),

    ("Alice", 20),

    ("Charlie", 22)

]

result = sorted(

    students,

    key=lambda x: x[1]

)

print(result)
```

Output

```
[
 ('Alice',20),
 ('Charlie',22),
 ('Bob',24)
]
```

---

# Tuple Hashing

Tuples can be dictionary keys.

```python
point = (10, 20)

data = {

    point: "Origin"

}

print(data)
```

Output

```
{
 (10,20): 'Origin'
}
```

---

Python computes a hash for the tuple.

Conceptually

```
Tuple

↓

Hash

↓

Dictionary Lookup
```

---

# Hashability Rule

A tuple is hashable **only if every element is hashable**.

Valid

```python
(1,2,3)
```

Valid

```python
("A",5)
```

Invalid

```python
([1,2],3)
```

because the list is mutable.

---

# Why Tuples Are Used in Dictionaries

Example

```python
visited = {

    (2,5): True,

    (4,1): True

}
```

Common in

* BFS
* DFS
* Matrix Problems
* Dynamic Programming

---

# Tuples in Heap

Python's heap stores tuples very frequently.

```python
import heapq

heap = []

heapq.heappush(

    heap,

    (5,"A")

)

heapq.heappush(

    heap,

    (2,"B")

)

heapq.heappush(

    heap,

    (7,"C")

)

print(heapq.heappop(heap))
```

Output

```
(2,'B')
```

Python compares tuples automatically.

First priority

↓

Second value if needed

---

# Why Heap Uses Tuples

Suppose

```
(priority,node)
```

Lowest priority automatically comes first.

No extra comparison code is needed.

---

# Tuple Memory

Tuples generally use less memory than lists because they are immutable.

Conceptually

```
List

↓

Supports Append

Supports Remove

Supports Insert

Supports Resize

Extra Memory Needed
```

Tuple

```
Fixed Size

↓

No Resize

↓

Less Overhead
```

---

# Performance

Creating

```
Tuple

↓

Slightly Faster
```

Iteration

```
Tuple

↓

Slightly Faster
```

Memory

```
Tuple

↓

Slightly Less Memory
```

These are optimizations.

For most applications, choose tuples for immutability rather than micro-performance.

---

# DSA Applications

## Coordinates

```python
(row,col)
```

---

## Graph Edge

```python
(u,v)
```

---

## Heap

```python
(priority,node)
```

---

## DP State

```python
(index,target)
```

---

## Dictionary Key

```python
(point_x,point_y)
```

---

## BFS Queue

```python
(row,col)
```

---

# Tuple vs List Decision

Use **tuple** when

* Data should never change.
* Using dictionary keys.
* Using heap elements.
* Returning multiple values.
* Representing coordinates.

Use **list** when

* Adding elements.
* Removing elements.
* Updating elements.
* Dynamic collection.

---

# Common Mistakes

❌

Thinking tuples are deeply immutable.

```
([1],)
```

The list can still change.

---

❌

Using

```python
tuple.append()
```

There is no append method.

---

❌

Using

```python
tuple.remove()
```

No remove method exists.

---

❌

Thinking

```python
sorted(tuple)
```

returns a tuple.

It returns a list.

---

❌

Using a tuple containing a list as a dictionary key.

```
([1],2)
```

Invalid.

---

# Interview Questions

1. Why are tuples immutable?
2. Why do tuples have only two methods?
3. Difference between tuple and list?
4. Can tuples be dictionary keys?
5. Why can't a tuple containing a list be a dictionary key?
6. Explain lexicographical comparison.
7. Why are tuples used in heaps?
8. Why are tuples used in BFS and graph problems?
9. Does `sorted()` return a tuple?
10. Why are tuples slightly more memory efficient?

---

# Quick Revision

✔ Tuples have only two methods.

✔ `count()` counts occurrences.

✔ `index()` returns the first occurrence.

✔ Both methods take `O(n)` time.

✔ `sorted()` returns a list.

✔ Tuple concatenation creates a new tuple.

✔ Tuple repetition creates a new tuple.

✔ Tuples are compared lexicographically.

✔ Tuples can be dictionary keys if all elements are hashable.

✔ Tuples are heavily used in heaps, graphs, BFS, DP, and memoization.

✔ Tuples are chosen mainly because they are immutable.
