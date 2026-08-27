# Balanced Binary Tree

## Problem

Given the root of a binary tree, determine whether the tree is **height-balanced**.

A binary tree is balanced if, for **every node**:

```text
|height(left subtree) - height(right subtree)| <= 1
```

### Example

Balanced:

```text
        3
       / \
      9   20
         /  \
        15   7
```

At every node, the difference between left and right subtree heights is at most `1`.

Answer:

```text
True
```

Unbalanced:

```text
        1
       /
      2
     /
    3
```

At node `1`:

```text
left height  = 2
right height = 0

difference = 2
```

So the tree is not balanced.

Answer:

```text
False
```

---

# Pattern

```text
Binary Tree + DFS + Height
```

---

# Approach 1: Basic Recursive Approach

## Main Idea

For every node, we need to check three things:

```text
1. Is the current node balanced?
2. Is the left subtree balanced?
3. Is the right subtree balanced?
```

For the current node:

```python
left = self.getHeight(root.left)
right = self.getHeight(root.right)
```

Calculate the difference:

```python
absDiff = abs(left - right)
```

The current node is balanced if:

```python
absDiff <= 1
```

Then recursively check:

```python
leftTree = self.isBalanced(root.left)
rightTree = self.isBalanced(root.right)
```

Finally:

```python
status and leftTree and rightTree
```

must be `True`.

---

# Why Do We Need to Check Every Node?

It is not enough to check only the root.

Example:

```text
        1
       / \
      2   3
     /
    4
   /
  5
```

The root may look balanced, but the left subtree is not balanced.

Therefore:

```text
Every node must satisfy:

|left height - right height| <= 1
```

---

# Height Function

Your code uses a separate function:

```python
def getHeight(self, root):

    if root is None:
        return 0

    left = self.getHeight(root.left)
    right = self.getHeight(root.right)

    return max(left, right) + 1
```

This calculates the height of a subtree.

For:

```text
    1
   / \
  2   3
```

the height is:

```text
2
```

because height here is measured in number of nodes.

---

# Code: Basic Approach

```python
class Solution:

    def getHeight(self, root):

        if root is None:
            return 0

        left = self.getHeight(root.left)
        right = self.getHeight(root.right)

        maxDigit = max(left, right)

        return maxDigit + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return True

        # Height of both subtrees
        left = self.getHeight(root.left)
        right = self.getHeight(root.right)

        # Check current node
        absDiff = abs(left - right)
        status = absDiff <= 1

        # Check left and right subtrees
        leftTree = self.isBalanced(root.left)
        rightTree = self.isBalanced(root.right)

        return status and leftTree and rightTree
```

---

# Why Is This O(n²)?

This is the important drawback.

At every node, we call:

```python
getHeight(root.left)
getHeight(root.right)
```

Then we recursively call:

```python
isBalanced(root.left)
isBalanced(root.right)
```

The problem is that `getHeight()` repeatedly visits the same nodes.

For example, when checking the root, we calculate the height of the entire subtree.

Then when checking a child, we calculate the height of that subtree again.

So the same nodes are visited multiple times.

In the worst case:

```text
Time → O(n²)
```

---

# Approach 2: Optimized O(n)

## Main Idea

We can check **balance and height at the same time**.

Instead of:

```text
Calculate height
        ↓
Check balance
```

we do:

```text
Calculate height + Check balance
```

in a single DFS.

---

# Key Idea

For every node, the DFS returns:

```text
Height of subtree
```

But if the subtree is unbalanced, we return:

```text
-1
```

So:

```text
-1 = This subtree is not balanced
```

This allows us to detect imbalance immediately.

---

# Why Return `-1`?

Normally height is:

```text
0, 1, 2, 3, ...
```

So `-1` can be used as a special value meaning:

```text
This subtree is unbalanced.
```

Example:

```text
        1
       /
      2
     /
    3
```

When DFS reaches node `1`, its left subtree will eventually report:

```text
-1
```

Then node `1` also returns:

```text
-1
```

There is no need to calculate anything else.

---

# Optimized Code

```python
class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):

            if root is None:
                return 0

            # Get left subtree height
            left = dfs(root.left)

            # Left subtree is unbalanced
            if left == -1:
                return -1

            # Get right subtree height
            right = dfs(root.right)

            # Right subtree is unbalanced
            if right == -1:
                return -1

            # Current node is unbalanced
            if abs(left - right) > 1:
                return -1

            # Return height of current subtree
            return max(left, right) + 1

        return dfs(root) != -1
```

---

# How Optimized Approach Works

At every node:

### Step 1

Find left subtree height:

```python
left = dfs(root.left)
```

### Step 2

If left subtree is already unbalanced:

```python
if left == -1:
    return -1
```

Immediately stop.

### Step 3

Find right subtree height:

```python
right = dfs(root.right)
```

### Step 4

If right subtree is unbalanced:

```python
if right == -1:
    return -1
```

### Step 5

Check current node:

```python
if abs(left - right) > 1:
    return -1
```

### Step 6

If everything is balanced, return height:

```python
return max(left, right) + 1
```

---

# Important Concept

The DFS has **two jobs**:

```text
1. Return height
2. Detect imbalance
```

So the return value has two meanings:

```text
Positive value → Height of balanced subtree

-1 → Subtree is unbalanced
```

This is the main trick of the optimized solution.

---

# Dry Run

Consider:

```text
        1
       / \
      2   3
     / \
    4   5
```

### Node 4

```text
left = 0
right = 0
```

Difference:

```text
0
```

Balanced.

Return height:

```text
1
```

---

### Node 5

Same:

```text
height = 1
```

---

### Node 2

```text
left = 1
right = 1
```

Difference:

```text
|1 - 1| = 0
```

Balanced.

Return:

```text
max(1, 1) + 1 = 2
```

---

### Node 3

```text
left = 0
right = 0
```

Balanced.

Return:

```text
1
```

---

### Node 1

```text
left = 2
right = 1
```

Difference:

```text
|2 - 1| = 1
```

Balanced.

Return:

```text
max(2, 1) + 1 = 3
```

Finally:

```python
dfs(root) != -1
```

gives:

```text
True
```

---

# Dry Run: Unbalanced Tree

Consider:

```text
        1
       /
      2
     /
    3
```

### Node 3

```text
left = 0
right = 0

height = 1
```

---

### Node 2

```text
left = 1
right = 0

difference = 1
```

Balanced.

Return:

```text
2
```

---

### Node 1

```text
left = 2
right = 0

difference = 2
```

Since:

```text
2 > 1
```

return:

```text
-1
```

Finally:

```python
dfs(root) != -1
```

becomes:

```text
False
```

---

# Why Is Optimized Approach O(n)?

Each node is visited only once.

At each node we perform constant work:

```text
Get left height
Get right height
Check difference
Calculate height
```

There is no repeated `getHeight()` calculation.

Therefore:

```text
Time → O(n)
```

---

# Why Space Is O(h)

The optimized solution uses recursion.

The recursive calls are stored in the **call stack**.

We only keep the current path from the root to the deepest node.

Therefore:

```text
Space → O(h)
```

where:

```text
h = height of tree
```

For a balanced tree:

```text
h = O(log n)

Space = O(log n)
```

For a skewed tree:

```text
h = O(n)

Space = O(n)
```

---

# Basic vs Optimized

| Approach | Idea | Time | Space |
|---|---|---:|---:|
| Basic | Calculate height separately | `O(n²)` | `O(h)` |
| Optimized | Height + balance in one DFS | `O(n)` | `O(h)` |

---

# Important Interview Point

The optimized solution is a very common **Tree DFS pattern**:

```text
Child returns information
        ↓
Parent uses that information
        ↓
Parent returns updated information
```

Here:

```text
Child returns:
Height

Special value:
-1 = Unbalanced
```

So the parent can immediately detect whether a subtree is invalid.

---

# Common Mistakes

## 1. Checking Only the Root

Wrong idea:

```text
Check height difference only at root.
```

A subtree can be unbalanced even if the root looks balanced.

You must check every node.

---

## 2. Recalculating Height

Calling a separate `getHeight()` for every node causes repeated work.

This leads to:

```text
O(n²)
```

The optimized solution calculates height and balance together.

---

## 3. Forgetting `+1`

Height of current node:

```python
return max(left, right) + 1
```

The `+1` represents the current node.

---

## 4. Confusing `-1` With Height

In the optimized solution:

```text
-1 does NOT mean height -1.
```

It is a special signal:

```text
-1 = subtree is unbalanced
```

---

# Revision Cheat Sheet

```text
Balanced Binary Tree

Pattern:
Binary Tree + DFS + Height

Condition:

abs(left_height - right_height) <= 1

This condition must be true
for EVERY node.

--------------------------------------------------

Basic Approach:

For every node:

1. Calculate left height.
2. Calculate right height.
3. Check difference.
4. Recursively check left subtree.
5. Recursively check right subtree.

Problem:
Height gets recalculated repeatedly.

Time  → O(n²)
Space → O(h)

--------------------------------------------------

Optimized Approach:

One DFS calculates both:

1. Height
2. Balance

DFS returns:

positive value → subtree height
-1             → subtree is unbalanced

At every node:

left = dfs(root.left)

if left == -1:
    return -1

right = dfs(root.right)

if right == -1:
    return -1

if abs(left - right) > 1:
    return -1

return max(left, right) + 1

Final:

return dfs(root) != -1

--------------------------------------------------

Why O(n)?

Every node is visited only once.

Why O(h) space?

Recursion call stack stores the
current root-to-leaf path.

h = height of tree.

Balanced tree:
O(log n)

Skewed tree:
O(n)
```

---

# One-Line Pattern

```text
DFS returns subtree height, and if the height difference at any node exceeds 1, return -1 to propagate the imbalance upward.
```