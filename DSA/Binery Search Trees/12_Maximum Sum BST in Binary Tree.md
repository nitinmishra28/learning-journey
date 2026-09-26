# Maximum Sum BST in Binary Tree

## 1. Problem

Given a Binary Tree, find the **maximum sum of all nodes among all subtrees that are valid Binary Search Trees (BSTs)**.

A subtree is a valid BST if:

```text
All values in left subtree < root
and
All values in right subtree > root
```

We need to find the BST subtree having the maximum sum.

---

# 2. Example

Consider:

```text
          1
         / \
        4   3
       / \   \
      2   4   5
```

Consider the subtree:

```text
        3
         \
          5
```

It is a valid BST:

```text
3 < 5
```

Its sum is:

```text
3 + 5 = 8
```

Another subtree may have a larger sum.

The goal is:

```text
Find every BST subtree
        ↓
Calculate its sum
        ↓
Return maximum sum
```

---

# 3. Brute Force

## Idea

For every node:

1. Consider that node as the root of a subtree.
2. Check whether its subtree is a valid BST.
3. If it is a BST, calculate its sum.
4. Keep the maximum sum.

The problem is that checking whether a subtree is a BST may require traversing the subtree again.

So the same nodes can be visited many times.

### Complexity

Worst case:

```text
Time = O(n²)
```

because we may repeatedly validate and calculate information for overlapping subtrees.

The optimized solution avoids this repeated work by calculating all required information during one postorder traversal.

---

# 4. Main Idea

For every subtree, we need to know four things:

```text
1. Minimum value
2. Maximum value
3. Sum of values
4. Whether the subtree is a BST
```

We create an `Info` class to store exactly these four pieces of information.

```python
class Info:
    def __init__(self, minVal, maxVal, sumVal, isBST):
        self.minVal = minVal
        self.maxVal = maxVal
        self.sumVal = sumVal
        self.isBST = isBST
```

So every recursive call returns:

```text
Info
```

about its subtree.

---

# 5. Why Do We Need These Four Values?

Suppose we are currently at:

```text
        root
       /    \
      L      R
```

To determine whether the current subtree is a BST, we need to know:

```text
Maximum value in left subtree
Minimum value in right subtree
```

Because BST requires:

```text
root.val > maximum value in left subtree

root.val < minimum value in right subtree
```

We also need:

```text
left subtree is BST
right subtree is BST
```

And if the current subtree is a BST, we need its total sum.

Therefore we store:

```text
minVal
maxVal
sumVal
isBST
```

---

# 6. Pattern

This is a classic:

```text
Postorder Traversal

Left → Right → Node
```

Why postorder?

Because before deciding whether the current node forms a BST, we need information from:

```text
Left subtree
Right subtree
```

So:

```text
Solve Left
     ↓
Solve Right
     ↓
Use both answers at Current Node
```

This is called **Bottom-Up Tree DP**.

---

# 7. Base Case

When:

```python
root is None
```

we return:

```python
Info(
    float('inf'),
    float('-inf'),
    0,
    True
)
```

Code:

```python
if root is None:
    return Info(float('inf'), float('-inf'), 0, True)
```

Why these values?

### Minimum

```text
minVal = +∞
```

because we don't want an empty subtree to incorrectly reduce the minimum.

### Maximum

```text
maxVal = -∞
```

because we don't want an empty subtree to incorrectly increase the maximum.

### Sum

```text
sumVal = 0
```

because an empty subtree contributes nothing.

### BST

```text
isBST = True
```

An empty tree is considered a valid BST.

---

# 8. Complete Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Info:

    def __init__(self, minVal, maxVal, sumVal, isBST):
        self.minVal = minVal
        self.maxVal = maxVal
        self.sumVal = sumVal
        self.isBST = isBST


class Solution:

    def solve(self, root):

        # Base case
        if root is None:
            return Info(
                float('inf'),
                float('-inf'),
                0,
                True
            )

        # L
        leftAns = self.solve(root.left)

        # R
        rightAns = self.solve(root.right)

        # N
        currentAns = Info(0, 0, 0, False)

        # Minimum value of current subtree
        currentAns.minVal = min(
            leftAns.minVal,
            rightAns.minVal,
            root.val
        )

        # Maximum value of current subtree
        currentAns.maxVal = max(
            leftAns.maxVal,
            rightAns.maxVal,
            root.val
        )

        # Sum of current subtree
        currentAns.sumVal = (
            leftAns.sumVal
            + rightAns.sumVal
            + root.val
        )

        # Check whether current subtree is a BST
        currentAns.isBST = (
            leftAns.isBST
            and rightAns.isBST
            and root.val > leftAns.maxVal
            and root.val < rightAns.minVal
        )

        # If current subtree is a BST,
        # update maximum sum
        if currentAns.isBST:
            self.maxSum = max(
                self.maxSum,
                currentAns.sumVal
            )

        return currentAns

    def maxSumBST(self, root):

        self.maxSum = 0

        self.solve(root)

        return self.maxSum
```

---

# 9. Understanding the BST Condition

The most important line is:

```python
currentAns.isBST = (
    leftAns.isBST
    and rightAns.isBST
    and root.val > leftAns.maxVal
    and root.val < rightAns.minVal
)
```

There are four conditions.

---

## Condition 1

```python
leftAns.isBST
```

The left subtree itself must be a BST.

---

## Condition 2

```python
rightAns.isBST
```

The right subtree itself must be a BST.

---

## Condition 3

```python
root.val > leftAns.maxVal
```

The root must be greater than **every value** in the left subtree.

We only need the maximum value from the left subtree.

Example:

```text
       10
      /
     5
    / \
   2   7
```

Maximum value in left subtree:

```text
7
```

Check:

```text
10 > 7
```

So the left side satisfies the BST condition.

---

## Condition 4

```python
root.val < rightAns.minVal
```

The root must be smaller than **every value** in the right subtree.

We only need the minimum value from the right subtree.

Example:

```text
       10
         \
          15
         /  \
        12   20
```

Minimum value in right subtree:

```text
12
```

Check:

```text
10 < 12
```

So the right side satisfies the BST condition.

---

# 10. Why Do We Need `isBST` From Children?

Consider:

```text
        10
       /
      5
     / \
    2   20
```

At node `5`:

```text
2 < 5
20 > 5
```

So this subtree is a valid BST.

But consider:

```text
        10
       /
      5
     / \
    2   20
```

From the perspective of root `10`, the value `20` is in the **left subtree**.

Therefore the entire tree is not a BST.

The condition:

```python
root.val > leftAns.maxVal
```

catches this:

```text
10 > 20
```

which is false.

So:

```text
current subtree is NOT BST
```

---

# 11. Why Do We Calculate `minVal` and `maxVal`?

Suppose:

```text
        10
       /  \
      5    15
     / \
    2   8
```

For the current root `10`:

```text
left maximum = 8
right minimum = 15
```

Therefore:

```text
10 > 8
10 < 15
```

So the current subtree is a BST.

We don't need to search the entire left and right subtree again.

The child recursion has already given us:

```text
leftAns.maxVal
rightAns.minVal
```

This is what makes the solution efficient.

---

# 12. Why Do We Calculate `sumVal`?

If the current subtree is a valid BST, we need its sum.

So:

```python
currentAns.sumVal = (
    leftAns.sumVal
    + rightAns.sumVal
    + root.val
)
```

Example:

```text
        10
       /  \
      5    15
```

Then:

```text
left sum  = 5
root      = 10
right sum = 15
```

Therefore:

```text
current sum = 5 + 10 + 15
            = 30
```

If this subtree is a valid BST:

```text
maxSum = max(maxSum, 30)
```

---

# 13. Why Is `maxSum` Updated Only When `isBST` Is True?

We only want the sum of **valid BST subtrees**.

Therefore:

```python
if currentAns.isBST:
    self.maxSum = max(
        self.maxSum,
        currentAns.sumVal
    )
```

If:

```text
currentAns.isBST = False
```

we cannot use its sum as a BST answer.

So we don't update `maxSum`.

---

# 14. Dry Run

Consider:

```text
          1
         / \
        4   3
       / \   \
      2   4   5
```

Let's process using postorder.

---

## Node 2

```text
left = None
right = None
```

So:

```text
min = 2
max = 2
sum = 2
isBST = True
```

---

## Node 4

Left subtree:

```text
2
```

Right subtree:

```text
None
```

Check:

```text
4 > 2
```

So:

```text
min = 2
max = 4
sum = 6
isBST = True
```

---

## Node 4 on the right

This node has no children:

```text
min = 4
max = 4
sum = 4
isBST = True
```

---

## Node 5

```text
min = 5
max = 5
sum = 5
isBST = True
```

---

## Node 3

Right subtree contains:

```text
5
```

Check:

```text
3 < 5
```

Therefore:

```text
min = 3
max = 5
sum = 8
isBST = True
```

So:

```text
3
 \
  5
```

is a valid BST with sum:

```text
8
```

---

## Root 1

Left subtree:

```text
        4
       / \
      2   4
```

has:

```text
max = 4
```

Current root:

```text
1
```

Check:

```text
1 > 4
```

False.

Therefore:

```text
root 1 subtree is NOT a BST
```

We don't use its sum for `maxSum`.

The maximum valid BST sum found was:

```text
8
```

---

# 15. The Information Flow

This problem is easier if you think about information flowing **upward**.

```text
          Root
         /    \
        /      \
     Left      Right
       ↓         ↓
     Info      Info
       \         /
        \       /
         Current
           ↓
          Info
```

Every child gives the parent:

```text
min
max
sum
isBST
```

The parent combines them.

---

# 16. Why This Is Postorder DP

The traversal is:

```text
Left
 ↓
