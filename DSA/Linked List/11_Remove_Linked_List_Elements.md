# 203. Remove Linked List Elements

Given the head of a linked list and an integer `val`, remove all the nodes of the linked list that have `Node.val == val`, and return the new head.

# ------------------------------------------------------------

# Solution 1 - Iterative Approach using prev and curr

# Time Complexity: O(n)

# Space Complexity: O(1)

# ------------------------------------------------------------

# Definition for singly-linked list.

# class ListNode:

# def **init**(self, val=0, next=None):

# self.val = val

# self.next = next

class Solution:
def removeElements(
self,
head: Optional[ListNode],
val: int
) -> Optional[ListNode]:

```
    prev = None
    curr = head

    while curr:
        nxt = curr.next

        if curr.val == val:

            # Case 1: Current node is the head node
            if prev is None:
                head = nxt

            # Case 2: Current node is not the head node
            else:
                prev.next = nxt

            # Disconnect the current node
            curr.next = None

            # Move curr to the next node
            curr = nxt

        else:
            # Current node should not be deleted
            prev = curr
            curr = curr.next

    return head
```

# ============================================================

# Solution 1 Explanation

# ============================================================

"""
Approach
--------

We use two pointers:

prev -> keeps track of the previous valid node
curr -> keeps track of the current node

We traverse the linked list and check every node.

If curr.val == val:

```
We need to delete the current node.

There are two possible cases.
```

Case 1: curr is the head node

If prev is None, it means curr is currently pointing
to the head of the linked list.

Example:

7 -> 1 -> 2 -> 3

curr
↓
7 -> 1 -> 2 -> 3

prev = None

Since the head needs to be deleted:

head = curr.next

Now:

head
↓
1 -> 2 -> 3

Case 2: curr is not the head node

Example:

1 -> 2 -> 6 -> 3

```
 prev  curr
   ↓    ↓
```

1 -> 2 -> 6 -> 3

To remove 6:

prev.next = curr.next

Now:

1 -> 2 -------> 3

After removing the node:

curr.next = None

This disconnects the deleted node from the linked list.

Then:

curr = nxt

moves curr forward.

If curr.val != val:

The current node should remain in the linked list.

So we move both pointers:

prev = curr
curr = curr.next

---

Important Point

When we delete a node, we DO NOT move prev.

Example:

1 -> 7 -> 7 -> 3

Suppose:

prev = 1
curr = first 7

After deleting the first 7:

1 -> 7 -> 3

prev must still remain at 1 because the next node
could also need to be deleted.

This allows us to correctly remove consecutive nodes.

---

Why do we update head?

Consider:

7 -> 7 -> 7 -> 7

val = 7

Initially:

prev = None
curr = head

Because curr is the head and needs to be deleted:

head = nxt

This continues until all nodes are removed.

Finally:

head = None

---

Complexity

Time Complexity:
O(n)

Every node is visited once.

Space Complexity:
O(1)

Only a few pointer variables are used:

prev
curr
nxt

No extra data structure is required.

---

Pattern

Linked List Deletion using:

prev + curr pointers

Special handling is required when deleting the head node.
"""

# ============================================================

# Solution 2 - Iterative Approach using a Dummy Node

# Time Complexity: O(n)

# Space Complexity: O(1)

# ============================================================

class Solution:
def removeElements(
self,
head: Optional[ListNode],
val: int
) -> Optional[ListNode]:

```
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

# ============================================================

# Solution 2 Explanation

# ============================================================

"""
Approach
--------

We traverse the linked list once.

For every node:

• If its value equals 'val',
skip the node.

• Otherwise,
move the prev pointer forward.

A dummy node is used so that deleting
the head node becomes easy.

---

Example

Input:

1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6

val = 6

Initially:

dummy -> 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6

When curr reaches the first 6:

dummy -> 1 -> 2 -------> 3 -> 4 -> 5 -> 6

6

The node is skipped.

Continue traversing...

When curr reaches the last 6:

dummy -> 1 -> 2 -> 3 -> 4 -> 5

Done.

---

Why do we use a Dummy Node?

Suppose the head itself needs to be removed.

Example:

6 -> 1 -> 2 -> 3

Without a dummy node,
changing the head requires special handling.

With a dummy node:

dummy -> 6 -> 1 -> 2 -> 3

Removing 6 is simply:

dummy.next = 1

No extra conditions are needed.

---

Why do we return dummy.next?

The dummy node itself is not part of the answer.

dummy
↓

[-1] -> 1 -> 2 -> 3

The real linked list starts from:

dummy.next

Therefore:

return dummy.next

---

Complexity

Time Complexity:
O(n)

Space Complexity:
O(1)

---

Key Takeaways

✔ Both approaches are optimal with O(n) time and O(1) space.

✔ The prev + curr approach requires special handling when
deleting the head.

✔ The dummy node approach removes the need for a special
head-deletion condition.

✔ When deleting a node, do not move prev.

✔ Dummy nodes are a very common linked list interview pattern.
"""
