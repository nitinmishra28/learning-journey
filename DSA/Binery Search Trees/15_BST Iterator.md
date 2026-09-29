# BST Iterator

## 1. Problem

Design an iterator over a **Binary Search Tree (BST)**.

The iterator should support:

```python
next()
```

Returns the next smallest value in the BST.

And:

```python
hasNext()
```

Returns whether another value is available.

### Example

```text
        7
       / \
      3   15
         /  \
        9    20
```

Inorder traversal is:

```text
3 → 7 → 9 → 15 → 20
```

The iterator should return values in this order:

```text
next() → 3
next() → 7
next() → 9
next() → 15
next() → 20
```

---

# 2. Important Observation

A BST's inorder traversal:

```text
Left → Node → Right
```

produces values in **sorted order**.

So the problem is basically:

> How can we perform inorder traversal **one node at a time** instead of traversing the entire tree at once?

A normal inorder traversal would be:

```python
def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.val)
    inorder(root.right)
```

But an iterator cannot return all values at once.

We need to **pause the traversal**, return one value, and continue from where we stopped.

---

# 3. Brute Force Approach

The simplest approach is to perform a complete inorder traversal during initialization and store all values in an array.

```python
class BSTIterator:

    def __init__(self, root):
        self.inorder = []

        def traverse(root):
            if root is None:
                return

            traverse(root.left)
            self.inorder.append(root.val)
            traverse(root.right)

        traverse(root)

        self.index = 0

    def next(self):
        value = self.inorder[self.index]
        self.index += 1
        return value

    def hasNext(self):
        return self.index < len(self.inorder)
```

### Complexity

```text
Initialization:
O(n)

next():
O(1)

hasNext():
O(1)

Extra Space:
O(n)
```

The problem is that we store the **entire inorder traversal** even though we only need the next value at a time.

---

# 4. Optimized Approach

Instead of storing every node, we simulate inorder traversal using a **stack**.

The stack stores only the nodes that we need to visit later.

The key idea is:

```text
Always push the entire left path.
```

For this tree:

```text
        7
       / \
      3   15
```

Initially:

```text
        7
       /
      3
```

We push:

```text
7
3
```

Stack:

```text
TOP
 ↓
[3]
[7]
```

The top of the stack is the next smallest element.

---

# 5. Main Idea

There are two important operations.

### `pushLeftNodes(root)`

Keep moving left and push every node:

```python
while root:
    self.stack.append(root)
    root = root.left
```

This prepares the stack for the next smallest node.

---

### `next()`

Take the top node:

```python
top = self.stack.pop()
```

That node is the next smallest value.

But there is one important case.

If the node has a right subtree:

```python
if top.right:
    self.pushLeftNodes(top.right)
```

Why?

Because after visiting:

```text
Left → Node
```

inorder traversal must continue with:

```text
Right
```

And the next smallest node in the right subtree is its **leftmost node**.

---

# 6. Your Code

```python
class BSTIterator:

    def __init__(self, root: TreeNode | None):
        self.stack = []
        self.pushLeftNodes(root)

    def pushLeftNodes(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        top = self.stack.pop()

        if top.right:
            self.pushLeftNodes(top.right)

        return top.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0
```

---

# 7. Understanding `pushLeftNodes()`

This function is the heart of the iterator.

```python
def pushLeftNodes(self, root):
    while root:
        self.stack.append(root)
        root = root.left
```

Suppose:

```text
        7
       /
      3
     /
    1
```

Calling:

```python
self.pushLeftNodes(7)
```

does:

```text
push 7
move to 3

push 3
move to 1

push 1
move to None
```

Stack:

```text
TOP
 ↓
[1]
[3]
[7]
```

Why do we push all of them?

Because inorder traversal must visit:

```text
1 → 3 → 7
```

So `1` must be ready first.

---

# 8. Understanding `next()`

Consider:

```text
        7
       / \
      3   15
         /
        9
```

Initially:

```text
stack:

[3]
[7]
```

Call:

```python
next()
```

We pop:

```text
3
```

There is no right subtree.

Return:

```text
3
```

---

Now stack:

```text
[7]
```

Call:

```python
next()
```

Pop:

```text
7
```

`7` has a right subtree:

```text
15
/
9
```

So:

```python
self.pushLeftNodes(15)
```

pushes:

```text
15
9
```

Stack becomes:

```text
TOP
 ↓
[9]
[15]
```

Return:

```text
7
```

---

Next:

```python
next()
```

Pop:

```text
9
```

Return:

```text
9
```

Then:

```text
next() → 15
```

---

# 9. Why Do We Only Push the Right Subtree's Left Path?

This is one of the most important things to understand.

Suppose:

```text
        10
       /  \
      5    20
          /  \
         15   30
        /
       12
```

After visiting `10`, inorder says:

```text
Left → 10 → Right
```

So we now need to process:

```text
20
```

But inside the right subtree:

```text
        20
       /
      15
     /
    12
```

the smallest node is:

```text
12
```

Therefore:

```python
pushLeftNodes(20)
```

pushes:

```text
20
15
12
```

Stack:

```text
TOP
 ↓
[12]
[15]
[20]
```

So the next call returns `12`.

This exactly simulates recursive inorder traversal.

---

# 10. Connection With Recursive Inorder

Recursive inorder:

```python
def inorder(root):
    if root is None:
        return

    inorder(root.left)

    print(root.val)

    inorder(root.right)
```

The recursion stack automatically remembers:

```text
"After I finish the left subtree,
come back to this node."
```

Our explicit stack does the same thing.

### Recursive version

```text
Call Stack
    ↓
remember nodes
```

### Iterator version

```text
self.stack
    ↓
remember nodes
```

So the iterator is essentially:

> **Iterative inorder traversal where execution can be paused after every node.**

