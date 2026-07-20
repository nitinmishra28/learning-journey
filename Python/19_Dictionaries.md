# 📚 Python Dictionaries

> A dictionary is a mutable mapping that stores data as **key-value pairs**. Dictionaries are one of the most important Python data structures for DSA because they provide average `O(1)` lookup, insertion, and deletion using a hash table.

# 📖 Table of Contents

* What is a Dictionary?
* Why Use Dictionaries?
* Creating Dictionaries
* Key-Value Pairs
* Accessing Values
* Adding New Items
* Updating Existing Items
* Dictionary Keys
* Dictionary Values
* Duplicate Keys
* Mutable vs Immutable Keys
* Internal Working
* Hashing
* Hash Collisions
* Insertion Order
* Membership Checking
* Dictionary Length
* Iterating Through Dictionaries
* Nested Dictionaries
* Dictionary References and Aliasing
* Basic Time Complexity
* Common Mistakes
* DSA Tips
* Interview Questions
* Quick Revision

# 📖 What is a Dictionary?

A dictionary stores data in the form of:

```text
Key → Value
```

Example:

```python
student = {
    "name": "Nitin",
    "age": 23,
    "language": "Python"
}
```

Here:

```text
"name"      → "Nitin"

"age"       → 23

"language"  → "Python"
```

The keys are:

```python
"name"
"age"
"language"
```

The values are:

```python
"Nitin"
23
"Python"
```

The complete combinations are called **key-value pairs** or **items**.

# Dictionary Type

The built-in dictionary type is:

```python
dict
```

Example:

```python
student = {
    "name": "Nitin"
}

print(type(student))
```

Output:

```text
<class 'dict'>
```

# ⭐ Main Characteristics of Dictionaries

Python dictionaries are:

* Mutable
* Dynamic
* Key-value based
* Fast for lookup
* Fast for insertion
* Fast for deletion
* Insertion ordered in modern Python
* Unable to contain duplicate keys

A dictionary can grow and shrink dynamically.

# Why Use Dictionaries?

Suppose we want to store the frequency of numbers.

Using a list may not always be practical.

Example:

```python
numbers = [1000, 5000, 1000]
```

Instead, we can create:

```python
frequency = {
    1000: 2,
    5000: 1
}
```

Now accessing the frequency of `1000` is simple:

```python
print(frequency[1000])
```

Output:

```text
2
```

Average lookup complexity:

```text
O(1)
```

This is why dictionaries are heavily used in DSA.

# Creating an Empty Dictionary

Using curly braces:

```python
data = {}
```

Using `dict()`:

```python
data = dict()
```

Both create an empty dictionary.

```python
print(type(data))
```

Output:

```text
<class 'dict'>
```

# ⚠️ Important: `{}` Creates a Dictionary

This:

```python
data = {}
```

creates an empty dictionary.

It does **not** create an empty set.

To create an empty set:

```python
data = set()
```

This is a common Python interview question.

# Creating a Dictionary with Values

```python
student = {
    "name": "Nitin",
    "age": 23,
    "skills": ["Python", "DSA"]
}
```

Dictionary values can be almost any Python object.

For example:

```python
data = {
    "number": 10,
    "decimal": 3.14,
    "boolean": True,
    "list": [1, 2, 3],
    "tuple": (10, 20),
    "dictionary": {
        "language": "Python"
    }
}
```

# Creating a Dictionary Using `dict()`

You can also create dictionaries using `dict()`.

```python
student = dict(
    name="Nitin",
    age=23
)

print(student)
```

Output:

```text
{'name': 'Nitin', 'age': 23}
```

Important:

When using this form:

```python
dict(name="Nitin")
```

the keys are automatically strings.

# Creating a Dictionary from Key-Value Pairs

```python
data = dict([
    ("name", "Nitin"),
    ("age", 23)
])

print(data)
```

Output:

```text
{'name': 'Nitin', 'age': 23}
```

This works because each inner iterable contains exactly two elements:

```text
Key
↓
Value
```

# Accessing Dictionary Values

Use the key inside square brackets.

```python
student = {
    "name": "Nitin",
    "age": 23
}

print(student["name"])
```

Output:

```text
Nitin
```

Another example:

```python
print(student["age"])
```

Output:

```text
23
```

Average time complexity:

```text
O(1)
```

# 🚨 Accessing a Missing Key

Consider:

```python
student = {
    "name": "Nitin"
}

print(student["age"])
```

Python raises:

```text
KeyError
```

This is extremely important.

Square bracket access:

```python
dictionary[key]
```

assumes that the key exists.

Later, we will learn:

```python
dictionary.get(key)
```

which can safely handle missing keys.

# Adding a New Key-Value Pair

Dictionaries are mutable.

