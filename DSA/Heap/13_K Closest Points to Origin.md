# K Closest Points to Origin

## 1. Problem

Given an array `points` where `points[i] = [x, y]` represents a point on a 2D plane, return the `k` points closest to the origin `(0, 0)`.

The distance between a point `(x, y)` and the origin is calculated using the Euclidean distance formula:

\[
d = \sqrt{x^2 + y^2}
\]

**Important:** We do not need to calculate the square root because comparing \(x^2 + y^2\) gives the same ordering as comparing the actual distances.

### Example

**Input:**
```python
points = [[1, 3], [-2, 2], [5, 8], [0, 1]]
k = 2
```

**Output:**
```python
[[0, 1], [-2, 2]]
```

**Explanation:**

Squared distances from the origin:

| Point | Squared Distance |
|---|---:|
| `[1, 3]` | 1² + 3² = 10 |
| `[-2, 2]` | (-2)² + 2² = 8 |
| `[5, 8]` | 5² + 8² = 89 |
| `[0, 1]` | 0² + 1² = 1 |

The two closest points are `[0, 1]` and `[-2, 2]`.

---

## 2. Brute Force Approach

### Idea

1. Calculate the squared distance for every point.
2. Sort all points by their distance.
3. Return the first `k` points.

### Code

```python
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        points.sort(key=lambda point: point[0] ** 2 + point[1] ** 2)

        return points[:k]
```

### Complexity

- **Time Complexity:** `O(n log n)` — sorting all points.
- **Space Complexity:** `O(n)` in the worst case for sorting, depending on the sorting implementation.

### Why can we optimize it?

We only need the `k` closest points. Sorting every point is unnecessary when `k` is much smaller than `n`.

We can use a **Max Heap of size `k`** to efficiently keep the closest points.

---

## 3. Optimized Approach: Max Heap

### Pattern

**Top K Smallest Elements using a Max Heap of Size K**

### Main Idea

Python's `heapq` implements a **Min Heap** by default. However, we need a Max Heap because we want to remove the farthest point whenever we have more than `k` candidates.

We simulate a Max Heap by storing negative squared distances.

```python
distance = -(x * x + y * y)
```

Because the distances are negative:

- A farther point has a more negative value.
- A closer point has a less negative value.
- The Min Heap puts the most negative value at its root, representing the farthest point.

### Why use a Max Heap?

Suppose `k = 2`.

We want to keep only the two closest points.

If we have three candidate points, we remove the farthest one. A Max Heap allows us to access that farthest point in `O(1)` time and remove it in `O(log k)` time.

The heap never needs to grow beyond `k` elements.

---

## 4. Complete Code

```python
import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []

        for x, y in points:
            # Negative squared distance simulates a Max Heap.
            distance = -(x * x + y * y)

            if len(heap) == k:
                # Insert the new point and remove the farthest point.
                heapq.heappushpop(heap, (distance, x, y))
            else:
                # Fill the heap until it contains k points.
                heapq.heappush(heap, (distance, x, y))

        # Extract coordinates from the heap tuples.
        return [(x, y) for distance, x, y in heap]
```

---

## 5. Dry Run

Consider:

```python
points = [[1, 3], [-2, 2], [5, 8], [0, 1]]
k = 2
```

### Step 1: Process `[1, 3]`

Squared distance:

```python
1 * 1 + 3 * 3 = 10
```

Store negative distance:

```python
(-10, 1, 3)
```

Heap:

```python
[(-10, 1, 3)]
```

Only one point is present, so we insert it.

### Step 2: Process `[-2, 2]`

Squared distance:

```python
(-2) * (-2) + 2 * 2 = 8
```

Heap entry:

```python
(-8, -2, 2)
```

Heap:

```python
[(-10, 1, 3), (-8, -2, 2)]
```

The heap now contains `k = 2` points.

### Step 3: Process `[5, 8]`

Squared distance:

```python
5 * 5 + 8 * 8 = 89
```

Heap entry:

```python
(-89, 5, 8)
```

The heap already contains `k` points, so we use:

```python
heapq.heappushpop(heap, (-89, 5, 8))
```

Since `-89` is the smallest heap value, the new, farthest point is immediately removed.

Heap remains:

```python
[(-10, 1, 3), (-8, -2, 2)]
```

### Step 4: Process `[0, 1]`