Right
 ↓
Node
```

This is **postorder traversal**.

It is also a form of:

```text
Tree DP / Bottom-Up DP
```

because the current node's answer depends on answers calculated for its children.

The pattern is:

```text
Child Information
       ↓
Combine
       ↓
Current Node Information
       ↓
Return to Parent
```

---

# 17. Why `Info` Class Is Useful

Instead of returning four separate values:

```python
return minVal, maxVal, sumVal, isBST
```

we create:

```python
Info(...)
```

This groups all information about one subtree into a single object.

So:

```python
leftAns = self.solve(root.left)
```

gives us:

```text
leftAns.minVal
leftAns.maxVal
leftAns.sumVal
leftAns.isBST
```

Similarly:

```python
rightAns = self.solve(root.right)
```

gives all information about the right subtree.

This makes the recursive solution easier to organize.

---

# 18. Why `float('inf')` and `float('-inf')`?

For an empty subtree:

```python
Info(float('inf'), float('-inf'), 0, True)
```

We choose:

```text
min = +∞
max = -∞
```

because they work naturally with:

```python
min(...)
max(...)
```

Example for a leaf node `5`:

```text
left.min = +∞
right.min = +∞
root.val = 5
```

Then:

```python
min(+∞, +∞, 5)
```

gives:

```text
5
```

Similarly:

```python
max(-∞, -∞, 5)
```

gives:

```text
5
```

So the leaf correctly gets:

```text
min = 5
max = 5
```

---

# 19. Complexity

Every node is visited exactly once.

At every node we perform constant work:

```text
min()
max()
sum
BST checks
maxSum update
```

Therefore:

```text
Time = O(n)
```

The recursion stack depends on tree height:

```text
Space = O(h)
```

For a balanced tree:

```text
O(h) = O(log n)
```

For a skewed tree:

```text
O(h) = O(n)
```

There is no extra array or traversal required.

---

# 20. Common Mistakes

## 1. Checking only the root's immediate children

Wrong idea:

```text
root.left.val < root.val
root.right.val > root.val
```

This is not enough.

BST property must hold for the **entire subtree**.

That's why we use:

```python
root.val > leftAns.maxVal
```

and:

```python
root.val < rightAns.minVal
```

---

## 2. Forgetting child `isBST`

Even if the current root satisfies the value conditions, the subtree is not a BST if either child subtree is already invalid.

Therefore:

```python
leftAns.isBST and rightAns.isBST
```

is required.

---

## 3. Calculating the sum separately

Don't traverse the subtree again just to calculate its sum.

The child already gives:

```python
leftAns.sumVal
rightAns.sumVal
```

So:

```python
currentAns.sumVal = (
    leftAns.sumVal
    + rightAns.sumVal
    + root.val
)
```

---

## 4. Updating `maxSum` for invalid BSTs

Wrong:

```python
self.maxSum = max(
    self.maxSum,
    currentAns.sumVal
)
```

This would consider invalid subtrees.

Correct:

```python
if currentAns.isBST:
    self.maxSum = max(
        self.maxSum,
        currentAns.sumVal
    )
```

---

## 5. Using wrong values for the base case

The empty subtree should return:

```text
min = +∞
max = -∞
sum = 0
isBST = True
```

These values make the parent calculations work naturally.

---

# 21. Pattern Recognition

When you see:

```text
Binary Tree
+
Need information about subtree
+
Parent depends on child information
```

think:

```text
Postorder
Left → Right → Node
```

and ask:

> **What information does the parent need from each child?**

Here the answer is:

```text
min
max
sum
isBST
```

So:

```text
Postorder
   ↓
Return Info
   ↓
Combine Left + Right
   ↓
Check Current
   ↓
Update Answer
```

---

# 22. General Template for This Pattern

Many tree problems can follow this structure:

```python
def solve(root):

    if root is None:
        return base_information

    leftAns = solve(root.left)

    rightAns = solve(root.right)

    currentAns = combine(
        leftAns,
        rightAns,
        root
    )

    update_global_answer(currentAns)

    return currentAns
```

This is a very important **Tree DP** pattern.

---

# 23. Revision Cheat Sheet

```text
Maximum Sum BST

For every subtree store:

1. minVal
2. maxVal
3. sumVal
4. isBST
```

### Postorder

```text
L → R → N
```

### BST Condition

```text
left is BST
AND
right is BST
AND
root > left.max
AND
root < right.min
```

### Sum

```text
current.sum =
    left.sum
  + right.sum
  + root.val
```

### If Valid BST

```python
maxSum = max(maxSum, current.sum)
```

### Empty Tree

```text
min = +∞
max = -∞
sum = 0
isBST = True
```

### Complexity

```text
Time  = O(n)
Space = O(h)
```

> **One-Line Pattern: Maximum Sum BST = Postorder Tree DP + return `(min, max, sum, isBST)` from every subtree.**