# Merge Two Max Heaps

## 1. Problem

You are given two Max Heaps, `firstHeap` and `secondHeap`, containing `n` and `m` elements respectively.

Merge both heaps into a single **Max Heap** and return the resulting array.

A Max Heap must satisfy two properties:

1. **Complete Binary Tree:** All levels are full except possibly the last, which is filled from left to right.
2. **Max Heap Property:** Every parent node is greater than or equal to its children.

### Example

```python
firstHeap = [10, 5, 6, 2]
secondHeap = [12, 7, 9]

Output = [12, 10, 9, 2, 5, 7, 6]
```

The exact output array may differ, provided it represents a valid Max Heap containing all the elements from both input heaps.

---

## 2. Brute Force Approach

### Idea

1. Merge both arrays.
2. Sort the merged array in descending order.
3. Return the result.

Since every parent in a descending array is greater than or equal to the elements appearing after it, the resulting array satisfies the Max Heap property. It also represents a complete binary tree.

### Code

```python
class Solution:
    def mergeHeaps(self, firstHeap, secondHeap, n, m):
        mergedHeap = firstHeap + secondHeap
        mergedHeap.sort(reverse=True)

        return mergedHeap
```

### Complexity

Let `N = n + m`.

- Merging arrays: `O(N)`
- Sorting: `O(N log N)`
- **Total time:** `O(N log N)`
- **Auxiliary space:** Depends on the sorting implementation; Python's sorting may use `O(N)` temporary space.

### Why Is It Less Efficient?

Sorting is unnecessary. We only need to satisfy the Max Heap property, not completely sort the elements.

**Optimization:** Merge the arrays and use bottom-up heapification.

---

## 3. Pattern: Merge Arrays + Bottom-Up Heapify

The key idea is that both input arrays are already Max Heaps, but simply concatenating them does **not** guarantee that the resulting array is a Max Heap.

We must rebuild the heap property after merging.

```text
First Max Heap       Second Max Heap
      |                    |
      +---------+----------+
                |
                v
       Concatenate Arrays
                |
                v
        Merged Array
                |
                v
    Bottom-Up Heapification
                |
                v
          Final Max Heap
```

The important observation is that **all leaf nodes are already valid heaps** because they have no children.

Therefore, we start heapifying from the last non-leaf node and move backward to the root.

---

## 4. Main Idea

### Step 1: Merge the arrays

```python
mergedHeap = firstHeap + secondHeap
heapSize = len(mergedHeap)
```

This creates a new array containing all elements from both heaps.

For example:

```python
firstHeap = [10, 5, 6, 2]
secondHeap = [12, 7, 9]

mergedHeap = [10, 5, 6, 2, 12, 7, 9]
```

The array contains every element, but it may violate the Max Heap property.

For example, the root `10` is smaller than its right child `12`.

### Step 2: Calculate the children of a node

For a zero-indexed heap array, the child indices of a parent at index `i` are:

```python
leftChildIndex = 2 * i + 1
rightChildIndex = 2 * i + 2
```

The parent index of a node at index `i` is:

```python
parentIndex = (i - 1) // 2
```

These formulas allow us to navigate the heap without explicitly creating tree nodes.

### Step 3: Find the last non-leaf node

```python
for parentIndex in range(heapSize // 2 - 1, -1, -1):
```

The last non-leaf node is at index:

```python
heapSize // 2 - 1
```

Why?

In a zero-indexed binary heap, nodes from index `heapSize // 2` onward are leaf nodes.

Leaf nodes don't need heapification because they have no children.

Therefore, we begin with the last non-leaf node and move toward index `0`.

### Step 4: Heapify each subtree

For each node:

1. Assume the parent is the largest.
2. Compare it with its left child.
3. Compare it with its right child.
4. Identify the largest among the parent and its children.
5. Swap the parent with the largest child if necessary.
6. Recursively heapify the affected subtree.

After processing every non-leaf node from right to left, the entire array becomes a valid Max Heap.

---

## 5. Complete Code with Comments

```python
class Solution:
    def mergeHeaps(self, firstHeap, secondHeap, n, m):

        # Step 1: Merge both heaps into one array
        mergedHeap = firstHeap + secondHeap
        heapSize = len(mergedHeap)

        # Heapify the subtree rooted at parentIndex
        def heapify(heap, size, parentIndex):

            # Initially assume the parent is the largest
            largestIndex = parentIndex

            # Calculate child indices
            leftChildIndex = 2 * parentIndex + 1
            rightChildIndex = 2 * parentIndex + 2

            # Compare parent with left child
            if (leftChildIndex < size and
                    heap[leftChildIndex] > heap[largestIndex]):
                largestIndex = leftChildIndex

            # Compare the current largest with right child
            if (rightChildIndex < size and
                    heap[rightChildIndex] > heap[largestIndex]):
                largestIndex = rightChildIndex

            # If a child is larger, swap and fix that subtree
            if largestIndex != parentIndex:

                heap[parentIndex], heap[largestIndex] = (
                    heap[largestIndex],
                    heap[parentIndex]
                )

                # Continue heapifying the affected subtree
                heapify(heap, size, largestIndex)

        # Step 2: Start from the last non-leaf node
        for parentIndex in range(heapSize // 2 - 1, -1, -1):

            # Restore the Max Heap property
            heapify(mergedHeap, heapSize, parentIndex)

        # Step 3: Return the merged Max Heap
        return mergedHeap
```

