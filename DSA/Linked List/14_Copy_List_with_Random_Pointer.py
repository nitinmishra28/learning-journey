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











# ============================================================
# Solution 3 - Interweaving Nodes (Optimal)
# Time Complexity: O(n)
# Space Complexity: O(1)
# ============================================================

class Solution:
    def copyRandomList(
        self,
        head: 'Optional[Node]'
    ) -> 'Optional[Node]':

        if not head:
            return None

        # ----------------------------------------------------
        # Step 1: Create copied nodes and insert each copy
        # immediately after its original node.
        #
        # A -> B -> C
        #
        # becomes
        #
        # A -> A' -> B -> B' -> C -> C'
        # ----------------------------------------------------

        curr = head

        while curr:
            forward = curr.next

            copy_node = Node(curr.val)

            curr.next = copy_node
            copy_node.next = forward

            curr = forward


        # ----------------------------------------------------
        # Step 2: Connect random pointers of copied nodes.
        #
        # If:
        #
        # A.random -> C
        #
        # Then:
        #
        # A'.random -> C'
        #
        # Since C' is immediately after C:
        #
        # curr.random.next = copied version of curr.random
        # ----------------------------------------------------

        curr = head

        while curr:

            if curr.random:
                curr.next.random = curr.random.next

            # Move to the next ORIGINAL node.
            curr = curr.next.next


        # ----------------------------------------------------
        # Step 3: Separate the original and copied linked lists.
        #
        # Before:
        #
        # A -> A' -> B -> B' -> C -> C'
        #
        # After:
        #
        # Original:
        # A -> B -> C
        #
        # Copy:
        # A' -> B' -> C'
        # ----------------------------------------------------

        curr = head
        copy_head = head.next

        while curr:
            copy_node = curr.next

            # Restore original list
            curr.next = copy_node.next

            # Connect copied list
            if copy_node.next:
                copy_node.next = copy_node.next.next

            curr = curr.next

        return copy_head


# ============================================================
# Explanation
# ============================================================

"""
Why is this approach optimal?
-----------------------------

The Hash Map approach stores:

Original Node -> Copied Node

This requires O(n) extra space.

The interweaving approach avoids the dictionary by placing
each copied node immediately after its original node.

This gives us a direct relationship:

Original Node -> Original Node.next -> Copied Node


===============================================================
Step 1 - Insert Copied Nodes
===============================================================

Original:

A -> B -> C


Create a copy of A and insert it after A:

A -> A' -> B -> C


Create a copy of B:

A -> A' -> B -> B' -> C


Create a copy of C:

A -> A' -> B -> B' -> C -> C'


Now every original node's copy can be accessed using:

original.next


For example:

A.next = A'

B.next = B'

C.next = C'


===============================================================
Step 2 - Connect Random Pointers
===============================================================

Suppose:

A.random -> C


We want:

A'.random -> C'


We know:

A.next = A'

and:

C.next = C'


Therefore:

A.next.random = A.random.next


In code:

curr.next.random = curr.random.next


Here:

curr             = A

curr.next        = A'

curr.random      = C

curr.random.next = C'


Therefore:

A'.random = C'


===============================================================
Step 3 - Separate Both Lists
===============================================================

Currently:

A -> A' -> B -> B' -> C -> C'


We need to restore the original list:

A -> B -> C


And create the copied list:

A' -> B' -> C'


For every original node:

curr.next = copy_node.next

restores the original next pointer.


Then:

copy_node.next = copy_node.next.next

connects one copied node to the next copied node.


Finally, we get:

Original:

A -> B -> C


Copied:

A' -> B' -> C'


===============================================================
Complexity
===============================================================

Time Complexity:

O(n)

We traverse the linked list three times:

1. Create copied nodes      -> O(n)
2. Set random pointers      -> O(n)
3. Separate both lists      -> O(n)

O(n) + O(n) + O(n) = O(n)


Space Complexity:

O(1)

No Hash Map or additional data structure is used.

Note:

The newly created nodes are required for the answer,
so they are not counted as auxiliary extra space.


===============================================================
Comparison
===============================================================

Solution 1 - deepcopy

Time  : O(n)
Space : O(n)


Solution 2 - Hash Map

Time  : O(n)
Space : O(n)


Solution 3 - Interweaving Nodes

Time  : O(n)
Space : O(1) Extra Space


===============================================================
Key Pattern
===============================================================

The most important trick is:

Original node's copy:

curr.next


Copied version of the random node:

curr.random.next


Therefore:

curr.next.random = curr.random.next


This is what allows us to remove the Hash Map completely.
"""