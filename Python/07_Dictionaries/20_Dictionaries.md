# 🛠️ Python Dictionary Methods

Python provides several built-in methods for working with dictionaries.

Some methods:

* Modify the original dictionary
* Return a value
* Return a dynamic view object
* Return `None`

Understanding these differences is important because dictionary methods do **not** all behave the same way.

# 📚 Methods Covered

* `get()`
* `setdefault()`
* `update()`
* `keys()`
* `values()`
* `items()`
* `pop()`
* `popitem()`
* `clear()`
* `copy()`
* `fromkeys()`
* `del`
* Dictionary assignment
* `in` and `not in`

# 🔍 `get()`

The `get()` method retrieves the value associated with a key.

## Syntax

```python
dictionary.get(key, default)
```

The `default` argument is optional.

## Example

```python
student = {
    "name": "Nitin",
    "age": 23
}

print(student.get("name"))
```

Output:

```text
Nitin
```

## Return Value

If the key exists:

```text
Returns the associated value
```

If the key does not exist:

```text
Returns None
```

unless a custom default value is provided.

## Missing Key

```python
student = {
    "name": "Nitin"
}

print(student.get("age"))
```

Output:

```text
None
```

Unlike:

```python
student["age"]
```

`get()` does not raise a `KeyError` when the key is missing.

# `get()` with a Default Value

```python
student = {
    "name": "Nitin"
}

age = student.get("age", 0)

print(age)
```

Output:

```text
0
```

Important:

The default value is only returned.

It is **not inserted into the dictionary**.

```python
student = {
    "name": "Nitin"
}

age = student.get("age", 0)

print(student)
```

Output:

```text
{'name': 'Nitin'}
```

The key `"age"` was not added.

# `[]` vs `get()`

| `dictionary[key]`                  | `dictionary.get(key)`          |
| ---------------------------------- | ------------------------------ |
| Returns value if key exists        | Returns value if key exists    |
| Raises `KeyError` if missing       | Returns `None` by default      |
| Cannot directly specify a fallback | Can specify a default value    |
| Useful when key must exist         | Useful when key may be missing |

Use:

```python
dictionary[key]
```

when a missing key should be considered an error.

Use:

```python
dictionary.get(key)
```

when the key may legitimately be absent.

# ⭐ Frequency Counting with `get()`

One of the most important dictionary patterns in DSA.

```python
arr = [1, 2, 2, 3, 1, 1]

frequency = {}

for num in arr:
    frequency[num] = frequency.get(num, 0) + 1

print(frequency)
```

Output:

```text
{1: 3, 2: 2, 3: 1}
```

How it works:

For the first `1`:

```python
frequency.get(1, 0)
```

returns:

```text
0
```

Then:

```text
0 + 1
```

becomes:

```text
1
```

So:

```python
frequency[1] = 1
```

For the next occurrence:

```python
frequency.get(1, 0)
```

returns the existing count.

Then we increment it.

Overall time complexity:

```text
O(n)
```

Average additional dictionary lookup/update per element:

```text
O(1)
```

This pattern is extremely common in:

* Frequency counting
* Anagram problems
* Character counting
* Duplicate detection
* Sliding Window
* Hashing problems

# ⚠️ Important `get()` Detail

Consider:

```python
data = {
    "count": None
}

print(data.get("count", 0))
```

Output:

```text
None
```

Why?

Because the key `"count"` exists.

`get()` uses the default only when the key is **missing**, not when the stored value is `None`, `0`, `False`, or another falsy value.

# 🧩 `setdefault()`

`setdefault()` returns the value of a key if it exists.

If the key does not exist, it inserts the key with a default value.

## Syntax

```python
dictionary.setdefault(key, default)
```

## Existing Key

```python
student = {
    "name": "Nitin"
}

result = student.setdefault("name", "Unknown")

print(result)
print(student)
```

Output:

```text
Nitin
{'name': 'Nitin'}
```

Because `"name"` already exists, its value is returned and nothing changes.

## Missing Key

```python
student = {
    "name": "Nitin"
}

result = student.setdefault("age", 23)

print(result)
print(student)
```

Output:

