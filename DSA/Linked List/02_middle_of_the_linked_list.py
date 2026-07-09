# 876. Middle of the Linked List

# Given the head of a singly linked list, return the middle node of the linked list.
#
# If there are two middle nodes, return the second middle node.


# ------------------------------------------------------------
# Solution 1 - Find the length first, then traverse to the
#              middle node.
# Time Complexity: O(n)
# Space Complexity: O(1)
# ------------------------------------------------------------

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getLength(self, head):
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next

        return length

    def getMiddleNode(self, head, middle):
        curr = head

        for _ in range(middle):
            curr = curr.next

        return curr

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = self.getLength(head)
        middle = length // 2

        return self.getMiddleNode(head, middle)


# ------------------------------------------------------------
# Solution 2 - Fast and Slow Pointer (Optimal)
# Time Complexity: O(n)
# Space Complexity: O(1)
# ------------------------------------------------------------

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow