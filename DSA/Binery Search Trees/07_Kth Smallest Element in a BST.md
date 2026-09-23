# Kth Smallest Element in a BST

## 1. Problem

Given the root of a **Binary Search Tree (BST)** and an integer `k`, return the **kth smallest value** in the BST.

### Example

```text
        5
       / \
      3   6
     / \
    2   4
   /
  1

Inorder:

1 2 3 4 5 6
```

For:

```text
k = 3
```

The answer is:

```text
3
```

---

# 2. Important BST Property

The most important observation is:

> **Inorder traversal of a BST gives values in sorted order.**

Normal inorder:

```text
Left → Node → Right
```

For the above tree:

```text
1 → 2 → 3 → 4 → 5 → 6
```

Therefore:

```text
1st smallest = 1
2nd smallest = 2
3rd smallest = 3
4th smallest = 4
...
```

So the problem becomes:

> Find the `kth` element during inorder traversal.

---

# 3. Brute Force / Basic Approach

## Idea

Perform the complete inorder traversal and store all values in an array.

Because BST inorder is sorted:

```text
inorder = [1, 2, 3, 4, 5, 6]
```

The kth smallest element is:

```python
inorder[k - 1]
```

Why `k - 1`?

Because Python arrays use **0-based indexing**.

```text
1st smallest → index 0
2nd smallest → index 1
3rd smallest → index 2
```

Therefore:

```text
kth smallest → index k - 1
```

---

# 4. Basic Approach Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def storeInorder(self, root, inorder):
        if root is None:
            return

        # Left
        self.storeInorder(root.left, inorder)

        # Node
        inorder.append(root.val)

        # Right
        self.storeInorder(root.right, inorder)

        return root

    def kthSmallest(self, root: TreeNode | None, k: int) -> int:

        inorder = []

        # Store sorted inorder traversal
        self.storeInorder(root, inorder)

        # kth element in 1-based order
        return inorder[k - 1]
```

---

# 5. Complexity — Basic Approach

We visit every node to create the complete inorder array.

```text
Time:  O(n)
Space: O(n)
```

Why `O(n)` space?

Because we store all `n` node values:

```python
inorder = []
```

There is also recursion stack space:

```text
O(h)
```

So technically:

```text
Space = O(n + h)
```

But since `h <= n`:

```text
Overall = O(n)
```

---

# 6. Optimized Approach

We don't actually need to store the entire inorder traversal.

We only need the **kth** value.

So instead of:

```text
Visit every node
      ↓
Store every value
      ↓
Return kth value
```

we can:

```text
Inorder traversal
      ↓
Count visited nodes
      ↓
When count == k
      ↓
Return current node
```

This avoids the extra inorder array.

---

# 7. Optimized Idea

Suppose:

```text
        5
       / \
      3   6
     / \
    2   4
   /
  1
```

Inorder traversal:

```text
1 → 2 → 3 → 4 → 5 → 6
```

Suppose:

```text
k = 3
```

Track:

```text
k = 3
```

Visit `1`:

```text
k = 2
```

Visit `2`:

```text
k = 1
```

Visit `3`:

```text
k = 0
```

Now:

```text
3 is the answer
```

---

# 8. Optimized Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def kthSmallest(self, root: TreeNode | None, k: int) -> int:

        self.k = k
        self.result = None

        def inorder(root):

            if root is None or self.result is not None:
                return

            # Left
            inorder(root.left)

            # Node
            self.k -= 1

            if self.k == 0:
                self.result = root.val
                return

            # Right
            inorder(root.right)

        inorder(root)

        return self.result
```

---

# 9. Why `self.k -= 1`?

Every time we visit a node during inorder, we have found one more smallest element.

For example:

```text
Inorder:

1 2 3 4 5 6
```

If:

```text
k = 4
```

Then:

```text
Visit 1 → k = 3
Visit 2 → k = 2
Visit 3 → k = 1
Visit 4 → k = 0
```

When:

```python
self.k == 0
```

the current node is the kth smallest.

---

# 10. Why Do We Stop Immediately?

Once we find the kth smallest value:

```python
self.result = root.val
```

we don't need to process the remaining nodes.

That's why this condition is present:

```python
if root is None or self.result is not None:
    return
```

