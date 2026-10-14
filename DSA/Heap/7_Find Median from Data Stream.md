# Find Median from Data Stream

## 1. Problem

Design a data structure that supports two operations:

- `addNum(num)`: Add an integer to the data stream.
- `findMedian()`: Return the median of all numbers added so far.

The median is:
- **Odd number of elements:** The middle element after sorting.
- **Even number of elements:** The average of the two middle elements after sorting.

### Example

```python
addNum(1)
addNum(2)
findMedian()  # 1.5

addNum(3)
findMedian()  # 2.0
```

After adding `1` and `2`, the sorted values are `[1, 2]`. The median is `(1 + 2) / 2 = 1.5`.

After adding `3`, the sorted values are `[1, 2, 3]`. The median is `2`.

---

## 2. Brute Force Approach

### Idea

Store all numbers in a list. Whenever `findMedian()` is called:

1. Sort the list.
2. Find the middle element if the size is odd.
3. Return the average of the two middle elements if the size is even.

### Code

```python
class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)

    def findMedian(self) -> float:
        nums = sorted(self.nums)
        n = len(nums)

        if n % 2 == 1:
            return float(nums[n // 2])

        return (nums[n // 2 - 1] + nums[n // 2]) / 2.0
```

### Complexity

Let `n` be the number of elements currently stored.

- `addNum()`: `O(1)` amortized
- `findMedian()`: `O(n log n)` time for sorting
- Space: `O(n)` for storing the numbers and creating the sorted copy

### Why Is It Slow?

Every median query sorts all the numbers again, even though only one new number may have been added.

**Optimization:** Use two heaps to maintain the middle elements without sorting the entire collection.

---

## 3. Pattern: Two Heaps

**Pattern:** Use a Max Heap for the smaller half and a Min Heap for the larger half.

The key observation is that we don't need the entire collection sorted. We only need quick access to the middle element or the two middle elements.

### Why Two Heaps?

We divide all numbers into two halves:

- `max_heap`: Stores the smaller half of the numbers.
- `min_heap`: Stores the larger half of the numbers.

Python's `heapq` implements a Min Heap. To simulate a Max Heap, store negative values.

```text
                 All Numbers
                      |
             -------------------
             |                 |
          Max Heap          Min Heap
       (smaller half)     (larger half)
             |                 |
       Largest of         Smallest of
       smaller half       larger half
             |                 |
          max_heap[0]       min_heap[0]
```

The roots of these heaps give us direct access to the middle values.

---

## 4. Main Idea

### Rule 1: Max Heap stores the smaller half

```python
self.max_heap = []
```

Python's Min Heap stores the smallest value at index `0`. To simulate a Max Heap, insert negative numbers.

```python
heapq.heappush(self.max_heap, -num)
```

For example, inserting `10`, `5`, and `8` stores negative values internally:

```text
Original values: 10, 5, 8

Max Heap using negative values:
Internal values: -10, -8, -5  # Conceptual heap ordering

Root: -10
Actual maximum: -(-10) = 10
```

The internal array is not necessarily fully sorted; only the heap property is guaranteed.

### Rule 2: Min Heap stores the larger half

```python
self.min_heap = []
```

The Min Heap stores normal positive or negative input values, with the smallest value at the root.

```python
heapq.heappush(self.min_heap, num)
```

### Rule 3: Maintain the size balance

The heaps must satisfy:

1. `len(max_heap)` is either equal to `len(min_heap)` or exactly one greater.
2. Every value in the smaller half is less than or equal to every value in the larger half.

```text
Case 1: Odd number of elements

max_heap: [1, 2, 3]  # Conceptual values; actual storage uses negatives
min_heap: [4, 5]

The max heap has one extra element.
Median = largest value in the smaller half.


Case 2: Even number of elements

max_heap: [1, 2]
min_heap: [3, 4]

Both heaps have equal size.
Median = average of 2 and 3.
```

The heap arrays shown above are conceptual groups, not literal Python heap arrays.

---

## 5. Complete Code with Comments

```python
import heapq

class MedianFinder:

    def __init__(self):
        # Max Heap: stores the smaller half using negative values
        self.max_heap = []

        # Min Heap: stores the larger half using normal values
        self.min_heap = []

    def addNum(self, num: int) -> None:

        # Step 1: Insert into max_heap.
        # Negative values simulate a Max Heap.
        heapq.heappush(self.max_heap, -num)

        # Step 2: Move the largest value from the smaller half
        # to the larger half.
        # Negating again converts it back to its original value.
        heapq.heappush(
            self.min_heap,
            -heapq.heappop(self.max_heap)
        )

        # Step 3: If min_heap becomes larger than max_heap,
        # move its smallest value back to max_heap.
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(
                self.max_heap,
                -heapq.heappop(self.min_heap)
            )

    def findMedian(self) -> float:

        # Odd number of elements:
        # max_heap contains one extra element.
        # Its root is the middle element.
        if len(self.max_heap) > len(self.min_heap):
            return float(-self.max_heap[0])

        # Even number of elements:
        # The median is the average of the two heap roots.
        return (-self.max_heap[0] + self.min_heap[0]) / 2.0
```

---

## 6. How `addNum()` Works

The insertion logic has three steps.

### Step 1: Insert into `max_heap`

```python
heapq.heappush(self.max_heap, -num)
```

We initially put the new number into the smaller half.

### Step 2: Move the root from `max_heap` to `min_heap`

