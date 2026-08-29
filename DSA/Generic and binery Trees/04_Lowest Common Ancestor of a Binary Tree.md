# Lowest Common Ancestor of a Binary Tree

## Problem

Given the root of a binary tree and two nodes `p` and `q`, find their **Lowest Common Ancestor (LCA)**.

The Lowest Common Ancestor is:

> The lowest node in the tree that has both `p` and `q` as descendants.

A node can also be a descendant of itself.

### Example

```text
        3
       / \
      5   1
     / \ / \
    6  2 0  8
      / \
     7   4
```

For:

```text
p = 5
q = 1
```

LCA:

```text
3
```

For:

```text
p = 5
q = 4
```

LCA:

```text
5
```

Because `5` itself is an ancestor of `4`.

---

# Pattern

```text
Binary Tree + DFS + Recursion
```

---

# Main Idea

At every node, recursively search:

```text
Left subtree
Right subtree
```

Each recursive call tells the parent:

```text
Did I find p?
Did I find q?
Did I find their LCA?
```

The most important case is:

```text
p found in left subtree
q found in right subtree
```

Then:

```text
Current node = LCA
```

---

# Base Cases

## 1. Root is None

```python
if root is None:
    return None
```

There is nothing to search.

---

## 2. Current Node is `p`

```python
if root.val == p.val:
    return p
```

We found `p`.

---

## 3. Current Node is `q`

```python
if root.val == q.val:
    return q
```

We found `q`.

This is important because the LCA can be `p` or `q` itself.

---

# Recursive Search

```python
leftAns = self.lowestCommonAncestor(root.left, p, q)
rightAns = self.lowestCommonAncestor(root.right, p, q)
```

Now:

```text
leftAns
```

contains information from the left subtree.

And:

```text
rightAns
```

contains information from the right subtree.

Each result can be:

```text
None → nothing found

p    → p found

q    → q found

Node → LCA already found in that subtree
```

---

# Four Important Cases

After searching both subtrees, there are four possibilities.

## Case 1: Both Are None

```python
if leftAns is None and rightAns is None:
    return None
```

Neither `p` nor `q` exists in this subtree.

So:

```text
Nothing found
```

---

## Case 2: Only Left Has an Answer

```python
elif leftAns is not None and rightAns is None:
    return leftAns
```

Something useful was found in the left subtree.

It could be:

```text
p
q
or the LCA
```

So simply pass it upward.

---

## Case 3: Only Right Has an Answer

```python
elif leftAns is None and rightAns is not None:
    return rightAns
```

Same idea.

Something useful was found in the right subtree.

Pass it upward.

---

## Case 4: Both Have an Answer

```python
else:
    return root
```

This is the **most important case**.

If:

```text
leftAns != None
rightAns != None
```

then one target was found on the left and the other on the right.

Therefore:

```text
current root = Lowest Common Ancestor
```

---

# Why Does `leftAns != None` and `rightAns != None` Mean LCA?

Consider:

```text
        3
       / \
      5   1
     / \
    6   2
```

Suppose:

```text
p = 6
q = 2
```

At node `5`:

```text
leftAns  = 6
rightAns = 2
```

Both sides returned something.

Therefore:

```text
5
├── 6
└── 2
```

Node `5` is their first common ancestor.

So:

```python
return root
```

returns:

```text
5
```

---

# Why Is It Called "Lowest" Common Ancestor?

Suppose:

```text
        3
       /
      5
     / \
    6   2
```

For:

```text
p = 6
q = 2
```

Both:

```text
3
5
```

are ancestors of `6` and `2`.

But:

```text
5
```

is closer to them.

Therefore:

```text
5 = Lowest Common Ancestor
```

DFS naturally finds this because the first node where the two searches meet is the lowest common ancestor.

---

# Code

```python
class Solution:

    def lowestCommonAncestor(
        self,
        root: 'TreeNode',
        p: 'TreeNode',
        q: 'TreeNode'
    ) -> 'TreeNode':

        # Base case
        if root is None:
            return None

        # Found p
        if root.val == p.val:
            return p

        # Found q
        if root.val == q.val:
            return q

        # Search left subtree
        leftAns = self.lowestCommonAncestor(root.left, p, q)

        # Search right subtree
        rightAns = self.lowestCommonAncestor(root.right, p, q)

        # Nothing found
        if leftAns is None and rightAns is None:
            return None

        # Answer found in left subtree
        elif leftAns is not None and rightAns is None:
            return leftAns

        # Answer found in right subtree
        elif leftAns is None and rightAns is not None:
            return rightAns

        # One node found on each side
        else:
            return root
```

