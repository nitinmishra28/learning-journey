---

# 🔄 sort()

Sorts the original list in ascending order.

## Syntax

```python
list.sort(key=None, reverse=False)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| key | Function used for custom sorting |
| reverse | Sort in descending order if True |

---

## Example

```python
arr = [5,2,4,1]

arr.sort()

print(arr)
```

Output

```
[1,2,4,5]
```

---

## Return Value

```
None
```

---

## In-place?

✅ Yes

The original list is modified.

---

## Internal Working

Python uses **Timsort**.

Timsort is a hybrid sorting algorithm based on

- Merge Sort
- Insertion Sort

Advantages

- Stable
- Fast on partially sorted data
- Worst Case

```
O(n log n)
```

---

## Complexity

| Case | Complexity |
|-------|------------|
| Best | O(n) |
| Average | O(n log n) |
| Worst | O(n log n) |

Space

```
O(n)
```

---

## Stable Sort ⭐

Timsort is stable.

Equal elements keep their original order.

Example

```python
students = [

("Alice",90),

("Bob",90),

("Charlie",80)

]

students.sort(key=lambda x:x[1])

print(students)
```

Output

```
[
('Charlie',80),
('Alice',90),
('Bob',90)
]
```

Alice remains before Bob.

---

## Descending Order

```python
arr.sort(reverse=True)
```

Output

```
[5,4,2,1]
```

---

## Sorting by Key

Length

```python
words = ["apple","hi","banana"]

words.sort(key=len)

print(words)
```

Output

```
['hi','apple','banana']
```

---

# sorted()

Returns a **new sorted list**.

Original list remains unchanged.

---

## Syntax

```python
sorted(iterable,key=None,reverse=False)
```

---

Example

```python
arr = [5,2,4,1]

new_arr = sorted(arr)

print(arr)

print(new_arr)
```

Output

```
[5,2,4,1]

[1,2,4,5]
```

---

## Return Value

```
New List
```

---

## In-place?

❌ No

---

## Complexity

```
O(n log n)
```

---

# sort() vs sorted()

| sort() | sorted() |
|----------|-----------|
| List Method | Built-in Function |
| In-place | Returns New List |
| Returns None | Returns Sorted List |
| Works only on Lists | Works on Any Iterable |
| Memory Efficient | Uses Extra Memory |

---

# Common Mistake

```python
arr = [5,2,1]

arr = arr.sort()
```

Output

```
None
```

Because

```
sort()

↓

Returns None
```

Correct

```python
arr.sort()
```

---

# copy()

Creates a **shallow copy**.

---

## Syntax

```python
list.copy()
```

---

Example

```python
arr = [1,2,3]

copy_arr = arr.copy()

print(copy_arr)
```

Output

```
[1,2,3]
```

---

## Return Value

```
New List
```

---

## In-place?

❌ No

---

## Complexity

```
O(n)
```

---

# Slicing Copy

```python
copy_arr = arr[:]
```

Also creates a shallow copy.

---

# list()

```python
copy_arr = list(arr)
```

Another shallow copy.

---

# Three Ways to Copy

```python
arr.copy()

arr[:]

list(arr)
```

All create **shallow copies**.

---

# Shallow Copy ⭐⭐⭐

One of the most important Python interview questions.

Example

```python
arr = [

[1,2],

[3,4]

]

copy_arr = arr.copy()

copy_arr[0][0] = 100

print(arr)
```

Output

```
[[100,2],

[3,4]]
```

Why?

Only the outer list is copied.

Inner lists are shared.

Memory

```
Original

↓

Outer List

↓

Inner List

Copy

↓

New Outer List

↓

Same Inner List
```

---

# Deep Copy

Creates copies of every nested object.

```python
import copy

deep = copy.deepcopy(arr)
```

Now

```python
deep[0][0] = 100
```

Original remains unchanged.

---

# Aliasing

```python
a = [1,2]

b = a
```

Memory

```
a

↓

List

↑

b
```

Only one list exists.

Modify

```python
b.append(3)
```

Output

```
[1,2,3]
```

Both variables see the change.

---

# Aliasing vs Copy

| Aliasing | Copy |
|----------|------|
| Same Object | Different Object |
| Same Memory | Different Memory |
| Changes Reflect | Independent |

---

# List Slicing

Syntax

```python
list[start:end:step]
```

---

Example

```python
arr = [10,20,30,40,50]

print(arr[1:4])
```

Output

```
[20,30,40]
```

---

Beginning

```python
arr[:3]
```

---

End

```python
arr[2:]
```

---

Entire List

```python
arr[:]
```

---

Reverse

```python
arr[::-1]
```

---

## Complexity

```
O(k)
```

Where

```
k

↓

Elements Copied
```

---

# + vs +=

Example

```python
a = [1,2]

b = a

a += [3]
```

Output

```
b

↓

[1,2,3]
```

Same object modified.

---

Now

```python
a = [1,2]

b = a

a = a + [3]
```

Memory

```
New List
```

Output

```
a

↓

[1,2,3]

b

↓

[1,2]
```

Huge interview question.

---

# del Keyword

Delete Index

```python
del arr[2]
```

---

Delete Slice

```python
del arr[2:5]
```

---

Delete Entire Variable

```python
del arr
```

After this

```python
print(arr)
```

Output

```
NameError
```

---

# Nested Lists

```python
matrix = [

[1,2],

[3,4]
]
```

Access

```python
matrix[1][0]
```

Output

```
3
```

---

# Biggest Python Bug ⭐⭐⭐

Never do

```python
matrix = [[0]*3]*3
```

Looks correct.

Actually

```
All rows

↓

Same List
```

Example

```python
matrix[0][0] = 100

print(matrix)
```

Output

```
[[100,0,0],

[100,0,0],

[100,0,0]]
```

---

Correct

```python
matrix = [

[0]*3

for _ in range(3)

]
```

Now

Every row is independent.

---

# Best Practices

✅ Use

```python
arr.copy()
```

or

```python
arr[:]
```

instead of aliasing.

---

✅ Prefer

```python
sorted()
```

when original data must remain unchanged.

---

✅ Use

```python
sort()
```

when memory matters.

---

✅ Never use

```python
[[0]*n]*m
```

for matrices.

---

# Common Mistakes

❌

```python
arr = arr.sort()
```

---

❌

```python
copy = arr
```

thinking

```
Copy
```

Actually

```
Alias
```

---

❌

Using

```python
a = a + [x]
```

inside loops.

Creates many temporary lists.

---

# DSA Tips

✅ Learn

- sort()

- sorted()

Very important.

---

✅ Understand shallow copy before solving graph or matrix problems.

---

✅ Prefer list comprehensions for matrix creation.

---

✅ Never create 2D arrays using

```python
[[0]*n]*m
```

---

# Interview Questions

1. Difference between sort() and sorted()?

2. Why does sort() return None?

3. Explain Timsort.

4. Difference between shallow and deep copy?

5. Difference between copy() and aliasing?

6. Difference between + and += ?

7. Why is slicing O(k)?

8. Why is [[0]*n]*m dangerous?

---

# Quick Revision

✔ sort() modifies original list.

✔ sorted() returns new list.

✔ copy() creates shallow copy.

✔ deepcopy() creates independent copy.

✔ Slicing creates a new list.

✔ Lists store references.

✔ Avoid aliasing unless intentional.

✔ Never create matrices using

```python
[[0]*n]*m
```