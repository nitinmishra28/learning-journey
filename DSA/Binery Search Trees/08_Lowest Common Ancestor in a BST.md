# Lowest Common Ancestor in a BST

## 1. Problem

Given the root of a **Binary Search Tree (BST)** and two nodes `p` and `q`, find their **Lowest Common Ancestor (LCA)**.

### What is LCA?

The Lowest Common Ancestor of `p` and `q` is the lowest node in the tree that has both `p` and `q` in its subtree.

Example:

```text
        6
       / \
      2   8
     / \ / \
    0  4 7  9
      / \
     3   5
```

For:

```text
p = 2
q = 8
```

LCA is:

```text
6
```

For:

```text
p = 2
q = 4
```

LCA is:

```text
2
```

---

# 2. Brute Force

A general Binary Tree solution can be used without using the BST property.

## Idea

1. Find the path from root to `p`.
2. Find the path from root to `q`.
3. Compare both paths.
4. The last common node is the LCA.

Example:

```text
Path to 2:

6 → 2

Path to 4:

6 → 2 → 4
```

Last common node:

```text
2
```

### Complexity

```text
Time:  O(n)
Space: O(h)
```

The path-based approach may require storing paths of height `h`.

### Why can we do better?

Because this is a **BST**, we don't need to search the entire tree.

We can use:

```text
Left values  < Root
Right values > Root
```

---

# 3. Important BST Property

For every node:

```text
        root
       /    \
   smaller  greater
```

Therefore, for nodes `p` and `q`:

```text
If both are smaller than root:
    LCA must be in left subtree

If both are greater than root:
    LCA must be in right subtree

Otherwise:
    Current root is the LCA
```

This is the main idea of the problem.

---

# 4. Three Cases

Suppose:

```text
        6
       / \
      2   8
     / \ / \
    0  4 7  9
```

---

## Case 1 — Both Nodes Are in Left Subtree

If:

```python
p.val < root.val and q.val < root.val
```

then both nodes are smaller than the current root.

Therefore:

```text
        6
       /
      2
     / \
    p   q
```

The LCA must be somewhere in the left subtree.

So:

```python
return self.lowestCommonAncestor(root.left, p, q)
```

---

## Case 2 — Both Nodes Are in Right Subtree

If:

```python
p.val > root.val and q.val > root.val
```

then both nodes are greater than the current root.

Therefore:

```text
        6
          \
           8
          / \
         p   q
```

The LCA must be somewhere in the right subtree.

So:

```python
return self.lowestCommonAncestor(root.right, p, q)
```

---

## Case 3 — Nodes Are on Different Sides

Suppose:

```text
        6
       / \
      2   8
```

and:

```text
p = 2
q = 8
```

One node is smaller:

```text
p.val < root.val
```

and the other is greater:

```text
q.val > root.val
```

Therefore:

```text
6
├── left  → p
└── right → q
```

The current root is the LCA.

So:

```python
return root
```

---

# 5. Case 4 — One Node Is the Current Root

This is also handled automatically by:

```python
return root
```

Example:

```text
        6
       / \
      2   8
```

Suppose:

```text
p = 6
q = 8
```

Then:

```text
p.val == root.val
```

So `root` itself is the LCA.

The final:

```python
return root
```

correctly handles this case.

---

# 6. Complete Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def lowestCommonAncestor(
        self,
        root: 'TreeNode',
        p: 'TreeNode',
        q: 'TreeNode'
    ) -> 'TreeNode':

        if root is None:
            return None

        # Case 1:
        # Both p and q are smaller than root.
        # Therefore, LCA is in the left subtree.
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        # Case 2:
        # Both p and q are greater than root.
        # Therefore, LCA is in the right subtree.
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        # Case 3:
        # p and q are on different sides of root.
        #
        # Case 4:
        # One of p or q is the current root.
        #
        # In both cases, root is the LCA.
        return root
