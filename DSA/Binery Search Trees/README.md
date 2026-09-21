# 🌳 Binary Search Tree (BST) in Python — Lecture 2

## 1. What is a Binary Search Tree?

A **Binary Search Tree (BST)** is a Binary Tree with a special ordering rule.

For every node:

```text
Left Subtree  → values smaller than node
Node          → current value
Right Subtree → values greater than node
```

Example:

```text
             8
           /   \
          3     10
         / \      \
        1   6      14
           / \    /
          4   7  13
```

For node `8`:

```text
Left Subtree  → 1, 3, 4, 6, 7
Right Subtree → 10, 13, 14
```

So:

```text
All values in Left  < Node
All values in Right > Node
```

---

# 2. BST vs Binary Tree

A **Binary Tree** only has the rule:

```text
Each node can have at most two children.
```

There is no ordering requirement.

A **BST** additionally follows:

```text
Left < Node < Right
```

### Quick Comparison

```text
Binary Tree
    ↓
At most 2 children
No ordering required


Binary Search Tree
    ↓
At most 2 children
AND
Left < Node < Right
```

---

# 3. BST Node in Python

We can represent a BST node using a class.

```python
class Tree:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
```

Each node contains:

```text
data   → value stored in the node
left   → reference to left child
right  → reference to right child
```

Initially:

```python
self.left = None
self.right = None
```

because the node does not have any children yet.

---

# 4. Creating a BST Manually

Example:

```text
             8
           /   \
          3     10
         / \      \
        1   6      14
           / \    /
          4   7  13
```

Python:

```python
root = Tree(8)

root.left = Tree(3)
root.right = Tree(10)

root.left.left = Tree(1)
root.left.right = Tree(6)

root.left.right.left = Tree(4)
root.left.right.right = Tree(7)

root.right.right = Tree(14)
root.right.right.left = Tree(13)
```

---

# 5. The Main Rule of BST

The most important rule to remember:

```text
             Node
            /    \
           /      \
     Smaller     Greater
```

For every node:

```text
Left Subtree  < Node
Right Subtree > Node
```

Example:

```text
             8
           /   \
          3     10
```

For `8`:

```text
3 < 8
10 > 8
```

For `3`:

```text
1 < 3
6 > 3
```

This rule is the foundation of almost every BST problem.

---

# 6. Searching in a BST

One of the biggest advantages of a BST is that we do **not** need to search every node.

Suppose we want to search for:

```text
7
```

Tree:

```text
             8
           /   \
          3     10
         / \
        1   6
           / \
          4   7
```

Start at `8`.

```text
7 < 8
```

So go left.

```text
             8
           /
          3
```

Now:

```text
7 > 3
```

So go right.

```text
             3
               \
                6
```

Now:

```text
7 > 6
```

Go right.

```text
             6
               \
                7
```

Found `7`.

### Important Pattern

```text
target < root.data
    ↓
go left

target > root.data
    ↓
go right

target == root.data
    ↓
found
```

---

# 7. Search Code — Recursive

```python
def search(root, target):

    if root is None:
        return False

    if root.data == target:
        return True

    if target < root.data:
        return search(root.left, target)

    return search(root.right, target)
```

Call:

```python
print(search(root, 7))
```

Output:

```text
True
```

If the value does not exist:

```python
print(search(root, 20))
```

Output:

```text
False
```

### Pattern to Remember

```text
Target == Node
      ↓
    Found

Target < Node
      ↓
    Go Left

Target > Node
      ↓
    Go Right
```

---

# 8. Search Code — Iterative

BST searching can also be done without recursion.

```python
def search(root, target):

    while root is not None:

        if root.data == target:
            return True

        if target < root.data:
            root = root.left

        else:
            root = root.right

    return False
```

The logic is the same:

```text
Smaller → Left
Greater → Right
Equal   → Found
```

---

# 9. Insertion in a BST

