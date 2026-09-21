# Delete a Node from a Binary Search Tree

## 1. Problem

Given the root of a **Binary Search Tree (BST)** and a key, delete the node having that key and return the root of the modified BST.

### BST Property

```text
Left subtree  → smaller values
Right subtree → greater values
```

When deleting a node, we must make sure this BST property remains valid.

There are **3 main deletion cases**:

```text
1. Node is a leaf
2. Node has one child
3. Node has two children
```

The two-child case is the most important.

---

# 2. Example

Consider:

```text
        5
       / \
      3   7
     / \ / \
    2  4 6  8
```

Delete:

```text
3
```

Node `3` has two children:

```text
    3
   / \
  2   4
```

We can replace `3` with the **maximum value from its left subtree**.

Maximum of left subtree:

```text
2
```

So:

```text
        5
       / \
      2   7
       \ / \
        4 6 8
```

Then delete the original `2` from the left subtree.

---

# 3. Brute Force

A straightforward approach is:

1. Search the entire tree for the node.
2. Find its parent.
3. Determine the deletion case.
4. Rearrange the tree.

However, because this is a BST, we don't need to search the entire tree.

The BST property tells us exactly where the key can exist:

```text
key < root.val → left
key > root.val → right
```

Therefore, we can perform the deletion while following only one path.

### Complexity

For a BST of height `h`:

```text
Time → O(h)
```

Worst case:

```text
h = n
Time → O(n)
```

The recursive solution uses:

```text
Space → O(h)
```

because of the recursion stack.

---

# 4. Pattern

This is a:

```text
BST
 ↓
Search for key
 ↓
Found node?
 ↓
Handle 3 deletion cases
 ↓
0 children → None
1 child    → return child
2 children → replace with predecessor
```

### One-Line Pattern

> **BST Deletion = Search using BST property, then handle 0, 1, or 2 children; for 2 children, replace with the left subtree's maximum and delete that duplicate node.**

---

# 5. Main Idea

First, search for the node using the BST property.

```python
if key < root.val:
    root.left = self.deleteNode(root.left, key)

if key > root.val:
    root.right = self.deleteNode(root.right, key)
```

When:

```python
root.val == key
```

we have found the node that needs to be deleted.

Now there are three cases.

---

# 6. Case 1 — Leaf Node

A leaf has:

```text
left  = None
right = None
```

Example:

```text
    5
```

If we delete `5`, nothing needs to replace it.

So:

```python
return None
```

### Code

```python
if root.left is None and root.right is None:
    return None
```

---

# 7. Case 2 — Node Has Only Left Child

Example:

```text
      5
     /
    3
```

Delete `5`.

We can directly replace `5` with its left child:

```text
    3
```

So:

```python
return root.left
```

### Code

```python
if root.left is not None and root.right is None:
    return root.left
```

---

# 8. Case 3 — Node Has Only Right Child

Example:

```text
    5
     \
      7
```

Delete `5`.

Replace it with its right child:

```text
    7
```

So:

```python
return root.right
```

### Code

```python
if root.left is None and root.right is not None:
    return root.right
```

---

# 9. Case 4 — Node Has Two Children

This is the most important case.

Consider:

```text
        5
       / \
      3   7
     / \
    2   4
```

Delete:

```text
3
```

We cannot simply remove `3` because both children need to remain connected.

We need a replacement value.

There are two standard choices:

```text
1. Inorder predecessor → maximum value in left subtree
2. Inorder successor   → minimum value in right subtree
```

This code uses the **inorder predecessor**.

---

# 10. Why Maximum from Left Subtree?

For:

```text
        3
       / \
      2   4
```

The maximum value in the left subtree is:

```text
2
```

Replacing `3` with `2` maintains the BST property:

```text
left values < 2
right values > 2
```

The predecessor is the value immediately before the node in inorder traversal.

### Inorder

For:

```text
        5
       / \
      3   7
     / \
    2   4
```

Inorder is:

```text
2 → 3 → 4 → 5 → 7
```

The predecessor of `3` is:

```text
2
```

So `2` can replace `3`.

---

# 11. Finding the Maximum of the Left Subtree

The helper function:

```python
def getMax(self, root):
    if root is None:
        return -1

    while root.right:
        root = root.right

    return root.val
```

Why do we move right?

Because in a BST:

```text
Right subtree → greater values
```

Therefore:

```text
Maximum = rightmost node
```

For:

```text
      3
     /
    2
     \
      2.5
```

the maximum of the left subtree is the rightmost node.

So:

```python
while root.right:
    root = root.right
```

finds the predecessor.

---

# 12. Two-Child Deletion Steps

Suppose:

```text
        5
       / \
      3   7
     / \
    2   4
```

Delete `3`.

### Step 1: Find maximum of left subtree

```python
maxVal = self.getMax(root.left)
```

So:

```text
maxVal = 2
```

---

### Step 2: Replace current value

```python
root.val = maxVal
```

Tree temporarily becomes:

```text
        5
       / \
      2   7
     / \
    2   4
```

Now there are two `2`s.

---

### Step 3: Delete the duplicate

The original `2` is still inside the left subtree.

So:

```python
root.left = self.deleteNode(root.left, maxVal)
```

This removes the original `2`.

Final:

```text
        5
       / \
      2   7
       \
        4
```

BST property is preserved.

---

# 13. Complete Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def getMax(self, root):
        if root is None:
            return -1

        # Maximum in a BST is the rightmost node
        while root.right:
            root = root.right

        return root.val

    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:

        # Key not found / empty subtree
        if root is None:
            return None

        # Found the node
        if root.val == key:

            # Case 1: No children
            if root.left is None and root.right is None:
                return None

            # Case 2: Only left child
            if root.left is not None and root.right is None:
                return root.left

            # Case 3: Only right child
            if root.left is None and root.right is not None:
                return root.right

            # Case 4: Two children
            maxVal = self.getMax(root.left)

            # Replace current node with predecessor
            root.val = maxVal

            # Delete the duplicate predecessor
            root.left = self.deleteNode(root.left, maxVal)

            return root

        # Search in left subtree
        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        # Search in right subtree
        if key > root.val:
            root.right = self.deleteNode(root.right, key)

        return root
```

---

# 14. Dry Run — Leaf Node

Consider:

```text
        5
       / \
      3   7
```

Delete:

```text
7
```

Start:

```text
root = 5
key = 7
```

Since:

```text
7 > 5
```

go right:

```text
root = 7
```

Now:

```text
root.val == key
```

and:

```text
root.left = None
root.right = None
```

So:

```python
return None
```

Parent updates:

```python
root.right = None
```

Result:

```text
    5
   /
  3
```

---

# 15. Dry Run — One Child

Consider:

```text
        5
       /
      3
     /
    2
```

Delete:

```text
3
```

At node `3`:

```text
left  = 2
right = None
```

So:

```python
return root.left
```

which returns:

```text
2
```

Parent updates:

```python
5.left = 2
```

Result:

```text
    5
   /
  2
```

---

# 16. Dry Run — Two Children

Consider:

```text
        5
       / \
      3   7
     / \
    2   4
```

Delete:

```text
3
```

At node `3`:

```text
left  = 2
right = 4
```

Two children.

Find predecessor:

```text
max(left subtree) = 2
```

Replace:

```text
3 → 2
```

Temporarily:

```text
        5
       / \
      2   7
     / \
    2   4
```

Delete the old `2`:

```python
root.left = self.deleteNode(root.left, 2)
```

Result:

```text
        5
       / \
      2   7
       \
        4
```

---

# 17. Why Do We Recursively Delete `maxVal`?

After:

```python
root.val = maxVal
```

the original predecessor node still exists in the left subtree.

Example:

```text
Before:

      3
     / \
    2   4
```

After copying:

```text
      2
     / \
    2   4
```

There are now two `2`s.

We need to remove the original one:

```python
root.left = self.deleteNode(root.left, maxVal)
```

This is why the second recursive deletion is required.

---

# 18. Why Does the Recursive Result Need to Be Assigned?

This is important:

```python
root.left = self.deleteNode(root.left, maxVal)
```

and:

```python
root.right = self.deleteNode(root.right, key)
```

The recursive call can change the root of the subtree.

For example, deleting a node with one child:

```text
      5
     /
    3
   /
  2
```

Deleting `3` returns:

```text
2
```

Therefore the parent must update:

```python
5.left = 2
```

That's why we assign the recursive result.

---

# 19. Why Return `root`?

At the end:

```python
return root
```

returns the root of the current subtree to its parent.

This allows the parent to reconnect the modified subtree correctly.

Think:

```text
deleteNode(subtree)
        ↓
returns new root of subtree
        ↓
