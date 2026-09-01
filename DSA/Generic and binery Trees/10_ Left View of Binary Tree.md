# Left View of Binary Tree

## Problem

Given a binary tree, return the nodes visible when the tree is viewed from the **left side**.

For every level, we need to return the **first node encountered from the left**.

### Example

```text
          1
        /   \
       2     3
      / \     \
     4   5     6
```

Left view:

```text
[1, 2, 4]
```

Why?

```text
Level 0 → 1
Level 1 → 2
Level 2 → 4
```

---

# Pattern

```text
Binary Tree + DFS + Level Tracking
```

---

# Main Idea

We perform **DFS** and keep track of:

```python
level
```

`level` tells us the depth of the current node.

We also maintain:

```python
ans
```

where:

```text
ans[level]
```

represents the node already selected for that level.

The important condition is:

```python
if level == len(ans):
```

This means:

```text
We are visiting this level for the FIRST time.
```

So we add the current node.

---

# Why Does This Give the Left View?

We visit:

```text
left subtree first
right subtree second
```

Code:

```python
self.solve(root.left, level + 1, ans)
self.solve(root.right, level + 1, ans)
```

Therefore, at every level:

```text
Leftmost node is encountered first.
```

Once that level already has a node in `ans`, we don't add another node.

---

# Understanding `level`

At the root:

```text
level = 0
```

For its children:

```text
level = 1
```

For its grandchildren:

```text
level = 2
```

Example:

```text
          1          level 0
        /   \
       2     3        level 1
      / \     \
     4   5     6      level 2
```

So:

```text
1 → level 0
2 → level 1
3 → level 1
4 → level 2
5 → level 2
6 → level 2
```

---

# Why `level == len(ans)`?

This is the most important line:

```python
if level == len(ans):
```

Suppose:

```text
ans = [1, 2]
```

Then:

```text
len(ans) = 2
```

This means we already have answers for:

```text
level 0
level 1
```

Now if we reach:

```text
level 2
```

then:

```text
level == len(ans)

2 == 2
```

So this is the **first node of level 2**.

We add it:

```python
ans.append(root.data)
```

Now:

```text
ans = [1, 2, 4]
```

---

# Why Don't We Add Every Node?

Consider:

```text
          1
        /   \
       2     3
```

DFS visits:

```text
1
2
3
```

For node `2`:

```text
level = 1
len(ans) = 1
```

Therefore:

```text
1 == 1
```

Add `2`.

Now:

```text
ans = [1, 2]
```

When node `3` is visited:

```text
level = 1
len(ans) = 2
```

Therefore:

```text
1 != 2
```

Don't add `3`.

So only:

```text
2
```

is selected for level 1.

---

# Code

```python
class Solution:

    def solve(self, root, level, ans):

        if root is None:
            return

        # First node encountered at this level
        if level == len(ans):
            ans.append(root.data)

        # Visit left first
        self.solve(root.left, level + 1, ans)

        # Then visit right
        self.solve(root.right, level + 1, ans)


    def leftView(self, root):

        ans = []

        self.solve(root, 0, ans)

        return ans
```

---

# Dry Run

Consider:

```text
          1
        /   \
       2     3
      / \     \
     4   5     6
```

Initially:

```text
ans = []
level = 0
```

---

## Node 1

```text
level = 0
len(ans) = 0
```

Condition:

```text
0 == 0
```

Add:

```text
ans = [1]
```

---

## Node 2

Move left:

```text
level = 1
```

Current:

```text
len(ans) = 1
```

Condition:

```text
1 == 1
```

Add:

```text
ans = [1, 2]
```

---

## Node 4

Move left:

```text
level = 2
```

Current:

```text
len(ans) = 2
```

Condition:

```text
2 == 2
```

Add:

```text
ans = [1, 2, 4]
```

---

## Node 5

Move right from `2`:

```text
level = 2
```

But:

```text
len(ans) = 3
```

So:

```text
2 != 3
```

Don't add `5`.

---

## Node 3

Eventually DFS reaches:

```text
3
```

Its level:

```text
level = 1
```

But:

```text
len(ans) = 3
```

So:

```text
1 != 3
```

Don't add it.

---

## Node 6

Level:

```text
2
```

Again:

```text
2 != 3
```

Don't add it.

Final:

```text
[1, 2, 4]
```

---

# Why Left Child Is Visited First?

