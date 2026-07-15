# 🔗 Linked List — Complete Notes in Python

A **Linked List** is one of the most important linear data structures in DSA.

Unlike an array, where elements are stored together, a Linked List is made of separate objects called **nodes** that are connected using references.

Understanding Linked Lists is mainly about understanding:

* Nodes
* References
* `head` and `tail`
* Traversal
* Changing links
* Pointer/reference manipulation
* Important Linked List patterns
* Edge cases
* Time and space complexity

> In Python, variables such as `head`, `curr`, `prev`, and `next_node` store **references to objects**, not raw memory addresses like pointers in C++.

---

# 1. What is a Linked List?

A Linked List is a linear collection of nodes.

Each node usually contains two things:

```text
┌──────────────┬──────────────┐
│     Data     │     Next     │
└──────────────┴──────────────┘
```

For example:

```text
head
 ↓
10 → 20 → 30 → 40 → None
```

Here:

* `10`, `20`, `30`, and `40` are stored inside nodes.
* Every node contains a reference to the next node.
* `head` stores a reference to the first node.
* The final node stores `None` in its `next`.
* `None` represents the end of the Linked List.

---

# 2. Why Do We Need Linked Lists?

Consider an array:

```python
arr = [10, 20, 30, 40]
```

Arrays provide very fast random access.

```python
arr[2]
```

This takes:

```text
O(1)
```

However, inserting an element at the beginning may require shifting existing elements.

Conceptually:

```text
Before:

10 20 30 40

Insert 5:

5 10 20 30 40
```

In a Linked List, we don't shift elements.

We change connections.

```text
Before:

10 → 20 → 30

Insert 5:

5 → 10 → 20 → 30
```

This makes certain insertion and deletion operations very efficient when we already have access to the correct node.

---

# 3. Array vs Linked List

| Feature             | Array                        | Linked List         |
| ------------------- | ---------------------------- | ------------------- |
| Memory              | Contiguous                   | Non-contiguous      |
| Random Access       | O(1)                         | O(n)                |
| Search              | O(n)                         | O(n)                |
| Insert at Beginning | Usually O(n)                 | O(1)                |
| Delete at Beginning | Usually O(n)                 | O(1)                |
| Dynamic Growth      | Requires resizing internally | Naturally dynamic   |
| Extra Memory        | No link field                | Requires references |
| Cache Friendliness  | Better                       | Usually worse       |

The biggest disadvantage of a Linked List is:

```text
No direct/random access
```

If we want the fifth node, we must start from the beginning and move node by node.

---

# 4. Understanding a Node in Python

A node can be created using a class.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

Create a node:

```python
node1 = Node(10)
```

Conceptually:

```text
node1
  ↓
┌──────────┬──────────┐
│    10    │   None   │
└──────────┴──────────┘
```

Create another node:

```python
node2 = Node(20)
```

Connect them:

```python
node1.next = node2
```

Now:

```text
node1              node2
 ↓                   ↓
10  ───────────────→ 20 → None
```

The important thing is:

```python
node1.next = node2
```

does not copy `node2`.

It stores a reference to the same `node2` object.

---

# 5. References in Python

In C++, Linked Lists are often explained using pointers.

In Python, we normally use **object references**.

Consider:

```python
a = Node(10)
b = a
```

Now both variables refer to the same object.

```text
a ─────┐
       ↓
      [10]
       ↑
b ─────┘
```

Therefore:

```python
b.data = 100
```

also changes:

```python
a.data
```

to:

```text
100
```

because `a` and `b` are referencing the same node.

This concept is extremely important in Linked Lists.

---

# 6. What is `head`?

`head` is simply a variable containing a reference to the first node.

```python
head = Node(10)
```

Suppose:

```text
head
 ↓
10 → 20 → 30 → None
```

The entire Linked List can be accessed through `head`.

If we lose `head` and have no other reference to the first node, we may lose access to that part of the list.

For example:

```python
head = head.next
```

Before:

```text
head
 ↓
10 → 20 → 30
```

