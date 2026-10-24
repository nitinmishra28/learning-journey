# Sliding Window Maximum

## 1. Problem

Given an array `nums` and an integer `k`, a sliding window of size `k` moves from left to right across the array.

Return the maximum value in each window.

### Example

**Input:**

```python
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
```

**Output:**

```python
[3, 3, 5, 5, 6, 7]
```

**Explanation:**

The windows and their maximum values are:

| Window | Maximum |
|---|---:|
| `[1, 3, -1]` | 3 |
| `[3, -1, -3]` | 3 |
| `[-1, -3, 5]` | 5 |
| `[-3, 5, 3]` | 5 |
| `[5, 3, 6]` | 6 |
| `[3, 6, 7]` | 7 |

---

## 2. Brute Force Approach

### Idea

For every window of size `k`:

1. Identify the window's starting and ending indices.
2. Find the maximum element in that window.
3. Append the maximum to the answer.

### Code

```python
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        ans = []

        for i in range(len(nums) - k + 1):
            window = nums[i:i + k]
            ans.append(max(window))

        return ans
```

### Complexity

- **Time Complexity:** `O(n * k)` — finding the maximum in each window takes `O(k)`, and there are `n - k + 1` windows.
- **Space Complexity:** `O(k)` for the temporary window, excluding the output.

### Why is it inefficient?

Consecutive windows overlap. Many elements are checked repeatedly even though they were already considered in the previous window.

We can optimize this using a heap to efficiently access the maximum element.

---

## 3. Optimized Approach: Max Heap

### Pattern

**Sliding Window + Max Heap + Index-Based Expiration**

### Main Idea

We use a Max Heap to keep the largest element at the top.

Python's `heapq` is a Min Heap, so we store negative values:

```python
heapq.heappush(max_heap, (-nums[i], i))
```

Each heap entry contains:

```python
(-value, index)
```

For example:

```python
nums = [1, 3, -1]
```

The heap entries are:

```python
(-1, 0)
(-3, 1)
(1, 2)
```

Conceptually, the heap prioritizes the largest original number because its negative value is the smallest.

The index tells us **when an element is outside the current window**.

### Two Important Rules

1. **Maximum:** The root of the heap gives the largest value among the entries currently stored.
2. **Expiration:** If the root's index is outside the current window, remove it.

An expired element does not always need to be removed immediately. It only needs to be removed when it reaches the root, because only the root can affect the current maximum.

---

## 4. Complete Code

```python
import heapq

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        max_heap = []
        ans = []

        # Step 1: Add the first k elements.
        for i in range(k):
            heapq.heappush(max_heap, (-nums[i], i))

        # Maximum of the first window.
        ans.append(-max_heap[0][0])

        # Step 2: Slide the window one position at a time.
        for i in range(k, len(nums)):

            # Add the new element entering the window.
            heapq.heappush(max_heap, (-nums[i], i))

            # Remove expired elements from the heap's root.
            while max_heap and max_heap[0][1] <= i - k:
                heapq.heappop(max_heap)

            # Root contains the maximum of the current window.
            ans.append(-max_heap[0][0])

        return ans
```

---

## 5. Dry Run

Consider:

```python
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
```

### Step 1: Build the First Window

The first three elements are:

```python
[1, 3, -1]
```

Insert these entries into the heap:

```python
(-1, 0)
(-3, 1)
(1, 2)
```

The root is:

```python
(-3, 1)
```

The negative value is `-3`, so the actual maximum is:

```python
-(-3) = 3
```

Answer:

```python
ans = [3]
```

### Step 2: Move to the Next Window

The next element is `-3`, at index `3`.

Insert it:

```python
heapq.heappush(max_heap, (3, 3))
```

The current window is:

```python
[3, -1, -3]
```

The valid indices are:

```python
1, 2, 3
```

Check whether the root has expired:

```python
max_heap[0][1] <= i - k
```

Here:

```python
3 - 3 = 0
```

Index `0` is expired because:

```python
0 <= 0  # True
```

Remove it if it is at the root.

The next valid maximum is `3`.

Answer:

```python
ans = [3, 3]
```

### Step 3: Move to the Next Window

The next element is `5`, at index `4`.

Insert:

```python
(-5, 4)
```

The current window is:

```python
[-1, -3, 5]
```

The valid indices are:

```python
2, 3, 4
```

The root represents `5`, so the maximum is `5`.

Answer:

```python
ans = [3, 3, 5]
```

### Step 4: Continue Sliding

Repeat the same process for the remaining elements.

| Current Index `i` | New Element | Current Window | Maximum |
|---:|---:|---|---:|
| 5 | 3 | `[-3, 5, 3]` | 5 |
| 6 | 6 | `[5, 3, 6]` | 6 |
| 7 | 7 | `[3, 6, 7]` | 7 |

### Final Output

