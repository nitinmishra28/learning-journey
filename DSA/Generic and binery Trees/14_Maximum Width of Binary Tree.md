# Maximum Width of Binary Tree

## Problem

Given a binary tree, find its **maximum width**.

The width of a level is calculated as:

```text
Rightmost Position - Leftmost Position + 1
```

Important:

> We count the positions of the missing nodes between the leftmost and rightmost nodes as well.

### Example

```text
              1
            /   \
           2     3
          /       \
         4         7
```

If we imagine the complete binary tree positions:

```text
              1
           /     \
          2       3
        /  \     /  \
       4    -   -    7
```

The last level has:

```text
4  -  -  7
```

Therefore:

```text
Width = 4
```

Answer:

```text
4
```

---

# Pattern

```text
Binary Tree + BFS + Complete Binary Tree Indexing
```

---

# Main Idea

The tricky part of this problem is:

```text
How do we count the missing nodes?
```

Normal BFS only stores existing nodes.

For example:

```text
          1
        /   \
       2     3
      /       \
     4         7
```

Normal BFS at the last level sees only:

```text
4, 7
```

and might think:

```text
width = 2
```

But the actual positions are:

```text
4, _, _, 7
```

so:

```text
width = 4
```

To solve this, we assign every node an **index** as if the tree were a complete binary tree.

---

# Complete Binary Tree Indexing

We start the root with:

```text
index = 1
```

For a node at index `i`:

```text
Left child  = 2 * i
Right child = 2 * i + 1
```

Example:

```text
              1
            /   \
           2     3
          / \   / \
         4   5 6   7
```

Indexes:

```text
              1
            /   \
           2     3
          / \   / \
         4   5 6   7
```

This gives every possible position a unique index.

---

# Why Are We Storing Index?

This is the **most important point** of this problem.

Suppose:

```text
          1
        /   \
       2     3
      /       \
     4         7
```

The last level contains:

```text
4             7
```

If we only store nodes:

```text
[4, 7]
```

we don't know how many missing positions exist between them.

But with indexes:

```text
4 → index 4
7 → index 7
```

Now:

```text
width = 7 - 4 + 1
      = 4
```

So the index allows us to automatically count:

```text
existing nodes
+
missing nodes
```

between the two boundary nodes.

---

# Why `+1` in Width Formula?

The formula is:

```python
rightMostNodeIndex - leftMostNodeIndex + 1
```

Suppose:

```text
left = 4
right = 7
```

Positions are:

```text
4, 5, 6, 7
```

Number of positions:

```text
7 - 4 + 1 = 4
```

Without `+1`:

```text
7 - 4 = 3
```

which is incorrect.

### Simple Example

If:

```text
left = 5
right = 5
```

There is one node.

Formula:

```text
5 - 5 + 1
= 1
```

So:

```text
Width = right - left + 1
```

---

# Why Do We Use BFS?

We need to calculate width **level by level**.

BFS naturally processes:

```text
Level 0
Level 1
Level 2
Level 3
...
```

For each level we can get:

```python
queue[0]
```

which is the leftmost node.

And:

```python
queue[-1]
```

which is the rightmost node.

Therefore:

```python
leftMostNodeIndex = queue[0][1]
rightMostNodeIndex = queue[-1][1]
```

---

# Why Does `queue[0]` Give the Leftmost Node?

Because BFS stores nodes of the current level from:

```text
left → right
```

So the first element of the queue is the leftmost node of that level.

Similarly:

```python
queue[-1]
```

is the rightmost node of the current level.

---

# Code

```python
from collections import deque

class Solution:

    def widthOfBinaryTree(self, root):

        if root is None:
            return 0

        queue = deque()

        # Store (node, index)
        queue.append((root, 1))

        maxWidth = 1

        while queue:

            # Number of nodes in current level
            size = len(queue)

            # Leftmost node index
            leftMostNodeIndex = queue[0][1]

            # Rightmost node index
            rightMostNodeIndex = queue[-1][1]

            # Width of current level
            currentLevelWidth = (
                rightMostNodeIndex - leftMostNodeIndex + 1
            )

            # Update maximum width
            maxWidth = max(maxWidth, currentLevelWidth)

            # Process current level
            for i in range(size):

                node, index = queue.popleft()

                # Left child
                if node.left:
                    queue.append((node.left, 2 * index))

                # Right child
                if node.right:
                    queue.append((node.right, 2 * index + 1))

        return maxWidth
```

---

# Dry Run

Consider:

```text
              1
            /   \
           2     3
          /       \
         4         7
```

Assign indexes:

```text
              1
            /   \
           2     3
          /       \
         4         7
```

---

## Level 0

Queue:

```text
[(1, 1)]
```

Left index:

```text
1
```

Right index:

```text
1
```

Width:

```text
1 - 1 + 1
= 1
```

