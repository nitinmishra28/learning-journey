# Binary Tree Cameras

## Problem

Given a binary tree, place the **minimum number of cameras** so that every node is monitored.

A camera placed at a node can monitor:

```text
1. The node itself
2. Its left child
3. Its right child
4. Its parent
```

Example:

```text
        0
       / \
      0   0
     /
    0
```

We need to place cameras so that every node is covered using the minimum number of cameras.

---

# Brute Force

## Idea

For every node, we could try two possibilities:

```text
1. Place a camera
2. Don't place a camera
```

Then recursively check whether all nodes are covered.

This creates many combinations because each node has two choices.

For `n` nodes, the number of possible camera placements can become exponential:

```text
O(2^n)
```

This is clearly too slow.

We need to make a decision based on the information coming from the children.

---

# Pattern

This problem is a classic:

```text
Binary Tree
     ↓
Postorder DFS
     ↓
Children tell parent their state
     ↓
Parent decides whether camera is needed
```

The key idea is:

> Instead of asking every node whether it should have a camera, let every subtree return its current monitoring state.

We use **3 states**.

---

# Three Node States

Our code uses:

```text
0 → Node needs a camera
1 → Node is covered
2 → Node has a camera
```

This is the most important part of the problem.

---

## State 0 — Node Needs Camera

```text
0
```

means:

> This node is not covered by any camera from its children.

So its parent should put a camera here.

Example:

```text
    parent
       |
       0
```

The child is saying:

```text
"I need a camera."
```

Therefore, the parent should install a camera.

---

## State 1 — Node Is Covered

```text
1
```

means:

> This node is already covered, but it does not have a camera.

For example:

```text
      2
      |
      1
```

The child can be covered by a camera on its parent.

So state `1` basically means:

```text
"I am safe. I don't have a camera."
```

---

## State 2 — Node Has a Camera

```text
2
```

means:

> This node has a camera.

For example:

```text
      2
     📷
```

The camera covers:

```text
parent
node
left child
right child
```

So when a child returns state `2`, its parent is automatically covered.

---

# Why Does `None` Return `1`?

Your code:

```python
if root is None:
    return 1
```

This means:

```text
None → Covered
```

Why?

A `None` node does not need a camera.

Also, treating it as covered makes the parent logic easier.

Consider:

```text
    5
   /
  4
```

For node `4`:

```text
left  = None → 1
right = None → 1
```

So `4` does not need a camera just because its children are missing.

---

# Main Decision Logic

Your code:

```python
if left == 0 or right == 0:
    self.cameras += 1
    return 2
```

means:

> If either child needs a camera, put a camera on the current node.

Why?

Suppose:

```text
        5
       /
      4
     /
    3
```

Node `3` is a leaf.

It returns:

```text
0
```

meaning:

```text
"I need a camera."
```

Then node `4` sees:

```text
left = 0
```

So node `4` places a camera.

```text
        5
       /
      4 📷
     /
    3
```

Now:

- `3` is covered
- `4` has a camera
- `5` is covered by the camera at `4`

This is why we place the camera at the **parent** instead of immediately placing it on the leaf.

---

# Why Do We Place Cameras at Parents?

This is the greedy part.

Suppose:

```text
      P
      |
      C
```

If `C` needs a camera, we could place it on `C`.

But placing it on `P` is better because the camera on `P` can cover:

```text
P
C
P's other child
P's parent
```

So one camera can cover more nodes.

This gives us the greedy rule:

> **If a child needs a camera, place the camera at the parent.**

---

# Second Condition

Your code:

```python
if left == 2 or right == 2:
    return 1
```

means:

> If either child has a camera, the current node is already covered.

For example:

```text
        5
       /
      4 📷
```

The camera on `4` covers `5`.

Therefore `5` returns:

```text
1
```

because:

```text
5 is covered
5 does not have a camera
```

---

# Why Do We Check `left == 0` Before `left == 2`?

Consider:

```text
left == 0
```

The child needs a camera.

Therefore:

```text
Current node must get a camera.
```

But if:

```text
left == 2
```

the child already has a camera.

Therefore:

```text
Current node is already covered.
```

So the priority is:

```text
Child needs camera
        ↓
Place camera here
```

before:

```text
Child has camera
        ↓
Current node is covered
```

---

# Final `return 0`

Your code ends with:

```python
return 0
```

This means:

> The current node is not covered and does not have a camera.

When does this happen?

When:

```text
left = 1
right = 1
```

Both children are covered, but neither child has a camera.

Example:

```text
       5
      / \
     4   6
```

Suppose:

```text
4 → 1
6 → 1
```

Both children are safe.

But they don't have cameras.

So node `5` is not covered by either child.

Therefore:

```text
5 → 0
```

It tells the parent:

```text
"I need you to put a camera on me."
```

---

# Complete State Rules

The entire logic can be remembered as:

```text
Child needs camera?
(left == 0 OR right == 0)
        ↓
YES
        ↓
Put camera here
        ↓
return 2
```

Otherwise:

```text
Child has camera?
(left == 2 OR right == 2)
        ↓
YES
        ↓
Current node is covered
        ↓
return 1
```

Otherwise:

```text
Both children are covered
but neither has a camera
        ↓
Current node is not covered
        ↓
return 0
```

---

# Complete Code

```python
class Solution:

    def solve(self, root):

        # None node is considered covered
        if root is None:
            return 1

        # Get state of left subtree
        left = self.solve(root.left)

        # Get state of right subtree
        right = self.solve(root.right)

        # If any child needs a camera,
        # place a camera at current node
        if left == 0 or right == 0:
            self.cameras += 1
            return 2

        # If any child has a camera,
        # current node is covered
        if left == 2 or right == 2:
            return 1

        # Both children are covered,
        # but neither has a camera.
        # Current node needs a camera.
        return 0

    def minCameraCover(self, root):

        self.cameras = 0

        # Find state of root
        nodeState = self.solve(root)

        # If root itself needs a camera,
        # we must place one here
        if nodeState == 0:
            self.cameras += 1

        return self.cameras
```

---

# Why Do We Check the Root Separately?

This is a very important part:

```python
nodeState = self.solve(root)

if nodeState == 0:
    self.cameras += 1
```

Inside `solve()`, a node can tell its **parent** that it needs a camera.

But the root has no parent.

Consider:

```text
    1
   /
  2
 /
3
```

Processing from bottom:

```text
3 → 0
```

Then:

```text
2 → camera → 2
```

Then:

```text
1 → covered → 1
```

Fine.

But consider:

```text
      1
     / \
    2   3
```

Suppose both children return:

```text
2 → 1
3 → 1
```

Then root `1` returns:

```text
0
```

because:

```text
left = 1
right = 1
```

Root says:

```text
"I need a camera."
```

But there is no parent to install it.

Therefore we must handle it explicitly:

```python
if nodeState == 0:
    self.cameras += 1
```

This is why the root needs a separate check.

---

# Dry Run

Consider:

```text
        0
       / \
      0   0
     /
    0
```

Let's process bottom-up.

---

## Node 4

```text
    0
```

Both children are `None`.

So:

```text
left = 1
right = 1
```

Neither child needs a camera.

Neither child has a camera.

Therefore:

```text
node 4 → state 0
```

Meaning:

```text
"I need a camera."
```

---

## Node 2

```text
      0
     /
    0
```

Left child:

```text
left = 0
```

Therefore:

```python
if left == 0:
```

is true.

Place camera at node `2`.

```text
      0 📷
     /
    0
```

Camera count:

```text
cameras = 1
```

Node `2` returns:

```text
state = 2
```

---

## Node 3

Node `3` is a leaf.

So:

```text
left = 1
right = 1
```

Therefore:

```text
node 3 → 0
```

It needs a camera.

---

## Root

Root receives:

```text
left = 2
right = 0
```

Because:

```text
right == 0
```

we place a camera at root.

```text
        0 📷
       / \
      0   0
     📷
     /
    0
```

Camera count:

```text
cameras = 2
```

Root returns:

```text
2
```

Final answer:

```text
2
```

---

# Why Postorder DFS?

We process:

```text
Left subtree
Right subtree
Current node
```

This is **postorder traversal**.

Why?

Because the parent needs to know what is happening in its children before making its own decision.

Think:

```text
        Parent
        /    \
       L      R
```

Parent asks:

```text
L → What is your state?
R → What is your state?
```

Then parent decides:

```text
Should I install a camera?
Am I already covered?
Do I need my parent to install one?
```

Therefore:

```text
Children first → Parent decision
```

which naturally gives:

```text
Postorder DFS
```

---

# Why Is This Greedy?

The important greedy decision is:

```text
If child needs a camera
        ↓
Put camera on parent
```

