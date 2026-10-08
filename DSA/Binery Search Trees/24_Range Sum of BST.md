# Range Sum of BST

## 1. Problem

Given the root of a **Binary Search Tree (BST)** and two integers:

```text
low
high
```

find the sum of all node values that satisfy:

```text
low <= node.val <= high
```

### Example

```text
          10
         /  \
        5    15
       / \     \
      3   7     18
```

For:

```text
low = 7
high = 15
```

Valid values:

```text
7, 10, 15
```

Answer:

```text
32
```

The important part is that this is a **BST**, so we can skip entire subtrees that cannot contain valid values.

---

# 2. Brute Force Approach

The simplest approach is to visit **every node**.

For each node:

```text
If low <= node.val <= high:
    add node.val
```

We don't use the BST property for pruning.

```text
             BST
              |
        Visit every node
              |
      Check low <= value <= high
              |
             Sum
```

### Complexity

```text
Time:  O(n)
Space: O(h)
```

where:

- `n` = number of nodes
- `h` = height of the tree

This works, but we can do better in terms of the number of nodes visited by using the BST property.

---

# 3. Optimized Approach

For every node, compare its value with the range:

```text
low <= root.val <= high
```

There are three important cases.

### Case 1: Node is inside the range

```text
low <= root.val <= high
```

The current value should be added.

But we cannot skip either subtree because:

```text
left subtree  → may contain values inside range
right subtree → may contain values inside range
```

So:

```text
Add root.val
Go left
Go right
```

---

### Case 2: Node is smaller than `low`

```text
root.val < low
```

Because this is a BST:

```text
left subtree values < root.val
```

Therefore:

```text
left subtree values < low
```

So nothing in the left subtree can be part of the answer.

We only search:

```text
right subtree
```

```text
        root
       /    \
  too small   possible
              values
```

---

### Case 3: Node is greater than `high`

```text
root.val > high
```

Because this is a BST:

```text
right subtree values > root.val
```

Therefore:

```text
right subtree values > high
```

So nothing in the right subtree can be part of the answer.

We only search:

```text
left subtree
```

```text
        root
       /    \
 possible    too large
 values
```

---

# 4. Main Idea

The complete decision process is:

```text
                  root
                   |
          +--------+--------+
          |        |        |
      root < low   in range  root > high
          |          |          |
       Go right   Add value   Go left
                    |   |
                  left right
```

This is the main BST pruning pattern:

> **If the current value is outside the range, use the BST property to completely skip the subtree that cannot contain valid values.**

---

# 5. Code

```python
class Solution:
    def rangeSumBST(
        self,
        root: TreeNode | None,
        low: int,
        high: int
    ) -> int:

        if root is None:
            return 0

        ans = 0
        wasInRange = False

        # Current node is inside the range
        if root.val >= low and root.val <= high:
            wasInRange = True
            ans += root.val

        # Current node is inside the range.
        # Both subtrees may contain valid values.
        if wasInRange:
            ans += (
                self.rangeSumBST(root.left, low, high)
                + self.rangeSumBST(root.right, low, high)
            )

        # Current node is smaller than the range.
        # Skip the left subtree and go right.
        elif root.val < low:
            ans += self.rangeSumBST(root.right, low, high)

        # Current node is larger than the range.
        # Skip the right subtree and go left.
        elif root.val > high:
            ans += self.rangeSumBST(root.left, low, high)

        return ans
```

---

# 6. Understanding `wasInRange`

The variable:

```python
wasInRange = False
```

is used to determine whether the current node lies inside:

```text
[low, high]
```

This condition:

```python
if root.val >= low and root.val <= high:
```

means:

```text
low <= root.val <= high
```

If true:

```python
wasInRange = True
ans += root.val
```

Then both subtrees are explored.

---

# 7. Why Explore Both Subtrees When the Node Is in Range?

Suppose:

```text
          10
         /  \
        5    15
       / \     \
      3   7     18
```

Range:

```text
[7, 15]
```

At:

```text
root = 10
```

we have:

```text
7 <= 10 <= 15
```

So `10` is valid.

But:

```text
left subtree:
3, 5, 7
```

contains `7`, which is valid.

And:

```text
right subtree:
15, 18
```

contains `15`, which is valid.

Therefore we must explore both sides.

---

# 8. Why Can We Skip the Left Subtree?

Suppose:

```text
root.val = 5
low = 7
high = 15
```

Since:

```text
5 < 7
```

the current node is too small.

Because this is a BST:

```text
left subtree < 5
```

So:

```text
left subtree < 7
```

Every value there is invalid.

Therefore:

```python
self.rangeSumBST(root.right, low, high)
```

