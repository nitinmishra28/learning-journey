# Top View of Binary Tree

## Problem

Given a binary tree, return the nodes visible when the tree is viewed from the **top**.

For every **horizontal distance**, we need to select the **first node encountered**.

### Example

```text
          1
        /   \
       2     3
      / \   / \
     4   5 6   7
```

Top view:

```text
[4, 2, 1, 3, 7]
```

From the top:

```text
        4
         \
          2
           \
            1
             \
              3
               \
                7
```

Nodes `5` and `6` are hidden behind nodes `2` and `3`.

---

# Pattern

```text
Binary Tree + BFS + Horizontal Distance + Hash Map
```

---

# Main Idea

The important concept in Top View is:

```text
Horizontal Distance (HD)
```

We assign every node a horizontal distance from the root.

The root starts at:

```text
HD = 0
```

For every node:

```text
Left child  → HD - 1
Right child → HD + 1
```

Example:

```text
              1
            HD 0
           /    \
       HD -1    HD +1
          2       3
         / \     / \
    HD -2  HD 0 HD 0 HD +2
       4     5   6    7
```

---

# Why Do We Store Horizontal Distance?

This is the **most important concept** in Top View.

Nodes can exist at the same depth but still appear at different horizontal positions.

For example:

```text
          1
        /   \
       2     3
      / \   / \
     4   5 6   7
```

Horizontal distances:

```text
4 → -2
2 → -1
1 →  0
5 →  0
6 →  0
3 → +1
7 → +2
```

Notice:

```text
1, 5, 6
```

can have the same horizontal distance:

```text
HD = 0
```

But from the top, only:

```text
1
```

is visible.

Therefore, for each horizontal distance:

```text
Store only the FIRST node encountered.
```

---

# Why Do We Use BFS?

We use:

```text
BFS = Level Order Traversal
```

because BFS visits nodes:

```text
Top → Bottom
```

So the first node we encounter at a particular horizontal distance is automatically the **topmost node** at that horizontal distance.

This is the key reason BFS works naturally for Top View.

---

# Why Not DFS?

DFS can also solve Top View, but we need to explicitly track:

```text
depth
```

and compare which node is higher.

With BFS:

```text
First node at an HD
=
Topmost node at that HD
```

So BFS makes the logic simpler.

---

# Data Structures Used

We use three important things:

### 1. Queue

```python
queue = deque()
```

Used for BFS traversal.

Each queue element contains:

```text
(node, horizontal_distance)
```

Example:

```python
queue.append((root, 0))
```

---

### 2. Hash Map

```python
position = {}
```

It stores:

```text
horizontal distance → first node at that distance
```

Example:

```text
position = {
    -2: 4,
    -1: 2,
     0: 1,
     1: 3,
     2: 7
}
```

---

### 3. Answer Array

Finally, we need to return nodes from:

```text
left → right
```

So we sort the horizontal distances.

```python
for hd in sorted(position):
    ans.append(position[hd])
```

---

# Why `HD - 1` for Left?

If a node moves to the left:

```text
HD decreases by 1
```

So:

```python
queue.append((node.left, hd - 1))
```

Example:

```text
        1
       /
      2
```

Then:

```text
1 → HD 0
2 → HD -1
```

---

# Why `HD + 1` for Right?

If a node moves to the right:

```text
HD increases by 1
```

So:

```python
queue.append((node.right, hd + 1))
```

Example:

```text
1
 \
  3
```

Then:

```text
1 → HD 0
3 → HD +1
```

---

# Why Do We Store Only If `hd not in position`?

Code:

```python
if hd not in position:
    position[hd] = node.data
```

This means:

```text
If this horizontal distance has never been seen,
store this node.
```

If the HD already exists:

```text
Don't replace it.
```

Why?

Because BFS guarantees that the first node found at that HD is the **topmost** node.

---

# Example of Duplicate HD

Consider:

```text
          1
        /   \
       2     3
        \   /
         5 6
```

Horizontal distances:

```text
2 → -1
1 →  0
3 → +1
5 →  0
6 →  0
```

When BFS reaches:

```text
1
```

we store:

```text
HD 0 → 1
```

Later we encounter:

```text
5
```

with:

```text
HD 0
```

But:

```python
0 in position
```

so we don't replace `1`.

Therefore:

```text
HD 0 → 1
```

which is correct.

---

# Code

