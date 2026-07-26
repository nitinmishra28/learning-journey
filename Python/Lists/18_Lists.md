# ⭐ List Comprehensions

List comprehensions provide a concise and efficient way to create lists.

Instead of writing:

```python
squares = []

for i in range(5):
    squares.append(i * i)

print(squares)
```

You can write:

```python
squares = [i * i for i in range(5)]

print(squares)
```

Output:

```text
[0, 1, 4, 9, 16]
```

## Syntax

```python
[expression for item in iterable]
```

Conceptually:

```text
Expression
    ↓
   i * i

for

Item
 ↓
 i

in

Iterable
   ↓
range(5)
```

## Time Complexity

For `n` elements:

```text
O(n)
```

The exact complexity also depends on the work performed by the expression for each element.

## Space Complexity

Because a new list is created:

```text
O(n)
```

## Why Use List Comprehensions?

* Cleaner and more concise code
* Often slightly faster than an equivalent `for` loop with repeated `append()`
* Useful for transforming and filtering data

However, avoid overly complicated nested comprehensions when a normal loop would be easier to understand.

# Conditional List Comprehension

You can add a condition to decide which elements should be included.

Example: create a list containing only even numbers.

```python
even = [x for x in range(10) if x % 2 == 0]

print(even)
```

Output:

```text
[0, 2, 4, 6, 8]
```

The structure is:

```python
[expression for item in iterable if condition]
```

Another example:

```python
odd = [x for x in range(10) if x % 2 != 0]

print(odd)
```

Output:

```text
[1, 3, 5, 7, 9]
```

You may also see:

```python
odd = [x for x in range(10) if x % 2]
```

This works because:

```text
0 → Falsy
1 → Truthy
```

For readability, `x % 2 != 0` may be clearer when learning.

# `if...else` in a List Comprehension

An `if...else` expression transforms every element based on a condition.

Syntax:

```python
[value_if_true if condition else value_if_false for item in iterable]
```

Example:

```python
result = [
    "Even" if x % 2 == 0 else "Odd"
    for x in range(5)
]

print(result)
```

Output:

```text
['Even', 'Odd', 'Even', 'Odd', 'Even']
```

## Filtering vs `if...else`

These two forms serve different purposes.

### Filtering

```python
[x for x in numbers if x > 0]
```

Some elements may be excluded.

### Transformation

```python
["Positive" if x > 0 else "Non-Positive" for x in numbers]
```

Every input element produces an output element.

# Nested List Comprehension

List comprehensions can contain multiple loops.

Example:

```python
matrix = [
    [1, 2],
    [3, 4]
]

flattened = [
    num
    for row in matrix
    for num in row
]

print(flattened)
```

Output:

```text
[1, 2, 3, 4]
```

Equivalent normal loop:

```python
flattened = []

for row in matrix:
    for num in row:
        flattened.append(num)
```

The order of the `for` clauses follows the same order as the nested loops.

```text
for row in matrix
    ↓
for num in row
```

# Matrix Creation

A safe way to create an independently mutable matrix is:

```python
rows = 3
cols = 3

matrix = [
    [0 for _ in range(cols)]
    for _ in range(rows)
]

print(matrix)
```

Output:

```text
[
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
```

A shorter equivalent version is:

```python
matrix = [[0] * cols for _ in range(rows)]
```

Every iteration creates a separate inner list.

Avoid:

```python
matrix = [[0] * cols] * rows
```

because every row references the same inner list.

# Matrix Transpose

Suppose we have:

```text
1 2 3
4 5 6
```

The transpose is:

```text
1 4
2 5
3 6
```

Using a list comprehension:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

transpose = [
    [row[i] for row in matrix]
    for i in range(len(matrix[0]))
]

print(transpose)
```

Output:

```text
[
    [1, 4],
    [2, 5],
    [3, 6]
]
```

For a rectangular matrix, this works when all rows have the same length and the matrix is not empty.

Python also provides a concise approach using `zip()`:

```python
transpose = [list(row) for row in zip(*matrix)]
```

We'll understand `*matrix` in the unpacking section below.

# 🔢 `enumerate()`

`enumerate()` is useful when you need both the **index** and the **value** while iterating.

Instead of:

```python
arr = ["A", "B", "C"]

