# Check Completeness of a Binary Tree

## 1. Problem

Given the root of a binary tree, determine whether it is a **Complete Binary Tree**.

A binary tree is complete if:

1. Every level, except possibly the last, is completely filled.
2. In the last level, all nodes are as far left as possible.

### Example 1: Complete Binary Tree

```text
        1
       / \
      2   3
     / \  /
    4  5 6
```

This tree is complete because the last level is filled from left to right without gaps.

Answer:

```text
True
```

### Example 2: Not a Complete Binary Tree

```text
        1
       / \
      2   3
       \   \
        5   7
```

There are missing positions before existing nodes in the last level.

Answer:

```text
False
```

---

# 2. Brute Force Approach

A simple way to check completeness is to perform a level-order traversal and examine the positions of the nodes.

Using a queue:

1. Traverse the tree level by level.
2. Add both children of every non-null node to the queue, including missing children (`None`).
3. Once a `None` is encountered, every subsequent queue entry must also be `None`.
4. If a non-null node appears after a `None`, the tree is not complete.

This is the approach used by the given solution.

The algorithm is already efficient, so there is no need for a separate, slower brute-force implementation.

---

# 3. Main Idea: Level Order + Null Detection

The key observation is:

> **In a complete binary tree, once a missing child position is encountered during level-order traversal, no actual node can appear afterward.**

Consider:

```text
        1
       / \
      2   3
     / \  /
    4  5 6
```

The level-order traversal must include missing child positions.

Conceptually, the queue processes:

```text
1, 2, 3, 4, 5, 6, None, None, ...
```

Once `None` appears, all remaining entries must be `None`.

If a real node appears after `None`, there is a gap before that node, so the tree is not complete.

---

# 4. Code

```python
from collections import deque

class Solution:
    def solve(self, root):
        q = deque([root])
        nullFound = False

        while q:
            front = q.popleft()

            if front is None:
                nullFound = True

            else:
                # A real node appeared after a missing position
                if nullFound:
                    return False

                # Add both children, even if they are None
                q.append(front.left)
                q.append(front.right)

        return True

    def isCompleteTree(self, root: TreeNode | None) -> bool:
        ans = self.solve(root)
        return ans
```

---

# 5. Understanding the Queue

```python
q = deque([root])
```

We start with the root.

Why use a queue?

A queue follows FIFO:

```text
First In → First Out
```

This allows us to process nodes level by level.

For example:

```text
        1
       / \
      2   3
     / \
    4   5
```

The queue processes nodes in this order:

```text
1 → 2 → 3 → 4 → 5
```

This is called **level-order traversal**, or BFS.

---

# 6. Why Add `None` Children?

This is the most important part of the solution:

```python
q.append(front.left)
q.append(front.right)
```

We append both children even when a child is missing.

Consider:

```text
        1
       / \
      2   3
       \   \
        5   7
```

Node `2` has a missing left child but an existing right child.

Its child positions are:

```text
Left  = None
Right = 5
```

The queue encounters the missing position before the real node `5`.

That violates completeness.

If we skipped `None` children, we would lose information about the gaps and could incorrectly accept an incomplete tree.

---

# 7. Understanding `nullFound`

```python
nullFound = False
```

This variable records whether a missing position has been encountered.

There are two cases.

### Case 1: Current node is `None`

```python
if front is None:
    nullFound = True
```

We have encountered an empty position.

From now on, every subsequent queue entry must also be `None`.

### Case 2: Current node is not `None`

```python
else:
    if nullFound:
        return False
```

If a real node appears after a missing position, the tree is not complete.

Otherwise, add its children to the queue:

```python
q.append(front.left)
q.append(front.right)
```

If the queue finishes without finding a real node after a `None`, the tree is complete.

---

# 8. Dry Run: Complete Binary Tree

Consider:

```text
        1
       / \
      2   3
     / \  /
    4  5 6
```

### Initial state

```text
Queue = [1]
nullFound = False
```

### Step 1: Process `1`

```text
Queue = [2, 3]
nullFound = False
```

### Step 2: Process `2`

```text
Queue = [3, 4, 5]
nullFound = False
```

### Step 3: Process `3`

```text
Queue = [4, 5, 6, None]
nullFound = False
```

