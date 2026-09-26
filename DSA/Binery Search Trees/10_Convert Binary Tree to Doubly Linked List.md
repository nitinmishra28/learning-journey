# Convert Binary Tree to Doubly Linked List

## 1. Problem

Given a Binary Tree, convert it into a **Doubly Linked List (DLL)**.

The nodes in the DLL should follow the **inorder traversal** of the Binary Tree:

```text
Left → Node → Right
```

Each node's pointers become:

```text
left  → previous node
right → next node
```

### Example

Binary Tree:

```text
        10
       /  \
      5    20
     / \   / \
    2   7 15 25
```

Inorder traversal:

```text
2 → 5 → 7 → 10 → 15 → 20 → 25
```

DLL:

```text
None ← 2 ⇄ 5 ⇄ 7 ⇄ 10 ⇄ 15 ⇄ 20 ⇄ 25 → None
```

The first node is the:

```text
head
```

and the last node is the:

```text
tail
```

---

# 2. Brute Force

## Idea

A simple approach is:

1. Perform inorder traversal.
2. Store all nodes in an array/list.
3. Connect consecutive nodes.

Example:

```text
Inorder:

2 → 5 → 7 → 10 → 15 → 20 → 25
```

Then connect:

```text
2 ⇄ 5
5 ⇄ 7
7 ⇄ 10
10 ⇄ 15
15 ⇄ 20
20 ⇄ 25
```

### Complexity

```text
Time:  O(n)
Space: O(n)
```

The extra `O(n)` space comes from storing all nodes.

We can do the conversion **in-place** without using an array.

---

# 3. Optimized Approach 1 — Reverse Inorder Using `head`

The first optimized approach uses:

```text
RNL

Right → Node → Left
```

Instead of normal inorder:

```text
LNR

Left → Node → Right
```

---

# 4. Why Reverse Inorder?

For a BST, reverse inorder gives:

```text
Largest → Smallest
```

But this problem is a general Binary Tree problem where the required DLL order is inorder.

The trick is that we process nodes in reverse order and keep adding the current node **before** the already processed nodes.

Example:

```text
Reverse Inorder:

25 → 20 → 15 → 10 → 7 → 5 → 2
```

We build:

```text
25

20 ⇄ 25

15 ⇄ 20 ⇄ 25

10 ⇄ 15 ⇄ 20 ⇄ 25

...
```

At the end:

```text
2 ⇄ 5 ⇄ 7 ⇄ 10 ⇄ 15 ⇄ 20 ⇄ 25
```

The `head` keeps moving toward the smaller nodes.

---

# 5. Complete Code — Approach 1

```python
''' Structure for tree and linked list
class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None
'''

class Solution:

    def solve(self, root, head):

        if root is None:
            return head

        # RNL

        # R - Right
        head = self.solve(root.right, head)

        # Connect current node to already processed DLL
        root.right = head

        # Connect previous node back to current node
        if head is not None:
            head.left = root

        # Current node becomes the new head
        head = root

        # L - Left
        head = self.solve(root.left, head)

        return head

    def treeToDLL(self, root):

        head = None

        head = self.solve(root, head)

        return head
```

---

# 6. Most Important Concept — Why `head = self.solve(...)`?

This is the part that is easy to get stuck on.

You might think:

```python
self.solve(root.right, head)
```

is enough.

But it is not.

The function:

```python
solve()
```

returns an **updated `head`**.

Therefore, we need to store that returned value:

```python
head = self.solve(root.right, head)
```

The same thing happens here:

```python
head = self.solve(root.left, head)
```

---

# 7. One-Line Rule

Remember:

> **Function agar updated value return kar raha hai, aur tumhe woh updated value aage use karni hai, to usko variable mein assign karna padega.**

In this problem:

```python
head = self.solve(root.right, head)
```

means:

```text
solve()
   ↓
process nodes
   ↓
return updated head
   ↓
store it in head
   ↓
use new head
```

---

# 8. What Happens If We Don't Store It?

Suppose we write:

```python
self.solve(root.right, head)

root.right = head
```

The recursive function may have found a new head.

But that returned value is ignored.

The caller's `head` still contains the old value.

For example:

```python
def change(x):
    x = 10
    return x
```

If we do:

```python
x = 5

change(x)

print(x)
```

we still get:

```text
5
```

because the returned value was ignored.

But:

```python
x = change(x)
```

gives:

```text
10
```

Exactly the same idea applies here:

```python
head = self.solve(...)
```

---

# 9. Why Does `head` Keep Changing?

Consider:

```text
        10
       /  \
      5    20
```

Reverse inorder:

```text
20 → 10 → 5
```

Initially:

```text
head = None
```

### Process 20

```text
20.right = None

head = 20
```

Now:

```text
head
 ↓
20
```

### Process 10

```text
10.right = 20
20.left = 10

head = 10
```

Now:

```text
head
 ↓
10 ⇄ 20
```

### Process 5

```text
5.right = 10
10.left = 5

head = 5
```

Now:

```text
head
 ↓
5 ⇄ 10 ⇄ 20
```

So:

```text
head
```

keeps moving backward.

At the end, `head` points to the smallest/inorder-first node.

---

# 10. Pointer Logic

These three operations are the heart of Approach 1:

```python
root.right = head

if head is not None:
    head.left = root

head = root
```

Suppose:

```text
head
 ↓
20 ⇄ 25
```

and current node is:

```text
15
```

### Step 1

```python
root.right = head
```

creates:

```text
15 → 20
```

### Step 2

```python
head.left = root
```

creates:

```text
15 ⇄ 20
```

### Step 3

```python
head = root
```

moves the head:

```text
head
 ↓
15 ⇄ 20 ⇄ 25
```

---

# 11. Optimized Approach 2 — Normal Inorder Using `head` and `tail`

The second approach is more intuitive because it directly follows the required DLL order:

```text
LNR

Left → Node → Right
```

Instead of only maintaining `head`, we maintain:

```text
head
tail
```

Where:

```text
head = first node of DLL
tail = last node processed so far
```

This makes connecting the current node very straightforward.

---

# 12. Main Idea of Approach 2

Suppose inorder gives:

```text
2 → 5 → 7 → 10
```

When processing nodes:

### First node

```text
2
```

There is no previous node.

So:

```text
head = 2
tail = 2
```

### Next node

```text
5
```

Connect:

```text
tail.right = root
root.left = tail
```

So:

```text
2 ⇄ 5
```

Then:

```text
tail = root
```

Now:

```text
head = 2
tail = 5
```

### Next node

```text
7
```

Connect:

```text
5 ⇄ 7
```

Then:

```text
tail = 7
```

Continue the same process.

---

# 13. Complete Code — Approach 2

```python
''' Structure for tree and linked list
class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None
'''

class Solution:

    def solve(self, root, head, tail):

        if root is None:
            return head, tail

        # LNR

        # L - Left
        head, tail = self.solve(root.left, head, tail)

        # N - Node
        if tail is not None:

            # Connect previous node to current node
            tail.right = root

            # Connect current node back to previous node
            root.left = tail

            # Current node becomes the new tail
            tail = root

        else:

            # First node of DLL
            head = root
            tail = root

        # R - Right
        head, tail = self.solve(root.right, head, tail)

        return head, tail

    def treeToDLL(self, root):

        head = None
        tail = None

        head, tail = self.solve(root, head, tail)

        return head
```

---

# 14. Why Do We Need Both `head` and `tail`?

This is the main difference between the two approaches.

### Approach 1

Uses:

```text
head
```

and processes:

```text
Right → Node → Left
```

### Approach 2

Uses:

```text
head + tail
```

and processes:

```text
Left → Node → Right
```

With normal inorder, we naturally encounter nodes from:

```text
first → last
```

So we need `tail` to know where to attach the current node.

---

# 15. Understanding `tail`

Suppose:

```text
head
 ↓
2 ⇄ 5 ⇄ 7
         ↑
        tail
```

Now current node is:

```text
10
```

`tail` tells us:

```text
7 is the previous node
```

So:

```python
tail.right = root
```

creates:

```text
7 → 10
```

and:

```python
root.left = tail
```

creates:

```text
10 → 7
```

Together:

```text
7 ⇄ 10
```

Then:

```python
tail = root
```

moves the tail:

```text
head
 ↓
2 ⇄ 5 ⇄ 7 ⇄ 10
             ↑
            tail
```

---

# 16. Why Do We Return `head, tail`?

This is another important recursion concept.

The recursive function can update both:

```text
head
tail
```

Therefore it returns both:

```python
return head, tail
```

When calling recursively:

```python
head, tail = self.solve(root.left, head, tail)
```

we capture both updated values.

Same for the right subtree:

```python
head, tail = self.solve(root.right, head, tail)
```

---

# 17. The Same Rule Applies Here

The same rule from Approach 1 applies to both variables:

> **If the recursive function returns updated state, store the returned state.**

Therefore:

```python
head, tail = self.solve(...)
```

is necessary.

If we write only:

```python
self.solve(...)
```

we ignore the updated `head` and `tail`.

---

# 18. Why Is `tail` Initially `None`?

Initially the DLL is empty:

```text
head = None
tail = None
```

When we reach the first node during inorder:

```python
if tail is not None:
```

is false.

So:

```python
head = root
tail = root
```

Both point to the first node.

Example:

```text
head
 ↓
2
 ↑
tail
```

After that, every new node can be attached after `tail`.

---

# 19. Dry Run — Approach 2

Tree:

```text
        10
       /  \
      5    20
     / \   / \
    2   7 15 25
```

Inorder:

```text
2 → 5 → 7 → 10 → 15 → 20 → 25
```

### Process 2

First node:

```text
head = 2
tail = 2
```

```text
2
```

### Process 5

```text
tail.right = 5
5.left = tail
tail = 5
```

```text
2 ⇄ 5
```

### Process 7

```text
5 ⇄ 7
```

Now:

```text
head
 ↓
2 ⇄ 5 ⇄ 7
         ↑
        tail
```

