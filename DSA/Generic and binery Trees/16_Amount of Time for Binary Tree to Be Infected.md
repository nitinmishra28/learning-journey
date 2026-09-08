# Amount of Time for Binary Tree to Be Infected

## Problem

Given a binary tree and a starting node `start`, the infection starts from that node.

Every minute, the infection spreads from an infected node to its:

```text
1. Left child
2. Right child
3. Parent
```

Return the total number of minutes needed to infect the entire tree.

Example:

```text
        1
       / \
      5   3
     / \   \
    4   9   7

start = 5
```

Infection spreads:

```text
Minute 0:
        5

Minute 1:
      4   9   1

Minute 2:
              3

Minute 3:
              7
```

So the answer is:

```text
3
```

---

# Brute Force

## Idea

One possible approach is:

1. Find the distance from `start` to every node.
2. Take the maximum distance.

But to calculate the distance to every node separately, we may repeatedly traverse large parts of the tree.

In the worst case, this can take:

```text
O(n²)
```

So we need a better approach.

---

# Pattern

This is almost the same pattern as **All Nodes Distance K in Binary Tree**.

```text
Binary Tree
     ↓
Need to move:
Left + Right + Parent
     ↓
Create Parent Map
     ↓
Start BFS from infected node
     ↓
One BFS level = One minute
```

The key idea is:

> Treat the tree like an undirected graph and perform BFS from the starting node.

---

# Main Idea

Normally, a binary tree lets us move downward:

```text
        1
       / \
      2   3
```

From `1`:

```text
1 → 2
1 → 3
```

But infection can also move upward:

```text
2 → 1
```

Therefore, we need to know the parent of every node.

We create:

```python
parent[child] = parent
```

For example:

```text
        1
       / \
      2   3
     /
    4
```

Parent map:

```text
parent[2] = 1
parent[3] = 1
parent[4] = 2
```

Now from any node we can move in three directions:

```text
              parent
                ↑
                |
left ←-------- node --------→ right
```

---

# Step 1: Create Parent Map

Your `parents()` function does this:

```python
def parents(self, root):
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

The important line is:

```python
parent[node.left] = node
```

It means:

```text
node.left's parent = node
```

Similarly:

```python
parent[node.right] = node
```

means:

```text
node.right's parent = node
```

---

# Step 2: Find the Starting Node

The input gives:

```python
start
```

as a value, not the actual `TreeNode` object.

So we need to find the actual node whose value is `start`.

Your code uses BFS:

```python
queue = deque()
queue.append(root)
node_start = None

while queue:
    node = queue.popleft()

    if node.val == start:
        node_start = node
        break

    if node.left:
        queue.append(node.left)

    if node.right:
        queue.append(node.right)
```

After this:

```python
node_start
```

contains the actual `TreeNode` where the infection begins.

---

# Why Can't We Just Use `start`?

Because:

```python
start
```

is just an integer.

For example:

```text
start = 5
```

But to move to its children and parent, we need the actual node:

```python
node_start.left
node_start.right
parent[node_start]
```

Therefore, we first find the actual node object.

---

# Step 3: BFS Infection

Now we start BFS from:

```python
node_start
```

```python
queue = deque()
queue.append(node_start)
```

We also maintain:

```python
visited = set()
```

because after creating the parent map, the tree behaves like an undirected graph.

For example:

```text
    1
    |
    5
```

We can move:

```text
5 → 1
```

but then from `1` we could move back:

```text
1 → 5
```

Without `visited`, we could keep going:

```text
5 → 1 → 5 → 1 → ...
```

So:

```python
visited.add(node_start)
```

marks the starting node as already infected/visited.

---

# One BFS Level = One Minute

This is the most important idea in the problem.

Suppose:

```text
Minute 0:
        5
```

Queue:

```text
[5]
```

After processing `5`:

```text
Minute 1:
      4   9   1
