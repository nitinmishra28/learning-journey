# Smallest Range Covering Elements from K Lists

## 1. Problem

Given `k` sorted arrays, find the **smallest range `[start, end]` that contains at least one element from every array**.

The range must include at least one element from each list.

If multiple ranges have the same length, return the range with the smaller starting value.

### Example

```python
nums = [
    [4, 10, 15, 24, 26],
    [0, 9, 12, 20],
    [5, 18, 22, 30]
]
```

One smallest range is:

```text
[20, 24]
```

Why?

- Array 1 contributes `24`.
- Array 2 contributes `20`.
- Array 3 contributes `22`.

All three arrays have at least one element inside the range.

Range length:

```text
24 - 20 = 4
```

Answer:

```python
[20, 24]
```

---

# 2. Brute Force Approach

The straightforward approach is to consider possible ranges and check whether each range contains at least one element from every array.

For every candidate range:

1. Check each array.
2. Determine whether it contains an element inside the range.
3. If every array is represented, compare its length with the smallest range found so far.

This can be expensive because many candidate ranges may need to be checked.

A more practical baseline is to enumerate possible lower and upper endpoints from the input values, then test each candidate against all arrays.

### Complexity

Let:

- `k` = number of arrays
- `N` = total number of elements

There can be up to `O(N²)` candidate endpoint pairs. Checking one candidate against all arrays by scanning their elements can take `O(N)` time.

A straightforward implementation can therefore take:

```text
Time: O(N³) in the worst case
```

This is not efficient for large inputs.

Instead, we can use a **Min Heap + Sliding Range** to solve the problem in `O(N log k)` time.

---

# 3. Optimized Approach: Min Heap + Sliding Range

The key idea is:

> Keep one current element from every sorted array in a Min Heap, while tracking the maximum among those elements.

At any moment, we have:

```text
Minimum value = smallest element in the heap
Maximum value = largest current element among the arrays
```

These two values define a range covering at least one current element from every array.

```text
Current elements:
Array 1 → 4
Array 2 → 0
Array 3 → 5

Minimum = 0
Maximum = 5

Current range = [0, 5]
```

We repeatedly:

1. Evaluate the current range.
2. Remove the smallest element.
3. Advance in the array from which that element came.
4. Insert the next element from that array.
5. Update the maximum value.
6. Stop when one array runs out of elements.

Why stop when an array is exhausted?

Because we can no longer select another element from that array to continue the process. Every subsequent valid range would need an element from that array, so the current range is our final candidate to evaluate.

---

# 4. Code

```python
import heapq

class Solution:
    def smallestRange(self, nums: list[list[int]]) -> list[int]:
        min_heap = []
        max_value = float('-inf')

        # Insert the first element from every array
        for i in range(len(nums)):
            value = nums[i][0]

            heapq.heappush(min_heap, (value, i, 0))

            # Track the maximum current element
            max_value = max(max_value, value)

        # Initial range
        start = min_heap[0][0]
        end = max_value

        while True:
            # Remove the smallest current element
            min_value, list_index, element_index = heapq.heappop(min_heap)

            # Update the best range if the current one is smaller
            if max_value - min_value < end - start:
                start = min_value
                end = max_value

            # Stop if this array has no next element
            if element_index + 1 == len(nums[list_index]):
                break

            # Move to the next element in the same array
            next_index = element_index + 1
            next_element = nums[list_index][next_index]

            heapq.heappush(
                min_heap,
                (next_element, list_index, next_index)
            )

            # Update the maximum current element
            max_value = max(max_value, next_element)

        return [start, end]
```

---

# 5. Understanding the Heap Tuple

This line is important:

```python
heapq.heappush(min_heap, (value, i, 0))
```

Each heap entry contains:

```text
(value, list_index, element_index)
```

| Value | Meaning | Purpose |
|---|---|---|
| `value` | Current element | Finds the smallest current value |
| `list_index` | Which array contains the element | Identifies which array to advance |
| `element_index` | Position within that array | Finds the next element |

For example:

```text
(4, 0, 0)
(0, 1, 0)
(5, 2, 0)
```

