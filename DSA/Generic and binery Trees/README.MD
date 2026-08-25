````markdown
# 🌳 Trees in Python — Generic & Binary Trees

This README covers the **Generic Tree** and **Binary Tree** concepts required for DSA, problem solving, practical understanding, and interviews.

It focuses on:
- Core concepts
- Python implementation
- Tree representation
- DFS/BFS
- Recursive and iterative traversal
- Important problem-solving patterns
- Common interview problems
- Complexity analysis

It does **not** cover BST, Heap, Trie, or advanced specialized trees.

---

# 1. What is a Tree?

A **Tree** is a non-linear hierarchical data structure made up of nodes connected by edges.

Example:

```text
            1
          / | \
         2  3  4
        / \
       5   6
```

A tree has:

- **Nodes** → store data
- **Edges** → connect nodes
- **Root** → topmost node
- **Parent** → node directly above another node
- **Child** → node directly below another node
- **Leaf** → node with no children

### Important Properties

For a tree containing `n` nodes:

```text
Number of edges = n - 1
```

A tree:

- Has exactly one root.
- Has no cycles.
- Has exactly one path between any two nodes.

---

# 2. Tree Terminology

Consider:

```text
            1
          / | \
         2  3  4
        / \
       5   6
```

### Root

The topmost node.

```text
Root = 1
```

### Parent

A node directly connected above another node.

```text
Parent of 5 = 2
```

### Child

A node directly connected below another node.

```text
Children of 2 = 5, 6
```

### Siblings

Nodes having the same parent.

```text
5 and 6 are siblings
```

### Leaf Node

A node with no children.

```text
3, 4, 5, 6
```

### Internal Node

A node having at least one child.

```text
1, 2
```

### Edge

The connection between two nodes.

```text
1 → 2
1 → 3
```

### Subtree

A node together with all of its descendants.

For node `2`:

```text
      2
     / \
    5   6
```

This is a subtree.

---

# 3. Depth

**Depth of a node** = number of edges from the root to that node.

```text
            1
           /
          2
         /
        4
```

```text
depth(1) = 0
depth(2) = 1
depth(4) = 2
```

---

# 4. Height

**Height of a node** = number of edges in the longest path from that node to a leaf.

```text
            1
           /
          2
         / \
        4   5
```

```text
height(4) = 0
height(5) = 0
height(2) = 1
height(1) = 2
```

> Some problems define height in terms of nodes instead of edges. Always follow the definition given in the problem.

---

# 5. Generic Tree

A **Generic Tree** is a tree where a node can have any number of children.

Example:

```text
            1
        /   |   \
       2    3    4
      / \        |
     5   6       7
```

Here:

```text
1 → 3 children
2 → 2 children
4 → 1 child
5 → 0 children
```

There is no fixed limit on the number of children.

---

# 6. Generic Tree Node in Python

A common representation:

```python
class Node:

    def __init__(self, val=0):
        self.val = val
        self.children = []
```

Create a tree:

```python
root = Node(1)

root.children.append(Node(2))
root.children.append(Node(3))
root.children.append(Node(4))

root.children[0].children.append(Node(5))
root.children[0].children.append(Node(6))
```

Result:

```text
            1
        /   |   \
       2    3    4
      / \
     5   6
```

---

# 7. Generic Tree Traversal

The two main traversal techniques are:

```text
DFS → Depth First Search
BFS → Breadth First Search
```

For Generic Trees, DFS is usually implemented recursively because every node has a list of children.

---

# 8. Generic Tree DFS

Basic pattern:

```python
def dfs(node):

    if node is None:
        return

    # Process current node

    for child in node.children:
        dfs(child)
```

The pattern is:

```text
Process current node
        ↓
Visit every child
        ↓
Recursively process each child
```

---

# 9. Generic Tree Preorder

Preorder means:

```text
Root → Children
```

Example:

```text
            1
        /   |   \
       2    3    4
      / \
     5   6
```

Output:

```text
1 2 5 6 3 4
```

Implementation:

```python
def preorder(root):

    if root is None:
        return

    print(root.val)

    for child in root.children:
        preorder(child)
```

---

# 10. Generic Tree Postorder

