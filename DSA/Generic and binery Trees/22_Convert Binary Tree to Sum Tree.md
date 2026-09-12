# Convert Binary Tree to Sum Tree

## 1. Problem

Given a binary tree, convert it into a **Sum Tree**.

For every node:

```text
New value of node
=
sum of all values in its left subtree
+
sum of all values in its right subtree
```

The node's **own original value is not included** in its new value.

For a leaf node:

```text
New value = 0
```

because it has no left or right subtree.

### Example

Original Tree:

```text
        10
       /  \
      20   30
     /  \
    5    5
```

After conversion:

```text
        60
       /  \
      10    0
     /  \
    0    0
```

Why?

For node `20`:

```text
left subtree  = 5
right subtree = 5

new value = 5 + 5 = 10
```

For node `10`:

```text
left subtree  = 20 + 5 + 5 = 30
right subtree = 30

new value = 30 + 30 = 60
```

---

# 2. Brute Force

A straightforward approach is:

For every node:

1. Calculate the sum of its left subtree.
2. Calculate the sum of its right subtree.
3. Replace the node's value with `leftSum + rightSum`.

The problem is that calculating subtree sums repeatedly causes the same nodes to be visited multiple times.

### Example

For the root, we calculate:

```text
sum(left subtree)
sum(right subtree)
```

Then while calculating the left subtree, we again calculate its children.

This repeated work can make the solution **O(n²)** in the worst case, especially for a skewed tree.

### Complexity

```text
Time  → O(n²) worst case
Space → O(h)
```

where `h` is the height of the tree.

---

# 3. Pattern

This is a **Binary Tree DFS + Postorder Recursion** problem.

Think:

```text
Tree
 ↓
DFS
 ↓
Left
 ↓
Right
 ↓
Current Node
```

Why postorder?

Because to calculate the new value of a node, we first need:

```text
left subtree sum
right subtree sum
```

So the children must be processed before the current node.

---

# 4. Main Idea

The important trick is:

> The recursive function does TWO jobs at the same time.

It:

1. **Modifies the current node** to its Sum Tree value.
2. **Returns the original sum of the current subtree** to its parent.

This is the key idea behind the solution.

---

# 5. What Does `Sum()` Return?

Consider:

```text
        10
       /  \
      20   30
```

Suppose `Sum(20)` changes `20` to `0`.

The parent still needs to know:

```text
What was the original sum of the subtree rooted at 20?
```

That value is:

```text
20
```

So the recursive function cannot simply return the new node value.

It must return the **original subtree sum**.

---

# 6. How Does the Function Do Two Jobs?

Look at:

```python
lSum = self.Sum(root.left)
rSum = self.Sum(root.right)

temp = root.data

root.data = lSum + rSum

return temp + root.data
```

### Step 1: Get left subtree's original sum

```python
lSum = self.Sum(root.left)
```

---

### Step 2: Get right subtree's original sum

```python
rSum = self.Sum(root.right)
```

---

### Step 3: Save the original value

```python
temp = root.data
```

This is important because we are about to modify `root.data`.

---

### Step 4: Convert current node

```python
root.data = lSum + rSum
```

The node now contains:

```text
left subtree sum + right subtree sum
```

---

### Step 5: Return original subtree sum

```python
return temp + root.data
```

Since:

```text
root.data = leftSum + rightSum
```

we get:

```text
temp + root.data
=
original node value
+ left subtree sum
+ right subtree sum
```

Therefore:

```text
return value = original sum of the entire subtree
```

This is exactly what the parent needs.

---

# 7. Why Do We Need `temp`?

Suppose:

```text
root.data = 10
```

Then we do:

```python
root.data = lSum + rSum
```

The original `10` is lost.

But the parent needs the original subtree sum.

Therefore:

```python
temp = root.data
```

must happen **before** modifying the node.

Think:

```text
Save old value
      ↓
Calculate new value
      ↓
Update node
      ↓
Return old subtree sum
```

---

# 8. Base Cases

### Case 1: Empty Node

```python
if root is None:
    return 0
```

An empty subtree has sum:

```text
0
```

---

### Case 2: Leaf Node

```python
if root.left is None and root.right is None:
    temp = root.data
    root.data = 0
    return temp
```

A leaf has no children.

Therefore:

```text
new value = 0
```

But we still return its original value because its parent needs it.

For example:

```text
    5
```

After conversion:

```text
    0
```

but:

```text
Sum(5) returns 5
```

This allows the parent to use `5` in its calculation.

---

# 9. Complete Code

```python
''' Structure for Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:

    def Sum(self, root):
        # Empty subtree
        if root is None:
            return 0

        # Leaf node
        if root.left is None and root.right is None:
            temp = root.data

            # Leaf becomes 0 in Sum Tree
            root.data = 0

            # Return original value to parent
            return temp

        # Get original sum of left subtree
        lSum = self.Sum(root.left)

        # Get original sum of right subtree
        rSum = self.Sum(root.right)

        # Save original value before modifying it
        temp = root.data

        # Convert current node to Sum Tree value
        root.data = lSum + rSum

        # Return original sum of current subtree
        return temp + root.data

    def toSumTree(self, root):
        self.Sum(root)
```

---

# 10. Dry Run

Consider:

```text
        10
       /  \
      20   30
     /  \
    5    5
```

We start:

```python
self.Sum(10)
```

Because `10` is not a leaf, go left.

---

### Node `5`

```text
5 is a leaf
```

Save:

```python
temp = 5
```

Convert:

```text
5 → 0
```