This means:

```text
4 comes from nums[0][0]
0 comes from nums[1][0]
5 comes from nums[2][0]
```

We store the indices because after removing the minimum, we must know which array to advance.

---

# 6. Why Track `max_value` Separately?

```python
max_value = float('-inf')
```

The heap efficiently provides the minimum value:

```python
min_heap[0][0]
```

But we also need the maximum current value to calculate the range.

Instead of searching the heap for the maximum every time, we maintain:

```python
max_value
```

During initialization:

```python
max_value = max(max_value, value)
```

Whenever a new element enters the heap:

```python
max_value = max(max_value, next_element)
```

Because each array is sorted, its next element cannot be smaller than its previous element.

Therefore, the maximum of the current elements can never decrease as the algorithm progresses.

---

# 7. Why Does the Heap Contain One Element per Array?

Consider:

```text
Array 1: [4, 10, 15, 24, 26]
Array 2: [0, 9, 12, 20]
Array 3: [5, 18, 22, 30]
```

Initially:

```text
Array 1 → 4
Array 2 → 0
Array 3 → 5
```

Heap:

```text
[0, 4, 5]
```

The current range is:

```text
[0, 5]
```

We remove `0`, the smallest element.

Since `0` came from Array 2, we advance only Array 2:

```text
Array 2: 0 → 9
```

The new current elements are:

```text
Array 1 → 4
Array 2 → 9
Array 3 → 5
```

Heap values:

```text
[4, 5, 9]
```

The new range is:

```text
[4, 9]
```

We do not need every element from every array in the heap. We only need the next available candidate from each array.

---

# 8. Dry Run

Input:

```python
nums = [
    [4, 10, 15, 24, 26],
    [0, 9, 12, 20],
    [5, 18, 22, 30]
]
```

### Step 1: Initialize

Current elements:

```text
4, 0, 5
```

Therefore:

```text
min_value = 0
max_value = 5
```

Initial range:

```text
[0, 5]
```

Its length is:

```text
5 - 0 = 5
```

### Step 2: Remove `0`

`0` belongs to Array 2.

Advance Array 2:

```text
0 → 9
```

Current elements:

```text
4, 9, 5
```

Range:

```text
[4, 9]
```

Length:

```text
9 - 4 = 5
```

The length equals the previous best, so the strict comparison does not update the range.

### Step 3: Remove `4`

`4` belongs to Array 1.

Advance Array 1:

```text
4 → 10
```

Current elements:

```text
10, 9, 5
```

Range:

```text
[5, 10]
```

Length:

```text
10 - 5 = 5
```

Again, the range length is equal to the best length.

### Step 4: Remove `5`

`5` belongs to Array 3.

Advance Array 3:

```text
5 → 18
```

Current elements:

```text
10, 9, 18
```

Range:

```text
[9, 18]
```

Length:

```text
18 - 9 = 9
```

This is not better.

### Step 5: Continue

The algorithm continues by removing the smallest current element and advancing its array.

Eventually, the current elements include:

```text
Array 1 → 24
Array 2 → 20
Array 3 → 22
```

The range is:

```text
[20, 24]
```

Length:

```text
24 - 20 = 4
```

This improves the best range.

The algorithm continues until one array is exhausted, then returns:

```python
[20, 24]
```

---

# 9. Why Does This Work?

At every step, the heap contains one current element from each array.

Let:

```text
min_value = smallest current element
max_value = largest current element
```

Then:

```text
[max_value - (max_value - min_value), max_value]
```

is simply:

```text
[min_value, max_value]
```

This range contains one current element from every array.

We always advance the array containing the minimum value because the current range's lower endpoint is the smallest available element.

To potentially improve the range, we need to increase that lower endpoint. Advancing another array would leave the current minimum unchanged.

Since the arrays are sorted, advancing the minimum's array gives us the next possible candidate for a larger lower endpoint.

We record the best range encountered along the way.

---

# 10. Why Stop When One Array Is Exhausted?

Consider the point where the smallest element comes from Array 2:

