# Vertical Order Traversal of a Binary Tree

## 1. Problem

Given a binary tree, return its **vertical order traversal**.

For every node, we track:

```text
row → vertical level / depth
col → vertical column
```

Movement rules:

```text
Left child  → row + 1, col - 1
Right child → row + 1, col + 1
```

Nodes are returned:

1. From the **leftmost column to the rightmost column**.
2. Inside the same column, from **top to bottom** (`row` increasing).
3. If two nodes have the same row and column, sort them by their **value**.

### Example

```text
        3
       / \
      9   20
         /  \
        15   7
```

Coordinates:

```text
        3
      (0,0)
       /   \
 (1,-1)   (1,1)
   9         20
             / \
        (2,0) (2,2)
         15     7
```

Columns:

```text
Column -1 → [9]
Column  0 → [3, 15]
Column  1 → [20]
Column  2 → [7]
```

Answer:

```text
[
    [9],
    [3, 15],
    [20],
    [7]
]
```

---

# 2. Brute Force

A straightforward approach is to traverse the tree and store every node with its:

```text
(row, column, value)
```

Then:

1. Collect all nodes.
2. Sort them by:
   ```text
   column
   row
   value
   ```
3. Group nodes having the same column.

For example:

```python
nodes = [
    (0, 0, 3),
    (1, -1, 9),
    (1, 1, 20),
    (2, 0, 15),
    (2, 2, 7)
]
```

Then sort:

```text
(column, row, value)
```

and group by column.

### Complexity

If there are `n` nodes:

```text
Traversal → O(n)
Sorting   → O(n log n)

Total     → O(n log n)
Space     → O(n)
```

The sorting step is necessary to establish the required ordering.

---

# 3. Pattern

This is a:

```text
Binary Tree
     ↓
BFS
     ↓
Store (row, column, value)
     ↓
Group by column
     ↓
Sort columns
     ↓
Sort nodes inside each column
```

### One-Line Pattern

> **Vertical Traversal = BFS with `(node, row, col)` + group by column + sort by `(row, value)`.**

---

# 4. Main Idea

The most important part of this problem is assigning coordinates to every node.

Start with the root:

```text
row = 0
col = 0
```

For every node:

```text
Left:
row + 1
col - 1

Right:
row + 1
col + 1
```

So:

```text
             (0,0)
            /     \
       (1,-1)     (1,1)
        /   \       /  \
   (2,-2) (2,0) (2,0) (2,2)
```

The `col` tells us which vertical line the node belongs to.

The `row` tells us its vertical position inside that column.

The `value` is needed for the tie-breaking rule.

Therefore we store:

```python
(row, value)
```

inside:

```python
columns[col]
```

---

# 5. Why Do We Store the Column?

Consider:

```text
        1
       / \
      2   3
       \
        4
```

Coordinates:

```text
        1
      (0,0)
       /   \
   (1,-1) (1,1)
      2      3
       \
       (2,0)
         4
```

Notice:

```text
1 → column 0
4 → column 0
```

Even though they are at different rows, they belong to the same vertical column.

So we need:

```python
columns[0]
```

to contain both.

---

# 6. Why Do We Store the Row?

Suppose the same column contains:

```text
(0, 3)
(2, 15)
(3, 8)
```

We need the nodes from:

```text
top → bottom
```

Therefore we need the row.

That is why we store:

```python
columns[col].append((row, node.val))
```

Later:

```python
columns[col].sort()
```

sorts first by:

```text
row
```

and then by:

```text
value
```

because Python sorts tuples lexicographically.

---

# 7. Why Does `columns[col].sort()` Sort by Value Too?

Suppose two nodes have exactly the same coordinates:

```text
(row = 2, col = 0)
```

with values:

```text
15
8
```

We need:

```text
8, 15
```

because the problem requires value-based ordering for nodes sharing the same row and column.

Python tuple sorting automatically does:

```text
(row, value)
```

So:

```python
columns[col].sort()
```

means:

```text
First  → sort by row
Then   → if row is same, sort by value
```

This is a very useful Python trick.

---

# 8. Why BFS?