for i in range(len(arr)):
    print(i, arr[i])
```

Prefer:

```python
arr = ["A", "B", "C"]

for index, value in enumerate(arr):
    print(index, value)
```

Output:

```text
0 A
1 B
2 C
```

## Custom Starting Index

By default, indexing starts from `0`.

You can change it:

```python
arr = ["A", "B", "C"]

for index, value in enumerate(arr, start=1):
    print(index, value)
```

Output:

```text
1 A
2 B
3 C
```

## Important

`enumerate()` does not create a list of all index-value pairs immediately.

It returns an iterator-like enumerate object.

```python
arr = ["A", "B"]

result = enumerate(arr)

print(type(result))
```

Output:

```text
<class 'enumerate'>
```

Convert it to a list when needed:

```python
print(list(enumerate(arr)))
```

Output:

```text
[(0, 'A'), (1, 'B')]
```

# 🔗 `zip()`

`zip()` combines elements from multiple iterables position by position.

Example:

```python
names = ["Alice", "Bob"]
marks = [90, 80]

for name, mark in zip(names, marks):
    print(name, mark)
```

Output:

```text
Alice 90
Bob 80
```

Conceptually:

```text
Alice + 90 → ("Alice", 90)

Bob   + 80 → ("Bob", 80)
```

## `zip()` Returns an Iterator

```python
names = ["Alice", "Bob"]
marks = [90, 80]

result = zip(names, marks)

print(result)
```

You will see a zip object.

To view all values:

```python
print(list(result))
```

Output:

```text
[('Alice', 90), ('Bob', 80)]
```

## Unequal Length

By default, `zip()` stops when the shortest iterable is exhausted.

```python
a = [1, 2, 3]
b = [10]

print(list(zip(a, b)))
```

Output:

```text
[(1, 10)]
```

The values `2` and `3` are ignored because `b` has no corresponding elements.

# 📦 Unpacking

Python allows iterable elements to be assigned directly to variables.

```python
numbers = [10, 20, 30]

a, b, c = numbers

print(a, b, c)
```

Output:

```text
10 20 30
```

The number of variables must normally match the number of elements.

This raises an error:

```python
numbers = [10, 20, 30]

a, b = numbers
```

Output:

```text
ValueError: too many values to unpack
```

# Extended Unpacking with `*`

The `*` operator can collect multiple remaining values.

```python
numbers = [1, 2, 3, 4, 5]

first, *middle, last = numbers

print(first)
print(middle)
print(last)
```

Output:

```text
1
[2, 3, 4]
5
```

Important:

The starred variable receives a **list**.

## Collect Remaining Elements

```python
first, *rest = [1, 2, 3, 4]

print(first)
print(rest)
```

Output:

```text
1
[2, 3, 4]
```

You can also write:

```python
*start, last = [1, 2, 3, 4]
```

Output:

```text
start = [1, 2, 3]
last = 4
```

# Unpacking in Function Calls

The `*` operator can unpack a list into positional arguments.

```python
numbers = [1, 2, 3]

print(*numbers)
```

Output:

```text
1 2 3
```

This is why:

```python
zip(*matrix)
```

passes each matrix row as a separate argument to `zip()`.

For example:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

print(list(zip(*matrix)))
```

Output:

```text
[(1, 4), (2, 5), (3, 6)]
```

This effectively transposes the matrix into tuples.

# ✅ `any()`

`any()` returns `True` if **at least one element is truthy**.

```python
print(any([0, 0, 1]))
```

Output:

```text
True
```

Example:

```python
print(any([0, False, None, "Python"]))
```

Output:

```text
True
```

Because `"Python"` is truthy.

## Empty Iterable

```python
print(any([]))
```

Output:

```text
False
```

# ✅ `all()`

`all()` returns `True` if **every element is truthy**.

```python
print(all([1, 2, 3]))
```

Output:

```text
True
```

Example:

```python
print(all([1, 2, 0]))
```

Output:

```text
False
```

## Empty Iterable ⭐

