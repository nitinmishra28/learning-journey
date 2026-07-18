# 🔄 `sort()`

The `sort()` method sorts the **original list in place**.

## Syntax

```python
list.sort(key=None, reverse=False)
```

## Parameters

| Parameter | Description                                           |
| --------- | ----------------------------------------------------- |
| `key`     | Optional function used to determine the sorting value |
| `reverse` | Set to `True` for descending order                    |

## Example

```python
arr = [5, 2, 4, 1]

arr.sort()

print(arr)
```

Output:

```text
[1, 2, 4, 5]
```

## Return Value

```text
None
```

## In-place?

✅ **Yes**

The original list is modified.

```python
arr = [3, 1, 2]

result = arr.sort()

print(arr)
print(result)
```

Output:

```text
[1, 2, 3]
None
```

This is important:

```python
arr.sort()
```

sorts `arr`, but:

```python
arr = arr.sort()
```

sets `arr` to `None`.

## Internal Working

Python's built-in sorting implementation uses **Timsort**, a stable sorting algorithm designed to perform especially well on real-world and partially ordered data.

Important properties:

* Stable sorting
* Efficient on partially sorted data
* Worst-case time complexity of `O(n log n)`

## Complexity

| Case    | Time Complexity |
| ------- | --------------- |
| Best    | `O(n)`          |
| Average | `O(n log n)`    |
| Worst   | `O(n log n)`    |

The temporary memory required by the sorting implementation depends on the input and implementation details, with worst-case auxiliary space commonly described as `O(n)`.

## Stable Sort ⭐

Python's sorting is **stable**.

This means that when two elements have the same sorting key, their original relative order is preserved.

```python
students = [
    ("Alice", 90),
    ("Bob", 90),
    ("Charlie", 80)
]

students.sort(key=lambda x: x[1])

print(students)
```

Output:

```text
[
    ('Charlie', 80),
    ('Alice', 90),
    ('Bob', 90)
]
```

Both Alice and Bob have `90`, and Alice originally appeared before Bob, so that order is preserved.

## Descending Order

Use `reverse=True`.

```python
arr = [5, 2, 4, 1]

arr.sort(reverse=True)

print(arr)
```

Output:

```text
[5, 4, 2, 1]
```

## Sorting Using `key`

You can control what value Python uses for comparison.

```python
words = ["apple", "hi", "banana"]

words.sort(key=len)

print(words)
```

Output:

```text
['hi', 'apple', 'banana']
```

Here, the strings are sorted according to their lengths.

# 🔃 `sorted()`

The `sorted()` function returns a **new sorted list**.

The original iterable remains unchanged.

## Syntax

```python
sorted(iterable, key=None, reverse=False)
```

## Example

```python
arr = [5, 2, 4, 1]

new_arr = sorted(arr)

print(arr)
print(new_arr)
```

Output:

```text
[5, 2, 4, 1]
[1, 2, 4, 5]
```

## Return Value

Returns a:

```text
New List
```

## In-place?

❌ **No**

The original data is not modified.

## Complexity

For sorting `n` elements:

```text
O(n log n)
```

in the average and worst cases.

# `sort()` vs `sorted()`

| `sort()`                                       | `sorted()`                            |
| ---------------------------------------------- | ------------------------------------- |
| List method                                    | Built-in function                     |
| Modifies the original list                     | Does not modify the original iterable |
| Returns `None`                                 | Returns a new list                    |
| Works only with lists                          | Works with any iterable               |
| Usually avoids creating a separate result list | Creates a new result list             |

## Common Mistake

❌ Wrong:

```python
arr = [5, 2, 1]

arr = arr.sort()

print(arr)
```

Output:

```text
None
```

Why?

Because `sort()` modifies the existing list and returns `None`.

✅ Correct:

```python
arr = [5, 2, 1]

arr.sort()

print(arr)
```

# 📋 `copy()`

The `copy()` method creates a **shallow copy** of a list.

## Syntax

```python
list.copy()
```

## Example

```python
arr = [1, 2, 3]

copy_arr = arr.copy()

print(copy_arr)
```

Output:

```text
[1, 2, 3]
```

## Return Value

Returns a new list.

## In-place?

❌ **No**

The original list is not modified.

## Complexity

```text
O(n)
```

Python must copy the references of all `n` elements into the new outer list.

# Three Common Ways to Make a Shallow Copy

Using `copy()`:

```python
copy_arr = arr.copy()
```

Using slicing:

```python
copy_arr = arr[:]
```

Using `list()`:

```python
copy_arr = list(arr)
```

All three create a **new outer list**, but nested mutable objects are still shared.

