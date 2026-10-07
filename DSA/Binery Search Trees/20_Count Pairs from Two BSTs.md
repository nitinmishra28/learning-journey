# Count Pairs from Two BSTs

## 1. Problem

Given two Binary Search Trees `root1` and `root2` and an integer `x`, count the number of pairs:

```text
(node from BST1, node from BST2)
```

such that:

```text
node1.data + node2.data = x
```

### Example

```text
BST 1:

        5
       / \
      3   7
     / \
    2   4


BST 2:

        10
       /  \
      6    12
```

Suppose:

```text
x = 14
```

BST 1 inorder:

```text
2 → 3 → 4 → 5 → 7
```

BST 2 inorder:

```text
6 → 10 → 12
```

Valid pairs:

```text
2 + 12 = 14
4 + 10 = 14
```

Therefore:

```text
Answer = 2
```

---

# 2. Important Observation

Both trees are BSTs.

Therefore:

```text
BST
 ↓
Inorder Traversal
 ↓
Sorted Order
```

For example:

```text
BST 1:
2 → 3 → 4 → 5 → 7

BST 2:
6 → 10 → 12
```

Now the problem becomes:

> Find pairs from two sorted arrays whose sum is `x`.

This immediately suggests a **Two Pointer** approach.

---

# 3. Brute Force Approach

The simplest solution is to compare every node from the first BST with every node from the second BST.

Conceptually:

```python
for value1 in inorder1:
    for value2 in inorder2:
        if value1 + value2 == x:
            count += 1
```

If the first tree has `n` nodes and the second has `m` nodes:

```text
Time = O(n * m)
```

If we also need to store the inorder arrays:

```text
Space = O(n + m)
```

This ignores the fact that both BSTs give us sorted order.

---

# 4. Approach 1 — Inorder Arrays + Two Pointers

Your first solution converts both BSTs into sorted arrays.

```python
self.solve(root1, inorder1)
self.solve(root2, inorder2)
```

Because inorder traversal of a BST is sorted:

```text
inorder1 = ascending
inorder2 = ascending
```

Then you use:

```python
left = 0
right = len(inorder2) - 1
```

So:

```text
BST 1 → smallest → larger → larger → ...
                         ↑
                       left


BST 2 → ... → larger → largest
                         ↑
                       right
```

This is the same idea as the classic two-sum problem on sorted arrays.

---

# 5. Why One Pointer Starts at the Beginning and the Other at the End

Suppose:

```text
inorder1 = [2, 3, 4, 5, 7]
inorder2 = [6, 10, 12]

x = 14
```

Start:

```text
left  = 2
right = 12
```

Sum:

```text
2 + 12 = 14
```

Found a pair.

If:

```text
curr_sum < x
```

we need a **larger sum**.

So increase the value from BST1:

```python
left += 1
```

If:

```text
curr_sum > x
```

we need a **smaller sum**.

So decrease the value from BST2:

```python
right -= 1
```

---

# 6. Your First Solution

```python
class Solution:

    def solve(self, root, inorder):
        if root is None:
            return

        # LNR

        # L
        self.solve(root.left, inorder)

        # N
        inorder.append(root.data)

        # R
        self.solve(root.right, inorder)

    def countPairs(self, root1: 'Node', root2: 'Node', x: int) -> int:

        inorder1 = []
        inorder2 = []

        self.solve(root1, inorder1)
        self.solve(root2, inorder2)

        cnt = 0
        left = 0
        right = len(inorder2) - 1

        while left < len(inorder1) and right >= 0:

            curr_sum = inorder1[left] + inorder2[right]

            if curr_sum == x:
                cnt += 1
                left += 1
                right -= 1

            elif curr_sum < x:
                left += 1

            else:
                right -= 1

        return cnt
```

---

# 7. Why the Two-Pointer Logic Works

Consider:

```text
A = [2, 3, 4, 5, 7]
B = [6, 10, 12]

x = 15
```

Start:

```text
2 + 12 = 14
```

Too small:

```text
14 < 15
```

So we need a larger value.

Move:

```text
2 → 3
```

Now:

```text
3 + 12 = 15
```

Found.

---

Suppose instead:

```text
A = [2, 3, 4, 5, 7]
B = [6, 10, 12]

x = 16
```

Start:

```text
2 + 12 = 14
```

Too small:

```text
14 < 16
```

Move `left`:

```text
3 + 12 = 15
```

Still too small.

Move again:

```text
4 + 12 = 16
```

Found.

---

If the sum is too large:

```text
7 + 12 = 19
```

and:

```text
19 > 16
```

we need a smaller value.

So:

```text
12 → 10
```

This is why:

```python
elif curr_sum < x:
    left += 1
else:
    right -= 1
```

works.

---

# 8. Complexity of Approach 1

Let:

```text
n = number of nodes in BST1
m = number of nodes in BST2
```

### Inorder Traversal

```text
BST1 → O(n)
BST2 → O(m)
```

### Two Pointers

Each pointer moves only forward/backward:

```text
O(n + m)
```

Therefore:

```text
Time = O(n + m)
```

But we store both inorder arrays:

```text
Space = O(n + m)
```

So:

```text
Approach 1:
Time  = O(n + m)
Space = O(n + m)
```

---

# 9. Can We Reduce the Space?

Yes.

The sorted arrays are only being used to simulate two iterators:

```text
BST1:
smallest → larger → larger → ...

BST2:
largest → smaller → smaller → ...
```

We don't actually need to store all nodes.

We can perform:

```text
Normal Inorder
```

on the first BST and:

```text
Reverse Inorder
```

on the second BST using stacks.

This gives the same two-pointer behavior with much less extra space.

That is exactly what your second solution does.

---

# 10. Approach 2 — Two BST Iterators

Instead of:

```text
BST1 → inorder array
BST2 → inorder array
```

we maintain:

```text
BST1 → forward inorder iterator
BST2 → reverse inorder iterator
```

### BST 1

Use:

```text
Left → Node → Right
```

This produces:

```text
smallest → largest
```

### BST 2

Use:

```text
Right → Node → Left
```

This produces:

```text
largest → smallest
```

So conceptually:

```text
BST 1:

2 → 3 → 4 → 5 → 7
↑
smallest


BST 2:

12 → 10 → 6
↑
largest
```

Now we have two pointers without storing the arrays.

---

# 11. Your Second Solution

```python
class Solution:

    def countPairs(self, root1: 'Node', root2: 'Node', x: int):

        a = root1
        b = root2

        s1 = []
        s2 = []

        ans = 0

        while True:

            # Forward inorder for BST1
            while a:
                s1.append(a)
                a = a.left

            # Reverse inorder for BST2
            while b:
                s2.append(b)
                b = b.right

            if not s1 or not s2:
                break

            a_top = s1[-1]
            b_top = s2[-1]

            curr_sum = a_top.data + b_top.data

            if curr_sum == x:

                ans += 1

                s1.pop()
                s2.pop()

                a = a_top.right
                b = b_top.left

            elif curr_sum < x:

                s1.pop()
                a = a_top.right

            else:

                s2.pop()
                b = b_top.left

        return ans
```

---

# 12. Understanding `s1`

For the first BST, we want normal inorder:

```text
L → N → R
```

So we keep moving left:

```python
while a:
    s1.append(a)
    a = a.left
```

For example:

```text
        5
       /
      3
     /
    2
```

Stack becomes:

```text
TOP
 ↓
2
3
5
```

Therefore:

```python
s1[-1]
```

gives:

```text
2
```

which is the smallest value.

---

# 13. Understanding `s2`

For the second BST, we want reverse inorder:

```text
R → N → L
```

So we keep moving right:

```python
while b:
    s2.append(b)
    b = b.right
```

For:

```text
        10
          \
           12
             \
              15
```

stack becomes:

```text
TOP
 ↓
15
12
10
```

Therefore:

```python
s2[-1]
```

gives:

```text
15
```

which is the largest value.

---

# 14. Why We Use `s1[-1]` and `s2[-1]`

We don't immediately pop the nodes.

First we need to inspect their values:

```python
a_top = s1[-1]
b_top = s2[-1]
```

Then:

```python
curr_sum = a_top.data + b_top.data
```

Now we decide which pointer should move.

This is exactly like:

```text
left pointer
right pointer
```

in a sorted array.

The stack is simply helping us implement those pointers without creating arrays.

---

# 15. If `curr_sum == x`

Suppose:

```text
a_top.data = 4
b_top.data = 10

4 + 10 = 14
```

We found a valid pair.

So:

```python
ans += 1
```

Now both current nodes have been consumed:

```python
s1.pop()
s2.pop()
```