### Process 10

```text
7 ⇄ 10
```

### Process 15

```text
10 ⇄ 15
```

### Process 20

```text
15 ⇄ 20
```

### Process 25

```text
20 ⇄ 25
```

Final:

```text
head
 ↓
2 ⇄ 5 ⇄ 7 ⇄ 10 ⇄ 15 ⇄ 20 ⇄ 25
                                      ↑
                                     tail
```

---

# 20. Approach 1 vs Approach 2

| Feature | Approach 1 | Approach 2 |
|---|---|---|
| Traversal | RNL | LNR |
| Order processed | Largest → Smallest | Smallest → Largest |
| Variables | `head` | `head`, `tail` |
| Main connection | Insert before head | Insert after tail |
| Extra array | No | No |
| Time | O(n) | O(n) |
| Space | O(h) | O(h) |
| Easiness | Slightly tricky | More intuitive |

---

# 21. Which Pointer Should You Remember?

For **Approach 1**:

```text
RNL

head = already processed DLL

root.right = head
head.left = root
head = root
```

Think:

```text
Insert current node BEFORE head
```

---

For **Approach 2**:

```text
LNR

tail = last processed node

tail.right = root
root.left = tail
tail = root
```

Think:

```text
Insert current node AFTER tail
```

---

# 22. Why Both Approaches Are O(1) Extra Pointer Space

We are not creating a new linked-list node.

We reuse the existing tree nodes.

The pointers:

```text
left
right
```

are repurposed:

```text
left  → previous
right → next
```

So no extra `Node` objects or array are required.

Only recursion stack space is used.

```text
Space = O(h)
```

---

# 23. Common Mistakes

## 1. Ignoring the returned `head`

Wrong:

```python
self.solve(root.right, head)
```

Correct:

```python
head = self.solve(root.right, head)
```

---

## 2. Ignoring returned `head, tail`

Wrong:

```python
self.solve(root.left, head, tail)
```

Correct:

```python
head, tail = self.solve(root.left, head, tail)
```

---

## 3. Forgetting the reverse pointer

Wrong:

```python
tail.right = root
```

This only creates:

```text
tail → root
```

For a DLL we also need:

```python
root.left = tail
```

giving:

```text
tail ⇄ root
```

---

## 4. Forgetting to update `tail`

After adding a node:

```python
tail = root
```

must be done.

Otherwise `tail` keeps pointing to the old node.

---

## 5. Mixing the traversal logic

Approach 1:

```text
RNL
```

uses:

```text
head
```

Approach 2:

```text
LNR
```

uses:

```text
head + tail
```

Don't mix the pointer logic between the two approaches.

---

# 24. Complexity

For both optimized approaches:

Every tree node is visited exactly once.

```text
Time = O(n)
```

No array or extra linked-list nodes are created.

Recursion stack:

```text
Space = O(h)
```

where `h` is the height of the tree.

For a balanced tree:

```text
O(h) = O(log n)
```

For a skewed tree:

```text
O(h) = O(n)
```

---

# 25. Pattern Recognition

When you see:

```text
Binary Tree
+
Convert to DLL
+
Inorder order required
```

think of two patterns.

### Pattern 1

```text
RNL
 ↓
Reverse Inorder
 ↓
Maintain head
 ↓
Insert current before head
```

### Pattern 2

```text
LNR
 ↓
Normal Inorder
 ↓
Maintain head + tail
 ↓
Insert current after tail
```

---

# 26. Revision Cheat Sheet

## Approach 1 — Reverse Inorder

```text
R → N → L

head = None

Process right

root.right = head

if head:
    head.left = root

head = root

Process left

return head
```

Core idea:

```text
Insert current node BEFORE head
```

---

## Approach 2 — Normal Inorder

```text
L → N → R

head = None
tail = None

Process left

if tail:
    tail.right = root
    root.left = tail
    tail = root
else:
    head = root
    tail = root

Process right

return head, tail
```

Core idea:

```text
Insert current node AFTER tail
```

---

# 27. Most Important Recursion Rule

```text
If a recursive function returns updated state
and you need that state:

    variable = recursive_call(...)
```

For one returned value:

```python
head = self.solve(root.right, head)
```

For two returned values:

```python
head, tail = self.solve(root.left, head, tail)
```

If you don't store the returned value:

```python
self.solve(...)
```

you may lose the updated state.

---

# 28. Final Revision

```text
Tree → DLL

No new nodes.
Reuse tree nodes.

DLL:
left  = previous
right = next
```

### Approach 1

```text
RNL
Right → Node → Left

Maintain:
head

Connect:
root.right = head
head.left = root
head = root
```

### Approach 2

```text
LNR
Left → Node → Right

Maintain:
head + tail

Connect:
tail.right = root
root.left = tail
tail = root
```

Both:

```text
Time  = O(n)
Space = O(h)
```

> **One-Line Pattern: Tree to DLL = Inorder-based traversal + reuse `left/right` pointers + maintain the current DLL boundary (`head` or `head/tail`).**