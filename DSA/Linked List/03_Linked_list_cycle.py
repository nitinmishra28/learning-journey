# 141. Linked List Cycle

# Given head, the head of a linked list, determine if the linked list
# has a cycle in it.


# ------------------------------------------------------------
# Solution 1 - Hash Set
# Time Complexity: O(n)
# Space Complexity: O(n)
# ------------------------------------------------------------

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()

        curr = head

        while curr:
            if curr in visited:
                return True

            visited.add(curr)
            curr = curr.next

        return False


# ------------------------------------------------------------
# Solution 2 - Fast & Slow Pointer (Optimal)
# Time Complexity: O(n)
# Space Complexity: O(1)
# ------------------------------------------------------------

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False