After:

```text
     head
       ↓
10    20 → 30
```

Now `head` points to `20`.

If nothing else references node `10`, Python can eventually remove it through garbage collection.

---

# 7. What is `tail`?

`tail` usually refers to the last node.

```text
head                 tail
 ↓                     ↓
10 → 20 → 30 → 40 → None
```

The defining property of the tail in a normal Linked List is:

```python
tail.next is None
```

Keeping a `tail` reference can make insertion at the end faster.

Without a tail:

```text
Insert at end → O(n)
```

because we must traverse the list.

With a tail:

```text
Insert at end → O(1)
```

because we already know the last node.

---

# 8. Empty Linked List

An empty Linked List has no nodes.

```python
head = None
```

Representation:

```text
head
 ↓
None
```

Many Linked List problems require handling this case.

Always think about:

```python
if head is None:
```

or simply:

```python
if not head:
```

---

# 9. Single Node Linked List

A single-node list looks like:

```text
head
 ↓
10 → None
```

Here:

```python
head.next is None
```

If maintaining a tail:

```python
head is tail
```

Single-node lists are important edge cases for insertion, deletion, reversal, and pointer movement.

---

# 10. Traversing a Linked List

To visit every node, we use a temporary reference.

```python
curr = head

while curr:
    print(curr.data)
    curr = curr.next
```

Suppose:

```text
head
 ↓
10 → 20 → 30 → None
```

Initially:

```text
curr
 ↓
10 → 20 → 30
```

After:

```python
curr = curr.next
```

we get:

```text
     curr
       ↓
10 → 20 → 30
```

Eventually:

```text
curr = None
```

and the loop stops.

---

# 11. Why Should We Use `curr` Instead of Moving `head`?

Technically, this works:

```python
while head:
    print(head.data)
    head = head.next
```

But we keep changing the `head` variable.

It is safer to use:

```python
curr = head
```

and traverse using:

```python
curr
```

This preserves the original head reference.

---

# 12. Insertion Concepts

Insertion in a Linked List means creating a node and changing connections.

## Insert at Beginning

Before:

```text
head
 ↓
10 → 20 → 30
```

Create:

```python
new_node = Node(5)
```

Connect:

```python
new_node.next = head
head = new_node
```

After:

```text
head
 ↓
5 → 10 → 20 → 30
```

Time Complexity:

```text
O(1)
```

---

## Insert at End

Without a tail, traverse until:

```python
curr.next is None
```

Then:

```python
curr.next = new_node
```

Time:

```text
O(n)
```

With a tail:

```python
tail.next = new_node
tail = new_node
```

Time:

```text
O(1)
```

---

## Insert Between Nodes

Suppose:

```text
10 → 20 → 30
```

Insert `25` after `20`.

Correct order:

```python
new_node.next = curr.next
curr.next = new_node
```

Result:

```text
10 → 20 → 25 → 30
```

The order matters because changing a link too early can make us lose access to the remaining list.

---

# 13. Deletion Concepts

Deletion means removing a node from the chain by changing references.

Suppose:

```text
10 → 20 → 30
```

To remove `20`:

```text
10 ───────→ 30
```

Conceptually:

```python
prev.next = curr.next
```

The important idea is:

> We usually do not physically "destroy" a node manually in Python.

We remove references to it.

If nothing references that object anymore, Python's garbage collector can clean it up.

---

# 14. The Most Important Rule of Linked Lists

Whenever changing a link, make sure you do not lose the remaining list.

Suppose:

```text
10 → 20 → 30
```

If `curr` points to `10` and we immediately do:

```python
curr.next = None
```

we lose the connection from `10` to `20`.

Therefore, when necessary, first save the next node:

```python
next_node = curr.next
```

Then modify the connection.

This gives us the most important Linked List pattern:

```text
Previous → Current → Next
```

---

# 15. The `prev`, `curr`, `next_node` Pattern

This is the foundation of Linked List pointer manipulation.

