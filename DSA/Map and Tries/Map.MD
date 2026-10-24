# Hash Map in Python

My personal notes for learning **Hash Maps from basic to advanced**, including hashing, collisions, collision resolution techniques, load factor, Python dictionaries, time complexity, and DSA interview patterns.

## 1. What Is a Hash Map?

A **Hash Map** is a data structure that stores data in **key-value pairs** and uses a hash function to determine where a key should be stored.

In Python, the built-in `dict` implements a hash table.

### Example

```python
student = {
    "name": "Rahul",
    "age": 22,
    "city": "Bangalore"
}

print(student["name"])  # Rahul
print(student["age"])   # 22
```

Here:
- `"name"`, `"age"`, and `"city"` are keys.
- `"Rahul"`, `22`, and `"Bangalore"` are values.

### Why Use a Hash Map?

Without a hash map, searching for an element in an unsorted list takes `O(n)` time.

With a hash map, lookup takes **`O(1)` average time**.

Hash maps are useful for:
- Frequency counting
- Duplicate detection
- Fast lookups
- Grouping elements
- Prefix sum problems
- Caching
- Two Sum and other DSA problems

---

## 2. How Does a Hash Map Work Internally?

A hash map uses a **hash function** to convert a key into a hash value, which helps determine where the key should be stored.

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
       Find Table Position
              |
              v
        Store / Retrieve
           Key-Value
```

For example, imagine a hash table with 10 slots.

A simplified hash function could be:

\[
\text{index} = \text{hash(key)} \bmod 10
\]

Suppose the hash function returns `123`.

```text
index = 123 % 10
index = 3
```

The key is assigned to slot `3`.

**Important:** This is a simplified illustration. Python's actual dictionary implementation uses its own hashing and table-indexing strategy.

---

## 3. What Is a Hash Function?

A **hash function** converts a key into an integer hash value.

For example, Python provides the built-in `hash()` function.

```python
print(hash("apple"))
print(hash(100))
print(hash((1, 2)))
```

The exact hash values are implementation-dependent. In particular, hashes of strings can differ between Python processes.

A good hash function should distribute keys across the table to reduce collisions.

### Hashable Objects in Python

Dictionary keys must be hashable.

Common examples:

```python
my_map = {
    "name": "Rahul",
    100: "Hundred",
    (1, 2): "Tuple"
}
```

Lists and dictionaries cannot be used as keys because they are mutable and unhashable.

```python
# Invalid
# my_map[[1, 2]] = "value"
```

A tuple is usable as a key only when all its elements are hashable.

---

## 4. What Is a Collision?

A **collision** occurs when two different keys map to the same hash table slot.

For example, suppose we use this simplified hash function:

\[
\text{index} = \text{key} \bmod 10
\]

Consider these keys:

```text
Key 12  -> 12 % 10 = 2
Key 22  -> 22 % 10 = 2
Key 32  -> 32 % 10 = 2
```

All three keys map to index `2`.

This is a collision.

```text
Hash Table

Index 0: Empty
Index 1: Empty
Index 2: 12, 22, 32  <- Collision
Index 3: Empty
Index 4: Empty
...
```

A hash map must handle collisions correctly so that different keys can coexist and still be retrieved.

Two classic collision-resolution techniques are:

1. **Open Addressing**
2. **Separate Chaining** (sometimes discussed as closed addressing)

---

## 5. Collision Resolution Technique 1: Open Addressing

In **open addressing**, all entries are stored directly inside the hash table's array.

When a collision occurs, the hash map searches for another available slot using a probing strategy.

There are three important probing techniques:

1. Linear Probing
2. Quadratic Probing
3. Double Hashing

### 5.1 Linear Probing

If the calculated index is occupied, check the next slot.

A simplified formula is:

\[
\text{index}_i = (h(key) + i) \bmod m
\]

Where:
- \(h(key)\) is the initial hash index.
- \(i\) is the probe number: `0, 1, 2, ...`.
- \(m\) is the table size.

#### Example

Suppose the table size is `10` and the hash function is:

```python
index = key % 10
```

Insert keys `12`, `22`, and `32`.

All initially map to index `2`.

```text
Insert 12:
Index 2 is empty -> Store 12