Postorder means:

```text
Children → Root
```

Example:

```text
            1
        /   |   \
       2    3    4
      / \
     5   6
```

Output:

```text
5 6 2 3 4 1
```

Implementation:

```python
def postorder(root):

    if root is None:
        return

    for child in root.children:
        postorder(child)

    print(root.val)
```

### When is Postorder Useful?

When the current node depends on information calculated from its children.

Examples:

- Height
- Subtree sum
- Number of nodes
- Tree DP

---

# 11. Generic Tree BFS

BFS visits nodes level by level.

Use `deque`:

```python
from collections import deque
```

Implementation:

```python
def bfs(root):

    if root is None:
        return

    q = deque([root])

    while q:

        node = q.popleft()

        print(node.val)

        for child in node.children:
            q.append(child)
```

For:

```text
            1
        /   |   \
       2    3    4
      / \
     5   6
```

Output:

```text
1 2 3 4 5 6
```

---

# 12. Generic Tree Level Order

If the problem requires nodes grouped by levels:

```python
from collections import deque

def levelOrder(root):

    if root is None:
        return []

    q = deque([root])
    result = []

    while q:

        level = []

        for _ in range(len(q)):

            node = q.popleft()

            level.append(node.val)

            for child in node.children:
                q.append(child)

        result.append(level)

    return result
```

Output:

```python
[
    [1],
    [2, 3, 4],
    [5, 6]
]
```

### Important Pattern

```python
for _ in range(len(q)):
```

processes exactly one tree level.

This same pattern is heavily used in Binary Tree BFS problems.

---

# 13. Generic Tree Height

If height is measured in **number of nodes**:

```python
def height(root):

    if root is None:
        return 0

    max_height = 0

    for child in root.children:
        max_height = max(max_height, height(child))

    return 1 + max_height
```

If height is measured in **edges**:

```python
def height(root):

    if root is None:
        return -1

    max_height = -1

    for child in root.children:
        max_height = max(max_height, height(child))

    return 1 + max_height
```

---

# 14. Generic Tree Count Nodes

```python
def countNodes(root):

    if root is None:
        return 0

    count = 1

    for child in root.children:
        count += countNodes(child)

    return count
```

Pattern:

```text
Current node
+
All child subtree counts
```

---

# 15. Generic Tree Sum

```python
def treeSum(root):

    if root is None:
        return 0

    total = root.val

    for child in root.children:
        total += treeSum(child)

    return total
```

---

# 16. Generic Tree Search

A Generic Tree has no ordering property, so search may require visiting every node.

```python
def search(root, target):

    if root is None:
        return False

    if root.val == target:
        return True

    for child in root.children:

        if search(child, target):
            return True

    return False
```

Complexity:

```text
Time: O(n)
Space: O(h)
```

---

# 17. Generic Tree Recursive Pattern

The most important Generic Tree template:

```python
def dfs(node):

    if node is None:
        return

    # Process node

    for child in node.children:
        dfs(child)
```

When solving a problem, identify:

```text
1. What should happen at the current node?
2. What information should come from each child?
3. What should this function return?
```

---

# 18. Binary Tree

A **Binary Tree** is a tree where every node has at most two children.

The children are specifically:

```text
Left Child
Right Child
```

Example:

```text
        1
       / \
      2   3
     / \
    4   5
```

A node can have:

```text
0 children
1 child
2 children
```

but never more than 2.

---

# 19. Binary Tree Node in Python

Standard representation:

```python
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

Create a tree:

```python
root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
```

Result:

```text
        1
       / \
      2   3
     / \
    4   5
```

---

# 20. Types of Binary Trees

These are important for DSA and interviews.

---

## Full Binary Tree

Every node has either:

```text
0 children
OR
2 children
```

Example:

```text
        1
       / \
      2   3
     / \
    4   5
```

No node has exactly one child.

---

## Complete Binary Tree

All levels are completely filled except possibly the last.

The last level is filled:

```text
Left → Right
```

Example:

```text
        1
       / \
      2   3
     / \  /
    4  5 6
```

This concept becomes important when learning:

```text
Heap
Priority Queue
```

---

## Perfect Binary Tree

Every internal node has exactly two children and all leaves are at the same level.

Example:

```text
          1
        /   \
       2     3
      / \   / \
     4   5 6   7
