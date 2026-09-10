# Diameter of Binary Tree

## Problem

Given the root of a binary tree, return the **diameter** of the tree.

The diameter is the **number of edges** on the longest path between any two nodes.

The path does **not necessarily have to pass through the root**.

### Example

```text
        1
       / \
      2   3
     / \
    4   5
```

The longest path is:

```text
4 → 2 → 1 → 3
```

Number of edges:

```text
3
```

So:

```text
Diameter = 3
```

---

# Pattern

```text
Binary Tree + DFS + Height
```

The important idea is:

```text
Diameter through a node
=
Height of left subtree
+
Height of right subtree
```

---

# Approach 1: Brute Force / Basic Recursive Approach

## Main Idea

For every node, there are three possibilities:

```text
1. Diameter exists completely in the left subtree
2. Diameter exists completely in the right subtree
3. Diameter passes through the current node
```

So:

```text
answer = max(option1, option2, option3)
```

---

# Option 1: Diameter in Left Subtree

```python
option1 = self.diameterOfBinaryTree(root.left)
```

The longest path might be completely inside the left subtree.

---

# Option 2: Diameter in Right Subtree

```python
option2 = self.diameterOfBinaryTree(root.right)
```

The longest path might be completely inside the right subtree.

---

# Option 3: Diameter Through Current Node

If the longest path passes through the current node:

```text
left subtree
      ↓
    current
      ↓
right subtree
```

The number of edges is:

```python
height(left) + height(right)
```

So:

```python
option3 = self.getHeight(root.left) + self.getHeight(root.right)
```

---

# Why Do We Add Left Height + Right Height?

Suppose:

```text
        1
       / \
      2   3
     /
    4
```

Height of left subtree:

```text
2 → 4
```

Height:

```text
2
```

Height of right subtree:

```text
3
```

Height:

```text
1
```

Path through `1`:

```text
4 → 2 → 1 → 3
```

Edges:

```text
4 → 2   = 1
2 → 1   = 1
1 → 3   = 1
```

Total:

```text
3
```

And:

```python
left_height + right_height
```

gives:

```text
2 + 1 = 3
```

So the formula works.

---

# Height Function

```python
def getHeight(self, root):

    if root is None:
        return 0

    left = self.getHeight(root.left)
    right = self.getHeight(root.right)

    return max(left, right) + 1
```

This returns the height in terms of **number of nodes**.

For:

```text
    1
   /
  2
 /
3
```

height is:

```text
3
```

But diameter is measured in **edges**.

---

# Code: Basic Approach

```python
class Solution:

    def getHeight(self, root):

        if root is None:
            return 0

        left = self.getHeight(root.left)
        right = self.getHeight(root.right)

        maxHeight = max(left, right)

        return maxHeight + 1

    def diameterOfBinaryTree(self, root):

        if root is None:
            return 0

        # Diameter completely inside left subtree
        option1 = self.diameterOfBinaryTree(root.left)

        # Diameter completely inside right subtree
        option2 = self.diameterOfBinaryTree(root.right)

        # Diameter passing through current node
        option3 = (
            self.getHeight(root.left)
            + self.getHeight(root.right)
        )

        maxDiameter = max(
            option1,
            max(option2, option3)
        )

        return maxDiameter
```

---

# Why This Approach Is O(n²)

This is the important drawback.

At every node, we calculate:

```text
diameter(left)
diameter(right)
height(left)
height(right)
```

The problem is:

> We repeatedly calculate the height of the same subtrees.

For example:

```text
        1
       / \
      2   3
     / \
    4   5
```

When calculating the diameter of node `1`, we calculate:

```text
height(left)
height(right)
```

But while recursively calculating the diameter of node `2`, we again calculate the heights of its subtrees.

So the same nodes can be visited multiple times.

Therefore, in the worst case:

```text
Time = O(n²)
```

Space:

```text
O(h)
```

because of recursion.

---

# Approach 2: Optimized O(n) — Global Diameter

## Main Idea

Instead of calculating:

```text
Height
+
Diameter
```

separately, calculate both during **one DFS traversal**.

For every node:

```text
1. Get left subtree height
2. Get right subtree height
3. Calculate diameter through current node
4. Update global diameter
5. Return current subtree height
```

This is exactly what your second code does.

---

# Your Approach

```python
class Solution:

    D = 0

    def height(self, root):

        if root is None:
            return 0

        left = self.height(root.left)
        right = self.height(root.right)

        currD = left + right

        self.D = max(currD, self.D)

        return max(left, right) + 1

    def diameterOfBinaryTree(self, root):

        self.height(root)

        return self.D
```