```python
print(all([]))
```

Output:

```text
True
```

This sometimes surprises beginners.

# `any()` and `all()` with Conditions

These functions become very useful with generator expressions.

Check whether at least one number is negative:

```python
numbers = [10, 20, -5, 30]

has_negative = any(x < 0 for x in numbers)

print(has_negative)
```

Output:

```text
True
```

Check whether every number is positive:

```python
numbers = [10, 20, 30]

all_positive = all(x > 0 for x in numbers)

print(all_positive)
```

Output:

```text
True
```

# ➕ `sum()`

Returns the sum of numeric elements.

```python
numbers = [1, 2, 3]

print(sum(numbers))
```

Output:

```text
6
```

## Starting Value

`sum()` accepts an optional starting value.

```python
numbers = [1, 2, 3]

print(sum(numbers, 10))
```

Output:

```text
16
```

Because:

```text
10 + 1 + 2 + 3 = 16
```

## Complexity

For `n` elements:

```text
O(n)
```

# 🔽 `min()`

Returns the smallest element.

```python
numbers = [5, 2, 8]

print(min(numbers))
```

Output:

```text
2
```

Complexity:

```text
O(n)
```

Python must inspect the elements to find the minimum.

# 🔼 `max()`

Returns the largest element.

```python
numbers = [5, 2, 8]

print(max(numbers))
```

Output:

```text
8
```

Complexity:

```text
O(n)
```

# `min()` and `max()` with `key`

You can control how values are compared.

```python
words = ["apple", "hi", "banana"]

print(min(words, key=len))
print(max(words, key=len))
```

Output:

```text
hi
banana
```

# 🔃 `sorted()` with `lambda`

Suppose we have:

```python
students = [
    ("Alice", 90),
    ("Bob", 75),
    ("Charlie", 85)
]
```

Sort according to marks:

```python
result = sorted(
    students,
    key=lambda student: student[1]
)

print(result)
```

Output:

```text
[
    ('Bob', 75),
    ('Charlie', 85),
    ('Alice', 90)
]
```

Here:

```python
lambda student: student[1]
```

means:

```text
For every student tuple
        ↓
Use index 1 as the sorting key
        ↓
Marks
```

Descending order:

```python
result = sorted(
    students,
    key=lambda student: student[1],
    reverse=True
)
```

# 📊 List Performance Cheat Sheet

| Operation                    | Time Complexity         |
| ---------------------------- | ----------------------- |
| Indexing                     | `O(1)`                  |
| Updating by index            | `O(1)`                  |
| `len()`                      | `O(1)`                  |
| `append()`                   | `O(1)` amortized        |
| `pop()` from end             | `O(1)`                  |
| `pop(0)`                     | `O(n)`                  |
| `insert(0, x)`               | `O(n)`                  |
| Insert in middle             | `O(n)`                  |
| `remove()`                   | `O(n)`                  |
| `x in list`                  | `O(n)`                  |
| `index()`                    | `O(n)`                  |
| `count()`                    | `O(n)`                  |
| `copy()`                     | `O(n)`                  |
| `reverse()`                  | `O(n)`                  |
| `reversed()` creation        | `O(1)`                  |
| `sort()`                     | `O(n log n)` worst case |
| `sorted()`                   | `O(n log n)` worst case |
| Slice of `k` elements        | `O(k)`                  |
| `extend()` with `k` elements | `O(k)`                  |
| `sum()`                      | `O(n)`                  |
| `min()`                      | `O(n)`                  |
| `max()`                      | `O(n)`                  |

# When Should You Use Lists?

Use a list when:

* Order matters
* Duplicate values are allowed
* Fast indexing is required
* You frequently append to the end
* You need a dynamically sized sequence

Lists are especially useful for:

* Arrays
* Stacks
* Matrices
* Dynamic Programming tables
* Backtracking paths
* Graph adjacency lists

# When Should You Avoid Lists?

## Frequent Membership Checking

This:

```python
x in arr
```

takes:

```text
O(n)
```

If you repeatedly need fast membership checking, consider a `set`.

Average membership complexity:

```text
O(1)
```

