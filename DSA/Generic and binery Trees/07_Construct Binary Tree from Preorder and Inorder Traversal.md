# Construct Binary Tree from Preorder and Inorder Traversal

## Problem

Given two arrays:

```text
preorder
inorder
```

construct the original binary tree.

### Preorder

```text
Root → Left → Right
```

### Inorder

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
Inorder tells us where to split LEFT and RIGHT.
```

For every subtree:

```text
1. Take the current element from preorder as root.
2. Find that root's position in inorder.
3. Everything left of root → left subtree.
4. Everything right of root → right subtree.
5. Recursively build both subtrees.
```

---

# Example

```text
preorder = [3, 9, 20, 15, 7]
inorder  = [9, 3, 15, 20, 7]
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

# Step 1: Find the Root

Preorder:

```text
[3, 9, 20, 15, 7]
```

Preorder is:

```text
Root → Left → Right
```

Therefore:

```text
3
```

is the root.

```python
rootVal = preorder[preIndex]
```

---

# Step 2: Find Root in Inorder

Inorder:

```text
[9, 3, 15, 20, 7]
```

Root:

```text
3
```

Its position is:

```text
index = 1
```

So:

```text
Left subtree:

[9]
```

and:

```text
Right subtree:

[15, 20, 7]
```

Because inorder is:

```text
Left → Root → Right
```

---

# Important Rule

Remember this:

```text
PREORDER

[ ROOT | LEFT | RIGHT ]

INORDER

[ LEFT | ROOT | RIGHT ]
```

Therefore:

```text
preorder → tells ROOT

inorder → tells LEFT and RIGHT
```

This is the entire logic of the problem.

---

# Why Do We Need `preIndex`?

In the optimized solution we don't create new preorder arrays.

Instead, we maintain:

```python
preIndex = 0
```

It points to the next root that needs to be created.

Example:

```text
preorder = [3, 9, 20, 15, 7]
```

Initially:

```text
preIndex = 0
```

Take:

```text
preorder[0] = 3
```

Then:

```text
preIndex = 1
```

Now take:

```text
preorder[1] = 9
```

Then:

```text
preIndex = 2
```

Now:

```text
preorder[2] = 20
```

And so on.

So `preIndex` simply moves through preorder:

```text
0 → 1 → 2 → 3 → 4
```

---

# Why `nonlocal preIndex`?

`solve()` is an inner function:

```python
preIndex = 0

def solve(left, right):
    nonlocal preIndex
```

All recursive calls need to modify the **same `preIndex`**.

Without `nonlocal`, Python would treat:

```python
preIndex += 1
```

as trying to create a local variable inside `solve()`.

With:

```python
nonlocal preIndex
```

all recursive calls share the same variable.

Think:

```text
One preorder pointer
        ↓
All recursive calls use it
```

---

# Why Do We Need `position`?

We need to find the root's position in inorder.

A simple approach would be:

```python
inorder.index(rootVal)
```

But `.index()` takes:

```text
O(n)
```

in the worst case.

Instead, create a hashmap:

```python
position = {}
```

Store:

```text
value → index
```

Example:

```text
inorder = [9, 3, 15, 20, 7]
```

Then:

```text
position = {
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

# Why `left` and `right`?

Instead of creating new inorder arrays like:

```python
inorder[:index]
inorder[index+1:]
```

we simply maintain the current range:

```text
left ... right
```

For example:

```text
inorder = [9, 3, 15, 20, 7]
```

Initially:

```text
left = 0
right = 4
```

This means:

```text
Use the complete inorder array.
```

If root `3` is at:

```text
mid = 1
```

then:

```text
Left subtree:
left → mid - 1

Right subtree:
mid + 1 → right
```

So:

```text
Left:
0 → 0

Right:
2 → 4
```

---

# Why `left > right`?

Base case:

```python
if left > right:
    return None
