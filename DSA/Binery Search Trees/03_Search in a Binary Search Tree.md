# Search in a Binary Search Tree

## 1. Problem

Given the root of a **Binary Search Tree (BST)** and a value `val`, search for a node whose value is equal to `val`.

If the value exists:

```text
Return that node
```

If the value does not exist:

```text
Return None
```

### Example

```text
        8
       / \
      3   10
     / \    \
    1   6    14
       / \
      4   7
```

Search:

```text
6
```

Path:

```text
8
 ↓
3
 ↓
6
```

Found:

```text
6
```

---

# 2. Brute Force

If this were a normal binary tree, we would have to search both subtrees.

For example:

```python
def search(root, val):
    if root is None:
        return None

    if root.val == val:
        return root

    left = search(root.left, val)

    if left:
        return left

    return search(root.right, val)
```

This may visit every node.

### Complexity

```text
Time  → O(n)
Space → O(h)
```

But a BST gives us extra information that lets us eliminate half of the possible directions at every node.

---

# 3. Pattern

This is a:

```text
Binary Search Tree
        ↓
Compare target with current node
        ↓
Equal      → Found
Smaller    → Go Left
Greater    → Go Right
```

### One-Line Pattern

> **BST Search = Compare target with current node and move left if smaller, otherwise right, until found or `None`.**

---

# 4. Main Idea

The BST property is:

```text
Left subtree  → smaller values
Right subtree → greater values
```

So at every node:

### Case 1: Value found

```python
if root.val == val:
    return root
```

We are done.

---

### Case 2: Target is smaller

```python
if val < root.val:
    root = root.left
```

The target can only exist in the left subtree.

---

### Case 3: Target is greater

```python
else:
    root = root.right
```

The target can only exist in the right subtree.

---

# 5. Why Can We Ignore One Subtree?

Consider:

```text
        8
       / \
      3   10
```

Suppose we are searching for:

```text
3
```

Since:

```text
3 < 8
```

we know that `3` can only be in the left subtree.

There is no reason to search:

```text
10
```

because every value in the right subtree is greater than `8`.

This is the main advantage of a BST.

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
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:

        while root:

            # Target found
            if root.val == val:
                return root

            # Target is smaller → move left
            if val < root.val:
                root = root.left

            # Target is greater → move right
            else:
                root = root.right

        # Value does not exist
        return root
```

---

# 7. Dry Run — Value Found

Consider:

```text
        8
       / \
      3   10
     / \
    1   6
       / \
      4   7
```

Search:

```text
7
```

### Step 1

```text
root = 8
val = 7
```

Compare:

```text
7 < 8
```

Go left:

```text
root = 3
```

---

### Step 2

```text
root = 3
val = 7
```

Compare:

```text
7 > 3
```

Go right:

```text
root = 6
```

---

### Step 3

```text
root = 6
val = 7
```

Compare:

```text
7 > 6
```

Go right:

```text
root = 7
```

---

### Step 4

```text
root.val == val
```

Therefore:

```python
return root
```

The node containing `7` is returned.

---

# 8. Dry Run — Value Not Found

Search:

```text
5
```

Using:

```text
        8
       / \
      3   10
     / \
    1   6
       / \
      4   7
```

Start:

```text
8
```

Since:

```text
5 < 8
```

go left:

```text
3
```

Since:

```text
5 > 3
```

go right:

```text
6
```

Since:

```text
5 < 6
```

go left:

```text
4
```

Since:

```text
5 > 4
```

go right:

```text
None
```

Loop ends:

```python
while root:
```

and:

```text
root = None
```

Therefore:

```python
return root
```

returns:

```text
None
```

---

# 9. Why Use `while root`?

The search continues until one of two things happens:

```text
1. We find the value
       ↓
   return root

2. We reach None
       ↓
   value doesn't exist
