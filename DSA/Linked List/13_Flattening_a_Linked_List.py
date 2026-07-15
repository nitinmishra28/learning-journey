# Flattening a Linked List

# Given a linked list where every node has:
# - next pointer: points to the next linked list
# - bottom pointer: points to a sorted linked list
#
# Flatten the entire linked list into a single sorted linked list
# using the bottom pointers.


# ------------------------------------------------------------
# Solution - Recursion + Merge Two Sorted Linked Lists
# Time Complexity: O(N * M) in the common recursive merge analysis
# Space Complexity: O(N) due to the recursive call stack
# ------------------------------------------------------------

"""
class Node:
    def __init__(self, d):
        self.data = d
        self.next = None
        self.bottom = None
"""


class Solution:

    def merge(self, l1, l2):
        # Dummy node to simplify the merging process
        dummy = Node(-1)
        temp = dummy

        # Merge two sorted bottom-linked lists
        while l1 and l2:

            if l1.data <= l2.data:
                temp.bottom = l1
                l1 = l1.bottom
            else:
                temp.bottom = l2
                l2 = l2.bottom

            temp = temp.bottom

            # The flattened list should only use bottom pointers
            temp.next = None

        # Attach the remaining nodes
        if l1:
            temp.bottom = l1

        if l2:
            temp.bottom = l2

        # Return the actual head after the dummy node
        return dummy.bottom

    def flatten(self, root):

        # Base Case:
        # No list or only one vertical linked list
        if root is None or root.next is None:
            return root

        # Step 1:
        # Recursively flatten all linked lists on the right
        flattenedRight = self.flatten(root.next)

        # Step 2:
        # Merge the current vertical list with the
        # already flattened right-side list
        root = self.merge(root, flattenedRight)

        return root


# ============================================================
# Explanation
# ============================================================

"""
Approach
--------

The linked list contains two types of pointers:

next   -> connects the heads horizontally

bottom -> connects nodes vertically


Example:

5  -> 10 -> 19 -> 28
|      |     |     |
7      20    22    35
|            |     |
8            50    40
|                  |
30                 45


Each vertical linked list is already sorted.

Our goal is to create one sorted linked list using
only the bottom pointers.


---------------------------------------------------------------

Main Idea
---------

We use recursion to flatten the linked lists from
right to left.

Suppose we have:

List1 -> List2 -> List3 -> List4

The recursion first reaches List4.

Then:

Merge List3 with List4

Then:

Merge List2 with the flattened result

Then:

Merge List1 with the flattened result


Conceptually:

flatten(List1)

    flatten(List2)

        flatten(List3)

            flatten(List4)

            return List4

        merge(List3, List4)

    merge(List2, flattenedRight)

merge(List1, flattenedRight)


---------------------------------------------------------------

Base Case
---------

if root is None or root.next is None:
    return root


If root is None:

There is nothing to flatten.


If root.next is None:

There is only one vertical linked list remaining.

Example:

5
|
7
|
8
|
30

It is already flattened, so we simply return root.


---------------------------------------------------------------

Recursive Call
--------------

flattenedRight = self.flatten(root.next)


Suppose:

5 -> 10 -> 19 -> 28


When root is 5, we first call:

flatten(10)


That function internally calls:

flatten(19)


Which calls:

flatten(28)


Since 28.next is None, recursion returns 28.

Now the recursion starts returning back.


---------------------------------------------------------------

Important Point:
Where does root move?
---------------------

We do NOT manually increment root like:

root = root.next


The recursion handles moving to the right.

When we call:

self.flatten(root.next)

a new function call receives root.next as its root.


Example:

First call:

root = 5

self.flatten(root.next)

Second call:

root = 10

self.flatten(root.next)

Third call:

root = 19

self.flatten(root.next)

Fourth call:

root = 28


So every recursive call has its own root variable.

That is how recursion moves through the horizontal list.


---------------------------------------------------------------

Merge Step
----------

After the right side is completely flattened:

root = self.merge(root, flattenedRight)


Suppose:

Current List:

10
|
20


Flattened Right:

19
|
22
|
28
|
35


The merge function combines them into:

10
|
19
|
20
|
22
|
28
|
35


The result is returned to the previous recursive call.


---------------------------------------------------------------

Why Dummy Node?
---------------

dummy = Node(-1)

The dummy node provides a temporary starting point
while merging two linked lists.

Instead of separately handling the first node,
we can always write:

temp.bottom = selected_node
temp = temp.bottom


Finally, the actual merged list starts from:

dummy.bottom

Therefore we return:

return dummy.bottom


---------------------------------------------------------------

Why do we set:

temp.next = None
----------------

The final flattened linked list should use only
bottom pointers.

During merging, nodes may still contain their old
horizontal next pointers.

Setting:

temp.next = None

removes those horizontal connections from the nodes
that are added during the merge.


---------------------------------------------------------------

Key Takeaways
-------------

1. Recursion moves to the right side of the linked list.

2. The base case returns the last vertical linked list.

3. While recursion returns, we merge from right to left.

4. merge() works like merging two sorted linked lists.

5. The final flattened list is connected using bottom pointers.

6. The dummy node simplifies the merge operation.
"""