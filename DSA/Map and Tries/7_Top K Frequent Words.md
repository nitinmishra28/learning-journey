# Top K Frequent Words — Hash Map + Sorting

## 1. Problem Statement

Given a list of strings `words` and an integer `k`, return the `k` most frequent words.

The result must be sorted by:

1. **Frequency:** Higher frequency comes first.
2. **Lexicographical order:** If two words have the same frequency, the alphabetically smaller word comes first.

This problem is commonly known as **Top K Frequent Words (LeetCode 692)**.

### Example 1

**Input:**

```python
words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
```

**Output:**

```python
["i", "love"]
```

**Explanation:**

- `"i"` appears twice.
- `"love"` appears twice.
- `"coding"` appears once.
- `"leetcode"` appears once.

Both `"i"` and `"love"` have the highest frequency. Since their frequencies are equal, alphabetical order determines their order.

### Example 2

**Input:**

```python
words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4
```

**Output:**

```python
["the", "is", "sunny", "day"]
```

**Explanation:**

| Word | Frequency |
|---|---:|
| `"the"` | 4 |
| `"is"` | 3 |
| `"sunny"` | 2 |
| `"day"` | 1 |

The words are ordered by decreasing frequency.

---

## 2. Approach: Hash Map + Sorting

We use two important concepts:

- **Hash Map (`Counter`):** Count how many times each word appears.
- **Sorting:** Sort words by frequency in descending order and alphabetically when frequencies are equal.

### Overall Strategy

1. Count the frequency of every word.
2. Sort the word-frequency pairs using a custom sorting key.
3. Traverse the sorted pairs.
4. Add words to the answer until we have `k` words.
5. Return the answer.

---

## 3. Complete Python Code

Your original solution uses `Counter` and sorting.

```python
from collections import Counter

class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        new_words = Counter(words)
        ans = []

        for char, val in sorted(
            new_words.items(),
            key=lambda x: (-x[1], x[0])
        ):
            if len(ans) < k:
                ans.append(char)
            else:
                continue

        return ans
```

### A Slightly Cleaner Version

Once we have collected `k` words, we can stop iterating.

```python
from collections import Counter

class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        new_words = Counter(words)

        sorted_words = sorted(
            new_words.items(),
            key=lambda x: (-x[1], x[0])
        )

        ans = []

        for word, frequency in sorted_words:
            ans.append(word)

            if len(ans) == k:
                break

        return ans
```

Both versions produce the same result for valid inputs.

---

## 4. Understanding `Counter`

```python
new_words = Counter(words)
```

`Counter` is available in Python's `collections` module.

It counts how many times each element appears in an iterable.

Example:

```python
from collections import Counter

words = ["i", "love", "i", "coding", "love", "i"]

new_words = Counter(words)

print(new_words)
```

Output:

```python
Counter({
    "i": 3,
    "love": 2,
    "coding": 1
})
```

We can access individual frequencies:

```python
print(new_words["i"])       # 3
print(new_words["love"])    # 2
print(new_words["coding"])  # 1
```

**Key idea:** `Counter` saves us from manually maintaining a frequency dictionary.

---

## 5. Understanding `new_words.items()`

```python
new_words.items()
```

The `items()` method returns the word-frequency pairs.

For example:

```python
Counter({
    "i": 3,
    "love": 2,
    "coding": 1
})
```

The items are conceptually:

```python
[
    ("i", 3),
    ("love", 2),
    ("coding", 1)
]
```

Each pair contains:

```python
(word, frequency)
```

In your loop:

```python
for char, val in sorted_words:
```

- `char` represents the word.
- `val` represents its frequency.

More descriptive variable names would be:

```python
for word, frequency in sorted_words:
```

---

## 6. Understanding the Sorting Key

This is the most important line in the solution.

```python
sorted(
    new_words.items(),
    key=lambda x: (-x[1], x[0])
)
```

Let's break it down.

### What Is `lambda x`?

A lambda is a small anonymous function.

```python
lambda x: (-x[1], x[0])
```

Here, `x` represents a tuple:

```python
(word, frequency)
```

Therefore:

- `x[0]` is the word.
- `x[1]` is the frequency.

For example:

```python
x = ("love", 2)
```

Then:

```python
x[0]  # "love"
x[1]  # 2
```

### Why Use `-x[1]`?

We want the highest frequency first.

By default, Python sorts numbers in ascending order.

For example:

```python
[1, 3, 2]
```

becomes:

```python
[1, 2, 3]
```

Negating the frequencies reverses their numerical order when sorting in ascending order.

Example:

| Word | Frequency | Negative frequency |
|---|---:|---:|
| `"i"` | 3 | -3 |
| `"love"` | 2 | -2 |
| `"coding"` | 1 | -1 |

Sorting `-3`, `-2`, and `-1` in ascending order gives the highest original frequency first.

### Why Use `x[0]`?

```python
(-x[1], x[0])
```

Python sorts tuples by their first element. If the first elements are equal, it compares the second elements.

Therefore:

1. `-x[1]` sorts by decreasing frequency.
2. `x[0]` sorts alphabetically when frequencies are equal.

### Example

```python
words = [
    ("love", 2),
    ("i", 2),
    ("coding", 1)
]
```

Sorting produces:

```python
[
    ("i", 2),
    ("love", 2),
    ("coding", 1)
]
```

The two most frequent words have equal frequencies, so `"i"` comes before `"love"` alphabetically.

