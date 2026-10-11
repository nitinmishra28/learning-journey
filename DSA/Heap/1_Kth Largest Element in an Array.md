# Kth Largest Element in an Array

## 1. Problem

Given an integer array `nums` and an integer `k`, return the **kth largest element** in the array.

The kth largest element is based on sorted order, not the kth distinct value.

### Example

```python
nums = [3, 2, 1, 5, 6, 4]
k = 2
```

Sorted in descending order:

```text
[6, 5, 4, 3, 2, 1]
```

Answer:

```text
5
```

The second-largest element is `5`.

---

# 2. Brute Force Approach

Sort the array in descending order and return the element at index `k - 1`.

```python
def findKthLargest(nums, k):
    nums.sort(reverse=True)
    return nums[k - 1]
```

### Why `k - 1`?

Python uses zero-based indexing.

```text
Largest element      → index 0
2nd largest element  → index 1
3rd largest element  → index 2
kth largest element  → index k - 1
```

### Complexity

```text
Time:  O(n log n)
Space: O(n) worst-case auxiliary space for sorting,
       depending on the sorting implementation
```

### Limitation

We sort the entire array even though we only need one element.

Can we solve this without fully sorting the array?

Yes, using a **Min Heap of size k**.

---

# 3. Optimized Approach: Min Heap

The key idea is:

> Maintain a Min Heap containing only the largest `k` elements seen so far.

Python's `heapq` implements a Min Heap, where:

```python
heap[0]
```

is the smallest element in the heap.

Why is this useful?

If we maintain the largest `k` elements, the smallest among those `k` elements is exactly the **kth largest element**.

### Example

```text
nums = [3, 2, 1, 5, 6, 4]
k = 2
```

We want to keep only the two largest elements.

Eventually:

```text
Heap contains: [5, 6]
```

Because it is a Min Heap:

```text
heap[0] = 5
```

Therefore:

```text
2nd largest = 5
```

We never need to sort the entire array.

---

# 4. Code

```python
import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # Keep the first k elements
        heap = nums[:k]

        # Convert them into a Min Heap
        heapq.heapify(heap)

        # Process the remaining elements
        for num in nums[k:]:

            # Replace the smallest element
            # only if the new number is larger
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

        # Smallest among the k largest elements
        # is the kth largest element
        return heap[0]
```

---

# 5. Understanding the Code

## Step 1: Create a Heap of Size k

```python
heap = nums[:k]
```

For:

```text
nums = [3, 2, 1, 5, 6, 4]
k = 2
```

We get:

```text
heap = [3, 2]
```

We initially select the first `k` elements.

---

## Step 2: Convert the List into a Min Heap

```python
heapq.heapify(heap)
```

Now the list satisfies the Min Heap property.

For this example:

```text
heap = [2, 3]
```

The smallest element is always available at:

```python
heap[0]
```

So:

```text
heap[0] = 2
```

**Important:** A heap is not a fully sorted array. Only the heap property is guaranteed.

---

## Step 3: Process Remaining Elements

```python
for num in nums[k:]:
```

The remaining elements are:

```text
[1, 5, 6, 4]
```

For every number, compare it with the smallest element currently in the heap.

```python
if num > heap[0]:
```

There are two cases.

### Case A: New Number Is Smaller or Equal

Suppose:

```text
num = 1
heap = [2, 3]
```

Since:

```text
1 < 2
```

we ignore it.

Why?

The heap already contains two elements greater than `1`.

So `1` cannot be among the two largest elements.

### Case B: New Number Is Larger

Suppose:

```text
num = 5
heap = [2, 3]
```

Since:

```text
5 > 2
```

we remove the smallest element:

```python
heapq.heappop(heap)
```

Heap becomes:

```text
[3]
```

Then insert `5`:

```python
heapq.heappush(heap, 5)
```

Heap becomes:

```text
[3, 5]
```

The heap size remains `k = 2`.

---

# 6. Dry Run

Input:

```text
nums = [3, 2, 1, 5, 6, 4]
k = 2
```

### Step 1: Initialize

```text
First k elements = [3, 2]
```

After heapify:

```text
Heap = [2, 3]
```

### Step 2: Process `1`

```text
num = 1
heap[0] = 2
```

Since:

```text
1 <= 2
```

Ignore it.

```text
Heap = [2, 3]
```

### Step 3: Process `5`

```text
num = 5
heap[0] = 2
```

Since:

```text
5 > 2
```

Remove `2` and insert `5`.

```text
Heap = [3, 5]
```

### Step 4: Process `6`

```text
num = 6
heap[0] = 3
```

Since:

```text
6 > 3
```

Remove `3` and insert `6`.

```text
Heap = [5, 6]
```

### Step 5: Process `4`

```text
num = 4
heap[0] = 5
```

Since:

```text
4 < 5
```

Ignore it.

```text
Heap = [5, 6]
```

### Step 6: Return

```python
return heap[0]
```

Answer:

```text
5
```

---

# 7. Why Does This Work?

Suppose:

```text
nums = [7, 10, 4, 3, 20, 15]
k = 3
```

The three largest elements are:

```text
[10, 15, 20]
```

The smallest among them is:

```text
10
```

Therefore:

```text
3rd largest = 10
```

Our algorithm maintains exactly `k` elements that are the largest among the numbers processed so far.

Whenever a new number is greater than the smallest heap element:

1. Remove the current smallest.
2. Insert the new number.

Otherwise, ignore it.

At the end:

```text
Heap contains the k largest elements
```

Since it is a Min Heap:

```text
heap[0] = kth largest element
```

---

# 8. Why Use a Min Heap Instead of a Max Heap?

A Max Heap gives quick access to the largest element.

But for the kth largest problem, we don't need to extract all the largest elements.

We only need to maintain the largest `k` elements.

A Min Heap of size `k` lets us quickly remove the smallest element whenever a better candidate arrives.

```text
Min Heap of size k
        |
        ├── Keeps only k largest elements
        |
        └── Root = smallest among them
                    |
                    └── kth largest element
```

This is why a **Min Heap** is the natural choice.

---

# 9. Complexity

Let:

- `n` = number of elements
- `k` = required rank

### Heap Initialization

```python
heap = nums[:k]
heapq.heapify(heap)
```

Creating the slice takes `O(k)` time and space.

Heapifying takes `O(k)` time.

### Processing Remaining Elements

There are:

```text
n - k
```

remaining elements.

Each comparison takes:

```text
O(1)
```

If replacement is needed, popping and pushing take:

```text
O(log k)
```

Therefore, the total time complexity is:

```text
O(k) + O((n-k) log k)
```

Simplified upper bound:

```text
O(n log k)
```

### Space Complexity

The heap stores at most `k` elements:

```text
O(k)
```

**Note:** In the given implementation, `nums[k:]` creates a separate list containing the remaining elements, which can use up to `O(n-k)` additional space. If you iterate using indices instead, the auxiliary space can remain `O(k)`.

---

# 10. Complexity Comparison

| Approach | Time | Auxiliary Space |
|---|---:|---:|
| Sort entire array | O(n log n) | Depends on sorting implementation |
| Min Heap of size k | O(n log k) | O(k) with index iteration |

The heap approach is particularly useful when `k` is much smaller than `n`.

For example:

```text
n = 1,000,000
k = 5
```

We only maintain five elements rather than sorting the entire array.

---

# 11. Common Mistakes

### Mistake 1: Using a Max Heap of size k

A Max Heap of size `k` does not directly maintain the kth largest element in the same way.

Use a Min Heap because its root is the smallest among the selected `k` largest elements.

### Mistake 2: Removing the root for every number

Incorrect approach:

```python
heapq.heappop(heap)
heapq.heappush(heap, num)
```

If we do this for every element, smaller numbers may replace larger candidates.

Always compare first:

```python
if num > heap[0]:
```

### Mistake 3: Returning the Largest Element

```python
return max(heap)
```

This returns the largest element among the retained `k` elements, not the kth largest.

For example:

```text
Heap = [5, 6]
```

The second-largest element is:

```text
heap[0] = 5
```

### Mistake 4: Forgetting Heap Size

The heap should never contain more than `k` elements.

Removing one element before inserting the replacement preserves this property.

### Mistake 5: Confusing Largest with Distinct Largest

The problem asks for the kth largest element, not the kth distinct element.

For example:

```text
nums = [3, 2, 3, 1]
k = 2
```

Sorted descending:

```text
[3, 3, 2, 1]
```

The second-largest element is:

```text
3
```

Duplicates count as separate elements.

---

# 12. Pattern Recognition

When you see:

```text
Find kth largest element
```

think:

```text
Min Heap of size k
```

When you see:

```text
Find kth smallest element
```

think:

```text
Max Heap of size k
```

The general rule:

| Requirement | Heap |
|---|---|
| Kth largest | Min Heap of size k |
| Kth smallest | Max Heap of size k |
| Top k largest elements | Min Heap of size k |
| Top k smallest elements | Max Heap of size k |

---

# 13. Revision Cheat Sheet

```text
Kth Largest Element
        |
        ↓
Create Min Heap of First k Elements
        |
        ↓
Heapify
        |
        ↓
Process Remaining Elements
        |
        ↓
num > heap[0]?
        |
    +---+---+
    |       |
   Yes      No
    |       |
 Pop root  Ignore
 Push num
    |
    ↓
Return heap[0]
```

### Key operations

```python
heapq.heapify(heap)     # Build Min Heap
heapq.heappop(heap)     # Remove smallest
heapq.heappush(heap, x) # Insert element
heap[0]                 # Smallest element
```

### Complexity

```text
Time:  O(n log k)
Space: O(k) using index iteration
```

### Core Insight

> **Maintain a Min Heap of size `k`. Its root is the smallest among the `k` largest elements, which is exactly the kth largest element.**

---

# One-Line Pattern

> **Kth Largest = Min Heap of Size k + Replace Root Only When a Larger Element Arrives.**