# Valid Parentheses

## Problem Overview

Given a string `s` containing only these bracket characters:

```text
( ) { } [ ]
```

Check whether the string is valid.

A string is valid when:

1. Every opening bracket has a matching closing bracket.
2. Brackets are closed in the correct order.
3. Every closing bracket has a corresponding opening bracket.

---

# Examples

### Valid

```text
()
```

```text
()[]{}
```

```text
{[()]}
```

### Invalid

```text
(]
```

```text
([)]
```

```text
(((
```

```text
)))
```

---

# Why Do We Use a Stack?

Consider:

```text
{ [ ( ) ] }
```

Opening brackets appear in this order:

```text
{
[
(
```

But they must close in the reverse order:

```text
)
]
}
```

So:

```text
Last Opening Bracket
        ↓
Must Close First
```

This is exactly:

```text
LIFO

Last In, First Out
```

Therefore, Stack is the perfect data structure for this problem.

---

# Approach — Stack + Hash Map

We use:

```python
stack = []
```

to store opening brackets.

We also use:

```python
mapping = {
    ")": "(",
    "}": "{",
    "]": "["
}
```

The mapping tells us which opening bracket belongs to each closing bracket.

For example:

```text
Current Closing    Expected Opening

)                   (
}                   {
]                   [
```

---

# Python Code

```python
class Solution:
    def isValid(self, s: str) -> bool:

        # Stack stores opening brackets
        stack = []

        # Closing bracket → Matching opening bracket
        mapping = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for ch in s:

            # If current character is a closing bracket
            if ch in mapping:

                # Get the latest opening bracket
                # If stack is empty, use a sentinel value
                topElement = stack.pop() if stack else '#'

                # Check whether brackets match
                if mapping[ch] != topElement:
                    return False

            # Current character is an opening bracket
            else:
                stack.append(ch)

        # Valid only if no unmatched opening brackets remain
        if len(stack) == 0:
            return True
        else:
            return False
```

---

# Core Idea

The algorithm follows this logic:

```text
Opening Bracket
      ↓
Push into Stack


Closing Bracket
      ↓
Get Stack Top
      ↓
Check Matching Pair
      ↓
Match?
 ┌────┴────┐
Yes        No
 ↓          ↓
Continue   False
```

After processing the complete string:

```text
Stack Empty?
 ┌────┴────┐
Yes        No
 ↓          ↓
True       False
```

---

# Understanding the Mapping

The dictionary is:

```python
mapping = {
    ")": "(",
    "}": "{",
    "]": "["
}
```

The keys are:

```text
)
}
]
```

These are all closing brackets.

The values are:

```text
(
{
[
```

These are their matching opening brackets.

Therefore:

```python
mapping[")"]
```

returns:

```text
(
```

Similarly:

```python
mapping["}"]
```

returns:

```text
{
```

And:

```python
mapping["]"]
```

returns:

```text
[
```

This lets us check a pair using:

```python
if mapping[ch] != topElement:
    return False
```

---

# Why Check `if ch in mapping`?

The dictionary contains only closing brackets:

```python
mapping = {
    ")": "(",
    "}": "{",
    "]": "["
}
```

Therefore:

```python
if ch in mapping:
```

means:

```text
Is the current character a closing bracket?
```

If yes:

```text
Check whether it matches the latest opening bracket.
```

Otherwise:

```text
It is an opening bracket.
```

So we push it:

```python
stack.append(ch)
```

---

# Why Do We Push Opening Brackets?

Suppose:

```text
{[(
```

We process:

```text
{
↓
Push

Stack = ["{"]
```

Then:

```text
[
↓
Push

Stack = ["{", "["]
```

Then:

```text
(
↓
Push

Stack = ["{", "[", "("]
```

The top is:

```text
(
```

This is important because the next closing bracket must match the most recently opened bracket.

---

# Why Do We Pop for a Closing Bracket?

Suppose the Stack is:

```text
["{", "[", "("]
```

Current character:

```text
)
```

The most recently opened bracket is:

```text
(
```

So we pop:

```python
topElement = stack.pop()
```

