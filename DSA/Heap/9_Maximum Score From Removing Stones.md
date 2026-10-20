# Maximum Score From Removing Stones

## 1. Problem

You are given three piles of stones containing `a`, `b`, and `c` stones.

In each move:
- Choose two **non-empty piles**.
- Remove one stone from each selected pile.
- Increase the score by `1`.

Return the maximum score possible.

### Example

```python
a = 2
b = 4
c = 6

Output: 6
```

**Explanation:**

We can make 6 moves by repeatedly selecting two non-empty piles until only one pile has stones left.

---

## 2. Brute Force Approach

### Idea

Since there are only three piles, we could simulate moves by choosing two non-empty piles, removing one stone from each, and tracking the score.

However, choosing the best pair at every step is important. A greedy strategy that repeatedly selects the two largest piles gives the maximum score.

A simple simulation that chooses any two non-empty piles without a strategy is not guaranteed to be optimal.

### Complexity

If we simulate one move at a time, the number of moves can be as large as approximately half the total number of stones.

Let `S = a + b + c`.

- **Time:** `O(S)` for a simulation that performs one operation per move.
- **Auxiliary space:** `O(1)` for a direct simulation using three variables.

**Optimization:** Use a Max Heap to efficiently select the two largest non-empty piles in every move.

---

## 3. Pattern: Greedy + Max Heap

The main idea is to always choose the **two largest non-empty piles**.

Why?

If we choose a small pile while leaving two larger piles untouched, we may leave the smaller pile empty too early and lose the opportunity to make more moves.

Choosing the two largest piles helps distribute the removals across the piles and maximizes the number of valid moves.

A Max Heap lets us retrieve the two largest piles efficiently.

Python's `heapq` implements a Min Heap, so we store negative values to simulate a Max Heap.

```text
Three piles
    |
    v
Insert negative pile sizes into Max Heap
    |
    v
Extract the two largest piles
    |
    v
Remove one stone from each
    |
    v
Increase score by 1
    |
    v
Insert non-empty piles back into heap
    |
    v
Repeat until fewer than two non-empty piles remain
```

---

## 4. Main Idea

### Step 1: Create a Max Heap

```python
max_heap = []

heapq.heappush(max_heap, -a)
heapq.heappush(max_heap, -b)
heapq.heappush(max_heap, -c)
```

Python's `heapq` keeps the smallest value at the root.

By inserting negative values, the largest actual pile becomes the root.

For example:

```python
a, b, c = 2, 4, 6
```

The heap stores:

```python
[-6, -4, -2]
```

The internal heap array is not necessarily fully sorted, but its root represents the largest actual pile after negation.

### Step 2: Continue while at least two piles are non-empty

```python
while len(max_heap) > 1:
```

Every move requires two non-empty piles.

If fewer than two piles remain, no more moves are possible.

### Step 3: Extract the two largest piles

```python
pile1 = -heapq.heappop(max_heap)
pile2 = -heapq.heappop(max_heap)
```

We negate the popped values to recover their original pile sizes.

### Step 4: Remove one stone from each pile

```python
pile1 -= 1
pile2 -= 1

score += 1
```

Each valid move removes exactly two stones, one from each selected pile, and increases the score by one.

### Step 5: Push non-empty piles back

```python
if pile1 > 0:
    heapq.heappush(max_heap, -pile1)

if pile2 > 0:
    heapq.heappush(max_heap, -pile2)
```

Empty piles cannot be selected again, so we do not reinsert them.

---

## 5. Complete Code with Comments

```python
import heapq

class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:

        # Step 1: Create a Max Heap using negative values
        max_heap = []

        heapq.heappush(max_heap, -a)
        heapq.heappush(max_heap, -b)
        heapq.heappush(max_heap, -c)

        score = 0

        # Step 2: Continue while at least two non-empty piles exist
        while len(max_heap) > 1:

            # Step 3: Extract the two largest piles
            pile1 = -heapq.heappop(max_heap)
            pile2 = -heapq.heappop(max_heap)

            # Step 4: Remove one stone from each pile
            pile1 -= 1
            pile2 -= 1

            # One valid move is completed
            score += 1

            # Step 5: Reinsert piles only if they are non-empty
            if pile1 > 0:
                heapq.heappush(max_heap, -pile1)

            if pile2 > 0:
                heapq.heappush(max_heap, -pile2)

        return score
```