```text
23
{'name': 'Nitin', 'age': 23}
```

The missing key was inserted.

# `get()` vs `setdefault()`

This difference is very important.

## `get()`

```python
data.get("count", 0)
```

Returns the default but does not insert it.

## `setdefault()`

```python
data.setdefault("count", 0)
```

Returns the default and inserts it if the key is missing.

| `get()`                     | `setdefault()`              |
| --------------------------- | --------------------------- |
| Does not modify dictionary  | May modify dictionary       |
| Missing key returns default | Missing key inserts default |
| Good for safe reading       | Good for initialization     |

# ⭐ Grouping with `setdefault()`

Example:

```python
words = ["apple", "ant", "banana", "ball"]

groups = {}

for word in words:
    first_character = word[0]

    groups.setdefault(first_character, []).append(word)

print(groups)
```

Output:

```text
{
    'a': ['apple', 'ant'],
    'b': ['banana', 'ball']
}
```

This works because:

```python
groups.setdefault(first_character, [])
```

returns the existing list if the key already exists.

Otherwise, it creates and stores a new empty list.

Later, we will learn that `collections.defaultdict` is often cleaner for this pattern.

# ⚠️ `setdefault()` Mutable Default Detail

Consider:

```python
data = {}

result = data.setdefault("items", [])

result.append(10)

print(data)
```

Output:

```text
{'items': [10]}
```

Why?

Because `result` and:

```python
data["items"]
```

refer to the same list object.

Conceptually:

```text
result ───────────┐
                  ↓
                [10]
                  ↑
data["items"] ────┘
```

# 🔄 `update()`

The `update()` method adds key-value pairs from another mapping or iterable.

If a key already exists, its value is replaced.

## Syntax

```python
dictionary.update(other)
```

## Adding New Keys

```python
student = {
    "name": "Nitin"
}

student.update({
    "age": 23,
    "language": "Python"
})

print(student)
```

Output:

```text
{
    'name': 'Nitin',
    'age': 23,
    'language': 'Python'
}
```

## Updating Existing Keys

```python
student = {
    "name": "Nitin",
    "age": 22
}

student.update({
    "age": 23
})

print(student)
```

Output:

```text
{'name': 'Nitin', 'age': 23}
```

Existing values are overwritten.

## Return Value

`update()` returns:

```text
None
```

## In-place?

✅ Yes

The original dictionary is modified.

Therefore, avoid:

```python
student = student.update({
    "age": 23
})
```

After this:

```text
student = None
```

Correct:

```python
student.update({
    "age": 23
})
```

# `update()` with Keyword Arguments

```python
student = {
    "name": "Nitin"
}

student.update(age=23, language="Python")

print(student)
```

Output:

```text
{
    'name': 'Nitin',
    'age': 23,
    'language': 'Python'
}
```

When using keyword arguments, the keys are strings.

# `update()` from Key-Value Pairs

```python
data = {}

data.update([
    ("a", 1),
    ("b", 2)
])

print(data)
```

Output:

```text
{'a': 1, 'b': 2}
```

# Complexity of `update()`

If `k` key-value pairs are added or processed:

```text
Average: O(k)
```

Each individual hash-table insertion/update is average `O(1)`.

# 🔑 `keys()`

The `keys()` method returns a view containing dictionary keys.

```python
student = {
    "name": "Nitin",
    "age": 23
}

result = student.keys()

print(result)
```

Output:

```text
dict_keys(['name', 'age'])
```

Important:

`keys()` does **not** return a list.

It returns:

```text
dict_keys
```

# Convert Keys to a List

```python
keys = list(student.keys())

print(keys)
```

Output:

```text
['name', 'age']
```

This conversion takes:

```text
O(n)
```

and creates a new list.

# ⭐ Dictionary Views Are Dynamic

This is an important Python behavior.

```python
student = {
    "name": "Nitin"
}

keys = student.keys()

student["age"] = 23

print(keys)
```

Output:

```text
dict_keys(['name', 'age'])
```

The view reflects changes made to the dictionary.

It is not a snapshot.

Conceptually:

```text
Dictionary
    ↑
    |
Dynamic View
```

