# Kth Node from End of Linked List

# Given the head of a linked list and an integer k,
# return the kth node from the end of the linked list.


# ------------------------------------------------------------
# Solution 1 - Find Length and Traverse Again
# Time Complexity: O(n)
# Space Complexity: O(1)
# ------------------------------------------------------------

# Node Structure
# class Node:
#     def __init__(self, x):
#         self.data = x
#         self.next = None

class Solution:

    def getLength(self, head):
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next

        return length

    def getKthFromLast(self, head, k):

        # Find the length of the linked list.
        length = self.getLength(head)

        # If k is greater than the length of the list,
        # the kth node from the end does not exist.
        if k > length:
            return -1

        # Position of the required node from the beginning.
        position = length - k + 1

        curr = head

        # Traverse to the required position.
        for _ in range(1, position):
            curr = curr.next

        return curr.data


# ============================================================
# Explanation
# ============================================================

"""
Approach
--------

Instead of traversing from the end (which is not possible in a
singly linked list), we first calculate the length of the list.

After finding the length, we determine the position of the
required node from the beginning.

Formula

Position from beginning = Length - K + 1


---------------------------------------------------------------

Example

Linked List

10 -> 20 -> 30 -> 40 -> 50

Length = 5

Suppose

k = 2

We need the 2nd node from the end.

Position from beginning

= 5 - 2 + 1
= 4

Now move to the 4th node.

10 -> 20 -> 30 -> 40 -> 50
                 ↑

Answer = 40


---------------------------------------------------------------

Another Example

Linked List

1 -> 2 -> 3 -> 4 -> 5 -> 6

Length = 6

k = 4

Position

= 6 - 4 + 1
= 3

Move to the 3rd node.

1 -> 2 -> 3 -> 4 -> 5 -> 6
          ↑

Answer = 3


---------------------------------------------------------------

Why do we calculate

position = length - k + 1 ?

Suppose

Length = 8

k = 1

We need the last node.

Position

8 - 1 + 1 = 8

Correct.


Suppose

k = 8

We need the first node.

Position

8 - 8 + 1 = 1

Correct.


---------------------------------------------------------------

Complexity

Time Complexity:
O(n)

One traversal to find the length.
Another traversal to reach the required node.

Overall complexity remains O(n).

Space Complexity:
O(1)

No extra data structure is used.

---------------------------------------------------------------

Key Takeaways

✔ First calculate the length of the linked list.

✔ Convert the kth node from the end into a position from the beginning.

✔ Traverse once more to reach the required node.

✔ Simple and easy-to-understand approach.
"""