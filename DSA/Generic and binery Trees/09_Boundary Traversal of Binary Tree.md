# Boundary Traversal of Binary Tree

## Problem

Given a binary tree, return its **boundary traversal** in anti-clockwise direction.

Boundary traversal consists of:

```text
1. Root
2. Left Boundary
3. Leaf Nodes
4. Right Boundary in Reverse
```

### Example

```text
          1
        /   \
       2     3
      / \   / \
     4   5 6   7
```

Boundary traversal:

```text
[1, 2, 4, 5, 6, 7, 3]
```

---

# Pattern

```text
Tree Traversal + Recursion
```

---

# Main Idea

We cannot simply use:

```text
Preorder
```

or:

```text
Inorder
```

because boundary traversal has a specific order.

We need to collect:

```text
Root
 ↓
Left Boundary
 ↓
All Leaf Nodes
 ↓
Right Boundary in Reverse
```

---

# Boundary Traversal Order

For the tree:

```text
          1
        /   \
       2     3
      / \   / \
     4   5 6   7
```

Think of walking around the tree anti-clockwise:

```text
        1
       ↙ ↘
      2   3
     ↓     ↓
    4 5   6 7
```

The answer becomes:

```text
1 → 2 → 4 → 5 → 6 → 7 → 3
```

---

# Four Parts

## Part 1: Root

First add the root:

```python
ans.append(root.data)
```

Example:

```text
1
```

---

# Part 2: Left Boundary

The left boundary contains nodes going from:

```text
Root's left
↓
towards the bottom
```

But **leaf nodes are not included** here.

For example:

```text
        1
       /
      2
     /
    4
```

Left boundary should contain:

```text
2
```

not:

```text
2, 4
```

because `4` is a leaf and will be added separately.

---

# How Do We Choose the Left Boundary?

At every node:

```text
If left child exists:
    go left

Else:
    go right
```

Code:

```python
if root.left is not None:
    self.leftBoundry(root.left, ans)
else:
    self.leftBoundry(root.right, ans)
```

This is important because sometimes the left child is missing.

Example:

```text
    1
     \
      2
     /
    3
```

Here, the boundary should continue through:

```text
1 → 2 → 3
```

So if left child doesn't exist, we move to the right child.

---

# Why Don't We Add Leaf Nodes in Left Boundary?

Suppose:

```text
    1
   /
  2
 /
4
```

If we add `4` in left boundary:

```text
1 → 2 → 4
```

then later when collecting leaf nodes, `4` would be added again.

Therefore:

```python
if root.left is None and root.right is None:
    return
```

This prevents duplicate leaf nodes.

---

# Part 3: Leaf Nodes

Now collect **all leaf nodes**.

A leaf node is a node having:

```text
left == None
right == None
```

Code:

```python
if root.left is None and root.right is None:
    ans.append(root.data)
```

Otherwise visit:

```text
left subtree
right subtree
```

Code:

```python
self.leafBoundry(root.left, ans)
self.leafBoundry(root.right, ans)
```

---

# Why Collect Leaves Separately?

Leaves are the bottom boundary of the tree.

They must be collected:

```text
Left → Right
```

Example:

```text
          1
        /   \
       2     3
      / \   / \
     4   5 6   7
```

Leaf nodes:

```text
4, 5, 6, 7
```

So:

```text
Leaf Boundary = [4, 5, 6, 7]
```

---

# Part 4: Right Boundary

The right boundary is collected from:

```text
Bottom → Top
```

because boundary traversal is anti-clockwise.

Suppose:

```text
        1
       / \
      2   3
           \
            7
```

Normal right boundary:

```text
3 → 7
```

But boundary traversal needs:

```text
7 → 3
```

Therefore the right boundary is added in reverse order.

---

# How Do We Reverse the Right Boundary?

Instead of storing it in another array and reversing it, recursion can do the work.

First recursively go down:

```python
if root.right is not None:
    self.rightBoundry(root.right, ans)
else:
    self.rightBoundry(root.left, ans)
```

Then add the node:

```python
ans.append(root.data)
```

So the node is added **while returning from recursion**.

This automatically produces:

```text
Bottom → Top
```

---

# Why Do We Add Right Boundary After Recursion?

This is the key idea.

Suppose:

```text
    1
     \
      2
       \
        3
```

Recursive calls:

```text
rightBoundry(1)
    ↓
rightBoundry(2)
    ↓
rightBoundry(3)
```

