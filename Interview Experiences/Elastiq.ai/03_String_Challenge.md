# Elastiq.ai - Python Developer Assessment

## Question 3: String Challenge

**Company:** Elastiq.ai  
**Role:** Python Developer  
**Assessment Type:** Quick Online Assessment  
**Category:** String Manipulation  

---

## Problem Statement

Transform the given input string according to the rules provided in the assessment.

The challenge involves cleaning and transforming a string containing:

- Uppercase letters
- Lowercase letters
- Special characters
- Separators

---

## Example

### Input

```text
"cats AND*Dogs-are Awesome"
```

### Intermediate / Expected Output

```text
cats_and_dogs_are_awesome
```

### Final Output Shown in Assessment

```text
ts_nd_dos_e_wesome
```

---

## Pattern

```text
String Traversal + Character Filtering + String Normalization
```

### Concepts Involved

- String traversal
- Lowercase conversion
- Character validation
- Special-character handling
- Replacing separators
- Building a normalized result

---

## General Processing Flow

```text
Original String

"cats AND*Dogs-are Awesome"

        ↓

Convert characters to lowercase

        ↓

Handle spaces and special characters

        ↓

Normalize separators

        ↓

Build transformed string

        ↓

Final Result
```

---

## Python Concepts Useful for This Problem

```python
.lower()
.isalpha()
.isalnum()
.replace()
split()
join()
```

Depending on the exact transformation rules, the string can also be processed manually using a loop.

---

## Example Normalization

Input:

```text
cats AND*Dogs-are Awesome
```

Normalized form:

```text
cats_and_dogs_are_awesome
```

Final output provided in the assessment:

```text
ts_nd_dos_e_wesome
```

---

## Pattern Recognition

When a problem asks you to:

- Remove unwanted characters
- Convert uppercase to lowercase
- Replace spaces or symbols
- Build a specific output format

Think about:

```text
String Traversal + Character Validation
```

A common structure is:

```python
result = ""

for char in text:

    # Check the character

    # Transform if required

    # Add it to the result
```

---

## Complexity

If the input string contains `n` characters:

```text
Time Complexity: O(n)
Space Complexity: O(n)
```

---

## Key Takeaways

- Process strings one character at a time when transformation rules are custom.
- Use built-in methods only when they directly match the required transformation.
- Normalize uppercase and lowercase early if the output is case-insensitive.
- Carefully distinguish between spaces, special characters, and alphanumeric characters.
- Always verify the final transformation rules against all provided examples.