parent reconnects it
```

This is a very common recursive BST pattern.

---

# 20. Important Recursion Flow

For deleting `3`:

```text
delete(5, 3)
      |
      | 3 < 5
      ↓
delete(3, 3)
      |
      | Found
      ↓
Find predecessor = 2
      |
      ↓
root.val = 2
      |
      ↓
delete(2, 2)
      |
      ↓
return None
      |
      ↓
3's left becomes None
      |
      ↓
return modified subtree
      |
      ↓
5.left = modified subtree
```

The important idea is:

```text
Recursive call
      ↓
Modify subtree
      ↓
Return new subtree root
      ↓
Parent reconnects subtree
```

---

# 21. Common Mistakes

### Mistake 1: Deleting a two-child node directly

You cannot simply:

```python
return root.left
```

or:

```python
return root.right
```

when both children exist.

You need a replacement node/value.

---

### Mistake 2: Forgetting to delete the predecessor

After:

```python
root.val = maxVal
```

the predecessor still exists.

You must remove it:

```python
root.left = self.deleteNode(root.left, maxVal)
```

---

### Mistake 3: Finding the wrong predecessor

For predecessor:

```text
Maximum of left subtree
```

So:

```python
getMax(root.left)
```

and move:

```text
RIGHT
```

until there is no right child.

---

### Mistake 4: Using minimum of the left subtree

That is not the standard predecessor.

Remember:

```text
Predecessor → maximum of left subtree
Successor   → minimum of right subtree
```

---

### Mistake 5: Not assigning recursive results

Wrong:

```python
self.deleteNode(root.left, key)
```

Correct:

```python
root.left = self.deleteNode(root.left, key)
```

Same for the right subtree.

---

### Mistake 6: Forgetting the three basic cases

When the node is found:

```text
0 children → None
1 child    → return child
2 children → predecessor/successor
```

---

# 22. Predecessor vs Successor

For a node with two children, we can use either:

### Inorder Predecessor

```text
Maximum of left subtree
```

```text
        5
       /
      3
     / \
    2   4

predecessor = 4
```

### Inorder Successor

```text
Minimum of right subtree
```

```text
        5
          \
           7
          / \
         6   8

successor = 6
```

Your code uses:

```text
Predecessor
=
Maximum of left subtree
```

---

# 23. Complexity

Let:

```text
h = height of BST
```

Searching for the node takes:

```text
O(h)
```

Finding the maximum in the left subtree takes:

```text
O(h)
```

Deleting the predecessor also takes:

```text
O(h)
```

These operations happen along BST paths, so the overall complexity is:

```text
Time → O(h)
```

For a balanced BST:

```text
h = O(log n)

Time → O(log n)
```

For a skewed BST:

```text
h = O(n)

Time → O(n)
```

Because the solution is recursive:

```text
Space → O(h)
```

### Final Complexity

```text
Time  → O(h)
Space → O(h)
```

---

# 24. Pattern Recognition

When you see:

```text
"Delete node from BST"
```

immediately think:

```text
1. Search using BST property
          ↓
2. Found node?
          ↓
3. Count children
          ↓
   ┌──────┼──────┐
   ↓      ↓      ↓
   0      1      2
   ↓      ↓      ↓
 None   Child  Predecessor/
                Successor
```

For two children:

```text
Predecessor
    ↓
Maximum of left subtree
```

or:

```text
Successor
    ↓
Minimum of right subtree
```

---

# 25. Revision Cheat Sheet

```text
BST Delete
     ↓
Search key
     ↓
key < root → left
key > root → right
     ↓
Found
     ↓
0 children → return None
     ↓
1 child → return that child
     ↓
2 children
     ↓
Find max(left subtree)
     ↓
Copy value to root
     ↓
Delete duplicate from left subtree
     ↓
Return root
```

### Core Two-Child Code

```python
maxVal = self.getMax(root.left)

root.val = maxVal

root.left = self.deleteNode(root.left, maxVal)

return root
```

### Core Helper

```python
def getMax(self, root):
    while root.right:
        root = root.right

    return root.val
```

### Complexity

```text
Time  → O(h)
Space → O(h)
```

---

# 26. Interview Memory Trick

Remember:

> **"Delete = Search + 0/1/2 children. For two children, replace with predecessor and delete the duplicate."**

### One-Line Pattern

> **BST Delete = Search → Handle 0/1 child directly → For 2 children, replace with maximum of left subtree and recursively delete that predecessor.**