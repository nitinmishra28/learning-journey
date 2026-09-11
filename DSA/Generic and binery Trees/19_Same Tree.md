# Same Tree

## Problem

Given the roots of two binary trees `p` and `q`, determine whether the two trees are **exactly the same**.

Two binary trees are considered the same if:

```text
1. They have the same structure.
2. Corresponding nodes have the same value.
```

### Example 1

```text
Tree p:          Tree q:

    1                1
   / \              / \
  2   3            2   3
```

Both structure and values are the same.

Answer:

```text
True
```

---

### Example 2

```text
Tree p:          Tree q:

    1                1
   /                  \
  2                    2
```

Values are the same, but the structure is different.

Answer:

```text
False
```

---

### Example 3

```text
Tree p:          Tree q:

    1                1
   / \              / \
  2   3            2   4
```

Structure is the same, but corresponding values are different.

Answer:

```text
False
```

---

# Pattern

```text
Binary Tree + DFS + Recursion
```

The important idea is:

> Compare the two trees **node by node at the same position**.

For every pair of nodes:

```text
p node ↔ q node
```

we check:

```text
1. Are both nodes None?
2. Is one None and the other not?
3. Do their values match?
4. Are their left subtrees the same?
5. Are their right subtrees the same?
```

---

# Main Idea

We recursively compare corresponding nodes.

Imagine:

```text
        p                    q
        1                    1
       / \                  / \
      2   3                2   3
```

We compare:

```text
p = 1 ↔ q = 1
```

Then:

```text
p.left  ↔ q.left
p.right ↔ q.right
```

So:

```text
        1                 1
       / \               / \
      2   3             2   3
     ↕   ↕             ↕   ↕
    2 ↔ 2             3 ↔ 3
```

If every corresponding pair matches, the trees are the same.

---

# Three Important Cases

## Case 1: Both Nodes Are `None`

```python
if p is None and q is None:
    return True
```

This means:

```text
Both trees have no node at this position.
```

Example:

```text
p:       q:

  1        1
 /        /
2        2

p.right = None
q.right = None
```

Both are empty at that position.

Therefore:

```text
True
```

This is the **base case** of the recursion.

---

# Case 2: Both Nodes Exist

```python
if p and q:
```

Now both nodes are present.

We need to check:

```python
p.val == q.val
```

and recursively compare:

```python
p.left  with q.left
p.right with q.right
```

So:

```python
return (
    p.val == q.val
    and self.isSameTree(p.left, q.left)
    and self.isSameTree(p.right, q.right)
)
```

There are three conditions:

```text
p.val == q.val
        AND
left subtrees are same
        AND
right subtrees are same
```

All three must be `True`.

---

# Case 3: One Node Is `None`

```python
return False
```

This happens when one tree has a node but the other doesn't.

Example:

```text
p:              q:

    1               1
   /                 \
  2                   2
```

At the left position:

```text
p.left  = 2
q.left  = None
```

The structures are different.

Therefore:

```text
False
```

---

# Why Do We Need to Check Structure?

This is very important.

It is not enough to compare only values.

Consider:

```text
p:

    1
   /
  2
```

and:

```text
q:

    1
     \
      2
```

Both contain:

```text
1, 2
```

But they are not the same tree.

The position of `2` is different:

```text
p → left child
q → right child
```

Therefore, our recursion compares:

```python
p.left  with q.left
p.right with q.right
```

This automatically checks the structure.

---

# Why Compare Left With Left and Right With Right?

Suppose:

```text
p:              q:

    1               1
   / \             / \
  2   3           3   2
```

If we simply checked whether both trees contain the same values, we might incorrectly say:

```text
True
```

But corresponding positions are different.

We specifically compare:

```text
p.left  ↔ q.left
p.right ↔ q.right
```

So:

```text
2 ↔ 3
```

fails immediately.

Therefore:

```text
False
```

---

# Complete Code

```python
class Solution:

    def isSameTree(self, p, q):

        # Both nodes are None
        if p is None and q is None:
            return True

        # Both nodes exist
        if p and q:
            return (
                p.val == q.val
                and self.isSameTree(p.left, q.left)
                and self.isSameTree(p.right, q.right)
            )

        # One node is None and the other exists
        return False
```

---

# How the Recursion Works

The most important thing to understand is that:

```python
self.isSameTree(p.left, q.left)
```

means:

> "Go and check whether the left subtree of `p` is exactly the same as the left subtree of `q`."

Similarly:

```python
self.isSameTree(p.right, q.right)
```

means:

> "Go and check whether the right subtrees are exactly the same."

So the problem is broken into smaller versions of itself.

```text
isSameTree(p, q)
       |
       +---- isSameTree(p.left, q.left)
       |
       +---- isSameTree(p.right, q.right)
```

This is classic recursion.

---

# Why `and` Is Used?

Your code:

```python
return (
    p.val == q.val
    and self.isSameTree(p.left, q.left)
    and self.isSameTree(p.right, q.right)
)
```

means:

```text
Current values same
        AND
Left subtrees same
        AND
Right subtrees same
```

For the trees to be identical:

```text
EVERY condition must be True.
```

If even one condition is false:

```text
False
```

---

# Dry Run

Consider:

```text
p:              q:

        1               1
       / \             / \
      2   3           2   3
```

Start:

```text
isSameTree(1, 1)
```

### Step 1 — Compare Values

```text
1 == 1
```

True.

Now compare left:

```text
isSameTree(2, 2)
```

---

## Node `2`

```text
2 == 2
```

True.

Compare left:

```text
None ↔ None
```

Returns:

```text
True
```

Compare right:

```text
None ↔ None
```

Returns:

```text
True
```

Therefore:

```text
isSameTree(2, 2) = True
```

---

## Node `3`

