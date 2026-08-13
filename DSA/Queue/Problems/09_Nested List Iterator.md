Nested List Iterator

Problem

Given a nested list containing integers and other nested lists, return all integers in their original left-to-right order.

Example

Input:
[1,[4,[6]]]

Output:
1 4 6

Another example:

Input:
[[1,1],2,[1,1]]

Output:
1 1 2 1 1

Pattern

Stack + Nested List Traversal

Why Do We Use a Stack?

The main reason is LIFO (Last In, First Out).

When we encounter a nested list, we need to process the nested list before moving to the elements that come after it.

Example:

[1,[2,3],4]

Required order:
1 → 2 → 3 → 4

A stack naturally supports this because the last added element is processed first.

But Python's:

stack.pop()

removes from the right side.

If we push:

1 2 3

then:

pop() → 3

But we need:

1 → 2 → 3

So we push elements in reverse order:

Original:
1 2 3

Push:
3 2 1

Pop:
1 2 3

Important Rule

Stack = LIFO
pop() = removes from right
Therefore = reverse before pushing

Why Are We Not Storing Indices?

In some stack problems, we store indices.

Here we don't need indices because we are not calculating:

distance

window boundaries

previous/next elements

We only need to maintain the order of:

Integer / Nested List

So we directly store the elements in the stack.

Main Idea

The stack can contain two types of elements:

1. Integer
2. Nested List

For the element at the top:

If it is an Integer

We are ready to return it.

If it is a List

We need to expand it:

Remove list
    ↓
Get its elements
    ↓
Reverse them
    ↓
Push them into stack
    ↓
Continue

The important condition is:

Top of stack = next element to process

Why Reverse the Initial List?

Suppose:

nestedList = [1,[2,3],4]

If we directly store it:

self.stack = nestedList

then:

self.stack.pop()

returns:

4

But we need:

1

first.

So:

self.stack = nestedList[::-1]

becomes:

[4,[2,3],1]

Now:

self.stack.pop()

returns:

1

which is correct.

[::-1] Reminder

arr[::-1]

means reverse the list.

Example:

[1,2,3][::-1]

Output:

[3,2,1]

The -1 means:

Move from right → left

Code

class NestedIterator:

    def __init__(self, nestedList):
        # pop() removes from the right.
        # Reverse so the original first element
        # comes out first.
        self.stack = nestedList[::-1]

    def next(self):
        # Make sure the top is an integer
        self.hasNext()

        # Remove and return the integer
        return self.stack.pop().getInteger()

    def hasNext(self):

        while self.stack:

            # Top is already an integer
            if self.stack[-1].isInteger():
                return True

            # Top is a nested list
            nested_list = self.stack.pop().getList()

            # Reverse because stack follows LIFO
            for item in nested_list[::-1]:
                self.stack.append(item)

        return False

Understanding hasNext()

hasNext() keeps expanding nested lists until an integer reaches the top.

Case 1: Top is an Integer

Stack:

[5,[6,7]]
 ↑
top

The top is 5.

So:

self.stack[-1].isInteger()

returns True.

Therefore:

return True

Case 2: Top is a List

Stack:

[[4,5],6]
 ↑
top

The top is a list.

Remove it:

nested_list = self.stack.pop().getList()

Now:

nested_list = [4,5]

Reverse it:

[5,4]

Push it:

Stack:

4
5
6

Now 4 is at the top and will be processed first.

Why while Instead of if?

Nested lists can have multiple levels.

Example:

[[[1]]]

We need:

[[[1]]]
   ↓
[[1]]
   ↓
[1]
   ↓
1

Therefore:

while self.stack:

is required.

It keeps expanding until:

Integer reaches the top

or:

Stack becomes empty

Why Does next() Call hasNext()?

next() expects an integer:

self.stack.pop().getInteger()

But the top of the stack might currently be a nested list.

So:

self.hasNext()

first prepares the stack.

Flow:

next()
  ↓
hasNext()
  ↓
Expand nested lists
  ↓
Integer reaches top
  ↓
pop() integer

Dry Run

Consider:

nestedList = [1,[2,[3,4]],5]

Step 1: Initial Stack

Reverse the outer list:

[5,[2,[3,4]],1]

Top:

1

So:

next() → 1

Step 2: Expand [2,[3,4]]

Current stack:

[5,[2,[3,4]]]

Top is a list.

Its elements are:

[2,[3,4]]

Reverse them:

[[3,4],2]

Push them.

Stack becomes:

[5,[3,4],2]

So:

next() → 2

Step 3: Expand [3,4]

Reverse:

[4,3]

Push:

[5,4,3]

Now:

next() → 3
next() → 4
next() → 5

Final output:

1 2 3 4 5

Common Mistakes

1. Forgetting to Reverse

Wrong:

for item in nested_list:
    self.stack.append(item)

This causes the order to become reversed because the stack is LIFO.

Correct:

for item in nested_list[::-1]:
    self.stack.append(item)

2. Forgetting to Reverse the Initial List

Wrong:

self.stack = nestedList

Correct:

self.stack = nestedList[::-1]

3. Using if Instead of while

Nested lists can have multiple levels.

Use:

while self.stack:

so all nested levels can be expanded.

4. Forgetting That Stack Contains Two Types

The stack can contain:

Integer

or:

Nested List

So first check:

self.stack[-1].isInteger()

before calling:

getInteger()

5. Thinking the Stack Is Used Just Because There Are Brackets

The important reason is:

Nested structure
      ↓
Depth-first processing
      ↓
LIFO behavior
      ↓
Stack

The brackets themselves are not the reason.

Complexity

Let N be the total number of elements in the nested structure.

Time  → O(N)
Space → O(N)

Each element is pushed and popped a limited number of times.

Revision Cheat Sheet

Nested List Iterator

Pattern:
Stack + Nested List Traversal

Why Stack?
Nested structure → process inner/latest structure first
→ LIFO naturally fits.

Python:
pop() → removes from right

Therefore:
Reverse → Push → Pop

Initial:
self.stack = nestedList[::-1]

If top is Integer:
→ return True

If top is List:
→ pop the list
→ get its elements
→ reverse them
→ push them

Why reverse?
Because stack is LIFO.

Why while?
Nested lists can have multiple levels.

next():
→ call hasNext()
→ make sure integer is on top
→ pop integer

Important:
Top of stack = next element to process

Time:
O(N)

Space:
O(N)

One-Line Pattern

Nested List → Stack for LIFO traversal → reverse before pushing → pop in original left-to-right order.