```text
Array 2: [0, 9, 12]
```

Suppose we remove `12`, and there is no next element.

Now Array 2 has no current candidate left.

We cannot continue the algorithm while maintaining one current element from every array.

Therefore, we stop after evaluating the current range.

This condition handles that case:

```python
if element_index + 1 == len(nums[list_index]):
    break
```

---

# 11. Complexity Analysis

Let:

- `k` = number of arrays
- `N` = total number of elements across all arrays

### Initialization

We insert the first element of every array.

```text
Time: O(k log k)
```

### Main Loop

Each element is removed from the heap at most once, and each next element is inserted at most once.

Each heap operation takes:

```text
O(log k)
```

Therefore:

```text
Time: O(N log k)
```

### Overall Time Complexity

```text
O(k log k + N log k)
```

Since `k <= N` for non-empty arrays:

```text
Time = O(N log k)
```

### Space Complexity

The heap contains at most one element per array.

```text
Space = O(k)
```

The result contains only two numbers, so its space is:

```text
O(1)
```

---

# 12. Complexity Comparison

| Approach | Time | Auxiliary Space |
|---|---:|---:|
| Brute-force candidate ranges | Can reach O(N³) | Depends on implementation |
| Min Heap + tracked maximum | O(N log k) | O(k) |

The Min Heap approach is efficient because it explores only the next candidate from each sorted array.

---

# 13. Common Mistakes

### Mistake 1: Forgetting to Update `max_value`

Whenever a next element is inserted, update:

```python
max_value = max(max_value, next_element)
```

Otherwise, the calculated range may use an outdated upper endpoint.

### Mistake 2: Advancing the Wrong Array

After removing:

```python
min_value, list_index, element_index
```

advance:

```python
nums[list_index]
```

Do not advance every array.

### Mistake 3: Inserting Every Element Initially

Only insert the first element of each array.

The heap should contain at most `k` elements.

### Mistake 4: Forgetting to Check the Range Before Breaking

The current range must be evaluated before stopping because the popped minimum may be the final element of its array.

Your code correctly evaluates the range before checking whether the array is exhausted.

### Mistake 5: Updating the Range on Equal Lengths Without Considering the Tie Rule

Your condition is:

```python
if max_value - min_value < end - start:
```

It updates only when the new range is strictly shorter.

For the usual smallest-range problem, this is sufficient when the initial range is initialized correctly: the algorithm processes lower endpoints in nondecreasing order, so retaining the earlier range on a tie preserves the smaller starting value.

---

# 14. Pattern Recognition

When you see:

- Multiple sorted arrays.
- A range that must contain at least one value from every array.
- A need to repeatedly identify the minimum current value.

Think:

```text
Min Heap + Track Maximum + Advance the Minimum's Array
```

This is closely related to:

- Merge K Sorted Arrays
- Merge K Sorted Linked Lists
- K-way merge
- Smallest range covering elements from K lists

---

# 15. Revision Cheat Sheet

```text
Smallest Range Covering K Lists
               |
               ↓
   Insert First Element from Each List
               |
               ↓
       Track Current Maximum
               |
               ↓
        Pop Minimum from Heap
               |
               ↓
       Evaluate [minimum, maximum]
               |
               ↓
       Update Best Range if Smaller
               |
               ↓
       Is Its Array Exhausted?
            /          \
          Yes           No
           |             |
          Stop      Insert Next Element
                         |
                         ↓
                 Update Maximum
                         |
                         ↓
                      Repeat
```

### Important Variables

```python
min_heap
```

Stores one current element from each array.

```python
max_value
```

Tracks the largest current element.

```python
start, end
```

Store the best range found so far.

```python
list_index, element_index
```

Identify which array and position to advance.

### Complexity

```text
Time  = O(N log k)
Space = O(k)
```

### Core Insight

> **Keep one current element from each sorted array in a Min Heap, track the maximum, evaluate the current range, and advance the array containing the minimum.**

---

# One-Line Pattern

> **Smallest Range in K Lists = Min Heap + Track Maximum + Repeatedly Advance the Minimum's Array.**