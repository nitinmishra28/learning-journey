# Stock Span Problem

## Problem

Design a data structure that receives stock prices one by one.

For every new stock price, return its **span**.

The **span** of today's price is:

> The number of **consecutive days (including today)** for which the stock price was **less than or equal to today's price**.

Example:

```text
Input

100
80
60
70
60
75
85
```

Output

```text
1
1
1
2
1
4
6
```

Explanation

```text
Day 1

100

No previous day

Span = 1


--------------------------------


Day 2

80

Previous price = 100

100 > 80

Span = 1


--------------------------------


Day 3

60

80 > 60

Span = 1


--------------------------------


Day 4

70

Previous prices

60 <= 70

Stop at 80

Span = 2


--------------------------------


Day 5

60

70 > 60

Span = 1


--------------------------------


Day 6

75

60 <=75

70 <=75

60 <=75

Stop at 80

Span = 4


--------------------------------


Day 7

85

75 <=85

80 <=85

60 <=85

70 <=85

60 <=85

Stop at 100

Span = 6
```

---

# Main Idea

For every new price we need to know

```text
How many consecutive previous prices
are <= current price?
```

Instead of checking every previous day again and again,

we use a

```text
Monotonic Decreasing Stack
```

The stack always stores prices in **strictly decreasing order**.

Whenever a bigger price comes,

all smaller prices become useless and are removed.

---

# Pattern

```text
Monotonic Decreasing Stack + Span Aggregation
```

This is one of the most important Stack interview patterns.

---

# Complete Code with Comments

```python
class StockSpanner:

    def __init__(self):

        # Stack stores:
        #
        # (price, span)
        #
        # Example:
        #
        # (100,1)
        # (80,1)
        # (75,4)
        #
        self.stack = []


    def next(self, price):

        # Every new day contributes
        # at least one day (today itself).
        span = 1


        # Remove all previous prices
        # which are smaller than
        # or equal to the current price.
        #
        # While removing,
        # also collect their span.
        while self.stack and self.stack[-1][0] <= price:

            previous_price, previous_span = self.stack.pop()

            span += previous_span


        # Save today's price
        # together with its span.
        self.stack.append((price, span))


        return span
```

---

# Brute Force Solution

For every new price:

```text
Start moving left

↓

Count every previous day

↓

Stop when price becomes greater
```

Example

```text
Prices

100
80
60
70
60
75
85
```

Suppose today's price is

```text
85
```

Brute Force checks

```text
75

↓

60

↓

70

↓

60

↓

80

↓

100
```

Every query scans many previous days.

If there are

```text
N prices
```

then worst case becomes

```text
1
2
3
4
...
N
```

Total

```text
O(N²)
```

Too slow.

---

# Why Monotonic Stack?

Suppose prices arrive like

```text
100

80

60

70
```

When

```text
70
```

arrives,

can

```text
60
```

ever help again?

No.

Why?

Because

```text
70
```

is newer

AND

```text
70 > 60
```

For every future price,

70 is always a better candidate than 60.

Therefore

```text
60
```

becomes completely useless.

We remove it forever.

Exactly the same idea is used in

```text
Next Greater Element

Largest Rectangle

Sum of Subarray Minimums

Stock Span
```

Whenever an element becomes useless,

remove it immediately.

---

# Why Is the Stack Monotonic?

Suppose prices come like

```text
100

80

60
```

Stack

```text
100

80

60
```

Notice

```text
100 > 80 > 60
```

The Stack is decreasing.

Now

```text
70
```

comes.

Before inserting

```text
70
```

remove

```text
60
```

because

```text
60 <=70
```

Stack becomes

```text
100

80
```

Now push

```text
70
```

Stack

```text
100

80

70
```

Again

```text
100 >80 >70
```

The Stack always remains decreasing.

This property is called

```text
Monotonic Decreasing Stack
```

---

# Why Store `(price, span)` Instead of Only Price?

This is the biggest idea of the problem.

Many beginners first write

```python
stack = [100,80,60]
```

Then when

```text
75
```

comes,

they know

```text
60
```

should be removed.

But they don't know

```text
How many days
60 already represented.
```

Instead we store

```text
(price, span)
```

Example

```text
(100,1)

(80,1)

(75,4)
```

The second value tells us

```text
How many consecutive days
this price already covers.
```

Later,

when this price gets popped,

we can reuse all those days instantly.

This is called

```text
Span Aggregation
```

Instead of recounting old days,

we simply add the stored span.

That is the reason this solution becomes nearly O(1) per operation.

---

# Mental Model

Imagine every stack node is carrying a backpack.

The backpack stores

```text
Price

+

Already Calculated Span
```

Whenever we pop a node,

we don't lose its work.

We simply take its backpack

and add it to today's span.

Instead of counting days again,

we reuse the previous calculation.

This is the biggest optimization of the Stock Span problem.
