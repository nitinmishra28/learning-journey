---

# 🛠️ List Methods

Python provides many built-in methods to manipulate lists.

Unlike strings, **most list methods modify the original list (in-place)** because lists are **mutable**.

---

# append()

Adds **one element** to the **end** of the list.

## Syntax

```python
list.append(item)
```

## Parameters

- `item` → Any Python object

## Return Value

```
None
```

## In-place?

✅ Yes

The original list is modified.

---

## Example

```python
arr = [10, 20, 30]

result = arr.append(40)

print(arr)

print(result)
```

Output

```
[10, 20, 30, 40]

None
```

---

## Internal Working

Python checks whether the internal array has enough capacity.

If space exists

```
↓

Store new reference

↓

Increase size by 1
```

If capacity is full

```
Allocate Larger Array

↓

Copy References

↓

Append Element

↓

Delete Old Array
```

---

## Time Complexity

| Case | Complexity |
|-------|------------|
| Average | O(1) |
| Worst | O(n) |

Why worst case?

When resizing happens.

---

## Space Complexity

```
O(1)
```

Except during resizing.

---

## Common Mistakes

❌

```python
arr = arr.append(10)
```

Output

```
None
```

Because

```
append()

↓

Returns None
```

Correct

```python
arr.append(10)
```

---

## DSA Tip

Use append() for

- Stack
- DFS
- Dynamic arrays

Very common.

---

# extend()

Adds **multiple elements** from another iterable.

## Syntax

```python
list.extend(iterable)
```

---

## Example

```python
arr = [1,2]

arr.extend([3,4])

print(arr)
```

Output

```
[1,2,3,4]
```

---

## Internal Working

Python iterates through the iterable.

Each element is appended individually.

```
[1,2]

↓

Extend

↓

3

↓

4

↓

[1,2,3,4]
```

---

## Return Value

```
None
```

---

## In-place?

✅ Yes

---

## Complexity

```
O(k)
```

where

```
k

↓

Number of new elements
```

---

## append() vs extend()

Example

```python
arr = [1,2]

arr.append([3,4])

print(arr)
```

Output

```
[1,2,[3,4]]
```

Now

```python
arr = [1,2]

arr.extend([3,4])

print(arr)
```

Output

```
[1,2,3,4]
```

Huge interview question.

---

# insert()

Inserts an element at a given index.

## Syntax

```python
list.insert(index,value)
```

---

Example

```python
arr = [1,2,3]

arr.insert(1,100)

print(arr)
```

Output

```
[1,100,2,3]
```

---

## Internal Working

Python shifts every element to the right.

```
Before

1 2 3

↓

Insert

↓

1 100 2 3
```

---

## Complexity

```
O(n)
```

Because shifting is required.

---

## Return Value

```
None
```

---

## In-place?

✅ Yes

---

# pop()

Removes and returns an element.

## Syntax

```python
list.pop(index=-1)
```

Default

Removes last element.

---

Example

```python
arr = [10,20,30]

value = arr.pop()

print(value)

print(arr)
```

Output

```
30

[10,20]
```

---

Removing middle

```python
arr.pop(1)
```

---

## Internal Working

Last Element

```
Simply decrease size
```

Middle

```
Shift remaining elements
```

---

## Complexity

Last Element

```
O(1)
```

Middle

```
O(n)
```

---

## Return Value

Returns removed element.

---

# remove()

Removes the **first occurrence** of a value.

Syntax

```python
list.remove(value)
```

---

Example

```python
arr = [10,20,30,20]

arr.remove(20)

print(arr)
```

Output

```
[10,30,20]
```

---

## If Value Doesn't Exist

```python
arr.remove(100)
```

Output

```
ValueError
```

---

## Complexity

Search

```
O(n)
```

Shift

```
O(n)
```

Overall

```
O(n)
```

---

# pop() vs remove()

| pop() | remove() |
|---------|----------|
| Uses Index | Uses Value |
| Returns Element | Returns None |
| O(1) at End | O(n) |

Interview Favorite.

---

# clear()

Removes every element.

Example

```python
arr = [1,2,3]

arr.clear()

print(arr)
```

Output

```
[]
```

---

## Return

```
None
```

---

## In-place?

✅ Yes

---

## Complexity

```
O(n)
```

References to all elements are released.

---

# index()

Returns first occurrence index.

```python
arr = [10,20,30]

print(arr.index(20))
```

Output

```
1
```

---

Not Found

```
ValueError
```

---

Complexity

```
O(n)
```

---

# count()

Counts occurrences.

```python
arr = [1,2,2,3]

print(arr.count(2))
```

Output

```
2
```

---

Complexity

```
O(n)
```

---

# reverse()

Reverses the original list.

```python
arr = [1,2,3]

arr.reverse()

print(arr)
```

Output

```
[3,2,1]
```

---

## Return

```
None
```

---

## In-place?

✅ Yes

---

## Complexity

```
O(n)
```

---

# reversed()

Returns an iterator.

```python
arr = [1,2,3]

print(reversed(arr))
```

Output

```
<list_reverseiterator>
```

Convert

```python
list(reversed(arr))
```

Output

```
[3,2,1]
```

---

## reverse() vs reversed()

| reverse() | reversed() |
|------------|------------|
| In-place | New Iterator |
| Returns None | Returns Iterator |
| Changes Original | Doesn't Change |

Interview Favorite.

---

# Method Summary

| Method | In-place | Return | Complexity |
|---------|----------|---------|------------|
| append() | ✅ | None | O(1) Amortized |
| extend() | ✅ | None | O(k) |
| insert() | ✅ | None | O(n) |
| pop() | ✅ | Removed Value | O(1)/O(n) |
| remove() | ✅ | None | O(n) |
| clear() | ✅ | None | O(n) |
| index() | ❌ | int | O(n) |
| count() | ❌ | int | O(n) |
| reverse() | ✅ | None | O(n) |
| reversed() | ❌ | Iterator | O(1) to create |

---

# 💡 Best Practices

✅ Use `append()` to add one element.

✅ Use `extend()` for multiple elements.

✅ Use `pop()` if you need the removed value.

✅ Use `remove()` when you know the value.

✅ Use `reverse()` when modifying the original list.

✅ Use `reversed()` when you need the original list unchanged.

---

# ⚠️ Common Mistakes

❌

```python
arr.append([1,2])
```

thinking

```
↓

[1,2]
```

Actually

```
↓

[[1,2]]
```

---

❌

```python
arr.reverse()

print(arr.reverse())
```

Output

```
None
```

Because

```
reverse()

↓

Returns None
```

---

# 🧠 DSA Tips

- `append()` and `pop()` from the end are ideal for implementing a **stack**.
- Avoid `insert(0, x)` and `pop(0)` in performance-critical code because they are **O(n)**.
- If you need efficient insertions/removals from both ends, use `collections.deque` instead of a list.
- Prefer `extend()` over repeatedly calling `append()` inside a loop when adding another iterable.

---

# 💼 Interview Questions

1. Why does `append()` return `None`?
2. Difference between `append()` and `extend()`?
3. Difference between `pop()` and `remove()`?
4. Why is `insert()` O(n)?
5. Difference between `reverse()` and `reversed()`?
6. Why is `append()` amortized O(1)?
7. Why is `pop()` from the end O(1) but `pop(0)` O(n)?