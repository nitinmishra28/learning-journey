# Merge K Sorted Arrays Using a Min Heap

## 1. Problem

Given a matrix `mat` containing `k` individually sorted arrays, merge all arrays into a single sorted array.

### Example

```python
mat = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]
```

Output:

```python
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Each individual array is already sorted. We need to combine them while maintaining the overall sorted order.

---

# 2. Brute Force Approach

The simplest approach is to combine all arrays into one array and sort it.

```python
def mergeArrays(mat):
    result = []

    for arr in mat:
        result.extend(arr)

    result.sort()

    return result
```

### Complexity

Let:

- `k` = number of arrays
- `N` = total number of elements across all arrays

Combining the arrays takes:

```text
O(N)
```

Sorting all elements takes:

```text
O(N log N)
```

Therefore:

```text
Time:  O(N log N)
Space: O(N)
```

### Why Can We Do Better?

Every individual array is already sorted.

We don't need to sort all elements again. Instead, we can repeatedly select the smallest available element using a **Min Heap**.

---

# 3. Optimized Approach: Min Heap

The key idea is:

> Keep only the smallest unprocessed element from each array in the Min Heap.

Initially, insert the first element of every non-empty array.

Whenever we remove the smallest element:

1. Add it to the result.
2. Identify which array it came from.
3. Insert the next element from that same array, if one exists.

Repeat until the heap becomes empty.

### Example

```text
mat = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]
```

Initially, insert the first element of each array:

```text
Heap = [1, 2, 3]
```

The smallest element is `1`.

After removing `1`, insert the next element from its array: `4`.

```text
Heap = [2, 3, 4]
```

Next, remove `2` and insert `5`.

```text
Heap = [3, 4, 5]
```

Continue until all elements are processed.

Final result:

```text
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

# 4. Code

```python
import heapq

class Solution:
    def mergeArrays(self, mat):
        min_heap = []
        result = []

        # Insert the first element of every non-empty array
        for i in range(len(mat)):
            if mat[i]:
                heapq.heappush(min_heap, (mat[i][0], i, 0))

        # Process elements in sorted order
        while min_heap:
            value, array_index, element_index = heapq.heappop(min_heap)

            # Add the smallest element to the result
            result.append(value)

            # Find the next element in the same array
            nxt_index = element_index + 1

            if nxt_index < len(mat[array_index]):
                heapq.heappush(
                    min_heap,
                    (mat[array_index][nxt_index], array_index, nxt_index)
                )

        return result
```

---

# 5. Understanding the Heap Tuple

This is the most important line:

```python
heapq.heappush(min_heap, (mat[i][0], i, 0))
```

Each heap entry contains three values:

```text
(value, array_index, element_index)
```

For example:

```python
mat = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]
```

The initial heap entries are:

```text
(1, 0, 0)
(2, 1, 0)
(3, 2, 0)
```

Each part has a specific purpose.

| Tuple Value | Meaning | Why Needed? |
|---|---|---|
| `value` | Current element | To find the smallest element |
| `array_index` | Which array contains it | To access the correct array |
| `element_index` | Position inside that array | To find the next element |

### Why Store the Array Index?

Suppose we remove:

```text
(2, 1, 0)
```

This tells us:

```text
value = 2
array_index = 1
element_index = 0
```

The value `2` came from:

```python
mat[1]
```

which is:

```text
[2, 5, 8]
```

After processing `2`, we need to insert `5`.

Without `array_index`, we wouldn't know which array to continue processing.

### Why Store the Element Index?

We need to know the position of the current element so we can calculate:

```python
nxt_index = element_index + 1
```

For:

```text
[2, 5, 8]
```

if the current index is `0`:

```text
nxt_index = 0 + 1 = 1
```

Therefore:

```python
mat[1][1] = 5
```

The next element can now be inserted into the heap.

---

# 6. Why Store Only One Element From Each Array?

Consider:

```text
Array 1: [1, 4, 7]
Array 2: [2, 5, 8]
Array 3: [3, 6, 9]
```

Initially, the heap contains:

```text
1, 2, 3
```

Why not insert every element?

Because each array is already sorted.

For Array 1:

```text
1 < 4 < 7
```

As long as `1` has not been processed, we don't need to consider `4` or `7`.

Once `1` is removed, `4` becomes eligible.

The same logic applies to every array.

Therefore, at any moment, we only need the **next unprocessed element from each array**.

This keeps the heap size at most `k`, where `k` is the number of arrays.

---

# 7. Dry Run

Input:

```python
mat = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]
```

### Step 1: Initialize Heap

Insert the first element from every array:

```text
Heap entries:

(1, 0, 0)
(2, 1, 0)
(3, 2, 0)
```

Conceptually:

```text
Heap values = [1, 2, 3]
Result = []
```

### Step 2: Remove `1`

Pop:

```text
(1, 0, 0)
```

Append `1`:

```text
Result = [1]
```

The next element from Array 0 is:

```text
mat[0][1] = 4
```

Insert:

```text
(4, 0, 1)
```

Heap values:

```text
[2, 3, 4]
```

### Step 3: Remove `2`

Pop:

```text
(2, 1, 0)
```

Append `2`:

```text
Result = [1, 2]
```