We can use DFS as well if we explicitly store coordinates and sort everything afterward.

But BFS naturally processes nodes level by level.

The queue stores:

```python
(node, row, col)
```

So every node carries its coordinate information.

For example:

```python
queue.append((root, 0, 0))
```

Then:

```python
queue.append((node.left, row + 1, col - 1))
queue.append((node.right, row + 1, col + 1))
```

---

# 9. Complete Code

```python
from collections import defaultdict, deque

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        # column -> list of (row, value)
        columns = defaultdict(list)

        queue = deque()
        queue.append((root, 0, 0))   # node, row, col

        while queue:

            node, row, col = queue.popleft()

            if node is None:
                continue

            # Store row and value inside this column
            columns[col].append((row, node.val))

            # Left child
            queue.append((node.left, row + 1, col - 1))

            # Right child
            queue.append((node.right, row + 1, col + 1))

        answer = []

        # Process columns from left to right
        for col in sorted(columns):

            # Sort by row first, then value
            columns[col].sort()

            current = []

            for row, value in columns[col]:
                current.append(value)

            answer.append(current)

        return answer
```

---

# 10. Dry Run

Consider:

```text
        3
       / \
      9   20
         /  \
        15   7
```

Start:

```text
queue = [(3, 0, 0)]
columns = {}
```

---

### Process `3`

```text
node = 3
row = 0
col = 0
```

Store:

```text
columns[0] = [(0, 3)]
```

Add children:

```text
9  → (1, -1)
20 → (1, 1)
```

Queue:

```text
[(9,1,-1), (20,1,1)]
```

---

### Process `9`

Store:

```text
columns[-1] = [(1,9)]
```

No children.

---

### Process `20`

Store:

```text
columns[1] = [(1,20)]
```

Children:

```text
15 → (2,0)
7  → (2,2)
```

---

### Process `15`

```text
columns[0] = [(0,3), (2,15)]
```

---

### Process `7`

```text
columns[2] = [(2,7)]
```

Final dictionary conceptually:

```text
-1 → [(1,9)]
 0 → [(0,3), (2,15)]
 1 → [(1,20)]
 2 → [(2,7)]
```

Now:

```python
for col in sorted(columns):
```

gives:

```text
-1, 0, 1, 2
```

So the columns are processed from:

```text
left → right
```

Final answer:

```text
[
    [9],
    [3, 15],
    [20],
    [7]
]
```

---

# 11. Why `defaultdict(list)`?

We need multiple nodes inside the same column.

For example:

```text
column 0:
    3
    15
```

Instead of checking:

```python
if col not in columns:
    columns[col] = []
```

we can use:

```python
columns = defaultdict(list)
```

Then:

```python
columns[col].append((row, node.val))
```

works directly.

---

# 12. Why Do We Add `None` Children?

The code does:

```python
queue.append((node.left, row + 1, col - 1))
queue.append((node.right, row + 1, col + 1))
```

even when a child is `None`.

Later:

```python
if node is None:
    continue
```

skips it.

This is valid, but it creates unnecessary queue entries.

A slightly cleaner version is:

```python
if node.left:
    queue.append((node.left, row + 1, col - 1))

if node.right:
    queue.append((node.right, row + 1, col + 1))
```

This avoids storing `None` values.

The logic remains the same.

---

# 13. Cleaner Version

```python
from collections import defaultdict, deque

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []

        columns = defaultdict(list)

        queue = deque()
        queue.append((root, 0, 0))

        while queue:
            node, row, col = queue.popleft()

            columns[col].append((row, node.val))

            if node.left:
                queue.append((node.left, row + 1, col - 1))

            if node.right:
                queue.append((node.right, row + 1, col + 1))

        answer = []

        for col in sorted(columns):
            columns[col].sort()

            current = []

            for row, value in columns[col]:
                current.append(value)

            answer.append(current)

        return answer
```

This version avoids putting `None` nodes into the queue.

---

# 14. The Three Important Pieces

Whenever you see this problem, remember these three things:

### 1. Coordinate System

```text
Root = (0, 0)

Left  → (row + 1, col - 1)
Right → (row + 1, col + 1)
```

