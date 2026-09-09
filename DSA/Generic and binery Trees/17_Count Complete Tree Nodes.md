# Count Complete Tree Nodes

## Problem

Given the root of a **complete binary tree**, return the total number of nodes in the tree.

A complete binary tree means:

```text
Every level is completely filled
except possibly the last level,

and the last level is filled from left to right.
```

Example:

```text
          1
        /   \
       2     3
      / \   /
     4   5 6
```

Number of nodes:

```text
6
```

---

# Brute Force

## Idea

The simplest solution is to traverse every node and count it.

We can use DFS:

```python
class Solution:
    def countNodes(self, root):
        if root is None:
            return 0

        left = self.countNodes(root.left)
        right = self.countNodes(root.right)

        return 1 + left + right
```

For every node:

```text
1 + nodes in left subtree + nodes in right subtree
```

We visit every node exactly once.

### Complexity

```text
Time  = O(n)
Space = O(h)
```

where:

- `n` = number of nodes
- `h` = height of tree

This works, but we can do better because the tree is **complete**.

---

# Pattern

```text
Complete Binary Tree
        ↓
Check left height
Check right height
        ↓
If equal
        ↓
Perfect Binary Tree
        ↓
Calculate directly

If not equal
        ↓
Recursively solve left + right
```

The important observation is:

> In a complete binary tree, if the leftmost height and rightmost height are equal, the entire tree is a perfect binary tree.

---

# Main Idea

For every subtree, calculate:

```text
left height
right height
```

If:

```python
lh == rh
```

then the subtree is a **perfect binary tree**.

A perfect binary tree looks like:

```text
          1
        /   \
       2     3
      / \   / \
     4   5 6   7
```

Every level is completely filled.

If height is:

```text
h
```

then number of nodes is:

```text
2^h - 1
```

Therefore:

```python
return (2 ** lh) - 1
```

We don't need to visit every node.

---

# Why Does `2^h - 1` Give the Number of Nodes?

Consider a perfect binary tree.

For height `1`:

```text
    1
```

Nodes:

```text
1
```

Formula:

```text
2^1 - 1 = 1
```

Height `2`:

```text
    1
   / \
  2   3
```

Nodes:

```text
3
```

Formula:

```text
2^2 - 1 = 3
```

Height `3`:

```text
        1
      /   \
     2     3
    / \   / \
   4   5 6   7
```

Nodes:

```text
7
```

Formula:

```text
2^3 - 1 = 7
```

In general:

```text
Level 1 → 1 node
Level 2 → 2 nodes
Level 3 → 4 nodes
Level 4 → 8 nodes
```

Total:

```text
1 + 2 + 4 + ... + 2^(h-1)

= 2^h - 1
```

---

# Why Are We Finding Left Height and Right Height?

Your code does:

```python
lh = self.findLeftHeight(root)
rh = self.findRightHeight(root)
```

The left height follows only:

```text
root
  ↓
left
  ↓
left
  ↓
left
```

The right height follows only:

```text
root
  ↓
right
  ↓
right
  ↓
right
```

For a perfect tree:

```text
        1
       / \
      2   3
     / \ / \
    4  5 6  7
```

Leftmost path:

```text
1 → 2 → 4
```

Height:

```text
3
```

Rightmost path:

```text
1 → 3 → 7
```

Height:

```text
3
```

Therefore:

```text
lh == rh
```

and we know the tree is perfect.

---

# Important Observation

For a **complete** binary tree:

```text
lh == rh
```

means:

```text
The tree is perfect.
```

But this is only safe because the problem guarantees a **complete binary tree**.

For a general binary tree, equal leftmost and rightmost heights do not necessarily prove that the tree is perfect.

---

# Example Where Heights Are Different

Consider:

```text
          1
        /   \
       2     3
      / \   /
     4   5 6
```

Leftmost path:

```text
1 → 2 → 4
```

So:

```text
lh = 3
```

Rightmost path:

```text
1 → 3
```

So:

```text
rh = 2
```

Therefore:

```text
lh != rh
```

We cannot directly calculate the number of nodes.

So we recursively count:

```python
lans = self.countNodes(root.left)
rans = self.countNodes(root.right)

return 1 + lans + rans
```

---

# Why Does Recursion Still Help?

Suppose:

```text
          1
        /   \
       2     3
      / \   /
     4   5 6
```

At root:

```text
lh = 3
rh = 2
```

So we recursively solve both subtrees.

Left subtree:

```text
      2
     / \
    4   5
```

Its heights are:

```text
lh = 2
rh = 2
```

Therefore it is perfect.

We immediately calculate:

```text
2^2 - 1 = 3
```

No need to visit:

```text
4
5
```

individually.

Right subtree:

```text
    3
   /
  6
```

Heights are different, so we continue recursively.

This is where the optimization comes from.

---

# Complete Code

```python
class Solution:

    def findLeftHeight(self, root):
        height = 0

        while root:
            height += 1
            root = root.left

        return height

    def findRightHeight(self, root):
        height = 0

        while root:
            height += 1
            root = root.right

        return height

    def countNodes(self, root):
        if root is None:
            return 0

        # Find height of leftmost path
        lh = self.findLeftHeight(root)

        # Find height of rightmost path
        rh = self.findRightHeight(root)

        # If both heights are equal,
        # this subtree is a perfect binary tree
        if lh == rh:
            return (2 ** lh) - 1

        # Otherwise recursively count
        # nodes in both subtrees
        lans = self.countNodes(root.left)
        rans = self.countNodes(root.right)

        return 1 + lans + rans
```

