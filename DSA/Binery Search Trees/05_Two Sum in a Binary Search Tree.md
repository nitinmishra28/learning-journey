# Two Sum in a Binary Search Tree

## 1. Problem

Given the root of a **Binary Search Tree (BST)** and an integer `k`, determine whether there exist **two different nodes** in the BST whose values add up to `k`.

Return:

```text
True  → if a pair exists
False → otherwise
```

### Example

```text
        5
       / \
      3   6
     / \   \
    2   4   7
```

Given:

```text
k = 9
```

Possible pair:

```text
2 + 7 = 9
```

Therefore:

```text
True
```

---

# 2. Brute Force

A straightforward approach is:

1. Traverse the tree.
2. For every node, search for another node whose value is:
   ```text
   k - current value
   ```
3. If found, return `True`.

This can require searching the tree repeatedly.

### Complexity

In the worst case:

```text
Time  → O(n²)
Space → O(h)
```

where:

```text
n = number of nodes
h = height of tree
```

We can do better by using the BST property.

---

# 3. Pattern

This is a:

```text
BST
 ↓
Inorder Traversal
 ↓
Sorted Array
 ↓
Two Pointer
 ↓
Find Two Values With Sum = k
```

### One-Line Pattern

> **BST Two Sum = Inorder traversal gives sorted values, then use two pointers from both ends to find the target sum.**

---

# 4. Main Idea

The key property of a BST is:

```text
Inorder Traversal
        ↓
Sorted Order
```

For example:

```text
        5
       / \
      3   6
     / \   \
    2   4   7
```

Inorder:

```text
2, 3, 4, 5, 6, 7
```

Now the problem becomes a normal **Two Sum in a sorted array** problem.

Use two pointers:

```text
i = 0
j = n - 1
```

So:

```text
i → smallest value
j → largest value
```

---

# 5. Two Pointer Logic

Calculate:

```python
Sum = inorder[i] + inorder[j]
```

Three cases are possible.

### Case 1: Sum == k

We found the required pair.

```python
return True
```

---

### Case 2: Sum < k

We need a larger sum.

Since the array is sorted:

```text
Move i forward
```

```python
i += 1
```

This increases the smaller value.

---

### Case 3: Sum > k

We need a smaller sum.

So:

```text
Move j backward
```

```python
j -= 1
```

This decreases the larger value.

---

# 6. Why Does Two Pointer Work?

Suppose:

```text
inorder = [2, 3, 4, 5, 6, 7]
k = 9
```

Start:

```text
i = 0 → 2
j = 5 → 7
```

Sum:

```text
2 + 7 = 9
```

Found.

---

Suppose:

```text
k = 10
```

Start:

```text
2 + 7 = 9
```

Since:

```text
9 < 10
```

we need a larger value.

Move:

```text
i++
```

Now:

```text
3 + 7 = 10
```

Found.

---

Suppose:

```text
k = 15
```

Start:

```text
2 + 7 = 9
```

Need larger:

```text
i++
```

Then:

```text
3 + 7 = 10
4 + 7 = 11
5 + 7 = 12
6 + 7 = 13
```

Eventually:

```text
i >= j
```

and no pair exists.

---

# 7. Complete Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def inOrder(self, root, inorder):
        if root is None:
            return

        # Left
        self.inOrder(root.left, inorder)

        # Root
        inorder.append(root.val)

        # Right
        self.inOrder(root.right, inorder)

    def checkTwoSum(self, inorder, k):
        n = len(inorder)

        i = 0
        j = n - 1

        while i < j:

            Sum = inorder[i] + inorder[j]

            if Sum == k:
                return True

            elif Sum < k:
                i += 1

            else:
                j -= 1

        return False

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        inorder = []

        # Convert BST into sorted array
        self.inOrder(root, inorder)

        # Apply two pointer technique
        ans = self.checkTwoSum(inorder, k)

        return ans
```

---

# 8. Dry Run

Consider:

```text
        5
       / \
      3   6
     / \   \
    2   4   7
```

Target:

```text
k = 9
```

### Step 1: Inorder Traversal

```text
2 → 3 → 4 → 5 → 6 → 7
```

So:

```python
inorder = [2, 3, 4, 5, 6, 7]
```

---

### Step 2: Initialize Pointers

```text
i = 0
j = 5
```

Values:

```text
inorder[i] = 2
inorder[j] = 7
```

Sum:

```text
2 + 7 = 9
```

Since:

```text
Sum == k
```

return:

```text
True
```

---

# 9. Dry Run When Pair Is Not Found

Consider:

```text
inorder = [2, 3, 4, 5, 6, 7]
k = 20
```

Start:

```text
i = 0 → 2
j = 5 → 7
```

```text
2 + 7 = 9
```

Since:

```text
9 < 20
```

move:

```text
i++
```

Now:

```text
3 + 7 = 10
```

Continue:

```text
4 + 7 = 11
5 + 7 = 12
6 + 7 = 13
```

Eventually:

```text
i >= j
```

So:

```python
return False
```

---

# 10. Why Inorder Traversal?

This is the most important BST observation.

For a BST:

```text
Inorder Traversal
        ↓
