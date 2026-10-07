# Balance a Binary Search Tree

## 1. Problem

Given a **Binary Search Tree (BST)** that may be unbalanced, convert it into a **balanced BST** containing the same values.

A BST is balanced when the height difference between the left and right subtrees is kept small.

### Example

Unbalanced BST:

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
```

Inorder:

```text
[1, 2, 3, 4, 5]
```

Balanced BST:

```text
        3
       / \
      2   4
     /     \
    1       5
```

The important observation is:

> **Inorder traversal of a BST gives values in sorted order.**

So we can:

```text
BST
 ↓
Inorder Traversal
 ↓
Sorted Array
 ↓
Choose Middle Element as Root
 ↓
Recursively Build Left + Right
 ↓
Balanced BST
```

---

# 2. Brute Force Approach

A simple way is to:

1. Store all BST values using inorder traversal.
2. Build a new BST by repeatedly choosing a suitable element.
3. Insert elements into the new BST.

For example:

```text
inorder = [1, 2, 3, 4, 5]
```

If we insert them in sorted order:

```text
1 → 2 → 3 → 4 → 5
```

we again get a skewed tree.

So insertion order would need to be carefully chosen, for example:

```text
3, 2, 1, 4, 5
```

This can produce a balanced tree, but repeatedly inserting elements is unnecessary work.

### Complexity

If we insert `n` elements one by one:

```text
Average: O(n log n)
Worst:   O(n²)
```

depending on the tree structure and insertion order.

### Why not use it?

We already have the sorted inorder array.

There is a much simpler way:

> Pick the middle element directly as the root.

---

# 3. Optimized Approach

The solution has two main steps.

### Step 1: Get sorted values

Perform inorder traversal:

```text
Left → Root → Right
```

Because the input is a BST, this produces sorted values.

```text
        4
       / \
      2   5
     / \
    1   3

Inorder:
[1, 2, 3, 4, 5]
```

---

### Step 2: Build a balanced BST

For a sorted array:

```text
[1, 2, 3, 4, 5]
```

choose the middle element:

```text
        3
       / \
[1,2]   [4,5]
```

Then recursively do the same thing:

```text
        3
       / \
      2   4
     /     \
    1       5
```

This keeps the left and right sides approximately equal.

---

# 4. Why Choose the Middle?

Suppose we have:

```text
[1, 2, 3, 4, 5, 6, 7]
```

If we choose `4`:

```text
            4
          /   \
     [1,2,3] [5,6,7]
```

Both sides contain the same number of elements.

Then:

```text
[1,2,3] → choose 2
[5,6,7] → choose 6
```

Result:

```text
            4
          /   \
         2     6
        / \   / \
       1   3 5   7
```

This gives a balanced BST.

---

# 5. Code

```python
class Solution:
    def solve(self, root, inorder):
        if root is None:
            return

        # Visit left subtree
        self.solve(root.left, inorder)

        # Store current node
        inorder.append(root.val)

        # Visit right subtree
        self.solve(root.right, inorder)

    def buildTree(self, inorder, start, end):
        # No elements in this range
        if start > end:
            return None

        # Choose middle element as root
        mid = (start + end) // 2

        root = TreeNode(inorder[mid])

        # Build left subtree
        root.left = self.buildTree(
            inorder,
            start,
            mid - 1
        )

        # Build right subtree
        root.right = self.buildTree(
            inorder,
            mid + 1,
            end
        )

        return root

    def balanceBST(self, root: TreeNode | None) -> TreeNode | None:
        inorder = []

        # Step 1: Get sorted values
        self.solve(root, inorder)

        # Step 2: Build balanced BST
        return self.buildTree(
            inorder,
            0,
            len(inorder) - 1
        )
```

---

# 6. Understanding `solve()`

```python
def solve(self, root, inorder):
    if root is None:
        return

    self.solve(root.left, inorder)
    inorder.append(root.val)
    self.solve(root.right, inorder)
```

This is simply inorder traversal:

```text
Left
 ↓
Root
 ↓
Right
```

For:

```text
        4
       / \
      2   5
     / \
    1   3
```

the recursive traversal produces:

```text
1 → 2 → 3 → 4 → 5
```

Therefore:

```python
inorder = [1, 2, 3, 4, 5]
```

Since the input is a BST, this array is sorted.

---

# 7. Understanding `buildTree()`

The function receives:

```python
start
end
```

which represent the portion of the sorted array currently being processed.

For:

```text
[1, 2, 3, 4, 5]
```

initially:

```text
start = 0
end = 4
```

So:

```python
mid = (0 + 4) // 2
    = 2
```

Therefore:

```text
inorder[2] = 3
```

becomes the root.

```text
        3
       / \
```

Now recursively build:

```text
Left:
start = 0
end = 1

Right:
start = 3
end = 4
```

---

# 8. Recursive Structure

For:

```text
[1, 2, 3, 4, 5]
```

the calls conceptually look like:

```text
buildTree(0, 4)
       |
       3
      / \
     /   \
build(0,1)  build(3,4)
    |           |
    1?          4?
```

More accurately:

```text
             3
           /   \
          1     4
           \     \
            2     5