When inserting a new value, we follow the BST rule.

Suppose we want to insert:

```text
5
```

Tree:

```text
             8
           /   \
          3     10
         / \
        1   6
           / \
          4   7
```

Start at `8`:

```text
5 < 8
```

Go left.

At `3`:

```text
5 > 3
```

Go right.

At `6`:

```text
5 < 6
```

Go left.

At `4`:

```text
5 > 4
```

Go right.

The right side of `4` is empty.

So insert `5` there.

Result:

```text
             8
           /   \
          3     10
         / \
        1   6
           / \
          4   7
           \
            5
```

---

# 10. BST Insertion Code

```python
def insert(root, value):

    if root is None:
        return Tree(value)

    if value < root.data:
        root.left = insert(root.left, value)

    else:
        root.right = insert(root.right, value)

    return root
```

Call:

```python
root = insert(root, 5)
```

### Pattern to Remember

```text
value < root.data
        ↓
      Insert Left

value > root.data
        ↓
     Insert Right
```

At the end:

```python
return root
```

is important because we need to return the root of the subtree.

---

# 11. Why Do We Return `root`?

Consider:

```python
root.left = insert(root.left, value)
```

The recursive call may create a new node.

For example:

```text
root.left
   ↓
None
```

When we insert a value:

```python
return Tree(value)
```

creates the new node.

Then:

```python
root.left = insert(root.left, value)
```

connects that new node to the tree.

Therefore:

```python
return root
```

keeps the root connected while recursion comes back.

---

# 12. Inorder Traversal of BST

This is one of the **most important BST concepts**.

For a Binary Tree:

```text
Inorder = Left → Node → Right
```

For a BST:

```text
Inorder traversal gives values in sorted order.
```

Example:

```text
             8
           /   \
          3     10
         / \      \
        1   6      14
           / \    /
          4   7  13
```

Inorder:

```text
1 → 3 → 4 → 6 → 7 → 8 → 10 → 13 → 14
```

Notice:

```text
1 < 3 < 4 < 6 < 7 < 8 < 10 < 13 < 14
```

### Interview Rule

```text
BST + Inorder
      ↓
Sorted Order
```

This is extremely important for interviews.

---

# 13. Inorder Code

```python
def inorder(root):

    if root is None:
        return

    inorder(root.left)

    print(root.data)

    inorder(root.right)
```

Call:

```python
inorder(root)
```

Output:

```text
1
3
4
6
7
8
10
13
14
```

---

# 14. Finding Minimum Value in BST

In a BST:

```text
Smallest value
      ↓
Far left node
```

Example:

```text
             8
           /   \
          3     10
         /
        1
```

Minimum value:

```text
1
```

Why?

Because every time we move left:

```text
Current Node
     ↓
   Smaller
     ↓
    Left
```

### Code

```python
def findMin(root):

    if root is None:
        return None

    while root.left is not None:
        root = root.left

    return root
```

Call:

```python
minimum = findMin(root)

print(minimum.data)
```

---

# 15. Finding Maximum Value in BST

In a BST:

```text
Largest value
      ↓
Far right node
```

Example:

```text
             8
               \
                10
                  \
                   14
```

Maximum value:

```text
14
```

### Code

```python
def findMax(root):

    if root is None:
        return None

    while root.right is not None:
        root = root.right

    return root
```

Call:

```python
maximum = findMax(root)

print(maximum.data)
```

---

# 16. Minimum and Maximum Pattern

Very important:

```text
BST

Minimum
   ↓
Keep going LEFT

Maximum
   ↓
Keep going RIGHT
```

Remember:

```text
Minimum → Leftmost Node
Maximum → Rightmost Node
```

---

# 17. Deletion in a BST

Deletion is one of the most important BST interview topics.

When deleting a node, there are **three cases**.

```text
Case 1 → Node is a Leaf

Case 2 → Node has One Child

Case 3 → Node has Two Children
```

---