---

# Important Idea: `D` Stores the Best Diameter

Here:

```python
D = 0
```

means:

```text
D = maximum diameter found so far
```

At every node we calculate:

```python
currD = left + right
```

This represents:

```text
Diameter passing through the current node
```

Then:

```python
self.D = max(currD, self.D)
```

means:

```text
Keep the largest diameter found anywhere in the tree.
```

---

# Why Is `D` Needed?

The diameter does **not necessarily pass through the root**.

For example:

```text
        1
       / \
      2   3
     /
    4
   /
  5
```

The longest path could be completely inside the left subtree.

Therefore, we cannot simply calculate:

```python
left_height + right_height
```

only at the root.

We calculate it at **every node**:

```python
currD = left + right
```

and keep the maximum:

```python
self.D = max(self.D, currD)
```

---

# Why Does `height()` Return Height?

This is very important.

The function:

```python
height(root)
```

has two jobs.

### Job 1: Calculate Diameter

```python
currD = left + right
self.D = max(self.D, currD)
```

### Job 2: Return Height to Parent

```python
return max(left, right) + 1
```

The parent needs the height of this subtree to calculate its own diameter.

So:

```text
height()
   │
   ├── Updates global diameter
   │
   └── Returns subtree height
```

This allows us to calculate everything in **one traversal**.

---

# Why `left + right`?

Suppose:

```text
      1
     / \
    2   3
```

For node `1`:

```text
left height  = 1
right height = 1
```

The path is:

```text
2 → 1 → 3
```

Number of edges:

```text
2
```

Therefore:

```python
left + right
= 1 + 1
= 2
```

So:

```python
currD = left + right
```

gives the diameter passing through the current node.

---

# Complete Optimized Code

```python
class Solution:

    def height(self, root):

        if root is None:
            return 0

        # Get left subtree height
        left = self.height(root.left)

        # Get right subtree height
        right = self.height(root.right)

        # Diameter passing through current node
        currD = left + right

        # Update maximum diameter
        self.D = max(currD, self.D)

        # Return height of current subtree
        return max(left, right) + 1

    def diameterOfBinaryTree(self, root):

        # Reset diameter for this problem call
        self.D = 0

        # Calculate heights and diameter together
        self.height(root)

        return self.D
```

> **Important:** I recommend resetting `self.D` inside `diameterOfBinaryTree()` rather than keeping only `D = 0` at class level.

---

# Why Reset `self.D`?

Your original code has:

```python
class Solution:
    D = 0
```

This creates a class-level variable.

A safer version is:

```python
def diameterOfBinaryTree(self, root):
    self.D = 0
    self.height(root)
    return self.D
```

Now every call starts with:

```text
D = 0
```

This avoids carrying an old diameter value into another call.

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

---

## Node 4

```text
left = 0
right = 0
```

Diameter through `4`:

```text
0 + 0 = 0
```

So:

```text
D = 0
```

Height:

```text
max(0, 0) + 1 = 1
```

Return:

```text
1
```

---

## Node 5

Same:

```text
left = 0
right = 0

currD = 0
height = 1
```

So:

```text
D = 0
```

---

## Node 2

Node `2` receives:

```text
left = 1
right = 1
```

Diameter through `2`:

```text
currD = 1 + 1 = 2
```

Update:

```text
D = 2
```

Height:

```text
max(1, 1) + 1
= 2
```

Return:

```text
2
```

---

## Node 3

Leaf:

```text
left = 0
right = 0
```

So:

```text
currD = 0
height = 1
```

`D` remains:

```text
2
```

---

## Node 1

Now:

```text
left = 2
right = 1
```

Diameter through `1`:

```text
currD = 2 + 1
      = 3
```

Update:

```text
D = max(3, 2)
  = 3
```

Height:

```text
max(2, 1) + 1
= 3
```

Final:

```text
D = 3
```

Therefore:

```text
Diameter = 3
```

---

# Approach 3: Optimized DFS + `-1` Sentinel

There is another way to write the optimized solution.

Instead of using:

```python
self.D
```

we can use a local variable with `nonlocal`.

```python
class Solution:

    def diameterOfBinaryTree(self, root):

        diameter = 0

        def dfs(root):

            nonlocal diameter

            if root is None:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            diameter = max(diameter, left + right)

            return max(left, right) + 1

        dfs(root)

        return diameter
```

This and your `self.D` approach have the same complexity.

The difference is mainly how the global result is stored.

---

