# Bottom View of Binary Tree

## Problem

Given a binary tree, return the nodes visible when the tree is viewed from the **bottom**.

For every **horizontal distance**, we need to select the **bottommost node**.

### Example

```text
          1
        /   \
       2     3
      / \   / \
     4   5 6   7
```

The horizontal distances are:

```text
4 → -2
2 → -1
1 →  0
5 →  0
6 →  0
3 → +1
7 → +2
```

For `HD = 0`, multiple nodes exist:

```text
1
5
6
```

From the bottom, the last/bottommost node is selected according to the traversal.

Result:

```text
[4, 2, 6, 3, 7]
```

---

# Pattern

```text
Binary Tree + BFS + Horizontal Distance + Hash Map
```

---

# Main Idea

The **Bottom View** is very similar to the **Top View**.

The main difference is:

### Top View

```text
Keep the FIRST node at every HD.
```

### Bottom View

```text
Keep the LAST node encountered at every HD.
```

So instead of:

```python
if hd not in position:
    position[hd] = node.data
```

we simply do:

```python
position[hd] = node.data
```

Every time we encounter a node, we overwrite the previous node.

Therefore, the last node stored for a horizontal distance becomes the bottom-view node.

---

# What is Horizontal Distance?

Horizontal distance tells us the node's horizontal position relative to the root.

Root:

```text
HD = 0
```

Left child:

```text
HD = -1
```

Right child:

```text
HD = +1
```

For every further level:

```text
Left  → HD - 1
Right → HD + 1
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

This is one of the most important concepts.

Top/Bottom View is not based on:

```text
level only
```

It is based on:

```text
vertical columns
```

Horizontal distance identifies those columns.

For example:

```text
          1
        /   \
       2     3
        \   /
         5 6
```

Here:

```text
1 → HD 0
5 → HD 0
6 → HD 0
```

All three nodes are on the same vertical line.

For Bottom View, we need the node that appears at the bottom of that vertical line.

---

# Why Do We Use BFS?

We use:

```text
BFS = Level Order Traversal
```

because BFS processes nodes level by level:

```text
Top → Bottom
```

Therefore, as we process the tree, nodes at greater depths are encountered later.

When we do:

```python
position[hd] = node.data
```

we keep overwriting the previous node.

So eventually:

```text
Last encountered node
=
Bottom View candidate
```

---

# Top View vs Bottom View

This is extremely important for revision.

## Top View

```python
if hd not in position:
    position[hd] = node.data
```

Meaning:

```text
Keep FIRST node.
```

Why?

```text
BFS → Top to Bottom
First node → Topmost
```

---

## Bottom View

```python
position[hd] = node.data
```

Meaning:

```text
Keep LAST node.
```

Why?

```text
BFS → Top to Bottom
Later node → Lower node
```

---

# Top View vs Bottom View

| Property | Top View | Bottom View |
|---|---|---|
| Traversal | BFS | BFS |
| Main concept | Horizontal Distance | Horizontal Distance |
| What to store | First node | Last node |
| Hash Map | Store only once | Keep overwriting |
| Direction | Topmost | Bottommost |

Memory trick:

```text
TOP → Don't replace

BOTTOM → Replace
```

---

# Code

```python
from collections import deque

class Solution:

    def bottomView(self, root):

        if root is None:
            return []

        ans = []
        queue = deque()

        # Store node and horizontal distance
        queue.append((root, 0))

        position = {}

        while queue:

            node, hd = queue.popleft()

            # Always overwrite
            # Last node at this HD remains
            position[hd] = node.data

            # Left child
            if node.left:
                queue.append((node.left, hd - 1))

            # Right child
            if node.right:
                queue.append((node.right, hd + 1))

        # Return from left to right
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

Initially:

```text
queue = [(1, 0)]
position = {}
```

---

## Step 1: Node 1

```text
node = 1
HD = 0
```

Store:

```text
position[0] = 1
```

Queue:

```text
[(2, -1), (3, 1)]
```

---

## Step 2: Node 2

```text
node = 2
HD = -1
```

Store:

```text
position[-1] = 2
```

Add children:

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

```text
node = 3
HD = 1
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

```text
HD = -2
```

Store:

```text
position[-2] = 4
```

---

## Step 5: Node 5

```text
HD = 0
```

Previously:

```text
position[0] = 1
```

Now overwrite:

```text
position[0] = 5
```

---

## Step 6: Node 6

```text
HD = 0
```

Previously:

```text
position[0] = 5
```

Overwrite:

```text
position[0] = 6
```

---

## Step 7: Node 7

```text
HD = 2
```

Store:

```text
position[2] = 7
```

Final map:

```text
{
    -2: 4,
    -1: 2,
     0: 6,
     1: 3,
     2: 7
}
```

Sort HD:

```text
-2, -1, 0, 1, 2
```

Answer:

```text
[4, 2, 6, 3, 7]
```

---

# Why Are We Overwriting?

This line is the heart of the problem:

```python
position[hd] = node.data
```

Suppose:

```text
HD = 0
```

and we encounter:

```text
1
5
6
```

We do:

```text
position[0] = 1
```

then:

```text
position[0] = 5
```

then:

```text
position[0] = 6
```

Final value:

```text
position[0] = 6
```

So:

```text
6
```

is the bottom-view node for that horizontal distance.

---

# Why Do We Sort the Horizontal Distance?

The map may contain:

```text
{
    0: 1,
    -1: 2,
    1: 3,
    -2: 4,
    2: 7
}
```

But the answer must be returned:

```text
Left → Right
```

Therefore we sort:

```python
sorted(position)
```

which gives:

```text
[-2, -1, 0, 1, 2]
```

Then take the corresponding values.

---

# Important Difference: Top View

Top View code:

```python
if hd not in position:
    position[hd] = node.data
```

Why?

Because we want:

```text
FIRST node
```

BFS visits:

```text
Top → Bottom
```

Therefore first = topmost.

---

# Important Difference: Bottom View

Bottom View code:

```python
position[hd] = node.data
```

Why?

Because we want:

```text
LAST node
```

BFS visits:

```text
Top → Bottom
```

Therefore later nodes are lower candidates.

---

# But Why Does BFS Give the Correct Bottom Node?

BFS processes nodes level by level.

Example:

```text
Level 0
↓
Level 1
↓
Level 2
↓
Level 3
```

So a deeper node is processed after a shallower node.

When the same HD appears again:

```python
position[hd] = node.data
```

the deeper node replaces the previous one.

Therefore the final stored node is the bottommost node encountered for that HD.

---

# Important Interview Note

There can be cases where two nodes have:

```text
same HD
same depth
```

In such situations, the exact answer can depend on the traversal/order convention used by the problem.

For the standard Bottom View implementation used in many coding problems, BFS with:

```text
left child → right child
```

and overwriting the HD is the common approach.

Always follow the ordering expected by the specific problem statement.

---

# DFS Approach

Bottom View can also be solved using DFS.

But unlike the simple BFS approach, DFS needs to track:

```text
HD
+
Depth
```

For each HD, store the node having the greatest depth.

---

# DFS Code

```python
class Solution:

    def bottomView(self, root):

        if root is None:
            return []

        position = {}

        def solve(node, hd, depth):

            if node is None:
                return

            # Store if:
            # 1. HD is not present
            # 2. Current node is deeper
            if hd not in position or depth >= position[hd][0]:
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
| BFS | Overwrite every HD | O(n log n) | O(n) |
| DFS | Keep maximum depth for every HD | O(n log n) | O(n + h) |

The BFS solution is generally easier for this problem.

---

# Why BFS is Preferred Here

The problem asks for:

```text
Bottommost node
```

and BFS naturally processes:

```text
Top → Bottom
```

So:

```text
Overwrite every HD
```

is a very clean solution.

With DFS, we need extra information:

```text
depth
```

because DFS does not guarantee that nodes are visited in top-to-bottom order.

---

# Common Mistakes

## 1. Using Top View Logic

Wrong:

```python
if hd not in position:
    position[hd] = node.data
```

