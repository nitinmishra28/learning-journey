# Minimum Value in a Binary Search Tree

## 1. Problem

Given the root of a **Binary Search Tree (BST)**, find the minimum value stored in the tree.

### BST Property

In a BST:

```text
        root
       /    \
   smaller  greater
```

All values in the left subtree are smaller than the root.

Therefore, the **minimum value is always present at the leftmost node**.

### Example

```text
        8
       / \
      3   10
     / \
    1   6
       / \
      4   7
```

The leftmost node is:

```text
1
```

Therefore:

```text
Minimum = 1
```

---

# 2. Brute Force

A brute force approach is to traverse the entire tree and keep track of the smallest value.

For example, using DFS:

```python
def findMin(root):
    if root is None:
        return -1

    minimum = root.data

    leftMin = findMin(root.left)
    rightMin = findMin(root.right)

    if leftMin != -1:
        minimum = min(minimum, leftMin)

    if rightMin != -1:
        minimum = min(minimum, rightMin)

    return minimum
```

This works for any binary tree, but it does not use the special property of a BST.

### Complexity

```text
Time  → O(n)
Space → O(h)
```

We visit every node even though the BST property allows us to ignore the right subtree.

---

# 3. Pattern

This is a:

```text
Binary Search Tree
        ↓
Minimum Value
        ↓
Go Left
        ↓
Keep going until left is None
```

### One-Line Pattern

> **BST Minimum = Keep moving left until there is no left child.**

---

# 4. Main Idea

The BST property tells us:

```text
Left subtree < Root < Right subtree
```

Therefore:

```text
Minimum
   ↓
Left subtree
   ↓
Left subtree
   ↓
Left subtree
   ↓
...
```

Eventually we reach a node where:

```python
root.left is None
```

That node is the leftmost node and therefore contains the minimum value.

---

# 5. Complete Code

```python
"""
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def minValue(self, root):

        # Empty tree
        if root is None:
            return -1

        # Keep moving to the leftmost node
        while root.left:
            root = root.left

        # Leftmost node contains the minimum value
        return root.data
```

---

# 6. Dry Run

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

Start:

```text
root = 8
```

Does `8` have a left child?

```text
Yes → 3
```

Move:

```python
root = root.left
```

Now:

```text
root = 3
```

Again:

```text
3.left = 1
```

Move:

```text
root = 1
```

Now:

```text
1.left = None
```

So the loop stops.

Return:

```python
return root.data
```

Therefore:

```text
Minimum = 1
```

---

# 7. Why Don't We Check the Right Subtree?

Consider:

```text
        8
       / \
      3   10
     / \
    1   6
```

Since this is a BST:

```text
10 > 8
3 < 8
```

The right subtree can never contain the minimum if a left subtree exists.

Similarly:

```text
6 > 3
```

So once we keep moving left, every node we encounter becomes a better candidate for the minimum.

We don't need to search:

```text
right subtree
```

at all.

This is the advantage of using the BST property.

---

# 8. Why Does the Loop Stop at the Answer?

The loop is:

```python
while root.left:
    root = root.left
```

It stops when:

```text
root.left == None
```

That means there is no smaller node on the left.

Because this is a BST, there cannot be any smaller value somewhere in the right subtree either.

Therefore:

```text
leftmost node = minimum node
```

---

# 9. Edge Cases

### Case 1: Empty Tree

```text
root = None
```

Code:

```python
if root is None:
    return -1
```

Result:

```text
-1
```

---

### Case 2: Only One Node

```text
    10
```

There is no left child.

So:

```python
while root.left:
```

does not execute.

Return:

```text
10
```

---

### Case 3: Completely Left-Skewed BST

```text
        5
       /
      4
     /
    3
   /
  2
 /
1
```

The loop simply follows:

```text
5 → 4 → 3 → 2 → 1
```

and returns:

```text
1
```

---

# 10. Recursive Version

The same idea can be written recursively:

```python
class Solution:
    def minValue(self, root):

        if root is None:
            return -1

        if root.left is None:
            return root.data

        return self.minValue(root.left)
```

The logic is exactly the same:

```text
Go left
   ↓
Go left
   ↓
Go left
   ↓
No left child
   ↓
Return value
```

### Complexity

```text
Time  → O(h)
Space → O(h)
```

The iterative version is preferable when we only need the minimum because it uses:

```text
O(1)
```

extra space.

---

# 11. Iterative vs Recursive

| Approach | Time | Extra Space |
|---|---:|---:|
| Iterative | O(h) | O(1) |
| Recursive | O(h) | O(h) |

For a balanced BST:

```text
h = O(log n)
```

For a skewed BST:

```text
h = O(n)
```

---

# 12. Complexity

Let `h` be the height of the BST.

We only follow the left path:

```text
root → left → left → left → ...
```

Therefore:

```text
Time = O(h)
```

For a balanced BST:

```text
O(log n)
```

For a skewed BST:

```text
O(n)
```

The iterative solution uses only one pointer:

```python
root
```

Therefore:

```text
Space = O(1)
```

### Final Complexity

```text
Time  → O(h)
Space → O(1)
```

---

# 13. Common Mistakes

### Mistake 1: Traversing the entire tree

You don't need:

```text
DFS/BFS on every node
```

The BST property already tells us where the minimum is.

Just:

```python
while root.left:
    root = root.left
```

---

### Mistake 2: Going right

For minimum:

```text
Go LEFT
```

For maximum:

```text
Go RIGHT
```

Remember:

```text
Minimum → leftmost
Maximum → rightmost
```

---

### Mistake 3: Returning the root value immediately

Wrong:

```python
return root.data
```

The root is not necessarily the minimum.

Example:

```text
        8
       /
      3
     /
    1
```

Minimum is `1`, not `8`.

---

### Mistake 4: Forgetting the empty tree case

Always handle:

```python
if root is None:
    return -1
```

for this implementation.

---

# 14. Related BST Pattern

Finding the maximum value is exactly the opposite:

```python
while root.right:
    root = root.right

return root.data
```

So remember:

```text
BST Minimum → Leftmost Node
BST Maximum → Rightmost Node
```

---

# 15. Pattern Recognition

When you see:

```text
"minimum value in BST"
"smallest element in BST"
"minimum node"
```

Think immediately:

```text
BST
 ↓
Minimum
 ↓
Keep going LEFT
 ↓
Left == None
 ↓
Answer
```

Similarly:

```text
BST
 ↓
Maximum
 ↓
Keep going RIGHT
 ↓
Right == None
 ↓
Answer
```

---

# 16. Revision Cheat Sheet

```text
BST Minimum
     ↓
Start at root
     ↓
Does left child exist?
     ↓
Yes → Move left
     ↓
Repeat
     ↓
Left child is None
     ↓
Return current node
```

### Core Code

```python
if root is None:
    return -1

while root.left:
    root = root.left

return root.data
```

### Complexity

```text
Time  → O(h)
Space → O(1)
```

---

# 17. Interview Memory Trick

> **"In a BST, the smallest value is always at the leftmost node."**

### One-Line Pattern

> **BST Minimum = Traverse to the leftmost node and return its value.**