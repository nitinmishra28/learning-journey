# Rotate List

## Problem Overview

Given the `head` of a singly linked list, rotate the list to the right by `k` positions.

### Example

```text
Input:

head = 1 → 2 → 3 → 4 → 5 → None
k = 2
```

After rotating once:

```text
5 → 1 → 2 → 3 → 4 → None
```

After rotating twice:

```text
4 → 5 → 1 → 2 → 3 → None
```

Final result:

```text
4 → 5 → 1 → 2 → 3 → None
```

---

# Approach 1 — Move Last Node to Front `k` Times

The basic idea is simple:

```text
Find the last node
        ↓
Remove it from the end
        ↓
Connect it before the current head
        ↓
Make it the new head
        ↓
Repeat k times
```

---

## Python Code

```python
class Solution:
    def rotateRight(
        self,
        head: Optional[ListNode],
        k: int
    ) -> Optional[ListNode]:

        # Empty list or single-node list
        if head is None or head.next is None:
            return head

        # Step 1: Find the length of the linked list
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next

        # Step 2: Reduce unnecessary rotations
        k = k % length

        # Step 3: Rotate one position at a time
        count = 0

        while count < k:
            prev = None
            curr = head

            # Find the last node
            while curr.next:
                prev = curr
                curr = curr.next

            # Remove the last node
            prev.next = None

            # Put the last node before the current head
            curr.next = head

            # Update head
            head = curr

            count += 1

        return head
```

---

# Why Do We Check the Edge Cases?

```python
if head is None or head.next is None:
    return head
```

There are two cases.

### Empty Linked List

```text
head = None
```

There is nothing to rotate.

### Single Node

```text
1 → None
```

No matter how many times we rotate:

```text
1 → None
```

The list remains unchanged.

---

# Step 1 — Find the Length

```python
length = 0
curr = head

while curr:
    length += 1
    curr = curr.next
```

For:

```text
1 → 2 → 3 → 4 → 5 → None
```

Traversal:

```text
curr = 1    length = 1
curr = 2    length = 2
curr = 3    length = 3
curr = 4    length = 4
curr = 5    length = 5
curr = None → Stop
```

Therefore:

```text
length = 5
```

---

# Why Do We Use `k % length`?

This is one of the most important concepts in this problem.

Suppose:

```text
1 → 2 → 3
```

Length:

```text
3
```

Rotate once:

```text
3 → 1 → 2
```

Rotate twice:

```text
2 → 3 → 1
```

Rotate three times:

```text
1 → 2 → 3
```

After exactly `length` rotations, the Linked List returns to its original state.

Therefore:

```text
k = length
```

is effectively the same as:

```text
k = 0
```

Similarly:

```text
k = 4
```

for a list of length `3` is the same as:

```text
k = 1
```

because:

```python
4 % 3
```

gives:

```text
1
```

So we use:

```python
k = k % length
```

---

# Why Is `k % length` Important for Very Large `k`?

Suppose:

```text
head = 1 → 2 → 3

k = 2,000,000,000
```

Without modulo, we would try to perform:

```text
2,000,000,000 rotations
```

But:

```python
k = 2_000_000_000 % 3
```

gives:

```text
2
```

So only:

```text
2 rotations
```

are actually required.

This is a common DSA pattern:

```text
Repeated operation
+
State repeats after n operations
        ↓
Use modulo
```

---

# Step 2 — Find the Last and Second-Last Nodes

For every rotation:

```python
prev = None
curr = head
```

Then:

```python
while curr.next:
    prev = curr
    curr = curr.next
```

Suppose:

```text
1 → 2 → 3 → 4 → 5 → None
```

Initially:

```text
prev = None

curr
 ↓
1 → 2 → 3 → 4 → 5
```

After traversal:

```text
                  prev    curr
                   ↓       ↓
1 → 2 → 3 → 4 → 5 → None
```

So:

```text
prev = 4
curr = 5
```

Here:

```text
curr = last node
prev = second-last node
```

We need both.

`curr` will become the new head.

`prev` is required to disconnect the last node.

---

# Step 3 — Remove the Last Node

We do:

```python
prev.next = None
```

Before:

```text
1 → 2 → 3 → 4 → 5 → None
              ↑    ↑
             prev curr
```

After:

```text
1 → 2 → 3 → 4 → None

5 → None
```

Now node `5` has been separated from the original list.

---

# Step 4 — Connect Last Node to the Old Head

We do:

```python
curr.next = head
```

Before:

```text
5 → None

head
 ↓
1 → 2 → 3 → 4 → None
```

After:

```text
5
↓
1 → 2 → 3 → 4 → None
```

More clearly:

```text
5 → 1 → 2 → 3 → 4 → None
```

But `head` still points to:

```text
1
```

So we need one final update.

---

# Step 5 — Update the Head

```python
head = curr
```

Now:

```text
head
 ↓
5 → 1 → 2 → 3 → 4 → None
```

One right rotation is complete.

---

# Complete Dry Run

Input:

```text
1 → 2 → 3 → 4 → 5
```

and:

```text
k = 2
```

Length:

```text
5
```

Reduced rotations:

```text
k = 2 % 5
k = 2
```

---

## Rotation 1

Find:

```text
prev = 4
curr = 5
```

Disconnect:

```text
1 → 2 → 3 → 4

5
```

Connect:

```text
5 → 1 → 2 → 3 → 4
```

Update:

```text
head = 5
```

---

## Rotation 2

Current list:

```text
5 → 1 → 2 → 3 → 4
```

Find:

```text
prev = 3
curr = 4
```

Disconnect:

```text
5 → 1 → 2 → 3

4
```

Connect:

```text
4 → 5 → 1 → 2 → 3
```

Final:

```text
head
 ↓
4 → 5 → 1 → 2 → 3 → None
```

---

# Pattern Used

The main pattern used in this approach is:

## Find → Disconnect → Move to Front

```text
Find Last Node
      ↓
Keep Previous Node
      ↓
Disconnect Last Node
      ↓
Connect Last to Head
      ↓
Update Head
      ↓
Repeat
```

It also uses the important Linked List pattern:

```text
prev + curr
```

where:

```text
prev → second-last node
curr → last node
```

---

# Time Complexity of This Approach

First, finding the length takes:

```text
O(n)
```

Then we perform:

```text
k % n
```

rotations.

For every rotation, we traverse almost the entire Linked List to find the last node.

Each rotation:

```text
O(n)
```

For `k` effective rotations:

```text
O(n × k)
```

So the total time complexity is:

```text
O(n + n × k)
```

which simplifies to:

```text
O(n × k)
```

where `k` is already reduced using:

```python
k = k % length
```

Since the reduced `k` is always less than `n`, the worst case can be:

```text
O(n²)
```

---

# Space Complexity

We only use a few extra variables:

```text
length
curr
prev
count
```

Therefore:

```text
Space Complexity = O(1)
```

---

# Important Optimization

Your approach is logically correct, but it repeatedly traverses the Linked List.

We can optimize the problem to:

```text
Time Complexity: O(n)

Space Complexity: O(1)
```

The key observation is that instead of moving the last node to the front one by one, we can directly find where the list needs to be cut.

---

# Optimal Pattern — Make Cycle → Find New Tail → Break Cycle

Suppose:

```text
1 → 2 → 3 → 4 → 5
```

and:

```text
k = 2
```

The final result is:

```text
4 → 5 → 1 → 2 → 3
```

Instead of performing two separate rotations, we can transform the list in one pass.

---

## Step 1 — Find Length and Tail

Traverse the list once.

At the end:

```text
head
 ↓
1 → 2 → 3 → 4 → 5
                  ↑
                 tail
```

And:

```text
length = 5
```

---

## Step 2 — Reduce `k`

```python
k = k % length
```

If:

```text
k = 0
```

we can immediately return:

```python
return head
```

because no effective rotation is needed.

---

## Step 3 — Create a Circular Linked List

Connect:

```python
tail.next = head
```

Now:

```text
1 → 2 → 3 → 4 → 5
↑                 ↓
└─────────────────┘
```

The Linked List temporarily becomes circular.

---

## Step 4 — Find the New Tail

For a right rotation by `k`:

```text
New Tail Position = length - k - 1
```

from the original head using zero-based movement.

For:

```text
length = 5
k = 2
```

we move:

```text
5 - 2 - 1 = 2 steps
```

Starting from node `1`:

```text
1 → 2 → 3
        ↑
    new_tail
```

So:

```text
new_tail = 3
```

The node after it becomes the new head:

```text
new_head = 4
```

---

## Step 5 — Break the Cycle

```python
new_head = new_tail.next
new_tail.next = None
```

Final:

```text
4 → 5 → 1 → 2 → 3 → None
```

---

# Optimal Python Code

```python
class Solution:
    def rotateRight(
        self,
        head: Optional[ListNode],
        k: int
    ) -> Optional[ListNode]:

        # Empty list or single node
        if head is None or head.next is None:
            return head

        # Step 1: Find length and tail
        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        # Step 2: Reduce unnecessary rotations
        k = k % length

        # No effective rotation
        if k == 0:
            return head

        # Step 3: Make the list circular
        tail.next = head

        # Step 4: Find the new tail
        steps = length - k - 1

        new_tail = head

        for _ in range(steps):
            new_tail = new_tail.next

        # Step 5: Find new head
        new_head = new_tail.next

        # Step 6: Break the cycle
        new_tail.next = None

        return new_head
```

---

# Why Is the Optimal Approach O(n)?

We traverse the Linked List to find:

```text
Length + Tail
```

which takes:

```text
O(n)
```

Then we move to the new tail.

This takes at most:

```text
O(n)
```

Therefore:

```text
O(n) + O(n)
```

becomes:

```text
O(n)
```

We do not perform `k` full traversals.

---

# Approach Comparison

| Approach                 |                  Time | Space |
| ------------------------ | --------------------: | ----: |
| Move Last Node `k` Times | O(n × k), worst O(n²) |  O(1) |
| Circular List + Break    |                  O(n) |  O(1) |

---

# Key Learning

The most important observation in this problem is:

```text
Rotating a list one node at a time
        ↓
Works, but repeats traversal


Find the final cut position directly
        ↓
Avoid repeated work
        ↓
O(n)
```

The important patterns are:

```text
1. Modulo Pattern

   k = k % length

   Used when operations repeat after
   a fixed number of steps.


2. prev + curr Pattern

   Used to find and disconnect
   the last node.


3. Circular Linked List Pattern

   Connect tail to head temporarily.


4. Find the Cut Point

   Find the new tail directly instead
   of rotating one node at a time.


5. Break the Cycle

   new_head = new_tail.next
   new_tail.next = None
```

The main optimization lesson is:

> When an operation is being repeated many times, check whether you can calculate the final position directly instead of simulating every operation.