Sorted Order
```

Example:

```text
        8
       / \
      3   10
     / \
    1   6
```

Inorder:

```text
1, 3, 6, 8, 10
```

Once we have this sorted sequence, we can apply the standard sorted-array two-pointer technique.

So the problem becomes:

```text
BST Two Sum
    ↓
Inorder
    ↓
Sorted Array
    ↓
Two Sum
    ↓
Two Pointers
```

---

# 11. Why `i < j`?

We need **two different nodes**.

Therefore we cannot allow:

```text
i == j
```

because that would use the same element twice.

So:

```python
while i < j:
```

ensures that:

```text
i and j always point to different positions
```

---

# 12. Why Move `i` When Sum Is Small?

Suppose:

```text
inorder = [2, 3, 4, 5, 6, 7]
```

and:

```text
2 + 7 = 9
```

but:

```text
k = 12
```

We need a bigger sum.

Since `j` is already at the largest value:

```text
7
```

moving `j` left would make the sum even smaller.

So we increase `i`:

```text
2 → 3 → 4 → ...
```

This increases the sum.

---

# 13. Why Move `j` When Sum Is Large?

Suppose:

```text
6 + 7 = 13
```

but:

```text
k = 10
```

We need a smaller sum.

Since `i` is already at a relatively large value, increasing it would make the sum even larger.

So move `j` backward:

```text
7 → 6 → 5 → ...
```

This decreases the sum.

---

# 14. Important BST Connection

This problem combines **two important patterns**:

### Pattern 1: BST Inorder

```text
BST
 ↓
Inorder
 ↓
Sorted array
```

### Pattern 2: Two Pointer

```text
Sorted array
 ↓
i = beginning
j = end
 ↓
sum < target → i++
sum > target → j--
sum == target → found
```

Combining them:

```text
BST
 ↓
Inorder
 ↓
Sorted
 ↓
Two Pointer
```

This is the main interview pattern.

---

# 15. Common Mistakes

### Mistake 1: Using preorder instead of inorder

Preorder does not guarantee sorted order.

Wrong:

```text
Preorder → Two Pointer
```

Correct:

```text
Inorder → Sorted → Two Pointer
```

---

### Mistake 2: Using `i <= j`

Wrong:

```python
while i <= j:
```

This could use the same node twice.

Correct:

```python
while i < j:
```

---

### Mistake 3: Moving the wrong pointer

Remember:

```text
sum < k
    ↓
Need larger
    ↓
i++

sum > k
    ↓
Need smaller
    ↓
j--
```

---

### Mistake 4: Searching the tree again for every node

That can lead to:

```text
O(n²)
```

Instead, convert the BST into sorted order once.

---

### Mistake 5: Forgetting the BST property

The reason this works efficiently is:

```text
BST → Inorder → Sorted
```

Without the BST property, inorder traversal does not necessarily produce sorted values.

---

# 16. Complexity

Let:

```text
n = number of nodes
```

### Inorder Traversal

Every node is visited once:

```text
O(n)
```

### Two Pointer

Each pointer moves only forward/backward through the array:

```text
O(n)
```

Therefore:

```text
Total Time = O(n)
```

### Space

The inorder list stores all nodes:

```text
O(n)
```

The recursion stack uses:

```text
O(h)
```

So overall:

```text
Space = O(n)
```

because the array dominates.

### Final Complexity

```text
Time  → O(n)
Space → O(n)
```

---

# 17. Can We Do Better in Space?

Yes.

Instead of storing the complete inorder array, we can use **BST iterators** to generate values from both ends:

```text
Left iterator  → smallest → larger
Right iterator → largest → smaller
```

Then perform the same two-pointer logic without storing the entire inorder array.

That can reduce auxiliary space to:

```text
O(h)
```

But the current solution is simpler and easier to understand.

---

# 18. Pattern Recognition

When you see:

```text
"Two Sum in BST"
"Find two nodes with sum K"
"BST + target sum"
```

Think immediately:

```text
BST
 ↓
Inorder
 ↓
Sorted
 ↓
Two Pointer
```

Then:

```text
i = 0
j = n - 1

while i < j:

    sum = arr[i] + arr[j]

    sum == k → True
    sum < k  → i++
    sum > k  → j--
```

---

# 19. Revision Cheat Sheet

```text
BST Two Sum
      ↓
Inorder Traversal
      ↓
Sorted Array
      ↓
Two Pointers
      ↓
i = 0
j = n - 1
      ↓
sum == k → True
sum < k  → i++
sum > k  → j--
      ↓
i >= j → False
```

### Core Code

```python
inorder = []

self.inOrder(root, inorder)

i = 0
j = len(inorder) - 1

while i < j:

    Sum = inorder[i] + inorder[j]

    if Sum == k:
        return True

    elif Sum < k:
        i += 1

    else:
        j -= 1

return False
```

### Complexity

```text
Time  → O(n)
Space → O(n)
```

---

# 20. Interview Memory Trick

> **"BST gives sorted order through inorder, then solve Two Sum using two pointers."**

### One-Line Pattern

> **BST Two Sum = Inorder → Sorted Array → Two Pointers → Find sum `k`.**