```

For height `h`:

```text
Number of nodes = 2^(h + 1) - 1
```

---

## Balanced Binary Tree

A Binary Tree is balanced when the heights of left and right subtrees remain sufficiently close.

Common definition:

```text
abs(height(left) - height(right)) <= 1
```

for every node.

A balanced tree generally has:

```text
Height = O(log n)
```

---

## Skewed Binary Tree

Every node has only one child.

Example:

```text
1
 \
  2
   \
    3
     \
      4
```

Height:

```text
O(n)
```

A skewed tree behaves similarly to a linked list.

---

# 21. Binary Tree Traversals

The four fundamental Binary Tree traversals are:

```text
1. Preorder
2. Inorder
3. Postorder
4. Level Order
```

First three:

```text
DFS
```

Last one:

```text
BFS
```

---

# 22. Preorder Traversal

Order:

```text
Root → Left → Right
```

Example:

```text
        1
       / \
      2   3
     / \
    4   5
```

Output:

```text
1 2 4 5 3
```

Recursive:

```python
def preorder(root):

    if root is None:
        return

    print(root.val)

    preorder(root.left)
    preorder(root.right)
```

---

# 23. Inorder Traversal

Order:

```text
Left → Root → Right
```

Example:

```text
        1
       / \
      2   3
     / \
    4   5
```

Output:

```text
4 2 5 1 3
```

Recursive:

```python
def inorder(root):

    if root is None:
        return

    inorder(root.left)

    print(root.val)

    inorder(root.right)
```

### Important Interview Fact

For a **Binary Search Tree**:

```text
Inorder Traversal = Sorted Order
```

This becomes very important when learning BST.

---

# 24. Postorder Traversal

Order:

```text
Left → Right → Root
```

Example:

```text
        1
       / \
      2   3
     / \
    4   5
```

Output:

```text
4 5 2 3 1
```

Recursive:

```python
def postorder(root):

    if root is None:
        return

    postorder(root.left)
    postorder(root.right)

    print(root.val)
```

### When is Postorder Useful?

When the current node requires information from both children.

Examples:

- Height
- Diameter
- Balanced Tree
- Maximum Path Sum
- Subtree calculations

---

# 25. Level Order Traversal

Level Order = BFS.

Example:

```text
        1
       / \
      2   3
     / \
    4   5
```

Output:

```text
[
    [1],
    [2, 3],
    [4, 5]
]
```

Implementation:

```python
from collections import deque

def levelOrder(root):

    if root is None:
        return []

    q = deque([root])
    result = []

    while q:

        level = []

        for _ in range(len(q)):

            node = q.popleft()

            level.append(node.val)

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

        result.append(level)

    return result
```

---

# 26. Why `len(q)` Matters in BFS

At the beginning of:

```python
for _ in range(len(q)):
```

the queue contains exactly the nodes of the current level.

Example:

```text
        1          ← Level 0
       / \
      2   3        ← Level 1
     / \
    4   5          ← Level 2
```

Queue progression:

```text
[1]

[2, 3]

[4, 5]
```

This pattern is essential for:

- Level Order
- Zigzag Traversal
- Right View
- Left View
- Minimum Depth
- Level-based problems

---

# 27. Recursive Binary Tree Template

Most Binary Tree recursive problems can start with:

```python
def dfs(root):

    if root is None:
        return ...

    left = dfs(root.left)
    right = dfs(root.right)

    # Process current node

    return ...
```

The most important question is:

```text
What should dfs(root) return?
```

---

# 28. Three Questions for Tree Recursion

Whenever you see a recursive tree problem:

### 1. What is the base case?

Usually:

```python
if root is None:
```

### 2. What information do I get from children?

```python
left = dfs(root.left)
right = dfs(root.right)
```

### 3. What should I return to my parent?

```python
return ...
```

This is the foundation of most recursive Binary Tree problems.

---

# 29. Maximum Depth / Height

```python
def maxDepth(root):

    if root is None:
        return 0

    left = maxDepth(root.left)
    right = maxDepth(root.right)

    return 1 + max(left, right)