```python
prev = None
curr = head

while curr:
    next_node = curr.next

    # modify connection

    prev = curr
    curr = next_node
```

The roles are:

### `prev`

Stores the previous node.

### `curr`

Stores the node currently being processed.

### `next_node`

Temporarily saves the remaining list.

Visual:

```text
prev       curr       next_node
 ↓           ↓            ↓
10    →     20     →      30
```

This pattern is heavily used whenever links need to be changed.

---

# 16. Reversing Links

Suppose:

```text
10 → 20 → 30 → None
```

We want:

```text
None ← 10 ← 20 ← 30
```

The core operation is:

```python
curr.next = prev
```

But before changing `curr.next`, save it:

```python
next_node = curr.next
```

Complete pattern:

```python
prev = None
curr = head

while curr:
    next_node = curr.next

    curr.next = prev

    prev = curr
    curr = next_node

head = prev
```

The order is critical:

```text
Save
↓
Reverse
↓
Move prev
↓
Move curr
```

Remember:

```text
next_node = curr.next
curr.next = prev
prev = curr
curr = next_node
```

---

# 17. Slow and Fast Pointer Pattern

Two references move at different speeds.

```python
slow = head
fast = head
```

Movement:

```python
slow = slow.next
fast = fast.next.next
```

Conceptually:

```text
slow → moves 1 step
fast → moves 2 steps
```

This pattern works because the difference in movement speed creates useful relationships between the two references.

Common uses include:

* Finding the middle
* Detecting cycles
* Finding a cycle's starting point
* Splitting a list

Safe loop condition:

```python
while fast and fast.next:
```

This is important because before accessing:

```python
fast.next.next
```

we must make sure the required references exist.

---

# 18. Floyd's Cycle Detection Concept

A cycle exists when some node eventually points back to an earlier node.

```text
10 → 20 → 30 → 40
          ↑       ↓
          ←───────
```

Using slow and fast references:

```python
slow = slow.next
fast = fast.next.next
```

If there is a cycle, they eventually meet.

```python
if slow is fast:
```

Notice:

```python
is
```

checks whether both variables reference the same object.

This is different from comparing values.

Two different nodes can both contain:

```text
10
```

but they are still different nodes.

---

# 19. Node Identity vs Node Value

This distinction is extremely important.

Suppose:

```text
Node A → data = 10
Node B → data = 10
```

They have equal values but are different objects.

Value comparison:

```python
node1.data == node2.data
```

Identity comparison:

```python
node1 is node2
```

When checking whether two pointers reached the exact same node, use identity.

---

# 20. Dummy Node Pattern

A dummy node is an extra temporary node created before the actual Linked List.

```python
dummy = Node(-1)
```

Conceptually:

```text
dummy → actual list
```

The value:

```text
-1
```

usually has no importance.

It can often be any value because the dummy node is not part of the final result.

The main purpose is to simplify edge cases involving the head.

Example setup:

```python
dummy = Node(-1)
tail = dummy
```

As nodes are added:

```python
tail.next = new_node
tail = tail.next
```

Finally:

```python
return dummy.next
```

Why?

Because:

```text
dummy → first actual node → second actual node
          ↑
       dummy.next
```

The dummy node is especially useful when:

* The head may change
* Building a new Linked List
* Removing nodes
* Merging lists

---

# 21. Dummy vs Tail

This is a common source of confusion.

```python
dummy = Node(-1)
tail = dummy
```

Initially, both reference the same node.

```text
dummy ──┐
        ↓
      [-1]
        ↑
tail ───┘
```

Later:

```python
tail = tail.next
```

moves only `tail`.

`dummy` stays where it started.

Therefore:

```text
dummy → remembers beginning

tail → moves while building the list
```

At the end:

```python
return dummy.next
```

---

# 22. Two Pointer Gap Pattern

Sometimes two references move at the same speed but maintain a fixed distance.

Example idea:

```text
first  → ahead
second → behind
```

First, move one pointer ahead by `k` steps.

Then move both together.

Because the distance stays fixed, when the first reaches the end, the second reaches a position relative to the end.

