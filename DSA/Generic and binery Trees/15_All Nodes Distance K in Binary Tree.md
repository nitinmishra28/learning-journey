# All Nodes Distance K in Binary Tree

## Problem

Given a binary tree, a target node, and an integer `k`, return all nodes that are exactly `k` distance away from the target.

Distance means the number of **edges** between two nodes.

Example:

```text
        3
       / \
      5   1
     / \ / \
    6  2 0  8
      / \
     7   4

Target = 5
K = 2
```

Nodes at distance `2` from `5`:

```text
5 → 3 → 1
5 → 2 → 7
5 → 2 → 4
5 → 6 → ...
```

So the answer is:

```text
[7, 4, 1]
```

---

# Brute Force

## Idea

For every node in the tree:

1. Find the distance from `target` to that node.
2. If distance is `k`, add it to the answer.

The problem is that a normal tree only lets us move:

```text
parent → child
```

But from the target we need to move in **three directions**:

```text
        parent
          ↑
          |
      left ← node → right
```

So we first need some way to move from a node to its parent.

A simple approach is to find the path from target to every node and calculate the distance.

This can take `O(n²)` time in the worst case.

### Why?

For many nodes, we may repeatedly traverse a large part of the tree to calculate distances.

So we can do better.

---

# Pattern

```text
Binary Tree
     ↓
Need to move UP + DOWN
     ↓
Store Parent of Every Node
     ↓
BFS from Target
     ↓
Distance K
```

The important pattern is:

> **Convert the tree into an undirected graph using a parent map, then run BFS from the target.**

---

# Main Idea

Normally, from a tree node we can only go:

```text
        3
       / \
      5   1
```

From `5`, we can directly go to:

```text
5 → 6
5 → 2
```

But we cannot directly go:

```text
5 → 3
```

because `3` is the parent.

For this problem, we need:

```text
             3
           ↙   ↘
          5     1
         ↙ ↘   ↙ ↘
        6   2 0   8
```

From `5`, we should be able to move:

```text
5 → 6
5 → 2
5 → 3
```

Therefore, we create a `parent` dictionary.

For example:

```text
parent[5] = 3
parent[1] = 3
parent[6] = 5
parent[2] = 5
```

Now every node knows its parent.

---

# Step 1: Find Parent of Every Node

We use BFS to traverse the entire tree.

```python
def find_parent(self, root):
    parent = {}

    queue = deque()
    queue.append(root)

    while queue:
        node = queue.popleft()

        if node.left:
            parent[node.left] = node
            queue.append(node.left)

        if node.right:
            parent[node.right] = node
            queue.append(node.right)

    return parent
```

For:

```text
        3
       / \
      5   1
     / \
    6   2
```

The dictionary becomes:

```text
parent[5] = 3
parent[1] = 3
parent[6] = 5
parent[2] = 5
```

---

# Why Are We Using the Node as the Dictionary Key?

Notice:

```python
parent[node.left] = node
```

Here:

```text
key   = child node
value = parent node
```

For example:

```python
parent[5] = 3
```

means:

> The parent of node `5` is node `3`.

This allows us to do:

```python
parent[node]
```

and immediately find the parent of that node.

---

# Step 2: BFS From Target

Now we have three possible directions from every node:

```text
              parent
                ↑
                |
left ←-------- node --------→ right
```

So for every node we check:

```python
node.left
node.right
parent[node]
```

We use BFS because BFS naturally explores nodes level by level.

For example:

```text
distance 0:
        5

distance 1:
      6   2   3

distance 2:
          7 4 1
```

Therefore, when BFS reaches level `k`, all nodes in the queue are exactly distance `k` from the target.

---

# Why Do We Need `visited`?

This is very important.

After creating the parent map, the tree effectively becomes an **undirected graph**.

For example:

```text
    3
    |
    5
```

From `5`:

```text
5 → 3
```

But from `3` we can go back:

```text
3 → 5
```

Without `visited`, BFS could keep going:

```text
5 → 3 → 5 → 3 → 5 → ...
```

So we maintain:

```python
visited = set()
```