# 18. Case 1 — Delete Leaf Node

A leaf node has no children.

Example:

```text
       8
      / \
     3   10
    /
   1
```

Suppose we delete:

```text
1
```

Since `1` has no children, simply remove it.

Result:

```text
       8
      / \
     3   10
```

Pattern:

```text
Leaf
 ↓
Simply remove
```

---

# 19. Case 2 — Node Has One Child

Example:

```text
       8
      /
     3
      \
       6
```

Suppose we delete:

```text
3
```

Node `3` has one child:

```text
6
```

So `6` takes the place of `3`.

Result:

```text
       8
      /
     6
```

Pattern:

```text
Node with one child
        ↓
Child takes node's place
```

---

# 20. Case 3 — Node Has Two Children

This is the most important deletion case.

Example:

```text
             8
           /   \
          3     10
         / \
        1   6
           / \
          4   7
```

Suppose we delete:

```text
3
```

Node `3` has two children:

```text
Left  → 1
Right → 6
```

We cannot simply remove `3`.

We replace it with either:

```text
Inorder Successor
```

or:

```text
Inorder Predecessor
```

---

# 21. Inorder Successor

For a node:

```text
Inorder Successor
      ↓
Smallest value in Right Subtree
```

For node `3`:

```text
Right Subtree:

      6
     / \
    4   7
```

Smallest value:

```text
4
```

So:

```text
Inorder Successor of 3 = 4
```

Replace `3` with `4`.

---

# 22. Inorder Predecessor

For a node:

```text
Inorder Predecessor
      ↓
Largest value in Left Subtree
```

For node `3`:

```text
Left Subtree:

1
```

So:

```text
Inorder Predecessor of 3 = 1
```

Therefore, for deletion with two children, we can use:

```text
Inorder Successor
OR
Inorder Predecessor
```

---

# 23. BST Delete Code

Using **Inorder Successor**:

```python
def delete(root, key):

    if root is None:
        return None

    if key < root.data:
        root.left = delete(root.left, key)

    elif key > root.data:
        root.right = delete(root.right, key)

    else:

        # Case 1: No child
        if root.left is None and root.right is None:
            return None

        # Case 2: Only right child
        if root.left is None:
            return root.right

        # Case 2: Only left child
        if root.right is None:
            return root.left

        # Case 3: Two children
        successor = findMin(root.right)

        root.data = successor.data

        root.right = delete(root.right, successor.data)

    return root
```

---

# 24. Delete Logic to Remember

Do not try to memorize the entire deletion code.

Remember the decision structure:

```text
Search for the node
       ↓
   Found node?
       ↓
      Yes
       ↓
 ┌─────┼─────┐
 ↓     ↓     ↓
0     1      2
child child children
 ↓     ↓      ↓
None  Return  Use
      child   Successor/
              Predecessor
```

More simply:

```text
0 Children
    ↓
Delete

1 Child
    ↓
Child takes its place

2 Children
    ↓
Replace with Successor/Predecessor
    ↓
Delete duplicate node
```

---

# 25. BST Traversals

For the BST:

```text
             8
           /   \
          3     10
         / \      \
        1   6      14
           / \    /
          4   7  13
```

### Preorder — NLR

```text
8 → 3 → 1 → 6 → 4 → 7 → 10 → 14 → 13
```

### Inorder — LNR

```text
1 → 3 → 4 → 6 → 7 → 8 → 10 → 13 → 14
```

### Postorder — LRN

```text
1 → 4 → 7 → 6 → 3 → 13 → 14 → 10 → 8
```

### Level Order — BFS

```text
8
3 10
1 6 14
4 7 13
```

---

# 26. Important BST Property

The most important property:

```text
Inorder Traversal of BST
          ↓
    Sorted Order
```

Example:

```text
BST:

       5
      / \
     3   7
    / \   \
   1   4   9
```

Inorder:

```text
1 3 4 5 7 9
```