```

Queue:

```text
[4, 9, 1]
```

After processing them:

```text
Minute 2:
              3
```

And so on.

Therefore:

```text
BFS level = infection time
```

That's why we process:

```python
for i in range(len(queue)):
```

The nodes currently in the queue belong to the same infection minute.

---

# Why `ans += 1`?

Your code has:

```python
while queue:

    for i in range(len(queue)):
        ...
    
    ans += 1
```

Suppose:

```text
Queue before processing:

[5]
```

These nodes are infected at:

```text
Minute 0
```

We process them and add their neighbors.

Now:

```text
Queue = [4, 9, 1]
```

These nodes become infected after **1 minute**.

So:

```python
ans += 1
```

The value of `ans` represents how many BFS levels have been processed.

---

# Why Do We Return `ans - 1`?

Your code starts with:

```python
ans = 0
```

and increments after every level:

```python
ans += 1
```

Even the starting node creates one processed level.

For example, if the tree has only one node:

```text
5
```

There is no infection spread needed.

Correct answer:

```text
0
```

But the loop processes the starting node:

```text
ans = 1
```

Therefore:

```python
return ans - 1
```

gives:

```text
0
```

For a tree where infection needs 3 actual minutes:

```text
ans = 4
```

so:

```text
ans - 1 = 3
```

---

# Complete Code

```python
from collections import deque

class Solution:

    def parents(self, root):
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

    def amountOfTime(self, root, start):

        # Find parent of every node
        parent = self.parents(root)

        # Find the actual node where infection starts
        queue = deque()
        queue.append(root)

        node_start = None

        while queue:
            node = queue.popleft()

            if node.val == start:
                node_start = node
                break

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        # BFS from starting node
        queue = deque()
        queue.append(node_start)

        visited = set()
        visited.add(node_start)

        ans = 0

        while queue:

            # Process all nodes infected at the same time
            for i in range(len(queue)):

                node = queue.popleft()

                # Infect left child
                if node.left and node.left not in visited:
                    visited.add(node.left)
                    queue.append(node.left)

                # Infect right child
                if node.right and node.right not in visited:
                    visited.add(node.right)
                    queue.append(node.right)

                # Infect parent
                if node in parent and parent[node] not in visited:
                    visited.add(parent[node])
                    queue.append(parent[node])

            # One minute has passed
            ans += 1

        return ans - 1
```

---

# Dry Run

Consider:

```text
        1
       / \
      5   3
     / \   \
    4   9   7

start = 5
```

## Parent Map

We get:

```text
parent[5] = 1
parent[3] = 1
parent[4] = 5
parent[9] = 5
parent[7] = 3
```

---

## Find Starting Node

We search for:

```text
start = 5
```

Eventually:

```python
node_start = node(5)
```

---

## Minute 0

Queue:

```text
[5]
```

Visited:

```text
{5}
```

Process `5`.

Its neighbors:

```text
left   → 4
right  → 9
parent → 1
```

Add all three:

```text
queue = [4, 9, 1]
```

Then:

```text
ans = 1
```

---

## Minute 1

Queue:

```text
[4, 9, 1]
```

Process `4`:

```text
parent → 5
```

But `5` is already visited.

Process `9`:

```text
parent → 5
```

Already visited.

Process `1`:

```text
left  → 5
right → 3
```

`5` is visited.

Add `3`.

Queue:

```text
[3]
```

Then:

```text
ans = 2
```

---

## Minute 2

Queue:

```text
[3]
```

Process `3`:

```text
right → 7
```

Add `7`.

Queue:

```text
[7]
```

Then:

```text
ans = 3
```

---

## Minute 3

Queue:

```text
[7]
```

`7` has no unvisited neighbors.

Queue becomes:

```text
[]
```

Then:

```text
ans = 4
```

Loop ends.

Return:

```python
ans - 1
```

Therefore:

```text
4 - 1 = 3
```

Answer:

```text
3
```

---

# Why Do We Need `visited` Even Though It Is a Tree?

This is a common interview question.

A tree itself does not contain cycles.

But once we add parent movement, we can travel in both directions.

Original:

```text
5 → 1
```

With parent map:

```text
5 ↔ 1
```

Now:

```text
5 → 1 → 5
```

is possible.

So after converting the tree into an undirected graph:

```text
visited
```

becomes necessary.

---

# Important Difference: Distance K vs Infection Time

These two problems use almost the same pattern.

### Distance K

You stop when:

```text
distance == k
```

and return all nodes at that level.

```text
Parent Map
    ↓
