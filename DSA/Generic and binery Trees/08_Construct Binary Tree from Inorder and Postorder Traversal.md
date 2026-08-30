# Construct Binary Tree from Inorder and Postorder Traversal

## Problem

Given two arrays:

```text
inorder
postorder
```

construct the original binary tree.

### Inorder

```text
Left → Root → Right
```

### Postorder

```text
Left → Right → Root
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
Postorder tells us the ROOT.
Inorder tells us where to split LEFT and RIGHT.
```

For every subtree:

```text
1. Take the current element from postorder as root.
2. Find that root's position in inorder.
3. Everything left of root → left subtree.
4. Everything right of root → right subtree.
5. Recursively build the subtrees.
```

---

# Important Difference From Preorder + Inorder

For:

```text
Preorder + Inorder
```

we process preorder from:

```text
LEFT → RIGHT
```

because:

```text
Preorder = Root → Left → Right
```

But here:

```text
Postorder = Left → Right → Root
```

So we process postorder from:

```text
RIGHT → LEFT
```

This is why we build:

```python
root.right
```

before:

```python
root.left
```

---

# Example

```text
inorder   = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
```

Tree:

```text
        3
       / \
      9   20
         /  \
        15   7
```

---

# Brute Force / Basic Approach

## Idea

Take the last element of `postorder` as the root.

Why?

Because:

```text
Postorder:

Left → Right → Root
```

Therefore:

```text
postorder[-1]
```

is the root.

Then find the root in inorder.

Example:

```text
inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
```

Root:

```text
3
```

In inorder:

```text
[9 | 3 | 15, 20, 7]
     ↑
    root
```

Therefore:

```text
Left subtree  = [9]
Right subtree = [15, 20, 7]
```

Then recursively construct both subtrees.

---

# Brute Force Code

```python
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        if not inorder:
            return None

        rootVal = postorder[-1]

        root = TreeNode(rootVal)

        index = inorder.index(rootVal)

        root.left = self.buildTree(
            inorder[:index],
            postorder[:index]
        )

        root.right = self.buildTree(
            inorder[index + 1:],
            postorder[index:-1]
        )

        return root
```

---

# Understanding the Slices

Suppose:

```text
inorder = [9, 3, 15, 20, 7]
```

Root:

```text
3
```

Index:

```text
1
```

Therefore:

```text
Left inorder:

[9]
```

and:

```text
Right inorder:

[15, 20, 7]
```

Since postorder is:

```text
[Left | Right | Root]
```

we get:

```text
postorder = [9 | 15, 20, 7 | 3]
```

Therefore:

```text
Left postorder:

[9]
```

and:

```text
Right postorder:

[15, 20, 7]
```

The root itself:

```text
3
```

is excluded.

---

# Brute Force Complexity

```text
inorder.index() → O(n)

Slicing → O(n)

Recursive calls → O(n)
```

Worst-case:

```text
Time → O(n²)
Space → O(n)
```

The `O(n²)` happens because every recursive call may search through a large part of `inorder`.

---

# Optimized Approach

The brute-force solution repeatedly does:

```python
inorder.index(rootVal)
```

This takes:

```text
O(n)
```

each time.

We can optimize this using a hashmap.

---

# Step 1: Create Hashmap

Store:

```text
value → index in inorder
```

Example:

```text
inorder = [9, 3, 15, 20, 7]
```

Hashmap:

```text
{
    9: 0,
    3: 1,
    15: 2,
    20: 3,
    7: 4
}
```

Now:

```python
position[rootVal]
```

gives the index in:

```text
O(1)
```

---

# Step 2: Use `postIndex`

Instead of creating new postorder arrays, maintain:

```python
postIndex = len(postorder) - 1
```

It points to the current root in postorder.

Remember:

```text
Postorder:

Left → Right → Root
```

So the last element is root.

After taking the root:

```python
postIndex -= 1
```

Now it points to the next element from the right.

Therefore we process:

```text
RIGHT → LEFT
```

---

# Step 3: Use `left` and `right`

Instead of slicing:

```python
inorder[:index]
inorder[index + 1:]
```

we maintain the current inorder range:

```text
left ... right
```

If:

```text
mid = position[rootVal]
```

