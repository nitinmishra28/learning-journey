# Predecessor and Successor in BST

## 1. Problem

Given a **Binary Search Tree (BST)** and a key `key`, find:

- **Inorder Predecessor** of `key`
- **Inorder Successor** of `key`

### Predecessor

The predecessor is the node with the **largest value smaller than `key`**.

### Successor

The successor is the node with the **smallest value greater than `key`**.

### Example

```text
        20
       /  \
      10   30
     / \   / \
    5  15 25  35
```

For:

```text
key = 20
```

Inorder traversal:

```text
5 → 10 → 15 → 20 → 25 → 30 → 35
```

Therefore:

```text
Predecessor = 15
Successor   = 25
```

---

# 2. Important Observation

A BST gives us an important property:

```text
        BST
         ↓
Left values < Root < Right values
```

Therefore, while searching for `key`, we can also keep track of possible predecessor and successor.

### If:

```text
curr.data < key
```

then `curr` can be a predecessor.

Why?

Because:

```text
curr.data < key
```

But there might be a larger value than `curr.data` that is still smaller than `key`.

So:

```python
pred = curr
curr = curr.right
```

We move right to search for a **larger predecessor**.

---

### If:

```text
curr.data > key
```

then `curr` can be a successor.

Why?

Because:

```text
curr.data > key
```

But there might be a smaller value than `curr.data` that is still greater than `key`.

So:

```python
succ = curr
curr = curr.left
```

We move left to search for a **smaller successor**.

---

# 3. Brute Force Approach

A straightforward approach is:

1. Perform inorder traversal.
2. Store all values.
3. Find `key`.
4. The value before `key` is the predecessor.
5. The value after `key` is the successor.

For example:

```text
Inorder:

5 → 10 → 15 → 20 → 25 → 30 → 35
                  ↑
                 key
```

Therefore:

```text
Previous = 15
Next     = 25
```

### Complexity

```text
Time  : O(n)
Space : O(n)
```

The entire tree needs to be traversed and the complete inorder sequence is stored.

We can do better by directly using the BST property.

---

# 4. Optimized Approach

We can find predecessor and successor using **BST search**.

Instead of generating the entire inorder traversal, we walk from the root toward `key`.

Maintain:

```python
pred = None
succ = None
```

These represent the best predecessor and successor found so far.

The search has three cases:

```text
curr.data < key
curr.data > key
curr.data == key
```

---

# 5. Case 1 — `curr.data < key`

Suppose:

```text
        20
       /
      10
```

and:

```text
key = 15
```

We are at:

```text
curr = 10
```

Since:

```text
10 < 15
```

`10` can be a predecessor.

So:

```python
pred = curr
```

But there may be a larger value between `10` and `15`.

Therefore we move right:

```python
curr = curr.right
```

### Rule

```text
curr < key
    ↓
curr is a possible predecessor
    ↓
Move RIGHT
```

Because we want the **largest value smaller than key**.

---

# 6. Case 2 — `curr.data > key`

Suppose:

```text
        20
       /
      10
```

and:

```text
key = 15
```

At the root:

```text
curr = 20
```

Since:

```text
20 > 15
```

`20` can be a successor.

So:

```python
succ = curr
```

But there may be a smaller value between `15` and `20`.

Therefore move left:

```python
curr = curr.left
```

### Rule

```text
curr > key
    ↓
curr is a possible successor
    ↓
Move LEFT
```

Because we want the **smallest value greater than key**.

---

# 7. Case 3 — `curr.data == key`

Once we find the exact key:

```python
curr.data == key
```

we can find predecessor and successor directly from its subtrees.

---

## Predecessor

The predecessor of a node is:

> The maximum value in its left subtree.

Therefore:

```python
temp = curr.left

while temp:
    pred = temp
    temp = temp.right
```

Why move right?

Because in a BST:

```text
Right = larger values
```

So the rightmost node in the left subtree is the maximum value smaller than `key`.

---

## Successor

The successor of a node is:

> The minimum value in its right subtree.

Therefore:

```python
temp = curr.right

while temp:
    succ = temp
    temp = temp.left
```

Why move left?

Because:

```text
Left = smaller values
```

So the leftmost node in the right subtree is the minimum value greater than `key`.

---

# 8. Your Code

```python
class Solution:

    def findPreSuc(self, root, key):

        pred = None
        succ = None
        curr = root

        while curr:

            if curr.data < key:

                # Current node can be predecessor
                pred = curr

                # Search for a larger predecessor
                curr = curr.right

            elif curr.data > key:

                # Current node can be successor
                succ = curr

                # Search for a smaller successor
                curr = curr.left

            else:

                # Key found

                # Find predecessor:
                # maximum value in left subtree
                temp = curr.left

                while temp:
                    pred = temp
                    temp = temp.right

                # Find successor:
                # minimum value in right subtree
                temp = curr.right

                while temp:
                    succ = temp
                    temp = temp.left

                break

        return pred, succ
```

---

# 9. Understanding the Main Search

Consider:

```text
        20
       /  \
      10   30
     / \   / \
    5  15 25 35
```

Find predecessor and successor of:

```text
key = 18
```

Start:

```text
curr = 20
```

Since:

```text
20 > 18
```

we have:

```text
succ = 20
```

and move left:

```text
curr = 10
```

Now:

```text
10 < 18
```

So:

```text
pred = 10
```

Move right:

```text
curr = 15
```

Again:

```text
15 < 18
```

So:

```text
pred = 15
```

Move right:

```text
curr = None
```

Search ends.

Final:

```text
Predecessor = 15
Successor   = 20
```

---

# 10. Why Do We Keep Updating `pred`?

Suppose:

```text
        20
       /
      10
        \
         15
           \
            18
```

and:

```text
key = 19
```

We encounter:

```text
10 < 19
```

So:

```text
pred = 10
```

Then:

```text
15 < 19
```

Update:

```text
pred = 15
```

Then:

```text
18 < 19
```

Update:

```text
pred = 18
```

Now `18` is the closest value below `19`.

So:

```text
Predecessor = 18
```

The rule is:

```text
Every time curr < key:
    pred = curr
    move right
```

Moving right tries to find a larger valid predecessor.

---

# 11. Why Do We Keep Updating `succ`?

Consider:

```text
        30
       /
      20
     /
    10
```

and:

```text
key = 15
```

At `30`:

```text
30 > 15
```

So:

```text
succ = 30
```

Move left.

At `20`:

```text
20 > 15
```

Update:

```text
succ = 20
```

Move left.

At `10`:

```text
10 < 15
```

Now:

```text
pred = 10
```

Final:

```text
Predecessor = 10
Successor   = 20
```

The rule is:

```text
Every time curr > key:
    succ = curr
    move left
```

Moving left tries to find a smaller valid successor.

---

# 12. Why Does the Search Work Without Finding `key`?

This is an important point.

The key may not actually exist in the BST.

For example:

```text
        20
       /  \
      10   30
     / \
    5  15
```

Search:

```text
key = 18
```

There is no `18`.

But while searching:

```text
20 > 18
```

so:

```text
succ = 20
```

Then:

```text
10 < 18
```

so:

```text
pred = 10
```

Then:

```text
15 < 18
```

so:

```text
pred = 15
```

Search ends.

Final:

```text
Predecessor = 15
Successor   = 20
```

Therefore, the algorithm can find the predecessor and successor even when `key` is not present.

---

# 13. When `key` Exists

If `key` exists, we eventually reach:

```python
curr.data == key
```

At that point, we can find the exact predecessor and successor using the two subtrees.

### Predecessor

```text
Left subtree
     ↓
Go right as much as possible
     ↓
Rightmost node
```

### Successor

```text
Right subtree
     ↓
Go left as much as possible
     ↓
Leftmost node
```

---

# 14. Dry Run — Key Exists

Consider:

```text
        20
       /  \
      10   30
     / \   / \
    5  15 25 35
```

Find:

```text
key = 20
```

At root:

```text
curr.data == key
```

Now find predecessor.

### Predecessor

Left subtree:

```text
       10
      /  \
     5   15
```

Start:

```text
temp = 10
```

Move right:

```text
temp = 15
```

Move right:

```text
temp = None
```

Therefore:

```text
pred = 15
```

### Successor

Right subtree:

```text
       30
      /  \
     25   35
```

Start:

```text
temp = 30
```

Move left:

```text
temp = 25
```

Move left:

```text
temp = None
```

Therefore:

```text
succ = 25
```

Final:

```text
Predecessor = 15
Successor   = 25
```

---

# 15. Dry Run — Key Does Not Exist

Consider:

```text
        20
       /  \
      10   30
     / \
    5  15
```

Find:

```text
key = 18
```

### Step 1

```text
curr = 20
```

```text
20 > 18
```

Therefore:

```text
succ = 20
curr = 10
```

---

### Step 2

```text
curr = 10
```

```text
10 < 18
```

Therefore:

```text
pred = 10
curr = 15
```

---

### Step 3

```text
curr = 15
```

```text
15 < 18
```

Therefore:

```text
pred = 15
curr = None
```

Search ends.

Final:

```text
pred = 15
succ = 20
```

---

# 16. Edge Cases

### Case 1 — Key is minimum

```text
        20
       /
      10
     /
    5
```

For:

```text
key = 5
```

There is no smaller value.

Therefore:

```text
pred = None
succ = 10
```

---

### Case 2 — Key is maximum

```text
    10
      \
       20
         \
          30
```

For:

```text
key = 30
```

There is no larger value.

Therefore:

```text
pred = 20
succ = None
```

---

### Case 3 — Single Node

```text
    10
```

For:

```text
key = 10
```

There is no predecessor or successor.

```text
pred = None
succ = None
```

---

### Case 4 — Key Smaller Than Minimum

```text
        20
       /  \
      10   30
```

For:

```text
key = 5
```

There is no predecessor.

The smallest value greater than `5` is:

```text
10
```

Therefore:

```text
pred = None
succ = 10
```

---

### Case 5 — Key Greater Than Maximum

For:

```text
key = 40
```

there is no successor.

```text
pred = 30
succ = None
```

---

# 17. Why the Algorithm Is O(h)

We do not traverse the entire tree.

The main search follows only one path:

```text
Root
 ↓
Left / Right
 ↓
Left / Right
 ↓
...
```

At most:

```text
h
```

nodes are visited.

When `key` exists, we may additionally traverse:

```text
Rightmost path of left subtree
```

and:

```text
Leftmost path of right subtree
```

Both are bounded by the tree height.

Therefore:

```text
Time = O(h)
```

For a balanced BST:

```text
h = O(log n)
```

So:

```text
Time = O(log n)
```

For a skewed BST:

```text
h = O(n)
```

So worst case:

```text
Time = O(n)
```

---

# 18. Space Complexity

The solution is iterative.

There is no recursion stack and no array.

We only use:

```python
pred
succ
curr
temp
```

These are constant-size variables.

Therefore:

```text
Space = O(1)
```

This is an important advantage over the inorder-array approach.

---

# 19. Complexity Comparison

| Approach | Time | Extra Space |
|---|---:|---:|
| Inorder + Array | `O(n)` | `O(n)` |
| Recursive Traversal | `O(n)` | `O(h)` |
| **BST Property + Iterative Search** | **`O(h)`** | **`O(1)`** |

For a balanced BST:

```text
Optimized:

Time  = O(log n)
Space = O(1)
```

For a skewed BST:

```text
Time  = O(n)
Space = O(1)
```

---

# 20. Common Mistakes

### Mistake 1: Moving in the wrong direction

If:

```text
curr < key
```

we want a **larger predecessor**.

Therefore:

```python
curr = curr.right
```

If:

```text
curr > key
```

we want a **smaller successor**.

Therefore:

```python
curr = curr.left
```

Remember:

```text
curr < key
    ↓
pred = curr
    ↓
GO RIGHT


curr > key
    ↓
succ = curr
    ↓
GO LEFT
```

---

### Mistake 2: Finding the wrong node in the subtree

For predecessor:

```text
Maximum of left subtree
```

Therefore:

```text
Go RIGHT
```

For successor:

```text
Minimum of right subtree
```

Therefore:

```text
Go LEFT
```

---

### Mistake 3: Returning the key itself

Predecessor and successor must be **strictly smaller/larger**.

So:

```text
predecessor < key
successor > key
```

The key itself cannot be either one.

---

### Mistake 4: Traversing the entire tree

We don't need:

```text
Inorder → Array → Search
```

The BST property lets us follow only relevant paths.

---

# 21. Important Mental Model

Think of the search as maintaining two candidates:

```text
             key
              |
        ----------------
        |              |
     smaller         larger
        |              |
      pred           succ
```

Whenever we see a value smaller than `key`:

```text
Could this be a better predecessor?
        ↓
Yes
        ↓
Save it
        ↓
Go right
```

Whenever we see a value larger than `key`:

```text
Could this be a better successor?
        ↓
Yes
        ↓
Save it
        ↓
Go left
```

This gradually gets us closer to `key`.

---

# 22. Pattern Recognition

When you see:

```text
BST
+
Find predecessor / successor
```

Think:

```text
BST Property
     ↓
Search Path
     ↓
Maintain Candidates
```

### Search Rules

```text
curr < key
    ↓
pred = curr
go RIGHT


curr > key
    ↓
succ = curr
go LEFT
```

### If key is found

```text
Predecessor:
maximum of left subtree
→ rightmost node

Successor:
minimum of right subtree
→ leftmost node
```

---

# 23. Revision Cheat Sheet

```text
Problem:
Find Predecessor and Successor in BST

Predecessor:
Largest value < key

Successor:
Smallest value > key

Main Pattern:
BST Search + Maintain Candidates

During Search:

if curr.data < key:
    pred = curr
    curr = curr.right

elif curr.data > key:
    succ = curr
    curr = curr.left

else:
    Key found

    Predecessor:
    rightmost node of left subtree

    Successor:
    leftmost node of right subtree

Why go right when curr < key?
Need a larger value that is still < key.

Why go left when curr > key?
Need a smaller value that is still > key.

If key doesn't exist:
The candidate tracking still gives the
closest predecessor and successor.

Time:
O(h)

Balanced BST:
O(log n)

Worst case:
O(n)

Space:
O(1)

One-Line Pattern:
BST Predecessor/Successor = Search toward the key while maintaining the best smaller/larger candidates.