# Convert Binary Tree to Doubly Linked List

## 1. Problem

Given a Binary Tree, convert it into a **Doubly Linked List (DLL)**.

The nodes of the DLL should follow the **inorder traversal** of the Binary Tree:

```text
Left → Node → Right
```

Each node should have:

```text
left  → previous node
right → next node
```

### Example

Binary Tree:

```text
        10
       /  \
      5    20
     / \   / \
    2   7 15  25
```

Inorder traversal:

```text
2 → 5 → 7 → 10 → 15 → 20 → 25
```

DLL:

```text
None ← 2 ⇄ 5 ⇄ 7 ⇄ 10 ⇄ 15 ⇄ 20 ⇄ 25 → None
```

The first node:

```text
2
```

is the `head` of the DLL.

---

# 2. Brute Force

## Idea

A simple approach is:

1. Perform inorder traversal.
2. Store all nodes in an array/list.
3. Connect consecutive nodes.

Example:

```text
Inorder:

2 → 5 → 7 → 10 → 15 → 20 → 25
```

Then:

```text
nodes[0].right = nodes[1]
nodes[1].left  = nodes[0]

nodes[1].right = nodes[2]
nodes[2].left  = nodes[1]

...
```

### Complexity

```text
Time:  O(n)
Space: O(n)
```

The extra `O(n)` space is required for storing all nodes.

But we can do this **in-place** without storing the nodes in an array.

---

# 3. Optimized Approach

We use:

```text
Reverse Inorder

Right → Node → Left
```

Why?

Normally inorder gives:

```text
Left → Node → Right
```

which gives the DLL from:

```text
Smallest → Largest
```

But if we process:

```text
Right → Node → Left
```

we get:

```text
Largest → Smallest
```

This allows us to maintain a `head` pointer and connect nodes while moving backward.

---

# 4. Main Idea

Consider:

```text
        10
       /  \
      5    20
     / \   / \
    2   7 15  25
```

Reverse inorder:

```text
25 → 20 → 15 → 10 → 7 → 5 → 2
```

We maintain:

```text
head
```

`head` represents the already processed part of the DLL.

Initially:

```text
head = None
```

---

## Process 25

```text
head = None
```

Set:

```python
root.right = head
```

So:

```text
25.right = None
```

Then:

```python
head = root
```

Now:

```text
head → 25
```

---

## Process 20

At this point:

```text
head → 25
```

Set:

```python
root.right = head
```

So:

```text
20.right = 25
```

Then:

```python
head.left = root
```

So:

```text
20 ⇄ 25
```

Finally:

```python
head = root
```

Now:

```text
head → 20
```

The processed DLL is:

```text
20 ⇄ 25
```

where `head` points to `20`.

---

# 5. Complete Code

```python
''' Structure for tree and linked list
class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None
'''

class Solution:

    def solve(self, root, head):

        if root is None:
            return head

        # RNL
        # R
        head = self.solve(root.right, head)

        # Connect current node to already processed nodes
        root.right = head

        # Connect previous node back to current node
        if head is not None:
            head.left = root

        # Current node becomes the new head
        head = root

        # L
        head = self.solve(root.left, head)

        return head

    def treeToDLL(self, root):

        head = None

        head = self.solve(root, head)

        return head
```

---

# 6. The Most Important Part — Why `head = self.solve(...)`?

This is the part that can be confusing.

You might think:

```python
self.solve(root.right, head)
```

is enough.

But it is **not** enough.

Why?

Because `solve()` returns an **updated `head`**.

Example:

```python
head = self.solve(root.right, head)
```

means:

```text
Call solve()
     ↓
solve processes nodes
     ↓
solve returns NEW head
     ↓
store that returned head
```

If you only write:

```python
self.solve(root.right, head)
```

you are ignoring the returned value.

---

# 7. Your One-Line Rule

Remember this:

> **Function agar updated value return kar raha hai, aur tumhe woh updated value aage use karni hai, to usko variable mein assign karna padega.**

Example:

```python
head = self.solve(root.right, head)
```

The function returns:

```text
updated head
```

Therefore we must store it.

---

# 8. What Happens If We Don't Store It?

Suppose we write:

```python
self.solve(root.right, head)

root.right = head
```

The recursive call may have created a new head internally.

But the caller's `head` variable is still pointing to the **old value**.

Remember:

```text
Python variable
      ↓
reference to an object
```

When the recursive function does:

```python
head = root
```

it changes the local variable `head` inside that function call.

It does **not automatically update the caller's local `head` variable**.

Therefore:

```python
head = self.solve(...)
```

is necessary to receive the updated value.

---

# 9. Simple Example of the Same Concept

Consider:

```python
def change(x):
    x = 10
    return x
```

Now:

```python
x = 5

change(x)

print(x)
```

Output:

```text
5
```

Why?

Because we ignored the returned value.

But:

```python
x = change(x)
```

Now:

```text
x = 10
```

Same concept in our tree problem:

```python
head = self.solve(root.right, head)
```

The recursive function gives us a new `head`.

We must capture it.

---

# 10. Why `head` Changes?

This is the most important concept in this problem.

Suppose:

```text
        10
       /  \
      5    20
```

Reverse inorder:

```text
20 → 10 → 5
```

### Initially

```text
head = None
```

### Process 20

```text
20.right = None
head = 20
```

Now:

```text
head → 20
```

### Process 10

```text
10.right = 20
20.left = 10

head = 10
```

Now:

```text
head → 10 ⇄ 20
```

### Process 5

```text
5.right = 10
10.left = 5

head = 5
```

Now:

```text
head → 5 ⇄ 10 ⇄ 20
```

Therefore:

```text
head
```

keeps moving toward the left/smaller nodes.

At the end:

```text
head = smallest node
```

which becomes the DLL head.

---

# 11. Why `root.right = head`?

Suppose the already processed part is:

```text
head → 20 ⇄ 25
```

Now current node is:

```text
15
```

We want:

```text
15 ⇄ 20 ⇄ 25
```

So:

```python
root.right = head
```

creates:

```text
15 → 20
```

---

# 12. Why `head.left = root`?

We also need the reverse connection.

After:

```python
root.right = head
```

we have:

```text
15 → 20
```

But we also need:

```text
20 → 15
```

So:

```python
head.left = root
```

creates:

```text
15 ⇄ 20
```

Therefore these two lines work together:

```python
root.right = head

if head is not None:
    head.left = root
```

---

# 13. Why `head = root`?

After connecting the current node:

```text
current ⇄ old head
```

the current node is now the **first node** of the processed DLL.

Therefore:

```python
head = root
```

Example:

Before:

```text
head
 ↓
20 ⇄ 25
```

Current node:

```text
15
```

After:

```text
head
 ↓
15 ⇄ 20 ⇄ 25
```

So:

```python
head = root
```

moves the head backward.

---

# 14. Why Process Right First?

This is the key trick.

We use:

```text
R → N → L
```

instead of:

```text
L → N → R
```

Because reverse inorder gives:

```text
Largest → Smallest
```

Example:

```text
        10
       /  \
      5    20
```

Reverse inorder:

```text
20 → 10 → 5
```

We can keep attaching the newly visited smaller node in front:

```text
20

10 ⇄ 20

5 ⇄ 10 ⇄ 20
```

At the end:

```text
head = 5
```

which is exactly the DLL head.

---

# 15. Why `head` Is Returned?

At every recursive call:

```python
return head
```

returns the **latest head** to the caller.

This is necessary because `head` changes during recursion.

For example:

```text
solve(20)
    returns 20

solve(10)
    returns 10

solve(5)
    returns 5
```

The returned value keeps propagating back.

Therefore:

```python
head = self.solve(root.right, head)
```

and:

```python
head = self.solve(root.left, head)
```

are both important.

---

# 16. The Two Most Important Assignments

These two lines are easy to miss:

```python
head = self.solve(root.right, head)
```

and:

```python
head = self.solve(root.left, head)
```

Why?

Because:

```text
solve()
```

returns an updated `head`.

So:

```text
Function returns updated value
            ↓
Store it
            ↓
Use updated value further
```

### Rule

```text
If a recursive function returns updated state:

    variable = recursive_call(...)
```

not:

```text
recursive_call(...)
```

