# Dead End in a BST

## 1. Problem

Given a **Binary Search Tree (BST)**, determine whether the tree contains a **dead end**.

A dead end occurs when a **leaf node** cannot have any new value inserted around it while maintaining the BST property.

For a leaf node with value `x`:

```text
Possible values around x:

x - 1
x
x + 1
```

If both:

```text
x - 1
x + 1
```

already exist in the BST, then `x` is a **dead end**.

### Example

Consider:

```text
        8
       / \
      5   10
     / \
    2   7
```

For leaf `7`:

```text
6 does not exist
8 exists
```

So `7` is not a dead end.

If we have:

```text
        8
       /
      5
     / \
    4   6
```

For leaf `5`:

```text
4 exists
6 exists
```

So `5` is a dead end.

---

# 2. Brute Force Approach

For every leaf node:

1. Find its value `x`.
2. Check whether `x - 1` exists in the BST.
3. Check whether `x + 1` exists in the BST.
4. If both exist, return `True`.

Searching for each value directly in the BST can take:

```text
O(h)
```

where `h` is the height of the BST.

If we check many leaf nodes, the total can become:

```text
O(nh)
```

Worst case, when the BST is skewed:

```text
h = n
```

so:

```text
O(n²)
```

---

# 3. Optimized Approach

Instead of repeatedly searching the BST, store all node values in a hash map/set.

The solution has two steps:

```text
BST
 ↓
Store all values
 ↓
Visit only leaf nodes
 ↓
Check x-1 and x+1
 ↓
Dead End?
```

The code uses a dictionary:

```python
visited = {0: True}
```

and then stores every node:

```python
visited[root.data] = True
```

This allows average:

```text
O(1)
```

lookup.

---

# 4. Why Do We Add `0`?

The smallest valid BST value is usually considered:

```text
1
```

Suppose we have a leaf:

```text
1
```

For this node:

```text
x - 1 = 0
x + 1 = 2
```

`0` acts as a boundary value.

So:

```python
visited = {0: True}
```

means that for node `1`, the lower boundary is already considered occupied.

For example:

```text
    1
     \
      2
```

If `1` is a leaf in the relevant structure and `2` also exists, then:

```text
0 exists
2 exists
```

so the allowed range around `1` is closed.

---

# 5. Code

```python
class Solution:
    def populate(self, root, visited):
        if root is None:
            return

        # Store current node value
        visited[root.data] = True

        # Traverse left subtree
        self.populate(root.left, visited)

        # Traverse right subtree
        self.populate(root.right, visited)

    def check(self, root, visited):
        if root is None:
            return False

        # Check only leaf nodes
        if root.left is None and root.right is None:
            xp1 = root.data + 1

            xm1 = (
                root.data
                if root.data - 1 == 0
                else root.data - 1
            )

            # If both neighboring values exist,
            # this leaf is a dead end
            if xp1 in visited and xm1 in visited:
                return True

        # Check left and right subtrees
        return (
            self.check(root.left, visited)
            or self.check(root.right, visited)
        )

    def isDeadEnd(self, root):
        # 0 handles the boundary case for value 1
        visited = {0: True}

        # Store all node values
        self.populate(root, visited)

        # Check whether any leaf is a dead end
        return self.check(root, visited)
```

---

# 6. Understanding `populate()`

The purpose of:

```python
populate()
```

is simply to store every node value.

For:

```text
        8
       / \
      5   10
     / \
    2   7
```

the dictionary becomes conceptually:

```text
{
    0: True,
    2: True,
    5: True,
    7: True,
    8: True,
    10: True
}
```

Now checking whether a value exists is fast:

```python
x in visited
```

Average:

```text
O(1)
```

---

# 7. Understanding `check()`

The important part is:

```python
if root.left is None and root.right is None:
```

This identifies a **leaf node**.

Only leaves can be dead ends.

For a leaf:

```text
x
```

we calculate:

```python
x + 1
```

and:

```python
x - 1
```

Then:

```python
if xp1 in visited and xm1 in visited:
    return True
```

If both values already exist, there is no available integer value that can be inserted around this leaf.

---

# 8. Why Only Check Leaf Nodes?

Suppose:

```text
        8
       /
      5
     / \
    4   6
```

Node `5` has:

```text
left child = 4
right child = 6
```

Even though:

```text
4 and 6 exist
```

`5` is not a leaf.

The dead-end condition is specifically checked at a leaf because insertion would normally continue through the BST structure.

Therefore:

```text
Internal Node → Ignore
Leaf Node     → Check x-1 and x+1
```

---

# 9. Dry Run

Consider:

```text
        8
       /
      5
     / \
    4   6
```

### Step 1: Populate values

Initially:

```python
visited = {0: True}
```

After traversal:

```text
{0, 4, 5, 6, 8}
```

### Step 2: Check leaves

Leaf `4`:

```text
x - 1 = 3
x + 1 = 5
```

