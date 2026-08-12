# 🔷 Python Sets

A **set** is an unordered collection of **unique** elements.

Sets are primarily used for:

- Removing duplicates
- Fast membership testing
- Mathematical set operations
- DSA problems involving uniqueness

---

# Why Use Sets?

Use a set when you need:

- Unique values only
- Fast lookup
- Fast insertion
- Fast deletion

Examples

- Remove duplicate elements
- Check if an item exists
- Find common elements
- Find unique elements

---

# Characteristics

| Property | Set |
|----------|-----|
| Ordered | ❌ No |
| Indexed | ❌ No |
| Mutable | ✅ Yes |
| Duplicate Elements | ❌ Not Allowed |
| Hashable | ❌ No |

---

# Creating a Set

```python
numbers = {1, 2, 3}

print(numbers)
```

Output

```
{1, 2, 3}
```

---

# Empty Set ⭐⭐⭐

One of the most common interview questions.

```python
data = {}
```

Output

```python
print(type(data))
```

```
<class 'dict'>
```

This creates an **empty dictionary**, not a set.

Correct way

```python
data = set()
```

Output

```python
print(type(data))
```

```
<class 'set'>
```

---

# Duplicate Elements

```python
numbers = {1, 2, 2, 3, 3, 3}

print(numbers)
```

Output

```
{1, 2, 3}
```

Duplicates are automatically removed.

---

# Mixed Data Types

```python
data = {
    10,
    "Python",
    True,
    5.5
}
```

A set can store different hashable data types.

---

# Why Lists Cannot Be Stored

```python
data = {
    [1,2]
}
```

Output

```
TypeError
```

Lists are mutable.

Only hashable objects can be stored inside a set.

---

# Valid Elements

✅

```python
10
```

```python
"Python"
```

```python
3.14
```

```python
(1,2)
```

```python
frozenset({1,2})
```

---

# Invalid Elements

❌

```python
[1,2]
```

```python
{1,2}
```

```python
{"a":1}
```

---

# Creating Using set()

List

```python
numbers = [1,2,2,3]

result = set(numbers)

print(result)
```

Output

```
{1,2,3}
```

---

Tuple

```python
set((1,2,3))
```

---

String

```python
set("Python")
```

Output

```
{'P','y','t','h','o','n'}
```

Duplicate characters are removed.

---

Dictionary

```python
student = {

    "name":"Nitin",

    "age":23

}

print(set(student))
```

Output

```
{'name','age'}
```

Only dictionary keys are converted.

---

Range

```python
set(range(5))
```

Output

```
{0,1,2,3,4}
```

---

# No Indexing

```python
numbers = {1,2,3}

numbers[0]
```

Output

```
TypeError
```

Sets do not support indexing.

---

# No Slicing

```python
numbers[1:3]
```

Output

```
TypeError
```

Because sets have no index positions.

---

# Membership

```python
numbers = {1,2,3}

print(2 in numbers)
```

Output

```
True
```

Complexity

```
Average O(1)
```

This is one of the biggest advantages of sets.

---

# Length

```python
len(numbers)
```

Complexity

```
O(1)
```

---

# Iteration

```python
for value in numbers:
    print(value)
```

Since sets are unordered, iteration order should not be relied upon.

---

# Adding Elements

## add()

```python
numbers = {1,2}

numbers.add(3)

print(numbers)
```

Output

```
{1,2,3}
```

---

Duplicate Add

```python
numbers.add(3)
```

Nothing happens.

No error is raised.

---

Complexity

```
Average O(1)
```

---

# Updating Multiple Elements

## update()

```python
numbers = {1,2}

numbers.update([3,4,5])

print(numbers)
```

Output

```
{1,2,3,4,5}
```

---

Multiple Iterables

```python
numbers.update(

    [3,4],

    (5,6),

    {7,8}

)
```

---

# Removing Elements

## remove()

```python
numbers = {1,2,3}

numbers.remove(2)

print(numbers)
```

Output

```
{1,3}
```

---

Element Missing

```python
numbers.remove(100)
```

Output

```
KeyError
```

---

Complexity

```
Average O(1)
```

---

# discard()

```python
numbers = {1,2,3}

numbers.discard(2)

print(numbers)
```

Output

```
{1,3}
```

---

Missing Element

```python
numbers.discard(100)
```

Nothing happens.

No error.

---

Difference

| remove() | discard() |
|-----------|-----------|
| Raises KeyError | No Error |

---

# pop()

```python
numbers = {10,20,30}

print(numbers.pop())
```

One arbitrary element is removed and returned.

Because sets are unordered, **do not rely on which element is returned**.

---

Empty Set

```python
set().pop()
```

Output

```
KeyError
```

---

# clear()

```python
numbers = {1,2,3}

numbers.clear()

print(numbers)
```

Output

```
set()
```

Removes every element.

---

# copy()

```python
a = {1,2,3}

b = a.copy()
```

Creates a shallow copy.

---

# Set Comprehension

```python
squares = {

    x*x

    for x in range(5)

}

print(squares)
```

Output

```
{0,1,4,9,16}
```

---

Conditional

```python
evens = {

    x

    for x in range(10)

    if x%2==0

}
```

---

# Removing Duplicates ⭐

Most common use.

```python
numbers = [1,2,2,3,3,4]

unique = list(set(numbers))

print(unique)
```

Output

```
[1,2,3,4]
```

Note

The original ordering is **not guaranteed** after conversion through a set.

---

# Set vs List

| Set | List |
|------|------|
| Unique Elements | Duplicates Allowed |
| No Indexing | Indexed |
| Fast Lookup | Linear Lookup |
| Unordered | Ordered |
| Mutable | Mutable |

---

# DSA Applications

Sets are heavily used for

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

## Membership Lookup

```python
if x in seen:
```

---

## Remove Duplicates

```python
list(set(arr))
```

---

## Sliding Window

```python
window = set()
```

---

# Common Mistakes

❌

```python
{}
```

creates a dictionary.

---

Correct

```python
set()
```

---

❌

Trying

```python
numbers[0]
```

Sets are not indexed.

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

Assuming pop removes the "first" element.

A set has no first element.

---

❌

Using mutable objects inside a set.

```python
{[1,2]}
```

Invalid.

---

# Interview Questions

1. Difference between list and set?
2. Why is `{}` a dictionary?
3. Why can't sets contain duplicates?
4. Difference between remove() and discard()?
5. Difference between add() and update()?
6. Can a set contain another set?
7. Why can't lists be stored in sets?
8. Why are sets used in BFS and DFS?
9. Why is membership testing fast in sets?

---

# Quick Revision

✔ Sets store unique elements.

✔ Sets are mutable.

✔ Sets are unordered.

✔ `{}` creates a dictionary.

✔ `set()` creates an empty set.

✔ Sets support fast membership testing.

✔ Sets do not support indexing.

✔ `remove()` raises an error if missing.

✔ `discard()` does not raise an error.

✔ `pop()` removes an arbitrary element.

✔ Sets are commonly used for visited nodes, duplicate removal, and fast lookups.