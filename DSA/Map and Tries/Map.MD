# Map (Hash Map / Dictionary) in Python

My notes for learning **Map / Hash Map in Python**, including fundamentals, implementation, complexity, common patterns, and interview problems.

## 1. What Is a Map?

A **Map** stores data in key-value pairs.

In Python, the built-in `dict` is used to implement a hash map.

Each key maps to a value, allowing us to retrieve, insert, and update data efficiently.

### Example

```python
student = {
    "name": "Rahul",
    "age": 22,
    "course": "Python"
}

print(student["name"])    # Rahul
print(student["age"])     # 22
```

Here:

- `"name"`, `"age"`, and `"course"` are keys.
- `"Rahul"`, `22`, and `"Python"` are values.

## 2. Why Do We Need a Map?

Suppose we want to find whether a number exists in a list.

### Without a Map

```python
nums = [10, 20, 30, 40, 50]

target = 40

for num in nums:
    if num == target:
        print("Found")
```

In the worst case, we examine every element.

**Time Complexity:** `O(n)`

### With a Map

```python
nums = [10, 20, 30, 40, 50]

num_map = {num: True for num in nums}

print(num_map.get(40, False))  # True
```

Dictionary lookups take `O(1)` average time.

**Important:** A dictionary is especially useful when we repeatedly need to look up information using a key.

## 3. Creating a Dictionary

```python
# Empty dictionary
my_map = {}

# Dictionary with initial values
student = {
    "name": "Rahul",
    "age": 22
}

# Using dict()
another_map = dict(name="Aman", age=24)

print(student)
print(another_map)
```

## 4. Basic Dictionary Operations

### Insert a Key-Value Pair

```python
student = {}

student["name"] = "Rahul"
student["age"] = 22

print(student)
```

### Access a Value

```python
student = {"name": "Rahul", "age": 22}

print(student["name"])
print(student.get("age"))
```

Difference:

```python
student["city"]       # Raises KeyError if missing
student.get("city")   # Returns None if missing
student.get("city", "Unknown")  # Returns "Unknown"
```

### Update a Value

```python
student = {"name": "Rahul", "age": 22}

student["age"] = 23

print(student)
```

### Delete a Key

```python
student = {"name": "Rahul", "age": 22}

del student["age"]

print(student)
```

### Check Whether a Key Exists

```python
student = {"name": "Rahul", "age": 22}

print("name" in student)  # True
print("city" in student)  # False
```

### Iterate Through a Dictionary

```python
student = {
    "name": "Rahul",
    "age": 22
}

for key, value in student.items():
    print(key, value)
```

## 5. Dictionary Frequency Counting

Frequency counting is one of the most important hash map patterns in DSA.

### Problem

Count how many times each number appears.

```python
nums = [1, 2, 2, 3, 1, 2]

freq = {}

for num in nums:
    freq[num] = freq.get(num, 0) + 1

print(freq)
```

Output:

```python
{
    1: 2,
    2: 3,
    3: 1
}
```

### Understanding This Line

```python
freq[num] = freq.get(num, 0) + 1
```

- If `num` exists, get its current frequency.
- Otherwise, use `0`.
- Add `1` and store the updated frequency.

For example, when `num = 2` appears for the first time:

```python
freq.get(2, 0) + 1
# 0 + 1 = 1
```

When it appears again:

```python
freq.get(2, 0) + 1
# 1 + 1 = 2
```

## 6. The `Counter` Class

Python provides `collections.Counter` for frequency counting.

```python
from collections import Counter

nums = [1, 2, 2, 3, 1, 2]

freq = Counter(nums)

print(freq)
print(freq[2])  # 3
```

`Counter` is convenient, but understanding manual frequency counting is important for interviews.

## 7. Common Hash Map Patterns

### Pattern 1: Frequency Counting

Use when a problem asks for:

- Frequency of elements.
- Duplicate detection.
- Most frequent element.
- Anagrams.

```python
from collections import Counter

nums = [1, 2, 2, 3, 1]

freq = Counter(nums)

print(freq[1])  # 2
```

### Pattern 2: Complement Lookup

Used in problems such as Two Sum.

Instead of checking every pair, store previously seen values in a dictionary.

```python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i

        return []
```

**Time Complexity:** `O(n)` average.

**Space Complexity:** `O(n)`.

### Pattern 3: Grouping Elements

Use a map when multiple values belong to the same category or key.

Example: Group anagrams.

```python
from collections import defaultdict

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

groups = defaultdict(list)

for word in words:
    key = "".join(sorted(word))
    groups[key].append(word)

print(list(groups.values()))
```