is enough.

---

# 9. Why Can We Skip the Right Subtree?

Suppose:

```text
root.val = 18
low = 7
high = 15
```

Since:

```text
18 > 15
```

the current node is too large.

Because this is a BST:

```text
right subtree > 18
```

Therefore:

```text
right subtree > 15
```

Every value there is invalid.

So we only search:

```python
self.rangeSumBST(root.left, low, high)
```

---

# 10. Dry Run

Consider:

```text
          10
         /  \
        5    15
       / \     \
      3   7     18
```

Range:

```text
low = 7
high = 15
```

### Step 1: Root = 10

```text
7 <= 10 <= 15
```

Add:

```text
ans = 10
```

Explore both sides.

---

### Step 2: Node = 5

```text
5 < 7
```

So `5` is too small.

Skip:

```text
3
```

Go right to:

```text
7
```

---

### Step 3: Node = 7

```text
7 <= 7 <= 15
```

Add:

```text
ans = 10 + 7
    = 17
```

---

### Step 4: Node = 15

```text
7 <= 15 <= 15
```

Add:

```text
ans = 17 + 15
    = 32
```

Its right child:

```text
18
```

is greater than `15`, so we go left, which is `None`.

Final answer:

```text
32
```

---

# 11. Recursion Tree

The traversal does not necessarily visit every node.

For the example:

```text
          10
         /  \
        5    15
       / \     \
      3   7     18
```

with:

```text
[7, 15]
```

the important paths are:

```text
             10
            /  \
           5    15
            \     \
             7     18
```

At `5`, we skip its left subtree.

At `18`, we skip its right subtree.

This is the advantage of using the BST property.

---

# 12. Complexity

Let `n` be the number of nodes and `h` be the tree height.

Every visited node takes:

```text
O(1)
```

work.

The algorithm can prune entire subtrees.

### Time

```text
Best / highly pruned: less than O(n)
Worst case: O(n)
```

The worst case can still require visiting every node.

So the standard complexity is:

```text
O(n)
```

### Space

The recursion stack depends on tree height:

```text
O(h)
```

For a balanced BST:

```text
h = O(log n)
```

For a skewed BST:

```text
h = O(n)
```

Therefore:

```text
Space = O(h)
```

---

# 13. Complexity Comparison

| Approach | Time | Space | BST Pruning |
|---|---:|---:|---|
| Visit every node | O(n) | O(h) | No |
| BST range pruning | O(n) worst case | O(h) | Yes |

Both have the same worst-case Big-O time, but the optimized approach can visit **far fewer nodes in practice** because entire subtrees are skipped.

---

# 14. Common Mistakes

### Mistake 1: Traversing both sides every time

This ignores the main BST advantage.

If:

```python
root.val < low
```

don't visit the left subtree.

If:

```python
root.val > high
```

don't visit the right subtree.

---

### Mistake 2: Forgetting boundary values

The range is inclusive:

```text
low <= value <= high
```

Therefore if:

```text
value == low
```

it must be included.

Similarly:

```text
value == high
```

must be included.

---

### Mistake 3: Thinking an out-of-range node means stop completely

Suppose:

```text
root.val < low
```

The current node is invalid, but its **right subtree may contain valid values**.

So:

```text
root < low → go right
```

Similarly:

```text
root > high → go left
```

---

### Mistake 4: Using this logic on a normal Binary Tree

This pruning works only because the tree is a BST.

For a general binary tree:

```text
root.val < low
```

does **not** tell us anything about the left subtree.

So both subtrees may need to be searched.

---

# 15. Cleaner Way to Think About the Code

You can reduce the entire problem to three rules:

```text
1. root is None
   → return 0

2. root is inside [low, high]
   → add root
   → search both sides

3. root is outside range
   → use BST property to search only the possible side
```

In short:

```text
             root
               |
       +-------+-------+
       |       |       |
      <low   valid    >high
       |       |        |
      right  both      left
```

---

# 16. Revision Cheat Sheet

```text
Range Sum BST
      ↓
Check root
      ↓
root < low?
      ↓
Go RIGHT

root > high?
      ↓
Go LEFT

root inside [low, high]?
      ↓
Add root.val
      ↓
Go LEFT + RIGHT
```

### Core BST pruning rules

```python
if root.val < low:
    # left subtree is too small
    go right
```

```python
elif root.val > high:
    # right subtree is too large
    go left
```

```python
else:
    # current value is valid
    add it
    search both sides
```

### Complexity

```text
Time  = O(n) worst case
Space = O(h)
```

---

# One-Line Pattern

> **Range Sum in BST = Check the Range + Use BST Property to Prune the Impossible Subtree.**