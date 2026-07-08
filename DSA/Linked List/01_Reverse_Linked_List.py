"""
LeetCode 206 - Reverse Linked List

Approach:
1. Use two pointers: prev and curr.
2. Reverse the next pointer of each node.
3. Move pointers forward until the end.
4. Return prev as the new head.

Time Complexity: O(n)
Space Complexity: O(1)
"""
# Linked List

## 206. Reverse Linked List

### Problem
# Reverse a singly linked list.

# ### Approach
# - Maintain two pointers: `prev` and `curr`.
# - Traverse the list.
# - Store the next node.
# - Reverse the current node's pointer.
# - Move both pointers forward.
# - Return `prev` as the new head.

### Time Complexity

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr is not None:
            forward = curr.next

            curr.next = prev
            prev = curr
            curr = forward
        
        return prev
        