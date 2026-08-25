# 🌳 Trees in Python — Lecture 1

## 1. What is a Tree?

A **Tree** is a non-linear data structure made up of **nodes** connected by edges.

A Binary Tree is a tree where each node can have at most:

- One left child
- One right child

Example:

```text
        10
       /  \
     20    30
    /  \
   40   50
```

---

# 2. Creating a Binary Tree Node

In Python, we can represent a Binary Tree node using a class.

```python
class Tree:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
```

Each node contains:

```text
data   → value stored in the node
left   → reference to left child
right  → reference to right child
```

Initially:

```python
self.left = None
self.right = None
```

because the node does not have any children yet.

---

# 3. Creating a Binary Tree

```python
root = Tree(10)

root.left = Tree(20)
root.right = Tree(30)

root.left.left = Tree(40)
root.left.right = Tree(50)
```

This creates:

```text
        10
       /  \
     20    30
    /  \
   40   50
```

Here:

```text
root = 10

10.left  = 20
10.right = 30

20.left  = 40
20.right = 50
```

---

# 4. Tree Traversal

**Traversal** means visiting every node of the tree in a particular order.

The three basic DFS traversals are:

```text
Preorder
Inorder
Postorder
```

And one common BFS traversal is:

```text
Level Order
```

---

# 5. Preorder Traversal — NLR

Preorder follows:

```text
N → L → R
```

Where:

```text
N = Node
L = Left
R = Right
```

So:

```text
Node → Left → Right
```

For:

```text
        10
       /  \
     20    30
    /  \
   40   50
```

Traversal:

```text
10 → 20 → 40 → 50 → 30
```

### Code

```python
def preorder(root):

    if root is None:
        return

    print(root.data)

    preorder(root.left)
    preorder(root.right)
```

Call:

```python
preorder(root)
```

### Pattern to remember

```text
Process Node
      ↓
Go Left
      ↓
Go Right
```

---

# 6. Inorder Traversal — LNR

Inorder follows:

```text
L → N → R
```

So:

```text
Left → Node → Right
```

For:

```text
        10
       /  \
     20    30
    /  \
   40   50
```

Traversal:

```text
40 → 20 → 50 → 10 → 30
```

### Code

```python
def inorder(root):

    if root is None:
        return

    inorder(root.left)

    print(root.data)

    inorder(root.right)
```

Call:

```python
inorder(root)
```

### Pattern to remember

```text
Go Left
   ↓
Process Node
   ↓
Go Right
```

---

# 7. Postorder Traversal — LRN

Postorder follows:

```text
L → R → N
```

So:

```text
Left → Right → Node
```

For:

```text
        10
       /  \
     20    30
    /  \
   40   50
```

Traversal:

```text
40 → 50 → 20 → 30 → 10
```

### Code

```python
def postorder(root):

    if root is None:
        return

    postorder(root.left)
    postorder(root.right)

    print(root.data)
```

Call:

```python
postorder(root)
```

### Pattern to remember

```text
Go Left
   ↓
Go Right
   ↓
Process Node
```

---

# 8. Quick Comparison of DFS Traversals

For:

```text
        10
       /  \
     20    30
    /  \
   40   50
```

| Traversal | Order | Output |
|---|---|---|
| Preorder | NLR | `10 20 40 50 30` |
| Inorder | LNR | `40 20 50 10 30` |
| Postorder | LRN | `40 50 20 30 10` |

### Easy way to remember

```text
Preorder  → Node comes first
Inorder   → Node comes in middle
Postorder → Node comes last
```

---

# 9. Level Order Traversal

Level Order Traversal visits nodes **level by level**.

It uses **BFS (Breadth First Search)**.

For:

```text
        10
       /  \
     20    30
    /  \
   40   50
```

Output:

```text
10
20 30
40 50
```

---

# 10. Why `deque`?

For Level Order Traversal, we need a **queue**.

Python provides an efficient queue using:

```python
from collections import deque
```

Create a queue:

```python
q = deque()
```

Important operations:

```python
q.append(x)      # Add to rear
q.popleft()      # Remove from front
```

This gives us FIFO behavior:

```text
First In → First Out
```

---

# 11. Level Order Traversal Using `None`

We can use `None` as a marker to identify the end of each level.

```python
from collections import deque

q = deque()

def levelOrderTraversal(root):

    if root is None:
        return

    q.append(root)
    q.append(None)

    while q:

        front = q.popleft()

        if front is None:

            print('')

            if q:
                q.append(None)

        else:

            print(front.data, end=' ')

            if front.left is not None:
                q.append(front.left)

            if front.right is not None:
                q.append(front.right)
```

Call:

```python
levelOrderTraversal(root)
```

Output:

```text
10
20 30
40 50
```

---

# 12. How Level Order Works

Initially:

```text
Queue:

10
None
```

Process `10`:

```text
Queue:

None
20
30
```

When `None` is found:

```python
if front is None:
```

it means:

```text
Current level is completed.
```

So we print a new line and add another `None` if nodes are still present.

---

# 13. Complete Code

```python
from collections import deque


class Tree:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Creating tree

root = Tree(10)

root.left = Tree(20)
root.right = Tree(30)

root.left.left = Tree(40)
root.left.right = Tree(50)


# NLR - Preorder

def preorder(root):

    if root is None:
        return

    print(root.data)

    preorder(root.left)
    preorder(root.right)


# LNR - Inorder

def inorder(root):

    if root is None:
        return

    inorder(root.left)

    print(root.data)

    inorder(root.right)


# LRN - Postorder

def postorder(root):

    if root is None:
        return

    postorder(root.left)
    postorder(root.right)

    print(root.data)


# Level Order

q = deque()


def levelOrderTraversal(root):

    if root is None:
        return

    q.append(root)
    q.append(None)

    while q:

        front = q.popleft()

        if front is None:

            print('')

            if q:
                q.append(None)

        else:

            print(front.data, end=' ')

            if front.left is not None:
                q.append(front.left)

            if front.right is not None:
                q.append(front.right)


preorder(root)

inorder(root)

postorder(root)

levelOrderTraversal(root)
```

---

# 14. Traversal Summary

For this tree:

```text
        10
       /  \
     20    30
    /  \
   40   50
```

Remember:

```text
Preorder  → NLR → 10 20 40 50 30

Inorder   → LNR → 40 20 50 10 30

Postorder → LRN → 40 50 20 30 10

LevelOrder       → 10 / 20 30 / 40 50
```

---

# 15. Complexity

For all four traversals:

```text
Time Complexity: O(n)
```

Because every node is visited once.

For recursive DFS:

```text
Space Complexity: O(h)
```

where `h` is the height of the tree because of the recursion stack.

For Level Order:

```text
Space Complexity: O(n)
```

in the worst case because the queue can contain many nodes.

---

# 16. Interview Points from Lecture 1

You should be able to answer:

### Q1. What are the three DFS traversals?

```text
Preorder
Inorder
Postorder
```

### Q2. What is the order of Preorder?

```text
NLR
Node → Left → Right
```

### Q3. What is the order of Inorder?

```text
LNR
Left → Node → Right
```

### Q4. What is the order of Postorder?

```text
LRN
Left → Right → Node
```

### Q5. Which traversal uses a queue?

```text
Level Order / BFS
```

### Q6. Why use `deque`?

Because:

```python
popleft()
```

provides efficient removal from the front of the queue.

### Q7. What is the base case in recursive tree traversal?

```python
if root is None:
    return
```

### Q8. What happens if we change the position of `print(root.data)`?

It changes the traversal:

```text
print before recursion  → Preorder
print between recursion  → Inorder
print after recursion   → Postorder
```

---

# 🎯 Lecture 1 Checklist

- [ ] Understand Binary Tree Node
- [ ] Create a Binary Tree manually
- [ ] Understand recursion on trees
- [ ] Preorder — NLR
- [ ] Inorder — LNR
- [ ] Postorder — LRN
- [ ] Level Order — BFS
- [ ] Understand `deque`
- [ ] Understand `None` as a level marker
- [ ] Know traversal time complexity
- [ ] Know recursive DFS space complexity
- [ ] Be able to write all four traversals without looking at code