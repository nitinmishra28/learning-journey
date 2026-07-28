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
# Why Span Aggregation Works

This is the most important concept in the Stock Span problem.

If you understand this section, you will never forget the solution.

---

# What Is Span Aggregation?

Instead of counting previous days again,

we **reuse** the span that was already calculated.

Suppose we already know

```text
(70, 2)
```

This means

```text
Price = 70

Span = 2
```

But what does Span = 2 actually mean?

It means

```text
70

↓

60
```

Both of these days are already covered.

So if a future price is greater than **70**,

it will automatically be greater than **60** as well.

Therefore,

there is no need to count those days again.

Simply reuse

```text
2
```

This is called

```text
Span Aggregation
```

---

# Visual Example

Prices

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

we remove

```text
60
```

Current span

```text
1

+

1

=

2
```

Stack becomes

```text
(100,1)

(80,1)

(70,2)
```

Notice carefully.

We are **not storing 60 anymore**.

Instead,

its information has been merged into

```text
(70,2)
```

Think of it like

```text
60

merged into

70
```

Now suppose

```text
75
```

comes.

Without Span Aggregation,

we would count

```text
70

↓

60
```

again.

Instead,

we simply do

```python
span += 2
```

Done.

Both days are counted instantly.

---

# Why Is This Correct?

Suppose

```text
70

covers

70

↓

60
```

Now today's price is

```text
75
```

Since

```text
75 >= 70
```

and

```text
70 already guaranteed

70 >= 60
```

Then

```text
75

also covers

60
```

Mathematically

```text
75 >=70

70 >=60

Therefore

75 >=60
```

That is why adding the previous span is always correct.

---

# Why Don't We Need the Removed Elements Again?

Suppose

```text
Stack

100

80

70
```

Now

```text
75
```

comes.

We remove

```text
70
```

Will

```text
70
```

ever be useful again?

No.

Future prices will always compare against

```text
75
```

instead.

Why?

Because

```text
75

is newer

AND

75 >70
```

For every future query,

75 is a better representative.

So

```text
70
```

can safely disappear forever.

This is exactly why every element is popped only once.

---

# Why Is the Complexity O(1)?

At first glance,

the while loop looks scary.

```python
while stack:
```

People think

```text
O(N)
```

for every query.

But that's not true.

Let's count pushes and pops.

Suppose prices are

```text
100

80

60

70

75

90
```

Every price

is pushed

exactly once.

```text
100

Push

✔
```

Later,

it may be popped

once.

```text
100

Pop

✔
```

Can it be popped again?

No.

Once removed,

it never comes back.

Therefore,

each element performs

```text
1 Push

+

1 Pop
```

Maximum.

So for

```text
N
```

prices,

total operations are

```text
N Pushes

+

N Pops
```

Total

```text
2N
```

Which is

```text
O(N)
```

for all queries together.

Therefore,

average cost of each query is

```text
O(1)
```

This is called

```text
Amortized O(1)
```

---

# Dry Run Showing Amortized Complexity

Prices

```text
100
80
60
70
75
90
```

Pushes

```text
100 ✔

80 ✔

60 ✔

70 ✔

75 ✔

90 ✔
```

Pops

```text
60 ✔

70 ✔

75 ✔

80 ✔
```

Notice

```text
60

was popped only once.
```

It never returns.

Same for every other price.

That is the entire reason why the algorithm is efficient.

---

# Common Mistakes

## Mistake 1

Using `if` instead of `while`

Wrong

```python
if stack[-1][0] <= price:
```

Correct

```python
while stack and stack[-1][0] <= price:
```

Why?

There can be many smaller prices.

---

## Mistake 2

Storing only the price

Wrong

```python
stack.append(price)
```

Correct

```python
stack.append((price, span))
```

Without storing the span,

you will have to count previous days again.

---

## Mistake 3

Using `<`

Wrong

```python
while stack[-1][0] < price
```

Correct

```python
while stack[-1][0] <= price
```

The problem clearly says

```text
Less than OR Equal
```

Equal prices must also be included.

---

## Mistake 4

Pushing Before Calculating Span

Wrong

```python
Push Current Price

↓

Calculate Span
```

Correct

```text
Remove Smaller Prices

↓

Calculate Span

↓

Push Current Price
```

---

# Pattern Recognition

Whenever you hear

```text
Nearest Greater

Nearest Smaller

Previous Greater

Previous Smaller

Span

Histogram

Temperature

Subarray Minimum

Subarray Maximum
```

Always think

```text
Monotonic Stack
```

If previous work can be reused,

think

```text
Aggregation
```

---

# Complexity

| Operation | Complexity         |
| --------- | ------------------ |
| next()    | Amortized **O(1)** |
| Space     | **O(N)**           |

---

# Revision Cheat Sheet

```text
Pattern

↓

Monotonic Decreasing Stack


Store

↓

(price, span)


Current Span

↓

Starts from 1


Remove

↓

All prices <= current


Reuse

↓

Previous Span


Push

↓

(price, span)


Time

↓

Amortized O(1)


Space

↓

O(N)
```

---

# One-Line Pattern

```text
Monotonic Decreasing Stack + Span Aggregation
```

---

# Interview Tips

Whenever the interviewer asks:

> Why are you storing `(price, span)` instead of only `price`?

Your answer should be:

> We store the span so that when a price is popped in the future, we can reuse all the consecutive days it already represents instead of recounting them. This aggregation avoids repeated work and gives an amortized **O(1)** time complexity.

If they ask:

> Why is the while loop not O(N) for every operation?

Answer:

> Although one call may pop multiple elements, every price is pushed exactly once and popped at most once. Across all operations, the total number of pops is at most **N**, so the average cost of each `next()` call is **Amortized O(1)**.

---

# Final Takeaway

The Stock Span problem is **not** about counting previous days.

It is about **reusing previously computed spans**.

The stack stores **compressed information**:

```text
(price, span)
```

Every time a bigger price arrives:

* Remove all smaller or equal prices.
* Reuse their spans.
* Merge them into today's span.
* Store the merged result for future days.

This simple idea transforms an **O(N²)** brute-force approach into an **Amortized O(1)** solution using a **Monotonic Decreasing Stack + Span Aggregation** pattern.