Return:

```text
5
```

So parent `20` receives:

```text
lSum = 5
```

---

### Other Node `5`

Same process:

```text
5 → 0
```

Return:

```text
5
```

So:

```text
rSum = 5
```

---

### Node `20`

Now:

```text
lSum = 5
rSum = 5
```

Save original value:

```python
temp = 20
```

Convert:

```python
root.data = 5 + 5
```

Therefore:

```text
20 → 10
```

Return:

```text
temp + root.data
= 20 + 10
= 30
```

So the parent receives:

```text
30
```

This represents the original sum:

```text
20 + 5 + 5 = 30
```

---

### Node `30`

`30` is a leaf.

So:

```text
30 → 0
```

and returns:

```text
30
```

---

### Root `10`

Now root receives:

```text
lSum = 30
rSum = 30
```

Save:

```text
temp = 10
```

Convert:

```text
root.data = 30 + 30
          = 60
```

So:

```text
10 → 60
```

Return:

```text
10 + 60 = 70
```

The returned `70` is the original sum of the entire tree:

```text
10 + 20 + 5 + 5 + 30 = 70
```

Final tree:

```text
        60
       /  \
      10    0
     /  \
    0    0
```

---

# 11. Why Is This Postorder?

The order is:

```text
Left
 ↓
Right
 ↓
Root
```

For example:

```text
        10
       /  \
      20   30
```

We cannot calculate the new value of `10` until we know:

```text
sum of 20's subtree
sum of 30's subtree
```

Therefore:

```text
Left subtree
      ↓
Right subtree
      ↓
Current node
```

This is exactly **postorder DFS**.

---

# 12. The Important Recursion Pattern

This problem teaches a very useful pattern:

```text
Recursive Call
      ↓
Get information from left
      ↓
Get information from right
      ↓
Modify current node
      ↓
Return information to parent
```

Here:

```text
Information returned
        ↓
Original subtree sum
```

and:

```text
Modification
        ↓
Left subtree sum + Right subtree sum
```

This pattern is very common in tree problems.

---

# 13. Why We Don't Need a Separate `sum()` Function

We could create separate functions:

```python
getSum(root)
```

and:

```python
convert(root)
```

But that can cause repeated traversal.

Instead, `Sum()` calculates the required information **while performing the conversion**.

So every node is processed only once.

That gives:

```text
O(n)
```

time.

---

# 14. Complexity

Let `n` be the number of nodes and `h` be the height of the tree.

### Time

Every node is visited exactly once.

```text
Time = O(n)
```

### Space

The recursion call stack contains at most `h` nodes.

```text
Space = O(h)
```

For a balanced tree:

```text
h = O(log n)
```

For a skewed tree:

```text
h = O(n)
```

Therefore:

```text
Time  → O(n)
Space → O(h)
```

---

# 15. Common Mistakes

### Mistake 1: Updating the node before saving its original value

Wrong:

```python
root.data = lSum + rSum
temp = root.data
```

Now `temp` contains the **new** value, not the original value.

Correct:

```python
temp = root.data
root.data = lSum + rSum
```

---

### Mistake 2: Returning only `root.data`

After conversion:

```python
root.data
```

is the new Sum Tree value.

But the parent needs the **original subtree sum**.

So we return:

```python
return temp + root.data
```

---

### Mistake 3: Forgetting the leaf case

A leaf must become:

```text
0
```

but its original value must be returned to its parent.

```python
temp = root.data
root.data = 0
return temp
```

---

### Mistake 4: Thinking `return temp + root.data` returns the new value

It does not.

Suppose:

```text
temp = 20
root.data = 10
```

Then:

```text
return 20 + 10 = 30
```

`30` represents:

```text
original sum of the subtree
```

not the value stored in the current node.

---

# 16. Pattern Recognition

When you see a tree problem where:

- child information is required to modify the parent
- the recursive function needs to return some calculated information
- the current node is also being updated

Think:

```text
DFS
 ↓
Postorder
 ↓
Get left information
 ↓
Get right information
 ↓
Modify current node
 ↓
Return information to parent
```

Typical question to ask yourself:

> **"What information does my parent need from me?"**

Here the answer is:

```text
Original sum of my subtree
```

That tells you what `Sum()` should return.

---

# 17. Revision Cheat Sheet

```text
Sum Tree
   ↓
Postorder DFS
   ↓
Process left
   ↓
Process right
   ↓
Save original value
   ↓
root.data = leftSum + rightSum
   ↓
return original subtree sum
```

### Base Cases

```python
if root is None:
    return 0
```

```python
if root.left is None and root.right is None:
    temp = root.data
    root.data = 0
    return temp
```

### Core Logic

```python
lSum = self.Sum(root.left)
rSum = self.Sum(root.right)

temp = root.data

root.data = lSum + rSum

return temp + root.data
```

### Complexity

```text
Time  → O(n)
Space → O(h)
```

---

# 18. Interview Memory Trick

Remember:

> **"Modify the node with child sums, but return the original subtree sum."**

Or:

```text
SAVE → LEFT → RIGHT → UPDATE → RETURN
```

The most important idea is:

```text
Node's NEW value
=
Left ORIGINAL subtree sum
+
Right ORIGINAL subtree sum

Function's RETURN value
=
Current ORIGINAL value
+
Left ORIGINAL subtree sum
+
Right ORIGINAL subtree sum
```

So the function simultaneously:

```text
                Sum()
               /     \
              /       \
     modifies tree   returns original sum
```

This is the core recursion pattern to remember.