# 🔥 Assignment Is Not Copying

This is extremely important for DSA.

```python
arr = [1, 2, 3]

arr1 = arr
```

This does **not** create a new list.

Memory representation:

```text
arr ─────┐
         ├──> [1, 2, 3]
arr1 ────┘
```

Both variables reference the same list.

```python
arr1.append(4)

print(arr)
print(arr1)
```

Output:

```text
[1, 2, 3, 4]
[1, 2, 3, 4]
```

Therefore, when you need a shallow copy, prefer:

```python
arr1 = arr[:]
```

or:

```python
arr1 = arr.copy()
```

# ⭐ Shallow Copy

Consider a nested list:

```python
arr = [
    [1, 2],
    [3, 4]
]

copy_arr = arr.copy()
```

The outer lists are different objects:

```python
print(arr is copy_arr)
```

Output:

```text
False
```

But the inner lists are still shared:

```python
print(arr[0] is copy_arr[0])
```

Output:

```text
True
```

Now modify a nested element:

```python
copy_arr[0][0] = 100

print(arr)
print(copy_arr)
```

Output:

```text
[[100, 2], [3, 4]]
[[100, 2], [3, 4]]
```

Why?

Because only the **outer list** was copied.

Conceptually:

```text
arr ───────────────> Outer List A
                         │
                         ├──> Inner List 1
                         └──> Inner List 2

copy_arr ──────────> Outer List B
                         │
                         ├──> Same Inner List 1
                         └──> Same Inner List 2
```

# 🔥 Deep Copy

A deep copy recursively copies nested objects.

```python
import copy

arr = [
    [1, 2],
    [3, 4]
]

deep_copy = copy.deepcopy(arr)
```

Now:

```python
deep_copy[0][0] = 100

print(arr)
print(deep_copy)
```

Output:

```text
[[1, 2], [3, 4]]
[[100, 2], [3, 4]]
```

The original nested list remains unchanged.

# Aliasing vs Shallow Copy vs Deep Copy

| Operation              | Outer Object | Nested Mutable Objects |
| ---------------------- | ------------ | ---------------------- |
| `b = a`                | Same         | Same                   |
| `b = a.copy()`         | Different    | Shared                 |
| `b = a[:]`             | Different    | Shared                 |
| `b = copy.deepcopy(a)` | Different    | Recursively copied     |

# ✂️ List Slicing

Syntax:

```python
list[start:end:step]
```

Example:

```python
arr = [10, 20, 30, 40, 50]

print(arr[1:4])
```

Output:

```text
[20, 30, 40]
```

The `end` index is excluded.

## From the Beginning

```python
arr[:3]
```

Result:

```text
[10, 20, 30]
```

## Until the End

```python
arr[2:]
```

Result:

```text
[30, 40, 50]
```

## Copy the Entire List

```python
copy_arr = arr[:]
```

This creates a **shallow copy**.

## Reverse Using Slicing

```python
reversed_arr = arr[::-1]
```

This creates a **new reversed list**.

It does not modify `arr`.

## Slicing Complexity

If the slice contains `k` elements:

```text
Time:  O(k)
Space: O(k)
```

A new list is created containing references to those `k` elements.

# 🔥 `+` vs `+=` with Lists

This difference is very important when aliasing is involved.

## Using `+=`

```python
a = [1, 2]

b = a

a += [3]

print(a)
print(b)
```

Output:

```text
[1, 2, 3]
[1, 2, 3]
```

For a list, `+=` normally modifies the existing list in place.

Both `a` and `b` still reference the same object.

## Using `+`

```python
a = [1, 2]

b = a

a = a + [3]

print(a)
print(b)
```

Output:

```text
[1, 2, 3]
[1, 2]
```

Here:

```python
a + [3]
```

creates a **new list**, and `a` is rebound to it.

`b` still references the old list.

Conceptually:

```text
Before:

a ───┐
     ├──> [1, 2]
b ───┘


After a = a + [3]:

a ───────> [1, 2, 3]

b ───────> [1, 2]
```

# 🗑️ `del` Keyword

`del` can remove elements, slices, or variable bindings.

## Delete an Element

```python
arr = [10, 20, 30]

del arr[1]

print(arr)
```

Output:

```text
[10, 30]
```

## Delete a Slice

```python
arr = [1, 2, 3, 4, 5]

del arr[1:4]

print(arr)
```

Output:

```text
[1, 5]
```

## Delete the Variable Name

```python
arr = [1, 2, 3]

del arr
```

Now:

```python
print(arr)
```

Raises:

```text
NameError
```

Important:

`del arr` removes the name `arr`.

It does not necessarily destroy the list object immediately if another reference still exists.

Example:

```python
arr = [1, 2, 3]

backup = arr

del arr

print(backup)
```

Output:

```text
[1, 2, 3]
```

# 🔢 Nested Lists and Matrices

A nested list is a list containing other lists.

```python
matrix = [
    [1, 2],
    [3, 4]
]
```

Access an element using two indices:

```python
print(matrix[1][0])
```

Output:

```text
3
```

Here:

```text
matrix[1]     → [3, 4]

matrix[1][0]  → 3
```

# 🚨 The Shared-Row Matrix Bug

Avoid this:

```python
matrix = [[0] * 3] * 3
```

At first, it appears to create:

```text
[
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
```

But the three rows are references to the **same inner list**.

Conceptually:

```text
matrix[0] ───┐
matrix[1] ───┼──> [0, 0, 0]
matrix[2] ───┘
```

Therefore:

```python
matrix[0][0] = 100

print(matrix)
```

Output:

```text
[
    [100, 0, 0],
    [100, 0, 0],
    [100, 0, 0]
]
```

All rows changed because they are the same object.

You can verify this:

```python
print(matrix[0] is matrix[1])
```

Output:

```text
True
```

# ✅ Correct Matrix Creation

Use a list comprehension:

```python
matrix = [[0] * 3 for _ in range(3)]
```

Now every iteration creates a new inner list.

Conceptually:

```text
matrix[0] ───> [0, 0, 0]

matrix[1] ───> [0, 0, 0]

matrix[2] ───> [0, 0, 0]
```

Verify:

```python
print(matrix[0] is matrix[1])
```

Output:

```text
False
```

Now:

```python
matrix[0][0] = 100

print(matrix)
```

Output:

```text
[
    [100, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
```

Only the first row changes.

# 💡 Best Practices

* Use `arr.sort()` when you intentionally want to modify the original list.
* Use `sorted(arr)` when you need to preserve the original order.
* Remember that `sort()` returns `None`.
* Use `arr.copy()` or `arr[:]` when you need a shallow copy.
* Use `copy.deepcopy()` when nested mutable objects must also be independent.
* Understand the difference between assignment and copying.
* Use `+=` carefully when multiple variables reference the same list.
* Never create a mutable 2D matrix using `[[0] * n] * m`.

# ⚠️ Common Mistakes

## Mistake 1

```python
arr = arr.sort()
```

`arr` becomes:

```text
None
```

## Mistake 2

```python
copy_arr = arr
```

This is **aliasing**, not copying.

## Mistake 3

```python
matrix = [[0] * n] * m
```

All rows reference the same inner list.

## Mistake 4

Assuming a shallow copy recursively copies everything.

It only creates a new outer container.

# 🧠 DSA Tips

Understanding references and copying is extremely important when solving:

* Matrix problems
* Backtracking
* Graph problems
* Dynamic Programming
* Recursive problems

For example, in backtracking:

```python
result.append(path)
```

may be wrong if `path` is later modified.

You often need:

```python
result.append(path[:])
```

Why?

Because:

```python
path[:]
```

creates a snapshot of the current list.

This small difference is extremely important in DSA.

# 💼 Interview Questions

1. What is the difference between `sort()` and `sorted()`?
2. Why does `sort()` return `None`?
3. What is a stable sorting algorithm?
4. What is Timsort?
5. What is aliasing?
6. What is a shallow copy?
7. What is a deep copy?
8. What is the difference between `arr.copy()` and `copy.deepcopy(arr)`?
9. Does `arr[:]` create a deep copy?
10. What is the difference between `+` and `+=` for lists?
11. Why is list slicing `O(k)`?
12. Why is `[[0] * n] * m` dangerous?
13. Why do we use `path[:]` while storing backtracking answers?

# 📌 Quick Revision

✔ `sort()` modifies the original list and returns `None`.

✔ `sorted()` returns a new sorted list.

✔ `arr = other` creates an alias, not a copy.

✔ `arr.copy()` creates a shallow copy.

✔ `arr[:]` also creates a shallow copy.

✔ `copy.deepcopy()` recursively copies nested objects.

✔ List slicing takes `O(k)` time and space for `k` copied elements.

✔ For lists, `+=` normally modifies the existing object.

✔ `+` creates a new list.

✔ `del` can remove an element, slice, or variable binding.

✔ Nested lists store references to inner lists.

✔ Never use `[[0] * n] * m` to create an independently mutable matrix.

✔ In backtracking, `path[:]` is commonly used to store a snapshot of the current path.