Therefore, if a problem asks something related to:

```text
Sorted order
Kth smallest
Kth largest
Minimum
Maximum
Range
```

think about:

```text
BST + Inorder
```

---

# 27. BST Validation

A common interview problem is:

```text
Check whether a Binary Tree is a valid BST.
```

Important:

We should **not** only compare a node with its immediate children.

Incorrect idea:

```text
        10
       /  \
      5    15
          /
         6
```

Here:

```text
6 < 15
```

so it looks valid locally.

But:

```text
6 < 10
```

and `6` is inside the right subtree of `10`.

Therefore, the tree is **not a valid BST**.

The correct rule is:

```text
Every node in left subtree < current node
Every node in right subtree > current node
```

---

# 28. BST Validation Using Range

We can keep a valid range for every node.

```python
def isValidBST(root, minimum=float("-inf"), maximum=float("inf")):

    if root is None:
        return True

    if root.data <= minimum or root.data >= maximum:
        return False

    left = isValidBST(root.left, minimum, root.data)

    right = isValidBST(root.right, root.data, maximum)

    return left and right
```

The important idea is:

```text
Left subtree
    ↓
(-∞, root.data)

Right subtree
    ↓
(root.data, +∞)
```

---

# 29. BST Height

The height of a BST depends on its shape.

### Balanced BST

```text
          8
        /   \
       4     12
      / \   / \
     2   6 10 14
```

Height is relatively small.

### Skewed BST

```text
1
 \
  2
   \
    3
     \
      4
       \
        5
```

This behaves almost like a linked list.

Therefore:

```text
BST performance depends on height.
```

---

# 30. BST Time Complexity

Let:

```text
h = height of BST
```

Search:

```text
O(h)
```

Insertion:

```text
O(h)
```

Deletion:

```text
O(h)
```

For a balanced BST:

```text
h ≈ log(n)
```

Therefore:

```text
Search    → O(log n)
Insertion → O(log n)
Deletion  → O(log n)
```

For a skewed BST:

```text
h ≈ n
```

Therefore:

```text
Search    → O(n)
Insertion → O(n)
Deletion  → O(n)
```

### Important Interview Point

```text
Balanced BST
     ↓
O(log n)

Skewed BST
     ↓
O(n)
```

---

# 31. BST Complexity Summary

| Operation | Average / Balanced | Worst Case |
| --------- | -----------------: | ---------: |
| Search    |         `O(log n)` |     `O(n)` |
| Insert    |         `O(log n)` |     `O(n)` |
| Delete    |         `O(log n)` |     `O(n)` |
| Find Min  |         `O(log n)` |     `O(n)` |
| Find Max  |         `O(log n)` |     `O(n)` |

The complexity depends on the height:

```text
O(h)
```

---

# 32. Important BST Patterns

When solving BST problems, remember these patterns.

### Pattern 1 — Search

```text
target < root
    ↓
go left

target > root
    ↓
go right
```

### Pattern 2 — Minimum

```text
Keep going left
```

### Pattern 3 — Maximum

```text
Keep going right
```

### Pattern 4 — Sorted Order

```text
BST + Inorder
     ↓
Sorted Order
```

### Pattern 5 — Delete

```text
0 children → remove

1 child → child replaces node

2 children → successor/predecessor
```

---

# 33. Complete BST Code

