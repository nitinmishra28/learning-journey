# Symmetric Tree

## Problem

Given the root of a binary tree, determine whether the tree is **symmetric around its center**.

In simple words:

> The left subtree must be a **mirror image** of the right subtree.

### Example 1

```text
        1
       / \
      2   2
     / \ / \
    3  4 4  3
```

The tree is symmetric.

Answer:

```text
True
```

---

### Example 2

```text
        1
       / \
      2   2
       \   \
        3   3
```

The tree is not symmetric.

Answer:

```text
False
```

---

# Pattern

```text
Binary Tree + DFS + Mirror Comparison
```

The key idea is:

> We don't compare the left and right subtrees in the same direction. We compare them as **mirror images**.

Normally, for the Same Tree problem:

```text
p.left  ↔ q.left
p.right ↔ q.right
```

But for a symmetric tree:

```text
p.left  ↔ q.right
p.right ↔ q.left
```

This is the main difference.

---

# Main Idea

Suppose we have:

```text
        1
       / \
      2   2
     / \ / \
    3  4 4  3
```

We compare:

```text
        2          2
       / \        / \
      3   4      4   3
```

The first pair is:

```text
left subtree root ↔ right subtree root
```

So:

```text
2 ↔ 2
```

Then their children must be compared in a **crossed** manner:

```text
left.left  ↔ right.right
left.right ↔ right.left
```

Therefore:

```text
3 ↔ 3
4 ↔ 4
```

This is exactly what the code does.

---

# Mirror Comparison

Your function:

```python
def isMirror(self, p, q):
```

takes two nodes and asks:

> Are these two subtrees mirror images of each other?

For example:

```text
        p                 q
        2                 2
       / \               / \
      3   4             4   3
```

We need:

```text
p.val == q.val
```

and:

```text
p.left  ↔ q.right
p.right ↔ q.left
```

---

# Three Important Cases

## Case 1: Both Nodes Are `None`

```python
if p is None and q is None:
    return True
```

This means:

```text
Both sides have no node
at this position.
```

Therefore they are mirror-compatible.

```text
True
```

---

# Case 2: Both Nodes Exist

```python
if p and q:
```

Now we need three things:

```text
1. Values must be equal.
2. p.left must mirror q.right.
3. p.right must mirror q.left.
```

So:

```python
return (
    p.val == q.val
    and self.isMirror(p.left, q.right)
    and self.isMirror(p.right, q.left)
)
```

The important part is:

```text
left ↔ right
right ↔ left
```

---

# Case 3: One Node Is `None`

```python
return False
```

Example:

```text
p:          q:

  2           2
 /             \
3               3
```

At one comparison:

```text
p.left = 3
q.right = None
```

One side has a node and the other does not.

Therefore the structure cannot be symmetric.

Return:

```text
False
```

---

# Why Do We Compare `p.left` With `q.right`?

This is the **most important part** of the problem.

Consider:

```text
        1
       / \
      2   2
     / \ / \
    3  4 4  3
```

Look at the mirror:

```text
        1
       / \
      2   2
     ↙     ↘
    3       3

     ↘     ↙
      4   4
```

Therefore:

```text
left side's LEFT
        ↕
right side's RIGHT
```

and:

```text
left side's RIGHT
        ↕
right side's LEFT
```

So:

```python
self.isMirror(p.left, q.right)
self.isMirror(p.right, q.left)
```

---

# Same Tree vs Symmetric Tree

This is a very important interview comparison.

## Same Tree

We compare corresponding positions:

```text
p.left  ↔ q.left
p.right ↔ q.right
```

Pattern:

```text
        p              q
       / \            / \
      L   R          L   R

      ↓              ↓
     L ↔ L          R ↔ R
```

---

## Symmetric Tree

We compare mirror positions:

```text
p.left  ↔ q.right
p.right ↔ q.left
```

Pattern:

```text
        p              q
       / \            / \
      L   R          R   L

      ↓              ↓
     L ↔ R          R ↔ L
```

### Memory Trick

```text
Same Tree:
same direction

Symmetric Tree:
opposite direction
```

---

# Complete Code

```python
class Solution:

    def isMirror(self, p, q):

        # Both nodes are None
        if p is None and q is None:
            return True

        # Both nodes exist
        if p and q:
            return (
                p.val == q.val
                and self.isMirror(p.left, q.right)
                and self.isMirror(p.right, q.left)
            )

        # One node is None
        return False

    def isSymmetric(self, root):

        return self.isMirror(root.left, root.right)
```

---

# Why Do We Start With `root.left` and `root.right`?

The root itself is the **center** of symmetry.

For:

```text
        1
       / \
      2   2
```

we don't need to compare:

```text
root ↔ root
```

Instead, we ask:

```text
Is root.left a mirror of root.right?
```

Therefore:

```python
return self.isMirror(root.left, root.right)
```

The root acts as the center line:

```text
        1
       / \
      /   \
     2     2
```

Everything on the left must mirror everything on the right.

---

# Dry Run

Consider:

```text
        1
       / \
      2   2
     / \ / \
    3  4 4  3
```

Call:

```python
isMirror(2, 2)
```

---

## Step 1 — Compare Root Children

```text
p.val = 2
q.val = 2
```

So:

```text
2 == 2
```

True.

Now recursively compare:

```text
p.left  ↔ q.right
p.right ↔ q.left
```

---

## Step 2 — Compare `3` and `3`

```text
p = 3
q = 3
```

Values match.

Then:

```text
None ↔ None
None ↔ None
```

Both return:

```text
True
```

Therefore:

```text
isMirror(3, 3) = True
```

---