```

Logic:

```text
Height(current)
=
1 + max(left height, right height)
```

Complexity:

```text
Time: O(n)
Space: O(h)
```

---

# 30. Minimum Depth

Minimum depth is the shortest path from root to a **leaf**.

Important:

A missing child is not automatically a leaf.

```python
def minDepth(root):

    if root is None:
        return 0

    if root.left is None:
        return 1 + minDepth(root.right)

    if root.right is None:
        return 1 + minDepth(root.left)

    return 1 + min(
        minDepth(root.left),
        minDepth(root.right)
    )
```

---

# 31. Count Nodes

```python
def countNodes(root):

    if root is None:
        return 0

    return (
        1
        + countNodes(root.left)
        + countNodes(root.right)
    )
```

Pattern:

```text
Current node
+
Left subtree
+
Right subtree
```

---

# 32. Sum of Nodes

```python
def treeSum(root):

    if root is None:
        return 0

    return (
        root.val
        + treeSum(root.left)
        + treeSum(root.right)
    )
```

---

# 33. Maximum Value

```python
def maxValue(root):

    if root is None:
        return float("-inf")

    left = maxValue(root.left)
    right = maxValue(root.right)

    return max(root.val, left, right)
```

---

# 34. Search in Binary Tree

A normal Binary Tree has no ordering property.

Therefore, both subtrees may need to be searched.

```python
def search(root, target):

    if root is None:
        return False

    if root.val == target:
        return True

    return (
        search(root.left, target)
        or
        search(root.right, target)
    )
```

Complexity:

```text
Time: O(n)
Space: O(h)
```

---

# 35. Same Binary Tree

Two Binary Trees are the same if:

1. Their structures are the same.
2. Corresponding node values are the same.

```python
def isSameTree(p, q):

    if p is None and q is None:
        return True

    if p is None or q is None:
        return False

    if p.val != q.val:
        return False

    return (
        isSameTree(p.left, q.left)
        and
        isSameTree(p.right, q.right)
    )
```

---

# 36. Invert Binary Tree

Swap left and right children at every node.

```python
def invertTree(root):

    if root is None:
        return None

    root.left, root.right = root.right, root.left

    invertTree(root.left)
    invertTree(root.right)

    return root
```

Core idea:

```text
Swap
↓
Solve left
↓
Solve right
```

---

# 37. Symmetric Binary Tree

A tree is symmetric if its left and right subtrees are mirror images.

```python
def isSymmetric(root):

    def mirror(left, right):

        if left is None and right is None:
            return True

        if left is None or right is None:
            return False

        if left.val != right.val:
            return False

        return (
            mirror(left.left, right.right)
            and
            mirror(left.right, right.left)
        )

    return mirror(root.left, root.right)
```

Important comparison:

```text
left.left  ↔ right.right
left.right ↔ right.left
```

---

# 38. Root-to-Leaf Path

Many tree problems require maintaining the current path.

```python
def dfs(node, path):

    if node is None:
        return

    path.append(node.val)

    if node.left is None and node.right is None:
        # Current path is a root-to-leaf path
        print(path)

    dfs(node.left, path)
    dfs(node.right, path)

    path.pop()
```

This introduces the concept of:

```text
Backtracking
```

---

# 39. Backtracking on Trees

The general pattern:

```python
path.append(node.val)

# Explore

dfs(node.left, path)
dfs(node.right, path)

path.pop()
```

Meaning:

```text
Choose
↓
Explore
↓
Undo
```

This pattern is important for:

- Root-to-leaf paths
- Path Sum II
- All paths
- Path construction

---

# 40. Path Sum

Check whether a root-to-leaf path has a target sum.

```python
def hasPathSum(root, targetSum):

    if root is None:
        return False

    if root.left is None and root.right is None:
        return root.val == targetSum

    remaining = targetSum - root.val

    return (
        hasPathSum(root.left, remaining)
        or
        hasPathSum(root.right, remaining)
    )