Then we move to their respective next nodes:

```python
a = a_top.right
b = b_top.left
```

Why?

For BST1:

```text
Inorder:
L → N → R
```

After processing `a_top`, continue with its right subtree.

For BST2:

```text
Reverse inorder:
R → N → L
```

After processing `b_top`, continue with its left subtree.

---

# 16. If `curr_sum < x`

Suppose:

```text
4 + 10 = 14

x = 16
```

We need a bigger sum.

Since:

```text
BST1 pointer = 4
BST2 pointer = 10
```

we should increase the smaller-side value.

Move forward in BST1:

```python
s1.pop()
a = a_top.right
```

This gives the next larger value from BST1.

So:

```text
sum < x
    ↓
Need bigger sum
    ↓
Move BST1 forward
```

---

# 17. If `curr_sum > x`

Suppose:

```text
7 + 12 = 19

x = 16
```

We need a smaller sum.

So move the pointer that is coming from the largest side.

For BST2:

```python
s2.pop()
b = b_top.left
```

This moves to the next smaller value.

Therefore:

```text
sum > x
    ↓
Need smaller sum
    ↓
Move BST2 backward
```

---

# 18. Why the Two Iterators Work

The second solution is essentially doing:

```text
BST1                      BST2

Inorder                   Reverse Inorder
  ↓                            ↓
Ascending                  Descending

2 → 3 → 4 → 5 → 7        12 → 10 → 6
↑                          ↑
left                       right
```

This is exactly equivalent to:

```text
Array 1                    Array 2

[2,3,4,5,7]               [6,10,12]
 ↑                           ↑
left                        right
```

The difference is:

```text
Approach 1:
Store arrays

Approach 2:
Generate values lazily
using stacks
```

---

# 19. Dry Run — Approach 2

Consider:

```text
BST1:

        5
       / \
      3   7
     / \
    2   4


BST2:

        10
       /  \
      6    12
```

And:

```text
x = 14
```

### Initial values

BST1 forward:

```text
2
```

BST2 backward:

```text
12
```

Sum:

```text
2 + 12 = 14
```

Found:

```text
ans = 1
```

Move both iterators.

Next values:

```text
BST1 → 3
BST2 → 10
```

Sum:

```text
3 + 10 = 13
```

Too small:

```text
13 < 14
```

Move BST1:

```text
BST1 → 4
```

Now:

```text
4 + 10 = 14
```

Found:

```text
ans = 2
```

Continue until one iterator becomes empty.

Final:

```text
answer = 2
```

---

# 20. Why `while True`?

The main loop is:

```python
while True:
```

because we don't know in advance how many pointer movements will be needed.

We stop when:

```python
if not s1 or not s2:
    break
```

Meaning:

```text
BST1 iterator finished
OR
BST2 iterator finished
```

Once either side has no more values, no additional pair can be formed.

---

# 21. Approach 1 vs Approach 2

| Feature | Approach 1 | Approach 2 |
|---|---|---|
| BST traversal | Inorder | Iterative Inorder |
| BST2 traversal | Inorder | Reverse Inorder |
| Sorted storage | Arrays | Stacks |
| Two pointers | Array indexes | Stack tops |
| Time | `O(n + m)` | `O(n + m)` |
| Extra Space | `O(n + m)` | `O(h1 + h2)` |
| Easier to understand | Yes | Slightly harder |
| Space efficient | No | **Yes** |

Where:

```text
n  = nodes in BST1
m  = nodes in BST2
h1 = height of BST1
h2 = height of BST2
```

---

# 22. Which One Is the Optimized Approach?

**Your second solution is the optimized approach.**

Both solutions have:

```text
Time = O(n + m)
```

But:

```text
Approach 1:
Space = O(n + m)
```

while:

```text
Approach 2:
Space = O(h1 + h2)
```

So the second approach avoids storing every node.

The key optimization is:

```text
Inorder Array
     ↓
Replace with
     ↓
BST Iterator using Stack
```

---

# 23. Why Space Becomes O(h)

In the second approach, we don't store all nodes.

The stacks contain only the nodes needed to continue traversal.

For a balanced BST:

```text
h = O(log n)
```

Therefore:

```text
Space = O(log n + log m)
```

For skewed trees:

```text
h1 = O(n)
h2 = O(m)
```

so worst-case:

```text
Space = O(n + m)
```