```python
heapq.heappush(
    self.min_heap,
    -heapq.heappop(self.max_heap)
)
```

`heappop()` removes the root of `max_heap`.

Because it stores negative numbers, its root represents the **largest actual number in the smaller half**.

Moving that value to `min_heap` helps maintain the ordering between the two halves.

### Step 3: Balance the heap sizes

```python
if len(self.min_heap) > len(self.max_heap):
    heapq.heappush(
        self.max_heap,
        -heapq.heappop(self.min_heap)
    )
```

If `min_heap` has more elements than `max_heap`, move its smallest value back to `max_heap`.

After these steps:

- `max_heap` has either the same number of elements as `min_heap` or one extra.
- The smaller and larger halves remain correctly ordered.

---

## 7. Dry Run

Let's insert the numbers `1`, `2`, and `3`.

### Insert `1`

After insertion and rebalancing:

```text
max_heap: [-1]
min_heap: []

findMedian() = 1.0
```

There is one element, so the median is `1`.

### Insert `2`

First, insert `2` into `max_heap`:

```text
max_heap: [-2, -1]  # Internal heap representation
```

The root `-2` represents the actual value `2`. Move it to `min_heap`, then rebalance if needed.

```text
max_heap: [-1]
min_heap: [2]

findMedian() = (-max_heap[0] + min_heap[0]) / 2
             = (1 + 2) / 2
             = 1.5
```

There are two elements, so the median is the average of `1` and `2`.

### Insert `3`

After insertion and rebalancing:

```text
max_heap: [-2, -1]
min_heap: [3]

findMedian() = -max_heap[0]
             = 2.0
```

There are three elements. The max heap has one extra element, so its root gives the median.

### Summary

| Inserted number | Smaller half | Larger half | Median |
|---|---|---|---:|
| `1` | `[1]` | `[]` | `1.0` |
| `2` | `[1]` | `[2]` | `1.5` |
| `3` | `[1, 2]` | `[3]` | `2.0` |

The halves above show actual values, not the negative values used internally by `max_heap`.

---

## 8. How `findMedian()` Works

### Case 1: Odd number of elements

```python
if len(self.max_heap) > len(self.min_heap):
    return float(-self.max_heap[0])
```

The max heap contains one extra element. Its root is the largest element in the smaller half, which is the middle element overall.

We negate the root because `max_heap` stores negative values.

### Case 2: Even number of elements

```python
return (-self.max_heap[0] + self.min_heap[0]) / 2.0
```

Both heaps have the same size.

- `-self.max_heap[0]` gives the largest element in the smaller half.
- `self.min_heap[0]` gives the smallest element in the larger half.

These are the two middle values, so their average is the median.

---

## 9. Complexity Analysis

Let `n` be the number of elements added so far.

| Operation | Time Complexity | Explanation |
|---|---|---|
| `__init__()` | `O(1)` | Initializes two empty heaps |
| `addNum()` | `O(log n)` | A constant number of heap insertions and removals |
| `findMedian()` | `O(1)` | Reads the roots and heap sizes |
| Auxiliary space | `O(n)` | Both heaps together store all elements |

**Important:** `findMedian()` is `O(1)` because it never sorts the elements or traverses either heap.

---

## 10. Common Mistakes

1. **Forgetting negative values in the Max Heap:** Python's `heapq` is a Min Heap, so use `-num` to simulate a Max Heap.
2. **Forgetting to negate the popped value:** When moving a value from `max_heap` to `min_heap`, use `-heapq.heappop(self.max_heap)`.
3. **Balancing incorrectly:** `max_heap` must always have either the same number of elements as `min_heap` or one extra.
4. **Returning the wrong root for an odd count:** Return `-self.max_heap[0]`, not `self.min_heap[0]`.
5. **Using integer division for the even median:** Use `/ 2.0` so the answer can be a floating-point number.
6. **Sorting on every query:** That defeats the purpose of maintaining two heaps.

---

## 11. Brute Force vs Optimized Approach

| Feature | Brute Force | Two Heaps |
|---|---|---|
| `addNum()` | `O(1)` amortized | `O(log n)` |
| `findMedian()` | `O(n log n)` | `O(1)` |
| Extra space | `O(n)` | `O(n)` |
| Maintains useful ordering | No | Yes |
| Best for frequent median queries | No | Yes |

---

## 12. Pattern Recognition

Use **Two Heaps** when a problem requires finding the median of a continuously growing data stream.

The general idea is to keep the smaller half in a Max Heap and the larger half in a Min Heap. Balance their sizes so the median is always available from their roots.

Related concepts:
- Min Heap and Max Heap
- Priority Queues
- Streaming Algorithms
- Heap balancing

---

## 13. Revision Cheat Sheet

- **Max Heap:** Stores the smaller half using negative values.
- **Min Heap:** Stores the larger half using normal values.
- **Odd count:** `max_heap` has one extra element; median is `-max_heap[0]`.
- **Even count:** Median is `(-max_heap[0] + min_heap[0]) / 2`.
- **Insertion:** Push into max heap → move its root to min heap → rebalance if needed.
- **`addNum()`:** `O(log n)`
- **`findMedian()`:** `O(1)`
- **Space:** `O(n)`

> **One-Line Pattern:** Find Median from Data Stream = Two Heaps + Max Heap for the Smaller Half + Min Heap for the Larger Half + Balance Their Sizes.