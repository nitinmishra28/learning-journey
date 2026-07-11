# Delete N Nodes After M Nodes of a Linked List

# Given a linked list, retain M nodes, then delete the next N nodes.
# Continue this process until the end of the linked list.


# ------------------------------------------------------------
# Solution 1 - Iterative Approach
# Time Complexity: O(n)
# Space Complexity: O(1)
# ------------------------------------------------------------

# Definition for singly-linked list.
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

class Solution:
    def linkdelete(self, head, n, m):
        curr = head

        while curr:

            # Skip M nodes
            for _ in range(1, m):
                if curr is None:
                    return head

                curr = curr.next

            if curr is None:
                return head

            # Delete next N nodes
            temp = curr.next

            for _ in range(n):
                if temp is None:
                    break

                temp = temp.next

            # Connect the retained part with the remaining list
            curr.next = temp
            curr = temp

        return head