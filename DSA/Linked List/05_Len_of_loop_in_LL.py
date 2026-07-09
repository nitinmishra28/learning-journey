# Find the Length of Loop in a Linked List

# Given the head of a linked list, determine the length of the loop.
# If there is no loop, return 0.


# ------------------------------------------------------------
# Solution 1 - Floyd's Cycle Detection Algorithm
# Time Complexity: O(n)
# Space Complexity: O(1)
# ------------------------------------------------------------

# Definition for singly-linked list.
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

class Solution:
    def findLengthOfLoop(self, head):
        slow = head
        fast = head

        # Detect the cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                count = 1
                fast = fast.next

                # Count the number of nodes in the loop
                while slow != fast:
                    count += 1
                    fast = fast.next

                return count

        return 0