```

---

# 41. Iterative Preorder

Preorder:

```text
Root → Left → Right
```

Use a stack.

```python
def preorder(root):

    if root is None:
        return []

    stack = [root]
    result = []

    while stack:

        node = stack.pop()

        result.append(node.val)

        # Push right first
        if node.right:
            stack.append(node.right)

        # Push left second
        if node.left:
            stack.append(node.left)

    return result
```

Why push right first?

Because the stack is LIFO.

```text
Push: Right
Push: Left

Pop: Left
```

Therefore Left is processed before Right.

---

# 42. Iterative Inorder

Inorder:

```text
Left → Root → Right
```

```python
def inorder(root):

    stack = []
    result = []
    curr = root

    while curr or stack:

        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()

        result.append(curr.val)

        curr = curr.right

    return result
```

### Key Idea

Keep moving left:

```text
Root
 ↓
Left
 ↓
Left
 ↓
...
```

Then process nodes while moving back up.

---

# 43. Iterative Postorder

One easy approach uses two stacks:

```python
def postorder(root):

    if root is None:
        return []

    stack1 = [root]
    stack2 = []
    result = []

    while stack1:

        node = stack1.pop()
        stack2.append(node)

        if node.left:
            stack1.append(node.left)

        if node.right:
            stack1.append(node.right)

    while stack2:
        result.append(stack2.pop().val)

    return result
```

Concept:

```text
Root → Right → Left
```

Reverse:

```text
Left → Right → Root
```

---

# 44. DFS vs BFS

| DFS | BFS |
|---|---|
| Depth First Search | Breadth First Search |
| Recursion / Stack | Queue |
| Goes deep first | Goes level by level |
| Preorder | Level Order |
| Inorder | |
| Postorder | |
| Useful for subtree problems | Useful for level problems |

---

# 45. Recursive DFS vs Iterative DFS

Recursive DFS uses the:

```text
Call Stack
```

Iterative DFS uses:

```text
Explicit Stack
```

Recursive:

```python
def dfs(root):

    if root is None:
        return

    dfs(root.left)
    dfs(root.right)
```

Iterative:

```python
stack = [root]

while stack:

    node = stack.pop()

    # Process node
```

Both are DFS.

---

# 46. Tree Traversal Complexity

For all standard traversals:

```text
Time = O(n)
```

because every node is visited once.

### Recursive DFS

```text
Space = O(h)
```

where `h` = height of tree.

Balanced tree:

```text
O(log n)
```

Skewed tree:

```text
O(n)
```

### BFS

```text
Space = O(w)
```

where `w` = maximum width of the tree.

Worst case:

```text
O(n)
```

---

# 47. Bottom-Up Tree Recursion

Many important tree problems are solved bottom-up.

Concept:

```text
            Current
           /       \
       Left         Right
        ↓             ↓
     answer         answer
        \             /
          combine
             ↓
       current answer
```

Template:

```python
def dfs(node):

    if node is None:
        return base_case

    left = dfs(node.left)
    right = dfs(node.right)

    return combine(left, right)
```

Common problems:

- Height
- Diameter
- Balanced Tree
- Maximum Path Sum
- Subtree calculations

---

# 48. Top-Down Tree Recursion

Sometimes information flows from parent to child.

Example:

```python
def dfs(node, current_sum):

    if node is None:
        return

    current_sum += node.val

    dfs(node.left, current_sum)
    dfs(node.right, current_sum)
```

Common uses:

- Root-to-leaf sum
- Depth tracking
- Path tracking
- Parent-based constraints

---

# 49. Global Answer Pattern

Sometimes the recursive function returns one thing, while the final answer is maintained separately.

Example:

```python
def diameter(root):

    ans = 0

    def height(node):

        nonlocal ans

        if node is None:
            return 0

        left = height(node.left)
        right = height(node.right)

        ans = max(ans, left + right)

        return 1 + max(left, right)

    height(root)

    return ans
```

Here:

```text
height()
```

returns information to the parent.

While:

```text
ans
```

stores the final answer.

This is a very common interview pattern.

---

# 50. Binary Tree Diameter

Diameter = longest path between two nodes.

For every node:

```text
Path through current node
=
left height + right height
```

Pattern:

```python
left = height(node.left)
right = height(node.right)

ans = max(ans, left + right)