It prevents unnecessary traversal after the answer has been found.

---

# 11. Why Use `self.k` and `self.result`?

The nested `inorder()` function recursively calls itself.

We need the updated `k` value to be shared across all recursive calls.

Using:

```python
self.k
```

allows every recursive call to access the same counter.

Similarly:

```python
self.result
```

stores the answer once it is found.

So:

```text
self.k
   ↓
shared counter

self.result
   ↓
shared answer
```

---

# 12. Dry Run

Consider:

```text
        5
       / \
      3   6
     / \
    2   4
   /
  1
```

Let:

```text
k = 3
```

### Inorder Traversal

```text
1 → 2 → 3 → 4 → 5 → 6
```

### Step-by-step

```text
Initial:
k = 3

Visit 1:
k = 2

Visit 2:
k = 1

Visit 3:
k = 0
result = 3
```

Now:

```text
result = 3
```

The remaining nodes don't need to be processed.

Answer:

```text
3
```

---

# 13. Complexity — Optimized Approach

Each visited node takes constant work.

In the worst case, we may still need to visit all nodes.

Therefore:

```text
Time = O(n)
```

The recursive call stack uses:

```text
O(h)
```

where `h` is the tree height.

Therefore:

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

Most importantly:

```text
No O(n) inorder array
```

is required.

---

# 14. Basic vs Optimized

| Feature | Basic Approach | Optimized Approach |
|---|---|---|
| Traversal | Inorder | Inorder |
| Uses BST property | Yes | Yes |
| Stores all values | Yes | No |
| Finds kth value | `inorder[k-1]` | Counter |
| Time | O(n) | O(n) |
| Extra array | O(n) | O(1) |
| Recursion stack | O(h) | O(h) |
| Overall space | O(n) | O(h) |

The optimized approach is better in space because we don't store the complete inorder traversal.

---

# 15. Common Mistakes

## 1. Using preorder or postorder

For BST:

```text
Inorder = Sorted Order
```

So use:

```text
Left → Node → Right
```

Not:

```text
Root → Left → Right
```

or:

```text
Left → Right → Root
```

---

## 2. Returning `inorder[k]`

`k` is 1-based, but Python indexing is 0-based.

Correct:

```python
inorder[k - 1]
```

---

## 3. Forgetting to decrease `k`

Every visited node represents the next smallest element.

Therefore:

```python
self.k -= 1
```

must happen when the node is visited.

---

## 4. Checking `k == 0` before decrementing

Correct:

```python
self.k -= 1

if self.k == 0:
    self.result = root.val
```

Because the current node itself must count toward `k`.

---

## 5. Continuing after finding the answer

Once:

```python
self.result = root.val
```

is set, further traversal is unnecessary.

Use:

```python
if root is None or self.result is not None:
    return
```

---

# 16. Important Interview Insight

The problem looks like a normal tree traversal problem, but the important observation is the **BST property**.

```text
BST
 ↓
Inorder
 ↓
Sorted values
 ↓
kth element = kth smallest
```

This is the main thing to recognize during an interview.

You don't need to sort the values separately because:

```text
BST inorder is already sorted.
```

---

# 17. Pattern Recognition

When you see:

```text
BST
+
kth smallest
```

Immediately think:

```text
Inorder Traversal
        ↓
Sorted Order
        ↓
Count Nodes
        ↓
When count == k
        ↓
Answer
```

For kth **largest**:

```text
Reverse Inorder

Right → Node → Left
```

For kth **smallest**:

```text
Inorder

Left → Node → Right
```

---

# 18. Revision Cheat Sheet

```text
Kth Smallest in BST

Key Property:
BST Inorder = Sorted Order

Basic:
1. Inorder traversal
2. Store values in array
3. Return inorder[k - 1]

Time  = O(n)
Space = O(n)

Optimized:
1. Perform inorder traversal
2. Decrease k at every visited node
3. When k == 0:
       result = root.val
4. Stop traversal

Time  = O(n)
Space = O(h)

Remember:

kth Smallest → Inorder
kth Largest  → Reverse Inorder
```

> **One-Line Pattern: Kth Smallest in BST = Inorder Traversal + Count Nodes Until `k == 0`.**