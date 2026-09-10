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

The important observation is:

> To check whether a node is balanced, we need the height of its left and right subtrees.

So this is naturally solved using **postorder DFS**:

```text
Left Subtree
     ↓
Right Subtree
     ↓
Current Node
```

The children calculate their heights first, and then the parent checks the balance condition.

---

# Approach 1: Basic Recursive Approach

## Main Idea

For every node, we need to check:

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

Then calculate:

```python
absDiff = abs(left - right)
```

The current node is balanced if:

```python
absDiff <= 1
```

Then recursively check the left and right subtrees.

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

For:

```text
    1
   / \
  2   3
```

height is:

```text
2
```

because height is measured in number of nodes.

---

# Code: Basic Approach

```python
class Solution:

    def getHeight(self, root):

        if root is None:
            return 0

        left = self.getHeight(root.left)
        right = self.getHeight(root.right)

        return max(left, right) + 1

    def isBalanced(self, root):

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

For example:

```text
At root:
    calculate height of entire subtree

Then at child:
    calculate height of that subtree again

Then at grandchild:
    calculate height again
```

So the same nodes are visited multiple times.

In the worst case:

```text
Time → O(n²)
```

Space:

```text
O(h)
```

because of the recursion call stack.

---

# Approach 2: Optimized DFS + Boolean Flag

Instead of calculating height separately and repeatedly, we can calculate the height **once** for every node.

Your approach uses:

```python
self.Balanced
```

to remember whether we have found an unbalanced node.

The idea is:

```text
DFS calculates height
        +
DFS checks balance
        ↓
self.Balanced = False
if imbalance is found
```

So we don't need to return `-1`.

---

# Main Idea

For every node:

```text
1. Calculate left subtree height.
2. Calculate right subtree height.
3. Check the height difference.
4. If difference > 1:
       Balanced = False
5. Return current subtree height.
```

The important thing is:

> Even though `height()` returns only the height, it also updates `self.Balanced` whenever it finds an imbalance.

---

# Your Code

```python
class Solution:

    Balanced = True

    def height(self, root):

        if root is None:
            return 0

        left = self.height(root.left)
        right = self.height(root.right)

        if abs(left - right) > 1:
            self.Balanced = False

        return max(left, right) + 1

    def isBalanced(self, root):

        self.height(root)

        return self.Balanced
```

---

# How This Works

Consider:

```text
        1
       / \
      2   3
     / \
    4   5
```

Start:

```text
Balanced = True
```

---

## Node 4

```text
left = 0
right = 0
```

Difference:

```text
0
```

Balanced.

Return:

```text
height = 1
```

---

## Node 5

Same:

```text
left = 0
right = 0
```

Return:

```text
height = 1
```

---

## Node 2

Now:

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

## Node 3

Leaf node:

```text
height = 1
```

---

## Node 1

Now:

```text
left = 2
right = 1
```

Difference:

```text
|2 - 1| = 1
```

Still balanced.

So:

```text
Balanced = True
```

Final answer:

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

Initially:

```text
Balanced = True
```

### Node 3

```text
left = 0
right = 0
```

Return:

```text
height = 1
```

### Node 2

```text
left = 1
right = 0

difference = 1
```

Still balanced.

Return:

```text
height = 2
```

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

we execute:

```python
self.Balanced = False
```

So:

```text
Balanced = False
```

Final:

```python
return self.Balanced
```

Answer:

```text
False
```

---

# Important: Why Don't We Stop Immediately?

Suppose we find:

```python
self.Balanced = False
```

The recursive function still returns height.

For example:

```python
if abs(left - right) > 1:
    self.Balanced = False

return max(left, right) + 1
```

Why?

Because the purpose of `height()` is still to calculate the height needed by its parent.

So it has two responsibilities:

```text
1. Calculate height
2. Update Balanced if needed
```

Once:

```text
Balanced = False
```

it stays false.

---

# Important Improvement to Your Code

Your code has:

```python
class Solution:
    Balanced = True
```

This creates a **class-level variable**.

A safer approach is to reset it inside `isBalanced()`:

```python
class Solution:

    def height(self, root):

        if root is None:
            return 0

        left = self.height(root.left)
        right = self.height(root.right)

        if abs(left - right) > 1:
            self.Balanced = False

        return max(left, right) + 1

    def isBalanced(self, root):

        self.Balanced = True

        self.height(root)

        return self.Balanced
```

The important line is:

```python
self.Balanced = True
```

inside `isBalanced()`.

This ensures every new call starts with:

```text
Balanced = True
```

---

# Why Is This Approach O(n)?

Every node is visited exactly once.

At every node we do constant work:

```text
1. Get left height
2. Get right height
3. Calculate difference
4. Update flag if needed
5. Return height
```

There is no repeated height calculation.

Therefore:

```text
Time = O(n)
```

Space comes from recursion:

```text
Space = O(h)
```

where `h` is the height of the tree.

---

# Approach 3: Optimized DFS + `-1` Sentinel

There is another optimized approach that combines:

```text
Height
+
Balance Status
```

into a single return value.

Instead of using:

```python
self.Balanced
```

we return:

```text
positive value → height
-1              → unbalanced
```

So:

```text
-1
```

acts as a special signal.

---

# Why Return `-1`?

Normally, height is:

```text
0, 1, 2, 3, ...
```

Therefore we can safely use:

```text
-1
```

to mean:

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

Node `1` eventually receives:

```text
left = -1
```

which means:

```text
The left subtree is already unbalanced.
```

So it immediately returns:

```text
-1
```

---

# Optimized Code Using `-1`

```python
class Solution:

    def isBalanced(self, root):

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

