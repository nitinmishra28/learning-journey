# Flatten Binary Tree to Linked List

## 1. Problem

Given the root of a binary tree, flatten the tree into a **linked list in-place**.

The flattened tree should follow the same order as **preorder traversal**:

```text
Root → Left → Right
```

After flattening:

- Every node's `left` must be `None`.
- Every node's `right` points to the next node in preorder.
- The tree becomes a right-skewed linked list.
- We must modify the original tree **in-place**.

### Example

Original tree:

```text
        1
       / \
      2   5
     / \   \
    3   4   6
```

Preorder traversal:

```text
1 → 2 → 3 → 4 → 5 → 6
```

Flattened tree:

```text
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
```

---

# 2. Brute Force

A straightforward approach is:

1. Perform preorder traversal.
2. Store all nodes in a list.
3. Connect them using their `right` pointers.
4. Set every `left` pointer to `None`.

### Example

Preorder:

```python
nodes = [1, 2, 3, 4, 5, 6]
```

Then:

```text
1.right → 2
2.right → 3
3.right → 4
4.right → 5
5.right → 6
```

and:

```text
1.left = None
2.left = None
...
```

### Complexity

```text
Time  → O(n)
Space → O(n)
```

The time is good, but the problem specifically asks us to modify the tree **in-place**, so we want to avoid storing all nodes.

---

# 3. Pattern

This is a:

```text
Binary Tree
     ↓
Preorder structure
     ↓
In-place modification
     ↓
Move current node
     ↓
Find predecessor
     ↓
Rewire pointers
```

### One-Line Pattern

> **Flatten Tree = In-place preorder restructuring using the rightmost node of the left subtree as a predecessor.**

---

# 4. Main Idea

The important observation is:

For the current node:

```text
        curr
       /    \
    left    right
```

We want preorder:

```text
curr → left subtree → right subtree
```

Therefore, the left subtree must come before the current right subtree.

So we rearrange it:

```text
        curr
       /    \
    left    right
```

into:

```text
        curr
          \
          left
            \
          ... 
            \
           right
```

But there is one problem:

> Where should the original right subtree be attached?

We attach it to the **rightmost node of the left subtree**.

---

# 5. Why Do We Find the Rightmost Node?

Suppose:

```text
        1
       / \
      2   5
     / \
    3   4
```

We want:

```text
1 → 2 → 3 → 4 → 5
```

The left subtree is:

```text
      2
     / \
    3   4
```

The rightmost node is:

```text
4
```

So we connect:

```text
4.right = 5
```

Then move the left subtree to the right:

```text
1.right = 2
```

and remove:

```text
1.left = None
```

Result:

```text
1
 \
  2
 / \
3   4
     \
      5
```

Continuing the process eventually gives:

```text
1 → 2 → 3 → 4 → 5
```

---

# 6. The Core Rewiring

This is the most important part of the code:

```python
pred = curr.left

while pred.right:
    pred = pred.right

pred.right = curr.right
curr.right = curr.left
curr.left = None
```

Let's understand it step by step.

---

## Step 1: Start at Left Subtree

```python
pred = curr.left
```

`pred` initially points to the root of the left subtree.

---

## Step 2: Find the Rightmost Node

```python
while pred.right:
    pred = pred.right
```

We keep moving right.

Why?

Because the rightmost node is the **last node of the left subtree in preorder**.

So it is the correct place to attach the original right subtree.

---

## Step 3: Connect Right Subtree

```python
pred.right = curr.right
```

Before:

```text
curr
 /  \
L    R
```

After:

```text
curr
 /
L
 \
  ...
    \
     R
```

The original right subtree is now connected after the left subtree.

---

## Step 4: Move Left Subtree to Right

```python
curr.right = curr.left
```

Now:

```text
curr
  \
   L
```

This puts the left subtree immediately after `curr`, which matches preorder.

---

## Step 5: Remove Left Pointer

```python
curr.left = None
```

The final flattened structure must contain no left pointers.

---

# 7. Why `pred.right = curr.right` Comes First

This order is important.

Suppose:

```text
curr.left = 2
curr.right = 5
```

If we do:

```python
curr.right = curr.left
```

first, we lose the reference to the original right subtree.

Therefore we first save/connect the original right subtree:

```python
pred.right = curr.right
```

Then:

```python
curr.right = curr.left
```

This preserves the entire tree.

Think:

```text
First connect old right subtree
        ↓
Then move left subtree to right
        ↓
Then remove left pointer
```

---

# 8. Complete Code

```python
class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything,
        modify root in-place instead.
        """

        curr = root

        while curr:

            # If there is no left subtree,
            # current node is already in the correct position.
            if curr.left:

                # Find the rightmost node of the left subtree.
                pred = curr.left

                while pred.right:
                    pred = pred.right

                # Attach the original right subtree
                # after the left subtree.
                pred.right = curr.right

                # Move the left subtree to the right.
                curr.right = curr.left

                # Remove the left pointer.
                curr.left = None

            # Move to the next node in the flattened structure.
            curr = curr.right
```

---

# 9. Dry Run

Consider:

```text
        1
       / \
      2   5
     / \   \
    3   4   6
```

Start:

```text
curr = 1
```

`1` has a left subtree.

Find rightmost node of:

```text
    2
   / \
  3   4
```

Rightmost node:

```text
4
```

So:

```text
pred = 4
```

Connect:

```python
pred.right = curr.right
```

Therefore:

```text
4.right = 5
```

Then:

```python
curr.right = curr.left
```

So:

```text
1.right = 2
```

And:

```python
curr.left = None
```

Tree becomes:

```text
        1
         \
          2
         / \
        3   4
             \
              5
               \
                6
```

