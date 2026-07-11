# 160. Intersection of Two Linked Lists

# Given the heads of two singly linked lists, return the node at which
# the two lists intersect. If the two linked lists have no intersection,
# return None.


# ------------------------------------------------------------
# Solution 1 - Two Pointer Approach
# Time Complexity: O(m + n)
# Space Complexity: O(1)
# ------------------------------------------------------------

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(
        self,
        headA: ListNode,
        headB: ListNode
    ) -> Optional[ListNode]:

        curr1 = headA
        curr2 = headB

        while curr1 != curr2:
            curr1 = curr1.next if curr1 else headB
            curr2 = curr2.next if curr2 else headA

        return curr1


# ============================================================
# Explanation
# ============================================================

"""
Approach
--------

We use two pointers, one starting from each linked list.

Pointer 1 starts from List A.
Pointer 2 starts from List B.

Both pointers move one step at a time.

When a pointer reaches the end of its list,
it starts traversing the other linked list.

Eventually,

• Both pointers meet at the intersection node.

OR

• Both become None if no intersection exists.


---------------------------------------------------------------

Example

List A

4 → 1
      \
       8 → 4 → 5

List B

5 → 6 → 1
          \
           8 → 4 → 5


Initially

curr1 = 4
curr2 = 5


After reaching the end

curr1 starts from List B

curr2 starts from List A


Eventually

curr1 == curr2

Both point to

8

which is the intersection node.


---------------------------------------------------------------

Why does this work?

Suppose

Length of List A = m

Length of List B = n

Pointer 1 travels

A + B

Pointer 2 travels

B + A

Both travel exactly

m + n

nodes.

If an intersection exists,
they reach it at the same time.

If no intersection exists,
both pointers become None together.

This removes the need to calculate
the lengths of both linked lists.

---------------------------------------------------------------

Example

List A

1 → 2 → 3 → 7 → 8

List B

4 → 5 → 7 → 8


Pointer 1

1 → 2 → 3 → 7 → 8 → None
                 ↓
4 → 5 → 7 → 8


Pointer 2

4 → 5 → 7 → 8 → None
          ↓
1 → 2 → 3 → 7 → 8


Both eventually meet at

7

---------------------------------------------------------------

Complexity

Time Complexity:
O(m + n)

Each pointer traverses both linked lists at most once.

Space Complexity:
O(1)

No extra data structure is used.

---------------------------------------------------------------

Key Takeaways

✔ No need to calculate the lengths of the linked lists.

✔ No extra space is required.

✔ Each pointer traverses exactly m + n nodes.

✔ Elegant and optimal two-pointer solution.

✔ One of the most important linked list interview patterns.
"""