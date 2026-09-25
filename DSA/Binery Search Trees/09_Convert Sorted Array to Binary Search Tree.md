# Convert Sorted Array to Binary Search Tree

## 1. Problem

Given a sorted array `nums`, convert it into a **height-balanced Binary Search Tree (BST)**.

A Binary Search Tree follows:

```text
Left subtree < Root < Right subtree
```

A height-balanced BST means:

> The heights of the left and right subtrees of every node differ by at most 1.

### Example

Input:

```text
nums = [-10, -3, 0, 5, 9]
```

One possible balanced BST:

```text
        0
       / \
     -3   9
     /   /
   -10   5
```

Its inorder traversal is:

```text
-10 → -3 → 0 → 5 → 9
```

which is the original sorted array.

---

# 2. Brute Force

One possible approach is to choose an element as the root and recursively build the tree without carefully choosing the middle element.

For example, if we always choose the first element:

```text
[-10, -3, 0, 5, 9]
   ↓
  -10
     \
     -3
       \
        0
         \
          5
           \
            9
```

This creates a highly skewed tree.

The problem is not necessarily the time complexity of creating nodes, but the resulting tree may not be **height-balanced**.

### Why is this not suitable?

The problem specifically asks for a:

```text
Height-Balanced BST
```

Therefore, we should choose the middle element as the root.

---

# 3. Main Idea

The array is already sorted:

```text
[-10, -3, 0, 5, 9]
```

To create a balanced BST:

```text
Choose middle element as root
        ↓
Left half → left subtree
Right half → right subtree
```

For:

```text
[-10, -3, 0, 5, 9]
```

middle element:

```text
0
```

So:

```text
        0
       / \
[-10,-3] [5,9]
```

Then recursively choose the middle of each half.

```text
        0
       / \
     -3   9
     /   /
   -10   5
```

---

# 4. Why Middle Element?

Suppose:

```text
nums = [1, 2, 3, 4, 5, 6, 7]
```

If we choose:

```text
1
```

as root:

```text
1
 \
  2
   \
    3
     \
      ...
```

The tree becomes skewed.

Instead, choose:

```text
4
```

as root:

```text
        4
       / \
    1,2,3  5,6,7
```

Both sides have almost the same number of elements.

Therefore:

```text
Middle element
      ↓
Balanced split
      ↓
Balanced BST
```

---

# 5. Divide and Conquer

The solution follows **Divide and Conquer**.

For every range:

```text
[s ... e]
```

we:

1. Find the middle index.
2. Create the middle element as the root.
3. Recursively build the left subtree.
4. Recursively build the right subtree.

The recursion looks like:

```text
solve(s, e)

       mid
      /   \
solve(s, mid-1)   solve(mid+1, e)
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

    def solve(self, nums, s, e):

        # No elements in this range
        if s > e:
            return None

        # Choose middle element
        mid = (s + e) // 2

        # Middle element becomes root
        element = nums[mid]
        root = TreeNode(element)

        # Build left subtree
        root.left = self.solve(nums, s, mid - 1)

        # Build right subtree
        root.right = self.solve(nums, mid + 1, e)

        return root

    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:

        s = 0
        e = len(nums) - 1

        root = self.solve(nums, s, e)

        return root
```

---

# 7. Understanding `s` and `e`

The variables:

```python
s
e
```

represent the current range of the array.

```text
s = start index
e = end index
```

Initially:

```python
s = 0
e = len(nums) - 1
```

For:

```text
nums = [-10, -3, 0, 5, 9]
```

we start with:

```text
s = 0
e = 4
```

Then:

```python
mid = (0 + 4) // 2
    = 2
```

So:

```text
nums[2] = 0
```

becomes the root.

---

# 8. Why `if s > e`?

This is the **base case**.

Suppose:

```text
s = 2
e = 1
```

There are no elements between these indices.

Therefore:

```python
if s > e:
    return None
```

This means:

```text
No element
   ↓
No node
   ↓
Return None
```

The parent can then correctly assign:

```python
root.left = None
```

or:

```python
root.right = None
```

---

# 9. Why Do We Create `TreeNode(element)`?

This line:

```python
root = TreeNode(element)
```

creates a **new tree node** using the middle array value.

For example:

```text
element = 0
```

Then:

```python
root = TreeNode(0)
```

creates:

```text
    0
   / \
 None None
```

Later we attach its subtrees:

```python
root.left = self.solve(...)
root.right = self.solve(...)
```

So eventually:

```text
        0
       / \
     -3   9
     /   /
   -10   5
```

The important distinction is:

```text
nums[mid]
```

is just an integer value.

While:

```python
TreeNode(nums[mid])
```

creates an actual tree node object that can have:

```text
val
left
right
```

---

# 10. Dry Run

Consider:

```text
nums = [-10, -3, 0, 5, 9]
```

### First Call

```text
s = 0
e = 4
mid = 2
```

Create:

```text
root = 0
```

Array:

```text
[-10, -3]  0  [5, 9]
```