BFS
    ↓
Distance K
```

### Infection Time

You continue BFS until:

```text
all nodes are infected
```

and count how many levels were required.

```text
Parent Map
    ↓
BFS
    ↓
Number of Levels = Time
```

---

# Complexity

Let `n` be the number of nodes.

## Parent Map

Every node is visited once:

```text
O(n)
```

## Finding Start Node

Worst case:

```text
O(n)
```

## Infection BFS

Every node is visited once:

```text
O(n)
```

Therefore total:

```text
O(n)
```

### Space

Parent map:

```text
O(n)
```

Queue:

```text
O(n)
```

Visited:

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

## 1. Forgetting Parent Movement

Only doing:

```python
node.left
node.right
```

is wrong.

Infection must also move:

```python
parent[node]
```

---

## 2. Forgetting `visited`

Without it:

```text
child → parent → child → parent
```

can happen.

Always use:

```python
visited = set()
```

---

## 3. Using `start` Directly

`start` is a value:

```text
start = 5
```

We need the actual node object to access:

```python
node.left
node.right
parent[node]
```

So we first find `node_start`.

---

## 4. Increasing Time for Every Node

Wrong:

```python
for node in queue:
    ans += 1
```

Time is based on BFS **levels**, not individual nodes.

Correct idea:

```python
for i in range(len(queue)):
    ...
    
ans += 1
```

One complete level represents one minute.

---

## 5. Forgetting the `-1`

The code counts the starting level as one processed level.

So:

```python
return ans - 1
```

converts:

```text
number of processed levels
```

into:

```text
actual number of minutes
```

---

# Pattern Recognition

When you see:

> Something spreads through a binary tree every minute.

Think:

```text
Spread / Infection
        ↓
BFS
        ↓
One level = One unit of time
```

If movement includes going upward:

```text
Need parent
    ↓
Create parent map
    ↓
Tree behaves like undirected graph
    ↓
Use visited
    ↓
BFS
```

### Shortcut

```text
Infection in Binary Tree
        ↓
Parent Map
        ↓
BFS
        ↓
One Level = One Minute
```

---

# Related Problems

| Problem | Pattern |
|---|---|
| All Nodes Distance K | Parent Map + BFS |
| Amount of Time for Binary Tree to Be Infected | Parent Map + BFS + Level Count |
| Level Order Traversal | BFS + Levels |
| Minimum Depth | BFS + First Leaf |
| Rotten Oranges | Multi-source BFS + Time |
| Word Ladder | BFS + Shortest Path |

---

# Revision Cheat Sheet

```text
Problem:
Find time required to infect entire binary tree.

Main Problem:
Infection can move:
Left + Right + Parent

Step 1:
Create parent map.

parent[child] = parent

Step 2:
Find actual TreeNode corresponding to start value.

Step 3:
Start BFS from start node.

Step 4:
Use visited because parent movement makes it an undirected graph.

Step 5:
For every BFS level:
    process all nodes
    infect left
    infect right
    infect parent

Step 6:
One BFS level = one minute.

Final:
return ans - 1

Complexity:
Time  = O(n)
Space = O(n)
```

# One-Line Pattern

> **For binary-tree infection problems, create parent pointers, treat the tree as an undirected graph, and use BFS where each level represents one minute of infection.**