Output:

```python
[
    ["eat", "tea", "ate"],
    ["tan", "nat"],
    ["bat"]
]
```

**Time Complexity:** `O(n * m log m)`, where `m` is the maximum word length.

### Pattern 4: Prefix Sum + Hash Map

Useful for subarray sum problems.

Example: Count subarrays whose sum equals `k`.

```python
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        prefix_count = {0: 1}
        prefix_sum = 0
        count = 0

        for num in nums:
            prefix_sum += num

            needed = prefix_sum - k
            count += prefix_count.get(needed, 0)

            prefix_count[prefix_sum] = (
                prefix_count.get(prefix_sum, 0) + 1
            )

        return count
```

**Time Complexity:** `O(n)` average.

**Space Complexity:** `O(n)`.

## 8. Hash Map Time Complexity

Let `n` be the number of entries in a dictionary.

| Operation | Average | Worst Case |
|---|---:|---:|
| Insert | `O(1)` | `O(n)` |
| Lookup | `O(1)` | `O(n)` |
| Update | `O(1)` | `O(n)` |
| Delete | `O(1)` | `O(n)` |
| Iterate | `O(n)` | `O(n)` |

Python dictionaries use hash tables. Collisions and implementation details can affect worst-case performance.

## 9. Hashing and Collisions

A hash map uses a hash function to help locate where a key belongs.

Conceptually:

```text
Key
 |
 v
Hash Function
 |
 v
Hash Value
 |
 v
Find Stored Entry
```

A **collision** occurs when different keys map to the same hash location.

Hash table implementations handle collisions internally. Python's dictionary manages this for you.

### Hashable Keys

Dictionary keys must be hashable.

Common valid keys:

```python
my_map = {
    "name": "Rahul",
    10: "Ten",
    (1, 2): "Tuple"
}
```

A list cannot be used as a dictionary key:

```python
# Invalid: list is unhashable
# my_map[[1, 2]] = "value"
```

An immutable tuple containing hashable elements can be used as a key.

## 10. `defaultdict`

`defaultdict` automatically creates a default value for a missing key.

### Frequency Counting

```python
from collections import defaultdict

freq = defaultdict(int)

for num in [1, 2, 2, 3]:
    freq[num] += 1

print(dict(freq))
```

### Grouping

```python
from collections import defaultdict

groups = defaultdict(list)

groups["fruits"].append("apple")
groups["fruits"].append("banana")

print(dict(groups))
```

Common defaults:

- `defaultdict(int)` — missing values start at `0`.
- `defaultdict(list)` — missing values start as empty lists.
- `defaultdict(set)` — missing values start as empty sets.

## 11. When Should You Use a Hash Map?

Look for these clues:

- Find duplicates or frequencies.
- Quickly check whether a value exists.
- Map one value to another.
- Store previously seen elements.
- Group elements by a common property.
- Count subarrays using prefix sums.
- Avoid repeated linear searches.

## 12. Common Mistakes

1. Using `student[key]` without checking whether the key exists.
2. Forgetting to update frequencies correctly.
3. Using mutable objects such as lists as dictionary keys.
4. Assuming dictionary operations always take `O(1)` in every possible case.
5. Using a hash map when a sorted array or two-pointer solution is more suitable.
6. Forgetting that dictionary membership checks keys, not values.

```python
student = {"name": "Rahul"}

print("name" in student)   # True: checks keys
print("Rahul" in student)  # False: not a key
```

## 13. Important Interview Problems

### Easy

- Two Sum
- Contains Duplicate
- Valid Anagram
- Ransom Note
- First Unique Character in a String
- Majority Element

### Medium

- Group Anagrams
- Top K Frequent Elements
- Longest Consecutive Sequence
- Subarray Sum Equals K
- Longest Substring Without Repeating Characters
- 4Sum II

### Advanced

- Minimum Window Substring
- Count of Range Sum
- Substring with Concatenation of All Words
- Longest Duplicate Substring

## 14. Revision Cheat Sheet

| Concept | Python Tool |
|---|---|
| Key-value storage | `dict` |
| Frequency counting | `dict` / `Counter` |
| Automatic defaults | `defaultdict` |
| Key existence | `key in my_map` |
| Safe lookup | `my_map.get(key, default)` |
| Iterate over pairs | `my_map.items()` |
| Store unique values | `set` |
| Complement lookup | Dictionary lookup |
| Prefix sum counting | Prefix sum + dictionary |

> **One-Line Pattern:** Hash Map = Store Information by Key + Use Fast Average Lookups to Avoid Repeated Searching.