We don't put the camera on the child.

Why?

Because a camera on the parent covers:

```text
       Parent 📷
       /      \
    Child    Sibling
       ↑
   also covers
    grandparent
```

So the camera covers more useful positions.

This allows us to achieve the minimum number of cameras.

---

# State Table

This table is the easiest way to revise the problem.

| Left | Right | Current Node |
|---|---|---|
| `0` | anything | Put camera → `2` |
| anything | `0` | Put camera → `2` |
| `2` | anything | Covered → `1` |
| anything | `2` | Covered → `1` |
| `1` | `1` | Needs camera → `0` |

Remember:

```text
0 → NEED CAMERA
1 → COVERED
2 → HAS CAMERA
```

---

# The Most Important Mental Model

Don't think:

> "Should I put a camera on this node?"

Instead think:

> "What state are my children giving me?"

Every child reports one of:

```text
0 → I need a camera
1 → I am covered
2 → I have a camera
```

Then the parent reacts.

```text
        Parent
        /    \
       L      R

       ↓      ↓
      State  State
         \    /
          \  /
           ↓
       Parent decides
```

---

# Complexity

Let:

```text
n = number of nodes
h = height of tree
```

Every node is visited exactly once.

Therefore:

```text
Time = O(n)
```

The recursion call stack can grow up to the height of the tree:

```text
Space = O(h)
```

For a balanced tree:

```text
h = O(log n)
```

For a completely skewed tree:

```text
h = O(n)
```

So worst-case auxiliary space:

```text
O(n)
```

---

# Complexity Comparison

| Approach | Time | Space |
|---|---:|---:|
| Brute Force | O(2^n) | O(h) |
| Greedy Postorder DFS | O(n) | O(h) |

The optimized solution is linear because every node makes one constant-time state decision.

---

# Common Mistakes

## 1. Putting Camera on Every Leaf

This is not optimal.

For:

```text
      1
     /
    2
   /
  3
```

Putting a camera on `3` is unnecessary.

Instead:

```text
      1
     /
    2 📷
   /
  3
```

The camera on `2` covers:

```text
1
2
3
```

with one camera.

---

## 2. Forgetting That Camera Covers the Parent

A camera covers:

```text
parent + current + children
```

This is what makes the greedy strategy work.

---

## 3. Confusing State `1` and State `2`

Remember:

```text
1 = Covered
2 = Camera
```

They are not the same.

A node can be:

```text
covered without having a camera
```

For example, its child might have a camera.

---

## 4. Forgetting Root's Special Case

The root has no parent.

So:

```python
if nodeState == 0:
    self.cameras += 1
```

is necessary.

---

## 5. Using Preorder Instead of Postorder

The parent needs information from its children first.

Therefore:

```text
Left
Right
Root
```

not:

```text
Root
Left
Right
```

So use:

```text
Postorder DFS
```

---

# Pattern Recognition

When you see:

> Place minimum cameras/monitors on a binary tree so every node is covered.

Think:

```text
Binary Tree
     ↓
Postorder DFS
     ↓
Child returns state
     ↓
Parent makes greedy decision
```

Three states:

```text
0 → Needs camera
1 → Covered
2 → Has camera
```

Decision:

```text
Child needs camera
        ↓
Camera here
        ↓
return 2
```

```text
Child has camera
        ↓
Current is covered
        ↓
return 1
```

```text
Both children covered
but no camera
        ↓
Current needs camera
        ↓
return 0
```

---

# Revision Cheat Sheet

```text
Problem:
Minimum cameras to monitor every node.

Camera covers:
Parent + Current + Left + Right

Pattern:
Postorder DFS + Greedy + 3 States

States:
0 → Needs camera
1 → Covered
2 → Has camera

Base Case:
None → 1 (covered)

Decision:

If left == 0 OR right == 0:
    cameras += 1
    return 2

If left == 2 OR right == 2:
    return 1

Otherwise:
    return 0

After DFS:
If root == 0:
    cameras += 1

Why postorder?
Parent needs child states first.

Why greedy?
If child needs camera,
put camera on parent because
it covers child + parent + sibling + grandparent.

Time:
O(n)

Space:
O(h)
```

# One-Line Pattern

> **Use postorder DFS where each node returns `0 = needs camera`, `1 = covered`, or `2 = has camera`; if a child needs a camera, place it on the parent, giving an O(n) greedy solution.**