then:

```text
Left subtree:
left ... mid - 1

Right subtree:
mid + 1 ... right
```

---

# Why Build Right Before Left?

This is the most important point in this problem.

Postorder is:

```text
Left → Right → Root
```

We start from the end:

```text
Root → Right → Left
```

Example:

```text
postorder = [9, 15, 7, 20, 3]
                         ↑
                       root
```

Start from the end:

```text
3 → 20 → 7 → 15 → 9
```

So after creating root `3`:

```text
20
```

belongs to the right subtree.

Therefore we must build:

```python
root.right
```

first.

Then:

```text
15
```

belongs to the left subtree.

So:

```python
root.left
```

comes after the right subtree.

### Remember

```text
Preorder + Inorder:

Root → Left → Right
          ↓
Build Left first


Postorder + Inorder:

Left → Right → Root

From the end:

Root → Right → Left
          ↓
Build Right first
```

---

# Optimized Code

```python
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        position = {}

        # Store value → index in inorder
        for i in range(len(inorder)):
            position[inorder[i]] = i

        # Start from the last element of postorder
        postIndex = len(postorder) - 1

        def solve(left, right):
            nonlocal postIndex

            # No elements in this subtree
            if left > right:
                return None

            # Current root
            rootVal = postorder[postIndex]
            postIndex -= 1

            root = TreeNode(rootVal)

            # Find root in inorder
            mid = position[rootVal]

            # Build RIGHT first
            root.right = solve(mid + 1, right)

            # Build LEFT
            root.left = solve(left, mid - 1)

            return root

        return solve(0, len(inorder) - 1)
```

---

# Dry Run

Given:

```text
inorder   = [9, 3, 15, 20, 7]

postorder = [9, 15, 7, 20, 3]
```

Initially:

```text
postIndex = 4
```

---

## Step 1

```text
postorder[4] = 3
```

So:

```text
root = 3
```

Then:

```text
postIndex = 3
```

Find `3` in inorder:

```text
position[3] = 1
```

Therefore:

```text
Left  → index 0
Right → indexes 2 to 4
```

Build:

```python
root.right = solve(2, 4)
```

first.

---

## Step 2

Now:

```text
postIndex = 3
```

Take:

```text
postorder[3] = 20
```

So:

```text
root = 20
```

Then:

```text
postIndex = 2
```

Find:

```text
position[20] = 3
```

Therefore:

```text
Left  → index 2
Right → index 4
```

Again, build right first.

---

## Step 3

```text
postorder[2] = 7
```

So:

```text
root = 7
```

`7` is a leaf.

Return:

```text
7
```

---

## Step 4

Now:

```text
postIndex = 1
```

Take:

```text
postorder[1] = 15
```

So:

```text
root = 15
```

`15` is a leaf.

Return:

```text
15
```

---

## Step 5

Now:

```text
postIndex = 0
```

Take:

```text
postorder[0] = 9
```

So:

```text
root = 9
```

`9` is a leaf.

---

# Final Tree

```text
        3
       / \
      9   20
         /  \
        15   7
```

---

# Why Does `postIndex` Move Backward?

Because postorder is:

```text
Left → Right → Root
```

The root is at the end.

Therefore we start:

```python
postIndex = len(postorder) - 1
```

and move:

```text
RIGHT → LEFT
```

Example:

```text
postorder:

[9, 15, 7, 20, 3]
                 ↑
              start here

3 → 20 → 7 → 15 → 9
```

This gives:

```text
Root → Right → Left
```

which is exactly why the code does:

```python
root.right = solve(...)
root.left = solve(...)
```

---

# Why Do We Need `nonlocal postIndex`?

`postIndex` is created outside `solve()`:

```python
postIndex = len(postorder) - 1
```

But we modify it inside:

```python
postIndex -= 1
```

Therefore we need:

```python
nonlocal postIndex
```

This allows every recursive call to share the same `postIndex`.

Think:

```text
One postorder pointer
        ↓
All recursive calls use it
```

---

# Why No Postorder Range?

Notice that optimized recursion only receives:

```python
solve(left, right)
```

There is no:

```text
postorder left/right
```

range.

That's because `postIndex` automatically keeps track of the next root in postorder.