---

# Dry Run

Consider:

```text
        3
       / \
      5   1
     / \
    6   2
```

Find LCA of:

```text
p = 6
q = 2
```

Start:

```text
root = 3
```

`3` is neither `6` nor `2`.

Search left:

```text
LCA(5, 6, 2)
```

Search right:

```text
LCA(1, 6, 2)
```

At node `1`:

```text
nothing found
```

So:

```text
rightAns = None
```

At node `5`:

Left subtree finds:

```text
6
```

Right subtree finds:

```text
2
```

Therefore:

```text
leftAns  = 6
rightAns = 2
```

Both are not `None`.

So:

```python
return root
```

returns:

```text
5
```

Then `5` is passed upward to node `3`.

Final answer:

```text
5
```

---

# Important Case: One Node Is Ancestor of the Other

Consider:

```text
        3
       /
      5
     /
    6
```

Find:

```text
p = 5
q = 6
```

When recursion reaches:

```text
5
```

we immediately get:

```python
if root.val == p.val:
    return p
```

So:

```text
5
```

is returned.

We don't need to continue searching below `5`.

Therefore:

```text
LCA = 5
```

This is why checking `p` and `q` before recursive calls is important.

---

# Important Understanding of the Return Value

This function does **not simply return `p` or `q`**.

The return value means:

```text
None
→ Neither target found

p
→ p found

q
→ q found

Some other node
→ LCA has already been found below
```

This information is passed from children to parents.

Think of it as:

```text
Child
  ↓
returns information
  ↓
Parent
  ↓
combines left + right information
  ↓
possibly becomes LCA
```

---

# Why Do We Return `leftAns` / `rightAns`?

Suppose:

```text
        3
       /
      5
     /
    6
```

Suppose we are looking for:

```text
p = 6
q = 8
```

The left subtree may find:

```text
6
```

but the right subtree finds nothing.

At node `5`:

```text
leftAns  = 6
rightAns = None
```

We return:

```python
return leftAns
```

So `6` can continue moving upward.

The parent can then use that information.

---

# Complexity

Every node is visited at most once.

Therefore:

```text
Time → O(n)
```

where `n` is the number of nodes.

Recursive calls use the call stack:

```text
Space → O(h)
```

where:

```text
h = height of tree
```

Balanced tree:

```text
O(log n)
```

Skewed tree:

```text
O(n)
```

---

# Common Mistakes

## 1. Checking Only One Side

You need to search both:

```python
leftAns = ...
rightAns = ...
```

because `p` and `q` may exist in different subtrees.

---

## 2. Forgetting the Ancestor Case

If:

```text
root == p
```

then `p` itself can be the LCA.

So return immediately.

---

## 3. Thinking LCA Must Be the Root

It can be any node.

Example:

```text
        3
       /
      5
     / \
    6   2
```

LCA of `6` and `2` is:

```text
5
```

not `3`.

---

## 4. Confusing LCA With Parent

LCA is the **lowest common ancestor**, not necessarily the direct parent.

---

# Revision Cheat Sheet

```text
Lowest Common Ancestor

Pattern:
Binary Tree + DFS + Recursion

Base Cases:

root == None
    → return None

root == p
    → return p

root == q
    → return q

--------------------------------------------------

Recursive:

leftAns = search(left)
rightAns = search(right)

--------------------------------------------------

Cases:

leftAns = None
rightAns = None
→ return None

leftAns != None
rightAns = None
→ return leftAns

leftAns = None
rightAns != None
→ return rightAns

leftAns != None
rightAns != None
→ current root is LCA

--------------------------------------------------

Most Important:

If one target is found in left subtree
and the other in right subtree:

        root
       /    \
      p      q

then:

root = LCA

--------------------------------------------------

Return value meaning:

None
→ nothing found

p / q
→ target found

other node
→ LCA already found

--------------------------------------------------

Complexity:

Time  → O(n)
Space → O(h)

h = tree height
```

---

# One-Line Pattern

```text
DFS searches both subtrees; if one target is found on each side, the current node is the LCA, otherwise pass the found result upward.
```