# `self.D` vs `nonlocal diameter`

### Your approach

```python
self.D = max(currD, self.D)
```

`D` belongs to the object.

### Local variable approach

```python
diameter = 0
```

and:

```python
nonlocal diameter
```

allows the nested `dfs()` function to modify it.

Both work.

For LeetCode, your `self.D` approach is perfectly valid.

---

# Why Is the Optimized Approach O(n)?

Every node is visited exactly once.

At every node:

```text
Get left height
Get right height
Calculate current diameter
Update maximum
Return height
```

All of these are `O(1)` work after the recursive calls.

Therefore:

```text
Time = O(n)
```

---

# Why Is Space O(h)?

The solution uses recursion.

The recursive calls are stored in the **call stack**.

For example, in a skewed tree:

```text
1
 \
  2
   \
    3
     \
      4
```

the call stack can become:

```text
height(1)
height(2)
height(3)
height(4)
```

So maximum recursion depth is:

```text
h
```

Therefore:

```text
Space = O(h)
```

For a balanced tree:

```text
h = O(log n)
```

For a skewed tree:

```text
h = O(n)
```

---

# Basic vs Optimized

| Approach | Idea | Time | Space |
|---|---|---:|---:|
| Basic | Recalculate heights repeatedly | O(n²) | O(h) |
| Optimized | Height + diameter in one DFS | O(n) | O(h) |

---

# Important Interview Distinction

### Height

For this solution:

```text
Height = number of nodes
```

Formula:

```python
max(left, right) + 1
```

### Diameter

For LeetCode:

```text
Diameter = number of edges
```

Formula:

```python
left + right
```

Remember:

```text
Height → returned to parent

Diameter → maximum maintained while traversing
```

---

# Common Mistakes

## 1. Returning Diameter Instead of Height

The recursive function should return:

```python
max(left, right) + 1
```

because the parent needs the subtree's height.

The diameter is maintained separately.

---

## 2. Using `max(left, right)` for Diameter

Wrong:

```python
currD = max(left, right)
```

Correct:

```python
currD = left + right
```

A diameter passing through the current node uses **both sides**.

---

## 3. Checking Diameter Only at Root

Wrong idea:

```text
Calculate left height + right height only once at root.
```

The longest path might be inside a subtree.

So:

```python
self.D = max(self.D, left + right)
```

must happen at every node.

---

## 4. Forgetting to Reset `self.D`

Prefer:

```python
def diameterOfBinaryTree(self, root):
    self.D = 0
```

before starting DFS.

---

## 5. Confusing Nodes and Edges

For:

```text
2 → 1 → 3
```

there are:

```text
3 nodes
2 edges
```

Therefore:

```text
Height = nodes
Diameter = edges
```

---

# Pattern Recognition

When you see:

> Find the longest path in a binary tree.

Think:

```text
Binary Tree
     ↓
DFS
     ↓
Need subtree heights
     ↓
Diameter through node
=
left height + right height
```

Then ask:

```text
Am I recalculating heights?
        ↓
YES
        ↓
Optimize!
        ↓
Calculate height + diameter
in the same DFS
```

---

# Revision Cheat Sheet

```text
Diameter of Binary Tree

Pattern:
Binary Tree + DFS + Height

Diameter can be:

1. Inside left subtree
2. Inside right subtree
3. Passing through current node

Through current node:

diameter = left_height + right_height

--------------------------------------------------

Basic Approach:

option1 = diameter(left)
option2 = diameter(right)
option3 = height(left) + height(right)

answer = max(option1, option2, option3)

Problem:
Height is recalculated repeatedly.

Time  → O(n²)
Space → O(h)

--------------------------------------------------

Optimized Approach:

Use one DFS.

At every node:

left = height(left subtree)
right = height(right subtree)

currD = left + right

D = max(D, currD)

return max(left, right) + 1

--------------------------------------------------

Your Code's Important Idea:

self.D
    ↓
Stores maximum diameter found so far.

height()
    ↓
1. Calculates current diameter
2. Updates self.D
3. Returns height to parent

--------------------------------------------------

Height:

max(left, right) + 1

Height counts:
Number of nodes

Diameter:

left + right

Diameter counts:
Number of edges

--------------------------------------------------

Why O(n)?

Every node is visited once.

Why O(h) space?

Recursion call stack stores
the current root-to-leaf path.

Balanced tree:
O(log n)

Skewed tree:
O(n)
```

# One-Line Pattern

```text
DFS returns subtree height, while at every node we calculate left_height + right_height and maintain the maximum as the diameter.
```