```

This means there are no elements left in the current subtree.

Example:

```text
left = 2
right = 1
```

Since:

```text
2 > 1
```

the range is empty.

Therefore:

```text
No subtree → None
```

---

# Optimized Code

```python
class Solution:
    def buildTree(
        self,
        preorder: List[int],
        inorder: List[int]
    ) -> Optional[TreeNode]:

        position = {}

        # Store value → index in inorder
        for i in range(len(inorder)):
            position[inorder[i]] = i

        # Pointer for preorder
        preIndex = 0

        def solve(left, right):
            nonlocal preIndex

            # No elements
            if left > right:
                return None

            # Current root comes from preorder
            rootVal = preorder[preIndex]
            preIndex += 1

            root = TreeNode(rootVal)

            # Find root in inorder
            mid = position[rootVal]

            # Build left subtree
            root.left = solve(left, mid - 1)

            # Build right subtree
            root.right = solve(mid + 1, right)

            return root

        return solve(0, len(inorder) - 1)
```

---

# Dry Run

Consider:

```text
preorder = [3, 9, 20, 15, 7]
inorder  = [9, 3, 15, 20, 7]
```

Initially:

```text
preIndex = 0
```

Call:

```python
solve(0, 4)
```

---

## Call 1

```text
preIndex = 0
```

Take:

```text
preorder[0] = 3
```

So:

```text
root = 3
```

Increment:

```text
preIndex = 1
```

Find `3`:

```text
position[3] = 1
```

So:

```text
left subtree  = inorder[0:0]
right subtree = inorder[2:4]
```

Recursively:

```python
solve(0, 0)
solve(2, 4)
```

---

## Build Left Subtree

Call:

```python
solve(0, 0)
```

`preIndex` is:

```text
1
```

Take:

```text
preorder[1] = 9
```

So:

```text
root = 9
```

Increment:

```text
preIndex = 2
```

Find:

```text
position[9] = 0
```

Left:

```text
solve(0, -1)
```

No elements:

```text
return None
```

Right:

```text
solve(1, 0)
```

Again:

```text
left > right
```

so:

```text
return None
```

Therefore:

```text
    9
```

is complete.

---

## Build Right Subtree

Now:

```text
preIndex = 2
```

Call:

```python
solve(2, 4)
```

Take:

```text
preorder[2] = 20
```

So:

```text
root = 20
```

Increment:

```text
preIndex = 3
```

Find:

```text
position[20] = 3
```

Therefore:

```text
Left:
solve(2, 2)

Right:
solve(4, 4)
```

---

## Build `20`'s Left

```text
preIndex = 3
```

Take:

```text
preorder[3] = 15
```

So:

```text
root = 15
```

`15` is a leaf.

Therefore:

```text
    15
```

---

## Build `20`'s Right

```text
preIndex = 4
```

Take:

```text
preorder[4] = 7
```

So:

```text
root = 7
```

`7` is a leaf.

Therefore:

```text
    7
```

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

# The Most Important Part to Understand

The recursion is doing this:

```text
preorder tells us WHICH node to create.

inorder tells us WHERE that node splits the tree.
```

For every root:

```text
1. Take preorder[preIndex]
2. Find it in inorder
3. Build left side
4. Build right side
```

---

# Why Left Subtree Is `solve(left, mid - 1)`?

In inorder:

```text
[ LEFT | ROOT | RIGHT ]
```

Root is at:

```text
mid
```

Therefore everything before `mid` is left subtree:

```text
left ... mid - 1
```

So:

```python
root.left = solve(left, mid - 1)
```

---

# Why Right Subtree Is `solve(mid + 1, right)`?

Everything after root belongs to the right subtree:

```text
mid + 1 ... right
```

So:

```python
root.right = solve(mid + 1, right)
```

We use:

```text
mid + 1
```

because `mid` itself is the root and must not be included again.

---

# Why Don't We Have a Separate Preorder Range?

This is an important difference from the basic solution.

In the basic solution we explicitly create:

```python
preorder[1:index+1]
preorder[index+1:]
```

In the optimized solution we don't.

We use:

```python
preIndex
```

to automatically consume preorder elements in the correct order.

Because preorder is:

```text
Root → Left → Right
```

once we create the root, the next unused preorder element is automatically the root of the left subtree.

After the left subtree is completely built, the next unused preorder element is automatically the root of the right subtree.

Therefore one pointer is enough:

```text
preIndex
```

---

# Basic vs Optimized

## Basic Version

Uses:

```python
root = TreeNode(preorder[0])

