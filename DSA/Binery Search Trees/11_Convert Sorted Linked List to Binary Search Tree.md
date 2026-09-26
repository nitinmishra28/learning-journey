# Convert Sorted Linked List to Binary Search Tree

## 1. Problem

Given the head of a **sorted singly linked list**, convert it into a **height-balanced Binary Search Tree (BST)**.

### Example

Input Linked List:

```text
-10 → -3 → 0 → 5 → 9
```

One possible balanced BST:

```text
        0
       / \
     -3   9
     /   /
   -10   5
```

The inorder traversal of the tree is:

```text
-10 → -3 → 0 → 5 → 9
```

which is exactly the original sorted linked list.

---

# 2. Important Observation

This problem is similar to:

```text
Sorted Array → Balanced BST
```

The main difference is:

### Sorted Array

We can directly access the middle element:

```python
nums[mid]
```

because arrays support random access.

### Linked List

We cannot directly access:

```python
head[mid]
```

because a linked list must be traversed node by node.

So we need a different technique.

---

# 3. Brute Force Approach

## Idea

We can repeatedly find the middle node of the linked list.

For each recursive call:

1. Find the middle node using slow/fast pointers.
2. Make it the root.
3. Recursively build the left subtree from the left half.
4. Recursively build the right subtree from the right half.

Example:

```text
-10 → -3 → 0 → 5 → 9
              ↑
             mid
```

`0` becomes the root.

Then:

```text
Left half:
-10 → -3

Right half:
5 → 9
```

### Problem

Finding the middle repeatedly requires traversing portions of the linked list again and again.

### Complexity

```text
Time:  O(n log n)
Space: O(log n)
```

The recursion depth is `O(log n)` for a balanced tree.

There is a better approach that runs in:

```text
O(n)
```

---

# 4. Optimized Approach

The key idea is:

> Instead of finding the middle node repeatedly, build the tree according to the number of nodes and move the linked-list pointer only once.

We first find:

```text
n = length of linked list
```

Then recursively construct a balanced BST containing exactly `n` nodes.

---

# 5. Main Idea

Suppose:

```text
Linked List:

1 → 2 → 3 → 4 → 5 → 6 → 7
```

There are:

```text
n = 7
```

nodes.

To create a balanced BST:

```text
        4
       / \
      2   6
     / \ / \
    1  3 5  7
```

We need:

```text
Left subtree  = 3 nodes
Root           = 1 node
Right subtree = 3 nodes
```

For `n` nodes:

```python
left nodes = n // 2
right nodes = n - n // 2 - 1
```

---

# 6. The Important Trick

We don't actually find the middle node.

Instead, we build the tree **in inorder order**.

Remember:

```text
Inorder:

Left → Root → Right
```

Suppose the linked list is:

```text
1 → 2 → 3 → 4 → 5
```

The desired BST's inorder should be:

```text
1 → 2 → 3 → 4 → 5
```

So we recursively build:

```text
Left subtree
      ↓
Current linked-list node becomes root
      ↓
Move linked-list pointer
      ↓
Right subtree
```

This exactly matches inorder traversal.

---

