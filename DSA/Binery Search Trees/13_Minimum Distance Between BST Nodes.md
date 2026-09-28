# Minimum Distance Between BST Nodes

## 1. Problem

Given the root of a **Binary Search Tree (BST)**, find the minimum difference between the values of any two different nodes.

### Example

```text
        4
       / \
      2   6
     / \
    1   3
```

Inorder traversal:

```text
1 → 2 → 3 → 4 → 6
```

Differences between consecutive values:

```text
2 - 1 = 1
3 - 2 = 1
4 - 3 = 1
6 - 4 = 2
```

Therefore:

```text
Minimum Difference = 1
```

---

# 2. Important BST Property

The most important observation is:

> **Inorder traversal of a BST gives values in sorted order.**

For:

```text
        4
       / \
      2   6
     / \
    1   3
```

Inorder:

```text
1 → 2 → 3 → 4 → 6
```

Because the values are sorted, the minimum difference can only occur between **adjacent values**.

So instead of comparing every pair:

```text
1 with 2, 3, 4, 6
2 with 3, 4, 6
...
```

we only need:

```text
current value - previous value
```

during inorder traversal.

---

# 3. Brute Force

## Idea

First store all BST values using inorder traversal.

Because inorder gives sorted values:

```text
[1, 2, 3, 4, 6]
```

Then compare every pair and find the minimum difference.

```python
minimum = float('inf')

for i in range(n):
    for j in range(i + 1, n):
        minimum = min(
            minimum,
            inorder[j] - inorder[i]
        )
```

### Complexity

```text
Inorder traversal: O(n)

Compare every pair: O(n²)

Total:
O(n²)
```

Extra array:

```text
O(n)
```

So:

```text
Time  = O(n²)
Space = O(n)
```

But because the array is already sorted, we don't need to compare every pair.

---

# 4. Optimized Approach

We can calculate the minimum difference **while performing inorder traversal**.

Maintain two variables:

```text
prevVal
minVal
```

Where:

```text
prevVal = previous node's value in inorder

minVal = minimum difference found so far
```

During inorder:

```text
Left → Node → Right
```

the values are sorted.

Therefore, when visiting the current node:

```text
current value
     -
previous value
```

gives the difference with the closest previous value.

---

# 5. Main Idea

Suppose inorder traversal gives:

```text
1 → 2 → 3 → 4 → 6
```

Maintain:

```text
prevVal = None
minVal = infinity
```

### Visit 1

There is no previous value.

```text
prevVal = 1
```

### Visit 2

```text
2 - 1 = 1
```

Update:

```text
minVal = 1
prevVal = 2
```

### Visit 3

```text
3 - 2 = 1
```

```text
minVal = 1
prevVal = 3
```

### Visit 4

```text
4 - 3 = 1
```

### Visit 6

```text
6 - 4 = 2
```

Final:

```text
minVal = 1
```

---

# 6. Complete Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        self.minVal = float('inf')
        self.prevVal = None

    def solve(self, root):

        if root is None:
            return

        # LNR
        # L
        self.solve(root.left)

        # N
        if self.prevVal is not None:
            self.minVal = min(
                self.minVal,
                root.val - self.prevVal
            )

        self.prevVal = root.val

        # R
        self.solve(root.right)

        return self.minVal

    def minDiffInBST(
        self,
        root: TreeNode | None
    ) -> int:

        self.solve(root)

        return self.minVal
```

---

# 7. Why Do We Only Compare With `prevVal`?

This is the key observation.

In sorted order:

```text
a < b < c < d
```

For example:

```text
1, 4, 7, 10
```

Differences:

```text
4 - 1 = 3
7 - 1 = 6
10 - 1 = 9
7 - 4 = 3
10 - 4 = 6
10 - 7 = 3
```

The minimum difference will always occur between adjacent sorted values:

```text
1 → 4 → 7 → 10
    ↑
adjacent
```

because if:

```text
a < b < c
```

then:

```text
c - a
```

is always greater than:

```text
b - a
```

and:

```text
c - b
```

Therefore:

```text
Only compare current node with previous inorder node.
```

---

# 8. Why Is `prevVal` Initially `None`?

For the first node visited in inorder, there is no previous node.

Example:

```text
Inorder:

1 → 2 → 3
```

When visiting `1`:

```text
prevVal = None
```

We cannot calculate:

```text
1 - None
```

Therefore:

```python
if self.prevVal is not None:
```

checks whether a previous value exists.

After processing the first node:

```python
self.prevVal = root.val
```

Now the next node can calculate a difference.

---

# 9. Why Update `prevVal` After Calculating Difference?

The order is important.

Correct:

```python
if self.prevVal is not None:
    self.minVal = min(
        self.minVal,
        root.val - self.prevVal
    )

self.prevVal = root.val
```

Suppose:

```text
prevVal = 2
root.val = 3
```

First calculate:

```text
3 - 2 = 1
```

Then:

```text
prevVal = 3
```

So the next node can compare against `3`.

If we updated `prevVal` first:

```python
self.prevVal = root.val
```

then:

```text
root.val - prevVal
```

would become:

```text
3 - 3 = 0
```

which is incorrect because we would be comparing the node with itself.

---

# 10. Why Use Inorder?

The solution depends completely on this property:

```text
BST
 ↓
Inorder
 ↓