```python
class Tree:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Insert
def insert(root, value):

    if root is None:
        return Tree(value)

    if value < root.data:
        root.left = insert(root.left, value)

    else:
        root.right = insert(root.right, value)

    return root


# Search
def search(root, target):

    if root is None:
        return False

    if root.data == target:
        return True

    if target < root.data:
        return search(root.left, target)

    return search(root.right, target)


# Inorder
def inorder(root):

    if root is None:
        return

    inorder(root.left)

    print(root.data, end=' ')

    inorder(root.right)


# Find Minimum
def findMin(root):

    if root is None:
        return None

    while root.left is not None:
        root = root.left

    return root


# Find Maximum
def findMax(root):

    if root is None:
        return None

    while root.right is not None:
        root = root.right

    return root


# Delete
def delete(root, key):

    if root is None:
        return None

    if key < root.data:
        root.left = delete(root.left, key)

    elif key > root.data:
        root.right = delete(root.right, key)

    else:

        # No child
        if root.left is None and root.right is None:
            return None

        # Only right child
        if root.left is None:
            return root.right

        # Only left child
        if root.right is None:
            return root.left

        # Two children
        successor = findMin(root.right)

        root.data = successor.data

        root.right = delete(root.right, successor.data)

    return root


# Creating BST
root = None

root = insert(root, 8)
root = insert(root, 3)
root = insert(root, 10)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 14)
root = insert(root, 13)


# Search
print(search(root, 7))


# Inorder
inorder(root)
print()


# Minimum
minimum = findMin(root)
print("Minimum:", minimum.data)


# Maximum
maximum = findMax(root)
print("Maximum:", maximum.data)


# Delete
root = delete(root, 3)

inorder(root)
print()
```

---

# 34. BST vs Binary Tree — Interview Revision

```text
Binary Tree
    ↓
Maximum 2 children
No ordering rule


BST
    ↓
Maximum 2 children
Left < Node < Right
```

Most important BST property:

```text
Inorder → Sorted Order
```

---

# 35. Interview Questions

You should be able to answer:

### Q1. What is a BST?

```text
A Binary Tree where:

Left Subtree  < Node
Right Subtree > Node
```

---

### Q2. What is the main advantage of BST?

```text
It allows us to eliminate half of the search space
based on comparison when the tree is balanced.
```

---

### Q3. What is the time complexity of searching in a BST?

```text
Balanced → O(log n)
Worst     → O(n)
```

---

### Q4. How do you find the minimum element?

```text
Keep moving left.
```

---

### Q5. How do you find the maximum element?

```text
Keep moving right.
```

---

### Q6. What does inorder traversal give in a BST?

```text
Sorted order.
```

---

### Q7. What are the three cases of BST deletion?

```text
1. Leaf node
2. Node with one child
3. Node with two children
```

---

### Q8. How do you delete a node with two children?

```text
Replace it with:

Inorder Successor
OR
Inorder Predecessor
```

---

### Q9. What is the inorder successor?

```text
Smallest value in the right subtree.
```

---

### Q10. What is the inorder predecessor?

```text
Largest value in the left subtree.
```

---

### Q11. Can a BST become a linked list?

Yes.

Example:

```text
1
 \
  2
   \
    3
     \
      4
       \
        5
```

This is a skewed BST.

---

### Q12. What is the worst-case complexity of BST operations?

```text
O(n)
```

because the tree can become skewed.

---

# 🎯 BST Lecture Checklist

* [ ] Understand what a BST is
* [ ] Understand `Left < Node < Right`
* [ ] Understand Binary Tree vs BST
* [ ] Create a BST Node in Python
* [ ] Create a BST manually
* [ ] Understand BST search
* [ ] Write recursive search
* [ ] Write iterative search
* [ ] Understand BST insertion
* [ ] Write BST insertion
* [ ] Understand why `return root` is needed
* [ ] Understand inorder traversal in BST
* [ ] Remember `BST + Inorder = Sorted Order`
* [ ] Find minimum
* [ ] Find maximum
* [ ] Understand BST deletion
* [ ] Handle deletion with 0 children
* [ ] Handle deletion with 1 child
* [ ] Handle deletion with 2 children
* [ ] Understand inorder successor
* [ ] Understand inorder predecessor
* [ ] Understand BST validation
* [ ] Understand BST height
* [ ] Know balanced vs skewed BST
* [ ] Know BST time complexity
* [ ] Be able to write Search, Insert, Delete without looking at code
