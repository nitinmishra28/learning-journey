# 206. Reverse Linked List

# Given the head of a singly linked list, reverse the list,
# and return the reversed list.


# ------------------------------------------------------------
# Solution 1 - Iterative Approach
# Time Complexity: O(n)
# Space Complexity: O(1)
# ------------------------------------------------------------

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            forward = curr.next
            curr.next = prev
            prev = curr
            curr = forward

        return prev


# ------------------------------------------------------------
# Solution 2 - Recursive Approach
# Time Complexity: O(n)
# Space Complexity: O(n)   # Recursive call stack
# ------------------------------------------------------------

class Solution:
    def recursiveWay(self, prev, curr):
        # Base Case
        if curr is None:
            return prev

        forward = curr.next
        curr.next = prev

        return self.recursiveWay(curr, forward)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.recursiveWay(None, head)