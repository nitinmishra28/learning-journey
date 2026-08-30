# Construct Binary Tree from Preorder and Inorder Traversal

## Problem

Given two arrays:

```text
preorder
inorder
```

construct the original binary tree.

### Preorder Traversal

Preorder follows:

```text
Root → Left → Right
```

### Inorder Traversal

Inorder follows:

```text
Left → Root → Right
```

---

# Pattern

```text
Binary Tree + Recursion + Divide and Conquer
```

---

# Main Idea

The most important observation is:

```text
Preorder tells us the ROOT.
Inorder tells us where to split LEFT and RIGHT subtrees.
```

For every subtree:

```text
1. First element of preorder = root
2. Find root in inorder
3. Elements left of root in inorder = left subtree
4. Elements right of root in inorder = right subtree
5. Recursively build both subtrees
```

---

# Example

Consider:

```text
preorder = [3, 9, 20, 15, 7]

inorder  = [9, 3, 15, 20, 7]
```

The tree is:

```text
        3
       / \
      9   20
         /  \
        15   7
```

---

# Step 1: Find the Root

Preorder is:

```text
[3, 9, 20, 15, 7]
```

The first element is:

```text
3
```

Therefore:

```python
root = TreeNode(preorder[0])
```

So:

```text
root = 3
```

---

# Step 2: Find Root in Inorder

Inorder:

```text
[9, 3, 15, 20, 7]
```

Find:

```text
3
```

Its index is:

```text
1
```

So:

```text
        3
       / \
      9   15 20 7
```

More precisely:

```text
Left subtree:

[9]

Right subtree:

[15, 20, 7]
```

Because everything before `3` belongs to the left subtree and everything after `3` belongs to the right subtree.

---

# The Most Important Part

Suppose:

```text
preorder = [3, 9, 20, 15, 7]
inorder  = [9, 3, 15, 20, 7]
```

Root:

```text
3
```

Index of `3` in inorder:

```text
index = 1
```

Therefore:

```text
Left subtree has 1 node.
Right subtree has 3 nodes.
```

Now we need to take exactly the same number of nodes from preorder.

---

# Why `preorder[1:index+1]`?

This is one of the most important things to understand.

We already used:

```text
preorder[0]
```

as the root.

So the left subtree starts from:

```text
preorder[1]
```

The left subtree has:

```text
index
```

number of nodes.

Therefore we need:

```python
preorder[1:index+1]
```

Remember Python slicing excludes the ending index.

For:

```text
index = 1
```

we get:

```python
preorder[1:2]
```

which gives:

```text
[9]
```

---

# Why `index + 1`?

Because Python slicing is:

```text
[start : end]
```

where `end` is excluded.

If:

```text
index = 3
```

and we need the first `3` elements after the root:

```text
preorder[1:4]
```

gives:

```text
index 1
index 2
index 3
```

So:

```python
preorder[1:index+1]
```

contains exactly `index` elements.

---

# Why `inorder[:index]`?

The root is at:

```text
index
```

in inorder.

Everything before it belongs to the left subtree.

Therefore:

```python
inorder[:index]
```

Example:

```text
inorder = [9, 3, 15, 20, 7]
             ↑
           index 1
```

Then:

```python
inorder[:1]
```

gives:

```text
[9]
```

---

# Left Subtree

Therefore:

```python
root.left = self.buildTree(
    preorder[1:index+1],
    inorder[:index]
)
```

For our example:

```text
preorder[1:2]
= [9]

inorder[:1]
= [9]
```

So we recursively build:

```text
    9
```

---

# Right Subtree

Everything after the root in inorder belongs to the right subtree:

```python
inorder[index+1:]
```

For:

```text
inorder = [9, 3, 15, 20, 7]
             ↑
           index 1
```

we get:

```text
[15, 20, 7]
```

The right subtree has `3` nodes.

We already used:

```text
preorder[0]
```

for the root.

The next `index` elements belong to the left subtree.

Therefore the right subtree starts from:

```text
index + 1
```

So:

```python
preorder[index+1:]
```

gives:

```text
[20, 15, 7]
```

Thus:

```python
root.right = self.buildTree(
    preorder[index+1:],
    inorder[index+1:]
)
```

---

# Why `preorder[index+1:]`?

This is another important point.

Suppose:

```text
index = 1
```

Then:

```python
preorder[index+1:]
```

becomes:

```python
preorder[2:]
```

giving:

```text
[20, 15, 7]
```

Why start at `2`?

Because:

```text
preorder[0] → root
preorder[1] → left subtree
```

Therefore:

```text
preorder[2:] → right subtree
```

---

# Complete Partition

For:

```text
preorder = [3, 9, 20, 15, 7]
inorder  = [9, 3, 15, 20, 7]
```

Root:

```text
3
```

Index:

```text
1
```

Partition:

```text
                3
              /   \
             /     \
        Left         Right

Preorder:
[9]            [20,15,7]

Inorder:
[9]            [15,20,7]
```

Notice:

```text
Number of nodes in left preorder
=
Number of nodes in left inorder
=
1
```

and:

```text
Number of nodes in right preorder
=
Number of nodes in right inorder
=
3
```

This matching size is the key.

---

# Recursive Tree Construction

Now build the left subtree:

```text
preorder = [9]
inorder  = [9]
```

Root:

```text
9
```

No elements remain.

So:

```text
left = None
right = None
```

Tree:

```text
    9
```

---

Now build the right subtree:

```text
preorder = [20, 15, 7]
inorder  = [15, 20, 7]
```

Root:

```text
20
```

Find `20` in inorder:

```text
[15, 20, 7]
     ↑
```

Index:

```text
1
```

Therefore:

```text
Left:

preorder = [15]
inorder  = [15]
```

Right:

```text
preorder = [7]
inorder  = [7]
```

So:

```text
        20
       /  \
      15   7
```

Finally:

```text
        3
       / \
      9   20
         /  \
        15   7
```

---

# Code

```python
class Solution:

    def buildTree(
        self,
        preorder: List[int],
        inorder: List[int]
    ) -> Optional[TreeNode]:

        # No elements → empty tree
        if not preorder:
            return None

        # First element of preorder is root
        root = TreeNode(preorder[0])

        # Find root position in inorder
        index = inorder.index(preorder[0])

        # Build left subtree
        root.left = self.buildTree(
            preorder[1:index + 1],
            inorder[:index]
        )

        # Build right subtree
        root.right = self.buildTree(
            preorder[index + 1:],
            inorder[index + 1:]
        )

        return root
```

---

# Why Does Preorder Give the Root?

Preorder traversal is:

```text
Root → Left → Right
```

Therefore the first element of every preorder array/subarray is always:

```text
Root of that subtree
```

So:

```python
root = TreeNode(preorder[0])
```

---

# Why Does Inorder Give the Boundary?

Inorder traversal is:

```text
Left → Root → Right
```

Once we find the root:

```text
        Root
```

everything:

```text
before root
```

belongs to the left subtree.

Everything:

```text
after root
```

belongs to the right subtree.

Therefore:

```python
inorder[:index]
```

is left.

And:

```python
inorder[index+1:]
```

is right.

---

# Base Case

```python
if not preorder:
    return None
```

If there are no elements, there is no subtree to build.

Therefore:

```text
Empty preorder
→ Empty tree
→ None
```

---

# Important Rule for Splitting Preorder

This is the easiest way to remember it.

If:

```text
root index in inorder = index
```

then:

```text
Left subtree size = index
```

Therefore:

```text
Left preorder:
preorder[1:index+1]
```

And the remaining elements belong to the right subtree:

```text
Right preorder:
preorder[index+1:]
```

---

# Visual Formula

```text
PREORDER

[ ROOT | LEFT SUBTREE | RIGHT SUBTREE ]
    0        index nodes

             ↓

INORDER

[ LEFT SUBTREE | ROOT | RIGHT SUBTREE ]
                   ↑
                 index
```

Therefore:

```text
preorder[0]
        ↓
      ROOT

preorder[1:index+1]
        ↓
   LEFT SUBTREE

preorder[index+1:]
        ↓
  RIGHT SUBTREE
```

And:

```text
inorder[:index]
        ↓
   LEFT SUBTREE

inorder[index+1:]
        ↓
  RIGHT SUBTREE
```

---

# Important Interview Point

The two traversal arrays must have the same number of elements.

Also, the standard problem assumes the tree has **unique node values**.

Why?

Because we use:

```python
inorder.index(preorder[0])
```

to find the root's position.

If duplicate values existed, `.index()` would not uniquely identify which occurrence represents the root.

---

# Complexity

Your exact implementation uses:

```python
inorder.index(...)
```

and creates new slices:

```python
preorder[...]
inorder[...]
```

Because of this, the practical worst-case time complexity can be:

```text
Time → O(n²)
```

especially for a skewed tree.

The recursion stack uses:

```text
Space → O(h)
```

and the slicing also creates additional arrays, so the implementation has additional memory overhead.

---

# Optimized Approach

The main problems with the current solution are:

```text
1. inorder.index() → O(n)
2. Slicing preorder → creates new list
3. Slicing inorder → creates new list
```

We can optimize all of this.

Use a hashmap:

```python
inorder_map[value] = index
```

Then finding the root's position becomes:

```text
O(1)
```

Instead of creating new arrays, use indexes:

```text
preorderStart
preorderEnd
inorderStart
inorderEnd
```

---

# Optimized Code