## Frequent Front Operations

Avoid repeatedly doing:

```python
arr.insert(0, value)
```

or:

```python
arr.pop(0)
```

Both require shifting elements and take:

```text
O(n)
```

For efficient operations at both ends, use:

```python
from collections import deque
```

A `deque` supports efficient appends and pops from both ends.

# 🧠 DSA Patterns Using Lists

Python lists are heavily used in the following patterns:

* Two Pointers
* Sliding Window
* Prefix Sum
* Binary Search
* Dynamic Programming
* Monotonic Stack
* Graph Adjacency Lists
* Matrix Problems
* Backtracking

Understanding list operations and their complexities helps you avoid hidden `O(n²)` solutions.

# Common LeetCode Problems

## Easy

* Two Sum
* Best Time to Buy and Sell Stock
* Contains Duplicate
* Merge Sorted Array
* Remove Duplicates from Sorted Array

## Medium

* 3Sum
* Product of Array Except Self
* Rotate Array
* Spiral Matrix
* Set Matrix Zeroes

## Hard

* Trapping Rain Water
* First Missing Positive
* Sliding Window Maximum
* Median of Two Sorted Arrays
* Largest Rectangle in Histogram

# 💼 Interview Questions

1. Why is `append()` amortized `O(1)`?
2. What is the difference between `append()` and `extend()`?
3. What is the difference between `sort()` and `sorted()`?
4. What is the difference between shallow copy and deep copy?
5. Why is `[[0] * n] * m` dangerous?
6. What is the difference between `+` and `+=` for lists?
7. What is the difference between `reverse()` and `reversed()`?
8. Why do in-place list methods such as `sort()` return `None`?
9. When should you use `deque` instead of a list?
10. Why are Python lists implemented as dynamic arrays?
11. What is the difference between filtering and `if...else` in a list comprehension?
12. What does `zip()` do when iterables have different lengths?
13. What type does the starred variable receive during extended unpacking?
14. What do `any([])` and `all([])` return?
15. Why is list membership `O(n)`?

# 📌 Quick Revision

✔ Lists are mutable.

✔ Python lists are dynamic arrays.

✔ Lists store references to objects.

✔ `append()` is `O(1)` amortized.

✔ `insert()` and front removal are `O(n)`.

✔ `pop()` from the end is `O(1)`.

✔ `sort()` modifies the original list and returns `None`.

✔ `sorted()` returns a new list.

✔ `copy()` and `[:]` create shallow copies.

✔ `deepcopy()` recursively copies nested objects.

✔ List comprehensions provide concise list creation.

✔ Filtering syntax excludes unwanted elements.

✔ `if...else` comprehensions transform every element.

✔ `enumerate()` provides both index and value.

✔ `zip()` combines corresponding elements.

✔ `zip()` stops at the shortest iterable by default.

✔ Extended unpacking with `*` collects remaining values into a list.

✔ `any()` checks whether at least one value is truthy.

✔ `all()` checks whether every value is truthy.

✔ Use a `set` for frequent membership checking.

✔ Use `deque` for frequent operations at both ends.

# 🎉 Congratulations!

You have completed **Python Lists**.

You now understand:

* Internal working of Python lists
* Dynamic array behavior
* Memory allocation
* Important list methods
* In-place vs non-in-place operations
* Shallow and deep copying
* Aliasing and references
* Sorting
* Slicing
* Nested lists and matrices
* List comprehensions
* `enumerate()`
* `zip()`
* Packing and unpacking
* `any()` and `all()`
* List performance
* DSA applications

This gives you a strong foundation for using Python lists correctly in both development and DSA.

# 📝 Practice Problems

## Easy

1. Reverse a List
2. Find the Maximum Element
3. Find the Second Largest Element
4. Remove Duplicates from a List
5. Rotate a List by `K` Positions

## Medium

1. Merge Intervals
2. Product of Array Except Self
3. 3Sum
4. Spiral Matrix
5. Next Permutation

## Hard

1. Trapping Rain Water
2. First Missing Positive
3. Sliding Window Maximum
4. Median of Two Sorted Arrays
5. Largest Rectangle in Histogram