# `keys()` and Set-Like Operations

Dictionary key views support useful set-like operations when the involved keys are hashable, as dictionary keys necessarily are.

```python
a = {
    "x": 1,
    "y": 2
}

b = {
    "y": 10,
    "z": 20
}

print(a.keys() & b.keys())
```

Output:

```text
{'y'}
```

Union:

```python
print(a.keys() | b.keys())
```

Output:

```text
{'x', 'y', 'z'}
```

Difference:

```python
print(a.keys() - b.keys())
```

Output:

```text
{'x'}
```

This can be useful when comparing dictionaries.

# 📦 `values()`

Returns a dynamic view of dictionary values.

```python
student = {
    "name": "Nitin",
    "age": 23
}

values = student.values()

print(values)
```

Output:

```text
dict_values(['Nitin', 23])
```

The return type is:

```text
dict_values
```

not a list.

# Convert Values to a List

```python
values = list(student.values())
```

Complexity:

```text
O(n)
```

# Values View Is Dynamic

```python
student = {
    "name": "Nitin"
}

values = student.values()

student["age"] = 23

print(values)
```

The new value is visible through the existing view.

# Membership in `values()`

```python
"Nitin" in student.values()
```

Generally requires scanning values.

Complexity:

```text
O(n)
```

Unlike:

```python
"name" in student
```

which is average:

```text
O(1)
```

# 🧩 `items()`

Returns a dynamic view of key-value pairs.

```python
student = {
    "name": "Nitin",
    "age": 23
}

items = student.items()

print(items)
```

Output:

```text
dict_items([
    ('name', 'Nitin'),
    ('age', 23)
])
```

Each item behaves like a two-element tuple:

```text
(key, value)
```

# Iterating with `items()`

```python
for key, value in student.items():
    print(key, value)
```

Output:

```text
name Nitin
age 23
```

This uses unpacking.

Conceptually:

```text
("name", "Nitin")
        ↓
key = "name"
value = "Nitin"
```

# `items()` Is Also Dynamic

```python
student = {
    "name": "Nitin"
}

items = student.items()

student["age"] = 23

print(items)
```

The new pair appears in the existing view.

# Membership in `items()`

You can check for an exact key-value pair:

```python
student = {
    "name": "Nitin"
}

print(("name", "Nitin") in student.items())
```

Output:

```text
True
```

The pair must match both the key and value.

# Dictionary View Summary

| Method     | Returns       |
| ---------- | ------------- |
| `keys()`   | `dict_keys`   |
| `values()` | `dict_values` |
| `items()`  | `dict_items`  |

These are view objects, not normal lists.

Important properties:

* They reflect dictionary changes dynamically.
* They are iterable.
* They can be converted to lists when a snapshot-like list is needed.
* Key views support set-like operations.
* Item views can also support set-like operations when their elements are hashable.

# 🗑️ `pop()`

Removes a key and returns its value.

## Syntax

```python
dictionary.pop(key)
```

Example:

```python
student = {
    "name": "Nitin",
    "age": 23
}

age = student.pop("age")

print(age)
print(student)
```

Output:

```text
23
{'name': 'Nitin'}
```

## Return Value

Returns the value associated with the removed key.

## In-place?

✅ Yes

The original dictionary is modified.

# Missing Key with `pop()`

```python
student.pop("language")
```

Raises:

```text
KeyError
```

if the key does not exist.

# `pop()` with Default Value

You can provide a default:

```python
result = student.pop("language", "Not Found")

print(result)
```

Output:

```text
Not Found
```

No `KeyError` is raised.

Important:

Unlike `dict.get()`, `pop()` removes the key when it exists.

# Complexity

Average:

```text
O(1)
```

# 🔚 `popitem()`

Removes and returns the most recently inserted key-value pair.

Modern Python dictionaries preserve insertion order, so `popitem()` follows:

```text
LIFO
```

Last In, First Out.

## Example

```python
data = {
    "a": 1,
    "b": 2,
    "c": 3
}

item = data.popitem()

print(item)
print(data)
```

Output:

```text
('c', 3)

{'a': 1, 'b': 2}
```

## Return Value

Returns a tuple:

```text
(key, value)
```

## In-place?

✅ Yes

# Empty Dictionary

```python
data = {}

data.popitem()
```

Raises:

```text
KeyError
```

# Complexity

Average:

```text
O(1)
```

# `pop()` vs `popitem()`

| `pop()`               | `popitem()`                |
| --------------------- | -------------------------- |
| Removes specified key | Removes last inserted pair |
| Returns value         | Returns `(key, value)`     |
| Requires a key        | Takes no key argument      |
| Supports a default    | No default argument        |

# 🧹 `clear()`

Removes all key-value pairs from the dictionary.

```python
student = {
    "name": "Nitin",
    "age": 23
}

result = student.clear()

print(student)
print(result)
```

Output:

```text
{}
None
```

## In-place?

✅ Yes

## Return Value

```text
None
```

# ⭐ `clear()` and Aliasing

This is a very important difference.

```python
a = {
    "x": 1
}

b = a

a.clear()

print(a)
print(b)
```

Output:

```text
{}
{}
```

Why?

Because the original dictionary object was emptied.

Both variables still reference that same object.

Compare that with:

```python
a = {
    "x": 1
}

b = a

a = {}

print(a)
print(b)
```

Output:

```text
{}
{'x': 1}
```

Here:

```python
a = {}
```

creates a new dictionary and rebinds `a`.

It does not modify the old dictionary referenced by `b`.

This is the dictionary version of the important list behavior involving mutation vs rebinding.

# 📋 `copy()`

Creates a shallow copy of a dictionary.

```python
original = {
    "name": "Nitin",
    "age": 23
}

copied = original.copy()

print(copied)
```

Output:

```text
{'name': 'Nitin', 'age': 23}
```

The outer dictionary is a different object.

```python
print(original is copied)
```

Output:

```text
False
```

# Shallow Copy with Mutable Values

Consider:

```python
original = {
    "skills": ["Python", "DSA"]
}

copied = original.copy()
```

The outer dictionaries are different.

But the nested list is shared.

```python
print(original["skills"] is copied["skills"])
```

Output:

```text
True
```

Now:

```python
copied["skills"].append("FastAPI")

print(original)
```

Output:

```text
{
    'skills': ['Python', 'DSA', 'FastAPI']
}
```

Why?

Because `copy()` performs a shallow copy.

Conceptually:

```text
original ───> Dictionary A ───┐
                              ↓
                         Skills List
                              ↑
copied ─────> Dictionary B ───┘
```

# Deep Copy

For independently copied nested mutable objects:

```python
import copy

original = {
    "skills": ["Python", "DSA"]
}

copied = copy.deepcopy(original)
```

Now:

```python
copied["skills"].append("FastAPI")

print(original)
print(copied)
```

Output:

```text
{'skills': ['Python', 'DSA']}

{'skills': ['Python', 'DSA', 'FastAPI']}
```

# Ways to Make a Shallow Dictionary Copy

Using:

```python
copied = original.copy()
```

Using:

```python
copied = dict(original)
```

Using dictionary unpacking:

```python
copied = {**original}
```

All create a new outer dictionary but preserve references to nested objects.

# 🏭 `fromkeys()`

Creates a new dictionary using keys from an iterable.

## Syntax

```python
dict.fromkeys(iterable, value)
```

Example:

```python
keys = ["a", "b", "c"]

data = dict.fromkeys(keys, 0)

print(data)
```

Output:

```text
{
    'a': 0,
    'b': 0,
    'c': 0
}
```

If no value is provided:

```python
data = dict.fromkeys(keys)
```

Output:

```text
{
    'a': None,
    'b': None,
    'c': None
}
```

# 🚨 `fromkeys()` with Mutable Values

This is one of the biggest dictionary traps.

Avoid:

```python
data = dict.fromkeys(
    ["a", "b", "c"],
    []
)
```

All keys receive a reference to the **same list object**.

```python
data["a"].append(10)

print(data)
```

Output:

```text
{
    'a': [10],
    'b': [10],
    'c': [10]
}
```

Why?

Conceptually:

```text
"a" ───┐
       │
"b" ───┼──> Same List
       │
"c" ───┘
```

