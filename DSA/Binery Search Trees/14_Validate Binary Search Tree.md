# Validate Binary Search Tree

## 1. Problem

Given the root of a binary tree, determine whether the tree is a **valid Binary Search Tree (BST)**.

A valid BST follows:

```text
For every node:

all values in left subtree  <  node.val
all values in right subtree >  node.val
```

### Example

```text
        5
       / \
      3   7
     / \   \
    2   4   8
```

This is a valid BST.

But:

```text
        5
       / \
      3   7
         /
        4
```

This is NOT a valid BST.

Why?

`4 < 5`, but `4` is inside the **right subtree of 5**.

So checking only:

```python
root.left.val < root.val < root.right.val
```

is not enough.

---

# 2. Brute Force Approach

A simple approach is to validate every subtree separately.

For every node:

1. Find the maximum value in its left subtree.
2. Find the minimum value in its right subtree.
3. Check:

```text
left_max < root.val < right_min
```

4. Recursively validate left and right subtrees.

The problem is that we repeatedly traverse subtrees to find their minimum and maximum values.

### Complexity

```text
Time  : O(n²) in the worst case
Space : O(h)
```

This is inefficient because the same nodes may be visited multiple times.

---

# 3. Optimized Pattern

The better approach is:

> **Range Validation / Lower Bound + Upper Bound**

Instead of checking only the parent-child relationship, we give every node a valid range:

```text
(lower_bound, upper_bound)
```

For the root:

```text
(-∞, +∞)
```

If the current node is:

```text
root.val
```

then it must satisfy:

```text
lower_bound < root.val < upper_bound
```

Then we create new ranges for its children.

---

# 4. Main Idea

Suppose we have:

```text
        10
       /  \
      5    15
```

Initially:

```text
10 must be between -∞ and +∞
```

So:

```text
10 ∈ (-∞, +∞)
```

For the left child:

```text
5 must be less than 10
```

Therefore:

```text
5 ∈ (-∞, 10)
```

For the right child:

```text
15 must be greater than 10
```

Therefore:

```text
15 ∈ (10, +∞)
```

Now consider:

```text
        10
       /  \
      5    15
          /
         7
```

When we reach `7`:

Because `7` is in the **left subtree of 15**, it must be:

```text
7 ∈ (10, 15)
```

But:

```text
7 < 10
```

Therefore it is invalid.

This is exactly why we need **ranges** instead of checking only the parent.

---

# 5. Your Code

```python
class Solution:
    def validate(self, root, lb, ub):
        if root is None:
            return True
        
        # NLR
        # N
        currentNode = root.val > lb and root.val < ub

        # L
        left = self.validate(root.left, lb, root.val)

        # R
        right = self.validate(root.right, root.val, ub)

        return currentNode and left and right

    def isValidBST(self, root: TreeNode | None) -> bool:
        return self.validate(root, float('-inf'), float('inf'))
```

---

# 6. Understanding `lb` and `ub`

The two parameters mean:

```text
lb = lower bound
ub = upper bound
```

For example:

```python
self.validate(root, -inf, +inf)
```

means:

```text
root can contain anything between -∞ and +∞
```

After visiting a node:

```text
             root
            /    \
           L      R
```

The ranges become:

```text
Left subtree:

(lb, root.val)


Right subtree:

(root.val, ub)
```

That's why your code has:

```python
left = self.validate(root.left, lb, root.val)

right = self.validate(root.right, root.val, ub)
```

---

# 7. The Most Important Recursion Concept

A common question while solving recursive problems is:

> **"Should this value be shared by all recursive calls, or should each recursive call have its own version?"**

This is a very important question.

For this problem:

```python
lb
ub
```

should **NOT** be shared globally.

Each recursive call needs its **own bounds**.

For example:

```text
                10
              /    \
             5      15
            / \
           2   7
```

For `5`:

```text
lb = -∞
ub = 10
```

For `15`:

```text
lb = 10
ub = +∞
```

For `2`:

```text
lb = -∞
ub = 5
```

For `7`:

```text
lb = 5
ub = 10
```

Notice that every recursive call has different bounds.

---

# 8. Why Don't We Use `self.lb` and `self.ub`?

Suppose we tried:

```python
self.lb
self.ub
```

These would be shared instance variables.

But each subtree needs different bounds.

We want:

```text
                 10
               /    \
              5      15
             / \
            2   7

5  → (-∞, 10)
15 → (10, +∞)
2  → (-∞, 5)
7  → (5, 10)
```

If we stored the bounds in shared variables, one recursive call could overwrite the bounds needed by another call.

Instead, we pass them as function parameters:

```python
self.validate(root.left, lb, root.val)
```

and:

```python
self.validate(root.right, root.val, ub)
```

Each function call receives its own `lb` and `ub`.

---

# 9. Very Important Rule for Recursion

When deciding whether a variable should be a parameter or shared state, ask:

> **Does each recursive branch need a different value?**

If **YES**:

```text
Pass it as a parameter.
```

If **NO**, and all recursive calls need the same evolving value:

```text
Shared state may be useful.
```

### Example

In this problem:

```text
lb / ub
```

are different for every subtree.

Therefore:

```python
validate(root, lb, ub)
```

is correct.

---

# 10. What Happens to Function Parameters During Recursion?

Consider:

```python
self.validate(root.left, lb, root.val)
```

Suppose the current node is `10`:

```text
Current call:

validate(10, -∞, +∞)
```

For the left child `5`:

```text
validate(5, -∞, 10)
```

For its left child `2`:

```text
validate(2, -∞, 5)
```

The calls have their own local parameter values:

```text
Call 1:
lb = -∞
ub = +∞

Call 2:
lb = -∞
ub = 10

Call 3:
lb = -∞
ub = 5
```

They are not all using one shared `lb`/`ub`.

Conceptually:

```text
Call Stack

validate(10, -∞, +∞)
        |
        └── validate(5, -∞, 10)
                    |
                    └── validate(2, -∞, 5)
```

Each function call has its own local variables.

---

# 11. Why `currentNode` Alone Is Not Enough

You might initially think:

```python
currentNode = root.val > lb and root.val < ub
```

Why not simply do:

```python
root.left.val < root.val
root.right.val > root.val
```

Because BST rules apply to the **entire subtree**, not only immediate children.

Consider:

```text
        10
       /  \
      5    15
          /
         7
```

At node `15`:

```text
7 < 15
```

So the parent-child relationship looks valid.

But `7` is in the right subtree of `10`.

Therefore:

```text
7 must be > 10
```

It isn't.

The range catches this:

```text
7 must be in (10, 15)
```

But:

```text
7 > 10
```

is false.

Therefore the tree is invalid.

---

# 12. Why `float('-inf')` and `float('inf')`?

At the root, there is initially no restriction.

So we use:

```python
float('-inf')
```

and:

```python
float('inf')
```

Therefore:

```python
self.validate(root, float('-inf'), float('inf'))
```

means:

```text
Root can be any valid integer value.
```

Then every node gradually gets a smaller valid range.

---

# 13. Why Strict `<` and `>`?

Your code uses:

```python
root.val > lb and root.val < ub
```

This means duplicate values are not allowed.

For example:

```text
        10
       /  \
      5    10
```

The right `10` must satisfy:

```text
10 > 10
```

which is false.

Therefore the tree is invalid.

This matches the standard BST definition used by this problem.

---

# 14. Dry Run

Consider:

```text
        10
       /  \
      5    15
     / \
    2   7
```

### Step 1

```text
validate(10, -∞, +∞)
```

Check:

```text
-∞ < 10 < +∞
```

Valid.

---

### Step 2 — Left

```text
validate(5, -∞, 10)
```

Check:

```text
-∞ < 5 < 10
```

Valid.

---

### Step 3 — Left of 5

```text
validate(2, -∞, 5)
```

Check:

```text
-∞ < 2 < 5
```

Valid.

---

### Step 4 — Right of 5

```text
validate(7, 5, 10)
```

Check:

```text
5 < 7 < 10
```

Valid.

---

### Step 5 — Right of 10

```text
validate(15, 10, +∞)
```

Check:

```text
10 < 15 < +∞
```

Valid.

Therefore:

```text
True
```

---

# 15. Complete Commented Code

