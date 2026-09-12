# Zigzag Level Order Traversal

## 1. Problem

Given the root of a binary tree, return its **level order traversal in zigzag order**.

That means:

- Level 0 → Left to Right
- Level 1 → Right to Left
- Level 2 → Left to Right
- Level 3 → Right to Left
- And so on...

### Example

```text
        3
       / \
      9   20
         /  \
        15   7
```

Normal Level Order:

```text
[
    [3],
    [9, 20],
    [15, 7]
]
```

Zigzag Level Order:

```text
[
    [3],
    [20, 9],
    [15, 7]
]
```

---

# 2. Brute Force

A simple way is:

1. Perform normal BFS level order traversal.
2. Store every level.
3. Reverse every alternate level.

This is actually the same basic idea used in the optimized solution below.

A less efficient approach would be to create each level and perform unnecessary extra processing/copying.

### Complexity

For `n` nodes:

```text
Time  → O(n)
Space → O(n)
```

We still need to visit every node, so `O(n)` is already optimal.

The important part is **how we organize the traversal**.

---

# 3. Pattern

This is a:

```text
Binary Tree
     ↓
Level Order Traversal
     ↓
BFS
     ↓
Queue
```

The important observation is:

> Zigzag traversal is just normal BFS + reversing alternate levels.

So we don't need a completely different traversal.

---

# 4. Main Idea

We use a queue for normal BFS.

For every level:

1. Take all nodes belonging to the current level.
2. Add their values to `level`.
3. Add their children to the queue.
4. If the current direction is Right → Left, reverse `level`.
5. Add `level` to the answer.
6. Change the direction for the next level.

We maintain:

```python
left_to_right = True
```

After every level:

```python
left_to_right = not left_to_right
```

So the direction keeps changing:

```text
Level 0 → L → R
Level 1 → R → L
Level 2 → L → R
Level 3 → R → L
...
```

---

# 5. Why BFS?

Because the problem specifically asks for traversal **level by level**.

BFS naturally processes one level at a time.

The queue contains:

```text
Current Level
      ↓
[ nodes being processed ]

Next Level
      ↓
[ their children ]
```

For example:

```text
        3
       / \
      9   20
         /  \
        15   7
```

Initially:

```text
queue = [3]
```

Process `3`:

```text
level = [3]

queue = [9, 20]
```

Now the entire next level is available in the queue.

---

# 6. Why `range(len(queue))`?

This is one of the most important parts of BFS.

```python
for i in range(len(queue)):
```

At the beginning of every level:

```python
len(queue)
```

tells us exactly how many nodes belong to the **current level**.

Example:

```text
        3
       / \
      9   20
         /  \
        15   7
```

Before processing level 1:

```text
queue = [9, 20]

len(queue) = 2
```

So:

```python
for i in range(2):
```

processes exactly:

```text
9
20
```

Their children are added to the queue, but those children belong to the **next level**.

This is how we separate levels.

---

# 7. Why Do We Add Children Before Reversing?

We always perform normal BFS:

```python
node = queue.popleft()
level.append(node.val)

if node.left:
    queue.append(node.left)

if node.right:
    queue.append(node.right)
```

This gives us every level in normal:

```text
Left → Right
```

order.

Then, if we need Right → Left:

```python
level.reverse()
```

This keeps the BFS logic simple.

---

# 8. Complete Code

```python
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        queue = deque([root])
        result = []

        left_to_right = True

        while queue:
            level = []

            # Process only the current level
            for i in range(len(queue)):
                node = queue.popleft()

                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            # Reverse every alternate level
            if left_to_right == False:
                level.reverse()

            result.append(level)

            # Change direction for next level
            left_to_right = not left_to_right

        return result
```

---

# 9. Dry Run

Consider:

```text
        3
       / \
      9   20
         /  \
        15   7
```

### Initial State

```text
queue = [3]
result = []
left_to_right = True
```

---

### Level 0

```text
queue = [3]
```

Process:

```text
node = 3
level = [3]
```

Children:

```text
queue = [9, 20]
```

Direction is Left → Right, so don't reverse.

```text
result = [[3]]
```

Change direction:

```text
left_to_right = False
```

---

### Level 1

```text
queue = [9, 20]
```

Process:

```text
9  → level = [9]
20 → level = [9, 20]
```

Children of `20`:

```text
queue = [15, 7]
```

Current direction is Right → Left.

So:

```python
level.reverse()
```

Before:

```text
[9, 20]
```

After:

```text
[20, 9]
```

Result:

```text
[
    [3],
    [20, 9]
]
```

Change direction:

```text
left_to_right = True
```

---

### Level 2

```text
queue = [15, 7]
```

Process:

```text
15 → level = [15]
7  → level = [15, 7]
```

Direction is Left → Right.

No reverse.

Result:

```text
[
    [3],
    [20, 9],
    [15, 7]
]
```

Final answer:

```text
[
    [3],
    [20, 9],
    [15, 7]
]
```

---

# 10. Important Variables

### `queue`

Stores nodes that still need to be processed.

```python
queue = deque([root])
```

---

### `level`

Stores values of the current level.

```python
level = []
```

Example:

```text
level = [9, 20]
```

---

### `result`

Stores the final answer.

```text
result = [
    [3],
    [20, 9],
    [15, 7]
]
```

---

### `left_to_right`

Controls the direction.

```python
left_to_right = True
```

After each level:

```python
left_to_right = not left_to_right
```

So:

```text
True
 ↓
False
 ↓
True
 ↓
False
```

---

# 11. Why `level.reverse()` Instead of Reversing the Queue?

We only want to change the **output order of the current level**.

The queue must continue maintaining normal BFS order because it is responsible for processing the next level correctly.

So:

```python
level.reverse()
```

is safe.

We should not disturb the queue's structure unnecessarily.

---

# 12. Common Mistakes

### Mistake 1: Using DFS without tracking levels

Zigzag is naturally a level-based problem.

Use:

```text
BFS + Queue
```

unless you have a specific reason to implement DFS.

---

### Mistake 2: Not using `len(queue)`

If you write:

```python
while queue:
    node = queue.popleft()
```

without capturing the current level size, you lose the separation between levels.

Use:

```python
for i in range(len(queue)):
```

to process one level at a time.

---

### Mistake 3: Reversing every level

Only alternate levels should be reversed.

```text
Level 0 → normal
Level 1 → reverse
Level 2 → normal
Level 3 → reverse
```

---

### Mistake 4: Forgetting to change direction

After processing every level:

```python
left_to_right = not left_to_right
```

---

### Mistake 5: Appending children in the wrong order

Keep normal BFS child insertion:

```python
if node.left:
    queue.append(node.left)

if node.right:
    queue.append(node.right)
```

Then reverse the `level` when required.

---

# 13. Complexity

Let `n` = number of nodes.

### Time

Every node is:

- added to the queue once
- removed from the queue once
- processed once

Reversing levels together costs at most `O(n)` overall.

Therefore:

```text
Time = O(n)
```

### Space

The queue can contain nodes from the largest level.

Also, the answer itself contains all nodes.

Auxiliary BFS space:

```text
O(n)
```

Overall:

```text
Time  → O(n)
Space → O(n)
```

---

# 14. Pattern Recognition

When you see:

```text
"level order"
"level by level"
"each level"
"alternate direction"
"left to right, then right to left"
"zigzag"
```

Think:

```text
Binary Tree
     ↓
BFS
     ↓
Queue
     ↓
Process one level at a time
     ↓
Reverse alternate levels
```

---

# 15. Related Problems

This problem is closely related to:

- Binary Tree Level Order Traversal
- Binary Tree Right Side View
- Binary Tree Left View
- Top View
- Bottom View
- Maximum Width of Binary Tree
- All Nodes Distance K
- Amount of Time for Binary Tree to Be Infected

The common idea is:

```text
Tree
 ↓
BFS
 ↓
Queue
 ↓
Level-by-level processing
```

---

# 16. Revision Cheat Sheet

```text
Zigzag Level Order
        ↓
      BFS
        ↓
     Queue
        ↓
Process one level using len(queue)
        ↓
Store values in level[]
        ↓
If direction is R → L:
        reverse(level)
        ↓
Add level to result
        ↓
Toggle direction
```

### Core Code

```python
while queue:
    level = []

    for i in range(len(queue)):
        node = queue.popleft()

        level.append(node.val)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    if not left_to_right:
        level.reverse()

    result.append(level)
    left_to_right = not left_to_right
```

---

# 17. Interview Memory Trick

Remember:

> **"BFS normally, reverse alternate levels."**

Or simply:

```text
Queue → Level → Reverse? → Result → Toggle
```

### One-Line Pattern

> **Zigzag Level Order = Level Order BFS + alternate level reversal.**