# 7. Complete Code

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def getLength(self, head):

        cnt = 0

        while head:
            cnt += 1
            head = head.next

        return cnt

    def solve(self, n):

        # No nodes to create
        if n <= 0:
            return None

        # Left subtree
        leftSubTree = self.solve(n // 2)

        # Current linked-list node becomes root
        root = TreeNode(self.head.val)

        # Attach left subtree
        root.left = leftSubTree

        # Move linked-list pointer
        self.head = self.head.next

        # Right subtree
        rightSubTree = self.solve(n - n // 2 - 1)

        # Attach right subtree
        root.right = rightSubTree

        return root

    def sortedListToBST(
        self,
        head: ListNode | None
    ) -> TreeNode | None:

        # Store linked-list pointer
        self.head = head

        # Find total number of nodes
        n = self.getLength(head)

        # Build balanced BST
        return self.solve(n)
```

---

# 8. Why Do We Store `self.head`?

This is one of the most important parts of the solution.

We need a linked-list pointer that keeps moving forward as tree nodes are created.

Initially:

```text
self.head
    ↓
1 → 2 → 3 → 4 → 5
```

When we create the root using `1`:

```python
root = TreeNode(self.head.val)
```

then move:

```python
self.head = self.head.next
```

Now:

```text
self.head
    ↓
2 → 3 → 4 → 5
```

Then after creating the next tree node:

```text
self.head
    ↓
3 → 4 → 5
```

And so on.

So `self.head` acts like a **shared pointer** across all recursive calls.

---

# 9. Why Build the Left Subtree First?

This is the most important idea.

Suppose:

```text
Linked List:

1 → 2 → 3 → 4 → 5
```

We want:

```text
        3
       / \
      1   4
       \   \
        2   5
```

Inorder traversal is:

```text
1 → 2 → 3 → 4 → 5
```

Therefore, before creating the root `3`, we must create the left subtree containing:

```text
1, 2
```

So:

```python
leftSubTree = self.solve(n // 2)
```

comes first.

Only after the left subtree is complete do we use:

```python
self.head
```

to create the current root.

---

# 10. The Most Important Sequence

Remember this order:

```python
# 1. Build left subtree
leftSubTree = self.solve(n // 2)

# 2. Create root from current linked-list node
root = TreeNode(self.head.val)

# 3. Attach left subtree
root.left = leftSubTree

# 4. Move linked-list pointer
self.head = self.head.next

# 5. Build right subtree
rightSubTree = self.solve(n - n // 2 - 1)

# 6. Attach right subtree
root.right = rightSubTree
```

This is basically simulating:

```text
L → N → R
```

---

# 11. Why `n // 2` for the Left Subtree?

Suppose:

```text
n = 7
```

Then:

```python
n // 2
```

gives:

```text
7 // 2 = 3
```

So:

```text
Left subtree = 3 nodes
Root = 1 node
Right subtree = 3 nodes
```

Perfectly balanced.

For:

```text
n = 5
```

we get:

```text
5 // 2 = 2
```

Therefore:

```text
Left subtree = 2
Root         = 1
Right subtree = 2
```

---

# 12. Why Is Right Subtree Size

```python
n - n // 2 - 1
```

?

There are `n` total nodes.

We use:

```text
n // 2
```

nodes for the left subtree.

We use:

```text
1
```

node for the root.

Whatever remains belongs to the right subtree.

Therefore:

```text
Right subtree
=
n - left nodes - root
```

which is:

```python
n - n // 2 - 1
```

Example:

```text
n = 7

Left  = 7 // 2 = 3
Root  = 1
Right = 7 - 3 - 1
      = 3
```

---

# 13. Dry Run

Consider:

```text
Linked List:

1 → 2 → 3 → 4 → 5 → 6 → 7
```

Initially:

```text
self.head → 1
n = 7
```

Call:

```python
solve(7)
```

---

## Root Structure

```text
left = solve(3)
root = current linked-list node
right = solve(3)
```

The left subtree is built first.

### `solve(3)`

```text
left = solve(1)
root = 2
right = solve(1)
```

### `solve(1)`

```text
left = None
root = 1
move head
right = None
```

Now:

```text
    1
```

Then root `2` is created:

```text
    2
   /
  1
```

Then the next node becomes:

```text
3
```

So:

```text
    2
   / \
  1   3
```

The process continues.

Final tree:

```text
        4
       / \
      2   6
     / \ / \
    1  3 5  7
```

---

# 14. Why Does `self.head` Move Only Once?

This is the reason the optimized solution is `O(n)`.

Every time we create a tree node:

```python
self.head = self.head.next
```

moves the linked-list pointer exactly one step.

There are `n` tree nodes.

Therefore:

```text
head moves n times
```

We never move backward.

We never repeatedly search for the middle.

So the linked list is processed in one pass.

---

# 15. Recursion Visualization

For:

```text
1 → 2 → 3 → 4 → 5
```

we need:

```text
        3
       / \
      1   4
       \   \
        2   5
```

The recursion conceptually does:

```text
solve(5)
│
├── solve(2)
│   │
│   ├── solve(1)
│   │
│   ├── create 2
│   │
│   └── solve(0)
│
├── create 3
│
└── solve(2)
    │
    ├── solve(1)
    │
    ├── create 4
    │
    └── solve(0)
```

The linked-list pointer moves:

```text
1 → 2 → 3 → 4 → 5
```

exactly in inorder order.

---

# 16. Why This Is Similar to Sorted Array → BST

For a sorted array:

```text
[1, 2, 3, 4, 5]
```

we can directly select:

```text
mid = 2
```

and create:

```text
root = 3
```

For a linked list, we cannot directly access the middle.

Instead:

```text
Array:
Random Access
     ↓
Pick Middle

Linked List:
No Random Access
     ↓
Simulate Inorder
     ↓
Use Current Pointer
```

The final idea is the same:

```text
Left Half → Root → Right Half
```

but the implementation is different.

---

# 17. Why We Don't Use Slow/Fast Pointer in Optimized Solution

A common solution is:

```text
Find middle using slow/fast
       ↓
Create root
       ↓
Repeat
```

But every recursive level searches for another middle.

This can lead to:

```text
O(n log n)
```

time.

Our solution instead knows the number of nodes in every subtree:

```text
Left size
Root
Right size
```

and consumes the linked list once.

Therefore:

```text
Time = O(n)
```

---

# 18. Complexity

## Step 1 — Find Length

```python
n = self.getLength(head)
```

We traverse the linked list once:

```text
O(n)
```

## Step 2 — Build Tree

Every linked-list node becomes exactly one tree node:

```text
O(n)
```

Therefore:

```text
Total Time = O(n)
```

---

## Space Complexity

The recursion depth is equal to the height of the balanced BST:

```text
O(log n)
```

Therefore:

```text
Auxiliary Space = O(log n)
```

The output tree itself contains:

```text
O(n)
```

nodes.

So:

```text
Time:
O(n)

Auxiliary Space:
O(log n)

Output Space:
O(n)
```

---

# 19. Common Mistakes

## 1. Trying to use `head[mid]`

Linked lists don't support random access.

This doesn't work:

```python
head[mid]
```

You have to move node by node.

---

## 2. Building the root before the left subtree

Wrong idea:

```python
root = TreeNode(self.head.val)

leftSubTree = self.solve(...)
```

This breaks the inorder simulation.

Correct:

```python
leftSubTree = self.solve(n // 2)

root = TreeNode(self.head.val)
```

---

## 3. Forgetting to move `self.head`

After consuming a linked-list node:

```python
self.head = self.head.next
```

must happen.

Otherwise, multiple tree nodes may use the same linked-list value.

---

## 4. Using the wrong right subtree size

Correct:

```python
n - n // 2 - 1
```

because:

```text
total nodes
- left nodes
- root
= right nodes
```

---

## 5. Using a local linked-list pointer

If we pass a normal local pointer through recursion without carefully returning it, keeping all recursive calls synchronized becomes difficult.

Using:

```python
self.head
```

gives all recursive calls access to the same moving pointer.

---

# 20. Important Recursion Insight

This problem is a very good example of using recursion to **simulate an inorder traversal**.

Normally, inorder traversal is:

```text
Left
 ↓
Node
 ↓
Right
```

Here:

```python
leftSubTree = self.solve(n // 2)
```

means:

```text
Build Left
```

Then:

```python
root = TreeNode(self.head.val)
```

means:

```text
Process Node
```

Then:

```python
rightSubTree = self.solve(...)
```

means:

```text
Build Right
```

So:

```text
solve()
=
Left → Node → Right
```

---

# 21. Pattern Recognition

When you see:

```text
Sorted Linked List
+
Balanced BST
```

think:

```text
Find length
     ↓
Know how many nodes belong
to left/right subtree
     ↓
Build left subtree
     ↓
Use current linked-list node as root
     ↓
Move linked-list pointer
     ↓
Build right subtree
```

The key pattern is:

> **Build the tree in inorder while consuming the linked list from left to right.**

---

# 22. Revision Cheat Sheet

```text
Sorted Linked List → Balanced BST

1. Find length:
   n = getLength(head)

2. Store shared pointer:
   self.head = head

3. solve(n):

   if n <= 0:
       return None

   # Left
   left = solve(n // 2)

   # Node
   root = TreeNode(self.head.val)

   # Attach left
   root.left = left

   # Move linked-list pointer
   self.head = self.head.next

   # Right
   right = solve(n - n // 2 - 1)

   # Attach right
   root.right = right

   return root
```

### Core Formula

```text
Left nodes  = n // 2

Root nodes  = 1

Right nodes = n - n // 2 - 1
```

### Complexity

```text
Time  = O(n)
Space = O(log n) auxiliary
```

### Core Pattern

```text
Linked List
     ↓
Inorder Simulation
     ↓
Left Subtree
     ↓
Current List Node = Root
     ↓
Move List Pointer
     ↓
Right Subtree
```

> **One-Line Pattern: Sorted Linked List to BST = Use subtree sizes to simulate inorder and consume the linked list exactly once.**