Insert 22:
Index 2 occupied -> Check index 3 -> Store 22

Insert 32:
Index 2 occupied -> Check index 3 -> Check index 4 -> Store 32
```

Result:

```text
Index 0: Empty
Index 1: Empty
Index 2: 12
Index 3: 22
Index 4: 32
Index 5: Empty
...
```

#### Disadvantage: Primary Clustering

Linear probing can create long groups of consecutive occupied slots.

These groups are called **primary clusters**.

As clusters grow, insertions and searches may require more probes.

### 5.2 Quadratic Probing

Quadratic probing uses increasingly larger jumps instead of checking every consecutive slot.

A common formula is:

\[
\text{index}_i = (h(key) + c_1i + c_2i^2) \bmod m
\]

Where:
- \(h(key)\) is the initial hash index.
- \(c_1\) and \(c_2\) are constants.
- \(i\) is the probe number.
- \(m\) is the table size.

For example, with \(c_1 = 0\) and \(c_2 = 1\), the offsets are:

```text
i = 0 -> 0² = 0
i = 1 -> 1² = 1
i = 2 -> 2² = 4
i = 3 -> 3² = 9
```

If the original index is `2`, the candidate slots are:

```text
2, 3, 6, 1, ...
```

This reduces primary clustering compared with linear probing.

However, quadratic probing can still have secondary clustering, and the table size and probing parameters affect whether every slot can be reached.

### 5.3 Double Hashing

Double hashing uses a second hash function to determine the step size.

A common formula is:

\[
\text{index}_i =
(h_1(key) + i \cdot h_2(key)) \bmod m
\]

Here:
- \(h_1(key)\) calculates the initial index.
- \(h_2(key)\) calculates the step size.
- \(m\) is the table size.

Example:

```text
Initial index = 2
Step size = 3
Table size = 10
```

Candidate positions:

```text
i = 0 -> (2 + 0 * 3) % 10 = 2
i = 1 -> (2 + 1 * 3) % 10 = 5
i = 2 -> (2 + 2 * 3) % 10 = 8
i = 3 -> (2 + 3 * 3) % 10 = 1
```

Double hashing often reduces clustering more effectively than linear or quadratic probing when the hash functions and table size are chosen appropriately.

For reliable coverage, the step size must be relatively prime to the table size.

### Open Addressing Summary

| Technique | Collision Handling | Main Concern |
|---|---|---|
| Linear Probing | Check consecutive slots | Primary clustering |
| Quadratic Probing | Use quadratic offsets | Secondary clustering and probe coverage |
| Double Hashing | Use a second hash function for step size | Requires suitable hash functions and table size |

**Important:** These are classic hash table techniques. They explain how hash tables can be implemented, but they are not descriptions of Python's exact dictionary collision-resolution algorithm.

---

## 6. Collision Resolution Technique 2: Separate Chaining

**Separate chaining** stores multiple entries associated with the same table index in a separate collection, commonly a linked list.

Instead of searching for another empty array slot, entries that collide share a bucket.

### Example

Suppose keys `12`, `22`, and `32` all map to index `2`.

```text
Hash Table

