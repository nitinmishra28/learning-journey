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


# Line by Line Explanation

Now let's understand every single line of the algorithm.

---

# Step 1 : Start With Span = 1

```python
span = 1
```

Why do we initialize the span with **1**?

Because today's price is always included in its own span.

The definition says:

> Number of consecutive days **including today**.

Even if every previous price is greater,

today itself still counts.

Example

```text
Today's Price

100
```

There are no previous days.

Answer

```text
Span = 1
```

Another example

```text
Prices

100
80
60
```

Today's price

```text
60
```

Previous day

```text
80 > 60
```

Span is still

```text
1
```

So every new price starts with

```text
Today's Day

+

Any previous consecutive days
```

That is why

```python
span = 1
```

is always correct.

---

# Step 2 : Why While Loop?

```python
while self.stack and self.stack[-1][0] <= price:
```

This is the heart of the algorithm.

Let's break it.

First condition

```python
self.stack
```

means

```text
Stack should not be empty.
```

Second condition

```python
self.stack[-1][0] <= price
```

means

```text
Top Price

<=

Current Price
```

If true,

that previous price belongs to today's span.

So remove it.

---

# Why NOT if?

Many beginners write

```python
if self.stack[-1][0] <= price:
```

This is wrong.

Suppose

```text
Stack

100
80
60
```

Current price

```text
90
```

We should remove

```text
60

↓

80
```

Both are smaller.

An **if** removes only one element.

A **while** keeps removing until the condition becomes false.

After popping

```text
60
```

Stack becomes

```text
100
80
```

Still

```text
80 <= 90
```

Pop again.

Finally

```text
100
```

is greater.

Now stop.

That is why

```python
while
```

is mandatory.

---

# Why Compare Only the Top?

Suppose stack is

```text
100

80

70

50
```

Current price

```text
75
```

We only compare with

```text
50
```

Why?

Because the stack is already sorted in decreasing order.

If the top is greater,

everything below it is also greater.

Example

```text
100

90

80
```

Current price

```text
70
```

Top

```text
80
```

already blocks us.

There is no need to check

```text
90

100
```

This is one of the biggest advantages of a Monotonic Stack.

---

# Why stack[-1][0]?

Remember,

our stack stores

```text
(price, span)
```

Example

```text
(100,1)

(80,1)

(75,4)
```

The first value is

```text
Price
```

The second value is

```text
Span
```

So

```python
stack[-1][0]
```

means

```text
Top Price
```

while

```python
stack[-1][1]
```

means

```text
Top Span
```

---

# Step 3 : Pop the Previous Node

```python
previous_price, previous_span = self.stack.pop()
```

Suppose

```text
Stack

(100,1)

(80,1)

(70,2)
```

Current price

```text
75
```

Top

```text
(70,2)
```

gets removed.

After pop

```text
previous_price

70


previous_span

2
```

Now we know

* previous price
* previous span

Both are available immediately.

---

# Why Store Span?

Suppose prices are

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

was inserted,

its span became

```text
2
```

because

```text
70

↓

60
```

Now suppose

```text
75
```

comes.

If we stored only

```text
70
```

we would again count

```text
60
```

This repeats unnecessary work.

Instead,

we stored

```text
(70,2)
```

Immediately we know

```text
70

already represents

2 consecutive days.
```

No recounting required.

---

# Step 4 : Span Aggregation

```python
span += previous_span
```

This is the magic line.

Suppose

```text
Current Span

1
```

because of today.

Top node

```text
(70,2)
```

means

```text
70 already covers

70

↓

60
```

Instead of counting both days again,

simply add

```text
2
```

Now

```text
Span

1 + 2

=

3
```

Notice something.

We didn't visit

```text
60
```

again.

The previous calculation was reused.

This idea is called

```text
Span Aggregation
```

---

# Visual Example

Suppose stack contains

```text
(100,1)

(80,1)

(75,4)
```

Current price

```text
85
```

Current span starts with

```text
1
```

Top

```text
(75,4)
```

gets removed.

Now

```text
Span

1

+

4

=

5
```

Stack becomes

```text
(100,1)

(80,1)
```

Again

```text
80 <= 85
```

Remove

```text
(80,1)
```

Now

```text
Span

5

+

1

=

6
```

Stack

```text
(100,1)
```

Since

```text
100 > 85
```

Stop.

Today's answer

```text
6
```

Without span aggregation,

we would have counted

```text
75

↓

70

↓

60

↓

60

↓

80
```

again.

Instead,

we reused previous work.

---

# Step 5 : Push Current Price

```python
self.stack.append((price, span))
```

Suppose today's price is

```text
85
```

and its span is

```text
6
```

Push

```text
(85,6)
```

Now future prices can directly reuse these

```text
6
```

days.

Example

```text
Stack

(100,1)

(85,6)
```

Imagine tomorrow's price is

```text
90
```

When

```text
(85,6)
```

is removed,

we immediately gain

```text
6
```

days.

No recounting.

---

# Why Push After the While Loop?

Suppose

```text
Current Price

75
```

If we push first,

stack becomes

```text
100

80

75

60
```

Now

```text
75
```

itself blocks the while loop.

The algorithm breaks.

Correct order is

```text
Remove Smaller Prices

↓

Calculate Span

↓

Push Current Price
```

Always remember this order.

---

# Complete Dry Run

Input

```text
100
80
60
70
60
75
85
```

Initially

```text
Stack

Empty
```

---

Insert

```text
100
```

Span

```text
1
```

Stack

```text
(100,1)
```

---

Insert

```text
80
```

Top

```text
100
```

greater.

Span

```text
1
```

Stack

```text
(100,1)

(80,1)
```

---

Insert

```text
60
```

Top

```text
80
```

greater.

Push

```text
(60,1)
```

---

Insert

```text
70
```

Remove

```text
(60,1)
```

Span

```text
1 + 1

=

2
```

Push

```text
(70,2)
```

Stack

```text
(100,1)

(80,1)

(70,2)
```

---

Insert

```text
60
```

Top

```text
70
```

greater.

Push

```text
(60,1)
```

---

Insert

```text
75
```

Remove

```text
(60,1)

↓

(70,2)
```

Span

```text
1

+

1

+

2

=

4
```

Push

```text
(75,4)
```

---

Insert

```text
85
```

Remove

```text
(75,4)

↓

(80,1)
```

Span

```text
1

+

4

+

1

=

6
```

Push

```text
(85,6)
```

Final Answers

```text
1
1
1
2
1
4
6
```
