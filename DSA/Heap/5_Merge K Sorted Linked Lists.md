# Merge K Sorted Linked Lists

## 1. Problem

Given an array `lists` containing `k` sorted linked lists, merge them into **one sorted linked list** and return its head.

Each individual linked list is already sorted in ascending order.

### Example

```text
List 1: 1 → 4 → 5
List 2: 1 → 3 → 4
List 3: 2 → 6
```

Output:

```text
1 → 1 → 2 → 3 → 4 → 4 → 5 → 6
```

The challenge is to merge all lists efficiently without repeatedly searching through every list.

---

# 2. Brute Force Approach

The simplest approach is to:

1. Traverse every linked list.
2. Store all node values in an array.
3. Sort the array.
4. Create a new linked list using the sorted values.

### Code

```python
def mergeKLists(lists):
    values = []

    for head in lists:
        while head:
            values.append(head.val)
            head = head.next

    values.sort()

    dummy = ListNode(0)
    curr = dummy

    for value in values:
        curr.next = ListNode(value)
        curr = curr.next

    return dummy.next
```

### Complexity

Let:

- `k` = number of linked lists
- `N` = total number of nodes across all lists

Collecting the values takes `O(N)` time, and sorting takes `O(N log N)`.

```text
Time:  O(N log N)
Space: O(N)
```

### Limitation

All values are sorted again, even though every individual linked list is already sorted.

We can use a Min Heap to merge them more efficiently.

---

# 3. Optimized Approach: Min Heap

The key idea is:

> Keep the smallest unprocessed node from each linked list in a Min Heap.

Since each linked list is already sorted, we only need to consider its current node.

Whenever we remove the smallest node:

1. Attach it to the merged linked list.
2. Move to its next node.
3. Insert that next node into the heap, if it exists.

Repeat until the heap becomes empty.

### Example

```text
List 1: 1 → 4 → 5
List 2: 1 → 3 → 4
List 3: 2 → 6
```

Initially, insert the head of each list:

```text
Heap values = [1, 1, 2]
```

Remove the smallest node and attach it to the result.

If it came from List 1, insert its next node, `4`.

The heap now contains the current candidates from the lists:

```text
List 1 → 4
List 2 → 1
List 3 → 2
```

Continue selecting the smallest candidate until all lists are exhausted.

Final result:

```text
1 → 1 → 2 → 3 → 4 → 4 → 5 → 6
```

---

# 4. Code

```python
import heapq

class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        min_heap = []

        # Insert the head of every non-empty linked list
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))

        # Dummy node simplifies linked list construction
        dummy = ListNode(0)
        curr = dummy

        while min_heap:
            # Remove the smallest available node
            value, i, node = heapq.heappop(min_heap)

            # Attach the existing node to the result
            curr.next = node
            curr = curr.next

            # Insert the next node from the same list
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))

        return dummy.next
```

---

# 5. Understanding the Heap Tuple

This is the most important line:

```python
heapq.heappush(min_heap, (node.val, i, node))
```

Each heap entry contains three values:

```text
(node.val, i, node)
```

| Value | Meaning | Why Needed? |
|---|---|---|
| `node.val` | Current node's value | Determines the smallest node |
| `i` | Index of the linked list | Identifies the source list |
| `node` | Actual linked list node | Allows us to attach it and access `node.next` |

## Why Store the List Index?

Python compares tuples element by element.

Suppose two nodes have the same value:

```text
(1, 0, nodeA)
(1, 1, nodeB)
```

Python compares:

1. First, the node values.
2. If they are equal, the list indices.
3. It only compares the third elements if the first two are also equal.

Because each list has a different index, Python can break ties without trying to compare the `ListNode` objects.

Without the index, two nodes with equal values could cause a `TypeError`, because custom linked list nodes generally do not support ordering comparisons.

The index also tells us which list the node belongs to.

## Why Store the Actual Node?

We need the node itself because we are reusing existing nodes.

After removing a node:

```python
curr.next = node
```

we attach it directly to the merged list.

Then:

```python
node.next
```

gives us the next node from the same list.

We don't need to create a new node for every value.

---

# 6. Understanding the Dummy Node

```python
dummy = ListNode(0)
curr = dummy
```

The dummy node is a placeholder that simplifies linked list construction.

Initially:

```text
dummy → None
curr
```

Whenever we remove a node from the heap:

```python
curr.next = node
curr = curr.next
```

For example, if the selected node has value `1`:

```text
dummy → 1
         ↑
        curr
```

After selecting `2`:

```text
dummy → 1 → 2
             ↑
            curr
```

We don't need special logic for the first node because the dummy node already provides a starting point.

At the end:

```python
return dummy.next
```

We return the actual head of the merged list, skipping the dummy node.

---

# 7. Why Insert Only One Node From Each List?

Consider:

```text
List 1: 1 → 4 → 7
List 2: 2 → 5 → 8
List 3: 3 → 6 → 9
```

Initially, the heap contains:

```text
1, 2, 3
```

Why not insert every node?

Because each list is sorted.

For List 1:

```text
1 < 4 < 7
```

As long as `1` has not been processed, `4` and `7` cannot be the smallest unprocessed node from that list.

After removing `1`, we insert `4`.

After removing `4`, we insert `7`.

The same process applies to every list.

Therefore, the heap only needs to store the **current smallest unprocessed node from each non-empty list**.

The heap size never exceeds `k`.

---

# 8. Dry Run

Input:

```text
List 1: 1 → 4 → 5
List 2: 1 → 3 → 4
List 3: 2 → 6
```

### Step 1: Initialize the Heap