The important point is that the algorithm uses:

```text
O(h1 + h2)
```

rather than always storing:

```text
O(n + m)
```

nodes.

---

# 24. Why This Is a Two-Pointer Problem

At first glance, this looks like a tree problem.

But the real pattern is:

```text
BST
 ↓
Sorted Order
 ↓
Two Sorted Sequences
 ↓
Two Pointers
```

Approach 1 makes this obvious:

```text
inorder1 → ascending
inorder2 → ascending

left  → beginning of inorder1
right → end of inorder2
```

Approach 2 implements the same idea without explicitly creating the arrays.

---

# 25. Important Difference From Two Sum in One BST

For one BST, we used:

```text
Forward Iterator
+
Backward Iterator
```

For this problem:

```text
BST1 → Forward Inorder
BST2 → Reverse Inorder
```

Why?

Because we need:

```text
Smallest from BST1
+
Largest from BST2
```

and then move the appropriate side.

So the pattern is:

```text
Two BSTs
   ↓
BST1: Inorder
BST2: Reverse Inorder
   ↓
Two Pointers
```

---

# 26. Common Mistakes

### Mistake 1: Doing nested loops

This gives:

```text
O(n * m)
```

and ignores sorted order.

---

### Mistake 2: Using normal inorder for both trees in Approach 2

If both stacks produce ascending values:

```text
BST1 → smallest to largest
BST2 → smallest to largest
```

the two-pointer movement becomes inconvenient.

We want:

```text
BST1 → smallest to largest
BST2 → largest to smallest
```

---

### Mistake 3: Moving the wrong iterator

Remember:

```text
sum < x
    ↓
Need larger sum
    ↓
Move BST1 forward
```

And:

```text
sum > x
    ↓
Need smaller sum
    ↓
Move BST2 backward
```

---

### Mistake 4: Forgetting subtree continuation

After popping a BST1 node:

```python
a = a_top.right
```

because we are doing normal inorder.

After popping a BST2 node:

```python
b = b_top.left
```

because we are doing reverse inorder.

---

# 27. Important Mental Model

Think of the two stacks as hidden pointers.

```text
BST1:

smallest
   ↓
[s1 stack]
   ↓
next larger
```

```text
BST2:

largest
   ↓
[s2 stack]
   ↓
next smaller
```

Then:

```text
             curr_sum
                ↓
       -------------------
       |        |        |
      < x      == x     > x
       |        |        |
    move A    count    move B
```

This is just the two-pointer pattern implemented on trees.

---

# 28. Complexity

Let:

```text
n = nodes in BST1
m = nodes in BST2
h1 = height of BST1
h2 = height of BST2
```

## Approach 1

```text
Inorder BST1       → O(n)
Inorder BST2       → O(m)
Two pointers       → O(n + m)

Total Time         → O(n + m)
Space              → O(n + m)
```

## Approach 2

Every node is pushed and popped at most once from its corresponding stack.

Therefore:

```text
Time = O(n + m)
```

The stacks store traversal paths:

```text
Space = O(h1 + h2)
```

### Final Optimized Complexity

```text
Time  : O(n + m)
Space : O(h1 + h2)
```

---

# 29. Revision Cheat Sheet

```text
Problem:
Count pairs from two BSTs whose sum = x.

Key Observation:
Inorder traversal of BST = Sorted Order.

Approach 1:
BST1 → Inorder Array → Ascending
BST2 → Inorder Array → Ascending

Then:
left = start of BST1
right = end of BST2

sum == x:
    count++

sum < x:
    move left forward

sum > x:
    move right backward

Complexity:
Time  = O(n + m)
Space = O(n + m)


Optimized Approach 2:
Don't store inorder arrays.

BST1:
Normal Inorder
L → N → R
→ smallest to largest

BST2:
Reverse Inorder
R → N → L
→ largest to smallest

Use:
s1 = stack for BST1
s2 = stack for BST2

sum == x:
    pop both

sum < x:
    move BST1 forward

sum > x:
    move BST2 backward

Optimized Complexity:
Time  = O(n + m)
Space = O(h1 + h2)

Core Pattern:
Two BSTs → Sorted Order → Two Pointers → BST Iterators

One-Line Pattern:
Count Pairs in Two BSTs = Forward Inorder Iterator on BST1 + Reverse Inorder Iterator on BST2 + Two-Pointer Sum.