Since postorder is processed backwards:

```text
Root → Right → Left
```

the next unused element automatically belongs to the correct subtree.

---

# Basic vs Optimized

| | Basic | Optimized |
|---|---|---|
| Find root in inorder | `.index()` | Hashmap |
| Inorder slicing | Yes | No |
| Postorder slicing | Yes | No |
| Pointer | No | `postIndex` |
| Time | O(n²) worst case | O(n) |
| Space | O(n) | O(n) |

---

# Important Interview Points

### 1. Root comes from postorder

```python
postorder[postIndex]
```

Because:

```text
Postorder = Left → Right → Root
```

---

### 2. Inorder tells the split

```python
mid = position[rootVal]
```

Everything before `mid`:

```text
Left subtree
```

Everything after `mid`:

```text
Right subtree
```

---

### 3. Process postorder backwards

```python
postIndex = len(postorder) - 1
```

because the root is at the end.

---

### 4. Build right before left

Because backwards postorder becomes:

```text
Root → Right → Left
```

Therefore:

```python
root.right = solve(...)
root.left = solve(...)
```

---

### 5. Use hashmap

Instead of:

```python
inorder.index(rootVal)
```

use:

```python
position[rootVal]
```

This changes lookup from:

```text
O(n) → O(1)
```

---

### 6. Avoid slicing

Instead of creating new arrays, use:

```text
left
right
```

to represent the current inorder range.

---

# Common Mistakes

## Mistake 1: Building Left First

Wrong:

```python
root.left = solve(...)
root.right = solve(...)
```

for this optimized postorder solution.

Correct:

```python
root.right = solve(...)
root.left = solve(...)
```

because we are traversing postorder backwards.

---

## Mistake 2: Starting `postIndex` at 0

Wrong:

```python
postIndex = 0
```

Correct:

```python
postIndex = len(postorder) - 1
```

because the root is at the end of postorder.

---

## Mistake 3: Including `mid` in Subtrees

Wrong:

```python
solve(left, mid)
```

Correct:

```python
solve(left, mid - 1)
```

and:

```python
solve(mid + 1, right)
```

The `mid` element is already the root.

---

## Mistake 4: Forgetting `nonlocal`

We modify:

```python
postIndex -= 1
```

inside `solve()`.

Therefore:

```python
nonlocal postIndex
```

is required.

---

# Complexity

## Basic

```text
Time  → O(n²) worst case
Space → O(n)
```

## Optimized

```text
Time  → O(n)
Space → O(n)
```

Why `O(n)` time?

```text
Every node is processed once
+
Every inorder lookup is O(1)
```

---

# Revision Cheat Sheet

```text
Construct Binary Tree
from Inorder + Postorder

Pattern:
Recursion + Divide and Conquer

--------------------------------------------------

Inorder:

Left → Root → Right

Postorder:

Left → Right → Root

--------------------------------------------------

Root:

postorder[last]

or optimized:

postorder[postIndex]

--------------------------------------------------

Why process backwards?

Postorder:

Left → Right → Root

Backward:

Root → Right → Left

--------------------------------------------------

Therefore:

Build RIGHT first
Build LEFT second

--------------------------------------------------

Hashmap:

position[value] = index

Why?

inorder.index()
→ O(n)

position[value]
→ O(1)

--------------------------------------------------

Current inorder range:

left ... right

Root position:

mid = position[rootVal]

Left subtree:

left ... mid - 1

Right subtree:

mid + 1 ... right

--------------------------------------------------

Base case:

if left > right:
    return None

--------------------------------------------------

Important pointer:

postIndex

Starts at:

len(postorder) - 1

Moves:

postIndex -= 1

--------------------------------------------------

Optimized complexity:

Time  → O(n)
Space → O(n)
```

---

# Memory Trick

```text
PREORDER + INORDER

Preorder:
Root → Left → Right

Start from LEFT

Build:
Root → Left → Right


POSTORDER + INORDER

Postorder:
Left → Right → Root

Start from RIGHT

Build:
Root → Right → Left
```

### One-Line Pattern

```text
Take the root from the end of postorder, find it in inorder, build the RIGHT subtree first because postorder is being processed backwards, then build the LEFT subtree.
```