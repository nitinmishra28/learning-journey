# Right Side View of Binary Tree

## Problem

Given a binary tree, return the nodes visible when the tree is viewed from the **right side**.

For every level, we need to return the **first node encountered from the right side**.

### Example

```text
          1
        /   \
       2     3
      / \     \
     4   5     6
```

Right side view:

```text
[1, 3, 6]
```

Why?

```text
Level 0 → 1
Level 1 → 3
Level 2 → 6
```

---

# Pattern

```text
Binary Tree + DFS + Level Tracking
```

---

# Main Idea

The idea is exactly the same as the **Left View**.

The only important difference is:

```text
For Left View:
    Visit LEFT first

For Right View:
    Visit RIGHT first
```

We perform DFS and maintain:

```python
level
```

`level` represents the depth of the current node.

We also maintain:

```python
ans
```

where:

```text
ans[level]
```

stores the node already selected for that level.

The important condition is:

```python
if level == len(ans):
```

This means:

```text
This is the FIRST node encountered at this level.
```

Since we visit the right subtree first, this first node is the **rightmost node**.

---

# Why Does This Give the Right View?

We use:

```python
self.solve(root.right, level + 1, ans)
self.solve(root.left, level + 1, ans)
```

So the traversal order is:

```text
RIGHT → LEFT
```

Therefore, at every level:

```text
Rightmost node is encountered first.
```

Once that level already has an answer, we don't add another node.

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
ans = [1, 3]
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

Now when we reach:

```text
level 2
```

we get:

```text
level == len(ans)

2 == 2
```

So this is the **first node encountered at level 2**.

Because we are traversing:

```text
RIGHT → LEFT
```

this node is the rightmost node.

Therefore we add it.

---

# Why Don't We Add Every Node?

Consider:

```text
          1
        /   \
       2     3
```

DFS order is:

```text
1
3
2
```

For node `3`:

```text
level = 1
len(ans) = 1
```

Therefore:

```text
1 == 1
```

Add `3`.

Now:

```text
ans = [1, 3]
```

When node `2` is visited:

```text
level = 1
len(ans) = 2
```

Therefore:

```text
1 != 2
```

Don't add `2`.

So:

```text
3
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
            ans.append(root.val)

        # Visit right first
        self.solve(root.right, level + 1, ans)

        # Then visit left
        self.solve(root.left, level + 1, ans)


    def rightSideView(self, root):

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

## Node 3

We visit right first.

```text
level = 1
len(ans) = 1
```

Condition:

```text
1 == 1
```

Add:

```text
ans = [1, 3]
```

---

## Node 6

From `3`, we go right.

```text
level = 2
len(ans) = 2
```

Condition:

```text
2 == 2
```

Add:

```text
ans = [1, 3, 6]
```

---

## Node 2

Eventually DFS visits `2`.

```text
level = 1
```

But:

```text
len(ans) = 3
```

Therefore:

```text
1 != 3
```

Don't add `2`.

---

## Node 4

```text
level = 2
len(ans) = 3
```

Don't add.

---

## Node 5

```text
level = 2
len(ans) = 3
```

Don't add.

Final answer:

```text
[1, 3, 6]
```

---

# Why Right Child Is Visited First?

This is the main difference between Left View and Right View.

## Left View

We want:

```text
Leftmost node
```

So:

```python
left
right
```

Traversal:

```text
LEFT → RIGHT
```

The first node at each level becomes the answer.

---

## Right View

We want:

```text
Rightmost node
```

So:

```python
right
left
```

Traversal:

```text
RIGHT → LEFT
```

The first node at each level becomes the answer.

---

# Left View vs Right View

| View | Traversal Order | Selected Node |
|---|---|---|
| Left View | Left → Right | First node at level |
| Right View | Right → Left | First node at level |

The underlying pattern is the same:

```text
DFS + Level Tracking
```

Only the traversal direction changes.

---

# BFS Alternative

We can also solve Right View using **Level Order Traversal (BFS)**.

For every level:

```text
Take the last node.
```

Because BFS processes the complete level from left to right.

---

# BFS Code

```python
from collections import deque