```python
class Solution:

    def buildTree(self, preorder, inorder):

        # Map value → index in inorder
        inorder_map = {
            value: i
            for i, value in enumerate(inorder)
        }

        def build(
            preorderStart,
            preorderEnd,
            inorderStart,
            inorderEnd
        ):

            # No elements
            if preorderStart > preorderEnd:
                return None

            # First preorder element is root
            rootValue = preorder[preorderStart]
            root = TreeNode(rootValue)

            # Find root in inorder in O(1)
            rootIndex = inorder_map[rootValue]

            # Number of nodes in left subtree
            leftSize = rootIndex - inorderStart

            # Build left subtree
            root.left = build(
                preorderStart + 1,
                preorderStart + leftSize,
                inorderStart,
                rootIndex - 1
            )

            # Build right subtree
            root.right = build(
                preorderStart + leftSize + 1,
                preorderEnd,
                rootIndex + 1,
                inorderEnd
            )

            return root

        return build(
            0,
            len(preorder) - 1,
            0,
            len(inorder) - 1
        )
```

---

# Why `leftSize`?

This is the key to understanding the optimized solution.

Suppose:

```text
inorder = [9, 3, 15, 20, 7]
```

Root:

```text
3
```

Root index:

```text
1
```

If the current inorder range starts at:

```text
0
```

then:

```python
leftSize = rootIndex - inorderStart
```

becomes:

```text
leftSize = 1 - 0
         = 1
```

So the left subtree contains:

```text
1 node
```

We use that number to split preorder.

---

# Optimized Preorder Split

Suppose:

```text
preorder = [3, 9, 20, 15, 7]
```

Root is:

```text
3
```

Left subtree size:

```text
1
```

Therefore:

```text
Root:
index 0

Left subtree:
index 1 → 1

Right subtree:
index 2 → 4
```

So:

```text
preorderStart + 1
```

to:

```text
preorderStart + leftSize
```

is the left subtree.

And:

```text
preorderStart + leftSize + 1
```

starts the right subtree.

---

# Why Optimized Version Is O(n)

Each node is processed once.

Finding its inorder position:

```text
O(1)
```

because of the hashmap.

No slicing is performed.

Therefore:

```text
Time → O(n)
```

The recursion stack requires:

```text
Space → O(h)
```

plus the hashmap:

```text
O(n)
```

So total auxiliary space is:

```text
O(n)
```

---

# Basic vs Optimized

| Approach | Time | Space | Main Issue |
|---|---:|---:|---|
| Basic | `O(n²)` worst case | `O(n)` due to slicing/recursion | `.index()` + slicing |
| Optimized | `O(n)` | `O(n)` | Hashmap + index ranges |

---

# Common Mistakes

## 1. Using `preorder[1:index]`

Wrong:

```python
preorder[1:index]
```

Correct:

```python
preorder[1:index+1]
```

because the ending index is excluded.

The left subtree contains exactly `index` nodes.

---

## 2. Using `preorder[index:]` for Right Subtree

Wrong:

```python
preorder[index:]
```

Correct:

```python
preorder[index+1:]
```

because:

```text
preorder[0] = root
preorder[1:index+1] = left subtree
preorder[index+1:] = right subtree
```

---

## 3. Mixing Up Preorder and Inorder

Remember:

```text
Preorder → tells ROOT

Inorder → tells LEFT/RIGHT boundary
```

---

## 4. Forgetting `index + 1` in Inorder Right Side

Correct:

```python
inorder[index+1:]
```

because the root itself should not be included in either subtree.

---

# Revision Cheat Sheet

```text
Construct Binary Tree from Preorder + Inorder

Pattern:
Binary Tree + Recursion + Divide & Conquer

Preorder:
Root → Left → Right

Inorder:
Left → Root → Right

--------------------------------------------------

Most Important:

preorder[0]
→ ROOT

Find root index in inorder.

inorder[:index]
→ LEFT SUBTREE

inorder[index+1:]
→ RIGHT SUBTREE

--------------------------------------------------

Left subtree has `index` nodes.

Therefore:

Left preorder:
preorder[1:index+1]

Right preorder:
preorder[index+1:]

--------------------------------------------------

Why index + 1?

Python slicing excludes the ending index.

preorder[1:index+1]
contains exactly `index` elements.

--------------------------------------------------

Basic Approach:

inorder.index(root)
+
array slicing

Worst-case:
O(n²)

--------------------------------------------------

Optimized Approach:

Use:

value → inorder index

Hashmap gives:
O(1) root lookup.

Use index ranges instead of slicing.

Time:
O(n)

Space:
O(n)

--------------------------------------------------

Key Formula:

leftSize = rootIndex - inorderStart

Left preorder:
preorderStart + 1
to
preorderStart + leftSize

Right preorder starts at:
preorderStart + leftSize + 1

--------------------------------------------------

Interview Memory Trick:

Preorder tells:
"WHO IS ROOT?"

Inorder tells:
"WHO IS LEFT AND WHO IS RIGHT?"
```

---

# One-Line Pattern

```text
Take the first preorder element as the root, find it in inorder to split left/right subtrees, then recursively build both sides using the corresponding preorder elements.
```