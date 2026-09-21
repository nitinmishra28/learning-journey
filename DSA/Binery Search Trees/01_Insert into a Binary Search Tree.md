# Insert into a Binary Search Tree

## 1. Problem

Given the root of a **Binary Search Tree (BST)** and an integer `val`, insert the value into the BST and return the root.

The BST property is:

```text
Left subtree  → values smaller than root
Right subtree → values greater than or equal to root
```

For every node:

```text
if val < root.val:
    go left
else:
    go right
```

### Example

Original BST:

```text
        4
       / \
      2   7
     / \
    1   3
```

Insert:

```text
5
```

Since:

```text
5 > 4 → go right
5 < 7 → go left
```

Result:

```text
        4
       / \
      2   7
     / \  /
    1   3 5
```

---

# 2. Brute Force

A simple approach is to first traverse the BST and find the correct empty position, then insert the new node.

For example, we could use:

```text
DFS / BFS
    ↓
Find a valid empty position
    ↓
Insert new node
```

However, this is unnecessary because the **BST property already tells us exactly which direction to go**.

We only need to follow:

```text
val < root.val → left
val >= root.val → right
```

The recursive solution uses this property directly.

### Complexity

If the tree height is `h`:

```text
Time  → O(h)
Space → O(h) because of recursion
```

Worst case for a skewed BST:

```text
h = n

Time  → O(n)
Space → O(n)
```

---

# 3. Pattern

This is a:

```text
Binary Search Tree
        ↓
Compare value with root
        ↓
Smaller → Left
Greater/Equal → Right
        ↓
Recursive insertion
```

### One-Line Pattern

> **BST Insertion = Compare with root, move left if smaller otherwise right, and insert at the first `None` position.**

---

# 4. Main Idea

At every node, compare:

```python
val
```

with:

```python
root.val
```

There are two cases.

### Case 1: `val < root.val`

The new value belongs somewhere in the left subtree.

```python
root.left = self.insertIntoBST(root.left, val)
```

---

### Case 2: `val >= root.val`

The new value belongs somewhere in the right subtree.

```python
root.right = self.insertIntoBST(root.right, val)
```

---

### Case 3: `root is None`

We found the correct empty position.

Create the new node:

```python
return TreeNode(val)
```

This is the actual insertion point.

---

# 5. Why Do We Assign the Recursive Result?

This line is extremely important:

```python
root.left = self.insertIntoBST(root.left, val)
```

Why not simply:

```python
self.insertIntoBST(root.left, val)
```

Because the recursive function returns the **possibly updated root of that subtree**.

Consider:

```text
        4
       /
      2
```

Insert:

```text
1
```

We call:

```python
insertIntoBST(2, 1)
```

Then:

```python
insertIntoBST(None, 1)
```

returns:

```python
TreeNode(1)
```

We need to connect this new node to `2`:

```python
root.left = TreeNode(1)
```

That's why we write:

```python
root.left = self.insertIntoBST(root.left, val)
```

Similarly for the right side:

```python
root.right = self.insertIntoBST(root.right, val)
```

---

# 6. Complete Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:

        # Found the correct empty position
        if root is None:
            return TreeNode(val)

        # Smaller values go to the left
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)

        # Greater/equal values go to the right
        else:
            root.right = self.insertIntoBST(root.right, val)

        # Return the current root
        return root
```

---

# 7. Dry Run

Consider:

```text
        4
       / \
      2   7
     / \
    1   3
```

Insert:

```text
5
```

### Step 1

Start:

```text
root = 4
val = 5
```

Compare:

```text
5 < 4 → False
```

So:

```python
root.right = self.insertIntoBST(root.right, 5)
```

Move to:

```text
7
```

---

### Step 2

```text
root = 7
val = 5
```

Compare:

```text
5 < 7 → True
```

So:

```python
root.left = self.insertIntoBST(root.left, 5)
```

Move to:

```text
None
```

---

### Step 3

Now:

```python
root is None
```

So:

```python
return TreeNode(5)
```

New node is created.

---

### Step 4

The returned node gets attached:

```text
7.left = 5
```

Tree becomes:

```text
        4
       / \
      2   7
     / \  /
    1   3 5
```

---

# 8. Understanding the Return

The final line:

```python
return root
```

is also important.

Why?

Because every recursive call must return the root of its subtree back to its parent.

For example:

```text
        4
         \
          7
         /
        5
```

When inserting `5`:

```text
insert(4)
    ↓
insert(7)
    ↓
insert(None)
    ↓
return Node(5)
```

Then:

```text
7.left = Node(5)
```

and:

```text
return 7
```

Then:

```text
4.right = 7
```

and finally:

```text
return 4
```

So the recursive returns rebuild the links while coming back up the call stack.

---

# 9. Recursion Flow

For:

```text
        4
       / \
      2   7
