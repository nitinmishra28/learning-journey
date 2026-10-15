# Top K Frequent Elements

## 1. Problem

Given an integer array `nums` and an integer `k`, return the `k` elements that appear most frequently.

### Example

```python
nums = [1, 1, 1, 2, 2, 3]
k = 2

Output: [1, 2]
```

**Explanation:**

- `1` appears 3 times.
- `2` appears 2 times.
- `3` appears 1 time.

The two most frequent elements are `1` and `2`.

---

## 2. Brute Force Approach

### Idea

1. Count the frequency of every number using a dictionary.
2. Sort the numbers by their frequencies in descending order.
3. Return the first `k` elements.

### Code

```python
from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = Counter(nums)

        sorted_items = sorted(
            freq.items(),
            key=lambda item: item[1],
            reverse=True
        )

        return [val for val, count in sorted_items[:k]]
```

### Complexity

Let:
- `n` = number of elements in `nums`
- `m` = number of distinct elements

- Frequency counting: `O(n)`
- Sorting distinct elements: `O(m log m)`
- **Total time:** `O(n + m log m)`
- **Space:** `O(m)`, excluding output and sorting implementation details

### Why Is It Less Efficient?

We sort every distinct element, even though we only need the `k` most frequent elements.

**Optimization:** Maintain a Min Heap containing only the `k` most frequent elements.

---

## 3. Pattern: Frequency Counter + Min Heap of Size K

The key idea is to combine two data structures:

1. **Hash Map:** Counts how many times each number appears.
2. **Min Heap:** Keeps only the `k` most frequent numbers.

```text
Input Array
    |
    v
Count Frequencies
    |
    v
Hash Map: {number: frequency}
    |
    v
Push (frequency, number) into Min Heap
    |
    v
If heap size > k, remove the root
    |
    v
Return the k remaining elements
```

### Why a Min Heap?

A Min Heap gives us the smallest frequency at its root.

Since we want the `k` largest frequencies, whenever the heap contains more than `k` elements, we remove the element with the smallest frequency.

This ensures that the heap retains only the `k` most frequent elements.

---

## 4. Main Idea

### Step 1: Count the frequency

```python
hash_map = {}

for val in nums:
    hash_map[val] = hash_map.get(val, 0) + 1
```

For this input:

```python
nums = [1, 1, 1, 2, 2, 3]
```

The resulting dictionary is:

```python
{
    1: 3,
    2: 2,
    3: 1
}
```

Each key represents a number, and its value represents its frequency.

### Step 2: Create a Min Heap

```python
min_heap = []
```

We store each element as a tuple:

```python
(count, val)
```

For example:

```python
(3, 1)
```

means the number `1` appears `3` times.

**Why store frequency first?**

Python compares tuples from left to right. The frequency is compared first, so the Min Heap prioritizes the smallest frequency.

If frequencies are equal, Python compares the numbers as a tie-breaker.

### Step 3: Push each frequency into the heap

```python
for val, count in hash_map.items():
    heapq.heappush(min_heap, (count, val))
```

Initially, all distinct numbers are inserted into the heap.

But we don't want the heap to grow beyond `k`.

### Step 4: Remove the smallest frequency when needed

```python
if len(min_heap) > k:
    heapq.heappop(min_heap)
```

If the heap contains more than `k` elements, remove the root.

The root has the smallest frequency among the elements currently in the heap.

This maintains the heap size at no more than `k`.

### Step 5: Extract the answer

```python
return [val for count, val in min_heap]
```

Each heap entry has the structure `(count, val)`. We extract only `val` because the question asks for the elements, not their frequencies.

**Note:** The returned list is not necessarily sorted by frequency.

---

## 5. Complete Code with Comments

```python
import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        # Step 1: Count the frequency of each number
        hash_map = {}

        for val in nums:
            hash_map[val] = hash_map.get(val, 0) + 1

        # Step 2: Create a Min Heap
        min_heap = []

        # Step 3: Process each distinct number and its frequency
        for val, count in hash_map.items():

            # Store (frequency, number)
            heapq.heappush(min_heap, (count, val))

            # Step 4: Keep only the k most frequent elements
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # Step 5: Extract the numbers from the remaining heap entries
        return [val for count, val in min_heap]
```

---

## 6. Dry Run

Consider:

```python
nums = [1, 1, 1, 2, 2, 3]
k = 2
```

### Step 1: Build the frequency map

```python
hash_map = {
    1: 3,
    2: 2,
    3: 1
}
```

There are three distinct numbers.

### Step 2: Process `(count, val)` pairs

The following table shows the heap's logical contents after each insertion. The heap array itself is not fully sorted.