class Solution:

    def rightSideView(self, root):

        if root is None:
            return []

        q = deque([root])
        ans = []

        while q:

            size = len(q)

            for i in range(size):

                node = q.popleft()

                # Last node of this level
                if i == size - 1:
                    ans.append(node.val)

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
| DFS | First node encountered at every level | O(n) | O(h) |
| BFS | Last node of every level | O(n) | O(w) |

Where:

```text
n = number of nodes
h = height of tree
w = maximum width of tree
```

---

# Why DFS Space is `O(h)`?

Your solution uses recursion:

```python
self.solve(...)
```

Every recursive call is stored in the:

```text
Call Stack
```

The maximum number of active recursive calls depends on the height of the tree.

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

we can have:

```text
h = n
```

So worst-case space:

```text
O(n)
```

For a balanced tree:

```text
h = O(log n)
```

so the recursive stack is:

```text
O(log n)
```

---

# Common Mistakes

## 1. Visiting Left Before Right

For Right View, don't do:

```python
self.solve(root.left, ...)
self.solve(root.right, ...)
```

That would give the:

```text
Left View
```

For Right View:

```python
self.solve(root.right, ...)
self.solve(root.left, ...)
```

---

## 2. Adding Every Node

We only need:

```text
One node per level.
```

The condition:

```python
if level == len(ans):
```

ensures that only the first node encountered at each level is stored.

---

## 3. Forgetting `level + 1`

Children are one level deeper:

```python
self.solve(root.right, level + 1, ans)
```

and:

```python
self.solve(root.left, level + 1, ans)
```

---

## 4. Confusing First Node With Rightmost Node

The code doesn't directly find:

```text
rightmost node
```

Instead, it uses:

```text
Right → Left DFS
```

Therefore:

```text
First node encountered at each level
=
Rightmost visible node
```

This is the key trick.

---

# Important Interview Insight

The important concept is:

```text
"First node at every level"
```

The meaning of "first" depends on traversal order.

For Left View:

```text
LEFT → RIGHT

First node
=
Leftmost node
```

For Right View:

```text
RIGHT → LEFT

First node
=
Rightmost node
```

This is a very useful DFS pattern.

---

# Edge Case: Empty Tree

If:

```text
root = None
```

then:

```python
ans = []
```

and `solve()` immediately returns.

Answer:

```text
[]
```

---

# Edge Case: Single Node

Tree:

```text
    1
```

At:

```text
level = 0
```

we have:

```text
len(ans) = 0
```

So:

```text
0 == 0
```

Add:

```text
1
```

Answer:

```text
[1]
```

---

# Edge Case: Right-Skewed Tree

```text
1
 \
  2
   \
    3
     \
      4
```

Right view:

```text
[1, 2, 3, 4]
```

Every node is visible.

---

# Edge Case: Left-Skewed Tree

```text
      1
     /
    2
   /
  3
 /
4
```

Even though there are no right children, the right view is:

```text
[1, 2, 3, 4]
```

Why?

At each level there is only one node.

The algorithm still works because when the right subtree is `None`, DFS eventually explores the left subtree.

---

# Complexity

For the DFS solution:

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

The result contains one node per level:

```text
Output Space → O(h)
```

---

# Revision Cheat Sheet

```text
RIGHT SIDE VIEW OF BINARY TREE

Pattern:
DFS + Level Tracking

Main Idea:

Visit:
RIGHT → LEFT

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

    ans.append(root.val)

Meaning:

"This is the first node
we have seen at this level."

--------------------------------------------------

Why right first?

Because we want the
rightmost node.

DFS order:

Right → Left

Therefore the first node
at each level is the right view.

--------------------------------------------------

Left View:

Left → Right
First node at every level

Right View:

Right → Left
First node at every level

--------------------------------------------------

BFS Alternative:

Process level by level.

Take the LAST node
of every level.

--------------------------------------------------

Complexity:

Time → O(n)
Space → O(h)

where:

n = number of nodes
h = height of tree

--------------------------------------------------

Memory Trick:

RIGHT VIEW

"First node at every level
when traversing RIGHT first."
```

---

# One-Line Pattern

```text
For Right View, perform DFS from right to left and add a node only when its level equals len(ans), because that means it is the first/rightmost node encountered at that level.
```

# Most Important Interview Point

```text
Left View  → DFS Left → Right  → First node of every level
Right View → DFS Right → Left  → First node of every level
```