```

Insert `5`:

```text
insert(4, 5)
      |
      | 5 > 4
      ↓
insert(7, 5)
      |
      | 5 < 7
      ↓
insert(None, 5)
      |
      ↓
  create Node(5)
      |
      ↓
return Node(5)
      |
      ↓
7.left = Node(5)
      |
      ↓
return 7
      |
      ↓
4.right = 7
      |
      ↓
return 4
```

This is a very important BST recursion pattern.

---

# 10. Why Does It Work?

The BST property guarantees that we never need to search both subtrees.

At each node:

```text
val < root.val
        ↓
      LEFT

val >= root.val
        ↓
      RIGHT
```

Therefore, instead of searching the entire tree:

```text
O(n)
```

we only follow one path from root to the insertion position:

```text
O(h)
```

where `h` is the height of the BST.

---

# 11. Common Mistakes

### Mistake 1: Searching both subtrees

Wrong idea:

```python
insert(root.left, val)
insert(root.right, val)
```

A BST doesn't require this.

Use the comparison:

```python
if val < root.val:
    go left
else:
    go right
```

---

### Mistake 2: Forgetting to return the new node

Wrong:

```python
if root is None:
    TreeNode(val)
```

The created node is lost.

Correct:

```python
if root is None:
    return TreeNode(val)
```

---

### Mistake 3: Not assigning the recursive result

Wrong:

```python
self.insertIntoBST(root.left, val)
```

Correct:

```python
root.left = self.insertIntoBST(root.left, val)
```

Similarly:

```python
root.right = self.insertIntoBST(root.right, val)
```

---

### Mistake 4: Forgetting `return root`

After inserting into a subtree:

```python
return root
```

is needed so the parent keeps its correct subtree root.

---

### Mistake 5: Using the wrong comparison for duplicates

This implementation uses:

```python
if val < root.val:
    # left
else:
    # right
```

Therefore equal values go to the **right subtree**.

```text
val < root.val → left
val >= root.val → right
```

---

# 12. Complexity

Let:

```text
h = height of BST
```

We only follow one path from the root to the insertion position.

### Time

```text
O(h)
```

For a balanced BST:

```text
h = O(log n)

Time = O(log n)
```

For a skewed BST:

```text
h = O(n)

Time = O(n)
```

### Space

Because we use recursion:

```text
Space = O(h)
```

Balanced:

```text
O(log n)
```

Skewed:

```text
O(n)
```

### Final

```text
Time  → O(h)
Space → O(h)
```

---

# 13. Iterative Version

The same logic can be implemented without recursion.

```python
class Solution:
    def insertIntoBST(self, root, val):

        if root is None:
            return TreeNode(val)

        curr = root

        while True:

            if val < curr.val:

                if curr.left is None:
                    curr.left = TreeNode(val)
                    break

                curr = curr.left

            else:

                if curr.right is None:
                    curr.right = TreeNode(val)
                    break

                curr = curr.right

        return root
```

### Complexity

```text
Time  → O(h)
Space → O(1)
```

The iterative version avoids the recursive call stack.

---

# 14. Recursive vs Iterative

| Approach | Time | Extra Space |
|---|---:|---:|
| Recursive | O(h) | O(h) |
| Iterative | O(h) | O(1) |

Both follow the same BST property:

```text
smaller → left
greater/equal → right
```

The difference is only how we traverse the path.

---

# 15. Pattern Recognition

When you see:

```text
"Insert into BST"
"Search in BST"
"Find a value in BST"
"Delete from BST"
```

First remember the BST rule:

```text
             root
            /    \
       smaller   greater
```

For insertion:

```text
Compare
   ↓
Smaller → Left
Greater/Equal → Right
   ↓
Repeat
   ↓
None → Insert
```

---

# 16. Revision Cheat Sheet

```text
BST Insertion
      ↓
root is None?
      ↓
Yes → Create Node
      ↓
No
      ↓
val < root.val?
   /          \
 Yes          No
  ↓            ↓
Left          Right
  ↓            ↓
Recursive     Recursive
      ↓
Return root
```

### Core Code

```python
if root is None:
    return TreeNode(val)

if val < root.val:
    root.left = self.insertIntoBST(root.left, val)
else:
    root.right = self.insertIntoBST(root.right, val)

return root
```

### Complexity

```text
Time  → O(h)
Space → O(h)
```

---

# 17. Interview Memory Trick

Remember:

> **"BST insertion follows one path: smaller goes left, greater/equal goes right, and `None` is the insertion point."**

### One-Line Pattern

> **BST Insert = Compare → Go Left/Right → Recurse → Insert at `None` → Return root.**