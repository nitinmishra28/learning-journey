# Maximum Depth of Binary Tree

## Problem

Given the root of a binary tree, return its **maximum depth**.

Maximum depth means:

> The number of nodes along the longest path from the root node down to the farthest leaf node.

### Example

```text
        3
       / \
      9   20
         /  \
        15   7
```

The longest path is:

```text
3 → 20 → 15
```

So:

```text
Maximum Depth = 3
```

---

# Pattern

```text
Binary Tree + Recursion + DFS
```

---

# Main Idea

For every node, we calculate:

```text
Maximum depth of left subtree
Maximum depth of right subtree
```

Then take the larger one and add `1` for the current node.

Formula:

```text
depth(root) =
1 + max(depth(root.left), depth(root.right))
```

---

# Base Case

If the tree is empty:

```python
if root is None:
    return 0
```

Why?

An empty tree has:

```text
0 nodes
```

So its depth is:

```text
0
```

This base case is important because recursion eventually reaches `None`.

---

# Recursive Case

For the current node:

```python
leftSubTree = self.maxDepth(root.left)
rightSubTree = self.maxDepth(root.right)
```

This recursively finds the depth of both subtrees.

Then:

```python
maxHeight = max(leftSubTree, rightSubTree)
```

We choose the deeper subtree.

Finally:

```python
totalHeight = maxHeight + 1
```

The `+1` is for the **current node**.

---

# Why `+1`?

Suppose a node has no children:

```text
    5
```

Both subtrees are empty:

```text
left  = 0
right = 0
```

So:

```text
max(0, 0) + 1 = 1
```

The node itself contributes one level.

For:

```text
    5
   /
  3
 /
1
```

At node `1`:

```text
0 + 1 = 1
```

At node `3`:

```text
1 + 1 = 2
```

At node `5`:

```text
2 + 1 = 3
```

Therefore:

```text
Depth = 3
```

---

# Code

```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # Empty tree
        if root is None:
            return 0

        # Find depth of left subtree
        leftSubTree = self.maxDepth(root.left)

        # Find depth of right subtree
        rightSubTree = self.maxDepth(root.right)

        # Take the deeper subtree
        maxHeight = max(leftSubTree, rightSubTree)

        # +1 for current node
        totalHeight = maxHeight + 1

        return totalHeight
```

---

# Dry Run

Consider:

```text
        1
       / \
      2   3
     /
    4
```

Start at:

```text
1
```

We recursively calculate:

```text
maxDepth(2)
maxDepth(3)
```

For node `2`:

```text
maxDepth(4)
```

For node `4`:

```text
left  = 0
right = 0

depth = max(0, 0) + 1
      = 1
```

Return:

```text
1
```

At node `2`:

```text
left  = 1
right = 0

depth = max(1, 0) + 1
      = 2
```

At node `3`:

```text
left  = 0
right = 0

depth = 1
```

Finally at node `1`:

```text
left  = 2
right = 1

depth = max(2, 1) + 1
      = 3
```

Answer:

```text
3
```

---

# How Recursion Thinks About the Problem

Don't try to calculate the entire tree at once.

For every node, simply ask:

```text
"What is the maximum depth of my left subtree?"

"What is the maximum depth of my right subtree?"
```

Then:

```text
My depth = deeper subtree + myself
```

So the recursive structure is:

```text
                Node
               /    \
              /      \
       left depth   right depth
              \      /
               \    /
             maximum
                +
               1
```

---

# Important Interview Point

This is a **post-order DFS idea**.

Why?

Because we need information from:

```text
left subtree
right subtree
```

before calculating the answer for:

```text
current node
```

The order is conceptually:

```text
Left → Right → Current
```

---

# Complexity

Every node is visited once.

```text
Time  → O(n)
```

Recursive calls use the tree height:

```text
Space → O(h)
```

Where:

```text
h = height of the tree
```

For a balanced tree:

```text
O(log n)
```

For a completely skewed tree:

```text
O(n)
```

---

# Common Mistakes

## 1. Forgetting the Base Case

You must handle:

```python
root is None
```

Otherwise recursion will not know when to stop.

---

## 2. Forgetting `+1`

The current node is also part of the depth.

Therefore:

```python
return max(left, right) + 1
```

---

## 3. Taking the Minimum

We need the **maximum** depth, so:

```python
max(leftSubTree, rightSubTree)
```

not:

```python
min(leftSubTree, rightSubTree)
```

---

# Revision Cheat Sheet

```text
Maximum Depth of Binary Tree

Pattern:
Binary Tree + Recursion + DFS

Base Case:

if root is None:
    return 0

Recursive Case:

left  = maxDepth(root.left)
right = maxDepth(root.right)

return max(left, right) + 1

Why +1?

Current node contributes one level.

Formula:

depth(root) =
1 + max(
    depth(root.left),
    depth(root.right)
)

Traversal idea:

Left → Right → Current

This is a post-order DFS idea.

Complexity:

Time  → O(n)
Space → O(h) (The auxiliary space is O(h) because of the recursion call stack, where h is the height of the tree.)

h = height of tree
```

---

# One-Line Pattern

```text
For every node, find the maximum depth of its left and right subtrees, take the larger one, and add 1 for the current node.
```