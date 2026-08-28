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

Number of edges:

```text
1
```

Height of right subtree:

```text
3
```

Number of edges:

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
1 + 1 = 2
```

So:

```python
left_height + right_height
```

gives the diameter passing through the current node.

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

For example:

```text
    1
   /
  2
 /
3
```

Height:

```text
3
```

But when calculating diameter:

```python
left_height + right_height
```

we are effectively counting the edges on both sides of the current node.

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

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

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

But while recursively calculating the diameter of node `2`, we again calculate heights of its subtrees.

So the same nodes can be visited multiple times.

Therefore, in the worst case:

```text
Time = O(n²)
```

---

# Approach 2: Optimized O(n) Approach

## Main Idea

Instead of calculating:

```text
Height
+
Diameter
```

separately, calculate both during **one DFS traversal**.

For every node, return:

```text
height
```

And maintain a global:

```text
diameter
```

---

# Key Observation

At every node:

```text
left_height = height of left subtree
right_height = height of right subtree
```

The diameter passing through this node is:

```text
left_height + right_height
```

So while calculating the height, we can also update the diameter.

---

# Optimized Code

```python
class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        diameter = 0

        def dfs(root):

            nonlocal diameter

            if root is None:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            # Diameter passing through current node
            diameter = max(diameter, left + right)

            # Return height of current node
            return max(left, right) + 1

        dfs(root)

        return diameter
```

---

# How Optimized Approach Works

For every node, DFS returns:

```text
Height of that subtree
```

At the same time:

```python
diameter = max(diameter, left + right)
```

checks whether the path passing through the current node is the largest diameter found so far.

So each node does only constant work:

```text
1. Get left height
2. Get right height
3. Calculate diameter through current node
4. Return height
```

No height is recalculated.

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

diameter = max(0, 0 + 0)
         = 0

height = max(0, 0) + 1
       = 1
```

Return:

```text
1
```

---

### Node 5

Same:

```text
height = 1
diameter = 0
```

---

### Node 2

Left height:

```text
1
```

Right height:

```text
1
```

Diameter through `2`:

```text
1 + 1 = 2
```

So:

```text
diameter = 2
```

Height of node `2`:

```text
max(1, 1) + 1
= 2
```

Return:

```text
2
```

---

### Node 3

```text
left = 0
right = 0

diameter = max(2, 0)
         = 2

height = 1
```

---

### Node 1

Left height:

```text
2
```

Right height:

```text
1
```

Diameter through `1`:

```text
2 + 1 = 3
```

So:

```text
diameter = 3
```

Height:

```text
max(2, 1) + 1
= 3
```

Final:

```text
Diameter = 3
```

---

# Why `nonlocal diameter`?

Inside:

```python
def dfs(root):
```

we need to update the `diameter` variable created in:

```python
diameter = 0
```

The variable belongs to the outer function.

So we use:

```python
nonlocal diameter
```

This allows `dfs()` to modify the outer `diameter`.

---

# Why Does DFS Return Height Instead of Diameter?

This is a very important interview concept.

At a node, to calculate the diameter through that node, we need:

```text
left height
right height
```

Therefore the recursive function must return:

```text
height
```

The diameter is simply updated separately:

```python
diameter = max(diameter, left + right)
```

So:

```text
Return value:
Height

Side effect:
Update Diameter
```

This lets us calculate both in one traversal.

---

# Why Is the Diameter `left + right`?

Remember:

```text
height = number of nodes
```

but diameter is:

```text
number of edges
```

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

The path:

```text
2 → 1 → 3
```

has:

```text
2 edges
```

And:

```text
left + right
= 1 + 1
= 2
```

So the formula works.

---

# Important Interview Distinction

### Height

Usually measured as:

```text
Number of nodes
```

So:

```python
height = max(left, right) + 1
```

### Diameter

Measured as:

```text
Number of edges
```

So:

```python
diameter = left + right
```

This distinction is important because many tree problems can define height/depth differently.

For this LeetCode problem:

```text
Height → nodes
Diameter → edges
```

---

# Why the Diameter Does Not Have to Pass Through Root

This is another important point.

Consider:

```text
        1
       / \
      2   3
     / \
    4   5
   /
  6
```

The longest path may be:

```text
6 → 4 → 2 → 5
```

It does not use the root `1`.

That's why at every node we consider:

```text
Diameter in left subtree
Diameter in right subtree
Diameter through current node
```

In the optimized solution, this is handled by updating:

```python
diameter = max(diameter, left + right)
```

at **every node**.

---

# Complexity

## Basic Approach

```text
Time  → O(n²)
Space → O(h)
```

Why `O(n²)`?

Because heights are recalculated repeatedly.

Why `O(h)`?

Because recursion uses the call stack.

---

## Optimized Approach

```text
Time  → O(n)
Space → O(h)
```

Every node is visited exactly once.

The recursive call stack still uses:

```text
O(h)
```

where `h` is the height of the tree.

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

## 1. Returning Diameter From DFS

Don't confuse the return value.

The DFS should return:

```text
Height
```

because the parent needs the height to calculate its own diameter.

---

## 2. Using `max(left, right)` for Diameter

Wrong:

```python
diameter = max(left, right)
```

Correct:

```python
diameter = left + right
```

because a path through the current node uses both sides.

---

## 3. Forgetting Diameter Can Be Inside a Subtree

The answer does not have to pass through the root.

We must check every node.

---

## 4. Confusing Height and Diameter

Remember:

```text
Height → information passed upward
Diameter → global maximum maintained during DFS
```

---

# Revision Cheat Sheet

```text
Diameter of Binary Tree

Pattern:
Binary Tree + DFS + Height

Diameter can be:

1. Completely inside left subtree
2. Completely inside right subtree
3. Passing through current node

Through current node:

diameter = left_height + right_height

--------------------------------------------------

Basic Approach:

For every node:

option1 = diameter(left)
option2 = diameter(right)
option3 = height(left) + height(right)

answer = max(option1, option2, option3)

Problem:
Height is recalculated many times.

Time  → O(n²)
Space → O(h)

--------------------------------------------------

Optimized Approach:

Use one DFS.

DFS returns:
Height

DFS updates:
Diameter

Code idea:

left = dfs(root.left)
right = dfs(root.right)

diameter = max(diameter, left + right)

return max(left, right) + 1

Time  → O(n)
Space → O(h)

--------------------------------------------------

Important:

Height:
Number of nodes  

Diameter:
Number of edges

Height formula:

max(left, right) + 1

Diameter formula:

left + right
```

---

# One-Line Pattern

```text
DFS returns subtree height, while at every node we use left_height + right_height to update the maximum diameter.
```