```

---

# 7. Dry Run

Consider:

```text
        6
       / \
      2   8
     / \ / \
    0  4 7  9
      / \
     3   5
```

Find:

```text
LCA(2, 8)
```

### At root = 6

Check:

```text
p = 2
q = 8
```

```text
2 < 6
8 > 6
```

They are on different sides.

Therefore:

```python
return root
```

Answer:

```text
6
```

---

# 8. Another Dry Run

Find:

```text
LCA(3, 5)
```

Tree:

```text
        6
       /
      2
       \
        4
       / \
      3   5
```

### At root = 6

```text
3 < 6
5 < 6
```

Both are smaller.

Move left:

```text
root = 2
```

### At root = 2

```text
3 > 2
5 > 2
```

Both are greater.

Move right:

```text
root = 4
```

### At root = 4

```text
3 < 4
5 > 4
```

They are on different sides.

Therefore:

```text
LCA = 4
```

---

# 9. Why We Don't Need to Find the Paths

In a normal Binary Tree:

```text
        root
       /    \
      ?      ?
```

we don't know where a value is located.

So we may need to search both subtrees.

But in a BST:

```text
value < root → LEFT
value > root → RIGHT
```

So at every node we immediately know which direction to go.

This reduces the work from potentially searching the entire tree to following only one path.

---

# 10. Complexity

At every step, we move to only one subtree.

Therefore, the time depends on the height of the BST.

```text
Time = O(h)
```

### Balanced BST

```text
h = log n

Time = O(log n)
```

### Skewed BST

```text
h = n

Time = O(n)
```

Because the solution is recursive:

```text
Space = O(h)
```

for the recursion call stack.

---

# 11. Iterative Version

The same logic can be implemented without recursion.

```python
class Solution:

    def lowestCommonAncestor(
        self,
        root: 'TreeNode',
        p: 'TreeNode',
        q: 'TreeNode'
    ) -> 'TreeNode':

        while root:

            if p.val < root.val and q.val < root.val:
                root = root.left

            elif p.val > root.val and q.val > root.val:
                root = root.right

            else:
                return root

        return None
```

### Complexity

```text
Time:  O(h)
Space: O(1)
```

The iterative version removes recursion stack space.

---

# 12. Common Mistakes

## 1. Treating BST like a normal Binary Tree

Don't search both sides unnecessarily.

Use:

```text
BST property
```

to decide the direction.

---

## 2. Checking only `p`

It is not enough to check:

```python
if p.val < root.val:
```

You need to know where **both** nodes are.

That's why:

```python
if p.val < root.val and q.val < root.val:
```

is used.

---

## 3. Forgetting the split case

If:

```text
p < root < q
```

or:

```text
q < root < p
```

then:

```text
root = LCA
```

This is the most important stopping condition.

---

## 4. Forgetting the case where root is p or q

Example:

```text
        6
       / \
      2   8
```

If:

```text
p = 6
q = 8
```

then `6` itself is the LCA.

The final:

```python
return root
```

handles this automatically.

---

# 13. Pattern Recognition

When you see:

```text
LCA
+
BST
```

think:

```text
Compare p and q with root

        ↓

Both smaller?
    → LEFT

Both greater?
    → RIGHT

Otherwise?
    → ROOT is LCA
```

The entire solution is based on one BST property:

```text
Left < Root < Right
```

---

# 14. Revision Cheat Sheet

```text
LCA in BST

At every root:

if p < root and q < root:
    go LEFT

elif p > root and q > root:
    go RIGHT

else:
    root is LCA
```

### Complexity

```text
Recursive:
Time  = O(h)
Space = O(h)

Iterative:
Time  = O(h)
Space = O(1)
```

### Tree Height

```text
Balanced BST:
O(log n)

Skewed BST:
O(n)
```

> **One-Line Pattern: LCA in BST = Compare both nodes with root → both smaller go Left, both greater go Right, otherwise current root is the LCA.**