### Step 4: Process `4`

```text
Queue = [5, 6, None, None, None]
nullFound = False
```

### Step 5: Process `5`

```text
Queue = [6, None, None, None, None, None]
nullFound = False
```

### Step 6: Process `6`

```text
Queue = [None, None, None, None, None, None, None]
nullFound = False
```

### Step 7: Process `None`

```text
nullFound = True
```

All remaining entries are `None`.

No real node appears after the missing position.

Answer:

```text
True
```

---

# 9. Dry Run: Incomplete Binary Tree

Consider:

```text
        1
       / \
      2   3
       \   \
        5   7
```

### Step 1: Process `1`

```text
Queue = [2, 3]
nullFound = False
```

### Step 2: Process `2`

Node `2` has:

```text
left = None
right = 5
```

After adding its children:

```text
Queue = [3, None, 5]
nullFound = False
```

### Step 3: Process `3`

Node `3` has:

```text
left = None
right = 7
```

Queue becomes:

```text
[None, 5, None, 7]
```

### Step 4: Process `None`

```text
nullFound = True
```

### Step 5: Process `5`

```python
if nullFound:
    return False
```

A real node appeared after a missing position.

Answer:

```text
False
```

---

# 10. Why Does This Work?

A complete binary tree has no gaps before existing nodes in its level-order sequence.

Conceptually, its positions look like:

```text
[Node, Node, Node, Node, Node, None, None, ...]
```

An incomplete tree may look like:

```text
[Node, Node, None, Node, ...]
```

The second sequence contains a real node after a missing position.

Therefore, the rule is:

```text
Before first None:
    Real nodes are allowed.

After first None:
    Only None values are allowed.
```

This is exactly what `nullFound` checks.

---

# 11. Complexity

Let `n` be the number of nodes.

### Time Complexity

Each real node is processed once.

Each real node adds two child positions to the queue. Therefore, the number of queue operations is proportional to the number of nodes.

```text
Time = O(n)
```

### Space Complexity

The queue stores nodes and missing child positions.

At most, the queue contains a number of entries proportional to the tree's width.

The maximum width of a binary tree is `O(n)`.

```text
Space = O(n)
```

---

# 12. Common Mistakes

### Mistake 1: Not adding `None` children

Incorrect:

```python
if front.left:
    q.append(front.left)

if front.right:
    q.append(front.right)
```

This skips missing positions, so the algorithm cannot detect gaps correctly.

Correct:

```python
q.append(front.left)
q.append(front.right)
```

### Mistake 2: Resetting `nullFound`

Once a missing position is encountered, `nullFound` must remain `True`.

Do not reset it when processing another node.

### Mistake 3: Returning `True` immediately after encountering `None`

A `None` alone does not mean the tree is incomplete.

For example:

```text
        1
       / \
      2   3
```

Missing child positions are expected in a complete tree.

The problem occurs only when a real node appears after a missing position.

### Mistake 4: Confusing Complete and Full Binary Trees

**Complete Binary Tree:**
- All levels except possibly the last are full.
- The last level is filled from left to right.

**Full Binary Tree:**
- Every node has either zero or two children.

These are different properties.

---

# 13. Complexity Summary

| Property | Complexity |
|---|---:|
| Time | O(n) |
| Auxiliary space | O(n) |
| Traversal | Level-order BFS |
| Data structure | Queue |
| Key variable | `nullFound` |

---

# 14. Revision Cheat Sheet

```text
Check Complete Binary Tree
          |
          ↓
    Level Order BFS
          |
          ↓
Add BOTH children, including None
          |
          ↓
Encounter None?
          |
          └── Yes → nullFound = True
                         |
                         ↓
              Real node appears later?
                    /          \
                  Yes           No
                   |             |
                Return False   Continue
                                 |
                                 ↓
                            Return True
```

### Core Rules

```python
if front is None:
    nullFound = True
```

```python
elif nullFound:
    return False
```

```python
q.append(front.left)
q.append(front.right)
```

### Complexity

```text
Time  = O(n)
Space = O(n)
```

---

# One-Line Pattern

> **Complete Binary Tree = Level-Order Traversal + Include Null Children + No Real Node After the First Null.**