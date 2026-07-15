# 203. Remove Linked List Elements

## Problem

Given the `head` of a linked list and an integer `val`, remove all nodes from the linked list where:

```text
Node.val == val
```

Return the new head of the linked list.

---

## Example

```text
Input:
head = [1, 2, 6, 3, 4, 5, 6]
val = 6

Output:
[1, 2, 3, 4, 5]
```

### Visualization

```text
Before:

1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6 -> None

After removing 6:

1 -> 2 -> 3 -> 4 -> 5 -> None
```

---

# Pattern Used

## Linked List Node Deletion

The main pattern used in this problem is:

```text
Previous Pointer + Current Pointer
```

We maintain:

```text
prev -> previous valid node
curr -> current node being checked
```

The important idea is:

```text
If curr needs to be deleted:
    connect prev directly to curr.next

If curr does not need to be deleted:
    move prev forward
```

One special situation occurs when the node being deleted is the `head`.

This can be handled in two ways:

1. Manually update the `head`.
2. Use a dummy node before the `head`.

---

# Solution 1: Previous + Current Pointer

This approach directly modifies the original linked list without using a dummy node.

```python
class Solution:
    def removeElements(
        self,
        head: Optional[ListNode],
        val: int
    ) -> Optional[ListNode]:

        prev = None
        curr = head

        while curr:
            nxt = curr.next

            if curr.val == val:

                # Current node is the head
                if prev is None:
                    head = nxt

                # Current node is somewhere after the head
                else:
                    prev.next = nxt

                # Disconnect the deleted node
                curr.next = None

                # Move curr forward
                curr = nxt

            else:
                prev = curr
                curr = curr.next

        return head
```

---

## How This Approach Works

We start with:

```text
prev = None
curr = head
```

For every node, we first store:

```python
nxt = curr.next
```

This is important because we may disconnect the current node.

Then we check:

```python
if curr.val == val:
```

If the value matches, the node needs to be removed.

---

## Case 1: Deleting the Head

Consider:

```text
7 -> 1 -> 2 -> 3
```

Suppose:

```text
val = 7
```

Initially:

```text
prev = None

curr
 ↓
 7 -> 1 -> 2 -> 3
 ↑
head
```

Because:

```text
prev is None
```

we know that `curr` is currently the head node.

So we update:

```python
head = nxt
```

Now:

```text
head
 ↓
1 -> 2 -> 3
```

---

## Case 2: Deleting a Node in the Middle

Consider:

```text
1 -> 2 -> 6 -> 3
```

Pointers:

```text
     prev  curr
       ↓    ↓
1 -> 2 -> 6 -> 3
```

Since `6` needs to be removed:

```python
prev.next = nxt
```

Now:

```text
1 -> 2 -------> 3
```

The node containing `6` is skipped.

---

## Why Do We Store `nxt`?

Before changing any links, we store:

```python
nxt = curr.next
```

Suppose:

```text
1 -> 2 -> 6 -> 3
          ↑
         curr
```

We store:

```text
nxt
 ↓
 3
```

Then we can safely disconnect `curr`:

```python
curr.next = None
```

and still move forward using:

```python
curr = nxt
```

---

## Important: Do Not Move `prev` After Deletion

Consider:

```text
1 -> 7 -> 7 -> 3
```

Suppose:

```text
val = 7
```

Initially:

```text
prev  curr
 ↓      ↓
 1 -> 7 -> 7 -> 3
```

After deleting the first `7`:

```text
prev  curr
 ↓      ↓
 1 --> 7 -> 3
```

`prev` must remain at `1`.

Why?

Because the next node is also `7` and must also be removed.

If we move `prev` after deleting a node, consecutive matching nodes may not be handled correctly.

### Rule

```text
Node deleted
    ↓
Do NOT move prev

Node kept
    ↓
Move prev to curr
```

---

## Dry Run

### Input

```text
head = [1, 2, 6, 3]
val = 6
```

### Initial State

```text
prev = None
curr = 1
```

### Step 1

```text
curr = 1
1 != 6
```

Move both pointers:

```text
prev = 1
curr = 2
```

### Step 2

```text
curr = 2
2 != 6
```

Move both pointers:

```text
prev = 2
curr = 6
```

### Step 3