return 1 + max(left, right)
```

Important:

```text
Return → Height
Update → Diameter
```

Do not confuse the two.

---

# 51. Balanced Binary Tree

Common condition:

```text
abs(height(left) - height(right)) <= 1
```

for every node.

Efficient implementation:

```python
def isBalanced(root):

    def dfs(node):

        if node is None:
            return 0

        left = dfs(node.left)

        if left == -1:
            return -1

        right = dfs(node.right)

        if right == -1:
            return -1

        if abs(left - right) > 1:
            return -1

        return 1 + max(left, right)

    return dfs(root) != -1
```

Why `-1`?

It means:

```text
This subtree is unbalanced.
```

This avoids recalculating heights.

---

# 52. Important Problem-Solving Patterns

## Pattern 1 — Simple DFS

Use when you simply need to visit nodes.

Examples:

```text
Count
Sum
Search
Maximum value
```

Template:

```python
def dfs(node):

    if node is None:
        return

    # Process node

    dfs(node.left)
    dfs(node.right)
```

---

## Pattern 2 — Return Information from Children

Use when the current node depends on its subtrees.

```python
left = dfs(node.left)
right = dfs(node.right)

return combine(left, right)
```

Examples:

```text
Height
Diameter
Balanced Tree
Subtree Sum
```

---

## Pattern 3 — Pass Information Down

Use when children need information from ancestors.

```python
def dfs(node, state):

    if node is None:
        return

    state = update(state, node)

    dfs(node.left, state)
    dfs(node.right, state)
```

Examples:

```text
Path Sum
Depth
Root-to-leaf constraints
```

---

## Pattern 4 — Backtracking

Use when maintaining a current path/state.

```python
path.append(node.val)

dfs(node.left, path)
dfs(node.right, path)

path.pop()
```

Examples:

```text
All root-to-leaf paths
Path Sum II
Path construction
```

---

## Pattern 5 — BFS by Level

Use when the problem depends on levels.

```python
q = deque([root])

while q:

    for _ in range(len(q)):

        node = q.popleft()

        # Process current level
```

Examples:

```text
Level Order
Zigzag
Right View
Left View
Minimum Depth
```

---

# 53. Common Interview Mistakes

### Mistake 1 — Forgetting Base Case

Always consider:

```python
if root is None:
```

---

### Mistake 2 — Confusing Height and Depth

Remember:

```text
Depth → Root to Node
Height → Node to Deepest Leaf
```

---

### Mistake 3 — Forgetting Both Subtrees

For a normal Binary Tree:

```python
dfs(root.left)
dfs(root.right)
```

may both be required.

---

### Mistake 4 — Forgetting Backtracking

If you do:

```python
path.append(...)
```

remember:

```python
path.pop()
```

---

### Mistake 5 — Recalculating Height

Repeatedly calculating height for every node can result in:

```text
O(n²)
```

Instead calculate subtree information once.

---

### Mistake 6 — Confusing BFS and DFS

BFS:

```python
q.popleft()
```

DFS:

```python
stack.pop()
```

---

### Mistake 7 — Not Defining the Return Value

Before writing recursive code, ask:

```text
What does dfs(node) return?
```

This is one of the most important tree problem-solving questions.

---

# 54. Practical Applications of Trees

Trees are widely used outside DSA problems.

### File Systems

```text
Root
├── Documents
│   ├── Resume.pdf
│   └── Notes.txt
└── Pictures
    ├── photo1.jpg
    └── photo2.jpg
```

### HTML DOM

HTML elements form a tree:

```text
html
├── head
└── body
    ├── div
    └── p
```

### Organization Hierarchy

```text
CEO
├── Manager
│   ├── Employee
│   └── Employee
└── Manager
    └── Employee
```

### Expression Trees

Expressions can be represented as trees.

Example:

```text
        +
       / \
      *   5
     / \
    2   3