This is a very important general Linked List technique.

---

# 23. Splitting a Linked List

A common operation is dividing a list into two halves.

Typical steps:

```text
1. Find middle
2. Save second half
3. Break the connection
```

Example:

```python
second = slow.next
slow.next = None
```

Before:

```text
10 → 20 → 30 → 40
```

After:

```text
10 → 20 → None

30 → 40 → None
```

Breaking the connection is important.

Otherwise, both parts may still remain connected.

---

# 24. Merge Pattern

When combining two lists, we commonly maintain:

```python
dummy = Node(-1)
tail = dummy
```

The general idea is:

```text
Compare / Select Node
        ↓
Attach to tail
        ↓
Move tail
        ↓
Move selected list
```

At the end, attach any remaining nodes.

The important concepts are:

```text
dummy → fixed starting reference
tail  → current ending node
```

---

# 25. Find → Reverse → Process Pattern

A very important Linked List combination is:

```text
Find Middle
     ↓
Split if needed
     ↓
Reverse One Half
     ↓
Compare or Merge
```

This is an important pattern because Linked Lists cannot be accessed backward directly.

Reversing one half allows us to traverse it in the opposite logical direction.

---

# 26. Recursion in Linked Lists

Linked Lists naturally work well with recursion because every node points to another smaller Linked List.

Consider:

```text
10 → 20 → 30 → None
```

From the perspective of node `10`:

```text
10 + Linked List starting at 20
```

From node `20`:

```text
20 + Linked List starting at 30
```

This gives a recursive structure.

Typical recursive base case:

```python
if head is None or head.next is None:
    return head
```

This means:

```text
Empty list
OR
One-node list
```

needs no further recursive processing.

---

# 27. Understanding Recursive Waiting

Consider:

```python
result = solve(head.next)
```

The current function call does not disappear.

It waits for:

```python
solve(head.next)
```

to finish.

Example:

```text
solve(10)
   ↓ waits

solve(20)
   ↓ waits

solve(30)
   ↓ base case

return 30
   ↑
solve(20) continues
   ↑
solve(10) continues
```

This is extremely important when understanding recursive Linked List algorithms.

The current node does not need to be manually incremented while waiting.

The recursive call itself receives the next node.

---

# 28. Recursive Right-to-Left Processing

Sometimes we process:

```python
head.next = solve(head.next)
```

This means:

```text
First completely solve everything on the right.
Then process the current node.
```

Example:

```text
A → B → C → D
```

Recursive calls:

```text
solve(A)
solve(B)
solve(C)
solve(D)
```

Then returns:

```text
D
↑
C processes
↑
B processes
↑
A processes
```

This pattern is useful when the solution depends on already processing the remaining list.

---

# 29. Deep Copy vs Shallow Copy

Consider:

```python
copy = head
```

This does **not** create a new Linked List.

Both variables reference the same nodes.

```text
head ───┐
        ↓
       10 → 20 → 30
        ↑
copy ───┘
```

This is a shallow reference copy.

A true deep copy requires creating completely new node objects.

```text
Original:

A → B → C


Copy:

A' → B' → C'
```

The copied nodes must be independent.

Changing:

```text
A'
```

must not affect:

```text
A
```

---

# 30. Hash Map Node Mapping Pattern

When nodes have complex relationships, we can map:

```text
Original Node → Copied Node
```

Conceptually:

```python
mapping[original_node] = copied_node
```

This works because Python objects can be used as dictionary keys when they are hashable by identity under normal custom-class behavior.

Then relationships can be recreated using the mapping.

This pattern uses:

```text
O(n)
```

extra space.

---

# 31. Interweaving Nodes Pattern

Sometimes extra hash-map space can be avoided by temporarily placing copied nodes inside the original structure.

Conceptually:

```text
A → B → C
```

becomes:

```text
A → A' → B → B' → C → C'
```

This creates a useful relationship:

```text
Original node's copy = original.next
```

After using this relationship to create additional links, the two lists can be separated.