```

So:

```python
while root:
```

means:

> Continue searching as long as there is a node to inspect.

---

# 10. Why Return `root` at the End?

At the end of the loop:

```python
root
```

will be:

```text
None
```

because we reached an empty position.

Therefore:

```python
return root
```

returns:

```text
None
```

when the value doesn't exist.

You could also write:

```python
return None
```

Both are equivalent here.

---

# 11. Why Iterative Approach?

The given solution uses:

```python
while root:
```

instead of recursion.

This means we only maintain one pointer:

```python
root
```

No recursive call stack is required.

### Space

```text
O(1)
```

This is an advantage over the recursive version.

---

# 12. Recursive Version

The same BST search can be written recursively:

```python
class Solution:
    def searchBST(self, root, val):

        if root is None:
            return None

        if root.val == val:
            return root

        if val < root.val:
            return self.searchBST(root.left, val)

        return self.searchBST(root.right, val)
```

The logic is exactly the same:

```text
Equal → return
Smaller → left
Greater → right
None → not found
```

---

# 13. Iterative vs Recursive

| Approach | Time | Space |
|---|---:|---:|
| Iterative | O(h) | O(1) |
| Recursive | O(h) | O(h) |

where `h` is the height of the BST.

For a balanced BST:

```text
h = O(log n)
```

For a skewed BST:

```text
h = O(n)
```

---

# 14. Complexity

Let:

```text
h = height of BST
```

We only follow one path from root to the target.

Therefore:

```text
Time = O(h)
```

### Balanced BST

```text
h = O(log n)

Time = O(log n)
```

### Skewed BST

```text
h = O(n)

Time = O(n)
```

Since the given solution is iterative:

```text
Space = O(1)
```

### Final Complexity

```text
Time  → O(h)
Space → O(1)
```

---

# 15. Common Mistakes

### Mistake 1: Searching both subtrees

Wrong approach for BST:

```python
search(root.left, val)
search(root.right, val)
```

We don't need both.

Use:

```text
val < root.val → left
val > root.val → right
```

---

### Mistake 2: Going in the wrong direction

Remember:

```text
Target smaller → LEFT
Target greater → RIGHT
```

---

### Mistake 3: Returning only the value

The problem asks for the **TreeNode**, not just the value.

Correct:

```python
return root
```

not:

```python
return root.val
```

---

### Mistake 4: Forgetting the `None` case

If the value doesn't exist, eventually:

```text
root = None
```

So the loop must stop safely.

---

### Mistake 5: Confusing BST Search with Binary Tree Search

Normal Binary Tree:

```text
May need to search both sides
```

BST:

```text
One direction is enough
```

This difference is extremely important.

---

# 16. Search vs Insert in BST

The decision logic is almost identical.

### Search

```text
Compare
   ↓
Smaller → Left
Greater → Right
Equal → Return node
None → Not found
```

### Insert

```text
Compare
   ↓
Smaller → Left
Greater/Equal → Right
None → Create node
```

So remember:

```text
BST Search and Insert
        ↓
Same direction logic
```

---

# 17. Pattern Recognition

When you see:

```text
"Search in BST"
"Find a value in BST"
"Find node with value X"
```

Immediately think:

```text
BST property
      ↓
Compare target with current node
      ↓
target == current → FOUND
target < current  → LEFT
target > current  → RIGHT
```

Never search both subtrees unless the problem has some special condition that breaks the normal BST ordering.

---

# 18. Revision Cheat Sheet

```text
BST Search
     ↓
Start at root
     ↓
root is None?
   /       \
 Yes       No
 ↓          ↓
Not Found  Compare
             ↓
       ┌─────┼─────┐
       ↓     ↓     ↓
    Smaller Equal Greater
       ↓      ↓      ↓
      Left   Found   Right
```

### Core Code

```python
while root:

    if root.val == val:
        return root

    if val < root.val:
        root = root.left
    else:
        root = root.right

return None
```

### Complexity

```text
Time  → O(h)
Space → O(1)
```

---

# 19. Interview Memory Trick

> **"Compare and choose one side: smaller → left, greater → right, equal → found."**

### One-Line Pattern

> **BST Search = Compare → Left/Right → Repeat until value is found or `None`.**