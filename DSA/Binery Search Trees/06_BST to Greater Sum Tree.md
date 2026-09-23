# BST to Greater Sum Tree

## 1. Problem

Convert a **Binary Search Tree (BST)** into a **Greater Sum Tree (GST)**.

For every node:

> Replace its value with the sum of all values that are **greater than or equal to** that node's value.

### Example

```text
BST:

        4
       / \
      2   6
     / \   \
    1   3   7

Inorder:
1 2 3 4 6 7
```

After conversion:

```text
        17
       /  \
     22    13
    /  \     \
   23  20     7
```

Because:

```text
1 → 1 + 2 + 3 + 4 + 6 + 7 = 23
2 →     2 + 3 + 4 + 6 + 7 = 22
3 →         3 + 4 + 6 + 7 = 20
4 →             4 + 6 + 7 = 17
6 →                 6 + 7 = 13
7 →                       7 = 7
```

---

# 2. Brute Force

## Idea

For every node:

1. Traverse the complete tree.
2. Find all nodes having value greater than or equal to the current node.
3. Calculate their sum.
4. Update the current node.

This repeats a tree traversal for every node.

### Complexity

```text
Time:  O(n²)
Space: O(h)
```

where `h` is the height of the tree.

### Why slow?

The same nodes are repeatedly visited for every node.

We can use the **BST property** to solve this in `O(n)` time.

---

# 3. Important BST Property

Inorder traversal of a BST gives values in sorted order:

```text
Left → Root → Right
```

Example:

```text
        4
       / \
      2   6
     / \   \
    1   3   7

Inorder:

1 2 3 4 6 7
```

For a node:

```text
Greater values
      ↓
Right side of sorted order
```

Therefore, instead of repeatedly searching for greater values, we can process the BST from:

```text
Largest → Smallest
```

There are two useful ways to do this.

---

# 4. Approach 1 — Inorder Array + Suffix Sum

## Idea

This approach has 3 steps.

```text
BST
 ↓
Inorder traversal
 ↓
Sorted array
 ↓
Suffix sums
 ↓
Update tree using inorder
```

---

## Step 1: Store Inorder

```text
BST:

        4
       / \
      2   6
     / \   \
    1   3   7

Inorder:

[1, 2, 3, 4, 6, 7]
```

---

## Step 2: Calculate Suffix Sum

Process from right to left.

```text
[1, 2, 3, 4, 6, 7]
```

becomes:

```text
[23, 22, 20, 17, 13, 7]
```

For example:

```text
7 → 7

6 → 6 + 7 = 13

4 → 4 + 6 + 7 = 17

3 → 3 + 4 + 6 + 7 = 20
```

Code:

```python
for i in range(n - 2, -1, -1):
    inorder[i] += inorder[i + 1]
```

---

## Step 3: Update the Tree

Perform inorder traversal again.

Because the tree is visited in sorted order:

```text
1 → 2 → 3 → 4 → 6 → 7
```

we can assign:

```text
23 → 22 → 20 → 17 → 13 → 7
```

to those nodes.

---

## Complete Code — Approach 1

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def inOrder(self, root, inorder):
        if root is None:
            return

        self.inOrder(root.left, inorder)

        inorder.append(root.val)

        self.inOrder(root.right, inorder)

        return root

    def updateNodes(self, root, inorder, index):
        if root is None:
            return index

        index = self.updateNodes(root.left, inorder, index)

        root.val = inorder[index]
        index += 1

        index = self.updateNodes(root.right, inorder, index)

        return index

    def bstToGst(self, root: TreeNode | None) -> TreeNode | None:

        if root is None:
            return None

        # Step 1:
        # Store BST values in sorted order
        inorder = []
        self.inOrder(root, inorder)

        # Step 2:
        # Create suffix sums from right to left
        n = len(inorder)

        for i in range(n - 2, -1, -1):
            inorder[i] += inorder[i + 1]

        # Step 3:
        # Update tree values using inorder
        self.updateNodes(root, inorder, 0)

        return root
```

---

# 5. Approach 2 — Reverse Inorder / RNL

This is the **more direct approach**.

Instead of:

```text
Inorder → Array → Suffix Sum → Update Tree
```

we can directly traverse the BST in:

```text
Right → Node → Left
```

This is called **Reverse Inorder** or **RNL**.

Why?

Normal inorder:

```text
Left → Node → Right
```

gives:

```text
Small → Large
```

Reverse inorder:

```text
Right → Node → Left
```

gives:

```text
Large → Small
```

That is exactly the order we need.

---

# 6. How Reverse Inorder Works

Consider:

```text
        4
       / \
      2   6
     / \   \
    1   3   7
```

Reverse inorder:

```text
7 → 6 → 4 → 3 → 2 → 1
```

Maintain a running sum:

```text
Sum = 0
```

### Visit 7

```text
Sum = 0 + 7
Sum = 7

7 → 7
```

### Visit 6

```text
Sum = 7 + 6
Sum = 13

6 → 13
```

### Visit 4

```text
Sum = 13 + 4
Sum = 17

4 → 17
```

### Visit 3

```text
Sum = 17 + 3
Sum = 20

3 → 20
```

Continue:

```text
2 → 22
1 → 23
```

Final values:

```text
        17
       /  \
     22    13
    /  \     \
   23  20     7