Similarly:

```text
isSameTree(3, 3) = True
```

---

## Back to Root

We now have:

```text
1 == 1                 → True
left subtree same      → True
right subtree same     → True
```

Therefore:

```text
True and True and True
= True
```

Final answer:

```text
True
```

---

# Dry Run: Different Value

Consider:

```text
p:              q:

    1               1
   / \             / \
  2   3           2   4
```

At root:

```text
1 == 1
```

True.

Left subtree:

```text
2 == 2
```

True.

Right subtree:

```text
3 == 4
```

False.

Therefore:

```python
True and True and False
```

gives:

```text
False
```

We don't need to explore further because the trees are already known to be different.

---

# Dry Run: Different Structure

Consider:

```text
p:              q:

    1               1
   /                 \
  2                   2
```

At root:

```text
1 == 1
```

True.

Now compare left:

```text
p.left = 2
q.left = None
```

So:

```python
if p is None and q is None:
```

is false.

Then:

```python
if p and q:
```

is also false because `q` is `None`.

Therefore:

```python
return False
```

So the trees are not the same.

---

# Why Does the Base Case Return `True`?

This is a common recursion question.

```python
if p is None and q is None:
    return True
```

Think of it as:

```text
Both trees have reached the end
at the same position.
```

There is nothing left to compare.

Therefore:

```text
They match.
```

So:

```text
True
```

---

# Why Does One `None` Return `False`?

Consider:

```text
p = None
q = 5
```

At this position:

```text
p has no node
q has a node
```

Therefore the structures are different.

So:

```text
False
```

---

# Recursion Tree

For:

```text
        1
       / \
      2   3
```

the recursive comparison looks like:

```text
                 compare(1, 1)
                    /      \
                   /        \
          compare(2, 2)   compare(3, 3)
             /    \          /    \
            /      \        /      \
         None     None    None    None
```

Every corresponding position is checked.

---

# Brute Force

A possible brute-force idea would be:

1. Traverse both trees.
2. Store their values and structure in separate arrays.
3. Compare the resulting representations.

For example, using preorder traversal with `None` markers:

```text
Tree:

    1
   / \
  2   3
```

can become:

```text
[1, 2, None, None, 3, None, None]
```

Then compare the representations.

This takes:

```text
Time  = O(n)
Space = O(n)
```

However, there is no real need to create the complete representation.

We can compare the two trees **directly during DFS**, which is simpler and avoids storing both traversals.

---

# Optimized Approach

The direct recursive comparison:

```python
isSameTree(p, q)
```

does the comparison while traversing.

We don't need:

```text
Tree 1 → Array
Tree 2 → Array
        ↓
Compare arrays
```

Instead:

```text
Tree 1 + Tree 2
       ↓
Compare directly
       ↓
DFS
```

Every node is checked once.

---

# Complexity

Let:

```text
n = number of nodes compared
```

In the worst case, we visit every node in both trees.

Therefore:

```text
Time = O(n)
```

The recursion call stack can go as deep as the height of the tree:

```text
Space = O(h)
```

where:

```text
h = height of the tree
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
| Brute Force | Serialize both trees and compare | O(n) | O(n) |
| Recursive DFS | Compare corresponding nodes directly | O(n) | O(h) |

The recursive approach is better in terms of auxiliary space because we don't need to build complete traversal arrays.

---

# Common Mistakes

## 1. Only Comparing Values

Wrong:

```python
return p.val == q.val
```

This ignores the structure.

You must also compare:

```python
p.left  ↔ q.left
p.right ↔ q.right
```

---

## 2. Comparing Left With Right

Wrong:

```python
self.isSameTree(p.left, q.right)
```

Correct:

```python
self.isSameTree(p.left, q.left)
self.isSameTree(p.right, q.right)
```

Corresponding positions must be compared.

---

## 3. Forgetting the One-None Case

These are different:

```text
p = None
q = node
```

and:

```text
p = node
q = None
```

So after checking:

```python
if p is None and q is None:
```

we must eventually return:

```python
False
```

when only one is `None`.

---

## 4. Forgetting to Compare Both Subtrees

Checking only:

```python
p.left
q.left
```

is not enough.

The right subtree must also match.

---

# Pattern Recognition

When you see:

> Check whether two binary trees are identical.

Think:

```text
Compare two trees
      ↓
Compare corresponding nodes
      ↓
DFS / Recursion
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
Compare values
    ↓
Compare left
    ↓
Compare right
```

### Shortcut

```text
Same Tree
    ↓
p ↔ q
    ↓
value same
+
left same
+
right same
```

---

# Related Tree Problems

| Problem | Main Pattern |
|---|---|
| Same Tree | DFS + Compare Two Trees |
| Symmetric Tree | DFS + Mirror Comparison |
| Subtree of Another Tree | Same Tree + DFS |
| Invert Binary Tree | DFS + Swap Children |
| Maximum Depth | DFS + Height |
| Balanced Tree | Postorder DFS + Height |
| Diameter | Postorder DFS + Height |

---

# Revision Cheat Sheet

```text
Problem:
Check whether two binary trees are identical.

Two trees are same if:
1. Structure is same.
2. Corresponding values are same.

Pattern:
Binary Tree + DFS + Recursion

At every pair of nodes:

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
left subtrees same
AND
right subtrees same

Code idea:

if p is None and q is None:
    return True

if p and q:
    return (
        p.val == q.val
        and isSameTree(p.left, q.left)
        and isSameTree(p.right, q.right)
    )

return False

Time:
O(n)

Space:
O(h)

Balanced tree:
O(log n) recursion space

Skewed tree:
O(n) recursion space
```

# One-Line Pattern

```text
Same Tree → Compare corresponding nodes → values must match + left subtrees must match + right subtrees must match.
```
```