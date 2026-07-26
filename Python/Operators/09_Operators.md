---

# 🔢 Bitwise Operators

Bitwise operators work directly on the **binary representation** of integers.

Instead of operating on decimal numbers, Python first converts numbers into binary, performs the operation, and then converts the result back to decimal.

Example

```python
5 & 3
```

Internally

```
5 = 101

3 = 011

---------
    001

= 1
```

---

# Binary Number System

Understanding binary is essential for bit manipulation.

| Decimal | Binary |
|---------:|:------|
| 0 | 0000 |
| 1 | 0001 |
| 2 | 0010 |
| 3 | 0011 |
| 4 | 0100 |
| 5 | 0101 |
| 6 | 0110 |
| 7 | 0111 |
| 8 | 1000 |

---

# Bitwise AND (&)

Returns **1** only if **both bits are 1**.

Truth Table

| A | B | A & B |
|---|---|-------|
|0|0|0|
|0|1|0|
|1|0|0|
|1|1|1|

Example

```python
print(5 & 3)
```

Binary

```
101

011

---

001
```

Output

```
1
```

### Common Uses

- Masking bits
- Checking flags
- Even/Odd checking

Example

```python
if n & 1:
    print("Odd")
else:
    print("Even")
```

Time Complexity

```
O(1)
```

---

# Bitwise OR (|)

Returns **1** if **either bit is 1**.

Truth Table

| A | B | A \| B |
|---|---|--------|
|0|0|0|
|0|1|1|
|1|0|1|
|1|1|1|

Example

```python
print(5 | 3)
```

Binary

```
101

011

---

111
```

Output

```
7
```

---

# Bitwise XOR (^)

Returns **1** when bits are different.

Truth Table

| A | B | A ^ B |
|---|---|-------|
|0|0|0|
|0|1|1|
|1|0|1|
|1|1|0|

Example

```python
print(5 ^ 3)
```

Output

```
6
```

Binary

```
101

011

---

110
```

---

## XOR Properties ⭐ (Very Important)

These properties are heavily used in DSA.

```
x ^ 0 = x
```

```
x ^ x = 0
```

```
x ^ y ^ x = y
```

```
XOR is commutative
```

```
a ^ b == b ^ a
```

```
XOR is associative
```

```
(a ^ b) ^ c

=

a ^ (b ^ c)
```

---

## DSA Trick 1: Find Single Number

Problem

Every element appears twice except one.

Example

```python
nums = [2,3,5,3,2]
```

Solution

```python
ans = 0

for x in nums:
    ans ^= x

print(ans)
```

Output

```
5
```

Time Complexity

```
O(n)
```

Space

```
O(1)
```

LeetCode

```
136. Single Number
```

---

## DSA Trick 2: Swap Without Extra Variable

```python
a = 10

b = 20

a ^= b

b ^= a

a ^= b
```

Works but **not recommended**.

Python provides

```python
a, b = b, a
```

which is cleaner.

---

# Bitwise NOT (~)

Flips every bit.

Example

```python
print(~5)
```

Output

```
-6
```

### Why?

Formula

```
~x

=

-(x+1)
```

So

```
~5

=

-(5+1)

=

-6
```

Interview Favorite.

---

# Left Shift (<<)

Moves bits left.

Example

```python
print(5 << 1)
```

Binary

```
101

↓

1010
```

Output

```
10
```

Formula

```
x << n

=

x × 2ⁿ
```

Example

```python
7 << 3
```

```
7 × 8

=

56
```

---

# Right Shift (>>)

Moves bits right.

Example

```python
print(8 >> 1)
```

Binary

```
1000

↓

100
```

Output

```
4
```

Formula

```
x >> n

=

x // 2ⁿ
```

---

# Operator Precedence

Python follows precedence rules.

Higher precedence executes first.

| Operator | Priority |
|----------|----------|
| () | Highest |
| ** | |
| +x -x ~x | |
| * / // % | |
| + - | |
| << >> | |
| & | |
| ^ | |
| \| | |
| Comparison | |
| not | |
| and | |
| or | Lowest |

---

Example

```python
print(2 + 3 * 4)
```

Output

```
14
```

Not

```
20
```

because

```
3 × 4
```

is evaluated first.

---

# Associativity

Example

```python
2 ** 3 ** 2
```

Python evaluates

```
2 ** (3 ** 2)
```

not

```
(2 ** 3) ** 2
```

Output

