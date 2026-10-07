# Find Median of a Binary Search Tree

## 1. Problem

Given the root of a **Binary Search Tree (BST)**, find the median of all the node values.

### Median

If the number of values is **odd**:

```text
Median = middle value
```

Example:

```text
[1, 2, 3, 4, 5]

Median = 3
```

If the number of values is **even**:

```text
Median = lower middle value
```

Example:

```text
[1, 2, 3, 4, 5, 6]

Median = 3
```

> This problem uses the BST property that **inorder traversal gives values in sorted order**.

---

# 2. Brute Force / Direct Approach

The straightforward approach is:

1. Perform inorder traversal.
2. Store all values in an array.
3. Find the middle element.

Because the tree is a BST:

```text
BST
 ↓
Inorder Traversal
 ↓
Sorted Array
```

Example:

```text
        4
       / \
      2   6
     / \ / \
    1  3 5  7
```

Inorder:

```text
[1, 2, 3, 4, 5, 6, 7]
```

Number of nodes:

```text
n = 7
```

Median:

```text
inorder[n // 2]
= inorder[3]
= 4
```

For an even number of nodes, this problem chooses the **lower middle element**.

Example:

```text
[1, 2, 3, 4, 5, 6]

n = 6

lower middle index = (n // 2) - 1
                  = 3 - 1
                  = 2

Median = 3
```

### Complexity

```text
Time:  O(n)
Space: O(n)
```

The array stores all `n` values.

---

# 3. Main Idea

The key observation is:

> **Inorder traversal of a BST produces values in sorted order.**

So instead of trying to calculate the median while traversing randomly, first obtain the sorted sequence.

```text
BST
 |
 | Inorder
 ↓
[sorted values]
 |
 | Find middle
 ↓
Median
```

---

# 4. Code

```python
class Solution:
    def solve(self, root, inorder):
        if root is None:
            return

        # Traverse left subtree
        self.solve(root.left, inorder)

        # Store current node
        inorder.append(root.data)

        # Traverse right subtree
        self.solve(root.right, inorder)

    def findMedian(self, root: 'Node') -> int:
        inorder = []

        # Get sorted values
        self.solve(root, inorder)

        n = len(inorder)

        # Empty tree
        if n == 0:
            return 0

        # Even number of nodes
        if n & 1 == 0:
            return inorder[(n // 2) - 1]

        # Odd number of nodes
        return inorder[n // 2]
```

---

# 5. Understanding the Inorder Traversal

The function:

```python
def solve(self, root, inorder):
    if root is None:
        return

    self.solve(root.left, inorder)
    inorder.append(root.data)
    self.solve(root.right, inorder)
```

follows:

```text
Left → Root → Right
```

For:

```text
        4
       / \
      2   6
     / \ / \
    1  3 5  7
```

Traversal:

```text
1 → 2 → 3 → 4 → 5 → 6 → 7
```

Therefore:

```python
inorder = [1, 2, 3, 4, 5, 6, 7]
```

This is exactly what we need to find the median.

---

# 6. Finding the Median

After traversal:

```python
n = len(inorder)
```

There are two cases.

## Case 1: Odd Number of Nodes

Suppose:

```text
inorder = [1, 2, 3, 4, 5]
n = 5
```

Middle index:

```text
n // 2
= 5 // 2
= 2
```

Therefore:

```python
inorder[2] = 3
```

So:

```python
return inorder[n // 2]
```

---

## Case 2: Even Number of Nodes

Suppose:

```text
inorder = [1, 2, 3, 4, 5, 6]
n = 6
```

The two middle positions are:

```text
index:   0  1  2  3  4  5
value:   1  2  3  4  5  6
                 ↑  ↑
```

The two middle values are:

```text
3 and 4
```

But this problem expects the **lower median**:

```text
3
```

Its index is:

```python
(n // 2) - 1
```

Therefore:

```python
return inorder[(n // 2) - 1]
```

---

# 7. Understanding `n & 1`

The code uses:

```python
if n & 1 == 0:
```

This checks whether `n` is even.

### Odd

```text
5 in binary = 101

101 & 001
    ↓
001

result = 1
```

So odd numbers give:

```python
n & 1 == 1
```

### Even

```text
6 in binary = 110

110 & 001
    ↓
000

result = 0
```

So:

```python
n & 1 == 0
```

means `n` is even.

You can also write the condition more explicitly as:

```python
if n % 2 == 0:
```

Both are valid.

---

# 8. Dry Run

Consider:

```text
        5
       / \
      3   7
     / \ / \
    2  4 6  8
```

### Step 1: Inorder