```text
curr = 6
6 == 6
```

Remove the node:

```python
prev.next = curr.next
```

Result:

```text
1 -> 2 -> 3
```

Keep `prev` at `2` and move `curr` to `3`.

### Step 4

```text
curr = 3
3 != 6
```

Move forward.

Final result:

```text
1 -> 2 -> 3
```

---

# Solution 2: Dummy Node Approach

A dummy node can be added before the original head.

This removes the need to handle head deletion separately.

```python
class Solution:
    def removeElements(
        self,
        head: Optional[ListNode],
        val: int
    ) -> Optional[ListNode]:

        dummy = ListNode(-1)
        dummy.next = head

        prev = dummy
        curr = head

        while curr:

            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr

            curr = curr.next

        return dummy.next
```

---

## Why Use a Dummy Node?

Consider:

```text
7 -> 1 -> 2 -> 3
```

Suppose:

```text
val = 7
```

Without a dummy node, the head requires special handling:

```python
head = head.next
```

With a dummy node:

```text
dummy -> 7 -> 1 -> 2 -> 3
```

Pointers:

```text
prev    curr
 ↓       ↓
dummy -> 7 -> 1 -> 2 -> 3
```

To remove `7`:

```python
prev.next = curr.next
```

Result:

```text
dummy -> 1 -> 2 -> 3
```

The same deletion logic now works for:

* The head node
* Middle nodes
* The last node

No special condition is required.

---

## Why Return `dummy.next`?

The dummy node is only a helper node.

For example:

```text
dummy -> 1 -> 2 -> 3
```

The actual linked list starts from:

```text
dummy.next
```

Therefore:

```python
return dummy.next
```

---

# Edge Cases

## 1. Empty Linked List

```text
Input:
head = []
val = 1

Output:
[]
```

---

## 2. Delete the Head

```text
Input:
[7, 1, 2, 3]

val = 7

Output:
[1, 2, 3]
```

---

## 3. Delete Multiple Head Nodes

```text
Input:
[7, 7, 1, 2]

val = 7

Output:
[1, 2]
```

---

## 4. Delete Consecutive Nodes

```text
Input:
[1, 7, 7, 7, 2]

val = 7

Output:
[1, 2]
```

This case demonstrates why `prev` should not move when a node is deleted.

---

## 5. Delete All Nodes

```text
Input:
[7, 7, 7, 7]

val = 7

Output:
[]
```

---

## 6. Value Does Not Exist

```text
Input:
[1, 2, 3, 4]

val = 7

Output:
[1, 2, 3, 4]
```

---

# Complexity Analysis

Both approaches have the same complexity.

### Time Complexity

```text
O(n)
```

Every node is visited once.

Since we must check every node to determine whether its value equals `val`, `O(n)` is optimal.

### Space Complexity

```text
O(1)
```

Only a constant number of pointers are used.

For Solution 1:

```text
prev
curr
nxt
```

For Solution 2:

```text
dummy
prev
curr
```

No additional data structure depending on the input size is used.

---

# Solution Comparison

| Approach      | Time   | Space  | Head Special Case |
| ------------- | ------ | ------ | ----------------- |
| `prev + curr` | `O(n)` | `O(1)` | Required          |
| Dummy Node    | `O(n)` | `O(1)` | Not Required      |

Both solutions are optimal.

The dummy-node approach usually produces cleaner code because it handles every node using the same deletion logic.

---

# Key Takeaways

* This problem follows the **Linked List Node Deletion** pattern.
* Use `prev` and `curr` pointers to remove nodes while traversing.
* When deleting a node, connect the previous node directly to the next node.
* Do not move `prev` when the current node is deleted.
* Consecutive deletions are an important edge case.
* Deleting the head requires special handling when no dummy node is used.
* A dummy node removes the head-deletion special case.
* `dummy.next` represents the actual head of the resulting linked list.
* Both approaches achieve optimal `O(n)` time and `O(1)` space.

---

## Pattern Recognition

Whenever a linked list problem asks you to:

```text
Delete nodes based on a condition
Remove specific values
Filter nodes from a linked list
Handle possible head deletion
```

think about:

```text
prev + curr
```

and consider whether using a:

```text
Dummy Node
```

can simplify the edge cases.