```
512
```

---

# Ternary Operator

Python provides a one-line if-else.

Syntax

```python
value_if_true if condition else value_if_false
```

Example

```python
age = 20

status = "Adult" if age >= 18 else "Minor"

print(status)
```

Output

```
Adult
```

---

# Walrus Operator (:=)

Introduced in Python 3.8.

Allows assignment inside an expression.

Example

```python
if (n := len("Python")) > 5:
    print(n)
```

Output

```
6
```

Use sparingly for readability.

---

# Time Complexity

Almost every operator works in

```
O(1)
```

except operations involving large objects.

Examples

```
String +

↓

O(n)
```

```
List +

↓

O(n)
```

```
Membership in list

↓

O(n)
```

```
Membership in set

↓

O(1)
```

---

# Best Practices

✅ Use

```python
a, b = b, a
```

instead of XOR swap.

---

✅ Use

```python
pow(a,b,mod)
```

instead of

```python
a ** b % mod
```

for modular exponentiation.

---

✅ Use

```python
x & 1
```

to check odd/even in bit manipulation problems.

---

✅ Prefer readability over clever bit hacks unless performance matters.

---

# Common Mistakes

❌

Confusing

```
^
```

with exponent.

In Python

```
^

↓

XOR
```

Exponent is

```
**
```

---

❌

Thinking

```
~

↓

Negative Sign
```

Actually

```
~x

=

-(x+1)
```

---

❌

Ignoring operator precedence.

Always use parentheses if the expression is not obvious.

---

# DSA Tips

Bitwise operators are used in

- Bit Manipulation
- Dynamic Programming
- Trie
- Segment Tree
- Fenwick Tree
- XOR Problems
- Competitive Programming

Important LeetCode problems

- 136 Single Number
- 137 Single Number II
- 190 Reverse Bits
- 191 Number of 1 Bits
- 231 Power of Two
- 268 Missing Number
- 338 Counting Bits

---

# Interview Questions

1. Difference between `&` and `&&`? (Python doesn't have `&&`; use `and`.)
2. Difference between `^` and `**`?
3. Why does `~5` equal `-6`?
4. How do left and right shift work?
5. What are XOR properties?
6. How do you find a unique number using XOR?
7. What is operator precedence?
8. What is the Walrus operator?
9. What is the ternary operator?
10. Why is `pow(a, b, mod)` preferred for modular arithmetic?

---

# Quick Revision

✔ Arithmetic operators perform mathematical operations.

✔ Comparison operators return Boolean values.

✔ Logical operators use short-circuit evaluation.

✔ Membership in sets and dictionaries is O(1) on average.

✔ `==` compares values.

✔ `is` compares object identity.

✔ Bitwise operators work on binary numbers.

✔ XOR is heavily used in DSA.

✔ `<<` multiplies by powers of 2.

✔ `>>` divides by powers of 2.

✔ `~x = -(x + 1)`.

✔ Python supports the ternary operator.

✔ Python supports the walrus operator (`:=`).

---

# Practice Questions

## Theory

1. Explain the difference between `==` and `is`.
2. What is short-circuit evaluation?
3. Why is `^` not exponentiation in Python?
4. Explain XOR properties.
5. What is the difference between `and` and `&`?
6. How does the walrus operator work?
7. Explain operator precedence.
8. Why does `~5` return `-6`?
9. When should you use `pow(a, b, mod)`?
10. What is the time complexity of bitwise operations?

---

## Coding

1. Check whether a number is even or odd using bitwise operators.
2. Find the only unique number in an array where every other element appears twice.
3. Swap two numbers using tuple unpacking.
4. Swap two numbers using XOR.
5. Count set bits in an integer.
6. Check whether a number is a power of two.
7. Reverse the bits of a number.
8. Use a ternary operator to classify a number as positive or negative.
9. Use the walrus operator in a simple program.
10. Solve LeetCode 136 (Single Number).

---

# 🎉 Congratulations!

You have successfully completed **03_Operators.md**.

In the next chapter (**04_Variables.md**), we'll dive into:

- Variable Assignment
- Multiple Assignment
- Object References
- Variable Aliasing
- Memory Addresses (`id()`)
- Mutable vs Immutable Variables
- Reference Counting
- Garbage Collection (Variable Perspective)
- Namespace
- Scope (Preview)
- Variable Shadowing
- `global` and `nonlocal` (Preview)
- Common Interview Questions
- DSA Tips