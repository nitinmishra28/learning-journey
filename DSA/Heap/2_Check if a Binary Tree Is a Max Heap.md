# Check if a Binary Tree Is a Max Heap

## 1. Problem

Given the root of a binary tree, determine whether it is a **Max Heap**.

A binary tree is a Max Heap if it satisfies both conditions:

1. **Complete Binary Tree:** Every level except possibly the last is completely filled, and the last level is filled from left to right.
2. **Max Heap Property:** Every parent node has a value greater than or equal to its children.

Both conditions must be satisfied.

### Example 1: Max Heap

```text
        10
       /  \
      9    8
     / \  /
    7  6 5
```

- The tree is complete.
- Every parent is greater than or equal to its children.

Answer:

```text
True
```

### Example 2: Not a Max Heap

```text
        10
       /  \
      12   8
```

The tree is complete, but:

```text
10 < 12
```

The parent is smaller than its left child.

Answer:

```text
False
```

### Example 3: Not a Complete Binary Tree

```text
        10
       /  \
      9    8
       \
        7
```

The Max Heap property holds, but the tree is not complete because a right child exists without the corresponding left child.

Answer:

```text
False
```

---

# 2. Brute Force Approach

We can check the two conditions separately.

### Step 1: Check Completeness

Use level-order traversal (BFS).

- Add both children to the queue, including `None`.
- Once a `None` position is encountered, no real node should appear afterward.
- If a real node appears after `None`, the tree is not complete.

### Step 2: Check Max Heap Property

For every node:

```text
parent >= left child
parent >= right child
```

Then recursively check the left and right subtrees.

### Complexity

Both checks traverse the tree.

```text
Time:  O(n)
Space: O(n)
```

This is already an efficient approach for this problem.

---

# 3. Main Idea

The solution uses two independent checks:

```text
                 Binary Tree
                      |
              +-------+-------+
              |               |
       Completeness       Max Heap Property
              |               |
       Level Order BFS      DFS Recursion
              |               |
              +-------+-------+
                      |
              Both must be True
                      |
                  Is a Heap
```

The final condition is:

```python
completeness and checkHeap
```

If either condition is `False`, the tree is not a Max Heap.

---

# 4. Code

```python
from collections import deque

class Solution:
    def completeNess(self, root):
        q = deque([root])
        nullFound = False

        while q:
            front = q.popleft()

            if front is None:
                nullFound = True

            else:
                # A real node appears after a missing position
                if nullFound:
                    return False

                # Add both children, even if they are None
                q.append(front.left)
                q.append(front.right)

        return True

    def checkHeapMax(self, root):
        if root is None:
            return True

        # A leaf has no children, so it satisfies
        # the Max Heap property automatically
        if root.left is None and root.right is None:
            return True

        # Check left and right subtrees recursively
        leftAns = self.checkHeapMax(root.left)
        rightAns = self.checkHeapMax(root.right)

        # Check parent >= left child
        option1 = True
        if root.left and root.data < root.left.data:
            option1 = False

        # Check parent >= right child
        option2 = True
        if root.right and root.data < root.right.data:
            option2 = False

        # Current node must satisfy both comparisons
        currAns = option1 and option2

        # Current node and both subtrees must be valid
        if currAns and leftAns and rightAns:
            return True
        else:
            return False

    def isHeap(self, root):
        completeness = self.completeNess(root)
        checkHeap = self.checkHeapMax(root)

        if completeness and checkHeap:
            return True
        else:
            return False
```

---

# 5. Understanding `completeNess()`

This function checks whether the tree is complete.

```python
q = deque([root])
nullFound = False
```

We use a queue because level-order traversal processes nodes level by level.

The important logic is:

```python
if front is None:
    nullFound = True
```

Once a missing position appears, the flag becomes `True`.

Then:

```python
if nullFound:
    return False
```

If a real node appears after that missing position, the tree is incomplete.

### Why Add Both Children?

```python
q.append(front.left)
q.append(front.right)
```

We must add both children even if one is `None`.

Otherwise, we would miss gaps in the tree.

For example:

```text
        10
       /  \
      9    8
       \
        7
```

The left child of `9` is missing, but its right child exists.

Level-order traversal encounters the missing left-child position before node `7`.

Therefore, the completeness check returns `False`.

---

# 6. Understanding `checkHeapMax()`

This function checks the Max Heap property recursively.

The rule is:

```text
parent >= left child
parent >= right child
```

Let's understand each part.

## Case 1: Empty Node

```python
if root is None:
    return True
```

An empty subtree does not violate the Max Heap property.

Returning `True` allows recursion to work correctly.

## Case 2: Leaf Node

```python
if root.left is None and root.right is None:
    return True
```

A leaf has no children to compare with.

Therefore, it automatically satisfies the Max Heap property.

## Case 3: Check Subtrees

```python
leftAns = self.checkHeapMax(root.left)
rightAns = self.checkHeapMax(root.right)
```

Both subtrees must satisfy the Max Heap property.