```

---

# 7. Complete Code — Approach 2

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def bstToGst(self, root: TreeNode | None) -> TreeNode | None:

        self.Sum = 0

        # Reverse Inorder = Right → Node → Left
        def reverse_order(root):

            if root is None:
                return

            # R - Right
            reverse_order(root.right)

            # N - Node
            self.Sum += root.val
            root.val = self.Sum

            # L - Left
            reverse_order(root.left)

        reverse_order(root)

        return root
```

---

# 8. Why Does Reverse Inorder Work?

The key idea is:

```text
BST
```

has:

```text
Left subtree < Root < Right subtree
```

So when we traverse:

```text
Right → Root → Left
```

we visit values from:

```text
Largest → Smallest
```

At any node, all greater values have already been visited.

Therefore:

```python
self.Sum += root.val
```

automatically gives:

```text
current value + all greater values
```

Then:

```python
root.val = self.Sum
```

updates the node.

---

# 9. Approach Comparison

| Approach | Main Idea | Time | Extra Space |
|---|---|---:|---:|
| Brute Force | Search all greater values for every node | O(n²) | O(h) |
| Inorder + Suffix Sum | Sorted array + suffix sums + update | O(n) | O(n + h) |
| Reverse Inorder | Directly process largest → smallest | O(n) | O(h) |

### Important

Both optimized approaches have:

```text
Time = O(n)
```

But Reverse Inorder does not need an extra `inorder` array.

It directly updates the tree while traversing.

---

# 10. Why `self.Sum` Is Needed

The running sum has to be shared between recursive calls.

Example:

```text
Visit 7
Sum = 7

Visit 6
Sum = 13

Visit 4
Sum = 17
```

Each node needs the sum calculated by the previous nodes.

Therefore:

```python
self.Sum
```

is used so that all recursive calls access the same variable.

---

# 11. Why Update the Node After Adding Its Value?

The order is:

```python
self.Sum += root.val
root.val = self.Sum
```

First:

```text
Sum = previous greater values
```

Then:

```text
Sum += current value
```

Now `Sum` represents:

```text
current value + all greater values
```

Then we store it:

```text
root.val = Sum
```

So the node gets the correct Greater Sum value.

---

# 12. Dry Run — Reverse Inorder

Tree:

```text
        4
       / \
      2   6
     / \   \
    1   3   7
```

Reverse inorder:

```text
7 → 6 → 4 → 3 → 2 → 1
```

| Node | Previous Sum | New Sum | New Value |
|---:|---:|---:|---:|
| 7 | 0 | 7 | 7 |
| 6 | 7 | 13 | 13 |
| 4 | 13 | 17 | 17 |
| 3 | 17 | 20 | 20 |
| 2 | 20 | 22 | 22 |
| 1 | 22 | 23 | 23 |

Final tree:

```text
        17
       /  \
     22    13
    /  \     \
   23  20     7
```

---

# 13. Common Mistakes

## 1. Using normal inorder

Normal inorder:

```text
Left → Node → Right
```

processes:

```text
Small → Large
```

That is not convenient for maintaining the greater-value sum.

Use:

```text
Right → Node → Left
```

---

## 2. Using the wrong traversal order

Remember:

```text
RNL = Reverse Inorder

R → N → L
```

---

## 3. Updating before adding to Sum

Wrong:

```python
root.val = self.Sum
self.Sum += root.val
```

Correct:

```python
self.Sum += root.val
root.val = self.Sum
```

The original node value must be added first.

---

## 4. Using a local Sum without sharing it

If every recursive call creates its own independent sum, the running total will not be preserved.

Use:

```python
self.Sum
```

or another shared/nonlocal variable.

---

## 5. Forgetting that the node's original value is needed

The current node's original value must be added before replacing it:

```python
self.Sum += root.val
root.val = self.Sum
```

---

# 14. Complexity of Reverse Inorder

Every node is visited exactly once.

Therefore:

```text
Time = O(n)
```

The recursive call stack can contain up to the height of the tree:

```text
Space = O(h)
```

For a balanced BST:

```text
O(h) = O(log n)
```

For a skewed BST:

```text
O(h) = O(n)
```

No extra array is required.

---

# 15. Pattern Recognition

When you see:

```text
BST
+
Greater values
+
Update every node
```

Think:

```text
BST
 ↓
Need largest → smallest
 ↓
Reverse Inorder
 ↓
Right → Node → Left
 ↓
Maintain running Sum
 ↓
Update current node
```

### The core pattern

```text
Greater Sum Tree
=
Reverse Inorder + Running Sum
```

---

# 16. Revision Cheat Sheet

```text
BST to Greater Sum Tree

Why Reverse Inorder?

BST:
Left < Root < Right

Normal Inorder:
Left → Root → Right
Small → Large

Reverse Inorder:
Right → Root → Left
Large → Small

Therefore:

reverse_order(root.right)

self.Sum += root.val
root.val = self.Sum

reverse_order(root.left)

Time:
O(n)

Space:
O(h)
```

### Two Optimized Approaches

```text
Approach 1:
Inorder
→ Sorted Array
→ Suffix Sum
→ Update Tree

Time: O(n)
Space: O(n)

Approach 2:
Reverse Inorder
→ Running Sum
→ Update Directly

Time: O(n)
Space: O(h)
```

> **One-Line Pattern: BST to GST = Reverse Inorder (RNL) + Running Sum, because Reverse Inorder visits nodes from largest to smallest.**