index = inorder.index(preorder[0])

root.left = self.buildTree(
    preorder[1:index+1],
    inorder[:index]
)

root.right = self.buildTree(
    preorder[index+1:],
    inorder[index+1:]
)
```

Problems:

```text
inorder.index() → O(n)

Slicing → creates new lists
```

Worst-case:

```text
Time → O(n²)
```

---

# Optimized Version

Uses:

```text
Hashmap
+
preIndex
+
inorder range
```

Instead of:

```python
inorder.index(rootVal)
```

we use:

```python
position[rootVal]
```

Instead of:

```python
inorder[:index]
inorder[index+1:]
```

we use:

```text
left
right
```

Therefore:

```text
Time → O(n)
```

---

# Complexity

### Time

Every node is created once:

```text
O(n)
```

Hashmap lookup:

```text
O(1)
```

Therefore:

```text
Time → O(n)
```

### Space

Hashmap stores every node:

```text
O(n)
```

Recursion stack:

```text
O(h)
```

where:

```text
h = height of tree
```

Overall auxiliary space:

```text
O(n)
```

---

# Important Interview Points

### 1. Preorder gives root

```text
preorder[preIndex]
```

is the current root.

### 2. Inorder gives the boundary

```text
position[rootVal]
```

tells us where left and right subtrees are separated.

### 3. `preIndex` always moves forward

```text
preIndex += 1
```

We never move it backward.

### 4. No slicing in optimized solution

Use:

```text
left
right
```

instead.

### 5. Hashmap avoids repeated searching

```text
position[value] → index
```

gives `O(1)` lookup.

### 6. Unique values are assumed

The standard problem assumes node values are unique, which allows:

```python
position[rootVal]
```

to identify exactly one position.

---

# Common Mistakes

## Mistake 1: Taking `inorder[0]` as root

Wrong.

Root comes from:

```text
preorder
```

because preorder starts with root.

---

## Mistake 2: Including root in both subtrees

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

---

## Mistake 3: Forgetting `preIndex += 1`

After taking the current root:

```python
rootVal = preorder[preIndex]
```

we must move:

```python
preIndex += 1
```

Otherwise every recursive call would keep using the same root.

---

## Mistake 4: Forgetting `nonlocal`

Because `preIndex` belongs to the outer function:

```python
preIndex = 0
```

the nested `solve()` needs:

```python
nonlocal preIndex
```

to modify it.

---

# Revision Cheat Sheet

```text
Construct Binary Tree
from Preorder + Inorder

Pattern:
Recursion + Divide and Conquer

--------------------------------------------------

Preorder:

Root → Left → Right

Therefore:

preorder[preIndex]
        ↓
      ROOT

--------------------------------------------------

Inorder:

Left → Root → Right

Therefore:

position[rootVal]
        ↓
      MID

Everything before MID:
→ Left subtree

Everything after MID:
→ Right subtree

--------------------------------------------------

Important variables:

position
→ value → inorder index

preIndex
→ current root position in preorder

left, right
→ current inorder range

--------------------------------------------------

Recursive calls:

Left:

solve(left, mid - 1)

Right:

solve(mid + 1, right)

--------------------------------------------------

Base case:

if left > right:
    return None

--------------------------------------------------

Why preIndex?

Preorder is already in:

Root → Left → Right

So one pointer can consume
nodes in the correct order.

--------------------------------------------------

Why hashmap?

inorder.index()
→ O(n)

position[value]
→ O(1)

--------------------------------------------------

Why no slicing?

Slicing creates new arrays.

Use:

left, right

to represent the current range.

--------------------------------------------------

Complexity:

Time  → O(n)
Space → O(n)

--------------------------------------------------

Memory Trick:

Preorder tells:
"WHO IS THE ROOT?"

Inorder tells:
"WHO IS ON THE LEFT
 AND WHO IS ON THE RIGHT?"
```

---

# One-Line Pattern

```text
Use preorder to pick the root, use a hashmap to find that root in inorder, recursively build the left and right ranges, and use one shared preIndex to consume preorder.
```