---

## 6. Dry Run

Consider:

```python
firstHeap = [10, 5, 6, 2]
secondHeap = [12, 7, 9]
```

### Step 1: Concatenate both heaps

```text
Index:       0   1   2   3   4   5   6
Merged:     [10,  5,  6,  2, 12,  7,  9]
```

The merged array is not a valid Max Heap because the value `12` is a child of `5`, but `12 > 5`.

### Step 2: Find the last non-leaf node

```python
heapSize = 7

lastNonLeaf = heapSize // 2 - 1
            = 7 // 2 - 1
            = 2
```

We heapify indices:

```text
2 → 1 → 0
```

### Step 3: Heapify index 2

```text
          6
         / \
        7   9
```

The largest value is `9`.

Swap `6` and `9`:

```text
          9
         / \
        7   6
```

Array:

```python
[10, 5, 9, 2, 12, 7, 6]
```

### Step 4: Heapify index 1

The subtree is:

```text
          5
         / \
        2   12
```

The largest value is `12`.

Swap `5` and `12`:

```text
          12
         /  \
        2    5
```

Array:

```python
[10, 12, 9, 2, 5, 7, 6]
```

### Step 5: Heapify index 0

The root is `10`, and its children are `12` and `9`.

The largest value is `12`, so swap `10` and `12`:

```text
          12
         /  \
       10    9
      / \   / \
     2   5 7   6
```

Array:

```python
[12, 10, 9, 2, 5, 7, 6]
```

The root is now the largest value, and the Max Heap property holds throughout the tree.

**Final output:**

```python
[12, 10, 9, 2, 5, 7, 6]
```

---

## 7. Why Do We Heapify from Bottom to Top?

This is the most important part of bottom-up heapification.

When we heapify a parent, we assume that its left and right subtrees are already valid Max Heaps.

Starting from the last non-leaf node ensures this assumption holds.

```text
          0
        /   \
       1     2
      / \   / \
     3   4 5   6
```

The processing order is:

```text
Index 2 → Fix subtree rooted at 2
Index 1 → Fix subtree rooted at 1
Index 0 → Fix the entire heap
```

- Nodes `3`, `4`, `5`, and `6` are leaves, so they are already valid heaps.
- Index `2` is fixed first.
- Index `1` is fixed next.
- Index `0` is fixed last, after its child subtrees have been processed.

**Remember:** Heapify moves from the last non-leaf node toward the root because the parent depends on its child subtrees being valid heaps.

---

## 8. Complexity Analysis

Let `N = n + m`.

### Time Complexity

- Concatenating the arrays: `O(N)`
- Bottom-up heapification: `O(N)`

Although a single `heapify()` call can take `O(log N)`, not every node travels through the entire tree. Most nodes are near the leaves, so bottom-up heapification takes linear time overall.

**Total time complexity: `O(n + m)`**

### Space Complexity

- The merged array requires `O(N)` space.
- Recursive `heapify()` uses `O(log N)` stack space in the worst case.

**Total auxiliary space:** `O(N)` including the merged array, or `O(log N)` for the recursive call stack alone, excluding the output array.

---

## 9. Common Mistakes

1. **Only concatenating the arrays:** Both inputs being Max Heaps does not mean their concatenation is a Max Heap.
2. **Starting heapification at the root:** Bottom-up heapification must begin at the last non-leaf node.
3. **Using incorrect child indices:** For zero-indexed heaps, use `2 * i + 1` and `2 * i + 2`.
4. **Forgetting the bounds checks:** A child index must be less than `size` before accessing the array.
5. **Comparing only the parent with the left child:** You must also compare with the right child.
6. **Recursing at the wrong index:** After swapping, recursively heapify the subtree rooted at `largestIndex`.
7. **Assuming the output must be fully sorted:** A Max Heap only guarantees that every parent is at least as large as its children.

---

## 10. Brute Force vs Optimized Approach

| Feature | Sort in Descending Order | Bottom-Up Heapify |
|---|---|---|
| Merge arrays | `O(n + m)` | `O(n + m)` |
| Restore Max Heap property | Sort entire array | Heapify from bottom to top |
| Total time | `O(N log N)` | `O(N)` |
| Output | Valid Max Heap | Valid Max Heap |
| Best choice | Simple baseline | Efficient solution |

Here, `N = n + m`.

---

## 11. Pattern Recognition

Recognize **Bottom-Up Heapification** when:

- You already have all the elements in an array.
- You need to construct or restore a heap.
- Repeatedly inserting every element would cost `O(N log N)`.
- You can start from the last non-leaf node and process toward the root.

The same technique is used to build a heap from an unsorted array.

---

## 12. Revision Cheat Sheet

- **Merge:** `firstHeap + secondHeap`
- **Left child:** `2 * i + 1`
- **Right child:** `2 * i + 2`
- **Last non-leaf:** `heapSize // 2 - 1`
- **Max Heap rule:** Parent must be greater than or equal to both children.
- **Heapify:** Find the largest of parent and children, swap if necessary, then recurse.
- **Processing order:** Last non-leaf node to root.
- **Time:** `O(n + m)`
- **Auxiliary space:** `O(n + m)` including the merged array; recursive stack is `O(log(n + m))`.

> **One-Line Pattern:** Merge Two Max Heaps = Concatenate Arrays + Bottom-Up Heapify from the Last Non-Leaf Node to the Root.