---

# Dry Run

Consider:

```text
          1
        /   \
       2     3
      / \   /
     4   5 6
```

We have:

```text
n = 6
```

## Step 1 — Root `1`

Leftmost path:

```text
1 → 2 → 4
```

So:

```text
lh = 3
```

Rightmost path:

```text
1 → 3
```

So:

```text
rh = 2
```

Therefore:

```text
lh != rh
```

We cannot directly calculate.

So:

```python
lans = countNodes(2)
rans = countNodes(3)
```

---

## Step 2 — Left Subtree

```text
      2
     / \
    4   5
```

Leftmost:

```text
2 → 4
```

```text
lh = 2
```

Rightmost:

```text
2 → 5
```

```text
rh = 2
```

Therefore:

```text
lh == rh
```

This subtree is perfect.

Calculate:

```text
2^2 - 1
= 4 - 1
= 3
```

So:

```text
lans = 3
```

---

## Step 3 — Right Subtree

```text
    3
   /
  6
```

Leftmost:

```text
3 → 6
```

```text
lh = 2
```

Rightmost:

```text
3
```

```text
rh = 1
```

Therefore:

```text
lh != rh
```

Continue recursively.

Node `6`:

```text
lh = 1
rh = 1
```

So:

```text
2^1 - 1 = 1
```

Therefore:

```text
rans = 1 + 1 = 2
```

---

## Step 4 — Root Result

Now:

```text
lans = 3
rans = 2
```

Root itself contributes:

```text
1
```

Therefore:

```text
1 + 3 + 2
= 6
```

Answer:

```text
6
```

---

# Complexity

Let:

```text
n = number of nodes
h = height of tree
```

At every recursive call, we calculate:

```text
left height → O(h)
right height → O(h)
```

But because the tree is complete, we don't visit all nodes individually.

The optimized complexity is:

```text
Time = O((log n)^2)
```

Why?

The tree height is:

```text
h = O(log n)
```

and at each recursion level we spend:

```text
O(log n)
```

finding the leftmost and rightmost heights.

The recursion itself has approximately:

```text
O(log n)
```

levels.

Therefore:

```text
O(log n × log n)
= O((log n)^2)
```

### Space

The recursion depth is the height:

```text
O(log n)
```

So:

```text
Space = O(log n)
```

---

# Complexity Comparison

| Approach | Time | Space |
|---|---:|---:|
| Brute Force DFS | O(n) | O(h) |
| Complete Tree Optimization | O((log n)²) | O(log n) |

For a complete binary tree:

```text
h = log n
```

so the optimized solution is significantly faster than visiting all `n` nodes.

---

# Common Mistakes

## 1. Using This Trick for Any Binary Tree

This optimization depends on:

```text
Complete Binary Tree
```

Do not assume:

```python
lh == rh
```

means perfect for an arbitrary binary tree.

---

## 2. Confusing Height With Number of Nodes

If:

```text
lh = 3
```

you cannot say there are `3` nodes.

It means there are `3` nodes along the leftmost path.

For a perfect tree:

```text
number of nodes = 2^h - 1
```

---

## 3. Forgetting the `-1`

Wrong:

```python
2 ** lh
```

Correct:

```python
(2 ** lh) - 1
```

Because:

```text
1 + 2 + 4 + ... + 2^(h-1)
= 2^h - 1
```

---

## 4. Using `2 ** lh` Without Understanding `h`

If:

```text
lh = 4
```

the tree has levels:

```text
1
2
4
8
```

Total:

```text
1 + 2 + 4 + 8 = 15
```

And:

```text
2^4 - 1 = 15
```

---

# Pattern Recognition

When the problem says:

> Count nodes in a **complete binary tree**

Immediately think:

```text
Complete Binary Tree
        ↓
Find leftmost height
Find rightmost height
        ↓
lh == rh ?
   /          \
 YES           NO
  ↓             ↓
Perfect       Recurse
 Tree        left + right
  ↓
2^h - 1
```

### Shortcut

```text
Complete Tree
    ↓
Left Height + Right Height
    ↓
Equal?
    ↓
Perfect Tree
    ↓
2^h - 1
```

---

# Connection With Perfect Binary Tree

Remember:

### Perfect Binary Tree

Every level is completely filled.

```text
        1
      /   \
     2     3
    / \   / \
   4   5 6   7
```

Number of nodes:

```text
2^h - 1
```

### Complete Binary Tree

All levels are full except possibly the last, and the last level is filled left-to-right.

```text
        1
      /   \
     2     3
    / \   /
   4   5 6
```

The optimization works by repeatedly finding **perfect subtrees inside the complete tree**.

---

# Revision Cheat Sheet

```text
Problem:
Count nodes in a complete binary tree.

Brute Force:
DFS every node.

Time:
O(n)

Optimized:
1. Find leftmost height.
2. Find rightmost height.
3. If equal:
      subtree is perfect
      return 2^h - 1
4. Otherwise:
      recursively count left + right.

Perfect Tree:
nodes = 2^h - 1

Why?
Levels contain:
1 + 2 + 4 + ... + 2^(h-1)

Pattern:
Complete Tree → Height Comparison → Perfect Subtree

Optimized Time:
O((log n)^2)

Space:
O(log n)
```

# One-Line Pattern

> **In a complete binary tree, equal leftmost and rightmost heights mean the subtree is perfect, so count it directly using `2^h - 1`; otherwise recurse.**