---

# 11. `hasNext()`

Your implementation is:

```python
def hasNext(self) -> bool:
    return len(self.stack) > 0
```

If the stack is not empty:

```text
There is still a node waiting to be processed.
```

Therefore:

```text
True
```

If the stack is empty:

```text
There are no more nodes.
```

Therefore:

```text
False
```

We don't need to traverse the tree again.

---

# 12. Dry Run

Consider:

```text
        7
       / \
      3   15
         /  \
        9    20
```

### Initialization

```python
BSTIterator(root)
```

Calls:

```python
pushLeftNodes(7)
```

Stack:

```text
[7, 3]
```

Top:

```text
3
```

---

### Call 1

```python
next()
```

Pop:

```text
3
```

Stack:

```text
[7]
```

Return:

```text
3
```

---

### Call 2

```python
next()
```

Pop:

```text
7
```

7 has right subtree.

Push left path of `15`:

```text
15 → 9
```

Stack:

```text
[15, 9]
```

Return:

```text
7
```

---

### Call 3

```python
next()
```

Pop:

```text
9
```

No right subtree.

Stack:

```text
[15]
```

Return:

```text
9
```

---

### Call 4

```python
next()
```

Pop:

```text
15
```

Push left path of `20`:

```text
20
```

Stack:

```text
[20]
```

Return:

```text
15
```

---

### Call 5

```python
next()
```

Pop:

```text
20
```

Stack:

```text
[]
```

Return:

```text
20
```

Now:

```python
hasNext()
```

returns:

```text
False
```

Final output:

```text
3 → 7 → 9 → 15 → 20
```

---

# 13. Why `next()` Is Not Always O(1)

It is tempting to say:

```text
next() = O(1)
```

because we normally only do:

```python
self.stack.pop()
```

But sometimes:

```python
if top.right:
    self.pushLeftNodes(top.right)
```

can push several nodes.

For example:

```text
        10
          \
           20
          /
         15
        /
       12
```

One call to `next()` could push:

```text
20
15
12
```

So a **single call** can take `O(h)`.

However, across the entire traversal, every node is pushed and popped only once.

Therefore the **amortized complexity** of `next()` is:

```text
O(1) amortized
```

And traversing all `n` nodes takes:

```text
O(n)
```

---

# 14. Complexity

Let:

```text
n = number of nodes
h = height of BST
```

### Initialization

We push only the left path:

```text
O(h)
```

### `next()`

Amortized:

```text
O(1)
```

Each node is pushed and popped once over the complete iteration.

### `hasNext()`

```text
O(1)
```

### Space

The stack contains at most one root-to-leaf path:

```text
O(h)
```

For a balanced BST:

```text
O(log n)
```

For a skewed BST:

```text
O(n)
```

### Final Complexity

```text
Initialization : O(h)
next()         : O(1) amortized
hasNext()      : O(1)
Space          : O(h)
```

Compared with storing the complete inorder traversal:

```text
Brute Force:
Space = O(n)

Optimized:
Space = O(h)
```

---

# 15. Important Recursion / Stack Concept

This problem is a good example of converting:

```text
Recursion
```

into:

```text
Explicit Stack
```

Normal inorder recursion automatically stores nodes in the call stack.

For example:

```text
inorder(7)
   |
   └── inorder(3)
          |
          └── inorder(1)
```

Python's call stack remembers:

```text
7
3
```

while going left.

In the iterator, we manually store those nodes:

```python
self.stack.append(root)
```

So:

```text
Recursive Call Stack
        ↓
    Explicit Stack
```

Both are doing the same fundamental job:

> **Remember where to return after processing the left subtree.**

---

# 16. Common Mistakes

### Mistake 1: Pushing only the root

Wrong:

```python
self.stack.append(root)
```

You need the entire left path.

Correct:

```python
while root:
    self.stack.append(root)
    root = root.left
```

---

### Mistake 2: Forgetting the right subtree

After popping a node:

```python
top = self.stack.pop()
```

you must process its right subtree.

Correct:

```python
if top.right:
    self.pushLeftNodes(top.right)
```

---

### Mistake 3: Pushing the entire right subtree

We don't push the entire right subtree immediately.

We only push its **left path**.

```text
Right subtree
      ↓
Move left as much as possible
      ↓
Push that path
```

---

### Mistake 4: Storing all values

You could store:

```python
[3, 7, 9, 15, 20]
```

but that uses:

```text
O(n)
```

extra space.

The iterator only needs to remember the nodes required for future traversal.

---

# 17. Pattern Recognition

When you see:

```text
BST
+
Need values in sorted order
+
Need one value at a time
```

Think:

```text
BST
 ↓
Inorder Traversal
 ↓
Sorted Order
 ↓
Iterative Inorder
 ↓
Explicit Stack
```

The standard pattern is:

```text
Push Left Path
      ↓
Pop Smallest
      ↓
If Right Exists:
    Push Its Left Path
      ↓
Repeat
```

---

# 18. Revision Cheat Sheet

```text
Problem:
Implement BST Iterator

BST property:
Inorder = Sorted Order

Core Pattern:
Iterative Inorder Traversal

Initialization:
Push entire left path.

next():
1. Pop top node.
2. If it has a right subtree,
   push the right subtree's left path.
3. Return popped node's value.

hasNext():
stack is not empty

Why stack?
It simulates the recursion stack of inorder traversal.

Why push left path?
The leftmost node is the next smallest value.

Why process right subtree after pop?
Inorder = Left → Node → Right

Complexity:
Initialization = O(h)
next()        = O(1) amortized
hasNext()     = O(1)
Space         = O(h)

One-Line Pattern:
BST Iterator = Iterative Inorder Traversal + Stack + Push Left Path.
```