```text
[2, 3, 4, 5, 6, 7, 8]
```

### Step 2: Number of nodes

```text
n = 7
```

### Step 3: Odd

```text
7 & 1 = 1
```

So:

```python
inorder[n // 2]
```

becomes:

```python
inorder[7 // 2]
= inorder[3]
= 5
```

Answer:

```text
5
```

---

# 9. Even Example

Consider:

```text
        4
       / \
      2   6
     / \   \
    1   3   7
```

Inorder:

```text
[1, 2, 3, 4, 6, 7]
```

Number of nodes:

```text
n = 6
```

Since:

```text
6 is even
```

use:

```python
inorder[(n // 2) - 1]
```

Therefore:

```text
inorder[(6 // 2) - 1]
= inorder[2]
= 3
```

Answer:

```text
3
```

---

# 10. Why Does This Work?

A median is defined based on the **sorted order** of values.

For a general binary tree, inorder traversal does not necessarily give sorted values.

But for a BST:

```text
Left values < Root < Right values
```

Therefore:

```text
Inorder Traversal
       ↓
Sorted Values
       ↓
Median can be found by index
```

This is the main BST property being used.

---

# 11. Edge Cases

### Empty Tree

```text
root = None
```

Then:

```python
n = 0
```

The code returns:

```text
0
```

---

### One Node

```text
    10
```

Inorder:

```text
[10]
```

```text
n = 1
```

Median:

```text
inorder[1 // 2]
= inorder[0]
= 10
```

---

### Two Nodes

```text
[1, 2]
```

```text
n = 2
```

Lower median:

```text
inorder[(2 // 2) - 1]
= inorder[0]
= 1
```

---

# 12. Complexity

Let `n` be the number of nodes.

### Inorder Traversal

Every node is visited once:

```text
O(n)
```

### Finding Median

Accessing an array element:

```text
O(1)
```

Therefore:

```text
Total Time = O(n)
```

### Space

The inorder array stores every node:

```text
O(n)
```

Recursion also uses:

```text
O(h)
```

where `h` is the tree height.

But the array dominates:

```text
Overall Space = O(n)
```

---

# 13. Complexity Summary

| Operation | Complexity |
|---|---:|
| Inorder traversal | O(n) |
| Find median | O(1) |
| Total Time | O(n) |
| Inorder array | O(n) |
| Recursion stack | O(h) |
| Total Space | O(n) |

---

# 14. Common Mistakes

### Mistake 1: Using preorder or postorder

Do not use:

```text
Preorder → Root Left Right
Postorder → Left Right Root
```

They do not produce sorted values.

Use:

```text
Inorder → Left Root Right
```

---

### Mistake 2: Using `n // 2` for even `n`

For:

```text
[1, 2, 3, 4]
```

`n // 2` gives:

```text
4 // 2 = 2
```

which points to:

```text
4
```

But this problem wants the lower median:

```text
3
```

Therefore use:

```python
(n // 2) - 1
```

for even `n`.

---

### Mistake 3: Forgetting the empty tree

Always handle:

```python
if n == 0:
    return 0
```

---

### Mistake 4: Thinking median always means average

In many mathematical contexts, for an even number of values:

```text
median = (lower middle + upper middle) / 2
```

But this problem specifically expects the **lower middle value**.

So:

```text
[1, 2, 3, 4]

Expected = 2
```

not:

```text
(2 + 3) / 2 = 2.5
```

---

# 15. Pattern Recognition

When you see:

```text
BST
+
Sorted order needed
+
Find kth/middle/median value
```

think:

```text
Inorder Traversal
        ↓
Sorted Sequence
        ↓
Use Index
```

This same pattern appears in:

- Kth Smallest Element in BST
- Kth Largest Element in BST
- Minimum Difference in BST
- BST Median
- BST Two Sum
- BST Iterator

---

# 16. Revision Cheat Sheet

```text
BST
 ↓
Inorder Traversal
 ↓
Sorted Array
 ↓
Count n
 ↓
If n is odd:
    inorder[n // 2]

If n is even:
    inorder[(n // 2) - 1]
```

### Median rules

```text
Odd:
[1, 2, 3, 4, 5]
         ↑
        3

index = n // 2
```

```text
Even:
[1, 2, 3, 4, 5, 6]
      ↑
     3

index = (n // 2) - 1
```

### Complexity

```text
Time  = O(n)
Space = O(n)
```

### Core Insight

> **BST inorder traversal gives sorted values, so the median can be found directly from the middle index.**

---

# One-Line Pattern

> **BST Median = Inorder Traversal → Sorted Values → Pick the Middle (lower middle for even n).**