```

Represents:

```text
2 * 3 + 5
```

These practical examples help understand why hierarchical data naturally maps to trees.

---

# 55. Generic Tree vs Binary Tree

| Feature | Generic Tree | Binary Tree |
|---|---|---|
| Maximum children | Any number | 2 |
| Children representation | `children` list | `left`, `right` |
| DFS | Preorder/Postorder | Preorder/Inorder/Postorder |
| BFS | Yes | Yes |
| Inorder | Not standard | Yes |
| Common problems | Hierarchy, subtree | Recursion, paths, traversal |

---

# 56. Must-Know Generic Tree Topics

Before moving forward, you should know:

- [ ] Tree terminology
- [ ] Generic Tree representation
- [ ] Generic Tree node implementation
- [ ] DFS
- [ ] Preorder
- [ ] Postorder
- [ ] BFS
- [ ] Level Order
- [ ] Height
- [ ] Count Nodes
- [ ] Sum of Nodes
- [ ] Search
- [ ] Recursive tree pattern
- [ ] Time and space complexity

---

# 57. Must-Know Binary Tree Topics

### Fundamentals

- [ ] Binary Tree
- [ ] TreeNode implementation
- [ ] Full Binary Tree
- [ ] Complete Binary Tree
- [ ] Perfect Binary Tree
- [ ] Balanced Binary Tree
- [ ] Skewed Binary Tree
- [ ] Height
- [ ] Depth

### Traversals

- [ ] Recursive Preorder
- [ ] Recursive Inorder
- [ ] Recursive Postorder
- [ ] Iterative Preorder
- [ ] Iterative Inorder
- [ ] Iterative Postorder
- [ ] Level Order
- [ ] BFS

### Basic Problems

- [ ] Maximum Depth
- [ ] Minimum Depth
- [ ] Count Nodes
- [ ] Sum of Nodes
- [ ] Maximum Value
- [ ] Search
- [ ] Same Tree
- [ ] Invert Tree
- [ ] Symmetric Tree

### Problem-Solving Patterns

- [ ] Bottom-up DFS
- [ ] Top-down DFS
- [ ] Backtracking
- [ ] Global answer
- [ ] Path problems
- [ ] BFS by level

### Interview Problems

- [ ] Root-to-Leaf Paths
- [ ] Path Sum
- [ ] Diameter
- [ ] Balanced Binary Tree
- [ ] Level Order Traversal
- [ ] Zigzag Level Order
- [ ] Iterative Traversals

---

# 58. Interview Questions You Should Be Able to Answer

You should be able to explain:

```text
1. What is a Tree?

2. What is a Binary Tree?

3. Generic Tree vs Binary Tree?

4. What are root, parent, child, leaf and sibling?

5. What is depth?

6. What is height?

7. Full vs Complete vs Perfect Binary Tree?

8. What is a balanced tree?

9. What is a skewed tree?

10. DFS vs BFS?

11. Preorder vs Inorder vs Postorder?

12. Why does inorder matter?

13. How do you implement level-order traversal?

14. Why do we use deque for BFS?

15. What is the time complexity of tree traversal?

16. What is the space complexity of recursive DFS?

17. When should you use preorder?

18. When should you use postorder?

19. How do you solve tree problems using bottom-up recursion?

20. How do you pass information from parent to child?

21. How does backtracking work on trees?

22. How do you calculate tree height?

23. How do you find the diameter?

24. How do you check whether a tree is balanced?

25. What should a recursive DFS function return?
```

---

# 59. Problem-Solving Checklist

When you get a Tree problem, go through this checklist:

```text
Step 1:
Identify the tree type.

        ↓

Generic Tree?
Binary Tree?

        ↓

Step 2:
Decide DFS or BFS.

        ↓

Step 3:
If DFS:

Preorder?
Inorder?
Postorder?

        ↓

Step 4:
Ask:

Does the current node need information
from its children?

        ↓

YES → Bottom-Up DFS

        ↓

Step 5:
Does the child need information
from its parent?

        ↓

YES → Top-Down DFS

        ↓

Step 6:
Do I need to maintain a path?

        ↓

YES → Backtracking

        ↓

Step 7:
Does the problem depend on levels?

        ↓

YES → BFS

        ↓

Step 8:
What should dfs(node) return?

        ↓

Step 9:
Calculate Time + Space Complexity
```

---

# 60. Core Templates to Memorize

## Generic Tree DFS

```python
def dfs(node):

    if node is None:
        return

    # Process node

    for child in node.children:
        dfs(child)
