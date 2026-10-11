# Minimum Cost to Connect Ropes

## 1. Problem

Given an array `arr`, where each element represents the length of a rope, connect all ropes into one rope with the **minimum total cost**.

The cost of connecting two ropes is the sum of their lengths.

After connecting two ropes, the resulting rope has a length equal to their sum and can be connected again with another rope.

### Example

```python
arr = [4, 3, 2, 6]
```

We need to connect all ropes into one.

One optimal sequence is:

```text
Ropes: [4, 3, 2, 6]

Step 1: Connect 2 and 3
        Cost = 2 + 3 = 5

        Ropes = [4, 5, 6]

Step 2: Connect 4 and 5
        Cost = 4 + 5 = 9

        Ropes = [6, 9]

Step 3: Connect 6 and 9
        Cost = 6 + 9 = 15

        Ropes = [15]
```

Total cost:

```text
5 + 9 + 15 = 29
```

Answer:

```text
29
```

---

# 2. Brute Force Approach

The simplest approach is to repeatedly:

1. Find the two smallest ropes.
2. Remove them from the array.
3. Connect them and calculate their cost.
4. Add the combined rope back.
5. Repeat until only one rope remains.

If we use a normal list and search for the two smallest elements each time, finding them takes `O(n)` time.

Since we perform this operation approximately `n - 1` times, the total time complexity is:

```text
O(n²)
```

### Why Is This Slow?

Every time two ropes are connected, we search the remaining list again to find the smallest ropes.

Instead, we can use a **Min Heap**, which gives us efficient access to the smallest elements.

---

# 3. Optimized Approach: Min Heap

The key observation is:

> **Always connect the two smallest ropes first to achieve the minimum total cost.**

This is a greedy approach.

A Min Heap is ideal because its root always contains the smallest element.

Python provides a Min Heap implementation through the `heapq` module.

```python
import heapq
```

The important operations are:

```python
heapq.heapify(pq)       # Convert a list into a Min Heap
heapq.heappop(pq)       # Remove the smallest element
heapq.heappush(pq, x)   # Insert an element
```

### Algorithm

```text
1. Convert all rope lengths into a Min Heap.
2. Initialize cost = 0.
3. While more than one rope remains:
      a. Remove the smallest rope.
      b. Remove the second-smallest rope.
      c. Add their lengths.
      d. Add this sum to the total cost.
      e. Insert the combined rope back into the heap.
4. Return the total cost.
```

---

# 4. Code

```python
import heapq

class Solution:
    def minCost(self, arr):
        # Convert the array into a Min Heap
        pq = list(arr)
        heapq.heapify(pq)

        cost = 0

        # Continue until only one rope remains
        while len(pq) > 1:

            # Remove the two smallest ropes
            first = heapq.heappop(pq)
            second = heapq.heappop(pq)

            # Connect the two ropes
            total_sum = first + second

            # Add the connection cost
            cost += total_sum

            # Insert the combined rope back
            heapq.heappush(pq, total_sum)

        return cost
```

---

# 5. Understanding the Code

## Step 1: Create the Min Heap

```python
pq = list(arr)
heapq.heapify(pq)
```

For:

```text
arr = [4, 3, 2, 6]
```

The heap contains all four rope lengths.

Conceptually:

```text
        2
       / \
      3   4
     /
    6
```

The exact internal arrangement may differ, but the smallest element is always at:

```python
pq[0]
```

Here:

```text
pq[0] = 2
```

**Important:** A heap is not a fully sorted array. It only guarantees the heap property.

---

## Step 2: Why `while len(pq) > 1`?

```python
while len(pq) > 1:
```

We need to connect at least two ropes.

When only one rope remains, all ropes have been connected.

For example:

```text
[15]
```

There is nothing left to connect, so the algorithm stops.

For `n` ropes, exactly `n - 1` connections are needed.

---

## Step 3: Remove the Two Smallest Ropes

```python
first = heapq.heappop(pq)
second = heapq.heappop(pq)
```

`heappop()` removes the smallest element.

For:

```text
[2, 3, 4, 6]
```

the two smallest values are:

```text
first = 2
second = 3
```

We always connect the two smallest available ropes.

---

## Step 4: Calculate the Connection Cost

```python
total_sum = first + second
```

For example:

```text
first = 2
second = 3

total_sum = 5
```

The cost of connecting these ropes is `5`.

---

## Step 5: Add the Cost

```python
cost += total_sum
```

The total cost includes the cost of every connection.

Initially:

```text
cost = 0
```

After connecting `2` and `3`:

```text
cost = 0 + 5 = 5
```

After the next connection costing `9`:

```text
cost = 5 + 9 = 14
```

---

## Step 6: Insert the Combined Rope

```python
heapq.heappush(pq, total_sum)
```

After connecting ropes of lengths `2` and `3`, we create a new rope of length `5`.

That rope must remain available for future connections.

```text
Before:
[2, 3, 4, 6]

Connect 2 + 3 = 5

After:
[4, 5, 6]
```

The combined rope is treated like any other rope in subsequent operations.

---

# 6. Dry Run

Input:

```python
arr = [4, 3, 2, 6]
```

Initially:

```text
Min Heap contains: [2, 3, 4, 6]
cost = 0
```

### Step 1

Remove:

```text
2 and 3
```

Connect:

```text
2 + 3 = 5
```

Update:

```text
cost = 5
```

Insert `5` back.

Remaining ropes:

```text
[4, 5, 6]
```

### Step 2

Remove:

```text
4 and 5
```

Connect:

```text
4 + 5 = 9
```

Update:

```text
cost = 5 + 9 = 14
```

Insert `9` back.

Remaining ropes:

```text
[6, 9]
```

### Step 3

Remove:

```text
6 and 9
```

Connect:

```text
6 + 9 = 15
```

Update:

```text
cost = 14 + 15 = 29
```

Insert `15` back.

Remaining ropes:

```text
[15]
```

Only one rope remains, so the loop stops.

Final answer:

```text
29
```

---

# 7. Why Does the Greedy Approach Work?

Suppose a rope is connected early.

The resulting rope may participate in several later connections.

For example:

```text
2 + 3 = 5
```

The cost `5` is counted immediately.

If the resulting rope `5` is connected again:

```text
4 + 5 = 9
```

the length `5` contributes again through the new connection cost.

Therefore, ropes that are repeatedly involved in connections can contribute to the total cost multiple times.

By connecting the two smallest ropes first, we keep these repeated contributions as small as possible.

This is the same greedy principle used in **Huffman Coding**:

> Repeatedly combine the two smallest available values.

---

# 8. Why Use a Min Heap?

We need to repeatedly retrieve the two smallest elements.

With a normal list, finding the minimum requires scanning the list.

With a Min Heap:

```python
heapq.heappop(pq)
```

removes the smallest element efficiently.

The relevant complexities are:

| Operation | Complexity |
|---|---:|
| `heapify()` | O(n) |
| `heappop()` | O(log n) |
| `heappush()` | O(log n) |
| Access minimum `pq[0]` | O(1) |

Each connection requires:

```text
2 heap pops + 1 heap push
```

Therefore, a Min Heap makes this repeated operation efficient.

---

# 9. Complexity Analysis

Let `n` be the number of ropes.

### Heap Initialization

```python
pq = list(arr)
heapq.heapify(pq)
```

Copying the array takes `O(n)` time.

Heapifying takes `O(n)` time.

### Main Loop

Each iteration connects two ropes and reduces the number of ropes by one.

Therefore, there are exactly:

```text
n - 1 iterations
```

Each iteration performs two pops and one push.

Each heap operation takes `O(log n)` time.

So the loop takes:

```text
O(n log n)
```

### Overall Time Complexity

```text
O(n) + O(n log n)
= O(n log n)
```

### Space Complexity

The heap stores at most `n` elements.

```text
O(n)
```

---

# 10. Complexity Comparison

| Approach | Time | Auxiliary Space | Idea |
|---|---:|---:|---|
| Repeatedly search for two minimums | O(n²) | O(n) | Scan the list each time |
| Min Heap | O(n log n) | O(n) | Efficiently remove the two smallest |

The Min Heap approach is more efficient because it avoids repeatedly scanning the remaining ropes.

---

# 11. Edge Cases

### Case 1: One Rope

```python
arr = [10]
```

No connection is needed.

```text
Answer = 0
```

The loop never executes because:

```python
len(pq) > 1
```

is false.

### Case 2: Two Ropes

```python
arr = [4, 6]
```

One connection:

```text
4 + 6 = 10
```

Answer:

```text
10
```

### Case 3: Equal Rope Lengths

```python
arr = [2, 2, 2]
```

First connection:

```text
2 + 2 = 4
cost = 4
```

Remaining ropes:

```text
[2, 4]
```

Second connection:

```text
2 + 4 = 6
cost = 4 + 6 = 10
```

Answer:

```text
10
```

### Case 4: Empty Array

The given implementation returns `0` for an empty array because the loop does not execute.

---

# 12. Common Mistakes

### Mistake 1: Connecting the Two Largest Ropes

Always remove the two smallest ropes:

```python
first = heapq.heappop(pq)
second = heapq.heappop(pq)
```

The greedy strategy depends on combining the minimum values first.

### Mistake 2: Forgetting to Add the Cost

This is essential:

```python
cost += total_sum
```

The answer is the sum of every connection cost, not just the final rope length.

### Mistake 3: Not Reinserting the Combined Rope

After connecting two ropes:

```python
heapq.heappush(pq, total_sum)
```

The resulting rope must be available for later connections.

### Mistake 4: Using `while pq`

Incorrect:

```python
while pq:
```

When only one rope remains, the algorithm would attempt to pop two elements.

Use:

```python
while len(pq) > 1:
```

### Mistake 5: Sorting After Every Connection

Repeated sorting is unnecessary.

The Min Heap maintains efficient access to the smallest ropes automatically.

---

# 13. Pattern Recognition

When you see a problem where you must:

- Repeatedly select the two smallest values.
- Combine them into a new value.
- Add a cost for each combination.
- Reinsert the combined value.

Think:

```text
Min Heap + Greedy
```

This pattern also appears in:

- Huffman Coding
- Connecting ropes with minimum cost
- Combining files with minimum cost
- Repeatedly merging the two smallest values

---

# 14. Revision Cheat Sheet

```text
Minimum Cost to Connect Ropes
             |
             ↓
       Build Min Heap
             |
             ↓
     More than one rope?
             |
             ↓
       Pop smallest
             |
             ↓
     Pop second smallest
             |
             ↓
       Sum = first + second
             |
             ↓
       cost += Sum
             |
             ↓
       Push Sum back
             |
             ↓
          Repeat
             |
             ↓
        Return cost
```

### Key Operations

```python
heapq.heapify(pq)
```

Build the Min Heap.

```python
first = heapq.heappop(pq)
second = heapq.heappop(pq)
```

Get the two smallest ropes.

```python
total_sum = first + second
cost += total_sum
heapq.heappush(pq, total_sum)
```

Connect, record the cost, and reinsert the combined rope.

### Complexity

```text
Time  = O(n log n)
Space = O(n)
```

### Core Insight

> **Always connect the two smallest ropes first, add their sum to the total cost, and push the combined rope back into the Min Heap.**

---

# One-Line Pattern

> **Minimum Cost to Connect Ropes = Greedy + Min Heap + Repeatedly Merge the Two Smallest Values.**