So:

```text
maxWidth = 1
```

Children:

```text
2 → index 2
3 → index 3
```

Queue:

```text
[(2, 2), (3, 3)]
```

---

## Level 1

Left index:

```text
2
```

Right index:

```text
3
```

Width:

```text
3 - 2 + 1
= 2
```

Update:

```text
maxWidth = 2
```

Now process children.

Node `2`:

```text
left child 4 → index 4
```

Node `3`:

```text
right child 7 → index 7
```

Queue:

```text
[(4, 4), (7, 7)]
```

---

## Level 2

Left index:

```text
4
```

Right index:

```text
7
```

Width:

```text
7 - 4 + 1
= 4
```

Notice that only two nodes exist:

```text
4       7
```

But their positions are:

```text
4, 5, 6, 7
```

So:

```text
Width = 4
```

Update:

```text
maxWidth = 4
```

Final answer:

```text
4
```

---

# Why Are Missing Nodes Counted?

This is what makes this problem different from normal level-order traversal.

Consider:

```text
          1
        /   \
       2     3
      /       \
     4         7
```

At the last level:

```text
4  _  _  7
```

The missing nodes still occupy positions.

Using indexes:

```text
4 → position 4
7 → position 7
```

Therefore:

```text
4, 5, 6, 7
```

contains 4 positions.

So:

```text
width = 4
```

---

# Why `maxWidth = 1` Initially?

If the tree is not empty:

```text
root
```

it already contains at least one node.

Therefore the minimum possible width is:

```text
1
```

So:

```python
maxWidth = 1
```

is safe.

If we initialized:

```python
maxWidth = 0
```

it would also work because the first level would update it to `1`.

But:

```python
maxWidth = 1
```

directly represents the fact that a non-empty tree has at least width `1`.

---

# Why Start Index From `1`?

We use:

```python
queue.append((root, 1))
```

because the complete binary tree indexing becomes:

```text
             1
           /   \
          2     3
         / \   / \
        4   5 6   7
```

You could also start from:

```text
0
```

using:

```text
left  = 2*i + 1
right = 2*i + 2
```

But starting from `1` makes the formulas simpler:

```text
left  = 2*i
right = 2*i + 1
```

---

# Brute Force Approach

A simple approach is to perform level-order traversal and try to represent the missing positions explicitly.

For every level, we can keep `None` placeholders for missing children.

For example:

```text
          1
        /   \
       2     3
      /       \
     4         7
```

We could represent the last level as:

```text
[4, None, None, 7]
```

Then:

```text
width = 4
```

---

# Brute Force Code

```python
from collections import deque

class Solution:

    def widthOfBinaryTree(self, root):

        if root is None:
            return 0

        q = deque([root])
        maxWidth = 0

        while q:

            # Remove unnecessary None values
            while q and q[0] is None:
                q.popleft()

            while q and q[-1] is None:
                q.pop()

            if not q:
                break

            # Current level width
            maxWidth = max(maxWidth, len(q))

            size = len(q)

            for i in range(size):

                node = q.popleft()

                if node is None:
                    q.append(None)
                    q.append(None)
                else:
                    q.append(node.left)
                    q.append(node.right)

        return maxWidth
```

This approach is mainly useful for understanding the concept.

The problem is that we explicitly create:

```text
None
None
None
...
```

for missing positions.

For a sparse tree, this can create a huge number of unnecessary placeholders.

Therefore, it is not a good practical solution.

---

# Why Indexing Is Better

Instead of storing:

```text
4, None, None, 7
```

we store:

```text
4 → index 4
7 → index 7
```

Then calculate:

```text
7 - 4 + 1
= 4
```

We don't need to physically create the missing nodes.

This is the main optimization.

---

# Brute Force vs Optimized

| Approach | Idea | Time | Space |
|---|---|---:|---:|
| Brute Force | Explicitly maintain missing positions | Can become very large | Can become very large |
| Indexing + BFS | Store position/index instead of `None` nodes | O(n) | O(n) |

The optimized approach is the one you should remember for interviews.

---

# Important: Why Isn't the Queue Size Enough?

This is a very common mistake.

You might think:

```python
len(queue)
```

gives the width.

But consider:

```text
          1
        /   \
       2     3
      /       \
     4         7
```

At the last level:

```text
queue = [4, 7]
```

So:

```text
len(queue) = 2
```

But actual width is:

```text
4
```

because:

```text
4 _ _ 7
```

Therefore:

```text
Queue size ≠ Width
```

We need indexes to account for missing positions.

---

# Important Formula

For every level:

```python
width = rightIndex - leftIndex + 1
```

Remember:

```text
R - L + 1
```

Example:

```text
L = 4
R = 7

Width = 7 - 4 + 1
      = 4
```

---

# Potential Index Growth

In a very deep tree, values like:

```text
2 * index
```

can become very large.

A common optimization is to normalize indexes at every level.

Instead of using the original huge indexes, subtract the first index of the current level.

Example:

```python
base = queue[0][1]

node, index = queue.popleft()

index = index - base
```

Then calculate children using the normalized index.

This keeps indexes small.

However, Python integers can grow automatically, so the original code is perfectly understandable and accepted for normal constraints.

---

# Optimized Index-Normalized Version

```python
from collections import deque

class Solution:

    def widthOfBinaryTree(self, root):

        if root is None:
            return 0

        queue = deque([(root, 1)])
        maxWidth = 0

        while queue:

            size = len(queue)

            # First index of this level
            base = queue[0][1]

            for i in range(size):

                node, index = queue.popleft()

                # Normalize index
                index = index - base

                if i == 0:
                    left = index

                if i == size - 1:
                    right = index

                if node.left:
                    queue.append(
                        (node.left, 2 * index)
                    )

                if node.right:
                    queue.append(
                        (node.right, 2 * index + 1)
                    )

            currentWidth = right - left + 1

            maxWidth = max(maxWidth, currentWidth)

        return maxWidth
```

The main idea is still exactly the same:

```text
BFS
+
Index
+
Right - Left + 1
```

Normalization only keeps the numbers smaller.

---

# Common Mistakes

## 1. Using `len(queue)`

Wrong:

```python
maxWidth = max(maxWidth, len(queue))
```

This counts only existing nodes.

The problem also counts missing positions between the boundary nodes.

---

## 2. Forgetting `+1`

Wrong:

```python
width = right - left
```

Correct:

```python
width = right - left + 1
```

---

## 3. Using Wrong Child Index

With root index `1`:

```text
Left  = 2 * index
Right = 2 * index + 1
```

Don't mix this with zero-based indexing.

---

## 4. Forgetting to Store Index With Node

We need:

```python
(node, index)
```

not just:

```python
node
```

The index tells us the node's position in the complete-tree structure.

---

## 5. Thinking Missing Nodes Must Be Created

We don't actually create:

```text
None
None
None
```

The index automatically represents their positions.

This is the main trick.

---

# Top View vs Bottom View vs Width

These problems all use BFS but for different reasons.

### Top View

```text
BFS
+
Horizontal Distance
+
Keep FIRST node
```

### Bottom View

```text
BFS
+
Horizontal Distance
+
Keep LAST node
```

### Maximum Width

```text
BFS
+
Complete Tree Index
+
Right Index - Left Index + 1
```

---

# Complexity

Let:

```text
n = number of nodes
```

Every node is processed once:

```text
Time → O(n)
```

The queue can contain nodes from a level.

In the worst case:

```text
Space → O(n)
```

Therefore:

```text
Time  → O(n)
Space → O(n)
```

---

# Revision Cheat Sheet

```text
MAXIMUM WIDTH OF BINARY TREE

Pattern:
BFS + Complete Binary Tree Indexing

--------------------------------------------------

Why store index?

To count missing positions
between the leftmost and
rightmost nodes.

--------------------------------------------------

Root:

index = 1

Left child:

2 * index

Right child:

2 * index + 1

--------------------------------------------------

For every level:

leftIndex = queue[0][1]

rightIndex = queue[-1][1]

Width:

rightIndex - leftIndex + 1

--------------------------------------------------

Why +1?

Positions are inclusive.

Example:

4, 5, 6, 7

Count = 7 - 4 + 1
      = 4

--------------------------------------------------

Why not len(queue)?

Because queue contains
only existing nodes.

Example:

4 _ _ 7

len(queue) = 2

Actual width = 4

--------------------------------------------------

Why BFS?

We need to calculate width
level by level.

--------------------------------------------------

Why index?

It represents the position
the node would have in a
complete binary tree.

--------------------------------------------------

Important:

Top View:
BFS + HD + FIRST

Bottom View:
BFS + HD + LAST

Maximum Width:
BFS + INDEX + R-L+1

--------------------------------------------------

Complexity:

Time  → O(n)
Space → O(n)

--------------------------------------------------

Memory Trick:

"Don't count nodes.
Count positions."

```

---

# One-Line Pattern

```text
For Maximum Width, use BFS with complete-binary-tree indexes so the width of each level can be calculated as rightmost index - leftmost index + 1, including missing positions.
```

# Most Important Interview Points

```text
1. Why index?
→ To represent missing positions.

2. Why BFS?
→ We need to process one level at a time.

3. Why R - L + 1?
→ Width includes both boundary positions.

4. Why not queue size?
→ Queue size counts only existing nodes.

5. Root index?
→ 1

6. Left child?
→ 2 * index

7. Right child?
→ 2 * index + 1

8. Complexity?
→ O(n) time, O(n) space.
```