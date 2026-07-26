---

# 🚀 String Formatting

Python provides multiple ways to format strings.

## 1. f-Strings (Recommended)

Introduced in **Python 3.6**.

Syntax

```python
f"{variable}"
```

Example

```python
name = "Nitin"
age = 23

print(f"My name is {name} and I am {age} years old.")
```

Output

```
My name is Nitin and I am 23 years old.
```

---

### Expressions

You can evaluate expressions directly.

```python
a = 10
b = 20

print(f"Sum = {a+b}")
```

Output

```
Sum = 30
```

---

### Formatting Numbers

```python
pi = 3.14159265

print(f"{pi:.2f}")
```

Output

```
3.14
```

---

### Alignment

Left

```python
print(f"{'Python':<10}")
```

Right

```python
print(f"{'Python':>10}")
```

Center

```python
print(f"{'Python':^10}")
```

---

# 2. format()

```python
name = "Python"

print("Hello {}".format(name))
```

Output

```
Hello Python
```

---

# 3. % Formatting (Old Style)

```python
name = "Python"

print("Hello %s" % name)
```

Still found in older codebases.

---

# String Comparison

Strings are compared **lexicographically**.

Example

```python
print("abc" < "abd")
```

Output

```
True
```

Comparison occurs character by character using Unicode values.

---

# Membership Operator

```python
text = "Python"

print("Py" in text)

print("Java" in text)
```

Output

```
True

False
```

Complexity

```
O(n)
```

---

# Iterating Over Strings

Using a character

```python
for ch in "Python":
    print(ch)
```

---

Using index

```python
text = "Python"

for i in range(len(text)):
    print(text[i])
```

---

Using enumerate()

```python
for index, ch in enumerate("Python"):
    print(index, ch)
```

---

# Reverse a String

Method 1 (Slicing)

```python
text = "Python"

print(text[::-1])
```

Complexity

```
O(n)
```

---

Method 2

```python
"".join(reversed(text))
```

---

Method 3

```python
for ch in reversed(text):
    print(ch)
```

---

# Convert String to List

```python
text = "Python"

chars = list(text)
```

Output

```
['P','y','t','h','o','n']
```

Useful because lists are mutable.

---

# Convert List to String

```python
chars = ['P','y','t','h','o','n']

text = "".join(chars)
```

---

# Why Convert?

Suppose

```python
text = "Python"

text[0] = "J"
```

Impossible.

Instead

```python
chars = list(text)

chars[0] = "J"

text = "".join(chars)
```

Output

```
Jython
```

---

# ⭐ Palindrome

A palindrome reads the same forwards and backwards.

Example

```
madam
```

---

Method

```python
text = "madam"

print(text == text[::-1])
```

Complexity

```
Time : O(n)

Space : O(n)
```

---

Interview Optimization

Use two pointers.

```
Left

↓

m a d a m

↑

Right
```

Time

```
O(n)
```

Space

```
O(1)
```

---

# ⭐ Anagram

Two strings are anagrams if they contain the same characters with the same frequencies.

Example

```
listen

silent
```

Method 1

```python
sorted(s1) == sorted(s2)
```

Complexity

```
O(n log n)
```

---

Better

Use frequency counting.

```
Counter
```

Complexity

```
O(n)
```

We'll study `Counter` later.

---

# ⭐ Frequency Counting

Very common in interviews.

Example

```python
text = "banana"

freq = {}

for ch in text:
    freq[ch] = freq.get(ch,0) + 1

print(freq)
```

Output

```
{'b':1,'a':3,'n':2}
```

Later we'll use

```python
Counter(text)
```

---

# ⭐ Prefix

```python
text.startswith("Py")
```

---

# ⭐ Suffix

```python
text.endswith("on")
```

---

# ⭐ Sliding Window

Many interview problems use strings.

Examples

```
Longest Substring Without Repeating Characters

Minimum Window Substring

Permutation in String
```

Time Complexity

Usually

```
O(n)
```

---

# ⭐ Two Pointer

Very common.

Examples

```
Palindrome

Reverse String

Merge Strings

Remove Characters
```

---

# ⭐ Hashing

Strings are often combined with

```
Dictionary

Set

Counter
```

Examples

```
Valid Anagram

Group Anagrams

First Unique Character
```

---

# String Complexity Cheat Sheet

| Operation | Complexity |
|-----------|------------|
| Index | O(1) |
| Slice | O(k) |
| Concatenation | O(n) |
| Repeat | O(n×k) |
| Membership | O(n) |
| find() | O(n) |
| replace() | O(n) |
| split() | O(n) |
| join() | O(n) |
| upper() | O(n) |
| lower() | O(n) |
| strip() | O(n) |
| Reverse | O(n) |

---

# When Should You Use Strings?

Use strings when

- Data is read-only.
- Working with text.
- Pattern matching.
- Parsing.
- Input processing.

---

# When Should You Convert to a List?

When

- Frequent modifications.
- Swapping characters.
- In-place updates.
- Building strings repeatedly.

---

# Common Interview Mistakes

❌

```python
result += ch
```

inside loops.

Creates many temporary strings.

Prefer

```python
chars = []

chars.append(ch)

"".join(chars)
```

---

❌

Using

```python
replace()
```

thinking it changes the original string.

It doesn't.

---

❌

Using

```python
is
```

to compare strings.

Always use

```python
==
```

---

# DSA Tips

✅ Strings are immutable.

✅ Slicing creates a new string.

✅ Membership is O(n).

✅ `join()` is much faster than repeated `+`.

✅ Convert to a list before making many modifications.

✅ Learn

- Two Pointer
- Sliding Window
- Hashing

Most string interview problems use these techniques.

---

# Common LeetCode Problems

Easy

- 344 Reverse String
- 125 Valid Palindrome
- 242 Valid Anagram
- 58 Length of Last Word

Medium

- 3 Longest Substring Without Repeating Characters
- 49 Group Anagrams
- 5 Longest Palindromic Substring
- 438 Find All Anagrams in a String

Hard

- 76 Minimum Window Substring
- 30 Substring with Concatenation of All Words

---

# Interview Questions

1. Why are strings immutable?

2. Why is `join()` faster than `+`?

3. Difference between `find()` and `index()`?

4. Why is slicing O(k)?

5. Explain string interning.

6. Why can strings be dictionary keys?

7. Difference between list and string?

8. How would you reverse a string?

9. How would you detect a palindrome?

10. How would you check whether two strings are anagrams?

---

# Quick Revision

✔ Strings are immutable.

✔ Every string method returns a new string.

✔ `join()` is O(n).

✔ String concatenation is O(n).

✔ Use lists for heavy modifications.

✔ `find()` returns -1.

✔ `index()` raises an exception.

✔ Strings support Unicode.

✔ Learn Two Pointer + Sliding Window + Hashing for DSA.

---

# 🎉 Congratulations!

You have completed **Python Strings**.

In the next chapter (**06_Lists.md**), we'll study one of the most important Python data structures.

Topics include

- Dynamic Arrays
- Internal Working
- Memory Allocation
- append()
- extend()
- insert()
- remove()
- pop()
- sort()
- sorted()
- reverse()
- copy()
- Shallow vs Deep Copy
- Aliasing
- List Comprehensions
- Nested Lists
- Matrix
- Performance Analysis
- DSA Patterns
- Common Interview Questions

This will be one of the largest and most important chapters in the entire handbook.