That gives:

```text
Top View
```

For Bottom View:

```python
position[hd] = node.data
```

---

## 2. Forgetting Horizontal Distance

Don't use only:

```text
level
```

Bottom View depends on:

```text
horizontal distance
```

---

## 3. Forgetting to Sort

The final answer must be:

```text
Left → Right
```

So:

```python
sorted(position)
```

is required.

---

## 4. Using DFS Without Depth

DFS does not naturally guarantee the bottommost node will be encountered last.

If using DFS, store:

```text
depth
```

and keep the node with the greatest depth.

---

## 5. Confusing Bottom View With Right View

Right View:

```text
One node per LEVEL
```

Bottom View:

```text
One node per HORIZONTAL DISTANCE
```

These are different.

---

# Top View vs Bottom View vs Right View

This distinction is extremely important for interviews.

### Top View

```text
BFS
+
Horizontal Distance
+
First node at each HD
```

### Bottom View

```text
BFS
+
Horizontal Distance
+
Last node at each HD
```

### Right View

```text
DFS/BFS
+
Level
+
Rightmost node at each level
```

---

# Top View vs Bottom View Example

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

### Top View

At `HD = 0`:

```text
1
```

is the first/topmost node.

So:

```text
Top View = [2, 1, 3]
```

### Bottom View

At `HD = 0`:

```text
1 → 5 → 6
```

The last/bottom candidate is:

```text
6
```

So:

```text
Bottom View = [2, 6, 3]
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

Sorting the horizontal distances:

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

nodes.

The hash map can also contain up to:

```text
O(n)
```

unique horizontal distances.

Therefore:

```text
Auxiliary Space → O(n)
```

---

# Can We Avoid Sorting?

Yes.

We can maintain:

```text
minHD
maxHD
```

while traversing.

Then iterate from:

```text
minHD → maxHD
```

instead of sorting the keys.

But the standard implementation:

```python
for hd in sorted(position):
```

is simpler and usually preferred in interviews unless O(n) time is specifically required.

---

# Revision Cheat Sheet

```text
BOTTOM VIEW OF BINARY TREE

Pattern:
BFS + Horizontal Distance + Hash Map

--------------------------------------------------

Horizontal Distance:

Root:
HD = 0

Left:
HD - 1

Right:
HD + 1

--------------------------------------------------

Why HD?

Top/Bottom View depends on
vertical columns, not levels.

Same HD = Same vertical line.

--------------------------------------------------

Why BFS?

BFS processes:

Top → Bottom

So nodes encountered later
are lower-level candidates.

--------------------------------------------------

Bottom View:

Always overwrite:

position[hd] = node.data

Therefore:

LAST node at each HD
remains.

--------------------------------------------------

Top View:

if hd not in position:
    position[hd] = node.data

Therefore:

FIRST node at each HD
remains.

--------------------------------------------------

Final Answer:

Sort HD:

sorted(position)

Then read:

Left → Right

--------------------------------------------------

Top View:

BFS + HD + FIRST

Bottom View:

BFS + HD + LAST

Right View:

Level + RIGHTMOST

Left View:

Level + LEFTMOST

--------------------------------------------------

Complexity:

Time → O(n log n)
Space → O(n)

--------------------------------------------------

Memory Trick:

TOP:
Don't Replace

BOTTOM:
Replace

```

---

# One-Line Pattern 

```text
For Bottom View, assign every node a horizontal distance, use BFS, overwrite the value for every HD so the bottommost candidate remains, and sort the HDs to return the result from left to right. 
``` 

# Most Important Interview Points

```text
Why HD?
→ Identifies the vertical column of a node.

Why BFS?
→ Processes nodes level by level from top to bottom.

Why overwrite?
→ We want the bottommost node, so later nodes replace earlier ones.

Why sort?
→ Horizontal distances must be returned from left to right.

Top View:
→ Keep FIRST node at every HD.

Bottom View:
→ Keep LAST node at every HD.

Right View:
→ Keep RIGHTMOST node at every level.

Left View:
→ Keep LEFTMOST node at every level.
```