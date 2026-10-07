# Heap Data Structure in Python

## 1. What is a Heap?

A **Heap** is a special tree-based data structure that follows the **Heap Property**.

A heap is usually represented as a **Complete Binary Tree**.

There are two main types:

- **Min Heap**
- **Max Heap**

---

# 2. Complete Binary Tree

A heap must be a **Complete Binary Tree**.

That means:

1. Every level is completely filled except possibly the last level.
2. The last level is filled from **left to right**.

Example:

```text
        10
       /  \
      20   30
     / \   /
    40 50 60
```

This is a complete binary tree.

But:

```text
        10
       /  \
      20   30
       \
        40
```

is not complete because the last level is not filled from left to right.

---

# 3. Min Heap

In a **Min Heap**:

```text
Parent <= Children
```

The smallest element is always at the root.

Example:

```text
        10
       /  \
      20   15
     / \   /
    30 40 25
```

Every parent is smaller than its children.

Therefore:

```text
Minimum element = root = 10
```

Important:

> A heap is NOT a Binary Search Tree.

In a BST:

```text
Left < Root < Right
```

In a Min Heap:

```text
Parent <= Children
```

There is no ordering requirement between the left and right subtrees.

---

# 4. Max Heap

In a **Max Heap**:

```text
Parent >= Children
```

The largest element is always at the root.

Example:

```text
        50
       /  \
      40   45
     / \   /
    20 30 35
```

Therefore:

```text
Maximum element = root = 50
```

---

# 5. Heap vs BST

| Property | Heap | BST |
|---|---|---|
| Structure | Complete Binary Tree | Binary Tree |
| Parent relationship | Parent dominates children | Left < Root < Right |
| Root | Min/Max element | Depends on tree |
| Searching arbitrary value | O(n) | O(h) |
| Insert | O(log n) | O(h) |
| Delete root | O(log n) | O(h) |
| Get min/max | O(1) depending on heap type | O(h) generally |
| Typical use | Priority Queue | Searching/Ordering |

---

# 6. Why Use an Array?

Although a heap is conceptually a tree, we usually store it in an **array/list**.

Example:

```text
        10
       /  \
      20   15
     / \   /
    30 40 25
```

Array representation:

```python
heap = [10, 20, 15, 30, 40, 25]
```

No explicit `TreeNode` objects are required.

---

# 7. Array Index Relationships

Using **0-based indexing**:

```text
Current node index = i
```

### Parent

```python
parent = (i - 1) // 2
```

### Left Child

```python
left = 2 * i + 1
```

### Right Child

```python
right = 2 * i + 2
```

Example:

```text
Array:

Index:   0   1   2   3   4   5
Value:  10  20  15  30  40  25
```

Tree:

```text
             10 (0)
            /      \
        20 (1)    15 (2)
        /   \       /
    30 (3) 40 (4) 25 (5)
```

For index `1`:

```python
parent = (1 - 1) // 2
       = 0

left = 2 * 1 + 1
     = 3

right = 2 * 1 + 2
      = 4
```

---

# 8. Why Array Representation Works

A complete binary tree has no unnecessary gaps.

Therefore, nodes can be stored continuously:

```text
Root
 ↓
Left / Right
 ↓
Next level
 ↓
Left to Right
```

The index formulas allow us to move between parent and children without storing pointers.

This gives:

```text
Tree nodes + pointers
        ↓
Array indices
```

and saves memory.

---

# 9. Heapify

**Heapify** means restoring the heap property.

There are two common operations:

```text
Min Heap:
Heapify Up
Heapify Down

Max Heap:
Heapify Up
Heapify Down
```

The direction depends on where the violation occurs.

---

# 10. Heapify Up

Heapify Up is mainly used after **inserting a new element**.

Suppose we have a Min Heap:

```text
        10
       /  \
      20   15
```

Insert:

```text
5
```

Because the tree must remain complete, `5` is inserted at the next available position:

```text
        10
       /  \
      20   15
     /
    5
```

Now:

```text
5 < 20
```

violates the Min Heap property.

So we swap:

```text
        10
       /  \
      5    15
     /
    20
```

But:

```text
5 < 10
```

still violates the heap property.

Swap again:

```text
        5
       / \
      10  15
     /
    20
```

Now the heap is valid.

This process is:

```text
Heapify Up
```

---

# 11. Heapify Up Logic

For a Min Heap:

```python
while index > 0:

    parent = (index - 1) // 2

    if heap[parent] <= heap[index]:
        break

    heap[parent], heap[index] = heap[index], heap[parent]

    index = parent
```

The element keeps moving toward the root until:

```text
Parent <= Current
```

---

# 12. Insert into Min Heap

```python
class MinHeap:

    def __init__(self):
        self.heap = []

    def insert(self, value):

        # Add element at the end
        self.heap.append(value)

        index = len(self.heap) - 1

        # Heapify Up
        while index > 0:

            parent = (index - 1) // 2

            if self.heap[parent] <= self.heap[index]:
                break

            self.heap[parent], self.heap[index] = (
                self.heap[index],
                self.heap[parent]
            )

            index = parent
```

### Complexity

```text
Insert = O(log n)
```

Why?

The element can move from the bottom to the root.

The height of a complete binary tree is:

```text
O(log n)
```

---

# 13. Heapify Down

Heapify Down is mainly used after removing the root.

Example:

```text
        10
       /  \
      20   15
     / \
    30 40
```

Remove `10`.

To maintain the complete tree structure, move the last element to the root:

```text
        40
       /  \
      20   15
     /
    30
```

Now:

```text
40 > 20
40 > 15
```

violates the Min Heap property.

We compare the children and swap with the **smaller child**:

```text
        15
       /  \
      20   40
     /
    30
```

Now the heap property is restored.

This is:

```text
Heapify Down
```

---

# 14. Heapify Down Logic

For a Min Heap:

```python
def heapifyDown(self, index):

    n = len(self.heap)

    while True:

        left = 2 * index + 1
        right = 2 * index + 2

        smallest = index

        if left < n and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < n and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest == index:
            break

        self.heap[index], self.heap[smallest] = (
            self.heap[smallest],
            self.heap[index]
        )

        index = smallest
```

Important:

> In a Min Heap, always move toward the **smaller child**.

---

# 15. Remove Minimum from Min Heap

The minimum element is always at:

```text
heap[0]
```

So:

```python
def remove(self):

    if not self.heap:
        return None

    minimum = self.heap[0]

    # Move last element to root
    self.heap[0] = self.heap[-1]
    self.heap.pop()

    # Restore heap property
    if self.heap:
        self.heapifyDown(0)

    return minimum
```

### Complexity

```text
Remove Min = O(log n)
```

---

# 16. Complete Min Heap Implementation

```python
class MinHeap:

    def __init__(self):
        self.heap = []

    def insert(self, value):

        self.heap.append(value)

        index = len(self.heap) - 1

        # Heapify Up
        while index > 0:

            parent = (index - 1) // 2

            if self.heap[parent] <= self.heap[index]:
                break

            self.heap[parent], self.heap[index] = (
                self.heap[index],
                self.heap[parent]
            )

            index = parent

    def heapifyDown(self, index):

        n = len(self.heap)

        while True:

            left = 2 * index + 1
            right = 2 * index + 2

            smallest = index

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == index:
                break

            self.heap[index], self.heap[smallest] = (
                self.heap[smallest],
                self.heap[index]
            )

            index = smallest

    def remove(self):

        if not self.heap:
            return None

        minimum = self.heap[0]

        self.heap[0] = self.heap[-1]
        self.heap.pop()

        if self.heap:
            self.heapifyDown(0)

        return minimum

    def peek(self):

        if not self.heap:
            return None

        return self.heap[0]

    def size(self):
        return len(self.heap)
```

---

# 17. Max Heap

The same concepts apply to a Max Heap.

The difference is the comparison.

### Min Heap

```text
Parent <= Children
```

### Max Heap

```text
Parent >= Children
```

For Max Heapify Up:

```python
if heap[parent] >= heap[index]:
    break
```

For Max Heapify Down:

```python
if heap[left] > heap[largest]:
    largest = left

if heap[right] > heap[largest]:
    largest = right
```

So the main difference is:

```text
Min Heap → choose smaller child
Max Heap → choose larger child
```

---

# 18. Python `heapq`

Python provides a built-in heap implementation through:

```python
import heapq
```

`heapq` implements a **Min Heap**.

Example:

```python
import heapq

heap = []

heapq.heappush(heap, 30)
heapq.heappush(heap, 10)
heapq.heappush(heap, 20)

print(heap)
```

The smallest element is always:

```python
heap[0]
```

Get minimum:

```python
print(heap[0])
```

Remove minimum:

```python
minimum = heapq.heappop(heap)
```

---

# 19. Important `heapq` Operations

### Push

```python
heapq.heappush(heap, value)
```

Complexity:

```text
O(log n)
```

---

### Pop Minimum

```python
heapq.heappop(heap)
```

Complexity:

```text
O(log n)
```

---

### Peek Minimum

```python
heap[0]
```

Complexity:

```text
O(1)
```

---

### Convert List Into Heap

```python
heapq.heapify(arr)
```

Example:

```python
import heapq

arr = [50, 20, 40, 10, 30]

heapq.heapify(arr)

print(arr)
```

Complexity:

```text
O(n)
```

This is important:

> Building a heap from an existing array using bottom-up heapify takes `O(n)`, not `O(n log n)`.

---

# 20. Why `heapify()` Is O(n)

If we insert every element one by one:

```text
n elements
×
O(log n) insertion
```

we get:

```text
O(n log n)
```

But bottom-up heap construction starts from the last non-leaf node and heapifies downward.

Most nodes are near the bottom and move only a small distance.

Therefore total work is:

```text
O(n)
```

This is called:

```text
Bottom-Up Heap Construction
```

---

# 21. Creating a Max Heap with `heapq`

Python's `heapq` is a Min Heap.

To simulate a Max Heap, use negative values:

```python
import heapq

heap = []

heapq.heappush(heap, -30)
heapq.heappush(heap, -10)
heapq.heappush(heap, -20)

maximum = -heapq.heappop(heap)

print(maximum)
```

Output:

```text
30
```

Why does this work?

Original:

```text
30 → 10 → 20
```

Store:

```text
-30 → -10 → -20
```

The smallest negative value corresponds to the largest original value.

---

# 22. Heap Sort

Heap can also be used for sorting.

For ascending order:

```text
Build Min Heap
      ↓
Repeatedly remove minimum
      ↓
Sorted output
```

Using `heapq`:

```python
import heapq

arr = [5, 2, 8, 1, 3]

heapq.heapify(arr)

result = []

while arr:
    result.append(heapq.heappop(arr))

print(result)
```

Output:

```text
[1, 2, 3, 5, 8]
```

### Complexity

```text
Time  : O(n log n)
Space : O(n) for the output/heap representation
```

---

# 23. Heap Applications

Heap is especially useful when we repeatedly need the:

```text
Minimum
or
Maximum
```

Common applications:

### 1. Priority Queue

```text
Highest priority item
        ↓
Process first
```

---

### 2. Kth Largest / Kth Smallest

Maintain a heap of size `k`.

---

### 3. Top K Elements

Examples:

```text
Top K largest numbers
Top K smallest numbers
Top K frequent elements
```

---

### 4. Merge K Sorted Lists

Use a Min Heap to always select the smallest current element.

---

### 5. Dijkstra's Algorithm

A priority queue / Min Heap is commonly used to select the next node with the smallest distance.

---

### 6. Scheduling

Tasks can be prioritized based on:

```text
priority
deadline
execution time
```

---

# 24. Heap vs Priority Queue

These concepts are related but not exactly the same.

### Priority Queue

An abstract data structure where elements are processed according to priority.

### Heap

A common data structure used to implement a priority queue efficiently.

```text
Priority Queue
      ↓
Can be implemented using
      ↓
Heap
```

In Python:

```python
heapq
```

is commonly used to implement priority queues.

---

# 25. Important Heap Patterns

### Pattern 1 — Need Minimum Quickly

Think:

```text
Min Heap
```

---

### Pattern 2 — Need Maximum Quickly

Think:

```text
Max Heap
```

---

### Pattern 3 — Need Top K

Think:

```text
Heap of size K
```

---

### Pattern 4 — Repeatedly Need Smallest Element

Think:

```text
Min Heap
```

---

### Pattern 5 — Repeatedly Need Largest Element

Think:

```text
Max Heap
```

---

### Pattern 6 — Merge Sorted Data

Think:

```text
Min Heap
```

because we repeatedly need the smallest current element.

---

# 26. Important Heap Complexity

| Operation | Complexity |
|---|---:|
| Peek Min/Max | `O(1)` |
| Insert | `O(log n)` |
| Delete Root | `O(log n)` |
| Heapify One Node | `O(log n)` |
| Build Heap | `O(n)` |
| Search Arbitrary Value | `O(n)` |
| Heap Sort | `O(n log n)` |

---

# 27. Heap Mental Model

Think of a heap as:

```text
Complete Binary Tree
        +
Heap Property
        ↓
Efficient Min/Max Access
```

The heap does **not** keep all elements sorted.

For example, this is a valid Min Heap:

```text
        5
       / \
      10  8
     / \  /
    20 15 12
```

But:

```text
10 > 8
```

and that's completely fine.

The only requirement is:

```text
5 < 10
5 < 8

10 < 20
10 < 15

8 < 12
```

So:

> A heap is **partially ordered**, not fully sorted.

---

# 28. Common Mistakes

### Mistake 1: Thinking Heap is a BST

Wrong:

```text
Left < Root < Right
```

That is a BST property.

Heap only requires:

```text
Parent <= Children    # Min Heap
Parent >= Children    # Max Heap
```

---

### Mistake 2: Searching a heap like a BST

You cannot generally do:

```text
if target < root:
    go left
else:
    go right
```

A heap does not provide that ordering.

Searching for an arbitrary value is generally:

```text
O(n)
```

---

### Mistake 3: Forgetting Complete Tree Property

A heap must remain complete.

When inserting:

```text
Add at next available position
        ↓
Heapify Up
```

When deleting root:

```text
Move last element to root
        ↓
Heapify Down
```

---

### Mistake 4: Choosing the Wrong Child

For Min Heap:

```text
Choose smaller child
```

For Max Heap:

```text
Choose larger child
```

---

# 29. Heapify Direction Cheat Sheet

```text
INSERT
  ↓
Add at bottom
  ↓
Heap property may break with parent
  ↓
HEAPIFY UP
```

```text
DELETE ROOT
  ↓
Move last element to root
  ↓
Heap property may break with children
  ↓
HEAPIFY DOWN
```

Remember:

```text
Insertion → Up
Deletion  → Down
```

---

# 30. Revision Cheat Sheet

```text
Heap:
Complete Binary Tree + Heap Property

Min Heap:
Parent <= Children
Root = Minimum

Max Heap:
Parent >= Children
Root = Maximum

0-Based Array:

Parent:
(i - 1) // 2

Left:
2 * i + 1

Right:
2 * i + 2

Insertion:
Append at end
↓
Heapify Up

Delete Root:
Move last element to root
↓
Heapify Down

Min Heapify:
Choose smaller child

Max Heapify:
Choose larger child

Peek:
O(1)

Insert:
O(log n)

Delete Root:
O(log n)

Build Heap:
O(n)

Search:
O(n)

Heap Sort:
O(n log n)

Python:
import heapq

heapq.heappush(heap, x)
heapq.heappop(heap)
heapq.heapify(arr)

heapq is a Min Heap.

Max Heap with heapq:
Store negative values.

Core Pattern:
Complete Binary Tree + Parent/Child Index Formula + Heapify Up/Down.

One-Line Pattern:
Heap = Complete Binary Tree + Heap Property → Efficient access to the minimum or maximum element.
```