```python
student = {
    "name": "Nitin"
}

student["age"] = 23

print(student)
```

Output:

```text
{'name': 'Nitin', 'age': 23}
```

If the key does not exist:

```text
New key-value pair is added
```

Average complexity:

```text
O(1)
```

# Updating an Existing Value

If the key already exists, assignment updates its value.

```python
student = {
    "name": "Nitin",
    "age": 22
}

student["age"] = 23

print(student)
```

Output:

```text
{'name': 'Nitin', 'age': 23}
```

Important rule:

```python
dictionary[key] = value
```

behaves differently depending on whether the key exists.

```text
Key does not exist
        ↓
Insert new key-value pair


Key already exists
        ↓
Update existing value
```

# Dictionary Keys Must Be Unique

A dictionary cannot contain duplicate keys.

Example:

```python
data = {
    "name": "Nitin",
    "name": "Python"
}

print(data)
```

Output:

```text
{'name': 'Python'}
```

The later value replaces the earlier value.

Conceptually:

```text
"name" → "Nitin"

Then

"name" → "Python"

Result

"name" → "Python"
```

# Dictionary Values Can Be Duplicated

Values do not need to be unique.

```python
data = {
    "a": 10,
    "b": 10,
    "c": 10
}
```

This is completely valid.

Keys:

```text
a
b
c
```

are unique.

Values:

```text
10
10
10
```

can repeat.

# ⭐ What Can Be a Dictionary Key?

Dictionary keys must be **hashable**.

Common valid keys include:

```python
data = {
    "name": "Nitin",
    10: "Integer Key",
    3.14: "Float Key",
    True: "Boolean Key",
    (1, 2): "Tuple Key"
}
```

Common hashable types include:

* Strings
* Integers
* Floats
* Booleans
* Tuples containing only hashable elements
* `frozenset`

# ❌ Lists Cannot Be Dictionary Keys

This is invalid:

```python
data = {
    [1, 2]: "value"
}
```

Python raises:

```text
TypeError: unhashable type: 'list'
```

Why?

Lists are mutable.

Their contents can change.

```python
arr = [1, 2]

arr.append(3)
```

If a mutable object could be used as a dictionary key, its hash-related identity could become unreliable for lookup.

Therefore, lists are not hashable.

# ❌ Dictionaries Cannot Normally Be Dictionary Keys

This is also invalid:

```python
data = {
    {"a": 1}: "value"
}
```

A normal dictionary is mutable and unhashable.

# ⭐ Tuples as Dictionary Keys

Tuples can be dictionary keys when all their elements are hashable.

Example:

```python
locations = {
    (10, 20): "Point A",
    (30, 40): "Point B"
}

print(locations[(10, 20)])
```

Output:

```text
Point A
```

This is extremely useful in DSA.

For example, matrix coordinates can be represented as:

```python
(row, col)
```

and used as dictionary keys.

# ⚠️ Not Every Tuple Is Hashable

This tuple is valid as a key:

```python
(1, 2, 3)
```

But this tuple is not:

```python
(1, [2, 3])
```

Why?

Because it contains a list.

Example:

```python
data = {
    (1, [2, 3]): "value"
}
```

Raises:

```text
TypeError: unhashable type: 'list'
```

Important rule:

> A tuple is hashable only when all objects required for its hash are themselves hashable.

# 🔥 Internal Working of Dictionaries

Python dictionaries are implemented using a **hash table**.

Suppose we create:

```python
student = {
    "name": "Nitin",
    "age": 23
}
```

Conceptually:

```text
Key
 ↓
"name"

Hash Function
 ↓
Hash Value

 ↓

Hash Table Position

 ↓

Value
"Nitin"
```

The dictionary does not normally search every key one by one.

Instead, Python uses the key's hash to locate where the entry should be found.

This is why average dictionary lookup is:

```text
O(1)
```

# What is Hashing?

Hashing converts a hashable object into an integer hash value.

You can inspect a hash using:

```python
print(hash("Python"))
```

Example output might look like:

```text
123456789
```

The exact value should not be relied upon across separate Python runs.

Another example:

```python
print(hash(100))
```

The hash is used internally by:

* Dictionaries
* Sets

# Why Must Keys Be Hashable?

When a key is inserted:

```python
data["name"] = "Nitin"
```

Python conceptually performs:

```text
"name"

↓

hash("name")

↓

Find table location

↓

Store entry
```

When retrieving:

```python
data["name"]
```

Python again computes the hash and uses it to locate the entry efficiently.

If the key's hash could unpredictably change after insertion, Python might no longer be able to find the entry correctly.

This is why dictionary keys must be hashable.

# Hashable Does Not Simply Mean Immutable

A useful beginner rule is:

```text
Immutable objects are often hashable.
Mutable objects are usually unhashable.
```

