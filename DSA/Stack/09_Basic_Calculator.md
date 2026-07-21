# Basic Calculator

## Problem

Given a string expression containing:

```text
Numbers
+
-
(
)
Spaces
```

calculate and return the final result.

Example:

```text
s = "(1+(4+5+2)-3)+(6+8)"
```

Output:

```text
23
```

---

# Main Idea

We process the expression character by character.

The complete flow is:

```text
Digit mila
    ↓
Number build karo

+ / - mila
    ↓
Previous number ko result me add karo
    ↓
New sign set karo

( mila
    ↓
Current result aur sign Stack me save karo
    ↓
Bracket ke andar fresh calculation start karo

) mila
    ↓
Bracket ka last pending number add karo
    ↓
Saved sign aur result nikalo
    ↓
Outside result + sign × inside result

String finish
    ↓
Last pending number add karo
```

### One-Line Mental Model

```text
Number banao
→ Operator par previous number process karo
→ '(' par result/sign save karo
→ ')' par bracket result combine karo
→ End me last number process karo
```

---

# Code with Comments

```python
class Solution:
    def calculate(self, s: str) -> int:

        # Stores previous result and sign
        # when we enter parentheses
        stack = []

        # Running result of current expression
        result = 0

        # Current number being built
        number = 0

        # Sign of current number
        # 1 means positive
        # -1 means negative
        sign = 1


        for ch in s:

            # -----------------------------------
            # CASE 1: Digit
            # -----------------------------------

            # Build complete multi-digit number
            if ch.isdigit():

                number = number * 10 + int(ch)


            # -----------------------------------
            # CASE 2: Plus Operator
            # -----------------------------------

            elif ch == '+':

                # Previous number is complete,
                # so add it to the result
                result += sign * number

                # Reset for next number
                number = 0

                # Next number will be positive
                sign = 1


            # -----------------------------------
            # CASE 3: Minus Operator
            # -----------------------------------

            elif ch == '-':

                # Previous number is complete,
                # so add it using its OLD sign
                result += sign * number

                # Reset for next number
                number = 0

                # Next number will be negative
                sign = -1


            # -----------------------------------
            # CASE 4: Opening Parenthesis
            # -----------------------------------

            elif ch == '(':

                # Save everything needed to return
                # to the outside expression later
                stack.append(result)
                stack.append(sign)

                # Start fresh calculation
                # for expression inside parentheses
                result = 0
                sign = 1


            # -----------------------------------
            # CASE 5: Closing Parenthesis
            # -----------------------------------

            elif ch == ')':

                # Process the last number inside
                # the parentheses
                result += sign * number

                number = 0


                # Because we pushed:
                #
                # result first
                # sign second
                #
                # Stack looks like:
                #
                # [..., previous_result, previous_sign]
                #
                # So sign comes out first
                previous_sign = stack.pop()

                previous_result = stack.pop()


                # Combine:
                #
                # result before bracket
                # +
                # sign before bracket × result inside bracket
                result = (
                    previous_result
                    + previous_sign * result
                )


        # The final number is not followed by
        # +, -, or ) in many cases,
        # so process it manually
        result += sign * number


        return result
```

---

# What Each Variable Means

## `result`

```python
result = 0
```

Stores the result calculated so far for the **current expression level**.

Example:

```text
10 + 20 - 5
```

After processing `+`:

```text
result = 10
```

After processing `-`:

```text
result = 30
```

At the end:

```text
result = 25
```

---

## `number`

```python
number = 0
```

Stores the number currently being built.

For example:

```text
123
```

is read one character at a time:

```text
'1'
'2'
'3'
```

We build it using:

```python
number = number * 10 + int(ch)
```

Dry run:

```text
number = 0

Read 1:
0 × 10 + 1
= 1

Read 2:
1 × 10 + 2
= 12

Read 3:
12 × 10 + 3
= 123
```

Remember:

```text
Old Number × 10
        ↓
Shift digits one place left
        ↓
Add new digit
```

---

## `sign`

```python
sign = 1
```

Stores the sign that should be applied to the current `number`.

```text
sign = 1
→ Positive


sign = -1
→ Negative
```

So:

```python
result += sign * number
```

automatically handles both cases.

For:

```text
+ 5
```

we get:

```text
result += 1 * 5
```

For:

```text
- 5
```

we get:

```text
result += -1 * 5
```

---

# Most Important Concept — Operator Processes the Previous Number

Consider:

```text
12 + 5
```

When we reach:

```text
+
```

the number already built is:

```text
12
```

Therefore:

```python
result += sign * number
```

processes:

```text
12
```

Then:

```python
number = 0
sign = 1
```

prepares us for the next number.

So remember:

```text
When an operator arrives,
the number BEFORE that operator is complete.
```

---

# Why Do We Add Before Changing the Sign?

Consider:

```text
10 - 5
```

When we reach `-`:

```text
number = 10
sign = 1
```

First:

```python
result += sign * number
```

So:

```text
result = 0 + 1 × 10
       = 10
```

Then:

```python
sign = -1
```

This `-1` belongs to the **next number**:

```text
5
```

So:

```text
Operator processes previous number
and sets the sign for the next number.
```

This is an important thing to remember.

---

# Why Do We Need a Stack?

The Stack is needed because parentheses temporarily interrupt the current calculation.

Consider:

```text
10 - (2 + 3)
```

Before entering the bracket, we need to remember:

```text
result = 10

sign = -1
```

Then we calculate:

```text
2 + 3
```

separately.

After the bracket finishes, we need to restore:

```text
10 - (...)
```

So we store:

```python
stack.append(result)
stack.append(sign)
```

The Stack remembers:

```text
What was the result before '('?

What sign was before '('?
```

---

# What Happens When `(` Arrives?

Suppose:

```text
10 - (2 + 3)
```

Before `(`:

```text
result = 10
sign = -1
```

We save:

```python
stack.append(result)
stack.append(sign)
```

Stack:

```text
[10, -1]
```

Then start fresh:

```python
result = 0
sign = 1
```

Now we calculate:

```text
2 + 3
```

independently.

---

# Why Do We Save Both Result and Sign?

Saving only the result is not enough.

For:

```text
10 + (2 + 3)
```

the bracket should be:

```text
+5
```

But for:

```text
10 - (2 + 3)
```

the same bracket should become:

```text
-5
```

Therefore, we need both:

```text
Previous Result

and

Sign Before Parentheses
```

That is why we store:

```python
stack.append(result)
stack.append(sign)
```

---

# What Happens When `)` Arrives?

Suppose we have:

```text
10 - (2 + 3)
```

When `)` arrives, the bracket calculation has reached:

```text
2 + 3
```

But notice:

```text
3
```

has not necessarily been processed yet.

So first:

```python
result += sign * number
```

Now the inside result becomes:

```text
5
```

Then restore:

```python
previous_sign = stack.pop()
previous_result = stack.pop()
```

We get:

```text
previous_sign = -1

previous_result = 10
```

Now combine:

```python
result = previous_result + previous_sign * result
```

So:

```text
result = 10 + (-1 × 5)

       = 5
```

---

# The Parentheses Formula

The most important formula for brackets is:

```text
Outside Result
+
Sign Before Bracket × Inside Result
```

In code:

```python
result = previous_result + previous_sign * result
```

Example:

```text
10 - (2 + 3)
```

becomes:

```text
10 + (-1 × 5)
```

Result:

```text
5
```

Another example:

```text
10 + (2 + 3)
```

becomes:

```text
10 + (1 × 5)
```

Result:

```text
15
```

---

# Why Does `previous_sign` Pop First?

At `(`, we push:

```python
stack.append(result)
stack.append(sign)
```

Suppose:

```text
result = 10
sign = -1
```

Stack becomes:

```text
[10, -1]
```

Stack follows:

```text
Last In, First Out
```

The last thing pushed was:

```text
sign
```

So the first thing popped must be:

```python
previous_sign = stack.pop()
```

Then:

```python
previous_result = stack.pop()
```

Remember:

```text
PUSH:
result → sign

POP:
sign → result
```

---

# Why Do We Add `sign * number` Inside `)`?

Consider:

```text
(2 + 3)
```

When `+` arrives:

```text
2
```

gets processed.

Then we build:

```text
3
```

But after `3`, the next character is:

```text
)
```

There is no `+` or `-` to process `3`.

Therefore, when `)` arrives:

```python
result += sign * number
```

processes the last number inside the bracket.

Without this line, the final number inside every bracket could be missed.

---

# Why Do We Again Add `sign * number` Before Return?

This is another easy thing to forget.

Consider:

```text
1 + 2
```

When `+` arrives:

```text
1
```

is processed.

Then:

```text
2
```

is built.

But the string ends.

There is no operator after `2`.

Therefore, `2` has not yet been added to `result`.

So before returning:

```python
result += sign * number
```

This processes the final pending number.

Remember:

```text
Numbers are normally processed
when we hit an operator.

But the last number has no operator after it.

So process it manually at the end.
```

---

# Important Difference Between These Two Lines

You will see this line twice:

```python
result += sign * number
```

### Inside `)`

```text
Finish the last pending number
inside the current parentheses.
```

### Before `return`

```text
Finish the last pending number
of the complete expression.
```

Same code, different stopping point.

---

# Dry Run

Consider:

```text
1 + (2 - 3)
```

Initial:

```text
result = 0
number = 0
sign = 1
stack = []
```

### Read `1`

```text
number = 1
```

### Read `+`

Process `1`:

```text
result = 1
number = 0
sign = 1
```

### Read `(`

Save:

```text
stack = [1, 1]
```

Reset:

```text
result = 0
sign = 1
```

### Read `2`

```text
number = 2
```

### Read `-`

Process `2`:

```text
result = 2
```

Set:

```text
sign = -1
number = 0
```

### Read `3`

```text
number = 3
```

### Read `)`

Process pending `3`:

```text
result = 2 + (-1 × 3)

       = -1
```

Restore:

```text
previous_sign = 1
previous_result = 1
```

Combine:

```text
result = 1 + 1 × (-1)

       = 0
```

Final answer:

```text
0
```

---

# Spaces

The code does not explicitly handle spaces:

```python
elif ch == ' ':
```

because spaces match none of the conditions.

So they are automatically ignored.

For:

```text
"1 + 2"
```

when `ch` is a space, nothing happens and the loop simply continues.

---

# Things You May Forget

## 1. Multi-digit number building

Do not do:

```python
number = int(ch)
```

because `123` would not be built correctly.

Use:

```python
number = number * 10 + int(ch)
```

---

## 2. Operator processes the previous number

When `+` or `-` arrives:

```python
result += sign * number
```

first.

Then reset:

```python
number = 0
```

Then set the sign for the next number.

---

## 3. Sign belongs to the current pending number

```text
10 - 5
```

When `-` is encountered:

```text
10 uses the old sign.

-1 is saved for 5.
```

---

## 4. At `(` save result and sign

```python
stack.append(result)
stack.append(sign)
```

Then reset:

```python
result = 0
sign = 1
```

---

## 5. Push and pop order

```text
Push:
result → sign

Pop:
sign → result
```

Because Stack is LIFO.

---

## 6. At `)` process the pending number first

```python
result += sign * number
number = 0
```

Then restore the outside context.

---

## 7. Parentheses combination formula

Never forget:

```python
result = previous_result + previous_sign * result
```

Meaning:

```text
Outside Result
+
Sign Before Bracket × Inside Result
```

---

## 8. Process the last number before return

```python
result += sign * number
```

because the final number may never encounter an operator.

---

# Complexity

## Time Complexity

```text
O(n)
```

We process every character once.

## Space Complexity

```text
O(n)
```

In the worst case, nested parentheses can store previous results and signs in the Stack.

---

# Pattern Recognition

```text
Stack + Expression Parsing
```

More specifically:

```text
Running Result + Sign Tracking + Parentheses Stack
```

---

# Revision Cheat Sheet

```text
DIGIT
    ↓
number = number * 10 + digit


+ or -
    ↓
result += sign * number
number = 0
set new sign


(
    ↓
push current result
push current sign
reset result and sign


)
    ↓
process pending number
pop previous sign
pop previous result
combine both


END
    ↓
process final pending number
```

The easiest way to remember the whole solution is:

```text
Number banao

→ Operator mila:
  previous number result me daalo

→ '(' mila:
  current result + sign save karo

→ ')' mila:
  bracket ka last number add karo
  aur outside calculation se combine karo

→ End:
  last pending number add karo
```

## Pattern Name

```text
Stack + Expression Parsing
```

The key idea is:

```text
Stack parentheses ka context save karta hai:

"Bracket se pehle result kya tha?"

and

"Bracket se pehle sign kya tha?"
```