```

---

## Generic Tree BFS

```python
from collections import deque

def bfs(root):

    if root is None:
        return

    q = deque([root])

    while q:

        node = q.popleft()

        # Process node

        for child in node.children:
            q.append(child)
```

---

## Binary Tree DFS

```python
def dfs(root):

    if root is None:
        return ...

    left = dfs(root.left)
    right = dfs(root.right)

    # Process root

    return ...
```

---

## Binary Tree BFS

```python
from collections import deque

def bfs(root):

    if root is None:
        return

    q = deque([root])

    while q:

        for _ in range(len(q)):

            node = q.popleft()

            # Process node

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)
```

---

## Binary Tree Backtracking

```python
def dfs(node, path):

    if node is None:
        return

    path.append(node.val)

    dfs(node.left, path)
    dfs(node.right, path)

    path.pop()
```

---

# 61. Recommended Learning Order

Follow this order:

```text
Generic Tree
    ↓
Tree Terminology
    ↓
Generic Tree Representation
    ↓
Generic Tree DFS
    ↓
Generic Tree BFS
    ↓
Height / Count / Sum / Search
    ↓
Binary Tree
    ↓
Binary Tree Representation
    ↓
Tree Types
    ↓
Recursive DFS
    ↓
Preorder
    ↓
Inorder
    ↓
Postorder
    ↓
Level Order / BFS
    ↓
Iterative Traversals
    ↓
Height / Depth
    ↓
Basic Tree Problems
    ↓
Path Problems
    ↓
Backtracking
    ↓
Bottom-Up Recursion
    ↓
Top-Down Recursion
    ↓
Diameter
    ↓
Balanced Tree
```

After these concepts are strong, move to:

```text
Binary Search Tree
```

---

# 62. Final Takeaways

The most important things to master are:

```text
Tree Structure
      ↓
TreeNode Representation
      ↓
DFS / BFS
      ↓
Preorder / Inorder / Postorder
      ↓
Level Order
      ↓
Recursion
      ↓
Bottom-Up
      ↓
Top-Down
      ↓
Backtracking
      ↓
Path Problems
      ↓
Tree Properties
      ↓
Diameter / Balanced Tree
```

The goal is **not** to memorize individual solutions.

The key skill is to recognize the pattern:

```text
"What information does the current node
need from its children?"
```

and:

```text
"What information does the child
need from its parent?"
```

Once you can answer these questions, most Generic Tree and Binary Tree problems can be approached using a small number of reusable patterns.

---

# 🎯 Generic & Binary Tree Completion Checklist

- [ ] Understand Tree terminology
- [ ] Understand Generic Trees
- [ ] Implement Generic Tree Node
- [ ] Generic Tree DFS
- [ ] Generic Tree BFS
- [ ] Generic Tree Preorder
- [ ] Generic Tree Postorder
- [ ] Generic Tree Level Order
- [ ] Generic Tree Height
- [ ] Generic Tree Count
- [ ] Generic Tree Sum
- [ ] Generic Tree Search
- [ ] Understand Binary Trees
- [ ] Implement Binary Tree Node
- [ ] Full Binary Tree
- [ ] Complete Binary Tree
- [ ] Perfect Binary Tree
- [ ] Balanced Binary Tree
- [ ] Skewed Binary Tree
- [ ] Recursive Preorder
- [ ] Recursive Inorder
- [ ] Recursive Postorder
- [ ] Iterative Preorder
- [ ] Iterative Inorder
- [ ] Iterative Postorder
- [ ] Level Order BFS
- [ ] Maximum Depth
- [ ] Minimum Depth
- [ ] Count Nodes
- [ ] Sum of Nodes
- [ ] Search
- [ ] Same Tree
- [ ] Invert Tree
- [ ] Symmetric Tree
- [ ] Root-to-Leaf Paths
- [ ] Path Sum
- [ ] Backtracking
- [ ] Bottom-Up DFS
- [ ] Top-Down DFS
- [ ] Diameter
- [ ] Balanced Tree
- [ ] Understand DFS vs BFS complexity
- [ ] Understand recursion space complexity
- [ ] Recognize common tree problem patterns
- [ ] Explain tree concepts in an interview
````