Index 0 -> None
Index 1 -> None
Index 2 -> 12 -> 22 -> 32
Index 3 -> None
Index 4 -> None
```

The bucket at index `2` contains all three entries.

When searching for key `22`, the hash map:
1. Calculates its bucket index.
2. Accesses the bucket.
3. Searches the entries in that bucket for the requested key.

### Advantages

- Multiple keys can share a bucket.
- Deletion can be straightforward when the bucket structure supports it.
- It does not require finding another empty table slot for every collision.

### Disadvantages

- Extra memory may be needed for the bucket structures.
- Long chains can make lookups slower.
- Performance depends on how evenly keys are distributed.

### Open Addressing vs Separate Chaining

| Feature | Open Addressing | Separate Chaining |
|---|---|---|
| Where entries are stored | Inside the table array | In bucket collections |
| Collision handling | Probe for another slot | Add to the same bucket |
| Extra bucket structures | No | Usually yes |
| Main concern | Clustering and probe sequences | Long buckets or chains |

**Terminology note:** Separate chaining is also called *closed addressing* in some materials. Terminology can vary, so remember the mechanism: open addressing probes other slots; chaining stores colliding entries together in a bucket.

---

## 7. What Is the Load Factor?

The **load factor** measures how full a hash table is.

It is calculated as:

\[
\alpha = \frac{n}{m}
\]

Where:
- \(n\) = number of stored entries.
- \(m\) = number of available table slots.

### Example

Suppose:

```text
Number of entries = 6
Table capacity = 10
```

Then:

\[
\alpha = \frac{6}{10} = 0.6
\]

The load factor is `0.6`, or `60%`.

### Why Does Load Factor Matter?

As the load factor increases, collisions or probe lengths can become more frequent, depending on the hash table design.

A high load factor can therefore reduce performance.

For open addressing, performance often degrades significantly as the table becomes nearly full because finding an empty slot becomes harder.

For separate chaining, higher load factors generally mean more entries per bucket on average.

---

## 8. Why Keep the Load Factor Below 0.7?

A common teaching guideline for some hash table implementations is to resize when the load factor reaches approximately `0.7`.

For example:

```text
Table capacity = 10
Stored entries = 6

Load factor = 6 / 10 = 0.6
```

The table is below `0.7`.

If another entry is added:

```text
Stored entries = 7
Load factor = 7 / 10 = 0.7
```

At this threshold, an implementation might resize the table.

**Important:** `0.7` is a useful illustrative threshold, not a universal rule. The appropriate threshold depends on the collision-resolution strategy and implementation. Python's built-in `dict` does not expose a configurable load-factor setting, and you should not assume that its internal resize threshold is exactly `0.7`.

### What Happens During Resizing?

A simplified resizing process is:

1. Allocate a larger table.
2. Recalculate the positions of existing keys using the new capacity.
3. Insert the entries into the new table.
4. Continue normal operations.

This process is often called **rehashing**, although implementations can differ in how they rebuild or redistribute entries.

### Why Does Resizing Help?

Suppose a table has:

```text
Capacity = 10
Entries = 8
Load factor = 0.8
```

If the table grows to capacity `20`:

```text
Capacity = 20
Entries = 8
Load factor = 0.4
```

The lower load factor can reduce collisions or probing, improving expected performance.

Resizing is expensive when it happens, but if the table grows geometrically, insertion can still have amortized `O(1)` complexity under typical assumptions.

---

## 9. Hash Map Time Complexity

Let `n` be the number of entries.

| Operation | Average Time | Worst Case |
|---|---:|---:|
| Insert | `O(1)` | `O(n)` |
| Lookup | `O(1)` | `O(n)` |
| Update | `O(1)` | `O(n)` |
| Delete | `O(1)` | `O(n)` |
| Iterate over entries | `O(n)` | `O(n)` |

Average constant-time performance depends on hashing behavior, table resizing, and collision handling.

Worst-case linear time can occur when many keys must be examined.

---

## 10. Python Dictionary Operations

### Create a Dictionary

```python
student = {
    "name": "Rahul",
    "age": 22
}
```

### Insert or Update

```python
student["city"] = "Bangalore"
student["age"] = 23
```

### Lookup

```python
print(student["name"])
print(student.get("city", "Unknown"))
```

### Check Whether a Key Exists

```python
if "age" in student:
    print("Age exists")