```python
from collections import deque

class Solution:

    def topView(self, root):

        if root is None:
            return []

        ans = []
        queue = deque()

        # (node, horizontal distance)
        queue.append((root, 0))

        position = {}

        while queue:

            node, hd = queue.popleft()

            # Store only the first node at this HD
            if hd not in position:
                position[hd] = node.data

            # Left child → HD - 1
            if node.left:
                queue.append((node.left, hd - 1))

            # Right child → HD + 1
            if node.right:
                queue.append((node.right, hd + 1))

        # Sort HD from left to right
        for hd in sorted(position):
            ans.append(position[hd])

        return ans
```

---

# Dry Run

Consider:

```text
          1
        /   \
       2     3
      / \   / \
     4   5 6   7
```

Start:

```text
queue = [(1, 0)]
position = {}
```

---

## Step 1: Node 1

Remove:

```text
(1, 0)
```

HD:

```text
0
```

Not present in map.

Store:

```text
position[0] = 1
```

Add children:

```text
2 → HD -1
3 → HD +1
```

Queue:

```text
[(2, -1), (3, 1)]
```

---

## Step 2: Node 2

Remove:

```text
(2, -1)
```

HD `-1` doesn't exist.

Store:

```text
position[-1] = 2
```

Add:

```text
4 → HD -2
5 → HD 0
```

Queue:

```text
[(3, 1), (4, -2), (5, 0)]
```

---

## Step 3: Node 3

Remove:

```text
(3, 1)
```

Store:

```text
position[1] = 3
```

Add:

```text
6 → HD 0
7 → HD 2
```

Queue:

```text
[(4, -2), (5, 0), (6, 0), (7, 2)]
```

---

## Step 4: Node 4

HD:

```text
-2
```

Not present.

Store:

```text
position[-2] = 4
```

---

## Step 5: Node 5

HD:

```text
0
```

But:

```text
position[0] = 1
```

already exists.

So:

```text
Don't replace 1 with 5.
```

---

## Step 6: Node 6

HD:

```text
0
```

Again already exists.

Don't store.

---

## Step 7: Node 7

HD:

```text
2
```

Not present.

Store:

```text
position[2] = 7
```

Final map:

```text
{
    -2: 4,
    -1: 2,
     0: 1,
     1: 3,
     2: 7
}
```

---

# Why Do We Sort `position`?

The dictionary does not represent the answer order.

We have:

```text
HD → Node
```

For example:

```text
{
    0: 1,
    -1: 2,
    1: 3,
    -2: 4,
    2: 7
}
```

But we need:

```text
Left → Right
```

Therefore we sort the horizontal distances:

```text
-2, -1, 0, 1, 2
```

Then:

```text
4, 2, 1, 3, 7
```

So:

```python
for hd in sorted(position):
    ans.append(position[hd])
```

---

# Why Is BFS Important Here?

Suppose two nodes have the same HD:

```text
          1
        /   \
       2     3
        \   /
         5 6
```

Both:

```text
5 → HD 0
6 → HD 0
```

But `1` is already at:

```text
HD 0
```

BFS processes:

```text
Level 0
↓
Level 1
↓
Level 2
```

So the higher node is encountered first.

Therefore:

```text
First node at each HD = topmost node
```

---

# Brute Force / DFS Approach

We can also solve Top View using DFS.

But with DFS, we cannot simply say:

```text
First node at HD
```

because DFS does not guarantee that the first node encountered is the highest node.

Therefore, we need to store:

```text
horizontal distance
+
depth
+
node value
```

For each HD, keep the node having the smallest depth.

---

# DFS Code

```python
class Solution:

    def topView(self, root):

        if root is None:
            return []

        position = {}

        def solve(node, hd, depth):

            if node is None:
                return

            # Store if HD is new
            # or current node is higher
            if hd not in position or depth < position[hd][0]:
                position[hd] = (depth, node.data)

            solve(node.left, hd - 1, depth + 1)
            solve(node.right, hd + 1, depth + 1)

        solve(root, 0, 0)

        ans = []

        for hd in sorted(position):
            ans.append(position[hd][1])

        return ans
```

---

# BFS vs DFS

| Approach | Main Idea | Time | Auxiliary Space |
|---|---|---:|---:|
| BFS | First node at every HD | O(n log n) with sorting | O(n) |
| DFS | Store minimum depth for every HD | O(n log n) with sorting | O(h + n) |

The BFS approach is generally easier to understand for Top View because:

```text
BFS = top to bottom
```

and therefore:

```text
First node at HD = topmost node
```

---

# Why Do We Need Both HD and BFS?

This is a common interview question.

### HD tells us:

```text
Where is the node horizontally?
```

### BFS tells us:

```text
Which node is on top?
```

Together:

```text
Horizontal Distance
+
BFS
=
Top View
```

---

# Top View vs Left View vs Right View

These problems look similar but use different concepts.

### Left View

```text
DFS
Level
Left → Right

First node at every level
```

### Right View

```text
DFS
Level
Right → Left

First node at every level
```

### Top View

```text
BFS
Horizontal Distance

First node at every HD
```

This distinction is very important for interviews.

---

# Top View vs Boundary Traversal

Don't confuse them.

### Boundary Traversal

Collects:

```text
Root
+
Left Boundary
+
Leaves
+
Right Boundary
```

### Top View

Collects:

```text
First/topmost node
for every horizontal distance
```

They are completely different concepts.

---

# Common Mistakes

## 1. Storing Every Node at an HD

Wrong:

```python
position[hd] = node.data
```

for every node.

This can overwrite the topmost node.

Correct:

```python
if hd not in position:
    position[hd] = node.data
```

---

## 2. Using Depth Instead of HD

Top View is not based on:

```text
level
```

It is based on:

```text
horizontal distance
```

Remember:

```text
Left → HD - 1
Right → HD + 1
```

---

## 3. Forgetting to Sort HD

The dictionary represents:

```text
HD → Node
```

We need the final answer from:

```text
left → right
```

So:

```python
sorted(position)
```

is required.

---

## 4. Using DFS Without Depth

DFS does not naturally guarantee:

```text
topmost node first
```

If using DFS, track:

```text
depth
```

and keep the node with the smallest depth for each HD.

---

## 5. Confusing Top View With Level Order

Level order gives:

```text
every node
```

Top view gives:

```text
only one node per horizontal distance
```

---

# Complexity

Let:

```text
n = number of nodes
```

BFS visits every node once:

```text
O(n)
```

We also sort the horizontal distances.

There can be at most `n` unique horizontal distances:

```text
O(n log n)
```

Therefore:

```text
Time → O(n log n)
```

The queue can contain up to:

```text
O(n)
```

nodes in the worst case.

The hash map also stores at most:

```text
O(n)
```

entries.

Therefore:

```text
Auxiliary Space → O(n)
```

---

# Can We Get O(n)?

Yes, if we avoid sorting by tracking:

```text
minimum HD
maximum HD
```

and then iterate through that range.

However, the standard and clean solution usually uses:

```python
sorted(position)
```

because it is simple and robust.

For interview purposes, remember:

```text
BFS + Hash Map + Sorting
→ O(n log n)
```

---

# Revision Cheat Sheet

```text
TOP VIEW OF BINARY TREE

Pattern:
BFS + Horizontal Distance + Hash Map

--------------------------------------------------

Horizontal Distance:

Root:
HD = 0

Left child:
HD - 1

Right child:
HD + 1

--------------------------------------------------

Why store HD?

Because Top View depends on
horizontal position.

Nodes with the same HD
are on the same vertical line.

--------------------------------------------------

Why BFS?

BFS visits:

Top → Bottom

Therefore the FIRST node
found at an HD is the
topmost node at that HD.

--------------------------------------------------

Hash Map:

position[hd] = node.data

Store only:

if hd not in position

Because the first node
is the visible one.

--------------------------------------------------

Final Answer:

Sort HD:

sorted(position)

Then read values:

left → right

--------------------------------------------------

Example:

HD:
-2  -1   0   1   2

Node:
 4   2   1   3   7

Answer:

[4, 2, 1, 3, 7]

--------------------------------------------------

Top View:

BFS + HD

Left View:

DFS + Level + Left first

Right View:

DFS + Level + Right first

Boundary:

Root + Left Boundary +
Leaves + Reverse Right Boundary

--------------------------------------------------

Complexity:

Time → O(n log n)
Space → O(n)

--------------------------------------------------

Memory Trick:

TOP VIEW

"Give every node a horizontal
distance. Using BFS, keep the
FIRST node seen at each distance."
```

---

# One-Line Pattern

```text
For Top View, assign horizontal distance (left = -1, right = +1), use BFS so the topmost node is encountered first, store only the first node for each HD, and sort HDs to get the answer from left to right.
```

# Most Important Interview Point

```text
Why HD?
→ It tells us which vertical line the node belongs to.

Why BFS?
→ It processes nodes from top to bottom.

Why first node only?
→ The first node at an HD is the topmost visible node.

Why sort?
→ To return the vertical lines from left to right.
```