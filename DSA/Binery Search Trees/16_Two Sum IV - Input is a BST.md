# Two Sum IV - Input is a BST

## 1. Problem

Given the root of a **Binary Search Tree (BST)** and an integer `k`, determine whether there exist **two different nodes** whose values add up to `k`.

### Example

```text
        5
       / \
      3   6
     / \   \
    2   4   7

k = 9
```

There are two nodes:

```text
2 + 7 = 9
```

Therefore:

```text
True
```

---

# 2. Brute Force Approach

A simple approach is:

1. Traverse the entire BST.
2. Store all node values in an array.
3. Use two loops to check every pair.

Example:

```python
values = [2, 3, 4, 5, 6, 7]

for i in range(len(values)):
    for j in range(i + 1, len(values)):
        if values[i] + values[j] == k:
            return True
```

### Complexity

```text
Time  : O(n²)
Space : O(n)
```

We can improve the time using a hash set:

```python
seen = set()

def dfs(root):
    if root is None:
        return False

    if k - root.val in seen:
        return True

    seen.add(root.val)

    return dfs(root.left) or dfs(root.right)
```

This gives:

```text
Time  : O(n)
Space : O(n)
```

But we are not taking advantage of the special property of the BST.

---

# 3. Optimized Approach

A BST has an important property:

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
2 → 3 → 4 → 5 → 6 → 7
```

Once we have sorted values, we can use the **Two Pointer** technique.

Normally with an array:

```text
left  → smallest
right → largest
```

Then:

```text
sum < k → move left forward
sum > k → move right backward
sum == k → found
```

But storing the entire inorder array would require `O(n)` space.

Instead, we can create:

```text
Forward BST Iterator
        ↓
smallest → larger → larger → ...

Backward BST Iterator
        ↓
largest → smaller → smaller → ...
```

This gives us the same behavior as two pointers **without storing the complete sorted array**.

---

# 4. Main Idea

We create two BST iterators.

### Forward Iterator

It produces values in ascending order:

```text
2 → 3 → 4 → 5 → 6 → 7
```

It uses:

```python
pushLeftNodes()
```

because the leftmost node is the smallest node.

---

### Backward Iterator

It produces values in descending order:

```text
7 → 6 → 5 → 4 → 3 → 2
```

It uses:

```python
pushRightNodes()
```

because the rightmost node is the largest node.

---

# 5. Two Pointers Without an Array

Think of the two iterators as:

```text
Forward Iterator
       ↓
2 → 3 → 4 → 5 → 6 → 7
↑
i


Backward Iterator
       ↓
7 → 6 → 5 → 4 → 3 → 2
↑
j
```

Initially:

```text
i = smallest
j = largest
```

Then:

```text
i + j < k
      ↓
Move i forward
```

and:

```text
i + j > k
      ↓
Move j backward
```

This is exactly the two-pointer technique.

---

# 6. BST Iterator

Your iterator supports both directions using:

```python
reverse=False
```

or:

```python
reverse=True
```

### Normal Mode

```python
BSTIterator(root, False)
```

Uses:

```python
pushLeftNodes(root)
```

and produces:

```text
smallest → largest
```

### Reverse Mode

```python
BSTIterator(root, True)
```

Uses:

```python
pushRightNodes(root)
```

and produces:

```text
largest → smallest
```

---

# 7. Your Code

```python
class BSTIterator:

    def __init__(self, root, reverse=False):
        self.stack = []
        self.reverse = reverse

        if reverse:
            self.pushRightNodes(root)
        else:
            self.pushLeftNodes(root)

    def pushLeftNodes(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def pushRightNodes(self, root):
        while root:
            self.stack.append(root)
            root = root.right

    def next(self):
        top = self.stack.pop()

        if top.right:
            self.pushLeftNodes(top.right)

        return top.val

    def before(self):
        top = self.stack.pop()

        if top.left:
            self.pushRightNodes(top.left)

        return top.val

    def hasNext(self):
        return len(self.stack) > 0


class Solution:

    def findTarget(self, root, k):

        if root is None:
            return False

        forward = BSTIterator(root, False)
        backward = BSTIterator(root, True)

        i = forward.next()
        j = backward.before()

        while i < j:

            if i + j == k:
                return True

            elif i + j < k:
                if forward.hasNext():
                    i = forward.next()
                else:
                    break

            else:
                if backward.hasNext():
                    j = backward.before()
                else:
                    break

        return False
```

---

# 8. Understanding the Forward Iterator

The forward iterator performs:

```text
Inorder:
Left → Node → Right
```

The initial call:

```python
forward = BSTIterator(root, False)
```

calls:

```python
self.pushLeftNodes(root)
```

For:

```text
        5
       / \
      3   6
     / \
    2   4
```

the stack initially contains:

```text
TOP
 ↓
2
3
5
```

So:

```python
forward.next()
```

returns:

```text
2
```

After popping `2`, there is no right subtree.

Next:

```python
forward.next()
```

returns:

```text
3
```

Since `3` has a right child `4`, we push:

```text
4
```

Therefore the iterator continues:

```text
2 → 3 → 4 → 5 → 6
```

---

# 9. Understanding the Backward Iterator

The backward iterator performs **reverse inorder**:

```text
Right → Node → Left
```

The initial call:

```python
backward = BSTIterator(root, True)
```

calls:

```python
self.pushRightNodes(root)
```

For:

```text
        5
       / \
      3   6
           \
            7
```

the stack becomes:

```text
TOP
 ↓
7
6
5
```

Therefore:

```python
backward.before()
```

returns:

```text
7
```

After visiting `7`, we move backward toward smaller values.

So the sequence becomes:

```text
7 → 6 → 5 → 3 → ...
```

---

# 10. Why `next()` and `before()` Are Different

### Forward

We want:

```text
smallest → larger
```

So after popping a node, we need to process its:

```text
right subtree
```

Therefore:

```python
if top.right:
    self.pushLeftNodes(top.right)
```

---

### Backward

We want:

```text
largest → smaller
```

So after popping a node, we need to process its:

```text
left subtree
```

Therefore:

```python
if top.left:
    self.pushRightNodes(top.left)
```

This is the mirror image of normal inorder traversal.

---

# 11. Important Connection

Normal inorder:

```text
L → N → R
```

uses:

```text
Push Left
Pop Node
Go Right
```

Reverse inorder:

```text
R → N → L
```

uses:

```text
Push Right
Pop Node
Go Left
```

So:

```text
Normal Iterator:

Push Left
   ↓
Pop
   ↓
Push Left of Right


Reverse Iterator:

Push Right
   ↓
Pop
   ↓
Push Right of Left
```

---

# 12. Dry Run

Consider:

```text
        5
       / \
      3   6
     / \   \
    2   4   7

k = 9
```

Sorted order:

```text
2 → 3 → 4 → 5 → 6 → 7
```

Reverse sorted order:

```text
7 → 6 → 5 → 4 → 3 → 2
```

Initialize:

```python
i = forward.next()
j = backward.before()
```

Therefore:

```text
i = 2
j = 7
```

Check:

```text
2 + 7 = 9
```

So:

```text
return True
```

---

# 13. Another Dry Run

Consider:

```text
        5
       / \
      3   6
     / \   \
    2   4   7

k = 10
```

Initial:

```text
i = 2
j = 7
```

Calculate:

```text
2 + 7 = 9
```

Since:

```text
9 < 10
```

we need a larger sum.

Therefore move the smaller pointer:

```python
i = forward.next()
```

Now:

```text
i = 3
j = 7
```

Calculate:

```text
3 + 7 = 10
```

Found:

```text
True
```

---

# 14. What If the Sum Is Too Large?

Suppose:

```text
i = 4
j = 7

i + j = 11
k = 10
```

The sum is too large.

We need a smaller value.

So move the larger pointer backward:

```python
j = backward.before()
```

Now:

```text
j = 6
```

New sum:

```text
4 + 6 = 10
```

Found.

Therefore:

```text
sum > k
    ↓
Move backward iterator
```

---

# 15. Why `while i < j`?

We need **two different nodes**.

Suppose:

```text
i = 5
j = 5
```

We cannot use:

```text
5 + 5
```

if there is only one node containing `5`.

Therefore:

```python
while i < j:
```

ensures that we stop when the two iterators meet or cross.

Since BST values are assumed to be ordered and the iterators move monotonically:

```text
i < j
```

represents that the two positions are still different.

---

# 16. Why We Don't Store the Inorder Array

Another common solution is:

```python
inorder = []
```

Then:

```text
BST
 ↓
Inorder
 ↓
Sorted Array
 ↓
Two Pointers
```

That uses:

```text
O(n)
```

extra space.

Your solution does:

```text
BST
 ↓
Two BST Iterators
 ↓
Forward + Backward
 ↓
Two Pointers
```

The iterators store only traversal state.

Therefore extra space becomes:

```text
O(h)
```

instead of:

```text
O(n)
```

---

# 17. Why the Stack Is Needed

The iterator needs to remember where it should return after processing a subtree.

For example:

```text
        5
       /
      3
     /
    2
```

When we move left:

```text
5 → 3 → 2
```

we need to remember:

```text
3
5
```

for later.

The stack does this:

```text
TOP
 ↓
2
3
5
```

After returning `2`:

```text
TOP
 ↓
3
5
```

Then after returning `3`:

```text
TOP
 ↓
5
```

This is the same idea as the recursion stack in recursive inorder traversal.

---

# 18. Complexity

Let:

```text
n = number of nodes
h = height of the BST
```

### Initialization

Each iterator initially pushes one root-to-leaf path:

```text
O(h)
```

We have two iterators:

```text
O(h) + O(h) = O(h)
```

asymptotically.

### Each Iterator Operation

A single call can sometimes push multiple nodes.

However, every node is pushed and popped at most once by each iterator.

Therefore operations are:

```text
O(1) amortized
```

### Total Time

Across the complete traversal:

```text
O(n)
```

### Extra Space

Two stacks are maintained:

```text
O(h)
```

For a balanced BST:

```text
O(log n)
```

For a skewed BST:

```text
O(n)
```

### Final Complexity

```text
Time  : O(n)
Space : O(h)
```

---

# 19. Brute Force vs Optimized

| Approach | Time | Space | Uses BST Property? |
|---|---:|---:|---|
| Nested loops | `O(n²)` | `O(n)` | No |
| Hash Set | `O(n)` | `O(n)` | No |
| Inorder + Two Pointers | `O(n)` | `O(n)` | Yes |
| **Two BST Iterators** | **`O(n)`** | **`O(h)`** | **Yes** |

The important optimization in your solution is:

```text
Same O(n) time
BUT
O(n) space → O(h) space
```

---

# 20. Common Mistakes

### Mistake 1: Using only one iterator

One iterator gives:

```text
smallest → largest
```

But two pointers require:

```text
smallest ←→ largest
```

Therefore we use:

```python
forward
backward
```

---

### Mistake 2: Using `pushLeftNodes()` for both

The backward iterator must start from the largest node.

Therefore:

```python
reverse=True
```

must use:

```python
pushRightNodes(root)
```

---

### Mistake 3: Forgetting the right subtree in `next()`

Correct:

```python
if top.right:
    self.pushLeftNodes(top.right)
```

---

### Mistake 4: Forgetting the left subtree in `before()`

Correct:

```python
if top.left:
    self.pushRightNodes(top.left)
```

---

### Mistake 5: Moving the wrong pointer

Remember:

```text
sum < k
    ↓
Need bigger sum
    ↓
Move forward / smaller pointer
```

And:

```text
sum > k
    ↓
Need smaller sum
    ↓
Move backward / larger pointer
```

---

# 21. Pattern Recognition

When you see:

```text
BST
+
Find two values
+
Target sum
+
Need better than O(n²)
```

Think:

```text
BST
 ↓
Inorder = Sorted
 ↓
Two Pointers
```

If you want to avoid storing the complete inorder array:

```text
Sorted Array
     ↓
Replace with
     ↓
Two BST Iterators
```

Pattern:

```text
Forward Iterator
        ↓
Smallest → Larger → Larger

Backward Iterator
        ↓
Largest → Smaller → Smaller

             ↓
        Two Pointers
             ↓
        Compare Sum
```

---

# 22. Revision Cheat Sheet

```text
Problem:
Two Sum in BST

Brute Force:
Nested loops
O(n²) time

Better:
Hash Set
O(n) time
O(n) space

Optimized:
Two BST Iterators

Forward:
Inorder
L → N → R
Smallest → Largest

Backward:
Reverse Inorder
R → N → L
Largest → Smallest

Forward Iterator:
pushLeftNodes()

Backward Iterator:
pushRightNodes()

If sum == k:
    return True

If sum < k:
    move forward iterator

If sum > k:
    move backward iterator

Stop:
while i < j

Time:
O(n)

Space:
O(h)

Core Pattern:
BST → Sorted Order → Two Pointers → Two BST Iterators

One-Line Pattern:
Two Sum in BST = Forward Inorder Iterator + Reverse Inorder Iterator + Two Pointers.
```