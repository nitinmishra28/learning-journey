# Path Sum II

## Problem

Given the root of a binary tree and an integer `targetSum`, return **all root-to-leaf paths** where the sum of node values is equal to `targetSum`.

Each path should be returned as a list of node values.

### Example

```text
        5
       / \
      4   8
     /   / \
    11  13  4
   /  \      \
  7    2      1
```

For:

```text
targetSum = 22
```

Valid paths are:

```text
5 → 4 → 11 → 2
5 → 8 → 4 → 1
```

Answer:

```text
[
    [5, 4, 11, 2],
    [5, 8, 4, 1]
]
```

---

# Pattern

```text
Binary Tree + DFS + Backtracking + Running Sum
```

---

# Main Idea

We need to find **all** valid root-to-leaf paths.

During DFS, maintain:

```text
Sum
```

→ Current sum from root to the current node.

And:

```text
path
```

→ Current root-to-current-node path.

When we reach a leaf:

```text
If Sum == targetSum
    → store the current path
```

After returning from a node, we must remove that node from `path`.

This is called:

```text
Backtracking
```

---

# Why Do We Need `path`?

In the previous **Path Sum** problem, we only needed:

```text
True / False
```

So we only maintained the running sum.

Here we need to return:

```text
The actual paths
```

Therefore we need:

```python
path = []
```

Example:

```text
5 → 4 → 11 → 2
```

The `path` contains:

```python
[5, 4, 11, 2]
```

---

# Why Do We Need Backtracking?

This is the most important concept in this problem.

We use the same `path` list while exploring both left and right subtrees.

Example:

```text
        5
       / \
      4   8
```

When going left:

```text
path = [5, 4]
```

After finishing the left subtree, we must remove:

```text
4
```

so that when we go right:

```text
path = [5]
```

Then we can add:

```text
8
```

and get:

```text
[5, 8]
```

Without backtracking, the path would incorrectly contain nodes from the previous branch.

---

# Path Flow

For:

```text
        5
       / \
      4   8
```

The traversal looks like:

```text
Add 5
path = [5]

    Add 4
    path = [5, 4]

    Explore 4
    ...

    Remove 4
    path = [5]

    Add 8
    path = [5, 8]

    Explore 8
    ...

    Remove 8
    path = [5]
```

This:

```text
Add → Explore → Remove
```

is the basic backtracking pattern.

---

# Code

```python
class Solution:

    def solve(self, root, targetSum, Sum, path, ans):

        if root is None:
            return

        # Add current node to sum
        Sum = Sum + root.val

        # Add current node to path
        path.append(root.val)

        # Check only at leaf
        if root.left is None and root.right is None:

            if Sum == targetSum:
                # Store a copy of current path
                ans.append(path.copy())

            # Backtrack
            path.pop()
            return

        # Explore left subtree
        self.solve(root.left, targetSum, Sum, path, ans)

        # Explore right subtree
        self.solve(root.right, targetSum, Sum, path, ans)

        # Backtrack
        path.pop()

    def pathSum(
        self,
        root: Optional[TreeNode],
        targetSum: int
    ) -> List[List[int]]:

        Sum = 0
        path = []
        ans = []

        self.solve(root, targetSum, Sum, path, ans)

        return ans
```

---

# Why `path.copy()`?

This is extremely important.

We cannot do:

```python
ans.append(path)
```

because `path` is the **same list** that we continue modifying during backtracking.

Suppose:

```python
path = [5, 4, 11, 2]
```

We find a valid path.

If we do:

```python
ans.append(path)
```

we store a reference to the same list.

Later backtracking does:

```python
path.pop()
```

and changes the list.

Therefore the stored answer can also change.

Instead:

```python
ans.append(path.copy())
```

creates a separate copy.

So:

```text
Current path
     ↓
copy
     ↓
ans
```

The answer remains unchanged when backtracking modifies `path`.

---

# Why `Sum` Does Not Need Backtracking

Notice:

```python
Sum = Sum + root.val
```

but we never do:

```python
Sum -= root.val
```

Why?

Because `Sum` is an integer.

Each recursive call gets its own value.

Example:

```text
        5
       / \
      4   8
```

At node `5`:

```text
Sum = 5
```

Left call:

```text
Sum = 5 + 4
    = 9
```

Right call:

```text
Sum = 5 + 8
    = 13
```

The left call's `Sum = 9` does not modify the parent's `Sum = 5`.

So:

```text
Sum → No explicit backtracking required
path → Backtracking required
```

---

# Why Does `path` Need Backtracking But `Sum` Doesn't?

This is a very important interview concept.

### `Sum`

```python
Sum = Sum + root.val
```

Integers are immutable.

Each recursive call has its own value.

Therefore:

```text
No backtracking needed.
```

### `path`

```python
path.append(root.val)
```

Lists are mutable.

The same list is shared between recursive calls.

Therefore:

```text
Backtracking is required.
```

---

# Why Check Only at a Leaf?

The problem requires:

```text
Root → Leaf
```

path.

Suppose:

```text
        5
       /
      4
     /
    3
```

Target:

```text
9
```

At node `4`:

```text
5 + 4 = 9
```

But `4` is not a leaf.

So this is **not** a valid answer.

We only check:

```python
if root.left is None and root.right is None:
```

then:

```python
if Sum == targetSum:
```

---

# Dry Run

Consider:

```text
        5
       / \
      4   8
     /     \
    3       2
```

Target:

```text
12
```

Start:

```text
path = []
Sum = 0
```

### Node 5

```text
Sum = 5
path = [5]
```

Go left.

### Node 4

```text
Sum = 9
path = [5, 4]
```

Go left.

### Node 3

```text
Sum = 12
path = [5, 4, 3]
```

`3` is a leaf.

Check:

```text
12 == 12
```

Valid.

Store:

```python
ans.append([5, 4, 3])
```

Then backtrack:

```text
path = [5, 4]
```

Return to node `4`.

Backtrack again:

```text
path = [5]
```

Now explore right subtree.

### Node 8

```text
Sum = 13
path = [5, 8]
```

Continue...

The previous path:

```text
[5, 4, 3]
```

remains safely stored because we used:

```python
path.copy()
```

---

# Recursive Structure

At every node:

```text
1. Add node to path
2. Add node value to sum
3. If leaf:
      check sum
4. Explore left
5. Explore right
6. Remove node from path
```

In short:

```text
Add
 ↓
Explore
 ↓
Backtrack
```

---

# Why `path.pop()` Is After Both Recursive Calls

We do:

```python
self.solve(root.left, ...)
self.solve(root.right, ...)
path.pop()
```

because the current node must remain in the path while exploring **both** children.

Example:

```text
        5
       / \
      4   8
```

Before exploring children:

```text
path = [5]
```

Explore left:

```text
[5, 4]
```

After returning:

```text
[5, 4]
```

Then `4` must be removed by its own recursive call.

Now:

```text
[5]
```

Explore right:

```text
[5, 8]
```

Finally remove `5`.

```text
[]
```

---

# Important Backtracking Pattern

For tree path problems, remember:

```python
path.append(root.val)

# Explore

path.pop()
```

This means:

```text
Choose
Explore
Undo
```

or:

```text
Add
DFS
Backtrack
```

---

# Difference: Path Sum vs Path Sum II

### Path Sum

Question:

```text
Does at least one valid path exist?
```

Return:

```text
True / False
```

So:

```text
Running Sum
+
DFS
```

is enough.

### Path Sum II

Question:

```text
Return ALL valid paths.
```

So we need:

```text
Running Sum
+
DFS
+
Path
+
Backtracking
```

---

# Complexity

Let:

```text
n = number of nodes
```

Every node is visited during DFS:

```text
O(n)
```

But we also have to store the valid paths.

If there are many valid paths, the output itself can contain many elements.

Therefore the practical complexity includes the cost of producing the output.

For the traversal:

```text
Time → O(n)
```

plus the cost of copying/storing valid paths.

The recursion stack uses:

```text
Space → O(h)
```

where:

```text
h = height of tree
```

Additionally:

```text
path → O(h)
```

and:

```text
ans → Output space
```

---

# Common Mistakes

## 1. Using `ans.append(path)`

Wrong:

```python
ans.append(path)
```

Correct:

```python
ans.append(path.copy())
```

because `path` is modified during backtracking.

---

## 2. Forgetting `path.pop()`

Without:

```python
path.pop()
```

nodes from previous branches remain in the path.

---

## 3. Checking Sum at Every Node

Wrong:

```python
if Sum == targetSum:
    ans.append(...)
```

Correct:

```text
Check only when the node is a leaf.
```

---

## 4. Forgetting to Add Current Node

Before exploring children:

```python
Sum += root.val
path.append(root.val)
```

---

## 5. Not Exploring Both Subtrees

We need:

```python
self.solve(root.left, ...)
self.solve(root.right, ...)
```

because valid paths can exist on either side.

---

# Revision Cheat Sheet

```text
Path Sum II

Pattern:
Binary Tree + DFS + Backtracking + Running Sum

Goal:
Find ALL root → leaf paths
whose sum == targetSum.

--------------------------------------------------

Maintain:

Sum:
Current root → node sum.

path:
Current root → node path.

ans:
All valid paths.

--------------------------------------------------

At every node:

Sum += root.val
path.append(root.val)

--------------------------------------------------

At leaf:

if Sum == targetSum:
    ans.append(path.copy())

--------------------------------------------------

After exploring:

path.pop()

--------------------------------------------------

Why path.pop()?

Same path list is shared by
recursive calls.

We must remove the current node
when returning from the subtree.

--------------------------------------------------

Why path.copy()?

ans.append(path)

stores the same list reference.

Backtracking would modify it.

Therefore:

ans.append(path.copy())

stores an independent copy.

--------------------------------------------------

Why Sum doesn't need backtracking?

Sum is an integer.

Each recursive call gets
its own value.

path is a mutable list,
so path needs backtracking.

--------------------------------------------------

Important:

Only check targetSum at a LEAF.

Because the required path is:

Root → Leaf

--------------------------------------------------

Complexity:

Traversal:
O(n)

Recursion stack:
O(h)

Path:
O(h)

Answer:
Depends on number and size
of valid paths.

h = tree height
```

---

# One-Line Pattern

```text
DFS maintains the current path and running sum; when a leaf reaches the target sum, store a copy of the path, then backtrack by removing the current node.
```