But the precise requirement is that the object must provide a stable hash and valid equality behavior.

For everyday Python and DSA:

```text
str       → Hashable
int       → Hashable
tuple     → Usually hashable if contents are hashable

list      → Unhashable
dict      → Unhashable
set       → Unhashable
```

# ⭐ Hash Collision

Two different keys can theoretically produce the same hash or map to competing table positions.

This is called a:

```text
Hash Collision
```

Conceptually:

```text
Key A
  ↓
Hash Position 5


Key B
  ↓
Hash Position 5
```

Python's dictionary implementation handles collisions internally.

A collision does **not** mean that one key automatically overwrites another.

Python uses both hashing and equality checks to distinguish keys.

# Average vs Worst-Case Complexity

Dictionary operations are usually:

```text
O(1)
```

But theoretical worst-case behavior can degrade to:

```text
O(n)
```

because of pathological collision behavior.

For normal DSA complexity analysis, dictionary lookup, insertion, and deletion are generally treated as:

```text
O(1) Average
```

# Dictionary Insertion Order ⭐

Modern Python dictionaries preserve insertion order.

Example:

```python
data = {
    "a": 1,
    "b": 2,
    "c": 3
}

for key in data:
    print(key)
```

Output:

```text
a
b
c
```

The order in which keys were inserted is preserved.

Important historical detail:

* Python 3.7+ guarantees insertion order as part of the language specification.
* CPython 3.6 already preserved it as an implementation detail.

# Updating a Key Does Not Move It

Consider:

```python
data = {
    "a": 1,
    "b": 2,
    "c": 3
}

data["b"] = 100

print(data)
```

Output:

```text
{'a': 1, 'b': 100, 'c': 3}
```

The key `"b"` keeps its original position.

Its value changes, but its insertion position does not.

# Delete and Reinsert Changes Position

Example:

```python
data = {
    "a": 1,
    "b": 2,
    "c": 3
}

del data["b"]

data["b"] = 200

print(data)
```

Output:

```text
{'a': 1, 'c': 3, 'b': 200}
```

Because `"b"` was removed and inserted again, it now appears at the end.

# Membership Checking

The `in` operator checks **keys**, not values.

```python
student = {
    "name": "Nitin",
    "age": 23
}

print("name" in student)
```

Output:

```text
True
```

But:

```python
print("Nitin" in student)
```

Output:

```text
False
```

Why?

Because Python checks:

```text
Keys
```

not:

```text
Values
```

To check values:

```python
print("Nitin" in student.values())
```

Output:

```text
True
```

Important performance difference:

```python
key in dictionary
```

Average:

```text
O(1)
```

But:

```python
value in dictionary.values()
```

is generally:

```text
O(n)
```

because Python may need to inspect values one by one.

# Dictionary Length

Use:

```python
len(dictionary)
```

Example:

```python
student = {
    "name": "Nitin",
    "age": 23
}

print(len(student))
```

Output:

```text
2
```

`len()` returns the number of key-value pairs.

Complexity:

```text
O(1)
```

Python stores the dictionary's current size internally.

# Iterating Through a Dictionary

By default, iteration gives keys.

```python
student = {
    "name": "Nitin",
    "age": 23
}

for item in student:
    print(item)
```

Output:

```text
name
age
```

This:

```python
for key in student:
```

is effectively the common way to iterate over keys.

# Iterating Over Keys Explicitly

```python
for key in student.keys():
    print(key)
```

Output:

```text
name
age
```

For normal iteration, this is often unnecessary:

```python
for key in student:
```

is simpler.

# Iterating Over Values

```python
for value in student.values():
    print(value)
```

Output:

```text
Nitin
23
```

# Iterating Over Key-Value Pairs

Use:

```python
items()
```

Example:

```python
for key, value in student.items():
    print(key, value)
```

Output:

```text
name Nitin
age 23
```

This works using tuple unpacking.

Conceptually, `items()` provides pairs like:

```text
("name", "Nitin")
("age", 23)
```

Then:

```python
key, value
```

unpacks each pair.

# Nested Dictionaries

A dictionary can contain another dictionary.

```python
students = {
    "student1": {
        "name": "Nitin",
        "age": 23
    },
    "student2": {
        "name": "Rahul",
        "age": 22
    }
}
```

Access nested data:

```python
print(students["student1"]["name"])
```

Output:

```text
Nitin
```

# Dictionary Values Store References

Just like lists, dictionaries store references to Python objects.

Example:

```python
skills = ["Python", "DSA"]

student = {
    "skills": skills
}
```

Conceptually:

```text
skills ──────────────┐
                     ↓
              ["Python", "DSA"]
                     ↑
student["skills"] ───┘
```

Now:

```python
skills.append("FastAPI")

print(student)
```

