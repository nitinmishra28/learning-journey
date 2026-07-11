---

# ⭐ List Comprehensions

List comprehensions provide a concise and efficient way to create lists.

Instead of writing

```python
squares = []

for i in range(5):
    squares.append(i * i)

print(squares)
```

You can write

```python
squares = [i * i for i in range(5)]

print(squares)
```

Output

```
[0, 1, 4, 9, 16]
```

---

## Syntax

```python
[expression for item in iterable]
```

---

## Components

```
Expression

↓

i*i

↓

for

↓

Iterator

↓

range(5)
```

---

## Time Complexity

```
O(n)
```

---

## Space Complexity

```
O(n)
```

---

## Why Use List Comprehensions?

✅ Cleaner code

✅ Faster than a normal for loop (slightly, due to internal optimizations)

✅ Easy to read

---

# Conditional List Comprehension

Create a list containing only even numbers.

```python
even = [x for x in range(10) if x % 2 == 0]

print(even)
```

Output

```
[0,2,4,6,8]
```

---

Odd numbers

```python
odd = [x for x in range(10) if x % 2]

print(odd)
```

Output

```
[1,3,5,7,9]
```

---

# if...else in List Comprehension

Syntax

```python
[value_if_true if condition else value_if_false for item in iterable]
```

Example

```python
result = ["Even" if x % 2 == 0 else "Odd" for x in range(5)]

print(result)
```

Output

```
['Even','Odd','Even','Odd','Even']
```

---

# Nested List Comprehension

Example

```python
matrix = [[1,2],[3,4]]

flatten = [num for row in matrix for num in row]

print(flatten)
```

Output

```
[1,2,3,4]
```

---

Equivalent Loop

```python
flatten = []

for row in matrix:
    for num in row:
        flatten.append(num)
```

---

# Matrix Creation

Correct way

```python
matrix = [[0 for _ in range(3)] for _ in range(3)]
```

Output

```
[
[0,0,0],
[0,0,0],
[0,0,0]
]
```

Every row is independent.

---

# Matrix Transpose

Original

```
1 2 3

4 5 6
```

Transpose

```python
matrix = [

[1,2,3],

[4,5,6]
]

transpose = [

[row[i] for row in matrix]

for i in range(len(matrix[0]))
]

print(transpose)
```

Output

```
[
[1,4],

[2,5],

[3,6]
]
```

---

# enumerate()

One of the most useful built-in functions.

Instead of

```python
for i in range(len(arr)):
    print(i, arr[i])
```

Use

```python
for index, value in enumerate(arr):
    print(index, value)
```

Cleaner and more Pythonic.

---

## Start Index

```python
arr = ["A","B","C"]

for i,v in enumerate(arr,start=1):
    print(i,v)
```

Output

```
1 A

2 B

3 C
```

---

# zip()

Combines multiple iterables.

Example

```python
names = ["Alice","Bob"]

marks = [90,80]

for n,m in zip(names,marks):
    print(n,m)
```

Output

```
Alice 90

Bob 80
```

---

## Unequal Length

```python
a = [1,2,3]

b = [10]

print(list(zip(a,b)))
```

Output

```
[(1,10)]
```

Stops at the shortest iterable.

---

# Unpacking

Example

```python
numbers = [10,20,30]

a,b,c = numbers

print(a,b,c)
```

Output

```
10 20 30
```

---

# Extended Unpacking

```python
numbers = [1,2,3,4,5]

first,*middle,last = numbers

print(first)

print(middle)

print(last)
```

Output

```
1

[2,3,4]

5
```

Very useful in interviews.

---

# any()

Returns True if at least one element is truthy.

```python
print(any([0,0,1]))
```

Output

```
True
```

---

# all()

Returns True only if every element is truthy.

```python
print(all([1,2,3]))
```

Output

```
True
```

---

# sum()

```python
numbers = [1,2,3]

print(sum(numbers))
```

Output

```
6
```

Complexity

```
O(n)
```

---

# min()

```python
print(min([5,2,8]))
```

Output

```
2
```

---