This is essential.

We want:

```text
LEFT VIEW
```

So for every level, we want the:

```text
leftmost node
```

Therefore:

```python
self.solve(root.left, ...)
self.solve(root.right, ...)
```

The left subtree is explored first.

The **first node encountered at every level** becomes the answer.

---

# What If We Visit Right First?

If we write:

```python
self.solve(root.right, level + 1, ans)
self.solve(root.left, level + 1, ans)
```

then the first node encountered at every level would be the:

```text
rightmost node
```

That would give the:

```text
Right View
```

So:

```text
Left first  → Left View
Right first → Right View
```

This is a very important interview pattern.

---

# Brute Force / BFS Approach

Another common way is to use **Level Order Traversal (BFS)**.

For every level:

```text
Take the first node.
```

Because BFS processes one complete level at a time.

---

# BFS Code

```python
from collections import deque

class Solution:

    def leftView(self, root):

        if root is None:
            return []

        q = deque([root])
        ans = []

        while q:

            size = len(q)

            for i in range(size):

                node = q.popleft()

                # First node of this level
                if i == 0:
                    ans.append(node.data)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

        return ans
```

---

# DFS vs BFS

| Approach | Idea | Time | Extra Space |
|---|---|---:|---:|
| BFS | First node of every level | O(n) | O(w) |
| DFS | First node encountered at every level | O(n) | O(h) |

Where:

```text
n = number of nodes
w = maximum width
h = height
```

Your solution uses:

```text
DFS
```

and is already:

```text
O(n)
```

---

# Why DFS Space is `O(h)`?

Your solution uses recursion:

```python
self.solve(...)
```

Every recursive call is stored in the:

```text
call stack
```

The maximum number of active calls depends on the height of the tree.

Therefore:

```text
Auxiliary Space = O(h)
```

For a skewed tree:

```text
    1
     \
      2
       \
        3
         \
          4
```

height is:

```text
h = n
```

So worst case:

```text
O(n)
```

For a balanced tree:

```text
h = O(log n)
```

---

# Important Interview Point

The trick is **not** simply:

```text
Go left.
```

The actual idea is:

```text
Visit left before right
+
Keep track of level
+
Store only the first node at each level
```

This pattern can also be used for:

```text
Left View
Right View
Top View variations
Level-based DFS problems
```

---

# Common Mistakes

## 1. Using `level <= len(ans)`

Wrong:

```python
if level <= len(ans):
```

Correct:

```python
if level == len(ans):
```

We only want to add the **first node** of a level.

---

## 2. Visiting Right Before Left

For left view, don't do:

```python
right
left
```

because then the rightmost node will be selected first.

---

## 3. Forgetting `level + 1`

Children are one level deeper:

```python
self.solve(root.left, level + 1, ans)
```

---

## 4. Adding Every Node

We only add:

```text
first node of every level
```

not every node.

---

# Complexity

For your DFS solution:

```text
Time → O(n)
```

Every node is visited once.

Recursive call stack:

```text
Space → O(h)
```

where:

```text
h = height of tree
```

Output array:

```text
O(h)
```

because there is at most one answer per level.

---

# Revision Cheat Sheet

```text
LEFT VIEW OF BINARY TREE

Pattern:
DFS + Level Tracking

Main Idea:

Visit:
LEFT → RIGHT

At every level:
take the FIRST node encountered.

--------------------------------------------------

level:

Root:
0

Child:
1

Grandchild:
2

--------------------------------------------------

Important condition:

if level == len(ans):

    ans.append(root.data)

Meaning:

"This is the first node
we have seen at this level."

--------------------------------------------------

Why left first?

Because we want the
leftmost node.

DFS order:

Left → Right

Therefore the first node
at each level is the left view.

--------------------------------------------------

If we visit right first:

Right → Left

We get the right view.

--------------------------------------------------

Complexity:

Time → O(n)
Space → O(h)

where:

n = number of nodes
h = height of tree

--------------------------------------------------

Memory Trick:

LEFT VIEW

"First node at every level
when traversing LEFT first."

--------------------------------------------------

Key line:

if level == len(ans)

means:

"No answer exists for this
level yet → this is the
leftmost node."
```

---

# One-Line Pattern

```text
For Left View, perform DFS from left to right and add a node only when its level equals len(ans), because that means it is the first node encountered at that level.
```