Squared distance:

```python
0 * 0 + 1 * 1 = 1
```

Heap entry:

```python
(-1, 0, 1)
```

The heap is full. `heappushpop()` inserts the new point and removes the smallest heap value, `-10`.

Heap now contains:

```python
[(-8, -2, 2), (-1, 0, 1)]
```

These represent the two closest points.

### Final Output

```python
[[-2, 2], [0, 1]]
```

The order may differ because the problem does not require the result to be sorted.

---

## 6. Understanding `heappushpop()`

```python
heapq.heappushpop(heap, (distance, x, y))
```

This operation:

1. Adds the new element to the heap.
2. Removes and returns the smallest element.
3. Restores the heap property.

Because our distances are negative, the smallest value represents the farthest point.

**Purpose:** Keep the heap size fixed at `k` while retaining the `k` closest points.

### Why not use a Min Heap of positive distances?

A Min Heap of positive distances would remove the closest point first, which is the opposite of what we need.

We need to remove the farthest candidate, so we simulate a Max Heap using negative distances.

---

## 7. Why Store `(distance, x, y)`?

```python
heapq.heappush(heap, (distance, x, y))
```

Python compares tuples lexicographically:

1. Compare `distance`.
2. If distances are equal, compare `x`.
3. If `x` is equal, compare `y`.

This allows the heap to organize points by negative distance while retaining their coordinates.

The return statement:

```python
return [(x, y) for distance, x, y in heap]
```

extracts the coordinates and ignores the stored distance.

---

## 8. Complexity Analysis

Let `n` be the total number of points and `k` be the number of closest points requested.

| Operation | Complexity |
|---|---|
| Insert a point while filling the heap | `O(log k)` |
| Replace the farthest point | `O(log k)` |
| Process all `n` points | `O(n log k)` |
| Heap storage | `O(k)` |

**Time Complexity:** `O(n log k)`

We process every point, and each heap operation costs at most `O(log k)`.

**Auxiliary Space Complexity:** `O(k)`

The heap stores at most `k` points. The returned list also contains `k` points, so total additional space including the output is `O(k)`.

---

## 9. Common Mistakes

### Mistake 1: Forgetting the negative sign

Incorrect:

```python
distance = x * x + y * y
```

With a Min Heap, this would prioritize the closest point for removal.

Correct:

```python
distance = -(x * x + y * y)
```

### Mistake 2: Using the wrong heap size condition

Correct:

```python
if len(heap) == k:
    heapq.heappushpop(heap, (distance, x, y))
else:
    heapq.heappush(heap, (distance, x, y))
```

This ensures that the heap never exceeds size `k`.

### Mistake 3: Calculating the square root

You do not need:

```python
distance = math.sqrt(x * x + y * y)
```

Squared distances preserve the same ordering and avoid unnecessary computation.

### Mistake 4: Assuming the output is sorted

The heap guarantees the heap property, not fully sorted order. Any order containing the correct `k` points is valid.

---

## 10. Brute Force vs Optimized

| Feature | Brute Force | Max Heap |
|---|---|---|
| Approach | Sort all points | Maintain the `k` closest points |
| Time | `O(n log n)` | `O(n log k)` |
| Extra space | Up to `O(n)` for sorting | `O(k)` heap |
| Best when | Simplicity matters | `k` is much smaller than `n` |

---

## 11. How to Recognize This Pattern

Look for these clues:

- The problem asks for the **K closest**, **K smallest**, or **K best** elements.
- You do not need every element sorted.
- You need to maintain only `k` candidates.
- You need to remove the worst candidate whenever a better one appears.

For **K smallest elements**, use a Max Heap of size `k`.

For **K largest elements**, use a Min Heap of size `k`.

---

## 12. Revision Cheat Sheet

- **Problem:** Find the `k` closest points to the origin.
- **Pattern:** Top K Elements.
- **Data Structure:** Max Heap of size `k`.
- **Python Trick:** Negate squared distances to simulate a Max Heap.
- **Key Operation:** `heapq.heappushpop()`.
- **Time Complexity:** `O(n log k)`. 
- **Auxiliary Space:** `O(k)`.  

> **One-Line Pattern:** K Closest Points = Max Heap of Size K + Negative Squared Distances + Remove the Farthest Point Whenever a New Candidate Arrives.