# max()

```python
print(max([5,2,8]))
```

Output

```
8
```

---

# sorted() with Lambda

Sort by second element.

```python
students = [

("Alice",90),

("Bob",75),

("Charlie",85)

]

result = sorted(students,key=lambda x:x[1])

print(result)
```

Output

```
[
('Bob',75),

('Charlie',85),

('Alice',90)
]
```

---

# List Performance Cheat Sheet

| Operation | Complexity |
|-----------|------------|
| Index | O(1) |
| Update | O(1) |
| Append | O(1) Amortized |
| Pop Last | O(1) |
| Pop Front | O(n) |
| Insert Middle | O(n) |
| Remove | O(n) |
| Membership | O(n) |
| Copy | O(n) |
| Reverse | O(n) |
| Sort | O(n log n) |
| Slice | O(k) |
| Extend | O(k) |

---

# When Should You Use Lists?

Use lists when

- Order matters.
- Frequent indexing is required.
- Dynamic resizing is needed.
- Duplicates are allowed.

---

# When Should You Avoid Lists?

Avoid lists when

- Fast membership checking is required.

Use

```
set
```

instead.

---

Avoid lists when

- Frequent insertion/removal from the front is required.

Use

```
collections.deque
```

instead.

---

# DSA Patterns Using Lists

Lists are heavily used in

- Two Pointer
- Sliding Window
- Prefix Sum
- Binary Search
- Dynamic Programming
- Monotonic Stack
- Graph Adjacency Lists
- Matrix Problems
- Backtracking

---

# Common LeetCode Problems

Easy

- Two Sum
- Best Time to Buy and Sell Stock
- Contains Duplicate
- Merge Sorted Array
- Remove Duplicates from Sorted Array

Medium

- 3Sum
- Product of Array Except Self
- Rotate Array
- Spiral Matrix
- Set Matrix Zeroes

Hard

- Trapping Rain Water
- First Missing Positive
- Median of Two Sorted Arrays

---

# Interview Questions

1. Why is append() amortized O(1)?
2. Difference between append() and extend()?
3. Difference between sort() and sorted()?
4. Difference between shallow copy and deep copy?
5. Why is `[[0]*n]*m` incorrect?
6. Difference between `+` and `+=`?
7. Difference between reverse() and reversed()?
8. Why do list methods return None?
9. When should you use a deque instead of a list?
10. Why are Python lists dynamic arrays instead of linked lists?

---

# Quick Revision

✔ Lists are mutable.

✔ Lists store references.

✔ Lists are implemented as dynamic arrays.

✔ append() is amortized O(1).

✔ insert() is O(n).

✔ pop() from the end is O(1).

✔ sort() modifies the original list.

✔ sorted() returns a new list.

✔ copy() creates a shallow copy.

✔ deepcopy() copies nested objects.

✔ List comprehensions are concise and efficient.

✔ enumerate() provides index and value.

✔ zip() combines iterables.

✔ any() checks if at least one value is truthy.

✔ all() checks if every value is truthy.

✔ Use lists for ordered dynamic collections.

✔ Use sets for fast membership tests.

✔ Use deque for efficient front operations.

---

# 🎉 Congratulations!

You have completed **Python Lists**.

You now understand:

- Internal Working
- Memory Allocation
- Dynamic Arrays
- Every Important List Method
- Shallow vs Deep Copy
- Aliasing
- Sorting
- List Comprehensions
- Performance
- DSA Applications
- Interview Questions

This knowledge is enough to confidently solve most array/list problems in Python.

---

# 📝 Practice Problems

## Easy

1. Reverse a List
2. Find Maximum Element
3. Find Second Largest Element
4. Remove Duplicates from a List
5. Rotate a List by K Positions

---

## Medium

1. Merge Intervals
2. Product of Array Except Self
3. 3Sum
4. Spiral Matrix
5. Next Permutation

---

## Hard

1. Trapping Rain Water
2. First Missing Positive
3. Sliding Window Maximum
4. Median of Two Sorted Arrays
5. Largest Rectangle in Histogram