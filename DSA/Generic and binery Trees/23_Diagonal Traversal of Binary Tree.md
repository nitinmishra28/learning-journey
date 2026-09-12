# Diagonal Traversal of Binary Tree

## 1. Problem

Given a binary tree, return its **diagonal traversal**.

In diagonal traversal, nodes are grouped according to diagonal lines moving:

```text
Top-Right → Bottom-Right
```

Whenever we move:

```text
right → stay on the same diagonal
left  → move to the next diagonal
```

### Example

```text
        8
       / \
      3   10
     / \    \
    1   6    14
       / \   /
      4   7 13
```

Diagonal groups are:

```text
Diagonal 1: 8, 10, 14
Diagonal 2: 3, 6, 7, 13
Diagonal 3: 1, 4
```

So the traversal is:

```text
[8, 10, 14, 3, 6, 7, 13, 1, 4]
```

---

# 2. Brute Force

One way to solve diagonal traversal is to use recursion and maintain the diagonal number of every node.

For every node:

```text
root → diagonal 0
left child → diagonal + 1
right child → same diagonal
```

We can store nodes in a dictionary:

```python
diagonal[distance].append(node.data)
```

Then traverse the diagonals in order.

### Complexity

```text
Time  → O(n)
Space → O(n)
```

Although this approach is already `O(n)`, it requires explicitly maintaining diagonal numbers and then managing the groups.

The queue-based approach below follows the diagonal movement more naturally.

---

# 3. Pattern

This is a:

```text
Binary Tree
     ↓
Diagonal Traversal
     ↓
BFS + Queue
     ↓
Move Right → Same Diagonal
Move Left  → Next Diagonal
```

### One-Line Pattern

> **Diagonal Traversal = BFS queue for left children + keep moving right on the current diagonal.**

---

# 4. Main Idea

The most important observation is:

> **Right movement stays on the same diagonal, while left movement starts the next diagonal.**

Consider:

```text
        8
       / \
      3   10
     / \    \
    1   6    14
       / \
      4   7
```

Starting from `8`:

```text
8 → right → 10 → right → 14
```

All of these belong to the same diagonal:

```text
8, 10, 14
```

But when we reach:

```text
8 → left → 3
```

we need to process a new diagonal.

So whenever we see a left child:

```python
if temp.left:
    queue.append(temp.left)
```

we save it in the queue for a future diagonal.

Then we keep moving right:

```python
temp = temp.right
```

---

# 5. Why Do We Need a Queue?

The queue stores the **left children that will start future diagonals**.

For example:

```text
        8
       / \
      3   10
     / \    \
    1   6    14
```

Start:

```text
queue = [8]
```

Process `8`:

```text
answer = [8]
```

Its left child `3` cannot be processed in the same diagonal, so:

```text
queue = [3]
```

Then move right:

```text
8 → 10 → 14
```

After finishing:

```text
answer = [8, 10, 14]
queue = [3]
```

Now:

```text
3
```

starts the next diagonal.

---

# 6. Understanding the Two Loops

The code has:

```python
while queue:
```

and inside it:

```python
while temp:
```

They have different jobs.

### Outer loop

```python
while queue:
```

Means:

> Process the next diagonal.

---

### Inner loop

```python
while temp:
```

Means:

> Keep moving right along the current diagonal.

So think:

```text
Outer while
    ↓
Next diagonal

Inner while
    ↓
Move right through current diagonal
```

This is the most important thing to understand in the code.

---

# 7. Complete Code

```python
from collections import deque

class Solution:
    def diagonal(self, root):
        ans = []

        if root is None:
            return ans

        queue = deque()
        queue.append(root)

        while queue:
            temp = queue.popleft()

            # Move along the current diagonal
            while temp:
                ans.append(temp.data)

                # Left child belongs to the next diagonal
                if temp.left:
                    queue.append(temp.left)

                # Right child stays on the same diagonal
                temp = temp.right

        return ans
```

---

# 8. Dry Run

Consider:

```text
        8
       / \
      3   10
     / \    \
    1   6    14
       / \
      4   7
```

### Initial

```text
queue = [8]
ans = []
```

---

## Diagonal 1

Take:

```python
temp = queue.popleft()
```

So:

```text
temp = 8
queue = []
```

Process `8`:

```text
ans = [8]
```

Left child:

```text
3
```

belongs to the next diagonal:

```text
queue = [3]
```

Move right:

```text
temp = 10
```

Process `10`:

```text
ans = [8, 10]
```

Its left child doesn't exist.

Move right:

```text
temp = 14
```

Process:

```text
ans = [8, 10, 14]
```

`14` has left child `13`:

```text
queue = [3, 13]
```

Then:

```text
temp = None
```

Current diagonal is complete.

---

## Diagonal 2

Take:

```text
temp = 3
```

Queue becomes:

```text
queue = [13]
```

Process `3`:

```text
ans = [8, 10, 14, 3]
```

Its left child:

```text
1
```

goes into queue:

```text
queue = [13, 1]
```

Move right:

```text
temp = 6
```

Process:

```text
ans = [8, 10, 14, 3, 6]
```

Its left child:

```text
4
```

goes into queue:

```text
queue = [13, 1, 4]
```

Move right:

```text
temp = 7
```

Process:

```text
ans = [8, 10, 14, 3, 6, 7]
```

No right child.

Diagonal ends.

---

## Continue

Next:

```text
temp = 13
```

Then:

```text
temp = 1
```

Then:

```text
temp = 4
```

Final:

```text
[8, 10, 14, 3, 6, 7, 13, 1, 4]
```

---

# 9. Why Is the Right Child Not Added to the Queue?

This is the core concept.

Suppose:

```text
        8
         \
          10
            \
             14
```

These nodes are already on the same diagonal:

```text
8 → 10 → 14
```

Therefore we simply do:

```python
temp = temp.right
```

No queue is needed.

But:

```text
        8
       /
      3
```

`3` starts a new diagonal.

Therefore:

```python
queue.append(temp.left)
```

---

# 10. Why Are Left Children Processed Later?

Consider:

```text
        8
       / \
      3   10
```

If we immediately process `3`, we would leave the current diagonal:

```text
8
```

But we first need to continue:

```text
8 → 10
```

Therefore:

```text
8
 ↓
10
 ↓
14
```

is completed first.

Meanwhile, we save:

```text
3
```

in the queue.

So the queue acts like a list of:

```text
Future diagonal starting points
```

---

# 11. Important Invariant

At any moment:

```text
queue
```

contains nodes that are waiting to start future diagonals.

And:

```text
temp
```

moves only to the right.

So:

```text
temp → right → right → right
```

while:

```text
left children → queue
```

This gives a very simple mental model:

```text
              RIGHT
               ↓
Current Node → Current Node → Current Node
     |
     LEFT
     ↓
   Queue
     ↓
Next diagonal
```

---

# 12. Why BFS + Queue Instead of Normal Level Order?

Normal level order asks:

```text
Which nodes are on the same level?
```

So we use:

```text
BFS + queue
```

Diagonal traversal asks:

```text
Which nodes are on the same diagonal?
```

Here the movement rule is different:

```text
Right → same diagonal
Left  → next diagonal
```

The queue stores the nodes that need to begin those next diagonals.

So the queue is still useful, but its meaning is different from normal level-order traversal.

---

# 13. Common Mistakes

### Mistake 1: Adding right children to the queue

Wrong:

```python
if temp.right:
    queue.append(temp.right)
```

The right child is already part of the current diagonal.

Instead:

```python
temp = temp.right
```

---

### Mistake 2: Forgetting to add left children

Wrong:

```python
temp = temp.right
```

without saving the left child.

Then we lose entire parts of the tree.

Correct:

```python
if temp.left:
    queue.append(temp.left)
```

---

### Mistake 3: Using only one loop

If you only use:

```python
while queue:
```

you won't naturally traverse all the way along the current diagonal.

You need:

```python
while queue:
    temp = queue.popleft()

    while temp:
        ...
        temp = temp.right
```

---

### Mistake 4: Thinking this is normal level order

It is not.

Normal level order:

```text
        8
       / \
      3   10
```

gives:

```text
8, 3, 10
```

Diagonal traversal follows:

```text
8 → 10
```

and processes `3` later.

---

# 14. Complexity

Let `n` be the number of nodes.

### Time

Every node is:

- added to the queue at most once
- removed from the queue once
- processed once

Therefore:

```text
Time = O(n)
```

### Space

The queue can contain nodes waiting for future diagonals.

In the worst case:

```text
Space = O(n)
```

Therefore:

```text
Time  → O(n)
Space → O(n)
```

---

# 15. Pattern Recognition

When you see:

```text
"Diagonal Traversal"
```

Think:

```text
Right → same diagonal
Left  → next diagonal
```

Then:

```text
Current diagonal
        ↓
Keep moving right
        ↓
Store every left child in queue
        ↓
When current diagonal ends
        ↓
Take next node from queue
        ↓
Process next diagonal
```

---

# 16. Revision Cheat Sheet

```text
Diagonal Traversal
        ↓
Queue
        ↓
Take one diagonal-start node
        ↓
Move continuously RIGHT
        ↓
Add every LEFT child to queue
        ↓
Current diagonal ends
        ↓
Take next node from queue
```

### Core Code

```python
while queue:
    temp = queue.popleft()

    while temp:
        ans.append(temp.data)

        if temp.left:
            queue.append(temp.left)

        temp = temp.right
```

### Remember

```text
RIGHT → Same Diagonal
LEFT  → Next Diagonal
```

### Complexity

```text
Time  → O(n)
Space → O(n)
```

---

# 17. Interview Memory Trick

> **"Keep going right, save left children for later."**

That's the entire diagonal traversal pattern:

```text
RIGHT = Continue
LEFT  = Queue
```