```text
3 → does not exist
5 → exists
```

Not a dead end.

---

Leaf `6`:

```text
x - 1 = 5
x + 1 = 7
```

```text
5 → exists
7 → does not exist
```

Not a dead end.

So:

```text
False
```

---

# 10. Dead End Example

Consider:

```text
        8
       /
      5
     / \
    4   6
```

Here, if the problem treats `5` as the candidate leaf, the values:

```text
4
5
6
```

are consecutive.

But since `5` has children in this particular tree, it is not checked by this implementation.

This highlights an important point:

> **The given implementation checks the dead-end condition only for leaf nodes.**

For an actual leaf example:

```text
        5
       /
      4
```

Leaf `4` has:

```text
3 → missing
5 → exists
```

so it is not a dead end.

A leaf `1` with `2` also present:

```text
    1
     \
      2
```

has:

```text
0 → considered present
2 → present
```

so it satisfies the boundary condition.

---

# 11. Important BST Insight

For a BST, insertion follows comparisons:

```text
value < root → go left
value > root → go right
```

A leaf becomes a dead end when there is no valid integer position available around it.

For a leaf `x`:

```text
x - 1   x   x + 1
```

If both neighboring values are already occupied, no new value can be inserted between the existing boundaries.

Therefore the check becomes:

```python
(x - 1 exists) AND (x + 1 exists)
```

---

# 12. Why Use a Hash Map?

Without storing values, we might repeatedly search the BST:

```text
Search(x - 1)
Search(x + 1)
```

for every leaf.

With the dictionary:

```python
visited
```

we can directly ask:

```python
x - 1 in visited
x + 1 in visited
```

Average lookup:

```text
O(1)
```

This avoids repeated BST searches.

---

# 13. Complexity

Let `n` be the number of nodes.

### `populate()`

Every node is visited once:

```text
O(n)
```

### `check()`

Every node is visited once:

```text
O(n)
```

Each hash lookup is average:

```text
O(1)
```

Therefore:

```text
Total Time = O(n)
```

### Space

The dictionary stores every node:

```text
O(n)
```

The recursion stack can take:

```text
O(h)
```

where `h` is the tree height.

Overall:

```text
Space = O(n)
```

because the dictionary dominates.

---

# 14. Complexity Comparison

| Approach | Time | Extra Space | Idea |
|---|---:|---:|---|
| Search BST for every leaf | O(nh) | O(h) | Repeated BST searches |
| Store all values + check leaves | O(n) | O(n) | Hash lookup |

Worst case for the brute-force approach:

```text
h = n
```

Therefore:

```text
O(nh) = O(n²)
```

The hash-based solution improves this to:

```text
O(n)
```

---

# 15. Common Mistakes

### Mistake 1: Checking every node

The condition is specifically about a leaf.

Always check:

```python
if root.left is None and root.right is None:
```

---

### Mistake 2: Forgetting the boundary value `0`

For a node with value `1`:

```text
1 - 1 = 0
```

The code handles this using:

```python
visited = {0: True}
```

---

### Mistake 3: Checking only `x - 1`

Both neighboring values are required:

```python
x - 1
x + 1
```

So the condition must be:

```python
if xp1 in visited and xm1 in visited:
```

not `or`.

---

### Mistake 4: Searching repeatedly

If there are many leaves, repeatedly searching the BST can become expensive.

Store all values once:

```python
visited = {}
```

and use hash lookup.

---

### Mistake 5: Forgetting to continue after a non-dead-end leaf

If the current leaf is not a dead end, we still need to check the other parts of the tree:

```python
return self.check(root.left, visited) or self.check(root.right, visited)
```

---

# 16. Recursion Pattern

This solution separates the work into two DFS traversals.

### First DFS

```text
populate()
```

Purpose:

```text
BST → collect all values
```

### Second DFS

```text
check()
```

Purpose:

```text
visit leaves → check dead-end condition
```

So the overall structure is:

```text
             BST
              |
       +------+------+
       |             |
   populate()      check()
       |             |
  Store values    Check leaves
       |             |
       +------→ Hash Lookup
```

This is a useful pattern:

> **First traversal prepares information; second traversal uses that information.**

---

# 17. Revision Cheat Sheet

```text
Dead End in BST
      ↓
Store every node value
      ↓
Visit every leaf
      ↓
For leaf x:
      ↓
Check x - 1
Check x + 1
      ↓
Both exist?
      ↓
Yes → Dead End
No  → Continue
```

### Important condition

```python
if xp1 in visited and xm1 in visited:
    return True
```

### Boundary

```python
visited = {0: True}
```

### Complexity

```text
Time  = O(n)
Space = O(n)
```

### Core Insight

> **A leaf is a dead end when both neighboring values `x-1` and `x+1` are already present; store all BST values in a hash map so these checks are O(1) on average.**

---

# One-Line Pattern

> **Dead End in BST = Store All Values + Check Every Leaf for Both `x-1` and `x+1`.**