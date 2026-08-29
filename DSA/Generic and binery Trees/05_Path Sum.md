# Path Sum

## Problem

Given the root of a binary tree and an integer `targetSum`, determine whether the tree has a **root-to-leaf path** such that the sum of all node values on that path equals `targetSum`.

### Important

The path must:

```text
Start at the root
        ↓
End at a leaf
```

A leaf is a node where:

```python
root.left is None and root.right is None
```

---

# Pattern

```text
Binary Tree + DFS + Recursion + Running Sum
```

---

# Main Idea

While traversing the tree, maintain:

```text
Sum
```

which represents the sum of values from the **root to the current node**.

At every node:

```python
Sum = Sum + root.val
```

When we reach a leaf, check:

```python
Sum == targetSum
```

If yes:

```text
Path exists → True
```

Otherwise:

```text
False
```

---

# Why Do We Check Only at a Leaf?

The problem specifically asks for a:

```text
Root → Leaf
```

path.

So reaching the target sum at an intermediate node is **not enough**.

Example:

```text
        5
       /
      4
     /
    3
```

Suppose:

```text
targetSum = 9
```

At node `4`:

```text
5 + 4 = 9
```

But `4` is not a leaf.

So this is **not** a valid path.

We must continue until a leaf.

---

# Code

```python
class Solution:

    def solve(self, root, targetSum, Sum):

        # Empty subtree
        if root is None:
            return False

        # Add current node value
        Sum = Sum + root.val

        # Check only at leaf
        if root.left is None and root.right is None:

            if Sum == targetSum:
                return True
            else:
                return False

        # Search left subtree
        leftAns = self.solve(root.left, targetSum, Sum)

        # Search right subtree
        rightAns = self.solve(root.right, targetSum, Sum)

        # If either side has a valid path
        return leftAns or rightAns

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        Sum = 0

        return self.solve(root, targetSum, Sum)
```

---

# Understanding `Sum`

Suppose:

```text
        5
       / \
      4   8
     /     \
    3       2
```

For the path:

```text
5 → 4 → 3
```

The recursive calls maintain:

```text
At 5:
Sum = 5

At 4:
Sum = 5 + 4 = 9

At 3:
Sum = 9 + 3 = 12
```

At leaf `3`:

```text
Sum = 12
```

So if:

```text
targetSum = 12
```

we return:

```text
True
```

---

# Why Does `Sum` Not Need to Be Reset?

This is an important recursion concept.

We call:

```python
self.solve(root.left, targetSum, Sum)
self.solve(root.right, targetSum, Sum)
```

`Sum` is an integer.

Integers are immutable in Python, so:

```python
Sum = Sum + root.val
```

creates a new value for that particular recursive call.

The left subtree's `Sum` does not modify the `Sum` used by the right subtree.

Conceptually:

```text
              5 (Sum=5)
             /        \
       4 (Sum=9)    8 (Sum=13)
```

Each recursive path maintains its own running sum.

---

# Why Use `leftAns or rightAns`?

There can be two possibilities:

```text
Valid path exists in left subtree
OR
Valid path exists in right subtree
```

Therefore:

```python
return leftAns or rightAns
```

means:

```text
If either subtree has a valid path → True
```

---

# Dry Run

Consider:

```text
        5
       / \
      4   8
     /   / \
    3   7   2
```

Target:

```text
targetSum = 12
```

Start:

```text
Sum = 0
```

At `5`:

```text
Sum = 5
```

Go left.

At `4`:

```text
Sum = 5 + 4
     = 9
```

Go left.

At `3`:

```text
Sum = 9 + 3
     = 12
```

`3` is a leaf.

Check:

```text
Sum == targetSum
12 == 12
```

Therefore:

```text
True
```

The answer immediately propagates upward:

```text
3 → 4 → 5
```

---

# What Happens When One Side Fails?

Suppose:

```text
        5
       / \
      4   8
     /     \
    1       2
```

Target:

```text
10
```

Left path:

```text
5 → 4 → 1
```

Sum:

```text
10
```

So:

```text
leftAns = True
```

Even if the right side is:

```text
False
```

we have:

```python
True or False
```

Therefore:

```text
True
```

---

# Base Cases

There are two important stopping conditions.

## 1. Root is None

```python
if root is None:
    return False
```

There is no path in an empty subtree.

---

## 2. Current Node is a Leaf

```python
if root.left is None and root.right is None:
```

Now we have reached the end of a root-to-leaf path.

Check:

```python
Sum == targetSum
```

---

# Important Interview Point

Do **not** check:

```python
if Sum == targetSum:
    return True
```

before checking whether the current node is a leaf.

Because the problem asks for:

```text
Root → Leaf
```

not:

```text
Root → Any Node
```

---

# Complexity

Every node may be visited once.

```text
Time → O(n)
```

where `n` is the number of nodes.

The recursion call stack stores the current root-to-leaf path:

```text
Space → O(h)
```

where:

```text
h = height of tree
```

For a balanced tree:

```text
O(log n)
```

For a skewed tree:

```text
O(n)
```

---

# Common Mistakes

## 1. Checking Target Sum at Any Node

Wrong:

```text
If running sum == targetSum → True
```

Correct:

```text
Only check when current node is a leaf.
```

---

## 2. Forgetting the Current Node

Always update:

```python
Sum = Sum + root.val
```

before checking the leaf.

---

## 3. Checking Only One Subtree

A valid path can exist on either side.

So:

```python
leftAns = ...
rightAns = ...

return leftAns or rightAns
```

---

## 4. Forgetting the Empty Tree

For:

```python
root = None
```

there is no root-to-leaf path.

Return:

```python
False
```

---

# Revision Cheat Sheet

```text
Path Sum

Pattern:
Binary Tree + DFS + Recursion + Running Sum

Goal:
Find a ROOT → LEAF path whose sum
equals targetSum.

--------------------------------------------------

At every node:

Sum += root.val

--------------------------------------------------

If root is None:

return False

--------------------------------------------------

If root is a leaf:

if Sum == targetSum:
    return True

else:
    return False

--------------------------------------------------

Otherwise:

leftAns = solve(left)
rightAns = solve(right)

return leftAns or rightAns

--------------------------------------------------

Important:

Target sum must be checked
ONLY at a leaf.

--------------------------------------------------

Why?

Because the required path must be:

Root → Leaf

--------------------------------------------------

Complexity:

Time  → O(n)
Space → O(h)

h = tree height

Balanced tree:
O(log n)

Skewed tree:
O(n)
```

---

# One-Line Pattern

```text
DFS keeps a running root-to-current sum, and only when a leaf is reached do we check whether the sum equals targetSum.
```