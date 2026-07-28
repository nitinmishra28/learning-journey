# 1003. Check If Word Is Valid After Substitutions

## Problem

A string is considered **valid** if we can repeatedly remove the substring

```text
abc
```

until the string becomes empty.

Return

```text
True
```

if the string is valid,

otherwise return

```text
False
```

---

## Examples

### Example 1

```text
Input

abc
```

Output

```text
True
```

Explanation

```text
abc

↓

Remove abc

↓

Empty String
```

---

### Example 2

```text
Input

aabcbc
```

Output

```text
True
```

Explanation

```text
aabcbc

↓

a(abc)

↓

abc

↓

Remove abc

↓

Empty
```

---

### Example 3

```text
Input

abccba
```

Output

```text
False
```

Explanation

```text
abccba

↓

Remove abc

↓

cba
```

Now

```text
cba
```

cannot produce

```text
abc
```

Therefore answer is

```text
False
```

---

# Pattern

```text
Stack + Pattern Elimination (Continuous Pattern Reduction)
```

---

# Main Idea

Whenever the last three characters become

```text
abc
```

remove them immediately.

Repeat this until the entire string has been processed.

If the stack becomes empty,

the string was valid.

Otherwise,

some characters could never become

```text
abc
```

so the string is invalid.

---

# Complete Code with Comments

```python
class Solution:

    def isValid(self, s: str) -> bool:

        # Stack stores processed characters.
        stack = []

        # Process every character one by one.
        for ch in s:

            # Add current character.
            stack.append(ch)

            # If last three characters become "abc",
            # remove them immediately.
            if (
                len(stack) >= 3
                and stack[-3] == 'a'
                and stack[-2] == 'b'
                and stack[-1] == 'c'
            ):
                stack.pop()
                stack.pop()
                stack.pop()

        # If stack becomes empty,
        # every character was removed successfully.
        return len(stack) == 0
```

---

# Brute Force Solution

A straightforward idea is:

```text
Find "abc"

↓

Remove it

↓

Create a new string

↓

Again search for "abc"

↓

Repeat
```

Example

```text
aabcbc

↓

Remove abc

↓

abc

↓

Remove abc

↓

Empty
```

This works,

but every removal creates a new string.

Again we search from the beginning.

Again we copy characters.

Again we create another string.

This repeated work makes the solution inefficient.

---

# Why Stack?

Instead of rebuilding the string again and again,

we process every character only once.

Every new character is pushed into the stack.

Whenever the top becomes

```text
abc
```

remove it immediately.

Example

```text
Input

aabcbc
```

Process

```text
Push a

Stack

a
```

Push

```text
a

Stack

a
a
```

Push

```text
b

Stack

a
a
b
```

Push

```text
c

Stack

a
a
b
c
```

Last three characters are

```text
abc
```

Remove them.

Stack becomes

```text
a
```

Continue.

Push

```text
b

Stack

a
b
```

Push

```text
c

Stack

a
b
c
```

Again

```text
abc
```

Remove.

Stack

```text
Empty
```

No rebuilding.

No rescanning.

Everything happens while reading the string.

---

# Why Push First?

Notice the code

```python
stack.append(ch)
```

comes before checking

```python
if len(stack) >= 3 ...
```

Why?

Because the current character might complete

```text
abc
```

Suppose stack contains

```text
a
b
```

Current character

```text
c
```

If we check before pushing,

stack is

```text
a
b
```

There is no

```text
abc
```

After pushing

```text
c
```

Stack becomes

```text
a
b
c
```

Now

```text
abc
```

is complete.

Therefore

```text
Always Push First

↓

Then Check Pattern
```

---

# Why Check Only Last Three Characters?

Suppose stack is

```text
a
a
b
c
```

Only the newest characters can create a **new** pattern.

Everything before them has already been checked.

Therefore,

there is absolutely no need to scan the whole stack every time.

Simply check

```python
stack[-3]
stack[-2]
stack[-1]
```

Example

```text
Stack

a
a
b
c
```

Last three

```text
a
b
c
```

Pattern found.

Remove it.

Done.

Checking the entire stack every time would increase the complexity unnecessarily.

---

# Why Do We Remove Exactly Three Characters?

Because

```text
abc
```

contains exactly three characters.

After confirming

```text
stack[-3] == 'a'

stack[-2] == 'b'

stack[-1] == 'c'
```

we simply remove

```python
stack.pop()
stack.pop()
stack.pop()
```

Remember,

a stack always removes from the top.

Order of removal becomes

```text
c

↓

b

↓

a
```

which is perfectly fine because the whole substring disappears together.

You never need to remove

```text
a

↓

b

↓

c
```

A stack always pops from the top.

---

# Mental Model

Imagine the stack is a machine.

Every character enters from the right.

```text
Input

a → b → c
```

As soon as the machine sees

```text
abc
```

at the top,

it immediately destroys it.

```text
a b c

↓

Machine

↓

Removed
```

Then the next characters continue entering.

The machine keeps destroying every newly formed

```text
abc
```

until the input ends.

If nothing survives,

the string is valid.

Otherwise,

the remaining characters can never become

```text
abc
```

so the answer is **False**.