---

## 6. Dry Run

Consider:

```python
a = 2
b = 4
c = 6
```

Initial piles:

```text
Pile A = 2
Pile B = 4
Pile C = 6

Score = 0
```

We repeatedly select the two largest non-empty piles.

| Move | Selected piles before removal | Piles after removal `(A, B, C)` | Score |
|---|---|---|---:|
| 1 | `6, 4` | `(2, 3, 5)` | 1 |
| 2 | `5, 3` | `(2, 2, 4)` | 2 |
| 3 | `4, 2` | `(2, 1, 3)` | 3 |
| 4 | `3, 2` | `(1, 1, 2)` | 4 |
| 5 | `2, 1` | `(1, 0, 1)` | 5 |
| 6 | `1, 1` | `(0, 0, 1)` | 6 |

At the end, only one pile contains stones.

Since every move requires two non-empty piles, the process stops.

```python
Output: 6
```

---

## 7. Why Does the Algorithm Stop?

```python
while len(max_heap) > 1:
```

The heap stores only non-empty piles.

- Heap size `3`: Three piles are available; a move is possible.
- Heap size `2`: Two piles are available; a move is possible.
- Heap size `1`: Only one pile remains; no move is possible.
- Heap size `0`: All piles are empty; no move is possible.

Therefore, the algorithm stops when fewer than two non-empty piles remain.

---

## 8. Complexity Analysis

Let `S = a + b + c` be the total number of stones.

There are at most `min(S // 2, S - max(a, b, c))` moves, because each move removes two stones and the largest pile cannot be paired with itself.

| Operation | Complexity |
|---|---|
| Build heap using three pushes | `O(1)` |
| Each move: two pops and up to two pushes | `O(log 3) = O(1)` |
| Total time | `O(S)` upper bound |
| Auxiliary space | `O(1)` |

Because there are always at most three piles, each heap operation takes constant time. The total running time depends on how many moves are performed.

**Note:** For very large pile sizes, this simulation may be slow because it processes one move at a time. A mathematical solution can calculate the maximum score directly.

---

## 9. Common Mistakes

1. **Using a Min Heap with positive values:** This would select the smallest piles instead of the largest.
2. **Forgetting to negate popped values:** Convert the negative heap values back to actual pile sizes.
3. **Reinserting empty piles:** Only reinsert a pile if its remaining size is greater than zero.
4. **Continuing with one pile:** A valid move requires two non-empty piles.
5. **Forgetting to increment the score:** Each successful pair removal contributes exactly one point.
6. **Assuming a heap is fully sorted:** A heap guarantees its root property, not that every element is in sorted order.

---

## 10. Brute Force vs Greedy Max Heap

| Feature | Basic Simulation | Greedy Max Heap |
|---|---|---|
| Strategy | Select any two non-empty piles | Select the two largest piles |
| Guarantees maximum score | Not without an optimal selection rule | Yes |
| Time | `O(S)` | `O(S)` |
| Auxiliary space | `O(1)` | `O(1)` because there are only three piles |

Both approaches may simulate the same number of moves, but the heap makes the greedy selection rule explicit.

---

## 11. Revision Cheat Sheet

- **Pattern:** Greedy + Max Heap.
- **Heap entry:** Negative pile size.
- **Each move:** Pop two largest piles, subtract one from each, increment score.
- **Reinsert:** Only piles with remaining stones.
- **Stop:** Fewer than two non-empty piles remain.
- **Time:** `O(a + b + c)` upper bound for the simulation.
- **Space:** `O(1)` because the heap contains at most three elements.

> **One-Line Pattern:** Maximum Score From Removing Stones = Greedy + Max Heap + Repeatedly Remove One Stone from the Two Largest Non-Empty Piles.             