Output:

```text
{
    'skills': ['Python', 'DSA', 'FastAPI']
}
```

Why?

Because both references point to the same list object.

This is extremely important when dictionaries contain mutable values.

# Dictionary Aliasing

Consider:

```python
a = {
    "name": "Nitin"
}

b = a
```

This does not create a copy.

Both names reference the same dictionary.

```python
b["age"] = 23

print(a)
```

Output:

```text
{'name': 'Nitin', 'age': 23}
```

Conceptually:

```text
a ───┐
     ├──> Dictionary Object
b ───┘
```

We will cover:

* `copy()`
* Shallow copy
* Deep copy

in detail in the next dictionary part.

# Dictionary Basic Complexity

| Operation        | Average | Worst Case |
| ---------------- | ------: | ---------: |
| Access by key    |  `O(1)` |     `O(n)` |
| Insert           |  `O(1)` |     `O(n)` |
| Update           |  `O(1)` |     `O(n)` |
| Delete by key    |  `O(1)` |     `O(n)` |
| Key membership   |  `O(1)` |     `O(n)` |
| `len()`          |  `O(1)` |     `O(1)` |
| Iterate          |  `O(n)` |     `O(n)` |
| Value membership |  `O(n)` |     `O(n)` |

For normal DSA analysis, hash-table operations are generally treated as average `O(1)`.

# ⚠️ Common Mistakes

## Mistake 1: Accessing a Missing Key

```python
data = {
    "name": "Nitin"
}

print(data["age"])
```

Raises:

```text
KeyError
```

Use `get()` when a key may not exist.

We will cover it in the next part.

## Mistake 2: Thinking `in` Checks Values

```python
data = {
    "name": "Nitin"
}

print("Nitin" in data)
```

Output:

```text
False
```

Because `in` checks keys.

## Mistake 3: Using a List as a Key

```python
data = {
    [1, 2]: "value"
}
```

Raises:

```text
TypeError: unhashable type: 'list'
```

## Mistake 4: Thinking Assignment Creates a Copy

```python
b = a
```

This creates another reference to the same dictionary.

## Mistake 5: Assuming Dictionary Lookup Is Always Guaranteed `O(1)`

The commonly used complexity is:

```text
O(1) Average
```

The theoretical worst case is:

```text
O(n)
```

# 🧠 DSA Tips

Dictionaries are one of the most important tools in Python DSA.

They are heavily used for:

* Frequency counting
* Hash maps
* Two Sum
* Prefix Sum
* Sliding Window
* Memoization
* Graph representation
* Mapping values to indices
* Grouping elements
* Caching previously computed results

A very common DSA pattern is:

```python
frequency = {}

for num in arr:
    frequency[num] = frequency.get(num, 0) + 1
```

This counts frequencies in:

```text
O(n)
```

Instead of repeatedly using:

```python
arr.count(num)
```

which can lead to:

```text
O(n²)
```

when called for every element.

We will cover frequency counting deeply in the next parts.

# 💼 Interview Questions

1. What is a dictionary in Python?
2. How is a Python dictionary implemented internally?
3. Why is dictionary lookup average `O(1)`?
4. What is hashing?
5. What is a hash collision?
6. Can a list be used as a dictionary key?
7. Can a tuple be used as a dictionary key?
8. Why must dictionary keys be hashable?
9. Can dictionary values be duplicated?
10. Can dictionary keys be duplicated?
11. What happens when the same key is inserted twice?
12. Does `in` check dictionary keys or values?
13. Do dictionaries preserve insertion order?
14. What happens when a key is updated?
15. What happens to order when a key is deleted and reinserted?
16. What is the difference between aliasing and copying?
17. Why are dictionaries useful in DSA?

# 📌 Quick Revision

✔ Dictionaries store key-value pairs.

✔ Dictionaries are mutable.

✔ Dictionary keys must be hashable.

✔ Dictionary values can contain almost any Python object.

✔ Keys must be unique.

✔ Values can be duplicated.

✔ Dictionaries use a hash-table-based implementation.

✔ Key lookup is average `O(1)`.

✔ Key insertion is average `O(1)`.

✔ Key deletion is average `O(1)`.

✔ `len(dictionary)` is `O(1)`.

✔ `key in dictionary` checks keys.

✔ Key membership is average `O(1)`.

✔ Value membership is generally `O(n)`.

✔ Modern dictionaries preserve insertion order.

✔ Updating an existing key does not change its position.

✔ Deleting and reinserting a key moves it to the end.

✔ Lists cannot be dictionary keys.

✔ Tuples can be keys when their contents are hashable.

✔ `a = b` does not copy a dictionary.

✔ Dictionaries store references to objects.

✔ Dictionaries are heavily used for hashing and frequency-based DSA problems.
