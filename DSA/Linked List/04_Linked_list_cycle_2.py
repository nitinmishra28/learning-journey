# 142. Linked List Cycle II

# Given the head of a linked list, return the node where the cycle begins.
# If there is no cycle, return None.


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
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        curr = head

        while curr:
            if curr in visited:
                return curr

            visited.add(curr)
            curr = curr.next

        return None


# ------------------------------------------------------------
# Solution 2 - Floyd's Cycle Detection Algorithm (Optimal)
# Time Complexity: O(n)
# Space Complexity: O(1)
#Take Reference - https://www.youtube.com/watch?v=jcZtMh_jov0
# ------------------------------------------------------------

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        # Detect whether a cycle exists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            return None

        # Find the starting node of the cycle
        slow = head

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow