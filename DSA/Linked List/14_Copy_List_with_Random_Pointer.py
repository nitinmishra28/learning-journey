# 138. Copy List with Random Pointer

# A linked list is given where each node contains:
#
# next   -> points to the next node
# random -> points to any node in the list or None
#
# Create a deep copy of the linked list.


"""
# Definition for a Node.
class Node:
    def __init__(
        self,
        x: int,
        next: 'Node' = None,
        random: 'Node' = None
    ):
        self.val = int(x)
        self.next = next
        self.random = random
"""


# ============================================================
# Solution 1 - Using Python deepcopy
# Time Complexity: O(n)
# Space Complexity: O(n)
# ============================================================

import copy


class Solution:
    def copyRandomList(
        self,
        head: 'Optional[Node]'
    ) -> 'Optional[Node]':

        new_head = copy.deepcopy(head)

        return new_head


# ============================================================
# Solution 2 - Hash Map
# Time Complexity: O(n)
# Space Complexity: O(n)
# ============================================================

class Solution:
    def copyRandomList(
        self,
        head: 'Optional[Node]'
    ) -> 'Optional[Node]':

        if not head:
            return None

        # Maps every original node to its copied node.
        old_to_new = {}

        # Step 1:
        # Create a copy of every node.
        curr = head

        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        # Step 2:
        # Connect the next and random pointers.
        curr = head

        while curr:

            if curr.next:
                old_to_new[curr].next = old_to_new[curr.next]

            if curr.random:
                old_to_new[curr].random = old_to_new[curr.random]

            curr = curr.next

        # Return the copied version of the original head.
        return old_to_new[head]


# ============================================================
# Explanation
# ============================================================

"""
Solution 1 - deepcopy
---------------------

Python's copy.deepcopy() recursively creates completely new
objects, including the nodes referenced by next and random.

new_head = copy.deepcopy(head)

This is very simple in Python, but in interviews we are generally
expected to implement the deep-copy logic ourselves.


===============================================================

Solution 2 - Hash Map
---------------------

The main challenge is the random pointer.

For example:

Original List:

7 -> 13 -> 11 -> 10 -> 1

A node's random pointer may point to any node:

13.random -> 7

11.random -> 1

10.random -> 11


We need completely new nodes while maintaining the same
relationships.


---------------------------------------------------------------

Why can't we simply copy the pointers?
---------------------------------------

Suppose we write:

new_node.next = old_node.next

Then the copied node would still point to a node from the
original linked list.

That would NOT be a deep copy.

We need:

Original:

[7] -> [13]

Copied:

[7'] -> [13']

The copied 7 must point to copied 13, not original 13.


---------------------------------------------------------------

Why do we use a dictionary?
---------------------------

We create a mapping:

Original Node -> Copied Node

Conceptually:

old_to_new = {

    original_7  : copied_7,
    original_13 : copied_13,
    original_11 : copied_11,
    original_10 : copied_10,
    original_1  : copied_1

}


This allows us to quickly find the copied version of any
original node.


---------------------------------------------------------------

Step 1 - Create all copied nodes
--------------------------------

curr = head

while curr:
    old_to_new[curr] = Node(curr.val)
    curr = curr.next


At this point, all copied nodes exist.

But they are not connected yet.


Original:

7 -> 13 -> 11 -> 10 -> 1


Copies:

7'

13'

11'

10'

1'


---------------------------------------------------------------

Step 2 - Connect next pointers
------------------------------

Suppose:

curr = original 7

curr.next = original 13


We write:

old_to_new[curr].next = old_to_new[curr.next]


Which means:

copied_7.next = copied_13


Therefore:

Original:

7 -> 13


Copied:

7' -> 13'


The copied list never points to the original list.


---------------------------------------------------------------

Step 3 - Connect random pointers
--------------------------------

Suppose:

original_13.random = original_7


We write:

old_to_new[curr].random = old_to_new[curr.random]


Therefore:

copied_13.random = copied_7


The same random-pointer relationship is preserved in the
copied linked list.


---------------------------------------------------------------

Why do we return old_to_new[head]?
----------------------------------

head points to the first node of the ORIGINAL linked list.

The dictionary stores:

original_head -> copied_head


Therefore:

old_to_new[head]

gives us the head of the completely copied linked list.


===============================================================

Complexity
==========

Time Complexity:

O(n)

First traversal:
Create all copied nodes -> O(n)

Second traversal:
Connect next and random pointers -> O(n)

Overall:

O(n)


Space Complexity:

O(n)

The dictionary stores one mapping for every node.


===============================================================

Key Takeaways
=============

1. A deep copy must contain completely new nodes.

2. The copied nodes must not point to nodes from the original list.

3. The dictionary maps each original node to its copied node.

4. First create all nodes.

5. Then connect their next and random pointers.

6. Hash Map gives O(n) time and O(n) extra space.
"""