```python
[3, 3, 5, 5, 6, 7]
```

---

## 6. Understanding the Expiration Condition

```python
while max_heap and max_heap[0][1] <= i - k:
    heapq.heappop(max_heap)
```

This is one of the most important lines in the solution.

### What does `i - k` represent?

Suppose:

```python
i = 4
k = 3
```

The current window ends at index `4`.

Its starting index is:

```python
i - k + 1
= 4 - 3 + 1
= 2
```

Therefore, the valid window indices are:

```python
2, 3, 4
```

Any index less than `2` is expired.

The expiration condition becomes:

```python
index < i - k + 1
```

This is equivalent to:

```python
index <= i - k
```

So the code removes expired entries from the root.

**Important:** The `while` loop removes expired entries only while they are at the root. Expired entries deeper in the heap can remain temporarily because they cannot affect the current maximum. If one reaches the root later, it will be removed then.

---

## 7. Why Store the Index Along with the Value?

We store:

```python
(-nums[i], i)
```

Instead of storing only:

```python
-nums[i]
```

Why?

Because the value alone cannot tell us whether the element still belongs to the current window.

For example:

```python
nums = [10, 2, 3, 4]
k = 2
```

After the window moves, the value `10` must no longer be considered because its index is outside the window.

Storing the index lets us detect that the element has expired.

**Rule:** In sliding-window problems, store indices whenever you need to determine whether an element is still inside the current window.

---

## 8. Complexity Analysis

Let `n` be the length of `nums`.

### Time Complexity: `O(n log n)`

- Building the initial heap takes `O(k log k)` using repeated insertions.
- Each of the remaining `n - k` elements is inserted into the heap in `O(log n)`.
- Each heap entry can be removed at most once, costing `O(log n)` per removal.

Therefore, the overall worst-case time complexity is:

\[
O(n \log n)
\]

### Space Complexity: `O(n)`

The heap can retain entries from previous windows that have expired but are not yet at the root. Consequently, it can grow to `O(n)` in the worst case.

The output contains `n - k + 1` values, requiring `O(n)` space as well.

- **Auxiliary heap space:** `O(n)`
- **Output space:** `O(n)`
- **Total space including output:** `O(n)`

---

## 9. Important Note: Heap vs Monotonic Deque

The heap approach works, but it is not the most efficient standard solution for this problem.

A **monotonic decreasing deque** can solve Sliding Window Maximum in:

- **Time Complexity:** `O(n)`
- **Auxiliary Space Complexity:** `O(k)`

Why is the deque better?

- It removes elements that cannot become the maximum of any future window.
- It keeps indices in decreasing order of their corresponding values.
- The front always contains the maximum element's index.
- Each index is added and removed at most once.

The heap approach is still useful for learning heap operations and index-based expiration.

---

## 10. Common Mistakes

### Mistake 1: Forgetting to negate the value

Incorrect:

```python
heapq.heappush(max_heap, (nums[i], i))
```

This creates a Min Heap based on the original values, so the smallest element appears at the root.

Correct:

```python
heapq.heappush(max_heap, (-nums[i], i))
```

### Mistake 2: Forgetting to convert the root back to a positive value

Correct:

```python
ans.append(-max_heap[0][0])
```

### Mistake 3: Not storing indices

Without indices, we cannot determine whether an element has left the current window.

### Mistake 4: Removing expired entries from the wrong end

The heap does not keep elements in sorted order. We can efficiently inspect only the root, so the code removes expired entries from the root when necessary.

### Mistake 5: Using the wrong boundary condition

Correct:

```python
max_heap[0][1] <= i - k
```

An index equal to `i - k` is already outside the current window.

---

## 11. Brute Force vs Optimized

| Feature | Brute Force | Max Heap | Monotonic Deque |
|---|---|---|---|
| Approach | Scan every window | Heap with indices | Maintain decreasing values |
| Time | `O(nk)` | `O(n log n)` | `O(n)` |
| Auxiliary Space | `O(k)` | `O(n)` | `O(k)` |
| Main concept | Repeated maximum search | Heap + expiration | Monotonic ordering |

---

## 12. Revision Cheat Sheet

- **Problem:** Find the maximum in every window of size `k`.
- **Pattern:** Sliding Window + Max Heap.
- **Heap Entry:** `(-nums[i], i)`.
- **Maximum:** `-max_heap[0][0]`.
- **Expiration Condition:** `max_heap[0][1] <= i - k`.
- **Why Store Indices?** To identify elements outside the window.
- **Time Complexity:** `O(n log n)`.
- **Auxiliary Space:** `O(n)`.
- **Optimal Standard Approach:** Monotonic Deque, `O(n)` time and `O(k)` auxiliary space.

> **One-Line Pattern:** Sliding Window Maximum using a Heap = Store Negative Values with Indices + Remove Expired Root Entries + Read the Maximum from the Root.