# Recover Binary Search Tree

## 1. Problem

You are given a **Binary Search Tree (BST)** where exactly **two nodes have been swapped by mistake**.

Recover the tree without changing its structure.

You must:

- Find the two incorrect nodes.
- Swap their values.
- Modify the tree **in-place**.
- Do not create a new tree.

### Example

Original valid BST:

```text
        3
       / \
      1   4
         /
        2
```

Its inorder traversal is:

```text
1 → 2 → 3 → 4
```

Suppose `2` and `3` are swapped:

```text
        2
       / \
      1   4
         /
        3
```

Inorder becomes:

```text
1 → 3 → 2 → 4
```

This is not sorted, so the BST is invalid.

We need to restore it to:

```text
        3
       / \
      1   4
         /
        2
```

---

# 2. Important Observation

A valid BST has this property:

```text
BST
 ↓
Inorder Traversal
 ↓
Sorted Order
```

For example:

```text
        3
       / \
      1   4
         /
        2
```

Inorder:

```text
1 → 2 → 3 → 4
```

If two nodes are swapped, the inorder traversal will no longer be sorted.

Therefore:

> We can recover the BST by finding the two nodes that break the sorted inorder sequence.

---

# 3. Brute Force Approach

One approach is:

1. Perform inorder traversal.
2. Store all nodes in an array.
3. Find the two values that are out of order.
4. Swap their values.

For example:

```text
Inorder:

1 → 3 → 2 → 4
     ↑   ↑
   wrong order
```

We can detect:

```text
3 > 2
```

and identify:

```text
3 and 2
```

Then swap their values.

### Complexity

```text
Time  : O(n)
Space : O(n)
```

The time is already optimal, but the extra array requires `O(n)` space.

We can do better by using the inorder traversal directly.

---

# 4. Optimized Approach

Instead of storing the entire inorder traversal:

```text
1 → 3 → 2 → 4
```

we keep only the previous node:

```python
self.prev
```

During inorder traversal:

```text
Previous → Current
```

we check:

```python
curr.val < prev.val
```

If this happens, the inorder sequence is violating sorted order.

This means we have found one of the swapped nodes.

---

# 5. Core Idea

Maintain three important references:

```text
FV = First Violation
SV = Second Violation
prev = Previous node
```

Your code uses:

```python
self.FV
self.SV
self.prev
```

### Why?

During inorder traversal, a valid BST should produce:

```text
prev.val < curr.val
```

If we find:

```text
curr.val < prev.val
```

then we have found an inversion.

We save:

```text
FV = prev
SV = curr
```

---

# 6. Why Do We Need Two Violations?

There are two possible patterns depending on where the swapped nodes occur.

## Case 1: Swapped nodes are adjacent in inorder

Example:

```text
Correct:

1 → 2 → 3 → 4

Swapped:

1 → 3 → 2 → 4
```

Only one violation:

```text
3 > 2
```

So:

```text
FV = 3
SV = 2
```

---

## Case 2: Swapped nodes are not adjacent

Example:

```text
Correct:

1 → 2 → 3 → 4 → 5
```

Suppose `2` and `5` are swapped:

```text
1 → 5 → 3 → 4 → 2
```

Violations:

```text
5 > 3
4 > 2
```

First violation:

```text
FV = 5
SV = 3
```

Second violation:

```text
SV = 2
```

Notice:

```text
FV remains 5
SV gets updated to 2
```

This is exactly why your code has:

```python
if self.FV is None:
    self.FV = self.prev

self.SV = curr
```

---

# 7. Your Code

```python
class Solution:

    def __init__(self):
        self.FV = None
        self.SV = None
        self.prev = None

    def solve(self, curr):

        if curr is None:
            return

        # Inorder: Left → Node → Right
        self.solve(curr.left)

        # Check for inorder violation
        if self.prev and curr.val < self.prev.val:

            # First violation
            if self.FV is None:
                self.FV = self.prev

            # Second violation
            self.SV = curr

        # Move previous pointer forward
        self.prev = curr

        self.solve(curr.right)

    def recoverTree(self, root: TreeNode | None) -> None:

        if root is None:
            return

        self.solve(root)

        # Swap the values of the two incorrect nodes
        self.FV.val, self.SV.val = self.SV.val, self.FV.val
```

---

# 8. Understanding `prev`

This is one of the most important parts of the solution.

During inorder traversal:

```text
Left → Node → Right
```

we need to compare:

```text
previous node
        ↓
current node
```

So we maintain:

```python
self.prev
```

Initially:

```text
prev = None
```

After visiting the first node:

```python
self.prev = curr
```

Then when we visit the next node:

```python
if curr.val < self.prev.val:
```

we can compare them.

After the comparison:

```python
self.prev = curr
```

So `prev` always represents:

> The previously visited node in inorder traversal.

---

# 9. Why `prev` Is Shared State

This connects to the recursion question:

> "Should this value be shared by all recursive calls, or should each recursive call have its own version?"

Here:

```python
self.prev
```

**should be shared.**

Why?

Because `prev` represents the previous node in the **entire inorder traversal**.

We don't want every recursive call to have a separate `prev`.

We want:

```text
Node 1 → Node 2 → Node 3 → Node 4
            ↑
         same prev
```

For example:

```text
Visit 1:
prev = 1

Visit 2:
compare 2 with prev = 1
prev = 2

Visit 3:
compare 3 with prev = 2
prev = 3

Visit 4:
compare 4 with prev = 3
prev = 4
```

Therefore:

```python
self.prev
```

is shared across recursive calls.

---

# 10. Why `FV` and `SV` Are Also Shared

The same logic applies to:

```python
self.FV
self.SV
```

We want all recursive calls to contribute to the same answer.

Suppose the first violation is found in the left subtree:

```text
FV = 5
SV = 3
```

Then recursion moves into another subtree.

We don't want those values to disappear.

We want the later recursive calls to update:

```text
SV
```

if another violation is found.

Therefore:

```python
self.FV
self.SV
self.prev
```

are shared state.

---

# 11. Very Important Recursion Rule

Compare this problem with the previous BST validation problem.

### BST Validation

```python
validate(root, lb, ub)
```

The bounds are different for every recursive path.

Therefore:

```text
lb / ub
    ↓
Function parameters
```

---

### Recover BST

We want one common inorder traversal state:

```text
prev
FV
SV
```

Therefore:

```text
prev / FV / SV
        ↓
Shared state
```

### General Rule

Ask:

> Does each recursive branch need its own independent value?

If yes:

```text
Pass it as a parameter.
```

If all recursive calls must contribute to the same running state:

```text
Use shared state.
```

---

# 12. Finding the First Violation

Consider:

```text
Inorder:

1 → 5 → 3 → 4 → 2 → 6
```

Start:

```text
prev = 1
```

Compare:

```text
1 < 5
```

Valid.

Move:

```text
prev = 5
```

Next:

```text
5 > 3
```

Violation.

Therefore:

```text
FV = 5
SV = 3
```

The important part:

```python
if self.FV is None:
    self.FV = self.prev
```

Only the **first violation** sets `FV`.

---

# 13. Why `SV` Is Updated Every Time

Now continue:

```text
3 → 4
```

Valid.

Then:

```text
4 > 2
```

Another violation.

We already have:

```text
FV = 5
```

So we don't change it.

But:

```text
SV = 2
```

is updated.

Therefore:

```text
FV = 5
SV = 2
```

These are the actual swapped values.

---

# 14. Why Not Set `FV` Every Time?

Suppose we wrote:

```python
self.FV = self.prev
self.SV = curr
```

every time.

For:

```text
1 → 5 → 3 → 4 → 2 → 6
```

we would first get:

```text
FV = 5
SV = 3
```

Then later:

```text
FV = 4
SV = 2
```

Now `FV` is wrong.

Therefore:

```python
if self.FV is None:
    self.FV = self.prev
```

ensures that `FV` is captured only at the first violation.

---

# 15. Dry Run

Consider:

```text
        3
       / \
      1   4
         /
        2
```

Suppose `2` and `3` are swapped:

```text
        2
       / \
      1   4
         /
        3
```

Inorder:

```text
1 → 3 → 2 → 4
```

### Visit `1`

```text
prev = None
```

No comparison.

Set:

```text
prev = 1
```

---

### Visit `3`

Compare:

```text
3 > 1
```

No violation.

Set:

```text
prev = 3
```

---

### Visit `2`

Compare:

```text
2 < 3
```

Violation.

Set:

```text
FV = 3
SV = 2
```

Then:

```text
prev = 2
```

---

### Visit `4`

Compare:

```text
4 > 2
```

No violation.

Final:

```text
FV = 3
SV = 2
```

Swap:

```python
self.FV.val, self.SV.val = self.SV.val, self.FV.val
```

Result:

```text
        3
       / \
      1   4
         /
        2
```

BST recovered.

---

# 16. Another Dry Run — Two Violations

Consider the inorder sequence:

```text
1 → 5 → 3 → 4 → 2 → 6
```

### Compare `1` and `5`

```text
1 < 5
```

No violation.

```text
prev = 5
```

### Compare `5` and `3`

```text
5 > 3
```

First violation:

```text
FV = 5
SV = 3
```

### Compare `3` and `4`

```text
3 < 4
```

No violation.

### Compare `4` and `2`

```text
4 > 2
```

Second violation:

```text
FV = 5
SV = 2
```

### Compare `2` and `6`

```text
2 < 6
```

No violation.

Final:

```text
FV = 5
SV = 2
```

Swap:

```text
5 ↔ 2
```

Inorder becomes:

```text
1 → 2 → 3 → 4 → 5 → 6
```

Sorted again.

Therefore the BST is recovered.