**Interview takeaway:** `(-frequency, word)` means frequency descending, then word ascending.

---

## 7. Understanding the Loop

```python
ans = []

for char, val in sorted(new_words.items(), key=lambda x: (-x[1], x[0])):
    if len(ans) < k:
        ans.append(char)
    else:
        continue

return ans
```

### Step 1: Initialize the Answer

```python
ans = []
```

This list stores the top `k` words.

### Step 2: Iterate Over Sorted Pairs

```python
for char, val in sorted(...):
```

The words are already arranged according to the required ordering.

### Step 3: Add Words Until We Have `k`

```python
if len(ans) < k:
    ans.append(char)
```

If the answer currently contains fewer than `k` words, add the current word.

### Step 4: Return the Result

```python
return ans
```

Once the loop finishes, `ans` contains the first `k` words from the sorted list.

### Small Improvement

Your original code uses:

```python
else:
    continue
```

This skips the remaining iterations without doing any work. It is correct, but inefficient because the loop continues through every remaining word.

You can stop immediately:

```python
if len(ans) == k:
    break
```

Or use slicing:

```python
return sorted(
    new_words.items(),
    key=lambda x: (-x[1], x[0])
)[:k]
```

The slicing approach is concise, although sorting still processes all unique words.

---

## 8. Complete Dry Run

Consider:

```python
words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
```

### Step 1: Count Frequencies

```python
new_words = Counter(words)
```

Result:

```python
{
    "i": 2,
    "love": 2,
    "leetcode": 1,
    "coding": 1
}
```

### Step 2: Sort the Pairs

Sorting key:

```python
key=lambda x: (-x[1], x[0])
```

The sorted list is:

```python
[
    ("i", 2),
    ("love", 2),
    ("coding", 1),
    ("leetcode", 1)
]
```

Why does `"coding"` come before `"leetcode"`?

Both have frequency `1`, so alphabetical order determines their positions.

### Step 3: Initialize the Answer

```python
ans = []
```

### Step 4: Process the First Pair

```python
char = "i"
val = 2
```

Since:

```python
len(ans) < k
```

we append `"i"`.

```python
ans = ["i"]
```

### Step 5: Process the Second Pair

```python
char = "love"
val = 2
```

The answer still contains fewer than two words.

Append `"love"`.

```python
ans = ["i", "love"]
```

### Step 6: Finish

The answer now contains `k = 2` words.

The cleaner version stops here.

### Final Output

```python
["i", "love"]
```

---

## 9. Time and Space Complexity

Let:

- `N` = total number of words in the input.
- `U` = number of unique words.
- `L` = maximum word length.

### Step 1: Count Frequencies

```python
Counter(words)
```

Expected time:

\[
O(N)
\]

This assumes average-case constant-time hash map operations. Hashing strings also involves character processing, which can matter for very long words.

### Step 2: Sort the Unique Words

```python
sorted(new_words.items(), key=lambda x: (-x[1], x[0]))
```

Sorting `U` unique words takes:

\[
O(U \log U)
\]

String comparisons can take up to `O(L)` time in the worst case.

A more detailed upper bound is:

\[
O(U \log U \cdot L)
\]

### Step 3: Build the Answer

Collecting the first `k` words takes:

\[
O(k)
\]

excluding the cost of copying the returned strings.

### Overall Time Complexity

Using the simplified model where string comparisons are treated as constant-time:

\[
O(N + U \log U)
\]

### Space Complexity

- Frequency map: `O(U)`.
- Sorted list: `O(U)`.
- Answer: `O(k)` references.

Overall auxiliary space:

\[
O(U)
\]

excluding the input and the storage of the word strings themselves.

---

## 10. Common Mistakes

### Mistake 1: Sorting Frequencies in the Wrong Direction

Incorrect:

```python
key=lambda x: (x[1], x[0])
```

This sorts by increasing frequency.

Correct:

```python
key=lambda x: (-x[1], x[0])
```

### Mistake 2: Forgetting the Alphabetical Tie-Breaker

Incorrect:

```python
key=lambda x: -x[1]
```

This sorts only by frequency and does not explicitly apply the required alphabetical tie-breaker.

Correct:

```python
key=lambda x: (-x[1], x[0])
```

### Mistake 3: Sorting the Original Words Instead of Frequency Pairs

The problem requires ranking words by both frequency and alphabetical order.

Sorting `words` alone does not solve the frequency-ranking requirement.

### Mistake 4: Confusing the Word and Frequency

```python
for char, val in sorted_words:
```

Here, `char` is actually the word, not a single character.

Prefer:

```python
for word, frequency in sorted_words:
```

### Mistake 5: Continuing After Collecting `k` Words

Your original code is correct, but:

```python
else:
    continue
``` 

does unnecessary iterations.

Prefer:

```python
if len(ans) == k:
    break
```

---

## 11. Quick Revision Cheat Sheet

| Concept | Remember |
|---|---|
| `Counter(words)` | Counts word frequencies |
| `.items()` | Returns `(word, frequency)` pairs |
| `x[0]` | Word |
| `x[1]` | Frequency |
| `-x[1]` | Higher frequency first |
| `x[0]` | Alphabetical tie-breaker |
| Sorting key | `(-frequency, word)` |
| Time complexity | `O(N + U log U)` in the simplified model |
| Space complexity | `O(U)` |

## One-Line Pattern

**Top K Frequent Words pattern:** Count frequencies with a hash map, sort by `(-frequency, word)`, and return the first `k` words.