At `3`:

```text
3 is leaf
```

so we don't add it to right boundary.

Return to `2`:

```text
add 2
```

Return to `1`:

```text
add 1
```

Therefore the order becomes:

```text
2 → 1
```

which is the required reverse right boundary.

---

# Code

```python
class Solution:

    def leftBoundry(self, root, ans):

        if root is None:
            return

        # Don't add leaf nodes
        if root.left is None and root.right is None:
            return

        ans.append(root.data)

        # Prefer left
        if root.left is not None:
            self.leftBoundry(root.left, ans)
        else:
            self.leftBoundry(root.right, ans)


    def leafBoundry(self, root, ans):

        if root is None:
            return

        # Leaf node
        if root.left is None and root.right is None:
            ans.append(root.data)
        else:
            self.leafBoundry(root.left, ans)
            self.leafBoundry(root.right, ans)


    def rightBoundry(self, root, ans):

        if root is None:
            return

        # Don't add leaf nodes
        if root.right is None and root.left is None:
            return

        # Prefer right
        if root.right is not None:
            self.rightBoundry(root.right, ans)
        else:
            self.rightBoundry(root.left, ans)

        # Add while returning
        ans.append(root.data)


    def boundaryTraversal(self, root):

        ans = []

        if root is None:
            return ans

        # 1. Root
        ans.append(root.data)

        # 2. Left boundary
        self.leftBoundry(root.left, ans)

        # 3. Left subtree leaves
        self.leafBoundry(root.left, ans)

        # 4. Right subtree leaves
        self.leafBoundry(root.right, ans)

        # 5. Reverse right boundary
        self.rightBoundry(root.right, ans)

        return ans
```

---

# Dry Run

Consider:

```text
          1
        /   \
       2     3
      / \   / \
     4   5 6   7
```

## Step 1: Root

```text
ans = [1]
```

---

## Step 2: Left Boundary

Start from:

```text
2
```

Add:

```text
2
```

Then:

```text
2 → 4
```

But `4` is a leaf, so don't add it here.

Now:

```text
ans = [1, 2]
```

---

## Step 3: Leaf Nodes

Traverse the tree from left to right:

```text
4
5
6
7
```

Add them:

```text
ans = [1, 2, 4, 5, 6, 7]
```

---

## Step 4: Right Boundary

Start from:

```text
3
```

Then:

```text
7
```

But `7` is a leaf, so don't add it.

While returning:

```text
add 3
```

Therefore:

```text
ans = [1, 2, 4, 5, 6, 7, 3]
```

Final answer:

```text
[1, 2, 4, 5, 6, 7, 3]
```

---

# Important Edge Case: Single Node

Suppose:

```text
    1
```

We first add:

```text
1
```

Then:

```python
leftBoundry(root.left, ans)
```

does nothing.

Leaf traversal doesn't add root because we call it on:

```text
root.left
root.right
```

Right boundary also does nothing.

Answer:

```text
[1]
```

This is important because otherwise the root could be added multiple times.

---

# Important Edge Case: Skewed Tree

Example:

```text
1
 \
  2
   \
    3
     \
      4
```

Expected boundary:

```text
[1, 2, 3, 4]
```

The code handles this because:

```text
Left boundary
→ uses right child if left doesn't exist

Leaf boundary
→ adds 4

Right boundary
→ excludes leaf nodes
```

---

# Why Do We Call Leaf Traversal Twice?

The code does:

```python
self.leafBoundry(root.left, ans)
self.leafBoundry(root.right, ans)
```

We need leaves from:

```text
both left and right subtrees
```

Together, this gives all leaves from:

```text
Left → Right
```

We don't call:

```python
self.leafBoundry(root, ans)
```

because the root itself could be a leaf in a single-node tree, causing duplication.

---

# Why Are Leaf Nodes Excluded From Both Boundaries?

This is one of the most important points.

We have:

```text
Left Boundary
+
Leaves
+
Right Boundary
```

If leaves were included in boundaries, we could get duplicates.

Example:

```text
        1
       / \
      2   3
     /     \
    4       5
```

If `4` is included in left boundary:

```text
1 → 2 → 4
```

and then leaf traversal adds:

```text
4 → 5
```

we get:

```text
1 → 2 → 4 → 4 → 5 → 3
```

Wrong.

Therefore:

```text
Boundary functions → skip leaves
Leaf function → handles leaves
```

---

# Brute Force / Alternative Approach

A simple alternative is to explicitly store the left and right boundaries in separate arrays.

For example:

```python
class Solution:

    def boundaryTraversal(self, root):

        if root is None:
            return []

        if root.left is None and root.right is None:
            return [root.data]

        ans = [root.data]

        # Left boundary
        curr = root.left

        while curr:
            if curr.left is not None or curr.right is not None:
                ans.append(curr.data)

            if curr.left:
                curr = curr.left
            else:
                curr = curr.right

        # Leaves
        def addLeaves(node):
            if node is None:
                return

            if node.left is None and node.right is None:
                ans.append(node.data)
                return

            addLeaves(node.left)
            addLeaves(node.right)

        addLeaves(root)

        # Right boundary
        right = []
        curr = root.right

        while curr:
            if curr.left is not None or curr.right is not None:
                right.append(curr.data)

            if curr.right:
                curr = curr.right
            else:
                curr = curr.left

        # Reverse right boundary
        ans.extend(right[::-1])

        return ans
```

This approach is also efficient, but it explicitly stores the right boundary before reversing it.

The recursive solution is cleaner because:

```text
Recursion itself performs the reverse order.
```

---

# Complexity

Every node is visited a constant number of times.

Therefore:

```text
Time → O(n)
```

where `n` is the number of nodes.

### Auxiliary Space

Recursive calls can go as deep as the height of the tree:

```text
O(h)
```

where:

```text
h = height of tree
```

The answer array itself requires:

```text
O(n)
```

space.

So:

```text
Time → O(n)
Auxiliary Space → O(h)
Output Space → O(n)
```

---

# Common Mistakes

## 1. Adding Leaf Nodes in Left Boundary

Wrong:

```python
ans.append(root.data)
```

before checking whether the node is a leaf.

Correct:

```python
if root.left is None and root.right is None:
    return
```

---

## 2. Adding Right Boundary Before Recursion

Wrong:

```python
ans.append(root.data)

self.rightBoundry(root.right, ans)
```

This gives:

```text
Top → Bottom
```

Correct:

```python
self.rightBoundry(root.right, ans)
ans.append(root.data)
```

This gives:

```text
Bottom → Top
```

---

## 3. Going Only Left for Left Boundary

Wrong:

```python
root = root.left
```

because a left boundary can continue through a right child when the left child doesn't exist.

Correct:

```text
If left exists → left
Otherwise → right
```

---

## 4. Going Only Right for Right Boundary

Similarly:

```text
If right exists → right
Otherwise → left
```

---

## 5. Adding Root Multiple Times

Don't call the boundary functions on the root itself.

Start with:

```python
ans.append(root.data)
```

and then:

```python
leftBoundry(root.left, ans)
```

and:

```python
rightBoundry(root.right, ans)
```

---

# Revision Cheat Sheet

```text
Boundary Traversal

Order:

1. Root
2. Left Boundary
3. Leaf Nodes
4. Right Boundary in Reverse

--------------------------------------------------

LEFT BOUNDARY

Start:
root.left

Rule:

If left exists:
    go left
else:
    go right

Skip leaf nodes.

--------------------------------------------------

LEAF NODES

Leaf means:

left == None
right == None

Traverse:

Left → Right

Add every leaf.

--------------------------------------------------

RIGHT BOUNDARY

Start:
root.right

Rule:

If right exists:
    go right
else:
    go left

Skip leaf nodes.

IMPORTANT:

Recurse first
Add node after recursion.

Why?

We need:

Bottom → Top

--------------------------------------------------

Why skip leaves?

Leaves are already collected
separately.

Prevents duplicates.

--------------------------------------------------

Why root separately?

Root belongs to the boundary,
but should not be collected again
as a left/right boundary or leaf.

--------------------------------------------------

Complexity:

Time → O(n)

Auxiliary Space → O(h)

Output Space → O(n)

--------------------------------------------------

MEMORY TRICK:

Left Boundary:
Top → Bottom

Leaves:
Left → Right

Right Boundary:
Bottom → Top
```

---

# One-Line Pattern

```text
Boundary Traversal = Root + Left Boundary (skip leaves) + All Leaves + Right Boundary in reverse (skip leaves).
```

# Most Important Interview Point

```text
The right boundary is added after recursion because post-recursion gives Bottom → Top order automatically.
```