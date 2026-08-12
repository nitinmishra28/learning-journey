# 🚀 Advanced Python Dictionaries and DSA Patterns

This section covers advanced dictionary features that are especially useful in:

* DSA
* Backend development
* Data processing
* Python interviews

Topics include:

* Dictionary comprehensions
* Conditional comprehensions
* Dictionary merging
* `|` and `|=`
* `**` dictionary unpacking
* Sorting dictionaries
* Reversing dictionaries
* `defaultdict`
* `Counter`
* `OrderedDict`
* Dictionary equality
* Important key edge cases
* Frequency maps
* Index maps
* Two Sum pattern
* Grouping
* Prefix Sum + Hash Map
* Sliding Window frequency maps
* Memoization
* Graph adjacency lists
* Common mistakes
* Performance cheat sheet

# ⭐ Dictionary Comprehension

Dictionary comprehensions provide a concise way to create dictionaries.

Normal approach:

```python
squares = {}

for num in range(1, 6):
    squares[num] = num * num

print(squares)
```

Output:

```text
{
    1: 1,
    2: 4,
    3: 9,
    4: 16,
    5: 25
}
```

Using a dictionary comprehension:

```python
squares = {
    num: num * num
    for num in range(1, 6)
}

print(squares)
```

## Syntax

```python
{
    key_expression: value_expression
    for item in iterable
}
```

Example:

```python
numbers = [1, 2, 3]

result = {
    num: num * 10
    for num in numbers
}
```

Output:

```text
{
    1: 10,
    2: 20,
    3: 30
}
```

## Complexity

If the iterable contains `n` elements:

```text
Time:  O(n)
Space: O(n)
```

assuming average `O(1)` dictionary insertion and constant-time expressions.

# Conditional Dictionary Comprehension

You can filter elements using a condition.

```python
numbers = [1, 2, 3, 4, 5, 6]

even_squares = {
    num: num * num
    for num in numbers
    if num % 2 == 0
}

print(even_squares)
```

Output:

```text
{
    2: 4,
    4: 16,
    6: 36
}
```

Syntax:

```python
{
    key: value
    for item in iterable
    if condition
}
```

# `if...else` in Dictionary Comprehension

You can conditionally choose a value.

```python
numbers = [1, 2, 3, 4]

result = {
    num: "Even" if num % 2 == 0 else "Odd"
    for num in numbers
}

print(result)
```

Output:

```text
{
    1: 'Odd',
    2: 'Even',
    3: 'Odd',
    4: 'Even'
}
```

Important difference:

Filtering:

```python
{
    x: x * x
    for x in numbers
    if x % 2 == 0
}
```

Some elements are excluded.

Conditional value:

```python
{
    x: "Even" if x % 2 == 0 else "Odd"
    for x in numbers
}
```

Every element produces an entry.

# Transforming an Existing Dictionary

```python
prices = {
    "apple": 100,
    "banana": 50
}

discounted = {
    key: value * 0.9
    for key, value in prices.items()
}

print(discounted)
```

Output:

```text
{
    'apple': 90.0,
    'banana': 45.0
}
```

# Duplicate Keys in Dictionary Comprehensions

Keys must remain unique.

```python
result = {
    num % 2: num
    for num in range(5)
}

print(result)
```

Output:

```text
{
    0: 4,
    1: 3
}
```

Why?

Generated keys are:

```text
0 → 0
1 → 1
0 → 2
1 → 3
0 → 4
```

Later values overwrite earlier values for the same key.

This is an important detail when creating dictionaries using comprehensions.

# 🔀 Dictionary Merging Using `|`

Python 3.9+ supports the dictionary union operator:

```python
|
```

Example:

```python
a = {
    "x": 1,
    "y": 2
}

b = {
    "z": 3
}

result = a | b

print(result)
```

Output:

```text
{
    'x': 1,
    'y': 2,
    'z': 3
}
```

## Does `|` Modify the Original?

❌ No.

It creates a new dictionary.

```python
print(a)
print(b)
```

Both original dictionaries remain unchanged.

# Duplicate Keys with `|`

```python
a = {
    "x": 1,
    "y": 2
}

b = {
    "y": 100,
    "z": 3
}

result = a | b
```

Output:

```text
{
    'x': 1,
    'y': 100,
    'z': 3
}
```

When keys overlap:

```text
Right Dictionary Wins
```

So:

```python
a | b
```

and:

```python
b | a
```

may produce different values.

# `|=` Dictionary Merge

The operator:

```python
|=
```

updates the dictionary on the left.

```python
a = {
    "x": 1
}

b = {
    "y": 2
}

a |= b

print(a)
```

Output:

```text
{
    'x': 1,
    'y': 2
}
```

## In-place?

Conceptually, `|=` updates the left-hand dictionary rather than creating a separate result for normal dictionary usage.

If aliases exist:

```python
a = {
    "x": 1
}

b = a

a |= {
    "y": 2
}

print(b)
```

Output:

```text
{
    'x': 1,
    'y': 2
}
```

Both references observe the update.

# `|` vs `|=`

| `|` | `|=` |
|---|---|
| Creates a new dictionary | Updates left dictionary |
| Originals remain unchanged | Left dictionary changes |
| Returns merged dictionary | Assignment updates left target |

# 📦 Dictionary Unpacking with `**`

The `**` operator can unpack dictionary key-value pairs.

```python
a = {
    "x": 1
}

b = {
    "y": 2
}

result = {
    **a,
    **b
}

print(result)
```

Output:

```text
{
    'x': 1,
    'y': 2
}
```

# Duplicate Keys with `**`

```python
a = {
    "x": 1
}

b = {
    "x": 100
}

result = {
    **a,
    **b
}
```

Output:

```text
{
    'x': 100
}
```

Later unpacked values win.

Conceptually:

```text
Earlier Dictionary
        ↓
Later Dictionary
        ↓
Later Value Wins
```

# Merge Multiple Dictionaries

```python
a = {"a": 1}
b = {"b": 2}
c = {"c": 3}

result = {
    **a,
    **b,
    **c
}
```

# `update()` vs `|` vs `**`

| Method        | Modifies Original? | Returns             |
| ------------- | ------------------ | ------------------- |
| `a.update(b)` | Yes                | `None`              |
| `a \| b`      | No                 | New dictionary      |
| `a \|= b`     | Yes                | Updated left target |
| `{**a, **b}`  | No                 | New dictionary      |

# ⭐ Dictionary Unpacking in Function Calls

Suppose:

```python
def introduce(name, age):
    print(name, age)
```

Dictionary:

```python
person = {
    "name": "Nitin",
    "age": 23
}
```

You can write:

```python
introduce(**person)
```

Conceptually:

```python
introduce(
    name="Nitin",
    age=23
)
```

Important:

The dictionary keys must match valid parameter names expected by the function.

# 🔃 Sorting Dictionaries

Dictionaries preserve insertion order, but they are not automatically sorted.

Consider:

```python
data = {
    "c": 3,
    "a": 1,
    "b": 2
}
```

# Sorting Dictionary Keys

```python
result = sorted(data)

print(result)
```

Output:

```text
['a', 'b', 'c']
```

Important:

```python
sorted(data)
```

returns a:

```text
List of sorted keys
```

It does not return a dictionary.

The original dictionary remains unchanged.

# Sorting `keys()`

```python
result = sorted(data.keys())
```

Output:

```text
['a', 'b', 'c']
```

This is effectively similar to:

```python
sorted(data)
```

# Sorting Dictionary Values

```python
result = sorted(data.values())

print(result)
```

Output:

```text
[1, 2, 3]
```

This returns a list of sorted values.

# Sorting Dictionary Items by Key

```python
result = sorted(data.items())

print(result)
```

Output:

```text
[
    ('a', 1),
    ('b', 2),
    ('c', 3)
]
```

This returns a list of tuples.

# Creating a Dictionary Sorted by Key

```python
sorted_dict = dict(
    sorted(data.items())
)

print(sorted_dict)
```

Output:

```text
{
    'a': 1,
    'b': 2,
    'c': 3
}
```

Because dictionaries preserve insertion order, the newly created dictionary keeps the sorted insertion order.

# Sorting Dictionary by Value

```python
data = {
    "a": 30,
    "b": 10,
    "c": 20
}

result = dict(
    sorted(
        data.items(),
        key=lambda item: item[1]
    )
)

print(result)
```

Output:

```text
{
    'b': 10,
    'c': 20,
    'a': 30
}
```

Here:

```python
lambda item: item[1]
```

uses the value as the sorting key.

# Descending Sort by Value

```python
result = dict(
    sorted(
        data.items(),
        key=lambda item: item[1],
        reverse=True
    )
)
```

Output:

```text
{
    'a': 30,
    'c': 20,
    'b': 10
}
```

Complexity:

```text
O(n log n)
```

# Sorting by Multiple Conditions

Suppose:

```python
frequency = {
    "a": 2,
    "b": 3,
    "c": 2
}
```

Sort by:

1. Frequency
2. Key

```python
result = sorted(
    frequency.items(),
    key=lambda item: (
        item[1],
        item[0]
    )
)
```

Tuple sorting compares values from left to right.

This technique is very useful in DSA.

# 🔄 Reverse Mapping

Suppose:

```python
student = {
    "Alice": 1,
    "Bob": 2,
    "Charlie": 3
}
```

Reverse it:

```python
reversed_dict = {
    value: key
    for key, value in student.items()
}

print(reversed_dict)
```

Output:

```text
{
    1: 'Alice',
    2: 'Bob',
    3: 'Charlie'
}
```

# 🚨 Duplicate Values While Reversing

Consider:

```python
data = {
    "a": 1,
    "b": 1
}
```

Reverse:

```python
result = {
    value: key
    for key, value in data.items()
}
```

Output:

```text
{
    1: 'b'
}
```

The `"a"` mapping is lost because dictionary keys must be unique.

If multiple keys can share the same value, use grouping instead.

Example:

```python
result = {}

for key, value in data.items():
    result.setdefault(value, []).append(key)
```

Output:

```text
{
    1: ['a', 'b']
}
```

# 📦 `defaultdict`

`defaultdict` comes from:

```python
from collections import defaultdict
```

It is a subclass of `dict`.

It automatically creates a default value when a missing key is accessed using square brackets.

# Normal Dictionary Problem

```python
frequency = {}

frequency["a"] += 1
```

This raises:

```text
KeyError
```

because `"a"` does not exist yet.

# Using `defaultdict(int)`

```python
from collections import defaultdict

frequency = defaultdict(int)

frequency["a"] += 1

print(frequency["a"])
```

Output:

```text
1
```

Why?

`int()` returns:

```text
0
```

So a missing key behaves as if initialized to `0`, and accessing it inserts the key.

# Common `defaultdict` Factories

```python
defaultdict(int)
```

Default:

```text
0
```

```python
defaultdict(list)
```

Default:

```text
[]
```

```python
defaultdict(set)
```

Default:

```text
set()
```

# Frequency Counting with `defaultdict`

```python
from collections import defaultdict

arr = [1, 2, 1, 3, 1]

frequency = defaultdict(int)

for num in arr:
    frequency[num] += 1

print(frequency)
```

# Grouping with `defaultdict(list)`

```python
from collections import defaultdict

words = [
    "apple",
    "ant",
    "banana",
    "ball"
]

groups = defaultdict(list)

for word in words:
    groups[word[0]].append(word)

print(dict(groups))
```

Output:

```text
{
    'a': ['apple', 'ant'],
    'b': ['banana', 'ball']
}
```

This is often cleaner than:

```python
groups.setdefault(key, []).append(value)
```

# 🚨 `defaultdict` Missing-Key Side Effect

This is extremely important.

```python
from collections import defaultdict

data = defaultdict(int)

print(data)
```

Initially:

```text
defaultdict(<class 'int'>, {})
```

Now:

```python
print(data["missing"])
```

Output:

```text
0
```

But the key is now inserted.

```python
print(data)
```

Conceptually:

```text
{
    'missing': 0
}
```

Unlike:

```python
data.get("missing")
```

which does not create the key.

# `defaultdict` Membership

This:

```python
"missing" in data
```

does not itself create the key.

The automatic creation happens when the missing key is accessed through:

```python
data["missing"]
```

# 🔢 `Counter`

`Counter` comes from:

```python
from collections import Counter
```

It is designed for counting hashable objects.

Example:

```python
from collections import Counter

arr = [1, 2, 1, 3, 1, 2]

frequency = Counter(arr)

print(frequency)
```

Output:

```text
Counter({
    1: 3,
    2: 2,
    3: 1
})
```

# Character Frequency

```python
from collections import Counter

text = "banana"

frequency = Counter(text)

print(frequency)
```

Output:

```text
Counter({
    'a': 3,
    'n': 2,
    'b': 1
})
```

# Access Missing Counter Key

```python
frequency = Counter({
    "a": 3
})

print(frequency["b"])
```

Output:

```text
0
```

Unlike a normal dictionary, it does not raise a `KeyError` for a missing count.

An important detail is that simply reading a missing key this way does not need to insert it as a stored entry.

# `most_common()`

```python
frequency = Counter(
    "banana"
)

print(frequency.most_common())
```

Output:

```text
[
    ('a', 3),
    ('n', 2),
    ('b', 1)
]
```

Top two:

```python
frequency.most_common(2)
```

Output:

```text
[
    ('a', 3),
    ('n', 2)
]
```

Very useful for:

* Top K Frequent Elements
* Character frequency
* Word frequency

# `Counter.elements()`

```python
from collections import Counter

count = Counter({
    "a": 2,
    "b": 1
})

print(list(count.elements()))
```

Output:

```text
['a', 'a', 'b']
```

Counts less than `1` are ignored by `elements()`.

# Updating a Counter

```python
count = Counter("abc")

count.update("abb")
```

The counts are added rather than simply replaced.

Conceptually:

```text
Before

a → 1
b → 1
c → 1

Add

a → 1
b → 2

Result

a → 2
b → 3
c → 1
```

# `Counter.subtract()`

```python
count = Counter({
    "a": 5,
    "b": 3
})

count.subtract({
    "a": 2,
    "b": 5
})

print(count)
```

Counts can become zero or negative.

This is an important difference from a normal frequency map that you may manually clean up.

# Counter Arithmetic

Counters support useful operations.

```python
a = Counter({
    "x": 3,
    "y": 1
})

b = Counter({
    "x": 1,
    "y": 2
})
```

Addition:

```python
a + b
```

Subtraction:

```python
a - b
```

Intersection-like minimum:

```python
a & b
```

Union-like maximum:

```python
a | b
```

For these multiset operations, non-positive results are generally omitted from the resulting Counter.

# `Counter` vs Normal Dictionary

| Normal Dictionary                | `Counter`                    |
| -------------------------------- | ---------------------------- |
| General-purpose mapping          | Specialized counting mapping |
| Missing key may raise `KeyError` | Missing count returns `0`    |
| Manual frequency counting        | Direct counting              |
| No `most_common()`               | Supports `most_common()`     |

# `Counter` vs `defaultdict(int)`

Use `Counter` when the primary task is counting.

Use `defaultdict(int)` when you need more customized counting or state-management logic.

# 🕰️ `OrderedDict`

Import:

```python
from collections import OrderedDict
```

Before normal dictionaries officially guaranteed insertion order, `OrderedDict` was commonly used when order mattered.

Modern Python dictionaries already preserve insertion order.

Therefore, for most cases:

```python
dict
```

is enough.

However, `OrderedDict` still provides specialized order-related behavior and methods such as:

```python
move_to_end()
```

and ordered popping behavior.

Example:

```python
from collections import OrderedDict

data = OrderedDict()

data["a"] = 1
data["b"] = 2

data.move_to_end("a")

print(data)
```

Now `"a"` appears after `"b"`.

For normal DSA problems, you will usually use a regular dictionary.

# ⚖️ Dictionary Equality

Dictionary equality does not depend on insertion order.

```python
a = {
    "x": 1,
    "y": 2
}

b = {
    "y": 2,
    "x": 1
}

print(a == b)
```

Output:

```text
True
```

Why?

Both dictionaries contain the same key-value mappings.

Order does not affect normal dictionary equality.

# Dictionary Identity vs Equality

```python
a = {
    "x": 1
}

b = {
    "x": 1
}
```

Then:

```python
print(a == b)
```

Output:

```text
True
```

But:

```python
print(a is b)
```

Output:

```text
False
```

Why?

```text
==

Checks content equality


is

Checks object identity
```

This distinction is important throughout Python.

# 🚨 Important Key Edge Case: `True`, `1`, and `1.0`

Python considers:

```python
True == 1
```

as:

```text
True
```

And:

```python
1 == 1.0
```

also evaluates to:

```text
True
```

Their hashes are also compatible for dictionary-key purposes.

Therefore:

```python
data = {
    True: "Boolean",
    1: "Integer",
    1.0: "Float"
}

print(data)
```

The entries behave as the same dictionary key, so later assignments replace the value associated with that key rather than creating three independent entries.

This is an advanced but useful interview edge case.

# 🚨 `float("nan")` Key Edge Case

`NaN` has unusual equality behavior:

```python
nan = float("nan")

print(nan == nan)
```

Output:

```text
False
```

Because of its special equality semantics, using independently created NaN values as dictionary keys can behave unexpectedly.

For normal DSA work, avoid relying on NaN as a dictionary key unless you understand its identity, hashing, and equality behavior.

# 🧠 DSA Pattern 1: Frequency Map

One of the most common dictionary patterns.

```python
arr = [1, 2, 2, 3, 1, 1]

frequency = {}

for num in arr:
    frequency[num] = frequency.get(num, 0) + 1
```

Result:

```text
{
    1: 3,
    2: 2,
    3: 1
}
```

Complexity:

```text
Time:  O(n)
Space: O(k)
```

Where `k` is the number of distinct elements.

Used in:

* Valid Anagram
* Majority Element
* Duplicate detection
* Frequency sorting
* Sliding Window
* Top K Frequent Elements

# 🧠 DSA Pattern 2: Index Map

Store:

```text
Value → Index
```

Example:

```python
arr = [10, 20, 30]

index_map = {}

for index, value in enumerate(arr):
    index_map[value] = index
```

Result:

```text
{
    10: 0,
    20: 1,
    30: 2
}
```

Average lookup:

```text
O(1)
```

# 🧠 DSA Pattern 3: Two Sum

Brute force:

```text
O(n²)
```

Using a dictionary:

```python
def two_sum(nums, target):
    seen = {}

    for index, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [
                seen[complement],
                index
            ]

        seen[num] = index
```

How it works:

```text
Current Number
      ↓
Need = Target - Current
      ↓
Check Need in Dictionary
      ↓
Found?
      ↓
Return Indices
```

Complexity:

```text
Time:  O(n)
Space: O(n)
```

Average-case hash lookup is treated as `O(1)`.

# 🧠 DSA Pattern 4: Grouping

Example:

```python
words = [
    "eat",
    "tea",
    "tan",
    "ate",
    "nat",
    "bat"
]
```

Group anagrams:

```python
from collections import defaultdict

groups = defaultdict(list)

for word in words:
    key = "".join(sorted(word))

    groups[key].append(word)

result = list(groups.values())
```

The sorted word becomes the hash-map key.

Conceptually:

```text
eat → aet
tea → aet
ate → aet
```

All belong to the same group.

If each word has length `m`, sorting each word costs roughly:

```text
O(m log m)
```

For `n` words:

```text
O(n × m log m)
```

# 🧠 DSA Pattern 5: Prefix Sum + Hash Map

A very important advanced pattern.

Problem:

Count subarrays whose sum equals `k`.

```python
def subarray_sum(nums, k):
    prefix_count = {
        0: 1
    }

    prefix_sum = 0
    answer = 0

    for num in nums:
        prefix_sum += num

        needed = prefix_sum - k

        answer += prefix_count.get(
            needed,
            0
        )

        prefix_count[prefix_sum] = (
            prefix_count.get(prefix_sum, 0)
            + 1
        )

    return answer
```

Core idea:

If:

```text
Current Prefix Sum = P
```

and we want a subarray sum of:

```text
k
```

then we need an earlier prefix sum:

```text
P - k
```

Because:

```text
P - PreviousPrefix = k
```

Therefore:

```text
PreviousPrefix = P - k
```

The dictionary stores:

```text
Prefix Sum → Frequency
```

Why initialize:

```python
prefix_count = {
    0: 1
}
```

Because a prefix starting from index `0` may itself have sum `k`.

Complexity:

```text
Time:  O(n)
Space: O(n)
```

This pattern is extremely important.

# 🧠 DSA Pattern 6: Sliding Window Frequency Map

Example pattern:

```python
frequency = {}

left = 0

for right in range(len(arr)):
    value = arr[right]

    frequency[value] = (
        frequency.get(value, 0)
        + 1
    )

    while window_is_invalid:
        left_value = arr[left]

        frequency[left_value] -= 1

        if frequency[left_value] == 0:
            del frequency[left_value]

        left += 1
```

Why delete zero-frequency keys?

Because sometimes:

```python
len(frequency)
```

is used to represent the number of distinct elements.

If zero-count keys remain, the dictionary size becomes misleading.

This pattern appears in:

* Longest Substring Without Repeating Characters
* Minimum Window Substring
* Find All Anagrams in a String
* Subarrays with K Distinct Integers

# 🧠 DSA Pattern 7: Memoization

A dictionary can cache previously computed results.

Example:

```python
memo = {}

def fibonacci(n):
    if n <= 1:
        return n

    if n in memo:
        return memo[n]

    memo[n] = (
        fibonacci(n - 1)
        + fibonacci(n - 2)
    )

    return memo[n]
```

The dictionary stores:

```text
Input → Computed Result
```

Without memoization, naive recursive Fibonacci takes exponential time.

With memoization:

```text
Time:  O(n)
Space: O(n)
```

# Memoization with Multiple State Variables

Suppose a recursive state depends on:

```text
index
remaining_target
```

Use a tuple as the key:

```python
state = (
    index,
    remaining_target
)

if state in memo:
    return memo[state]
```

This is one of the most important uses of tuple dictionary keys in dynamic programming.

# 🧠 DSA Pattern 8: Graph Adjacency List

Dictionaries can represent graphs.

```python
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["B"]
}
```

Using `defaultdict(list)`:

```python
from collections import defaultdict

graph = defaultdict(list)

edges = [
    ("A", "B"),
    ("A", "C"),
    ("B", "D")
]

for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)
```

This builds an undirected graph.

Typical complexity:

```text
Space: O(V + E)
```

# 🧠 DSA Pattern 9: Character Mapping

Example:

```python
mapping = {}

for char in string:
    mapping[char] = mapping.get(char, 0) + 1
```

Used heavily in:

* Anagrams
* Isomorphic Strings
* Pattern Matching
* Sliding Window
* String frequency problems

# 🧠 DSA Pattern 10: Last Seen Index

Store the latest position of each element.

```python
last_seen = {}

for index, char in enumerate(text):
    last_seen[char] = index
```

Used in problems such as:

```text
Longest Substring Without Repeating Characters
```

A typical pattern:

```python
left = 0
last_seen = {}

for right, char in enumerate(text):
    if (
        char in last_seen
        and last_seen[char] >= left
    ):
        left = last_seen[char] + 1

    last_seen[char] = right
```

The dictionary allows direct access to the previous index.

# ⚡ Dictionary Performance Cheat Sheet

| Operation                   | Average Complexity |
| --------------------------- | -----------------: |
| Access by key               |             `O(1)` |
| Insert                      |             `O(1)` |
| Update                      |             `O(1)` |
| Delete                      |             `O(1)` |
| Key membership              |             `O(1)` |
| `get()`                     |             `O(1)` |
| `setdefault()`              |             `O(1)` |
| `pop()`                     |             `O(1)` |
| `popitem()`                 |             `O(1)` |
| `len()`                     |             `O(1)` |
| `keys()` view creation      |             `O(1)` |
| `values()` view creation    |             `O(1)` |
| `items()` view creation     |             `O(1)` |
| Iteration                   |             `O(n)` |
| Value membership            |             `O(n)` |
| `copy()`                    |             `O(n)` |
| `clear()`                   |             `O(n)` |
| `update()` with `k` entries |             `O(k)` |
| Dictionary comprehension    |             `O(n)` |
| Sorting                     |       `O(n log n)` |

Hash-table operations are average-case complexities.

# 🚨 Common Advanced Mistakes

## Mistake 1: Assuming `sorted(dictionary)` Returns a Dictionary

It returns:

```text
List of sorted keys
```

## Mistake 2: Forgetting Right-Side Precedence

```python
a | b
```

For duplicate keys:

```text
b wins
```

Likewise:

```python
{
    **a,
    **b
}
```

Later values win.

## Mistake 3: Reversing a Dictionary with Duplicate Values

```python
{
    value: key
    for key, value in data.items()
}
```

can lose information.

## Mistake 4: Accessing a Missing `defaultdict` Key Accidentally

```python
data[key]
```

can insert the missing key.

## Mistake 5: Forgetting to Delete Zero Counts

In sliding-window frequency maps:

```python
frequency[x] -= 1
```

may leave:

```text
x → 0
```

If `len(frequency)` represents distinct active values, remove zero-count keys.

## Mistake 6: Using Mutable Objects as Dictionary Keys

Lists, dictionaries, and normal sets cannot be dictionary keys.

## Mistake 7: Assuming Dictionary Equality Depends on Order

It does not.

## Mistake 8: Using Dictionary Lookup but Still Writing an `O(n)` Search

Bad:

```python
for key in data:
    if key == target:
        ...
```

Better:

```python
if target in data:
    ...
```

Average:

```text
O(1)
```

# 💼 Advanced Interview Questions

1. What is a dictionary comprehension?
2. What happens when a comprehension generates duplicate keys?
3. What is the difference between `|` and `|=`?
4. What happens when dictionaries with duplicate keys are merged?
5. What does `**` do with dictionaries?
6. What does `sorted(dictionary)` return?
7. How do you sort a dictionary by values?
8. What happens when reversing a dictionary containing duplicate values?
9. What is `defaultdict`?
10. How is `defaultdict` different from `get()`?
11. Does accessing a missing `defaultdict` key modify it?
12. What is `Counter`?
13. What does a missing key return in `Counter`?
14. What does `most_common()` do?
15. What is `OrderedDict`, and when is it still useful?
16. Does dictionary equality depend on insertion order?
17. What is the difference between `==` and `is`?
18. Why can `True`, `1`, and `1.0` behave as the same dictionary key?
19. How is a dictionary used in Two Sum?
20. How does a frequency map reduce complexity?
21. How are dictionaries used with prefix sums?
22. Why is `{0: 1}` important in the Subarray Sum Equals K pattern?
23. Why should zero-frequency keys sometimes be deleted?
24. How can tuples represent memoization states?
25. How can dictionaries represent graphs?

# 📌 Advanced Quick Revision

✔ Dictionary comprehensions create dictionaries concisely.

✔ Duplicate generated keys overwrite earlier values.

✔ `a | b` creates a new merged dictionary.

✔ `a |= b` updates the left dictionary.

✔ In merges, later/right-side values win for duplicate keys.

✔ `**` unpacks dictionary entries.

✔ `sorted(dictionary)` returns sorted keys as a list.

✔ Use `items()` to sort by dictionary values.

✔ Reverse mapping can lose data when values are duplicated.

✔ `defaultdict` automatically creates defaults on missing-key square-bracket access.

✔ `defaultdict(int)` is useful for counting.

✔ `defaultdict(list)` is useful for grouping.

✔ `Counter` is specialized for frequency counting.

✔ Missing Counter counts return `0`.

✔ `most_common()` helps find frequent elements.

✔ Normal dictionaries preserve insertion order.

✔ Dictionary equality does not depend on insertion order.

✔ `==` checks equality while `is` checks identity.

✔ Frequency maps are among the most important DSA dictionary patterns.

✔ Index maps convert repeated searches into average `O(1)` lookups.

✔ Two Sum is a classic hash-map problem.

✔ Prefix Sum + Hash Map is an important `O(n)` pattern.

✔ Sliding windows frequently maintain dictionary frequency counts.

✔ Memoization uses dictionaries to cache computed states.

✔ Tuple keys are useful for multi-variable DP states.

✔ Dictionaries and `defaultdict(list)` are useful for graph adjacency lists.