if you need that returned state.

---

# 17. Dry Run

Tree:

```text
        10
       /  \
      5    20
     / \   / \
    2   7 15  25
```

Reverse inorder:

```text
25 → 20 → 15 → 10 → 7 → 5 → 2
```

### Step 1 — 25

```text
head = 25
```

```text
25
```

---

### Step 2 — 20

```text
20.right = 25
25.left = 20

head = 20
```

```text
20 ⇄ 25
```

---

### Step 3 — 15

```text
15.right = 20
20.left = 15

head = 15
```

```text
15 ⇄ 20 ⇄ 25
```

---

### Step 4 — 10

```text
10.right = 15
15.left = 10

head = 10
```

```text
10 ⇄ 15 ⇄ 20 ⇄ 25
```

---

### Step 5 — 7

```text
7.right = 10
10.left = 7

head = 7
```

```text
7 ⇄ 10 ⇄ 15 ⇄ 20 ⇄ 25
```

---

### Step 6 — 5

```text
5.right = 7
7.left = 5

head = 5
```

```text
5 ⇄ 7 ⇄ 10 ⇄ 15 ⇄ 20 ⇄ 25
```

---

### Step 7 — 2

```text
2.right = 5
5.left = 2

head = 2
```

Final DLL:

```text
None ← 2 ⇄ 5 ⇄ 7 ⇄ 10 ⇄ 15 ⇄ 20 ⇄ 25 → None
```

Final:

```text
head = 2
```

---

# 18. Complexity

Every node is visited exactly once.

Therefore:

```text
Time = O(n)
```

No extra array/list is used.

The only extra space is the recursion stack:

```text
Space = O(h)
```

where `h` is the height of the tree.

For a balanced tree:

```text
O(h) = O(log n)
```

For a skewed tree:

```text
O(h) = O(n)
```

---

# 19. Common Mistakes

## 1. Forgetting to store the returned head

Wrong:

```python
self.solve(root.right, head)
```

Correct:

```python
head = self.solve(root.right, head)
```

Because `solve()` returns the updated `head`.

---

## 2. Forgetting the second assignment

Wrong:

```python
self.solve(root.left, head)
return head
```

Correct:

```python
head = self.solve(root.left, head)
return head
```

Again, the recursive call can return a new head.

---

## 3. Using normal inorder without changing the logic

Normal inorder:

```text
L → N → R
```

can also be used, but then the pointer logic is usually written differently.

This particular solution is designed around:

```text
R → N → L
```

---

## 4. Forgetting `head.left = root`

If we only write:

```python
root.right = head
```

we create only:

```text
root → head
```

not a proper doubly linked connection.

We need:

```python
head.left = root
```

to create:

```text
root ⇄ head
```

---

## 5. Not checking `head is not None`

Initially:

```text
head = None
```

For the largest node:

```python
head.left = root
```

would cause an error.

Therefore:

```python
if head is not None:
    head.left = root
```

is necessary.

---

# 20. Pattern Recognition

When you see:

```text
Binary Tree
+
Convert to DLL
+
Inorder order required
```

Think:

```text
Reverse Inorder
      ↓
Right → Node → Left
      ↓
Maintain head
      ↓
Connect current node with head
      ↓
Current node becomes new head
```

Core pointer operations:

```python
root.right = head

if head is not None:
    head.left = root

head = root
```

---

# 21. Revision Cheat Sheet

```text
Tree → DLL

Traversal:
R → N → L

Why?
Process largest → smallest.

Maintain:
head = already processed DLL head

For every node:

1. Process right subtree
   head = solve(root.right, head)

2. Connect current node:
   root.right = head

3. Connect backward:
   if head:
       head.left = root

4. Current becomes new head:
   head = root

5. Process left subtree:
   head = solve(root.left, head)

6. Return:
   return head
```

### Most Important Rule

```text
If recursive function returns updated value:

    head = self.solve(...)

Don't ignore the returned value.
```

### Complexity

```text
Time  = O(n)
Space = O(h)
```

> **One-Line Pattern: Tree to DLL = Reverse Inorder (RNL) + Maintain `head` + Connect `current ⇄ head` + Return the updated `head`.**