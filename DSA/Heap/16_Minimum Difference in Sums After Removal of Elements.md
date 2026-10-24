# Minimum Difference in Sums After Removal of Elements

## 1. Problem

You are given an integer array `nums` of length `3 * n`.

You must remove exactly `n` elements, leaving `2 * n` elements. Divide the remaining elements into two contiguous parts:

- The first `n` elements form the left part.
- The last `n` elements form the right part.

Find the **minimum possible difference** between:

- The sum of the first `n` elements.
- The sum of the last `n` elements.

In other words, minimize:

\[
\text{leftSum} - \text{rightSum}
\]

### Example

**Input:**

```python
nums = [3, 1, 2]
```

**Output:**

```python
-1
```

**Explanation:**

Here, `n = 1`. We remove one element and keep two elements.

If we remove `3`, the remaining elements are `[1, 2]`.

- Left sum = `1`
- Right sum = `2`
- Difference = `1 - 2 = -1`

Therefore, the minimum difference is `-1`.

---

## 2. Brute Force Approach

### Idea

Try every possible way to remove exactly `n` elements.

For each choice:

1. Keep the remaining `2 * n` elements.
2. Calculate the sum of the first `n` remaining elements.
3. Calculate the sum of the last `n` remaining elements.
4. Find their difference.
5. Return the minimum difference.

### Why is it inefficient?

There are many possible ways to select which `n` elements to remove. Checking all combinations becomes extremely expensive as the array grows.

A brute-force approach can take exponential time.

Instead, we can use **Two Heaps + Prefix and Suffix Sums** to solve the problem efficiently.

---

## 3. Optimized Approach: Two Heaps + Prefix/Suffix Sums

### Pattern

**Prefix Maximum-Selection Heap + Suffix Minimum-Selection Heap + Split Point**

### Main Idea

We need to minimize:

\[
\text{leftSum} - \text{rightSum}
\]

To make this difference as small as possible:

- We want the **left sum to be as small as possible**.
- We want the **right sum to be as large as possible**.

We can calculate these values independently using two heaps.

### Part 1: Prefix Array

For every valid split position, store the minimum possible sum of `n` elements chosen from the prefix.

We use a **Max Heap** to keep the `n` smallest elements seen so far.

Why a Max Heap?

Because if we have more than `n` elements, we need to remove the largest one.

Python's `heapq` is a Min Heap, so we store negative values to simulate a Max Heap.

```python
max_heap = []
total = 0

for i in range(2 * n):
    total += nums[i]
    heapq.heappush(max_heap, -nums[i])

    if len(max_heap) > n:
        total += heapq.heappop(max_heap)

    if len(max_heap) == n:
        prefix[i] = total
```

Since the heap stores negative numbers, adding the popped value back to `total` subtracts the largest original number.

After processing each position, `total` represents the sum of the `n` smallest elements in the prefix.

### Part 2: Suffix Array

For every valid split position, store the maximum possible sum of `n` elements chosen from the suffix.

We use a **Min Heap** to keep the `n` largest elements seen so far.

Why a Min Heap?

Because if we have more than `n` elements, we need to remove the smallest one.

```python
min_heap = []
total = 0

for i in range(3 * n - 1, n - 1, -1):
    total += nums[i]
    heapq.heappush(min_heap, nums[i])

    if len(min_heap) > n:
        total -= heapq.heappop(min_heap)

    if len(min_heap) == n:
        suffix[i] = total
```

The heap removes the smallest element whenever its size exceeds `n`. Therefore, `total` represents the sum of the `n` largest elements in the suffix.

### Part 3: Try Every Valid Split

For each valid split position `i`:

```python
ans = min(ans, prefix[i] - suffix[i + 1])
```

Here:

- `prefix[i]` is the minimum sum of `n` elements selected from `nums[0:i+1]`.
- `suffix[i + 1]` is the maximum sum of `n` elements selected from `nums[i+1:]`.

We calculate the difference and keep the minimum.

---

## 4. Complete Code