General pattern:

```text
Insert
  ↓
Connect
  ↓
Separate
```

This is an advanced example of temporarily modifying a data structure to avoid extra memory.

---

# 32. Doubly Linked List

A Doubly Linked List node stores:

```text
prev
data
next
```

Python representation:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
```

Structure:

```text
None ← 10 ⇄ 20 ⇄ 30 → None
```

Each node can move:

```text
Forward  → using next
Backward → using prev
```

---

# 33. Important Doubly Linked List Link Updates

Suppose:

```text
A ⇄ B ⇄ C
```

When removing or inserting nodes, both directions may need updating.

For example, connecting `A` directly to `C`:

```python
A.next = C
C.prev = A
```

A common mistake is updating only one direction.

Always think:

```text
Forward Link
+
Backward Link
```

---

# 34. Advantages of Doubly Linked Lists

Compared with a Singly Linked List:

* Can traverse backward
* Easier deletion when a node reference is available
* Easier insertion before a known node
* Useful for bidirectional navigation

The disadvantage is additional memory because every node stores another reference.

---

# 35. Circular Linked List

In a Circular Linked List, the final node does not point to `None`.

Instead:

```text
tail.next → head
```

Representation:

```text
10 → 20 → 30
↑         ↓
└─────────┘
```

Because there is no `None`, normal traversal like:

```python
while curr:
```

can run forever.

Instead, we stop when we return to the starting node.

---

# 36. Circular Doubly Linked List

A Circular Doubly Linked List has connections in both directions.

```text
head.prev → tail
tail.next → head
```

This creates a fully circular structure.

It is useful when repeated forward and backward movement is required.

---

# 37. Multi-Level Linked Lists

Some Linked Lists contain more than one type of link.

For example:

```text
next
bottom
```

Conceptually:

```text
5 → 10 → 19
↓    ↓     ↓
7    20    22
↓          ↓
8          50
```

These structures often require combining:

```text
Recursion
+
Merge
```

A common strategy is:

```text
Process the remaining structure
        ↓
Merge the current structure
        ↓
Return the merged result
```

---

# 38. Breaking Links Carefully

When rearranging a Linked List, old links can create unexpected connections or cycles.

Sometimes it is necessary to explicitly disconnect:

```python
node.next = None
```

For example, when building multiple separate lists from existing nodes.

General rule:

> If you move an existing node into a different structure, check whether its old `next` connection should be removed.

---

# 39. In-Place Linked List Algorithms

An algorithm is called **in-place** when it modifies the existing nodes rather than creating another complete data structure.

For example:

```text
O(1) auxiliary space
```

often means we are only using a few references:

```python
prev
curr
next_node
```

However, remember:

```text
O(1) extra space
```

does not mean the original Linked List takes no memory.

It means the algorithm uses constant additional memory.

---

# 40. Recursive Space Complexity

A recursive solution may not create an explicit array or hash map but still use additional memory.

Every recursive call occupies stack space.

For a Linked List with `n` nodes:

```text
Recursive depth = O(n)
```

Therefore:

```text
Auxiliary stack space = O(n)
```

An iterative solution may often reduce this to:

```text
O(1)
```

---

# 41. Important Python-Specific Syntax

## `None`

Represents no next node.

```python
node.next = None
```

---

## Identity Check

```python
node1 is node2
```

Checks whether both references point to the exact same object.

---

## None Check

Preferred:

```python
if head is None:
```

Common shorthand:

```python
if not head:
```

---

## Safe Traversal

```python
while curr:
    curr = curr.next
```

---

## Safe Fast Pointer Traversal

```python
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```

---

# 42. Understanding `ListNode`

Coding platforms commonly provide:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

This:

```python
ListNode(10)
```

creates:

```text
10 → None
```

This:

```python
ListNode(10, node2)
```

creates a node whose `next` references `node2`.

---

# 43. Understanding `Optional[ListNode]`

You may see:

```python
head: Optional[ListNode]
```

This means:

```text
head can contain:

ListNode
OR
None
```

Similarly:

```python
-> Optional[ListNode]
```

means the function may return:

```text
a ListNode
OR
None
```

`Optional` is mainly a type hint.

It does not change the Linked List algorithm.

---

# 44. Common Linked List Edge Cases

Always think about these cases:

```text
1. Empty List

None


2. Single Node

10 → None


3. Two Nodes

10 → 20 → None


4. Head Changes


5. Tail Changes


6. Odd Number of Nodes


7. Even Number of Nodes


8. Duplicate Values


9. Cycle Exists


10. Entire List Gets Removed
```

Many Linked List bugs come from ignoring these cases.

---

# 45. Common Mistake — Losing the List

Wrong:

```python
curr.next = prev
curr = curr.next
```

After:

```python
curr.next = prev
```

`curr.next` no longer points forward.

Therefore:

```python
curr = curr.next
```

moves backward instead of forward.

Correct:

```python
next_node = curr.next
curr.next = prev
curr = next_node
```

---

# 46. Common Mistake — Moving Head Unnecessarily

Avoid:

```python
head = head.next
```

when you still need the original head.

Prefer:

```python
curr = head
curr = curr.next
```

---

# 47. Common Mistake — Incorrect Loop Conditions

This can fail:

```python
while fast:
    fast = fast.next.next
```

because:

```python
fast.next
```

may be `None`.

Safer:

```python
while fast and fast.next:
```

---

# 48. Common Mistake — Value vs Identity

Two nodes can contain the same value.

```text
Node A = 5
Node B = 5
```

But:

```python
NodeA is NodeB
```

can still be:

```text
False
```

When the structure matters, compare node references, not only values.

---

# 49. Common Mistake — Forgetting Head Can Change

Operations that can change the head include:

* Inserting at the beginning
* Deleting the beginning
* Reversing a list
* Removing nodes
* Merging structures

Always check whether the returned node should become the new head.

---

# 50. Common Mistake — Forgetting Tail Can Change

If maintaining a tail pointer, update it when:

* Adding to an empty list
* Inserting at the end
* Deleting the final node
* Reversing the list

After reversing:

```text
Old Head → New Tail

Old Tail → New Head
```

---

# 51. Important Linked List Patterns Cheat Sheet

| Situation                       | Pattern                       |
| ------------------------------- | ----------------------------- |
| Normal traversal                | `curr = head`                 |
| Reverse links                   | `prev + curr + next`          |
| Find middle                     | Slow + Fast                   |
| Detect cycle                    | Slow + Fast                   |
| Fixed distance                  | Two Pointer Gap               |
| Head may change                 | Dummy Node                    |
| Build new list                  | Dummy + Tail                  |
| Process two halves              | Find + Split                  |
| Compare from opposite direction | Find + Reverse                |
| Combine lists                   | Merge Pattern                 |
| Sort efficiently                | Divide + Merge                |
| Complex node relationships      | Hash Map Mapping              |
| Reduce mapping space            | Interweaving                  |
| Process remaining list first    | Recursion                     |
| O(1) lookup + O(1) removal      | Hash Map + Doubly Linked List |

---

# 52. Time Complexity Cheat Sheet

| Operation                                 | Time Complexity |
| ----------------------------------------- | --------------: |
| Access by Index                           |            O(n) |
| Search                                    |            O(n) |
| Traversal                                 |            O(n) |
| Insert at Head                            |            O(1) |
| Delete Head                               |            O(1) |
| Insert at Tail without Tail               |            O(n) |
| Insert at Tail with Tail                  |            O(1) |
| Delete Tail in Singly List                |            O(n) |
| Delete Known Node with Previous Reference |            O(1) |
| Find Middle                               |            O(n) |
| Reverse                                   |            O(n) |
| Detect Cycle                              |            O(n) |
| Merge Two Lists                           |        O(n + m) |
| Merge Sort                                |      O(n log n) |

---

# 53. Space Complexity Cheat Sheet

Common iterative traversal:

```text
O(1)
```

Hash Set / Hash Map:

```text
O(n)
```

Recursive processing of `n` nodes:

```text
O(n)
```

because of the call stack.

In-place reference manipulation:

```text
O(1)
```

auxiliary space.

---

# 54. The Most Important Mental Model

Do not think of a Linked List as:

```text
[10, 20, 30, 40]
```

Think of it as separate objects:

```text
Node A
data = 10
next = Node B


