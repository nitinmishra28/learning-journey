# 21. Merge Two Sorted Lists

# Given the heads of two sorted linked lists, merge them into one
# sorted linked list and return its head.


# ------------------------------------------------------------
# Solution 1 - Iterative Approach using a Dummy Node
# Time Complexity: O(n + m)
# Space Complexity: O(1)
# ------------------------------------------------------------

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        # Create a dummy node.
        # It acts as a temporary starting point for the merged list.
        dummy = ListNode(-1)

        # Tail always points to the last node of the merged list.
        tail = dummy

        # Compare nodes from both lists and attach the smaller one.
        while list1 and list2:

            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            # Move tail to the newly added node.
            tail = tail.next

        # Attach the remaining nodes.
        if list1:
            tail.next = list1
        else:
            tail.next = list2

        # The actual merged list starts after the dummy node.
        return dummy.next


# ============================================================
# Explanation
# ============================================================

"""
Why do we create a Dummy Node?

dummy = ListNode(-1)

A dummy node is a temporary node that acts as the starting point
of the merged linked list. It simplifies the implementation by
avoiding special handling for the first node.

Without a Dummy Node:
---------------------
We would need to check if the head is None every time we add the
first node.

Example:

if head is None:
    head = node
    tail = head
else:
    tail.next = node

With a Dummy Node:
------------------
We can always write the same code.

tail.next = node
tail = tail.next

No special case is required.

---------------------------------------------------------------

Example:

List 1:
1 -> 3 -> 5

List 2:
2 -> 4 -> 6


Initially

dummy(-1)

tail
 ↓
[-1]


After inserting 1

[-1] -> 1
         ↑
       tail


After inserting 2

[-1] -> 1 -> 2
              ↑
            tail


After inserting 3

[-1] -> 1 -> 2 -> 3
                   ↑
                 tail

...

Finally

[-1] -> 1 -> 2 -> 3 -> 4 -> 5 -> 6

---------------------------------------------------------------

Why is the value -1?

The value stored in the dummy node does not matter.

It could be

ListNode(0)
ListNode(-1)
ListNode(100)

because this node is never returned.
It only helps us build the new linked list.

---------------------------------------------------------------

Why do we return dummy.next instead of dummy?

The dummy node is not part of the answer.

dummy
  ↓

[-1] -> 1 -> 2 -> 3 -> 4 -> 5 -> 6

Returning

return dummy

would return

-1 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6

which is incorrect.

The actual merged list starts from

dummy.next

Therefore we return

return dummy.next

which gives

1 -> 2 -> 3 -> 4 -> 5 -> 6

---------------------------------------------------------------

Key Takeaway

✔ Dummy Node removes special handling for the first node.
✔ Makes linked list code cleaner and easier to write.
✔ Very commonly used in Linked List interview problems.
"""