## Case 4: Check Current Parent

```python
if root.left and root.data < root.left.data:
    option1 = False
```

If the parent is smaller than its left child, the property is violated.

Similarly:

```python
if root.right and root.data < root.right.data:
    option2 = False
```

If the parent is smaller than its right child, the property is violated.

Finally:

```python
currAns = option1 and option2
```

The current node is valid only if both child comparisons pass.

The final return condition combines all three results:

```python
currAns and leftAns and rightAns
```

This ensures that the current node and both subtrees are valid.

---

# 7. Dry Run: Valid Max Heap

Consider:

```text
        10
       /  \
      9    8
     / \
    7   6
```

### Step 1: Completeness Check

Level-order traversal:

```text
10 → 9 → 8 → 7 → 6 → None → None → ...
```

After the first `None`, only `None` entries remain.

Therefore:

```text
completeness = True
```

### Step 2: Max Heap Check

At node `7`:

```text
Leaf → True
```

At node `6`:

```text
Leaf → True
```

At node `9`:

```text
9 >= 7 → True
9 >= 6 → True
```

Both child subtrees are valid:

```text
checkHeapMax(9) = True
```

At node `8`:

```text
Leaf → True
```

At node `10`:

```text
10 >= 9 → True
10 >= 8 → True
```

Both subtrees are valid.

Therefore:

```text
checkHeap = True
```

Final result:

```python
True and True
```

Answer:

```text
True
```

---

# 8. Dry Run: Parent-Child Violation

Consider:

```text
        10
       /  \
      12   8
```

### Step 1: Completeness Check

The tree is complete.

```text
completeness = True
```

### Step 2: Max Heap Check

At node `12`:

```text
Leaf → True
```

At node `8`:

```text
Leaf → True
```

At node `10`:

```text
10 < 12
```

Therefore:

```text
option1 = False
option2 = True
```

So:

```text
currAns = False
```

Final result:

```text
checkHeap = False
```

The final check becomes:

```python
True and False
```

Answer:

```text
False
```

---

# 9. Why Are Both Conditions Necessary?

A tree can satisfy one condition but fail the other.

| Completeness | Max Heap Property | Is a Max Heap? |
|---|---|---|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

Remember:

```text
Max Heap = Complete Binary Tree + Max Heap Property
```

Checking only the parent-child values is not enough.

Checking only completeness is not enough either.

---

# 10. Complexity

Let `n` be the number of nodes and `h` be the height of the tree.

### Completeness Check

Each node is processed once, and each real node adds two child positions to the queue.

```text
Time:  O(n)
Space: O(n)
```

### Max Heap Check

Each node is visited once.

```text
Time:  O(n)
Space: O(h)
```

The recursive call stack depends on the tree height.

- Balanced tree: `O(log n)`
- Skewed tree: `O(n)`

### Overall Complexity

The checks run sequentially, not simultaneously.

```text
Time:  O(n) + O(n) = O(n)
Space: O(n)
```

The queue used for completeness checking dominates the auxiliary space.

---

# 11. Common Mistakes

### Mistake 1: Checking Only Parent-Child Values

A tree can satisfy:

```text
parent >= children
```

but still have missing positions that violate completeness.

Always check both conditions.

### Mistake 2: Checking Only the Root

Even if the root is greater than its children, a deeper node may violate the property.

For example:

```text
        20
       /  \
      15   10
     /
    18
```

The root satisfies the property, but:

```text
15 < 18
```

So it is not a Max Heap.

### Mistake 3: Ignoring `None` in Completeness Checking

Always append both children:

```python
q.append(front.left)
q.append(front.right)
```

This is necessary to detect gaps.

### Mistake 4: Using `or` Instead of `and`

The current node must satisfy both child comparisons:

```python
currAns = option1 and option2
```

Also, both subtrees must be valid:

```python
currAns and leftAns and rightAns
```

If any condition fails, the result must be `False`.

### Mistake 5: Rejecting Equal Values

Your code checks:

```python
root.data < root.left.data
```

and:

```python
root.data < root.right.data
```

This allows equal parent and child values, which is correct for a Max Heap.

The requirement is:

```text
parent >= child
```

not strictly greater than the child.

---

# 12. Revision Cheat Sheet

```text
Check Max Heap
      |
      +-----------------------+
      |                       |
      ↓                       ↓
Completeness Check       Max Heap Check
      |                       |
   BFS Queue              Recursive DFS
      |                       |
No real node after       Parent >= children
first None               Everywhere
      |                       |
      +-----------+-----------+
                  |
              Both True
                  |
             Valid Max Heap
```

### Completeness Rule

```text
First None encountered
        ↓
No real node may appear afterward
```

### Max Heap Rule

```text
parent >= left child
parent >= right child
```

### Complexity

```text
Time  = O(n)
Space = O(n)
```

---

# One-Line Pattern

> **Check Max Heap = Complete Binary Tree Check (BFS) + Parent ≥ Children Check (DFS).**