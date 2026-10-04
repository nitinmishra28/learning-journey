# Inorder Successor in BST

## 1. Problem

Given a **Binary Search Tree (BST)** and a node `k`, find the **inorder successor** of `k`.

The inorder successor is:

> The node that comes immediately after `k` in the inorder traversal.

BST inorder traversal:

```text
Left → Node → Right
```

produces values in sorted order.

### Example

```text
        20
       /  \
      10   30
     / \
    5   15
```

Inorder traversal:

```text
5 → 10 → 15 → 20 → 30
```

Therefore:

```text
Successor of 10 = 15
Successor of 15 = 20
Successor of 20 = 30
Successor of 30 = -1
```

---

# 2. Important Observation

Since this is a BST:

```text
BST
 ↓
Inorder Traversal
 ↓
Sorted Order
```

So if we perform inorder traversal and find:

```text
k
```

the next node visited is the inorder successor.

For example:

```text
5 → 10 → 15 → 20 → 30
         ↑
         k

Next node = 20
```

Therefore, the basic idea is:

```text
Inorder traversal
      ↓
Find k
      ↓
Return the next node
```

---

# 3. Brute Force Approach

The simplest approach is to store the complete inorder traversal.

```python
inorder = []

def traverse(root):
    if root is None:
        return

    traverse(root.left)
    inorder.append(root.data)
    traverse(root.right)
```

Then find `k` in the array:

```python
for i in range(len(inorder)):
    if inorder[i] == k.data:
        if i + 1 < len(inorder):
            return inorder[i + 1]
        return -1
```

### Complexity

```text
Time  : O(n)
Space : O(n)
```

The entire inorder traversal is stored even though we only need one next value.

---

# 4. Optimized Approach

We can avoid storing the complete inorder array.

Instead, maintain only:

```python
self.prev
```

and:

```python
self.curr
```

Where:

```text
prev
 ↓
previous node visited in inorder
```

and:

```text
curr
 ↓
answer / inorder successor
```

During inorder traversal:

```text
Left → Node → Right
```

when we reach a node, we check:

```python
if self.prev == k.data:
```

If true:

```text
Previous node was k
Current node is the next node
```

Therefore:

```python
self.curr = root.data
```

and we are done.

---

# 5. Main Idea

Suppose the inorder traversal is:

```text
5 → 10 → 15 → 20 → 30
```

and:

```text
k = 15
```

During traversal:

```text
prev = 5
current = 10
```

Then:

```text
prev = 10
current = 15
```

Then:

```text
prev = 15
current = 20
```

At this moment:

```python
self.prev == k.data
```

is true.

Therefore:

```python
self.curr = root.data
```

So:

```text
Successor = 20
```

---

# 6. Your Code

```python
class Solution:

    def __init__(self):
        self.prev = None
        self.curr = None

    def solve(self, root, k):

        # Stop if tree is finished
        # or successor has already been found
        if root is None or self.curr is not None:
            return

        # L
        self.solve(root.left, k)

        # If successor was found in left subtree,
        # don't continue traversal
        if self.curr is not None:
            return

        # N
        if self.prev == k.data:
            self.curr = root.data
            return

        # Current node becomes previous node
        self.prev = root.data

        # R
        self.solve(root.right, k)

    def inOrderSuccessor(self, root, k):

        # Reset state so the object can be reused
        self.prev = None
        self.curr = None

        self.solve(root, k)

        return self.curr if self.curr is not None else -1
```

---

# 7. Understanding `prev`

The most important variable is:

```python
self.prev
```

It represents:

> The previous node visited during inorder traversal.

For:

```text
        20
       /  \
      10   30
     / \
    5   15
```

Inorder:

```text
5 → 10 → 15 → 20 → 30
```

The values of `prev` change like this:

```text
Visit 5:
prev = 5

Visit 10:
prev = 10

Visit 15:
prev = 15

Visit 20:
prev = 20

Visit 30:
prev = 30
```

But before updating `prev`, we check whether:

```text
previous node == k
```

If yes, current node is the successor.

---

# 8. Why Do We Check `prev == k`?

This is the key line:

```python
if self.prev == k.data:
```

Suppose:

```text
Inorder:

5 → 10 → 15 → 20 → 30
         ↑     ↑
        prev  current
```

If:

```text
k = 15
```

then:

```text
prev = 15
current = 20
```

Therefore:

```text
current = inorder successor of k
```

This works because inorder traversal visits BST nodes in sorted order.

---

# 9. Why Do We Check Before Updating `prev`?

The order is very important.

Correct:

```python
if self.prev == k.data:
    self.curr = root.data
    return

self.prev = root.data
```

Suppose:

```text
prev = 15
current = 20
```

We first need to detect:

```text
prev == k
```

and identify:

```text
20
```

as the answer.

If we wrote:

```python
self.prev = root.data

if self.prev == k.data:
    ...
```

then:

```text
prev = 20
```

and we would lose the information that the previous node was `15`.

So the order must be:

```text
1. Check previous
2. Find successor if previous == k
3. Update previous
```

---

# 10. Why Do We Return Immediately?

Your code has:

```python
if self.prev == k.data:
    self.curr = root.data
    return
```

Once we find the successor, there is no reason to continue traversal.

For example:

```text
5 → 10 → 15 → 20 → 30
             ↑     ↑
             k     successor
```

Once we find `20`, the answer is already known.

So:

```text
Found answer
     ↓
Stop traversal
```

This is an optimization.

---

# 11. Why This Condition Is Important

At the beginning:

```python
if root is None or self.curr is not None:
    return
```

There are two stopping conditions.

### Condition 1

```python
root is None
```

There is no node to process.

### Condition 2

```python
self.curr is not None
```

We already found the successor.

Therefore:

```text
No node
   OR
Answer already found
   ↓
Stop recursion
```

---

# 12. Why Do We Check Again After Left Subtree?

Your code has:

```python
self.solve(root.left, k)

if self.curr is not None:
    return
```

This is important.

Suppose the successor is found somewhere inside the left subtree.

After returning from:

```python
self.solve(root.left, k)
```

we need to stop the current call as well.

Otherwise, this current node could continue executing and modify the state.

So:

```text
Search left subtree
       ↓
Successor found?
       ↓
Yes → Stop
No  → Process current node
```

---

# 13. Dry Run

Consider:

```text
        20
       /  \
      10   30
     / \
    5   15
```

Find successor of:

```text
k = 15
```

Inorder:

```text
5 → 10 → 15 → 20 → 30
```

### Visit 5

```text
prev = None
```

No comparison.

Then:

```text
prev = 5
```

---

### Visit 10

Check:

```text
prev == 15?
5 == 15 → False
```

Update:

```text
prev = 10
```

---

### Visit 15

Check:

```text
prev == 15?
10 == 15 → False
```

Update:

```text
prev = 15
```

---

### Visit 20

Check:

```text
prev == 15?
15 == 15 → True
```

Therefore:

```text
curr = 20
```

Return immediately.

Final:

```text
Successor = 20
```

---

# 14. Case: No Successor

Consider:

```text
        20
       /  \
      10   30
```

Find successor of:

```text
k = 30
```

Inorder:

```text
10 → 20 → 30
```

When we visit `30`:

```text
prev = 20
```

Check:

```text
20 == 30
```

False.

Then:

```text
prev = 30
```

There are no more nodes.

Therefore:

```python
self.curr is None
```

and:

```python
return -1
```

So:

```text
Successor of 30 = -1
```

---

# 15. Why `-1`?

If there is no successor, your implementation returns:

```python
-1
```

This means:

```text
No node exists after k in inorder traversal.
```

The maximum-valued node in a BST has no inorder successor.

---

# 16. Important Recursion State Concept

This problem connects directly to the question:

> Should this value be shared by all recursive calls, or should each recursive call have its own version?

Here:

```python
self.prev
self.curr
```

are **shared state**.

Why?

Because `prev` must represent the previous node in the **entire inorder traversal**.

We need:

```text
Node 1 → Node 2 → Node 3 → Node 4
             ↑
          same prev
```

If every recursive call had its own `prev`, we could not compare nodes across different recursive branches.

So:

```text
prev
 ↓
Shared across recursive calls
```

And:

```text
curr
 ↓
Shared answer state
```

---

# 17. Compare With BST Validation

This is a useful comparison with the previous problem.

### Validate BST

```python
validate(root, lb, ub)
```

Each subtree needs different bounds:

```text
Left:
(lb, root.val)

Right:
(root.val, ub)
```

Therefore:

```text
lb / ub
   ↓
Function parameters
```

---

### Inorder Successor

We want one continuous inorder state:

```text
prev
curr
```

Therefore:

```text
prev / curr
     ↓
Shared state
```

### Rule

```text
Different value for each recursive branch
        ↓
      Parameter


Same running value across the whole traversal
        ↓
     Shared state
```

---

# 18. Why We Don't Need BST Comparisons

You might think we should use:

```text
if k < root.val:
    go left
else:
    go right
```

That is another valid way to solve the inorder successor problem.

But **your solution is specifically using inorder traversal**.

Your reasoning is:

```text
BST
 ↓
Inorder is sorted
 ↓
Find k
 ↓
Next visited node = successor
```

So the solution does not need to explicitly compare:

```text
k.data < root.data
```

---

# 19. Optimized vs Brute Force

### Brute Force

Store complete inorder traversal:

```text
BST
 ↓
Inorder Array
 ↓
Find k
 ↓
Return next element
```

Complexity:

```text
Time  : O(n)
Space : O(n)
```

### Your Approach

```text
BST
 ↓
Inorder traversal
 ↓
Keep only prev
 ↓
When prev == k
 ↓
Current node is successor
```

Complexity:

```text
Time  : O(n)
Space : O(h)
```

The time is the same asymptotically, but your solution avoids storing the entire inorder array.

---

# 20. Complexity

Let:

```text
n = number of nodes
h = height of tree
```

### Time

In the worst case, we may visit every node:

```text
O(n)
```

### Space

The recursion call stack can contain at most one root-to-leaf path:

```text
O(h)
```

Balanced BST:

```text
O(log n)
```

Skewed BST:

```text
O(n)
```

### Final Complexity

```text
Time  : O(n)
Space : O(h)
```

---

# 21. Common Mistakes

### Mistake 1: Updating `prev` before checking

Wrong:

```python
self.prev = root.data

if self.prev == k.data:
    ...
```

Correct:

```python
if self.prev == k.data:
    self.curr = root.data
    return

self.prev = root.data
```

---

### Mistake 2: Forgetting to stop after finding the answer

Use:

```python
if self.curr is not None:
    return
```

Otherwise recursion can continue unnecessarily.

---

### Mistake 3: Forgetting to reset state

Your code correctly does:

```python
self.prev = None
self.curr = None
```

inside:

```python
def inOrderSuccessor(self, root, k):
```

This is important if the same `Solution` object is reused.

Otherwise a previous call's answer could remain stored.

---

### Mistake 4: Using an array unnecessarily

You don't need:

```python
inorder = []
```

The previous node is enough.

---

# 22. Pattern Recognition

When you see:

```text
BST
+
Find inorder successor
```

Think:

```text
BST
 ↓
Inorder = Sorted
 ↓
Track previous node
 ↓
If previous == k
 ↓
Current node = successor
```

Core pattern:

```text
Inorder Traversal
      ↓
Previous Node
      ↓
Find k
      ↓
Next Node = Answer
```

---

# 23. Revision Cheat Sheet

```text
Problem:
Find Inorder Successor in BST

BST Property:
Inorder traversal gives sorted order.

Inorder:
Left → Node → Right

State:
prev = previous inorder node
curr = answer

At every node:

if prev == k:
    curr = current node
    stop

Then:

prev = current node

Why prev is shared:
It represents the previous node in the entire inorder traversal.

Why curr is shared:
It stores the answer found by any recursive call.

If no successor:
return -1

Brute Force:
Store complete inorder array
O(n) space    

Optimized:
Track only prev and curr
O(h) recursion space

Time:
O(n)

Space:
O(h)

One-Line Pattern:
Inorder Successor = Inorder Traversal + Track Previous Node + Current Node After `k` Is the Successor.
```