Node B
data = 20
next = Node C


Node C
data = 30
next = None
```

Variables like:

```python
head
curr
prev
slow
fast
tail
```

are simply references pointing to these node objects.

They are not the nodes themselves.

---

# 55. How to Dry Run Linked List Code

Always draw the nodes:

```text
10 → 20 → 30 → None
```

Then draw every important reference:

```text
prev       curr
 ↓           ↓
None        10 → 20 → 30
```

After every line, update the diagram.

For example:

```python
next_node = curr.next
```

Draw:

```text
prev       curr       next_node
 ↓           ↓            ↓
None        10    →       20 → 30
```

Then:

```python
curr.next = prev
```

Draw:

```text
None ← 10       20 → 30
       ↑         ↑
      curr    next_node
```

This technique makes pointer/reference problems much easier to understand.

---

# 56. How to Think Before Solving a Linked List Problem

Ask these questions:

```text
Do I only need to visit every node?
        ↓
Traversal


Do I need to change link direction?
        ↓
prev + curr + next


Do I need the middle?
        ↓
Slow + Fast


Do I need to detect repetition/cycle?
        ↓
Slow + Fast


Do I need a position relative to the end?
        ↓
Two Pointer Gap


Can the first node change?
        ↓
Consider Dummy Node


Am I building another list?
        ↓
Dummy + Tail


Do I need two separate halves?
        ↓
Find + Split


Do I need backward-like comparison?
        ↓
Reverse a Part


Do I need to combine ordered chains?
        ↓
Merge Pattern


Do I need to preserve complex relationships?
        ↓
Hash Map Mapping


Can I temporarily modify the structure?
        ↓
Consider In-Place / Interweaving
```

---

# 57. Final Revision Map

```text
Linked List
│
├── Node
│   ├── Data
│   └── Next
│
├── References
│   ├── Head
│   ├── Tail
│   ├── Current
│   ├── Previous
│   └── Next Node
│
├── Basic Operations
│   ├── Traversal
│   ├── Search
│   ├── Insertion
│   └── Deletion
│
├── Types
│   ├── Singly Linked List
│   ├── Doubly Linked List
│   ├── Circular Linked List
│   └── Multi-Level Linked List
│
├── Core Patterns
│   ├── prev + curr + next
│   ├── Slow + Fast
│   ├── Two Pointer Gap
│   ├── Dummy Node
│   ├── Dummy + Tail
│   ├── Find + Split
│   ├── Find + Reverse
│   ├── Merge
│   ├── Recursion
│   ├── Hash Map Mapping
│   └── Interweaving
│
└── Advanced Concepts
    ├── Node Identity
    ├── Deep Copy
    ├── In-Place Manipulation
    ├── Recursive Stack Space
    └── Hash Map + Doubly Linked List
```

---

# 🎯 Final Takeaway

Linked Lists are not mainly about memorizing code.

They are about understanding **references and connections between nodes**.

The most important ideas to master are:

```text
1. Never lose the next node.

2. Understand exactly what each reference points to.

3. Know when the head can change.

4. Save links before modifying them.

5. Use slow and fast pointers when positions depend on length or cycles.

6. Use a dummy node when head-related edge cases make the code complicated.

7. Think in terms of node identity, not only node values.

8. Draw the Linked List while dry-running.

9. Remember that recursion uses call-stack space.

10. Before changing any link, ask:

    "If I change this pointer/reference,
     can I still reach the remaining nodes?"
```

If you understand how:

```text
head
prev
curr
next_node
slow
fast
dummy
tail
```

move and what node each one references at every moment, Linked List problems become much easier to reason about.