| Processed pair | Action | Heap size |
|---|---|---:|
| `(3, 1)` | Insert | 1 |
| `(2, 2)` | Insert | 2 |
| `(1, 3)` | Insert, then remove the smallest | 2 |

After inserting `(1, 3)`, the heap temporarily contains three elements:

```text
(1, 3)  <- smallest frequency
(2, 2)
(3, 1)
```

Since `k = 2`, we remove `(1, 3)`.

The remaining elements are:

```text
(2, 2)
(3, 1)
```

### Step 3: Extract the numbers

```python
return [val for count, val in min_heap]
```

Possible output:

```python
[2, 1]
```

The order can vary because the heap is not sorted.

The correct set of top-frequency elements is `{1, 2}`.

---

## 7. Why Does Keeping Only K Elements Work?

Suppose we need the top `2` elements.

```text
Frequencies:

Number 1 -> 3
Number 2 -> 2
Number 3 -> 1
```

We want to retain the two largest frequencies: `3` and `2`.

When the heap contains three entries, the smallest frequency is `1`, so it gets removed.

```text
Before removal:
(1, 3), (2, 2), (3, 1)
 ^ remove this entry

After removal:
(2, 2), (3, 1)
```

Here, each tuple is `(frequency, number)`.

After processing all distinct numbers, the heap contains the `k` elements with the highest frequencies, subject to the tie-handling behavior described below.

### Important Note About Ties

If multiple numbers have the same frequency at the cutoff, your code uses the number itself as the tuple's second value. Python therefore uses the number to break ties.

For problems that allow **any** valid answer when frequencies tie, this is generally fine. If a problem specifies a particular tie-breaking rule, you must implement that rule explicitly.

---

## 8. Complexity Analysis

Let:
- `n` = total number of elements
- `m` = number of distinct elements
- `k` = number of elements to return

| Operation | Time Complexity |
|---|---|
| Build frequency map | `O(n)` |
| Process `m` distinct elements | `O(m log k)` |
| Extract result | `O(k)` |
| **Total** | **`O(n + m log k + k)`** |

Since `k <= m`, the total is commonly written as:

**Time Complexity:** `O(n + m log k)`

**Space Complexity:** `O(m + k)`, which simplifies to `O(m)` because the frequency map stores up to `m` distinct numbers and the heap stores at most `k` entries.

This is more efficient than sorting all distinct elements when `k` is much smaller than `m`.

---

## 9. Common Mistakes

1. **Putting the number before its frequency:** Use `(count, val)` so the heap prioritizes frequency.
2. **Forgetting to limit the heap size:** Without the size check, the heap stores every distinct element.
3. **Using a Max Heap unnecessarily:** A Min Heap of size `k` is sufficient because we want to discard the smallest frequencies.
4. **Returning the entire tuple:** The answer should contain numbers, not `(frequency, number)` pairs.
5. **Assuming the output is sorted:** A heap does not produce a fully sorted array.
6. **Confusing `n` and `m`:** Frequency counting processes `n` input elements, while the heap processes `m` distinct elements.

---

## 10. Brute Force vs Optimized Approach

| Feature | Brute Force | Min Heap |
|---|---|---|
| Frequency counting | `O(n)` | `O(n)` |
| Selection step | `O(m log m)` sorting | `O(m log k)` heap operations |
| Best when | Sorting all distinct elements is acceptable | `k` is much smaller than `m` |
| Extra space | `O(m)` | `O(m)` |
| Maintains only k candidates | No | Yes |

---

## 11. Pattern Recognition

Use **Frequency Counter + Min Heap of Size K** when a problem asks for:

- The `k` most frequent elements
- The `k` largest or smallest candidates
- Top `k` items without fully sorting all candidates

The general pattern is:

1. Count or calculate a score for each candidate.
2. Store `(score, candidate)` in a Min Heap.
3. Remove the root whenever the heap size exceeds `k`.
4. Extract the remaining candidates.

---

## 12. Revision Cheat Sheet

- **Hash Map:** Count the frequency of every number.
- **Heap Entry:** `(count, val)`.
- **Why Min Heap?** The smallest frequency stays at the root.
- **Why size K?** We only need the top `k` elements.
- **When size exceeds K:** Remove the smallest frequency.
- **Time:** `O(n + m log k)`, where `m` is the number of distinct elements.
- **Space:** `O(m)`.
- **Output order:** Not guaranteed to be sorted by frequency.

> **One-Line Pattern:** Top K Frequent Elements = Frequency Hash Map + Min Heap of Size K + Remove the Smallest Frequency When the Heap Exceeds K.