```

The exact shape depends on how the midpoint splits the ranges.

The important rule is:

```text
middle element → root
left portion   → left subtree
right portion  → right subtree
```

---

# 9. Why Does This Remain a BST?

The inorder array is sorted:

```text
[1, 2, 3, 4, 5]
```

When we choose:

```text
3
```

as root:

```text
[1, 2] < 3
[4, 5] > 3
```

So:

```text
        3
       / \
 [1,2]   [4,5]
```

The same property holds recursively.

Therefore the resulting tree is still a valid BST.

---

# 10. Why Is It Balanced?

At every recursive step, we choose the middle element.

For example:

```text
[1, 2, 3, 4, 5, 6, 7]

             4
           /   \
        [1,2,3] [5,6,7]
```

Both subarrays are approximately equal in size.

This continues recursively:

```text
             4
           /   \
          2     6
         / \   / \
        1   3 5   7
```

Therefore the height becomes approximately:

```text
O(log n)
```

instead of:

```text
O(n)
```

for a completely skewed BST.

---

# 11. Dry Run

Consider:

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
```

### Step 1: Inorder

```text
[1, 2, 3, 4, 5]
```

### Step 2: Choose middle

```text
mid = 2

root = 3
```

Remaining:

```text
Left  = [1, 2]
Right = [4, 5]
```

### Step 3: Build left

```text
[1, 2]

mid = 0

root = 1
right = [2]
```

### Step 4: Build right

```text
[4, 5]

mid = 3

root = 4
right = [5]
```

Final tree:

```text
        3
       / \
      1   4
       \   \
        2   5
```

This is much more balanced than the original skewed tree.

---

# 12. Recursion Space

There are two recursive functions.

### Inorder traversal

```python
self.solve(root.left, inorder)
...
self.solve(root.right, inorder)
```

The recursion depth is:

```text
O(h)
```

where `h` is the height of the original BST.

Worst case:

```text
O(n)
```

if the tree is completely skewed.

---

### Building the balanced tree

```python
self.buildTree(...)
```

Since the new tree is balanced, its recursion depth is:

```text
O(log n)
```

But the overall auxiliary recursion space is dominated by the original traversal in the worst case:

```text
O(n)
```

---

# 13. Complexity

Let `n` be the number of nodes.

### Inorder traversal

```text
Time:  O(n)
Space: O(n)
```

The `O(n)` space is mainly for the `inorder` array.

### Building the tree

Every value is used once:

```text
Time:  O(n)
```

The recursion depth of the balanced tree is:

```text
O(log n)
```

### Overall

```text
Time:  O(n)
Space: O(n)
```

The `O(n)` space is required for storing the inorder values.

---

# 14. Complexity Comparison

| Approach | Time | Extra Space | Idea |
|---|---:|---:|---|
| Insert elements into new BST | O(n log n) average / O(n²) worst | O(n) | Repeated insertion |
| Inorder + middle element | O(n) | O(n) | Sorted array + midpoint |

The inorder + midpoint approach is the clean and optimal approach for this problem.

---

# 15. Important Insight

This problem combines two important BST properties:

### Property 1

```text
BST → Inorder → Sorted Array
```

### Property 2

```text
Sorted Array + Middle Element
              ↓
        Balanced BST
```

Therefore:

```text
BST
 ↓
Inorder
 ↓
Sorted Array
 ↓
Middle as Root
 ↓
Balanced BST
```

---

# 16. Common Mistakes

### Mistake 1: Choosing the first element as root

```text
[1, 2, 3, 4, 5]

root = 1
```

This produces a skewed tree.

Use the middle element.

---

### Mistake 2: Forgetting BST inorder is sorted

The entire approach depends on:

```text
BST → inorder → sorted
```

If the input were a general binary tree, inorder would not necessarily be sorted.

---

### Mistake 3: Wrong boundaries

After choosing:

```python
mid
```

the left subtree must use:

```python
start, mid - 1
```

and the right subtree:

```python
mid + 1, end
```

Do not include `mid` again.

---

### Mistake 4: Wrong base condition

```python
if start > end:
    return None
```

This means there are no elements left to build.

---

### Mistake 5: Forgetting to return the root

The recursive function must return:

```python
return root
```

so the parent can attach it:

```python
root.left = self.buildTree(...)
root.right = self.buildTree(...)
```

---

# 17. Pattern Recognition

When you see:

```text
BST
+
Balance the tree
+
Same values
```

think:

```text
Inorder → Sorted Array → Middle Element → Recursively Build
```

This is a very common **BST transformation pattern**.

---

# 18. Revision Cheat Sheet

```text
Balance BST
    ↓
Inorder Traversal
    ↓
Sorted Array
    ↓
Choose Middle
    ↓
Middle = Root
    ↓
Left Half = Left Subtree
    ↓
Right Half = Right Subtree
    ↓
Repeat Recursively
```

### Key formulas

```python
mid = (start + end) // 2
```

Left subtree:

```python
start → mid - 1
```

Right subtree:

```python
mid + 1 → end
```

### Complexity

```text
Time  = O(n)
Space = O(n)
```

### Core idea

> **Use inorder traversal to convert the BST into a sorted array, then recursively choose the middle element as the root to build a balanced BST.**

---

# One-Line Pattern

> **Balance BST = Inorder Traversal → Sorted Array → Middle Element as Root → Recursively Build Left and Right.**