Insert all non-empty list heads:

```text
(1, 0, node)
(1, 1, node)
(2, 2, node)
```

Conceptually:

```text
Heap values = [1, 1, 2]
Result = None
```

### Step 2: Remove the First `1`

Suppose it comes from List 1.

Attach it:

```text
Result: 1
```

Its next node is `4`.

Insert `4` from List 1.

Current candidates:

```text
List 1 → 4
List 2 → 1
List 3 → 2
```

### Step 3: Remove the Second `1`

It comes from List 2.

Attach it:

```text
Result: 1 → 1
```

Its next node is `3`.

Insert `3` from List 2.

Current candidates:

```text
List 1 → 4
List 2 → 3
List 3 → 2
```

### Step 4: Remove `2`

It comes from List 3.

Attach it:

```text
Result: 1 → 1 → 2
```

Its next node is `6`.

Insert `6`.

Current candidates:

```text
List 1 → 4
List 2 → 3
List 3 → 6
```

### Step 5: Continue

| Selected Node | Next Node Inserted | Result |
|---:|---:|---|
| 3 | 4 from List 2 | `1 → 1 → 2 → 3` |
| 4 from List 1 | 5 | `1 → 1 → 2 → 3 → 4` |
| 4 from List 2 | None | `1 → 1 → 2 → 3 → 4 → 4` |
| 5 | None | `1 → 1 → 2 → 3 → 4 → 4 → 5` |
| 6 | None | `1 → 1 → 2 → 3 → 4 → 4 → 5 → 6` |

The heap is now empty.

Final answer:

```text
1 → 1 → 2 → 3 → 4 → 4 → 5 → 6
```

---

# 9. Why Does This Work?

At every step, the heap contains the first unprocessed node from every non-empty list.

Since every list is sorted:

```text
Current node ≤ Every later node in the same list
```

Therefore, the globally smallest unprocessed node must be among the nodes currently in the heap.

The Min Heap removes that smallest node.

Then we insert the next node from the same list, preserving the invariant that the heap contains the smallest unprocessed candidate from each list.

Repeating this process guarantees that nodes are attached in ascending order.

---

# 10. Complexity Analysis

Let:

- `k` = number of linked lists
- `N` = total number of nodes across all lists

### Heap Initialization

At most `k` nodes are inserted.

```text
Time: O(k log k)
```

### Processing Nodes

Every node is removed from the heap exactly once.

Each removal costs:

```text
O(log k)
```

For every node, we perform at most one insertion, which also costs `O(log k)`.

Therefore:

```text
Time: O(N log k)
```

### Overall Time Complexity

```text
O(k log k + N log k)
```

Since `k <= N` when the lists are non-empty:

```text
Time = O(N log k)
```

### Space Complexity

The heap contains at most one node per linked list:

```text
Auxiliary Space = O(k)
```

The merged linked list reuses the existing nodes, so we don't allocate a new node for every value.

---

# 11. Complexity Comparison

| Approach | Time | Auxiliary Space | Main Idea |
|---|---:|---:|---|
| Collect values and sort | O(N log N) | O(N) | Sort every value |
| Min Heap | O(N log k) | O(k) | Merge using current list heads |

The Min Heap approach is especially useful when `k` is much smaller than `N`.

---

# 12. Common Mistakes

### Mistake 1: Inserting Every Node Initially

This would make the heap size `N`.

Instead, insert only the head of each non-empty list.

### Mistake 2: Forgetting the List Index

Use:

```python
(node.val, i, node)
```

The index helps Python break ties when values are equal and identifies the source list.

### Mistake 3: Forgetting to Insert `node.next`

After attaching a node:

```python
if node.next:
    heapq.heappush(min_heap, (node.next.val, i, node.next))
```

Otherwise, the remaining nodes from that list would never be processed.

### Mistake 4: Creating a New Node for Every Value

Your optimized solution reuses the original nodes:

```python
curr.next = node
```

This avoids allocating a separate node for every element.

### Mistake 5: Returning `dummy`

The dummy node is only a placeholder.

Return:

```python
return dummy.next
```

### Mistake 6: Forgetting Empty Lists

The initial condition:

```python
if node:
```

skips empty linked lists and prevents invalid access.

---

# 13. Pattern Recognition

When you see:

- Multiple sorted linked lists.
- A requirement to merge them into one sorted list.
- A need to repeatedly select the smallest available node.

Think:

```text
Min Heap + K-Way Merge
```

This is the same pattern as merging `k` sorted arrays.

The main difference is that, with linked lists, we attach the existing nodes instead of building an array of values.

---

# 14. Revision Cheat Sheet

```text
Merge K Sorted Linked Lists
             |
             ↓
Insert Each Non-Empty List Head
             |
             ↓
           Min Heap
             |
             ↓
       Pop Smallest Node
             |
             ↓
       Attach to Result
             |
             ↓
      Get node.next
             |
             ↓
     Push Next Node If Any
             |
             ↓
           Repeat
             |
             ↓
      Return dummy.next
```

### Heap Entry

```python
(node.val, list_index, node)
```

- `node.val`: determines the smallest node.
- `list_index`: breaks ties and identifies the source list.
- `node`: allows us to link the actual node and access its successor.

### Complexity

```text
Time:  O(N log k)
Space: O(k) auxiliary
```

### Core Insight

> **Keep one current node from each sorted linked list in a Min Heap. Remove the smallest node, attach it to the result, and insert its next node.**

---

# One-Line Pattern

> **Merge K Sorted Lists = Min Heap + One Current Node per List + Attach the Smallest Node and Push Its Successor.**