```python
class Solution:

    def validate(self, root, lb, ub):

        # Empty subtree is valid
        if root is None:
            return True

        # Current node must lie inside its valid range
        currentNode = root.val > lb and root.val < ub

        # Left subtree:
        # values must be smaller than current node
        left = self.validate(
            root.left,
            lb,
            root.val
        )

        # Right subtree:
        # values must be greater than current node
        right = self.validate(
            root.right,
            root.val,
            ub
        )

        # Current node + left subtree + right subtree
        # must all be valid
        return currentNode and left and right

    def isValidBST(self, root):
        return self.validate(
            root,
            float('-inf'),
            float('inf')
        )
```

---

# 16. Why This Works

For every node, we maintain the only range in which that node is allowed to exist.

Initially:

```text
Root:
(-∞, +∞)
```

If the current node is `10`:

```text
Left subtree:
(-∞, 10)

Right subtree:
(10, +∞)
```

Then those restrictions continue down the tree.

For example:

```text
10
 \
  15
 /
12
```

For `12`:

```text
10 < 12 < 15
```

valid.

But:

```text
10
 \
  15
 /
7
```

For `7`:

```text
10 < 7 < 15
```

false.

So the tree is invalid.

The range carries the BST restrictions from all ancestors.

---

# 17. Complexity

Let `n` be the number of nodes and `h` be the height of the tree.

### Time

Every node is visited once:

```text
O(n)
```

### Space

The recursion stack contains at most one path from root to leaf:

```text
O(h)
```

For a balanced BST:

```text
O(log n)
```

For a skewed tree:

```text
O(n)
```

### Final Complexity

```text
Time  : O(n)
Space : O(h)
```

---

# 18. Common Mistakes

### Mistake 1: Checking only immediate children

Wrong idea:

```python
root.left.val < root.val < root.right.val
```

This does not validate the entire subtree.

---

### Mistake 2: Using one global lower/upper bound

Wrong:

```python
self.lb
self.ub
```

The bounds change depending on the recursive path.

Use:

```python
validate(root, lb, ub)
```

---

### Mistake 3: Forgetting to update bounds

Wrong:

```python
self.validate(root.left, lb, ub)
self.validate(root.right, lb, ub)
```

The children need new restrictions.

Correct:

```python
self.validate(root.left, lb, root.val)
self.validate(root.right, root.val, ub)
```

---

### Mistake 4: Using `>=` / `<=`

If duplicates are not allowed:

```python
root.val > lb and root.val < ub
```

not:

```python
root.val >= lb and root.val <= ub
```

---

# 19. Recursion Decision Rule

Whenever you write a recursive function, ask:

```text
"Should this value be shared by all recursive calls,
or should each recursive call have its own version?"
```

Use this rule:

```text
Different recursive branches need different values
                ↓
        Pass as parameter
```

Example:

```python
validate(root, lb, ub)
```

Here:

```text
lb / ub → different for each subtree
```

So they are parameters.

---

```text
All recursive calls need to update the same global result
                ↓
          Shared state
```

For example:

```python
self.maxSum
self.diameter
self.minVal
```

can be shared when all recursive calls contribute to the same final answer.

---

# 20. Pattern Recognition

When a problem says:

> "Check whether every node satisfies a constraint based on its ancestors."

Think:

```text
DFS
 ↓
Carry constraints/range
 ↓
Update range for children
 ↓
Validate current node
```

For BST validation:

```text
Range Validation
      ↓
(lower_bound, upper_bound)
      ↓
Left  → (lb, root.val)
Right → (root.val, ub)
```

---

# 21. Revision Cheat Sheet

```text
Problem:
Validate Binary Search Tree

Core Pattern:
Range Validation

Root range:
(-∞, +∞)

Current node:
lb < root.val < ub

Left subtree:
(lb, root.val)

Right subtree:
(root.val, ub)

Why ranges?
BST rule applies to the entire subtree,
not just the parent.

Important recursion question:
"Should this value be shared by all recursive calls,
or should each recursive call have its own version?"

Answer here:
lb and ub are different for each recursive path,
so pass them as parameters.

Time:
O(n)

Space:
O(h)

One-Line Pattern:
Validate BST = DFS + carry `(lower_bound, upper_bound)` + update the valid range for every child.
```