```python
import heapq

class Solution:
    def minimumDifference(self, nums: list[int]) -> int:
        n = len(nums) // 3

        prefix = [0] * (3 * n)
        suffix = [0] * (3 * n)

        # Part 1: Prefix - keep the n smallest elements.
        max_heap = []
        total = 0

        for i in range(2 * n):
            total += nums[i]
            heapq.heappush(max_heap, -nums[i])

            if len(max_heap) > n:
                # Remove the largest original number.
                total += heapq.heappop(max_heap)

            if len(max_heap) == n:
                prefix[i] = total

        # Part 2: Suffix - keep the n largest elements.
        min_heap = []
        total = 0

        for i in range(3 * n - 1, n - 1, -1):
            total += nums[i]
            heapq.heappush(min_heap, nums[i])

            if len(min_heap) > n:
                # Remove the smallest number.
                total -= heapq.heappop(min_heap)

            if len(min_heap) == n:
                suffix[i] = total

        # Part 3: Try every valid split.
        ans = float("inf")

        for i in range(n - 1, 2 * n):
            ans = min(ans, prefix[i] - suffix[i + 1])

        return ans
```

---

## 5. Dry Run

Consider the example:

```python
nums = [7, 9, 5, 8, 1, 3]
```

The length is `6`, so:

```python
n = 6 // 3
n = 2
```

We need to select two elements for the left sum and two elements for the right sum, while minimizing their difference.

### Part 1: Build the Prefix Array

We process the first `2 * n = 4` elements:

```python
[7, 9, 5, 8]
```

We maintain a Max Heap containing the two smallest elements seen so far.

| Index | Number | Two Smallest Elements | Prefix Sum |
|---:|---:|---|---:|
| 0 | 7 | `[7]` | Not recorded |
| 1 | 9 | `[7, 9]` | 16 |
| 2 | 5 | `[5, 7]` | 12 |
| 3 | 8 | `[5, 7]` | 12 |

Therefore:

```python
prefix[1] = 16
prefix[2] = 12
prefix[3] = 12
```

The important value is that the prefix sum becomes `12` after processing `5` and remains `12` after processing `8`, because the two smallest elements are still `5` and `7`.

### Part 2: Build the Suffix Array

We process the array from right to left, starting at index `5`.

The relevant suffixes begin at index `2` or later.

We maintain a Min Heap containing the two largest elements seen so far.

| Index | Number | Two Largest Elements | Suffix Sum |
|---:|---:|---|---:|
| 5 | 3 | `[3]` | Not recorded |
| 4 | 1 | `[1, 3]` | 4 |
| 3 | 8 | `[3, 8]` | 11 |
| 2 | 5 | `[5, 8]` | 13 |

Therefore:

```python
suffix[4] = 4
suffix[3] = 11
suffix[2] = 13
```

### Part 3: Calculate the Difference

The valid split indices are:

```python
range(n - 1, 2 * n)
```

For `n = 2`, this means indices `1`, `2`, and `3`.

We compare the prefix sum with the suffix sum immediately after the split.

| Split Index `i` | Prefix Sum | Suffix Sum | Difference |
|---:|---:|---:|---:|
| 1 | `prefix[1] = 16` | `suffix[2] = 13` | 3 |
| 2 | `prefix[2] = 12` | `suffix[3] = 11` | 1 |
| 3 | `prefix[3] = 12` | `suffix[4] = 4` | 8 |

The minimum difference is:

```python
min(3, 1, 8) = 1
```

**Output:**

```python
1
```

---

## 6. Why Do We Use Two Different Heaps?

The objective is:

\[
\min(\text{leftSum} - \text{rightSum})
\]

This means we want to minimize the left sum and maximize the right sum.

| Part | Goal | Heap | Reason |
|---|---|---|---|
| Prefix | Keep the `n` smallest elements | Max Heap | Remove the largest when the heap exceeds `n` |
| Suffix | Keep the `n` largest elements | Min Heap | Remove the smallest when the heap exceeds `n` |

### Prefix: Max Heap

Suppose the heap contains:

```python
[7, 9, 5]
```

We only want the two smallest elements.

Remove `9`, the largest element, leaving:

```python
[5, 7]
```

The sum is:

```python
5 + 7 = 12
```

### Suffix: Min Heap

Suppose the heap contains:

```python
[3, 1, 8]
```

We want the two largest elements.

Remove `1`, the smallest element, leaving:

```python
[3, 8]
```

The sum is:

```python
3 + 8 = 11
```

This is why we use a Max Heap for the prefix and a Min Heap for the suffix.

---

## 7. Understanding the `total` Updates

### Prefix

```python
total += nums[i]
heapq.heappush(max_heap, -nums[i])

if len(max_heap) > n:
    total += heapq.heappop(max_heap)
```

We first add the current number to `total` and insert it into the heap.

If the heap size becomes greater than `n`, we remove the largest original number.

Since the heap stores negative numbers, the popped value is negative.

For example:

```python
total = 21
popped = -9

total += popped
total = 12
```

This effectively subtracts `9`.

### Suffix

```python
total += nums[i]
heapq.heappush(min_heap, nums[i])

if len(min_heap) > n:
    total -= heapq.heappop(min_heap)
```

Here, the heap stores actual positive or negative array values.

When we remove the smallest element, we subtract that element from the running total.

For example:

```python
total = 21
popped = 1

total -= popped
total = 20
```

The heap and `total` always represent the same selected elements.

---

## 8. Why Does the Split Loop Start at `n - 1`?

```python
for i in range(n - 1, 2 * n):
    ans = min(ans, prefix[i] - suffix[i + 1])
```

The split must leave enough elements on both sides to select `n` elements.

The left side ends at index `i`, while the right side starts at index `i + 1`.

We require:

- At least `n` elements in the left prefix.
- At least `n` elements in the right suffix.

Therefore, valid split indices range from:

```python
n - 1
```

through:

```python
2 * n - 1
```

The Python range endpoint is exclusive, so:

```python
range(n - 1, 2 * n)
```

includes exactly those indices.

The corresponding suffix access is:

```python
suffix[i + 1]
```

because the right part begins immediately after the split.

---

## 9. Complexity Analysis

Let `n` represent one-third of the input array length. The full array contains `3n` elements.

### Time Complexity: `O(n log n)`

- Prefix processing visits `2n` elements.
- Suffix processing visits `2n` elements.
- Each heap insertion or removal takes at most `O(log n)`.
- The split loop visits `n + 1` positions and performs constant-time calculations.

Therefore, the overall time complexity is:

\[
O(n \log n)
\]

Since the input length is `3n`, this is also `O(N log N)` when `N` represents the full array length.

### Space Complexity: `O(n)`

- Prefix array: `O(n)`.
- Suffix array: `O(n)`.
- Each heap contains at most `n` elements: `O(n)`.

Therefore, the total auxiliary space complexity is:

\[
O(n)
\]

---

## 10. Common Mistakes

### Mistake 1: Using the wrong heap for the prefix

The prefix needs the smallest `n` elements, so we remove the largest element whenever the heap exceeds size `n`.

Use a Max Heap simulated with negative values.

### Mistake 2: Using the wrong heap for the suffix

The suffix needs the largest `n` elements, so we remove the smallest element whenever the heap exceeds size `n`.

Use a Min Heap with the original values.

### Mistake 3: Forgetting to update `total`

Every insertion and removal must be reflected in the running sum.

Otherwise, the prefix and suffix arrays will contain incorrect sums.

### Mistake 4: Using `suffix[i]` instead of `suffix[i + 1]`

The split divides the array between indices `i` and `i + 1`.

The suffix must start at `i + 1`.

### Mistake 5: Confusing selected elements with contiguous elements

The prefix and suffix define the available regions, but the heap selects the `n` smallest or largest elements within those regions. Those selected elements do not need to be adjacent.

---

## 11. Brute Force vs Optimized

| Feature | Brute Force | Two Heaps |
|---|---|---|
| Approach | Try possible removal combinations | Calculate optimal prefix and suffix sums |
| Time Complexity | Exponential in a basic recursive approach | `O(n log n)` |
| Space Complexity | `O(n)` recursion stack | `O(n)` |
| Main Concept | Enumerate choices | Greedy selection using heaps |
| Best Use | Understand the problem | Efficient solution |

---

## 12. Revision Cheat Sheet

- **Problem:** Minimize the difference between the left sum and the right sum after removing `n` elements.
- **Pattern:** Prefix + Suffix + Two Heaps.
- **Prefix Goal:** Find the sum of the `n` smallest elements in each eligible prefix.
- **Prefix Heap:** Max Heap using negative values.
- **Suffix Goal:** Find the sum of the `n` largest elements in each eligible suffix.
- **Suffix Heap:** Min Heap using original values.
- **Final Formula:** `prefix[i] - suffix[i + 1]`.
- **Time Complexity:** `O(n log n)`.
- **Space Complexity:** `O(n)`.

> **One-Line Pattern:** Minimum Difference = Prefix Sums of the N Smallest Elements + Suffix Sums of the N Largest Elements + Try Every Valid Split.