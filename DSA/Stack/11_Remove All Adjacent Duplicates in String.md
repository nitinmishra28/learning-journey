# Remove All Adjacent Duplicates in String

## Problem

Given a string `s`, repeatedly remove two adjacent characters if they are the same.

Continue until no adjacent duplicate pair remains.

Example:

```text id="6gqgnv"
s = "abbaca"
```

Process:

```text id="70al1n"
abbaca
 ↓
Remove "bb"

aaca
↓
Remove "aa"

ca
```

Output:

```text id="z0svbe"
"ca"
```

---

# Main Idea

Use a Stack to keep only the characters that are currently valid.

For every character:

```text id="qnj6wf"
Current character == Stack top
        ↓
Duplicate pair found
        ↓
Pop Stack top


Current character != Stack top
        ↓
No duplicate
        ↓
Push current character
```

The complete flow is:

```text id="j0ad8i"
Traverse string
      ↓
Compare current character with Stack top
      ↓
Same?
 /         \
Yes         No
 ↓           ↓
Pop         Push
      ↓
Join Stack
```

---

# Code with Comments

```python id="s9rxug"
class Solution:
    def removeDuplicates(self, s: str) -> str:

        # Stack stores characters that have
        # not been removed
        stack = []

        for ch in s:

            # If current character is same as
            # the previous remaining character,
            # we found an adjacent duplicate pair
            if stack and ch == stack[-1]:

                # Remove the previous character.
                #
                # Current character is also not added,
                # so both duplicates are removed.
                stack.pop()

            else:

                # No duplicate pair exists,
                # so keep the current character
                stack.append(ch)


        # Convert remaining characters
        # from list to string
        return "".join(stack)
```

---

# Why Do We Use a Stack?

We need to compare every new character with the:

```text id="gbrl3e"
Previous remaining character
```

Notice the word:

```text id="6xjtmz"
remaining
```

We cannot simply compare with:

```python id="yy7u6f"
s[i - 1]
```

because previous characters may already have been removed.

The Stack top always represents:

```python id="26bbd5"
stack[-1]
```

which is:

```text id="sk4dmv"
The latest character that still exists
in our final answer so far.
```

Therefore:

```python id="l84e0f"
ch == stack[-1]
```

checks whether the current character forms an adjacent duplicate with the previous remaining character.

---

# Dry Run

Consider:

```text id="k4t3gg"
s = "abbaca"
```

Initially:

```text id="7szv5l"
stack = []
```

---

## Character = `a`

Stack is empty.

Push:

```text id="0ynq1h"
stack = ['a']
```

---

## Character = `b`

Compare:

```text id="dck3az"
b != a
```

Push:

```text id="0fkaiq"
stack = ['a', 'b']
```

---

## Character = `b`

Compare:

```text id="l8b9dd"
b == b
```

Duplicate found.

Pop:

```text id="ebjspe"
stack = ['a']
```

Notice that the current `b` is also not pushed.

So both `b`s are removed.

---

## Character = `a`

Current Stack:

```text id="jyz8a2"
['a']
```

Compare:

```text id="n4r54p"
a == a
```

These two `a`s were not originally adjacent.

But after removing:

```text id="nax7bd"
bb
```

they became adjacent.

So pop:

```text id="pz2nsl"
stack = []
```

This automatically handles the new duplicate created after previous removals.

---

## Character = `c`

Push:

```text id="sujhlb"
stack = ['c']
```

---

## Character = `a`

```text id="8l6z6w"
a != c
```

Push:

```text id="pdj2kl"
stack = ['c', 'a']
```

Final Stack:

```text id="92lt7h"
['c', 'a']
```

Convert to string:

```text id="x62jpx"
"ca"
```

---

# Most Important Concept — Chain Reaction

Consider:

```text id="3i0k6n"
abbaca
```

Initially:

```text id="r52zkx"
a b b a
```

The two `a`s are not adjacent.

But after removing:

```text id="p2fr7k"
bb
```

we get:

```text id="axam35"
aa
```

Now these also need to be removed.

This is called a:

```text id="9tm8nr"
Chain Reaction
```

The Stack handles this automatically.

Why?

After removing `bb`:

```text id="2x91v0"
stack = ['a']
```

When the next `a` arrives:

```text id="rqtftl"
Current = 'a'

Stack Top = 'a'
```

So:

```text id="d2qyrm"
Duplicate found
```

and it gets removed automatically.

This is the main reason Stack is useful here.

---

# Why Does `pop()` Remove Both Characters?

The code only does:

```python id="8c84ai"
stack.pop()
```

So it may look like we are removing only one character.

But remember:

```text id="70fnku"
Previous duplicate
→ Already inside Stack


Current duplicate
→ Has NOT been pushed yet
```

When they are equal:

```python id="nj1lrz"
stack.pop()
```

removes the previous character.

And because we do not execute:

```python id="0oxdvu"
stack.append(ch)
```

the current character is also discarded.

Therefore:

```text id="1dnx7k"
Previous duplicate → Popped

Current duplicate  → Never pushed
```

So both characters are removed.

---

# Why Check `stack` First?

The condition is:

```python id="xwtdxb"
if stack and ch == stack[-1]:
```

We first check:

```python id="66k1o5"
stack
```

because if the Stack is empty:

```python id="ldsyjc"
stack[-1]
```

would cause an error.

So:

```text id="85gtp2"
stack
    ↓
Is Stack non-empty?


ch == stack[-1]
    ↓
Is current character equal to Stack top?
```

Python uses short-circuit evaluation.

If:

```text id="epn27e"
stack is empty
```

then Python does not evaluate:

```python id="1prujk"
ch == stack[-1]
```

So no error occurs.

---

# Why `"".join(stack)`?

At the end, the Stack is a Python list:

```python id="3yusbu"
['c', 'a']
```

But the required answer is a string:

```text id="x5t1rx"
"ca"
```

So:

```python id="9u68ho"
"".join(stack)
```

joins all characters with nothing between them.

Example:

```python id="xxo10p"
stack = ['c', 'a']

"".join(stack)
```

Result:

```text id="4qetly"
"ca"
```

If we used:

```python id="mtuupb"
"-".join(stack)
```

the result would be:

```text id="shqu9n"
"c-a"
```

So:

```text id="h50c1a"
""
```

means:

```text id="89qwhp"
Join characters without any separator.
```

---

# Things You May Forget

## 1. Compare With Stack Top

```python id="29e44f"
ch == stack[-1]
```

because Stack top is the latest remaining character.

---

## 2. Check If Stack Is Non-Empty

Correct:

```python id="tjd8k4"
if stack and ch == stack[-1]:
```

Otherwise:

```python id="i4cp1a"
stack[-1]
```

can fail when the Stack is empty.

---

## 3. Do Not Push Current Character After Finding Duplicate

When:

```python id="fz6sbv"
ch == stack[-1]
```

only:

```python id="awuv9n"
stack.pop()
```

is needed.

The current character should not be pushed.

That is how both duplicates disappear.

---

## 4. Stack Automatically Handles Chain Reactions

Example:

```text id="x7vnzg"
abbaca
  ↓
Remove bb
  ↓
aaca
  ↓
New aa becomes adjacent
  ↓
Remove aa
```

No extra loop is needed.

---

## 5. Convert Stack Back to String

```python id="u5cc8i"
return "".join(stack)
```

because the Stack is a list but the required answer is a string.

---

# Complexity

## Time Complexity

```text id="x76kpb"
O(n)
```

Every character is pushed at most once and popped at most once.

## Space Complexity

```text id="1jkjxr"
O(n)
```

In the worst case, there are no adjacent duplicates and every character remains in the Stack.

---

# Revision Summary

```text id="s9uqvw"
For every character:

Stack empty?
    ↓
Push


Current == Stack Top?
    ↓
Pop
(Both duplicates removed)


Current != Stack Top?
    ↓
Push


Finally:
"".join(stack)
```

The easiest way to remember:

```text id="gjp7wi"
Current character ko
previous REMAINING character se compare karo.

Same → Pop

Different → Push
```

The key word is:

```text id="xksn1b"
REMAINING
```

That is why Stack works better than simply checking the previous index.

## Pattern Name

```text id="p6kgjk"
Stack + Adjacent Pair Cancellation
```
