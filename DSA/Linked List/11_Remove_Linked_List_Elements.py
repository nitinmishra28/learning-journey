# 203. Remove Linked List Elements

# Given the head of a linked list and an integer val,
# remove all the nodes of the linked list that have
# Node.val == val, and return the new head.


# ------------------------------------------------------------
# Solution 1 - Iterative Approach using a Dummy Node
# Time Complexity: O(n)
# Space Complexity: O(1)
# ------------------------------------------------------------

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

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


# ============================================================
# Explanation
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

---------------------------------------------------------------

Example

Input

1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6

val = 6


Initially

dummy -> 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6


When curr reaches the first 6

dummy -> 1 -> 2 -------> 3 -> 4 -> 5 -> 6
                  \
                   6

The node is skipped.

Continue traversing...

When curr reaches the last 6

dummy -> 1 -> 2 -> 3 -> 4 -> 5

Done.

---------------------------------------------------------------

Why do we use a Dummy Node?

Suppose the head itself needs to be removed.

Example

6 -> 1 -> 2 -> 3

Without a dummy node,
changing the head requires special handling.

With a dummy node,

dummy -> 6 -> 1 -> 2 -> 3

Removing 6 is simply

dummy.next = 1

No extra conditions are needed.

---------------------------------------------------------------

Why do we return dummy.next?

dummy itself is not part of the answer.

dummy
  ↓

[-1] -> 1 -> 2 -> 3

The real linked list starts from

dummy.next

Therefore,

return dummy.next

---------------------------------------------------------------

Complexity

Time Complexity:
O(n)

Space Complexity:
O(1)

---------------------------------------------------------------

Key Takeaways

✔ Dummy node simplifies deleting the head node.

✔ Traverse the linked list only once.

✔ No extra data structure is required.

✔ A common linked list interview pattern.
"""