Next element:

```text
mat[1][1] = 5
```

Insert `(5, 1, 1)`.

Heap values:

```text
[3, 4, 5]
```

### Step 4: Remove `3`

Pop:

```text
(3, 2, 0)
```

Append `3`:

```text
Result = [1, 2, 3]
```

Next element:

```text
mat[2][1] = 6
```

Insert `(6, 2, 1)`.

Heap values:

```text
[4, 5, 6]
```

### Remaining Steps

Continue the same process:

| Removed | Insert Next | Result |
|---:|---:|---|
| 4 | 7 | `[1, 2, 3, 4]` |
| 5 | 8 | `[1, 2, 3, 4, 5]` |
| 6 | 9 | `[1, 2, 3, 4, 5, 6]` |
| 7 | Nothing | `[1, 2, 3, 4, 5, 6, 7]` |
| 8 | Nothing | `[1, 2, 3, 4, 5, 6, 7, 8]` |
| 9 | Nothing | `[1, 2, 3, 4, 5, 6, 7, 8, 9]` |

Once all arrays are exhausted, the heap becomes empty.

Final answer:

```text
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

# 8. Why Does This Work?

At any moment, the heap contains the smallest unprocessed element from each non-empty array.

Because every array is sorted:

```text
Current element ≤ Remaining elements in the same array
```

Therefore, the globally smallest unprocessed element must be among the elements currently in the heap.

The Min Heap returns that smallest element.

After removing it, we insert the next element from the same array so that the array continues to participate in the comparison.

Repeating this process produces elements in sorted order.

---

# 9. Complexity Analysis

Let:

- `k` = number of arrays
- `N` = total number of elements across all arrays

### Heap Initialization

We insert the first element of each non-empty array.

There are at most `k` insertions.

```text
Time: O(k log k)
```

### Processing Elements

Every element is removed from the heap exactly once.

For each element, we perform at most one heap insertion.

Each heap operation costs:

```text
O(log k)
```

because the heap contains at most `k` elements.

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

The heap contains at most one entry per array:

```text
O(k)
```

The result stores all `N` elements:

```text
O(N)
```

Therefore:

```text
Auxiliary Heap Space = O(k)
Total Extra Space     = O(N + k) = O(N)
```

The total space includes the output array.

---

# 10. Complexity Comparison

| Approach | Time | Extra Space | Main Idea |
|---|---:|---:|---|
| Combine and sort | O(N log N) | O(N) | Sort every element |
| Min Heap | O(N log k) | O(N), including output | Merge sorted arrays incrementally |

The heap approach is especially useful when the number of arrays `k` is much smaller than the total number of elements `N`.

---

# 11. Common Mistakes

### Mistake 1: Inserting All Elements Initially

That would make the heap size `N`.

Instead, insert only the first element of every non-empty array.

### Mistake 2: Forgetting the Array Index

```python
(array_index)
```

tells us which array to continue processing.

Without it, we cannot reliably find the next element.

### Mistake 3: Forgetting the Element Index

```python
element_index
```

tells us where the current element is located.

Use:

```python
nxt_index = element_index + 1
```

to move forward in that array.

### Mistake 4: Accessing an Out-of-Range Index

Always check:

```python
if nxt_index < len(mat[array_index]):
```

before accessing the next element.

Otherwise, an `IndexError` may occur.

### Mistake 5: Forgetting Empty Arrays

The initial loop uses:

```python
if mat[i]:
```

so empty arrays are skipped.

This prevents accessing `mat[i][0]` when the array has no elements.

### Mistake 6: Thinking the Heap Is Fully Sorted

The heap only guarantees that the smallest element is at the root.

It does not keep all elements in sorted order.

The final result is sorted because we repeatedly pop the smallest available element.

---

# 12. Pattern Recognition

When you see:

- Multiple sorted arrays or lists.
- A requirement to merge them into sorted order.
- A need to repeatedly find the smallest available element.

Think:

```text
Min Heap + K-Way Merge
```

This pattern also appears in:

- Merge K Sorted Linked Lists
- Merge K Sorted Lists
- External sorting
- Merging sorted data streams
- Finding the smallest element across multiple sorted sources

---

# 13. Revision Cheat Sheet

```text
Merge K Sorted Arrays
          |
          ↓
Insert First Element of Each Non-Empty Array
          |
          ↓
       Min Heap
          |
          ↓
      Heap Not Empty?
          |
          ↓
      Pop Minimum
          |
          ↓
     Append to Result
          |
          ↓
  Find Next Element in Same Array
          |
          ↓
    If It Exists, Push It
          |
          ↓
         Repeat
          |
          ↓
      Return Result
```

### Heap Entry

```python
(value, array_index, element_index)
```

- `value`: current element used for comparison.
- `array_index`: identifies the source array.
- `element_index`: identifies the element's position.

### Complexity

```text
Time:  O(N log k)
Heap:  O(k)
Output: O(N)
```

### Core Insight

> **Keep one current element from each sorted array in a Min Heap. Pop the smallest, add it to the result, and insert the next element from the same array.**

---

# One-Line Pattern

> **Merge K Sorted Arrays = Min Heap + One Current Element per Array + Track Array and Element Indices.**