This is similar to the matrix bug:

```python
[[0] * n] * m
```

# Correct Way for Independent Mutable Values

Use a dictionary comprehension:

```python
data = {
    key: []
    for key in ["a", "b", "c"]
}
```

Now every key receives a new list.

```python
data["a"].append(10)

print(data)
```

Output:

```text
{
    'a': [10],
    'b': [],
    'c': []
}
```

This small detail is extremely important.

# 🗑️ `del` with Dictionaries

The `del` statement removes a key-value pair.

```python
student = {
    "name": "Nitin",
    "age": 23
}

del student["age"]

print(student)
```

Output:

```text
{'name': 'Nitin'}
```

# Missing Key with `del`

```python
del student["language"]
```

Raises:

```text
KeyError
```

Unlike:

```python
student.pop("language", None)
```

which can safely handle a missing key.

# Delete Entire Dictionary Variable

```python
student = {
    "name": "Nitin"
}

del student
```

Now:

```python
print(student)
```

raises:

```text
NameError
```

Important:

`del student` removes the variable binding.

It does not necessarily destroy the dictionary object if another reference still exists.

```python
student = {
    "name": "Nitin"
}

backup = student

del student

print(backup)
```

Output:

```text
{'name': 'Nitin'}
```

# `del` vs `pop()`

| `del dictionary[key]`         | `dictionary.pop(key)`       |
| ----------------------------- | --------------------------- |
| Removes key                   | Removes key                 |
| Does not return removed value | Returns removed value       |
| Missing key raises `KeyError` | Missing key can use default |
| Statement                     | Method                      |

Use `pop()` when you need the removed value.

# 🔎 `in` Operator

Checks whether a key exists.

```python
student = {
    "name": "Nitin"
}

print("name" in student)
```

Output:

```text
True
```

Average complexity:

```text
O(1)
```

# `not in`

```python
print("age" not in student)
```

Output:

```text
True
```

# Check Before Accessing

```python
if "name" in student:
    print(student["name"])
```

This prevents a missing-key `KeyError`.

However, when you only need a fallback value, `get()` is often simpler.

# Dictionary Method Summary

| Method         | Modifies Original? | Return Value           | Average Complexity |
| -------------- | ------------------ | ---------------------- | ------------------ |
| `get()`        | ❌                  | Value/default          | `O(1)`             |
| `setdefault()` | Sometimes          | Value                  | `O(1)`             |
| `update()`     | ✅                  | `None`                 | `O(k)`             |
| `keys()`       | ❌                  | Dynamic key view       | `O(1)` to create   |
| `values()`     | ❌                  | Dynamic value view     | `O(1)` to create   |
| `items()`      | ❌                  | Dynamic item view      | `O(1)` to create   |
| `pop()`        | ✅                  | Removed value          | `O(1)`             |
| `popitem()`    | ✅                  | `(key, value)`         | `O(1)`             |
| `clear()`      | ✅                  | `None`                 | `O(n)`             |
| `copy()`       | ❌                  | New shallow dictionary | `O(n)`             |
| `fromkeys()`   | ❌                  | New dictionary         | `O(n)`             |

Complexities shown for hash-table operations are average-case unless stated otherwise.

# ⭐ In-Place vs Non-In-Place Summary

Methods that modify the dictionary:

```text
update()
setdefault()    → only when key is missing
pop()
popitem()
clear()
```

Methods that do not modify the dictionary:

```text
get()
keys()
values()
items()
copy()
fromkeys()
```

`fromkeys()` creates a new dictionary rather than modifying an existing dictionary.

# 🚨 Mutation During Iteration

Do not change the dictionary's size while directly iterating over it.

Bad:

```python
data = {
    "a": 1,
    "b": 2,
    "c": 3
}

for key in data:
    if data[key] % 2 == 0:
        del data[key]
```

This can raise:

```text
RuntimeError: dictionary changed size during iteration
```

# Safe Approach Using a Copy of Keys

```python
for key in list(data.keys()):
    if data[key] % 2 == 0:
        del data[key]
```

Why is this safe?

Because:

```python
list(data.keys())
```