---

### Build Left Subtree

Call:

```python
solve(nums, 0, 1)
```

```text
s = 0
e = 1
mid = 0
```

Create:

```text
root = -10
```

Remaining right side:

```text
[-3]
```

So:

```text
    -10
       \
       -3
```

---

### Build Right Subtree

Call:

```python
solve(nums, 3, 4)
```

```text
s = 3
e = 4
mid = 3
```

Create:

```text
root = 5
```

Then:

```text
    5
     \
      9
```

One valid balanced BST produced by this exact midpoint rule is therefore:

```text
        0
       / \
    -10   5
      \     \
      -3     9
```

Its inorder traversal is still:

```text
-10 → -3 → 0 → 5 → 9
```

The exact shape can vary depending on whether the lower or upper middle is selected when the range has an even number of elements.

---

# 11. Why Does This Produce a BST?

The input array is sorted.

When we select:

```text
nums[mid]
```

as the root:

```text
nums[s ... mid-1]
```

contains values smaller than the root.

And:

```text
nums[mid+1 ... e]
```

contains values greater than the root.

Therefore:

```text
             nums[mid]
             /       \
        smaller     greater
```

This property continues recursively.

So the resulting tree is a BST.

---

# 12. Why Is It Height-Balanced?

At every recursive call, we divide the array approximately in half:

```text
        middle
       /      \
    half      half
```

Therefore the left and right subtrees have almost the same number of nodes.

This keeps the height approximately:

```text
O(log n)
```

instead of:

```text
O(n)
```

for a completely skewed tree.

---

# 13. Recursion Tree

For:

```text
[1, 2, 3, 4, 5, 6, 7]
```

the recursive structure is approximately:

```text
              4
            /   \
           2     6
          / \   / \
         1   3 5   7
```

The recursive calls look like:

```text
solve(0, 6)
   |
   +--- solve(0, 2)
   |       |
   |       +--- solve(0, 0)
   |       +--- solve(2, 2)
   |
   +--- solve(4, 6)
           |
           +--- solve(4, 4)
           +--- solve(6, 6)
```

Each call works on roughly half of the previous range.

---

# 14. Complexity

Let `n` be the number of elements.

## Time Complexity

Every array element is used exactly once to create a tree node.

```text
Time = O(n)
```

There is no need to sort the array because the input is already sorted.

---

## Space Complexity

The recursion depth is equal to the height of the resulting tree.

Because the tree is balanced:

```text
h = O(log n)
```

Therefore:

```text
Auxiliary Space = O(log n)
```

The output tree itself contains `n` nodes:

```text
Output Space = O(n)
```

So:

```text
Time:
O(n)

Auxiliary Space:
O(log n)

Output Space:
O(n)
```

---

# 15. Common Mistakes

## 1. Choosing the first element every time

This can create:

```text
1
 \
  2
   \
    3
     \
      4
```

which is not balanced.

Use:

```python
mid = (s + e) // 2
```

---

## 2. Forgetting `s > e`

Without:

```python
if s > e:
    return None
```

the recursion will not know when to stop.

---

## 3. Using the wrong ranges

After choosing:

```text
mid
```

the left subtree must use:

```text
s ... mid - 1
```

and the right subtree must use:

```text
mid + 1 ... e
```

Correct:

```python
root.left = self.solve(nums, s, mid - 1)
root.right = self.solve(nums, mid + 1, e)
```

Do not include `mid` again because it is already used as the root.

---

## 4. Forgetting to return `root`

After building both subtrees:

```python
return root
```

is required so the parent can connect this subtree.

---

# 16. Important Interview Insight

This problem is a classic example of:

```text
Sorted Data
+
Choose Middle
+
Divide into Two Halves
```

Whenever you need to construct a balanced BST from sorted data, think:

```text
Middle element → Root
Left half      → Left subtree
Right half     → Right subtree
```

---

# 17. Pattern Recognition

When you see:

```text
Sorted Array
+
Balanced BST
```

immediately think:

```text
Find Middle
      ↓
Create Root
      ↓
Left Half → Left Subtree
      ↓
Right Half → Right Subtree
      ↓
Repeat
```

This is:

> **Divide and Conquer using the middle element.**

---

# 18. Revision Cheat Sheet

```text
Sorted Array → Balanced BST

1. Start with:
   s = 0
   e = n - 1

2. Base case:
   if s > e:
       return None

3. Find middle:
   mid = (s + e) // 2

4. Create node:
   root = TreeNode(nums[mid])

5. Build left:
   root.left = solve(s, mid - 1)

6. Build right:
   root.right = solve(mid + 1, e)

7. Return root
```

### Complexity

```text
Time:
O(n)

Auxiliary Space:
O(log n)

Output Space:
O(n)
```

### Core Pattern

```text
Sorted Array
     ↓
Middle Element
     ↓
    Root
   /    \
Left    Right
Half     Half
```

> **One-Line Pattern: Sorted Array to BST = Choose the middle element as root and recursively build the left and right halves.**