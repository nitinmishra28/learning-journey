# 148. Sort List

# This file contains:
# 1. Recursive Merge Sort (O(n log n), O(log n) stack)
# 2. Bottom-Up Iterative Merge Sort (O(n log n), O(1) extra space)

from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class RecursiveSolution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        prev = None
        slow = head
        fast = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None

        left = self.sortList(head)
        right = self.sortList(slow)

        return self.merge(left, right)

    def merge(self, left, right):
        dummy = ListNode(-1)
        tail = dummy

        while left and right:
            if left.val <= right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next

        tail.next = left if left else right
        return dummy.next



# Solution 2

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        length = self.getLength(head)
        dummy = ListNode(0)
        dummy.next = head
        size = 1

        while size < length:
            prev = dummy
            curr = dummy.next

            while curr:
                left = curr
                right = self.split(left, size)
                curr = self.split(right, size)

                merged_head, merged_tail = self.merge(left, right)
                prev.next = merged_head
                prev = merged_tail

            size *= 2

        return dummy.next

    def getLength(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    def split(self, head, size):
        if not head:
            return None

        for _ in range(size - 1):
            if head.next:
                head = head.next
            else:
                break

        second = head.next
        head.next = None
        return second

    def merge(self, left, right):
        dummy = ListNode(-1)
        tail = dummy

        while left and right:
            if left.val <= right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next

        tail.next = left if left else right

        while tail.next:
            tail = tail.next

        return dummy.next, tail


'''
Bottom-Up Merge Sort

Pass 1: Merge sublists of size 1
Pass 2: Merge sublists of size 2
Pass 3: Merge sublists of size 4
Pass 4: Merge sublists of size 8
...

Time Complexity : O(n log n)
Space Complexity: O(1)
'''