and mark nodes as soon as we add them:

```python
visited.add(node)
```

This ensures that every node is processed only once.

---

# Why `visited.add()` Before Adding to Queue?

We do:

```python
visited.add(node.left)
queue.append(node.left)
```

instead of waiting until we pop it.

This prevents the same node from being added multiple times.

For example, a node might be reachable from:

```text
parent
left child
right child
```

We want it in the queue only once.

---

# Complete Code

```python
from collections import deque

class Solution:

    def find_parent(self, root):
        parent = {}

        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()

            if node.left:
                parent[node.left] = node
                queue.append(node.left)

            if node.right:
                parent[node.right] = node
                queue.append(node.right)

        return parent

    def distanceK(self, root, target, k):

        # Find parent of every node
        parent = self.find_parent(root)

        # BFS from target
        queue = deque()
        queue.append(target)

        visited = set()
        visited.add(target)

        distance = 0

        while queue:

            # We reached distance K
            if distance == k:
                answer = []

                while queue:
                    node = queue.popleft()
                    answer.append(node.val)

                return answer

            size = len(queue)

            for i in range(size):

                node = queue.popleft()

                # Left child
                if node.left and node.left not in visited:
                    visited.add(node.left)
                    queue.append(node.left)

                # Right child
                if node.right and node.right not in visited:
                    visited.add(node.right)
                    queue.append(node.right)

                # Parent
                if node in parent and parent[node] not in visited:
                    visited.add(parent[node])
                    queue.append(parent[node])

            distance += 1

        return []
```

---

# Dry Run

Consider:

```text
        3
       / \
      5   1
     / \ / \
    6  2 0  8
      / \
     7   4
```

Target:

```text
5
```

and:

```text
k = 2
```

## Parent Map

After `find_parent()`:

```text
parent[5] = 3
parent[1] = 3
parent[6] = 5
parent[2] = 5
parent[0] = 1
parent[8] = 1
parent[7] = 2
parent[4] = 2
```

---

## Distance 0

Initially:

```text
queue = [5]
distance = 0
```

Target itself is distance `0`.

Since:

```python
distance != k
```

we process node `5`.

Its possible neighbors:

```text
left   → 6
right  → 2
parent → 3
```

So:

```text
queue = [6, 2, 3]
```

Then:

```text
distance = 1
```

---

## Distance 1

Current queue:

```text
[6, 2, 3]
```

These are exactly one edge away from `5`.

Process `6`:

```text
6 has no children
parent = 5
```

But `5` is already visited.

So nothing is added.

Process `2`:

```text
2 → 7
2 → 4
2 → 5
```

`5` is already visited.

Add:

```text
7, 4
```

Process `3`:

```text
3 → 5
3 → 1
```

`5` is already visited.

Add:

```text
1
```

Now:

```text
queue = [7, 4, 1]
distance = 2
```

---

## Distance 2

Now:

```python
if distance == k:
```

is:

```text
2 == 2
```

True.

Therefore all nodes currently in the queue are exactly distance `2` from target.

```text
queue = [7, 4, 1]
```

So:

```text
answer = [7, 4, 1]
```

Return:

```text
[7, 4, 1]
```

---

# Why Does `size = len(queue)` Matter?

This line is extremely important:

```python
size = len(queue)
```

It tells us:

> How many nodes belong to the current distance level?

For example:

```text
distance 0:
[5]
```

Then after processing `5`:

```text
distance 1:
[6, 2, 3]
```

Then after processing those:

```text
distance 2:
[7, 4, 1]
```

We need to finish processing one complete level before increasing distance.

That's why:

```python
for i in range(size):
```

is used.

---

# Why Is BFS Better Than DFS Here?

DFS goes deep into one branch first.

But this problem asks:

> Find nodes exactly `k` distance away.

That is naturally a **level-by-level** problem.

BFS gives:

```text
distance 0 → level 0
distance 1 → level 1
distance 2 → level 2
...
```

So BFS is the natural choice.

---

# Important Difference: Tree vs Graph

Originally, the structure is a tree:

```text
        3
       / \
      5   1
```

You normally think:

```text
parent → child
```

But after creating the parent map, we can move:

```text
        3
       ↙ ↘
      5   1
     ↙ ↘
    6   2
```

From any node:

```text
left
right
parent
```

Now it behaves like an **undirected graph**.

Therefore:

```text
Graph traversal → BFS → visited set
```

is the correct mental model.

---

# Why `if node in parent`?

The root has no parent.

For example:

```text
        3
       /
      5
```

We have:

```python
parent[5] = 3
```

but there is no:

```python
parent[3]
```

Therefore:

```python
if node in parent:
```

checks whether the current node actually has a parent before accessing:

```python
parent[node]
```

---

# Complexity

Let `n` = number of nodes.

## Parent Mapping

We visit every node once:

```text
O(n)
```

## BFS

Again, every node is visited at most once:

```text
O(n)
```

Therefore total:

```text
O(n)
```

### Space

Parent dictionary:

```text
O(n)
```

Queue:

```text
O(n)
```

Visited set:

```text
O(n)
```

Therefore:

```text
O(n)
```

### Complexity Table

| Approach | Time | Space |
|---|---:|---:|
| Brute Force | O(n²) worst case | O(n) |
| Parent Map + BFS | O(n) | O(n) |

---

# Common Mistakes

## 1. Only Checking Left and Right

Wrong:

```python
if node.left:
    ...
if node.right:
    ...
```

This cannot reach ancestors.

We also need:

```python
if node in parent:
    ...
```

---

## 2. Forgetting `visited`

Without:

```python
visited = set()
```

we can move back and forth:

```text
5 → 3 → 5 → 3 → ...
```

So `visited` is necessary.

---

## 3. Increasing Distance for Every Node

Wrong idea:

```python
distance += 1
```

after every node.

Distance belongs to a **level**, not an individual node.

That's why we first store:

```python
size = len(queue)
```

and process the complete level.

---

## 4. Adding the Target to Queue Without Visiting It

We must start with:

```python
queue.append(target)
visited.add(target)
```

Otherwise the target can later be reached again through its parent.

---

## 5. Forgetting That `k = 0`

If:

```text
target = 5
k = 0
```

the answer should simply be:

```text
[5]
```

Our code handles this because:

```python
distance = 0
```

and immediately:

```python
if distance == k:
```

becomes true.

---

# Pattern Recognition

When you see:

> Find all nodes exactly `K` distance from a target in a binary tree.

Think:

```text
Can I move only downward?
        ↓
       NO
        ↓
Need parent pointers
        ↓
Tree becomes undirected graph
        ↓
BFS from target
        ↓
Use visited
        ↓
Stop at distance K
```

### Shortcut

```text
Distance K in Binary Tree
        ↓
Parent Map
        ↓
BFS
        ↓
Visited
```

---

# Related Tree Patterns

| Problem | Main Pattern |
|---|---|
| Maximum Depth | DFS + Height |
| Diameter | DFS + Height |
| Balanced Tree | DFS + Height + Sentinel |
| Left View | DFS + Level |
| Right View | DFS + Level |
| Top View | BFS + Horizontal Distance + First |
| Bottom View | BFS + Horizontal Distance + Last |
| Distance K | Parent Map + BFS + Visited |
| Maximum Width | BFS + Position Index |

---

# Revision Cheat Sheet

```text
Problem:
Find all nodes exactly K distance from target.

Problem:
Tree normally allows only downward movement.

Solution:
1. Create parent map.
2. Start BFS from target.
3. Treat left, right and parent as neighbors.
4. Use visited to avoid going backward forever.
5. Process BFS level by level.
6. When distance == k, return all nodes in queue.

Parent Map:
parent[child] = parent

Neighbors:
node.left
node.right
parent[node]

Distance:
One complete BFS level = +1 distance

Important:
size = len(queue)

Visited:
Prevents:
A → B → A → B → ...

Complexity:
Time  = O(n)
Space = O(n)
```

# One-Line Pattern

> **For Distance K in a Binary Tree, create parent pointers to move upward, then use BFS from the target with a visited set to find the nodes at distance K.**