## Step 3 — Compare `4` and `4`

Same logic:

```text
isMirror(4, 4) = True
```

---

## Step 4 — Back to Nodes `2` and `2`

We have:

```text
values equal      → True
left/right mirror → True
right/left mirror → True
```

Therefore:

```text
True
```

Final answer:

```text
True
```

---

# Dry Run: Not Symmetric

Consider:

```text
        1
       / \
      2   2
       \   \
        3   3
```

Start:

```text
isMirror(2, 2)
```

Values:

```text
2 == 2
```

True.

Now compare:

```text
p.left ↔ q.right
```

That is:

```text
None ↔ 3
```

One is `None`.

Therefore:

```text
False
```

The tree is not symmetric.

---

# Why Is This DFS?

The function recursively goes down the tree:

```text
isMirror(p, q)
       |
       +── isMirror(p.left, q.right)
       |
       +── isMirror(p.right, q.left)
```

We go deep into the corresponding mirror branches before returning.

So this is:

```text
DFS + Recursion
```

---

# Why Does Recursion Fit This Problem?

The problem itself has a recursive structure.

If two subtrees are mirrors, then:

```text
Current values must match
        AND
Their outer children must mirror
        AND
Their inner children must mirror
```

In code:

```python
p.val == q.val
and isMirror(p.left, q.right)
and isMirror(p.right, q.left)
```

So the recursive function is almost a direct translation of the problem definition.

---

# Brute Force

One possible brute-force approach is to create a representation of the left and right subtrees and compare one with the reverse/mirrored representation of the other.

For example, we could:

```text
1. Traverse the left subtree.
2. Traverse the right subtree.
3. Store their structures and values.
4. Compare them in mirrored order.
```

But this requires extra arrays/representations.

The direct recursive approach is much cleaner:

```text
Compare corresponding mirror nodes directly.
```

The direct recursive solution visits each node once.

---

# Complexity

Let:

```text
n = number of nodes
```

Every node is visited at most once.

Therefore:

```text
Time = O(n)
```

The recursion call stack can grow up to the height of the tree:

```text
Space = O(h)
```

where:

```text
h = height of tree
```

For a balanced tree:

```text
h = O(log n)
```

For a skewed tree:

```text
h = O(n)
```

So worst-case space:

```text
O(n)
```

---

# Complexity Comparison

| Approach | Idea | Time | Space |
|---|---|---:|---:|
| Brute Force | Build/compare subtree representations | O(n) | O(n) |
| Recursive Mirror DFS | Compare mirror nodes directly | O(n) | O(h) |

---

# Common Mistakes

## 1. Comparing Left With Left

Wrong:

```python
self.isMirror(p.left, q.left)
```

For symmetry, we need:

```python
self.isMirror(p.left, q.right)
```

because we are checking a mirror.

---

## 2. Comparing Right With Right

Wrong:

```python
self.isMirror(p.right, q.right)
```

Correct:

```python
self.isMirror(p.right, q.left)
```

---

## 3. Only Comparing Values

Wrong:

```python
return p.val == q.val
```

Values alone are not enough.

Structure must also be mirrored.

---

## 4. Forgetting the One-None Case

These are not mirrors:

```text
p = None
q = node
```

So:

```python
return False
```

is necessary.

---

## 5. Forgetting That Root Is the Center

We don't compare the root with another node.

We compare:

```python
root.left
```

with:

```python
root.right
```

because the root is the center of symmetry.

---

# Pattern Recognition

When you see:

> Check whether a binary tree is symmetric.

Think:

```text
Symmetric
    ↓
Mirror
    ↓
Compare two subtrees
    ↓
DFS
```

At every pair:

```text
Both None?
    ↓
True

One None?
    ↓
False

Both exist?
    ↓
Values equal
    ↓
LEFT ↔ RIGHT
RIGHT ↔ LEFT
```

### Shortcut

```text
Same Tree:
L ↔ L
R ↔ R

Symmetric Tree:
L ↔ R
R ↔ L
```

---

# Related Tree Problems

| Problem | Main Pattern |
|---|---|
| Same Tree | DFS + Same Position Comparison |
| Symmetric Tree | DFS + Mirror Comparison |
| Subtree of Another Tree | DFS + Same Tree |
| Invert Binary Tree | DFS + Swap Left/Right |
| Maximum Depth | DFS + Height |
| Balanced Tree | Postorder DFS + Height |
| Diameter | Postorder DFS + Height |

---

# Revision Cheat Sheet

```text
Symmetric Binary Tree

Meaning:
Left subtree must be a mirror
of the right subtree.

Pattern:
Binary Tree + DFS + Mirror Comparison

Start:
isMirror(root.left, root.right)

At every pair (p, q):

Case 1:
p is None AND q is None
    ↓
True

Case 2:
One is None
    ↓
False

Case 3:
Both exist
    ↓
p.val == q.val
AND
p.left  ↔ q.right
AND
p.right ↔ q.left

Important:

Same Tree:
p.left  ↔ q.left
p.right ↔ q.right

Symmetric Tree:
p.left  ↔ q.right
p.right ↔ q.left

Why?
Because we are comparing mirror positions.

Time:
O(n)

Space:
O(h)

Balanced tree:
O(log n)

Skewed tree:
O(n)
```

# One-Line Pattern

```text
Symmetric Tree → Compare left and right subtrees as mirrors: left ↔ right and right ↔ left.
```

# Interview Memory Trick

```text
Same Tree:
"Same side"

Symmetric Tree:
"Opposite side"

Same:
L ↔ L
R ↔ R

Mirror:
L ↔ R
R ↔ L
```
```