Sorted Order
```

Without sorted order, comparing only with the previous node would not be enough.

For a normal Binary Tree:

```text
Inorder is NOT necessarily sorted.
```

So this technique specifically works because the input is a BST.

---

# 11. Dry Run

Consider:

```text
        10
       /  \
      5    15
     / \   / \
    2   7 12 20
```

Inorder:

```text
2 → 5 → 7 → 10 → 12 → 15 → 20
```

Initial:

```text
prevVal = None
minVal = ∞
```

### Visit 2

```text
prevVal = None
```

No comparison.

```text
prevVal = 2
```

---

### Visit 5

```text
5 - 2 = 3
```

```text
minVal = 3
prevVal = 5
```

---

### Visit 7

```text
7 - 5 = 2
```

```text
minVal = 2
prevVal = 7
```

---

### Visit 10

```text
10 - 7 = 3
```

```text
minVal = 2
prevVal = 10
```

---

### Visit 12

```text
12 - 10 = 2
```

```text
minVal = 2
prevVal = 12
```

---

### Visit 15

```text
15 - 12 = 3
```

---

### Visit 20

```text
20 - 15 = 5
```

Final:

```text
minVal = 2
```

---

# 12. Recursion Flow

The traversal is:

```text
        Root
       /    \
      L      R
```

Using:

```text
LNR
```

we do:

```text
solve(left)
     ↓
process current node
     ↓
solve(right)
```

At the `Node` step:

```python
if self.prevVal is not None:
    self.minVal = min(
        self.minVal,
        root.val - self.prevVal
    )

self.prevVal = root.val
```

This means the comparison happens exactly in sorted order.

---

# 13. Why `minVal` and `prevVal` Are Instance Variables

They need to be shared between recursive calls.

If we declared:

```python
prevVal = None
```

inside `solve()` every recursive call could have its own local variable.

Instead:

```python
self.prevVal
```

is shared across all recursive calls.

Similarly:

```python
self.minVal
```

stores the minimum found anywhere in the tree.

Think:

```text
self.prevVal
     ↓
shared previous value

self.minVal
     ↓
shared minimum answer
```

---

# 14. Complexity

Every node is visited exactly once.

At each node we perform constant work:

```text
Calculate difference
Update minimum
Update previous value
```

Therefore:

```text
Time = O(n)
```

The recursion stack depends on tree height:

```text
Space = O(h)
```

For a balanced BST:

```text
O(h) = O(log n)
```

For a skewed BST:

```text
O(h) = O(n)
```

No array is required.

---

# 15. Brute Force vs Optimized

| Approach | Idea | Time | Space |
|---|---|---:|---:|
| Brute Force | Store values and compare every pair | O(n²) | O(n) |
| Optimized | Inorder + previous value | O(n) | O(h) |

The optimized approach is better because:

```text
BST
 ↓
Inorder
 ↓
Sorted Order
 ↓
Only adjacent values matter
```

---

# 16. Common Mistakes

## 1. Comparing every pair

This works but is unnecessary.

Instead of:

```text
every pair
```

use:

```text
current - previous
```

because inorder is sorted.

---

## 2. Forgetting the first node

The first inorder node has no previous value.

Use:

```python
if self.prevVal is not None:
```

---

## 3. Updating `prevVal` too early

Wrong:

```python
self.prevVal = root.val

self.minVal = min(
    self.minVal,
    root.val - self.prevVal
)
```

This compares the node with itself.

Correct:

```python
if self.prevVal is not None:
    self.minVal = min(
        self.minVal,
        root.val - self.prevVal
    )

self.prevVal = root.val
```

---

## 4. Using normal Binary Tree logic

You cannot use this optimization on an arbitrary Binary Tree.

It depends on:

```text
BST Inorder = Sorted
```

---

## 5. Forgetting to initialize `minVal`

Use:

```python
self.minVal = float('inf')
```

because we are looking for the minimum difference.

---

# 17. Pattern Recognition

When you see:

```text
BST
+
Minimum Difference
```

think:

```text
BST
 ↓
Inorder
 ↓
Sorted Values
 ↓
Compare Current With Previous
 ↓
Track Minimum
```

The core pattern is:

> **In a sorted sequence, the minimum difference is always between adjacent elements.**

And:

```text
BST Inorder = Sorted Sequence
```

Therefore:

```text
Inorder + Previous Value
```

is enough.

---

# 18. Similar Problems

This pattern is useful for other BST problems involving sorted order.

```text
Kth Smallest
     ↓
Inorder + Count

Minimum Difference
     ↓
Inorder + Previous

Two Sum in BST
     ↓
Inorder + Two Pointers

BST to Greater Sum Tree
     ↓
Reverse Inorder + Running Sum
```

The common idea is:

```text
Use BST property through inorder traversal.
```

---

# 19. Revision Cheat Sheet

```text
Minimum Difference in BST

Key Property:
BST Inorder = Sorted Order

Maintain:

prevVal = previous inorder value
minVal  = minimum difference

At every node:

if prevVal exists:
    diff = root.val - prevVal
    minVal = min(minVal, diff)

prevVal = root.val
```

### Traversal

```text
L → N → R
```

### Complexity

```text
Time  = O(n)
Space = O(h)
```

### Why only previous?

```text
Inorder is sorted
      ↓
Minimum difference
      ↓
Always between adjacent values
      ↓
Current - Previous
```

> **One-Line Pattern: Minimum Difference in BST = Inorder Traversal + Previous Value + Minimum of Adjacent Differences.**  