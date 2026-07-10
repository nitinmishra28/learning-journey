# 234. Palindrome Linked List

# Given the head of a singly linked list, return true if it is a palindrome,
# otherwise return false.


# ------------------------------------------------------------
# Solution 1 - Find Middle, Reverse Second Half, and Compare
# Time Complexity: O(n)
# Space Complexity: O(1)
# ------------------------------------------------------------

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getMiddle(self, head):
        slow = head
        fast = head
        middleNodePrev = None

        while fast and fast.next:
            middleNodePrev = slow
            slow = slow.next
            fast = fast.next.next

        return middleNodePrev, slow

    def reverse(self, head):
        prev = None
        curr = head

        while curr:
            forward = curr.next
            curr.next = prev
            prev = curr
            curr = forward

        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True

        # Step 1: Find the middle of the linked list
        firstHalfHead = head
        middleNodePrev, middleNode = self.getMiddle(head)

        # Split the linked list into two halves
        middleNodePrev.next = None

        # Step 2: Reverse the second half
        secondHalfHead = self.reverse(middleNode)

        # Step 3: Compare both halves
        while firstHalfHead and secondHalfHead:
            if firstHalfHead.val != secondHalfHead.val:
                return False

            firstHalfHead = firstHalfHead.next
            secondHalfHead = secondHalfHead.next

        return True