Now:

```text
topElement = "("
```

Then check:

```python
mapping[")"] == topElement
```

which becomes:

```text
"(" == "("
```

So the pair is valid.

---

# Why Only Check the Stack Top?

Consider:

```text
([)]
```

After processing:

```text
(
[
```

the Stack is:

```text
["(", "["]
```

Now the current character is:

```text
)
```

Technically, there is a `(` somewhere inside the Stack.

But we cannot use it.

Why?

Because the most recently opened bracket is:

```text
[
```

So `[` must close before `(`.

The required order is:

```text
(
    [
    ]
)
```

But the input is:

```text
(
    [
)
    ]
```

Therefore:

```text
([)]
```

is invalid.

This is exactly why we only compare with:

```text
Stack Top
```

and not search the entire Stack.

---

# Understanding This Line

The most interesting line in the solution is:

```python
topElement = stack.pop() if stack else '#'
```

This is a Python conditional expression.

It means:

```python
if stack:
    topElement = stack.pop()
else:
    topElement = '#'
```

So:

```text
Stack has elements
        ↓
Pop the top element


Stack is empty
        ↓
Use '#'
```

---

# Why Do We Use `'#'`?

Suppose:

```text
s = ")"
```

The first character itself is a closing bracket.

But:

```text
stack = []
```

There is no opening bracket available.

If we directly write:

```python
stack.pop()
```

Python will raise:

```text
IndexError
```

Instead:

```python
topElement = stack.pop() if stack else '#'
```

gives:

```text
topElement = '#'
```

Now:

```python
mapping[")"] != '#'
```

becomes:

```text
"(" != "#"
```

which is:

```text
True
```

So the function safely returns:

```python
False
```

---

# `'#'` Is a Sentinel Value

The value:

```text
#
```

is acting as a:

```text
Sentinel Value
```

It represents:

```text
No valid opening bracket exists
```

Since `#` can never match:

```text
(
{
[
```

the comparison automatically fails.

This avoids writing an additional condition.

Instead of:

```python
if not stack:
    return False

topElement = stack.pop()
```

we write:

```python
topElement = stack.pop() if stack else '#'
```

Both approaches are valid.

---

# Complete Dry Run — Valid Input

Input:

```text
s = "{[()]}"
```

Initial:

```text
stack = []
```

---

## Character `{`

`{` is not a key in `mapping`.

So:

```python
stack.append("{")
```

Stack:

```text
["{"]
```

---

## Character `[`

Opening bracket.

Push:

```text
["{", "["]
```

---

## Character `(`

Opening bracket.

Push:

```text
["{", "[", "("]
```

---

## Character `)`

Closing bracket.

Pop:

```text
topElement = "("
```

Check:

```text
mapping[")"] == "("
```

Result:

```text
True
```

Stack:

```text
["{", "["]
```

---

## Character `]`

Closing bracket.

Pop:

```text
topElement = "["
```

Check:

```text
mapping["]"] == "["
```

Result:

```text
True
```

Stack:

```text
["{"]
```

---

## Character `}`

Closing bracket.

Pop:

```text
topElement = "{"
```

Check:

```text
mapping["}"] == "{"
```

Result:

```text
True
```

Stack:

```text
[]
```

All characters are processed.

The Stack is empty.

Therefore:

```text
True
```

---

# Complete Dry Run — Wrong Bracket Type

Input:

```text
s = "(]"
```

Process:

```text
(
↓
Push
```

Stack:

```text
["("]
```

Next:

```text
]
```

Pop:

```text
topElement = "("
```

Expected opening bracket:

```python
mapping["]"]
```

which is:

```text
[
```

Compare:

```text
"[" != "("
```

Therefore:

```text
False
```

---

# Complete Dry Run — Wrong Closing Order

Input:

```text
s = "([)]"
```

Process `(`:

```text
["("]
```

Process `[`:

```text
["(", "["]
```

Process `)`:

```text
topElement = "["
```

But:

```python
mapping[")"]
```

expects:

```text
(
```

Comparison:

```text
"(" != "["
```

Therefore:

```text
False
```

This demonstrates the most important idea:

```text
Correct brackets are not enough.

They must also close in the correct order.
```

---

# Edge Case — Only Opening Brackets

Input:

```text
(((
```

Processing pushes everything:

```text
["(", "(", "("]
```

No mismatch occurs during traversal.

But after the loop:

```text
stack is not empty
```

This means there are unmatched opening brackets.

Therefore:

```text
False
```

This is why the final empty-stack check is necessary.

---

# Edge Case — Only Closing Brackets

Input:

```text
)))
```

For the first `)`:

```text
stack = []
```

So:

```text
topElement = '#'
```

Comparison fails immediately.

Therefore:

```text
False
```

---

# Edge Case — Empty String

Input:

```text
""
```

No characters are processed.

Stack remains:

```text
[]
```

Therefore:

```text
True
```

An empty string is considered valid because there are no unmatched brackets.

---

# Why Must the Stack Be Empty at the End?

Consider:

```text
s = "(("
```

No incorrect closing bracket appears.

So the loop never returns `False`.

But:

```text
stack = ["(", "("]
```

after processing the complete string.

These represent opening brackets that were never closed.

Therefore:

```text
Stack Not Empty
        ↓
Unmatched Opening Brackets
        ↓
False
```

A valid parentheses string must finish with:

```text
stack = []
```

---

# Early Termination

The solution immediately returns:

```python
return False
```

when a mismatch is found.

For example:

```text
([)]
```

As soon as we compare:

```text
Current Closing = )

Stack Top = [
```

we know the complete string cannot be valid.

There is no reason to process the remaining characters.

This is called:

```text
Early Termination
```

---

# Time Complexity

We process every character at most once.

For each character:

```text
Push → O(1)

Pop → O(1)

Dictionary Lookup → O(1)
```

For a string of length `n`:

```text
Time Complexity = O(n)
```

---

# Space Complexity

In the worst case, every character is an opening bracket:

```text
(((((((
```

All characters are stored in the Stack.

Therefore:

```text
Space Complexity = O(n)
```

---

# Pattern Used

For your DSA pattern sheet, use:

```text
Stack + Matching Pairs
```

A slightly more complete name:

```text
Stack + Hash Map + Matching Pairs
```

The core flow is:

```text
Opening → Push

Closing → Pop + Match
```

---

# How to Recognize This Pattern

Think about using this pattern when the problem contains:

```text
Opening and Closing Symbols
        ↓
Nested Structure
        ↓
Most Recent Opening Must Close First
        ↓
STACK
```

Examples of similar ideas include:

```text
Parentheses Matching

Nested Brackets

HTML/XML-like Tag Matching

Expression Parsing

Nested Structures
```

The important clue is:

```text
The most recently opened thing
must be closed first.
```

That means:

```text
LIFO
```

which strongly suggests:

```text
Stack
```

---

# Key Learning

The complete algorithm is:

```text
Traverse String
      ↓

Opening Bracket?
      ↓
Push


Closing Bracket?
      ↓
Pop Most Recent Opening
      ↓
Check Matching Pair
      ↓

Mismatch?
      ↓
Return False


Traversal Complete
      ↓
Stack Empty?
   ┌─────┴─────┐
  Yes          No
   ↓            ↓
 True         False
```

The most important concepts are:

```text
1. Opening brackets are pushed into the Stack.

2. Closing brackets are used to check the Stack top.

3. The Stack top represents the most recently
   unmatched opening bracket.

4. A Hash Map stores matching bracket pairs.

5. If the Stack is empty when a closing bracket arrives,
   the string is invalid.

6. '#' acts as a sentinel for an empty Stack.

7. If brackets do not match, return False immediately.

8. The Stack must be empty after processing everything.

9. Time Complexity = O(n).

10. Space Complexity = O(n).
```

The strongest mental model is:

```text
Stack stores:

"Opening brackets waiting to be closed."
```

Whenever a closing bracket arrives, ask:

```text
"Does this close the most recent
unmatched opening bracket?"
```

If yes, pop it and continue.

If no, the string is invalid.