### 2. Group by Column

```python
columns[col].append((row, value))
```

### 3. Sort

```python
for col in sorted(columns):
    columns[col].sort()
```

This gives:

```text
Columns → left to right
Rows    → top to bottom
Values  → ascending for same row + column
```

---

# 15. Common Mistakes

### Mistake 1: Using only `column`

Wrong:

```python
columns[col].append(node.val)
```

You lose the row information.

You need:

```python
columns[col].append((row, node.val))
```

---

### Mistake 2: Forgetting to sort columns

Dictionary order should not be used to decide the required vertical order.

Use:

```python
for col in sorted(columns):
```

---

### Mistake 3: Sorting only by value

Wrong:

```python
columns[col].sort(key=lambda x: x[1])
```

This would ignore row ordering.

We need:

```text
row first
value second
```

So normal tuple sorting works:

```python
columns[col].sort()
```

---

### Mistake 4: Using `col + 1` for the left child

Wrong:

```python
left → col + 1
```

Correct:

```python
left → col - 1
right → col + 1
```

---

### Mistake 5: Confusing Vertical Traversal with Top View

Top View keeps only:

```text
first node for each column
```

Vertical Traversal keeps:

```text
ALL nodes for each column
```

So:

```text
Top View
    ↓
one node per column

Vertical Traversal
    ↓
all nodes per column
```

---

# 16. Vertical Traversal vs Top View vs Bottom View

| Problem | Main Idea |
|---|---|
| Top View | First node for each column |
| Bottom View | Last/lowest node for each column according to traversal rules |
| Vertical Traversal | All nodes grouped by column + sorting rules |

The coordinate system is similar:

```text
Left  → col - 1
Right → col + 1
```

but the final processing is different.

---

# 17. Complexity

Let `n` be the number of nodes.

### BFS

Every node is visited once:

```text
O(n)
```

### Sorting

We sort:

```python
columns[col]
```

and also sort the column keys.

Overall sorting costs:

```text
O(n log n)
```

in the general case.

Therefore:

```text
Time  → O(n log n)
Space → O(n)
```

The space includes:

```text
Queue
+
Dictionary
+
Stored node information
+
Answer
```

---

# 18. Pattern Recognition

When you see:

```text
"Vertical Traversal"
"Vertical Order"
"same column"
"top to bottom"
"left to right"
"same position"
```

Think:

```text
Binary Tree
      ↓
Assign coordinates
      ↓
(row, column)
      ↓
Group by column
      ↓
Sort columns
      ↓
Sort (row, value)
```

### Coordinate Trick

```text
             (0,0)
            /     \
       (-1,1)     (1,1)
```

More precisely using `(row, col)`:

```text
             (0,0)
            /     \
       (1,-1)     (1,1)
```

Remember:

```text
LEFT  → row + 1, col - 1
RIGHT → row + 1, col + 1
```

---

# 19. Revision Cheat Sheet

```text
Vertical Traversal
        ↓
BFS
        ↓
Store (node, row, col)
        ↓
Left  → (row+1, col-1)
Right → (row+1, col+1)
        ↓
columns[col].append((row, value))
        ↓
Sort columns
        ↓
Sort each column
        ↓
(row, value)
        ↓
Build answer
```

### Core Code

```python
columns = defaultdict(list)

queue = deque()
queue.append((root, 0, 0))

while queue:
    node, row, col = queue.popleft()

    if node is None:
        continue

    columns[col].append((row, node.val))

    queue.append((node.left, row + 1, col - 1))
    queue.append((node.right, row + 1, col + 1))
```

Then:

```python
for col in sorted(columns):
    columns[col].sort()
```

---

# 20. Interview Memory Trick

Remember:

> **"Give every node a `(row, col)`, group by column, then sort by `(row, value)`."**

The complete mental model:

```text
LEFT  → col - 1
RIGHT → col + 1

Same column?
    ↓
Group together

Same row too?
    ↓
Sort by value
```

### One-Line Pattern

> **Vertical Traversal = Coordinate `(row, col)` + BFS + column grouping + sort `(row, value)`.**