---

# 17. Why Inorder Is the Key

This entire solution depends on one BST property:

```text
BST
 ↓
Inorder Traversal
 ↓
Sorted Sequence
```

For a valid BST:

```text
1 → 2 → 3 → 4 → 5
```

For an invalid BST after swapping two nodes:

```text
1 → 5 → 3 → 4 → 2
```

So instead of checking every parent-child relationship, we simply detect where the inorder sequence stops being sorted.

---

# 18. Why We Swap Values Instead of Nodes

The problem asks us to recover the tree **without changing its structure**.

We therefore do:

```python
self.FV.val, self.SV.val = self.SV.val, self.FV.val
```

We only change:

```text
node values
```

We do NOT change:

```text
left pointers
right pointers
```

So the tree structure remains exactly the same.

---

# 19. Why This Is Optimized

The brute force version stores the complete inorder traversal:

```text
Tree
 ↓
Inorder Array
 ↓
Find violations
```

Space:

```text
O(n)
```

Your solution does:

```text
Tree
 ↓
Inorder Traversal
 ↓
prev + FV + SV
 ↓
Swap
```

No inorder array is required.

Therefore:

```text
Time  : O(n)
Space : O(h)
```

where `h` is the tree height.

This is the optimized approach.

---

# 20. Complexity

Let:

```text
n = number of nodes
h = height of tree
```

### Time

Every node is visited exactly once:

```text
O(n)
```

The final swap is:

```text
O(1)
```

Therefore:

```text
Time = O(n)
```

### Space

The recursive call stack can contain at most one root-to-leaf path:

```text
O(h)
```

For a balanced tree:

```text
O(log n)
```

For a skewed tree:

```text
O(n)
```

No `O(n)` inorder array is created.

### Final Complexity

```text
Time  : O(n)
Space : O(h)
```

---

# 21. Common Mistakes

### Mistake 1: Storing the entire inorder traversal unnecessarily

You don't need:

```python
inorder = []
```

You only need:

```python
prev
```

---

### Mistake 2: Updating `FV` every time

Wrong:

```python
self.FV = self.prev
```

Correct:

```python
if self.FV is None:
    self.FV = self.prev
```

`FV` should represent the first violation.

---

### Mistake 3: Not updating `SV`

Every violation should update:

```python
self.SV = curr
```

Because in the non-adjacent case, the second violation gives us the actual second swapped node.

---

### Mistake 4: Updating `prev` before checking

Wrong:

```python
self.prev = curr

if curr.val < self.prev.val:
    ...
```

This compares the node with itself.

Correct order:

```python
if self.prev and curr.val < self.prev.val:
    ...

self.prev = curr
```

---

### Mistake 5: Changing tree structure

You don't need to move nodes.

Only swap:

```python
FV.val
SV.val
```

---

# 22. Recursion State Cheat Sheet

This problem is a good example of **shared state in recursion**.

```text
FV
 ↓
First violation found anywhere in traversal

SV
 ↓
Latest/second violation found

prev
 ↓
Previous node in inorder traversal
```

All recursive calls need access to the same three values.

Therefore:

```python
self.FV
self.SV
self.prev
```

are appropriate.

Compare with range validation:

```python
validate(root, lb, ub)
```

where each recursive call needs different:

```text
lb / ub
```

So they should be parameters.

### Rule to remember

```text
Different value for each recursive branch
        ↓
      Parameter

Same running state across all branches
        ↓
     Shared state
```

---

# 23. Pattern Recognition

When you see:

```text
BST
+
Exactly two nodes swapped
+
Recover in-place
```

Think:

```text
BST
 ↓
Inorder = Sorted
 ↓
Find inversions
 ↓
First violation → FV
Second/latest violation → SV
 ↓
Swap values
```

The core pattern is:

```text
Inorder Traversal
      ↓
Previous Node
      ↓
Detect curr.val < prev.val
      ↓
Find FV + SV
      ↓
Swap Values
```

---

# 24. Revision Cheat Sheet

```text
Problem:
Recover Binary Search Tree

Key BST Property:
Inorder traversal of a valid BST is sorted.

Goal:
Find the two swapped nodes.

State:
FV   = First Violation
SV   = Second Violation
prev = Previous inorder node

During inorder:

if curr.val < prev.val:
    if FV is None:
        FV = prev

    SV = curr

Then:

prev = curr

After traversal:

FV.val, SV.val = SV.val, FV.val

Why FV is set only once?
The first violation identifies the first swapped node.

Why SV is updated every violation?
For non-adjacent swapped nodes, the second violation
contains the actual second swapped node.

Why prev is shared?
It represents the previous node in the entire inorder traversal.

Why no array?
We only need the previous node, not the complete sorted sequence.

Time:
O(n)

Space:
O(h)

One-Line Pattern:
Recover BST = Inorder Traversal + Detect Inversions + Track First/Second Violations + Swap Values.
```