```

### Delete

```python
del student["age"]
```

### Iterate

```python
for key, value in student.items():
    print(key, value)
```

---

## 11. Frequency Counting Using a Hash Map

Frequency counting is one of the most common hash map patterns in DSA.

### Example

```python
nums = [1, 2, 2, 3, 1, 2]

freq = {}

for num in nums:
    freq[num] = freq.get(num, 0) + 1

print(freq)
```

Output:

```python
{1: 2, 2: 3, 3: 1}
```

### Using `Counter`

```python
from collections import Counter

nums = [1, 2, 2, 3, 1, 2]

freq = Counter(nums)

print(freq[2])  # 3
```

**Time Complexity:** `O(n)` average.

**Space Complexity:** `O(n)`.

---

## 12. Important Hash Map Patterns

### Pattern 1: Complement Lookup

Example: Two Sum.

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

### Pattern 2: Grouping

Example: Group Anagrams.

```python
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))
            groups[key].append(word)

        return list(groups.values())
```

**Time Complexity:** `O(n * m log m)`, where `m` is the maximum word length.

### Pattern 3: Prefix Sum + Hash Map

Useful for counting subarrays whose sum equals a target.

```python
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        prefix_count = {0: 1}
        prefix_sum = 0
        count = 0

        for num in nums:
            prefix_sum += num

            count += prefix_count.get(prefix_sum - k, 0)

            prefix_count[prefix_sum] = (
                prefix_count.get(prefix_sum, 0) + 1
            )

        return count
```

**Time Complexity:** `O(n)` average.

**Space Complexity:** `O(n)`.

---

## 13. Hash Map vs Ordered Map vs Unordered Map

Python provides a built-in `dict`, not separate standard container types named `map`, `unordered_map`, and `ordered_map` like C++.

| Concept | Python Equivalent | Notes |
|---|---|---|
| Hash map | `dict` | Average `O(1)` lookup |
| Insertion-ordered map | `dict` | Preserves insertion order |
| Frequency map | `Counter` | Built on dictionary behavior |
| Default-valued map | `defaultdict` | Automatically supplies missing values |
| Sorted map | No built-in equivalent | Use a third-party sorted-map implementation or maintain sorted keys separately |

Python dictionaries preserve insertion order as a language guarantee since Python 3.7.

However, insertion order is not the same as sorting by key.

---

## 14. Important Interview Problems

### Easy

- Two Sum
- Contains Duplicate
- Valid Anagram
- Ransom Note
- First Unique Character in a String

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

---

## 15. Common Mistakes

1. Assuming hash map operations are always `O(1)` in every situation.
2. Confusing a hash value with the final table index.
3. Forgetting that different keys can collide.
4. Assuming `0.7` is the exact resize threshold for every hash table.
5. Using mutable objects such as lists as dictionary keys.
6. Confusing insertion order with sorted order.
7. Assuming Python's `dict` uses the same collision-resolution implementation as every textbook hash table.

---

## 16. Revision Cheat Sheet

| Concept | Key Point |
|---|---|
| Hash Map | Stores key-value pairs |
| Hash Function | Maps a key to a hash value |
| Collision | Different keys map to the same table position |
| Open Addressing | Find another slot using probing |
| Linear Probing | Check consecutive slots |
| Quadratic Probing | Use quadratic offsets |
| Double Hashing | Use a second hash function for the step size |
| Separate Chaining | Store colliding entries in the same bucket |
| Load Factor | `entries / table capacity` |
| Threshold `0.7` | Common illustrative resizing guideline, not universal |
| Average Lookup | `O(1)` |
| Worst-Case Lookup | `O(n)` |
| Python Hash Map | `dict` |

> **One-Line Pattern:** Hash Map = Hash Function + Key-Value Storage + Collision Resolution + Load-Factor Management for Efficient Average-Time Lookups.