# Boolean Flag vs `-1` Sentinel

Both approaches have:

```text
Time  = O(n)
Space = O(h)
```

But they handle the information differently.

### Boolean Flag

```text
height() → returns height

self.Balanced → stores whether tree is balanced
```

So information is stored in two places.

### `-1` Sentinel

```text
dfs() → returns either:

positive number → height
-1              → unbalanced
```

So both pieces of information are combined into one return value.

---

# Which One Should I Prefer?

For learning:

```text
Boolean Flag
```

is easier to understand initially.

You can think:

```text
height()
    ↓
calculate height

self.Balanced
    ↓
remember whether imbalance occurred
```

For interviews, the `-1` sentinel version is usually cleaner because:

```text
one return value
    ↓
height OR unbalanced
```

It also allows **early stopping**.

For example:

```python
left = dfs(root.left)

if left == -1:
    return -1
```

There is no need to process the right subtree once the left subtree is already unbalanced.

---

# Important Interview Pattern

This is a very common tree pattern:

```text
Child returns useful information
            ↓
Parent uses that information
            ↓
Parent returns updated information
```

For Balanced Binary Tree:

```text
Child
  ↓
returns height
  ↓
Parent calculates difference
  ↓
Parent returns height
```

Optimized version:

```text
Child
  ↓
height OR -1
  ↓
Parent
```

This pattern appears in many tree problems.

---

# Why Postorder DFS?

We need:

```text
left height
right height
```

before we can check:

```text
abs(left - right)
```

Therefore:

```text
Left
 ↓
Right
 ↓
Root
```

This is:

```text
Postorder DFS
```

Whenever the parent needs information from both children before making a decision, think:

```text
Postorder DFS
```

---

# Complexity Comparison

| Approach | Idea | Time | Space |
|---|---|---:|---:|
| Basic | Recalculate height at every node | O(n²) | O(h) |
| Boolean Flag | Height + `self.Balanced` in one DFS | O(n) | O(h) |
| `-1` Sentinel | Height + balance status in return value | O(n) | O(h) |

---

# Common Mistakes

## 1. Checking Only the Root

Wrong:

```text
Check height difference only at root.
```

A subtree can be unbalanced even if the root looks balanced.

The condition must hold for:

```text
EVERY NODE
```

---

## 2. Recalculating Height

If you do:

```python
getHeight(root.left)
getHeight(root.right)
```

at every node, you repeatedly visit the same nodes.

This leads to:

```text
O(n²)
```

---

## 3. Forgetting `+1`

Height of current node is:

```python
max(left, right) + 1
```

The `+1` represents the current node.

---

## 4. Confusing Height With Balance

Height answers:

```text
How tall is this subtree?
```

Balance answers:

```text
Is this subtree balanced?
```

The optimized approaches combine these two pieces of information.

---

## 5. Not Resetting `self.Balanced`

If using:

```python
self.Balanced
```

initialize it inside:

```python
def isBalanced(self, root):
    self.Balanced = True
```

This makes every call start fresh.

---

# Pattern Recognition

When you see:

> Check whether a binary tree is balanced.

Think:

```text
Need left height
+
Need right height
        ↓
Postorder DFS
        ↓
Check:
abs(left - right) <= 1
```

For optimization:

```text
Can I calculate height
and balance in the same DFS?
        ↓
YES
        ↓
O(n)
```

Two ways:

```text
Option 1:
Height + Boolean Flag

Option 2:
Height OR -1
```

---

# Revision Cheat Sheet

```text
Balanced Binary Tree

Condition:

abs(left_height - right_height) <= 1

This must be true for EVERY node.

Pattern:

Binary Tree + Postorder DFS + Height

--------------------------------------------------

Basic Approach:

For every node:

1. Calculate left height.
2. Calculate right height.
3. Check balance.
4. Recursively check both subtrees.

Problem:

Height is calculated repeatedly.

Time  → O(n²)
Space → O(h)

--------------------------------------------------

Optimized Approach 1:

Height + Boolean Flag

self.Balanced = True

At every node:

left = height(left)
right = height(right)

if abs(left - right) > 1:
    self.Balanced = False

return max(left, right) + 1

Time  → O(n)
Space → O(h)

Important:

Set:

self.Balanced = True

inside isBalanced().

--------------------------------------------------

Optimized Approach 2:

Height + -1 Sentinel

DFS returns:

positive value → subtree height
-1             → subtree unbalanced

At every node:

left = dfs(left)

if left == -1:
    return -1

right = dfs(right)

if right == -1:
    return -1

if abs(left - right) > 1:
    return -1

return max(left, right) + 1

Time  → O(n)
Space → O(h)

--------------------------------------------------

Why Postorder?

Parent needs child heights first.

Left → Right → Root

--------------------------------------------------

Why O(h) Space?

Recursion call stack stores
the current root-to-leaf path.

Balanced tree:
h = O(log n)

Skewed tree:
h = O(n)
```

# One-Line Pattern

```text
Balanced Tree → Postorder DFS → Get left/right heights → Check difference → Return height + balance information
```

# Interview Memory Trick

```text
Basic:
"Height baar-baar nikal raha hai"
        ↓
O(n²)

Optimized:
"Height ek hi DFS me nikal do"
        ↓
O(n)

Two ways:
1. Height + Boolean Flag
2. Height OR -1
```