Now:

```python
curr = curr.right
```

So:

```text
curr = 2
```

---

## Process Node `2`

Node `2` has:

```text
left = 3
right = 4
```

Find rightmost node of left subtree:

```text
3
```

So:

```python
pred = 3
```

Connect:

```python
pred.right = curr.right
```

Therefore:

```text
3.right = 4
```

Then:

```python
curr.right = curr.left
```

So:

```text
2.right = 3
```

Remove:

```text
2.left = None
```

Now:

```text
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
```

Now continue moving right.

Nodes `3`, `4`, `5`, and `6` already have no left subtree.

So we simply move:

```text
3 → 4 → 5 → 6
```

Final:

```text
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
```

---

# 10. Why Does the Rightmost Node Work?

This is the key insight.

Suppose:

```text
        1
       / \
      2   5
     / \
    3   4
```

Preorder traversal is:

```text
1 → 2 → 3 → 4 → 5
```

The last node of the left subtree in preorder is:

```text
4
```

Therefore the original right subtree should come after `4`.

So:

```text
4.right = 5
```

This gives:

```text
1 → 2 → 3 → 4 → 5
```

That is exactly preorder.

---

# 11. Why Do We Move `curr` to `curr.right`?

After restructuring:

```python
curr.right = curr.left
curr.left = None
```

the next node in the flattened structure is now:

```python
curr.right
```

So:

```python
curr = curr.right
```

moves us forward through the newly created linked list.

Think of `curr` as a pointer moving through:

```text
1 → 2 → 3 → 4 → 5 → 6
```

---

# 12. Why Is This In-Place?

We don't create:

```text
new tree
```

or:

```text
array of nodes
```

We only change existing pointers:

```python
pred.right
curr.right
curr.left
```

Therefore the tree itself is modified.

This satisfies:

```text
Do not return anything.
Modify root in-place.
```

---

# 13. Why Is This Preorder?

Preorder is:

```text
Root → Left → Right
```

For:

```text
        1
       / \
      2   5
```

we want:

```text
1 → 2 → 5
```

Our transformation does exactly this:

```text
curr
  ↓
left subtree
  ↓
original right subtree
```

So the flattened linked list follows preorder traversal.

---

# 14. Important Invariant

At every iteration:

```text
Everything before curr
```

has already been flattened correctly.

For example:

```text
1 → 2 → 3 → curr
```

and we only need to process the remaining part of the tree.

This allows us to keep moving:

```python
curr = curr.right
```

without needing a separate traversal stack.

---

# 15. Common Mistakes

### Mistake 1: Forgetting to set `curr.left = None`

The final tree must have:

```text
left = None
```

for every node.

So:

```python
curr.left = None
```

is required.

---

### Mistake 2: Losing the original right subtree

If you do:

```python
curr.right = curr.left
```

before connecting the old right subtree, you can lose its reference.

Correct order:

```python
pred.right = curr.right
curr.right = curr.left
curr.left = None
```

---

### Mistake 3: Finding the leftmost node instead of rightmost

We need:

```python
while pred.right:
    pred = pred.right
```

not:

```python
while pred.left:
```

The rightmost node is the last node of the left subtree in preorder.

---

### Mistake 4: Moving `curr` to the wrong pointer

After flattening:

```python
curr = curr.right
```

because the right pointer represents the next node in the flattened list.

---

### Mistake 5: Using extra array unnecessarily

A preorder list approach works, but it uses:

```text
O(n)
```

extra space.

The current approach modifies the tree directly and uses:

```text
O(1)
```

auxiliary space.

---

# 16. Complexity

Let `n` be the number of nodes.

### Time

At first glance, the nested loop:

```python
while pred.right:
```

may look like it makes the solution `O(n²)`.

However, with this pointer-rewiring approach, the predecessor traversal is amortized across the tree structure, giving:

```text
Time → O(n)
```

### Space

We don't use recursion or an explicit stack.

Only a few pointers are used:

```text
curr
pred
```

Therefore:

```text
Space → O(1)
```

Final:

```text
Time  → O(n)
Space → O(1)
```

---

# 17. Pattern Recognition

When you see:

```text
"Flatten binary tree"
"in-place"
"linked list"
"preorder"
"without extra space"
```

Think:

```text
Preorder
   ↓
Current node
   ↓
Left subtree
   ↓
Right subtree
```

If the current node has a left subtree:

```text
Find rightmost node of left subtree
        ↓
Connect it to original right subtree
        ↓
Move left subtree to right
        ↓
Set left = None
```

Then:

```text
Move curr = curr.right
```

---

# 18. Revision Cheat Sheet

```text
Flatten Binary Tree
        ↓
Preorder
        ↓
If curr.left exists
        ↓
Find rightmost node of curr.left
        ↓
pred.right = curr.right
        ↓
curr.right = curr.left
        ↓
curr.left = None
        ↓
curr = curr.right
```

### Core Code

```python
curr = root

while curr:

    if curr.left:

        pred = curr.left

        while pred.right:
            pred = pred.right

        pred.right = curr.right
        curr.right = curr.left
        curr.left = None

    curr = curr.right
```

### Complexity

```text
Time  → O(n)
Space → O(1)
```

---

# 19. Interview Memory Trick

Remember:

> **"Take the left subtree, put it on the right, and attach the old right subtree after the left subtree's rightmost node."**

Or:

```text
LEFT → RIGHT → REMOVE LEFT
```

More precisely:

```text
Find predecessor
      ↓
Connect old right
      ↓
Move left to right
      ↓
Delete left
      ↓
Move forward
```

### One-Line Pattern

> **Flatten = Preorder in-place pointer rewiring using the rightmost node of the left subtree as the predecessor.**