creates a separate list snapshot.

You iterate over the snapshot while modifying the original dictionary.

# Better Approach: Dictionary Comprehension

When creating filtered data, prefer:

```python
data = {
    "a": 1,
    "b": 2,
    "c": 3
}

data = {
    key: value
    for key, value in data.items()
    if value % 2 != 0
}
```

Result:

```text
{
    'a': 1,
    'c': 3
}
```

Dictionary comprehensions will be covered deeply in the next part.

# 🧠 DSA Patterns from These Methods

## Frequency Counting

```python
frequency = {}

for num in arr:
    frequency[num] = frequency.get(num, 0) + 1
```

## Grouping

```python
groups = {}

for word in words:
    groups.setdefault(word[0], []).append(word)
```

## Safe Lookup

```python
value = mapping.get(key, default_value)
```

## Check Before Processing

```python
if key in mapping:
    ...
```

## Remove and Retrieve

```python
value = mapping.pop(key)
```

## Store Index

```python
index_map = {}

for index, value in enumerate(arr):
    index_map[value] = index
```

This pattern is heavily used in problems such as Two Sum.

# ⚠️ Common Mistakes

## Mistake 1

```python
data = data.update(other)
```

`data` becomes:

```text
None
```

## Mistake 2

Thinking:

```python
data.get("x", [])
```

inserts the list.

It does not.

## Mistake 3

Confusing:

```python
get()
```

with:

```python
setdefault()
```

`get()` only reads.

`setdefault()` may insert.

## Mistake 4

Thinking:

```python
data.keys()
```

returns a list.

It returns a dynamic view.

## Mistake 5

Using:

```python
dict.fromkeys(keys, [])
```

when every key needs an independent list.

All keys share the same list.

## Mistake 6

Thinking:

```python
copied = original.copy()
```

deeply copies nested objects.

It creates only a shallow copy.

## Mistake 7

Modifying dictionary size during direct iteration.

This can raise a `RuntimeError`.

# 💼 Interview Questions

1. What is the difference between `get()` and `[]`?
2. What is the difference between `get()` and `setdefault()`?
3. Does `get()` insert the default value?
4. What happens if an existing key stores `None` and `get()` is called with a default?
5. Why does `update()` return `None`?
6. What do `keys()`, `values()`, and `items()` return?
7. Are dictionary views dynamic?
8. What is the difference between `pop()` and `popitem()`?
9. What does `popitem()` remove in modern Python?
10. What is the difference between `clear()` and `dictionary = {}` when aliases exist?
11. Does `copy()` create a deep copy?
12. Why is `dict.fromkeys(keys, [])` dangerous?
13. What is the difference between `del` and `pop()`?
14. Can you modify a dictionary while iterating over it?
15. How do you safely remove dictionary entries during iteration?
16. How do you count frequencies using `get()`?
17. How can `setdefault()` be used for grouping?
18. What is the complexity of key membership?
19. What is the complexity of value membership?
20. Do `keys()` and `items()` support set-like operations?

# 📌 Quick Revision

✔ `get()` safely retrieves values.

✔ `get()` does not insert missing keys.

✔ `setdefault()` inserts a default when the key is missing.

✔ `update()` modifies the original dictionary and returns `None`.

✔ `keys()`, `values()`, and `items()` return dynamic views.

✔ Dictionary views reflect later dictionary changes.

✔ `keys()` supports set-like operations.

✔ `pop()` removes a specified key and returns its value.

✔ `popitem()` removes the most recently inserted pair.

✔ `clear()` empties the existing dictionary object.

✔ Reassigning `{}` creates and binds a different dictionary.

✔ `copy()` creates a shallow copy.

✔ `deepcopy()` recursively copies nested objects when possible.

✔ `fromkeys()` creates a new dictionary.

✔ Mutable values passed to `fromkeys()` are shared between all keys.

✔ `del` removes a key but does not return its value.

✔ `in` and `not in` check dictionary keys.

✔ Avoid changing dictionary size during direct iteration.

✔ `get()` is one of the most important methods for DSA frequency counting.

✔ `setdefault()` is useful for grouping, though `defaultdict` is often cleaner.
