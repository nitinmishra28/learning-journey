---

# 🛠️ String Methods

Unlike lists, **string methods never modify the original string** because strings are **immutable**.

Instead, every string method returns a **new string**.

Example

```python
name = "python"

new_name = name.upper()

print(name)
print(new_name)
```

Output

```
python
PYTHON
```

Notice

The original string remains unchanged.

---

# upper()

Converts every lowercase character into uppercase.

Syntax

```python
string.upper()
```

Example

```python
name = "python"

print(name.upper())
```

Output

```
PYTHON
```

### In-place?

❌ No

### Return Value

Returns a **new string**.

### Time Complexity

```
O(n)
```

---

# lower()

Converts every uppercase character into lowercase.

```python
text = "PyThOn"

print(text.lower())
```

Output

```
python
```

Complexity

```
O(n)
```

---

# capitalize()

Capitalizes only the first character.

```python
text = "python programming"

print(text.capitalize())
```

Output

```
Python programming
```

---

# title()

Capitalizes the first letter of every word.

```python
text = "hello world"

print(text.title())
```

Output

```
Hello World
```

---

# swapcase()

Converts

Upper → Lower

Lower → Upper

```python
text = "PyThOn"

print(text.swapcase())
```

Output

```
pYtHoN
```

---

# strip()

Removes whitespace from both sides.

```python
text = "   Python   "

print(text.strip())
```

Output

```
Python
```

### Complexity

```
O(n)
```

---

# lstrip()

Removes whitespace from the left.

```python
print("   Python".lstrip())
```

Output

```
Python
```

---

# rstrip()

Removes whitespace from the right.

```python
print("Python   ".rstrip())
```

Output

```
Python
```

---

# Removing Specific Characters

```python
text = "###Python###"

print(text.strip("#"))
```

Output

```
Python
```

⚠️ Important

`strip()` removes characters from **both ends only**.

It does **not** remove characters from the middle.

Example

```python
print("abca".strip("a"))
```

Output

```
bc
```

---

# replace()

Replaces occurrences of a substring.

Syntax

```python
string.replace(old, new, count)
```

Example

```python
text = "I like Java"

print(text.replace("Java","Python"))
```

Output

```
I like Python
```

---

Replace only first occurrence

```python
text = "one one one"

print(text.replace("one","two",1))
```

Output

```
two one one
```

---

### Complexity

```
O(n)
```

---

# split()

Splits a string into a list.

```python
text = "Python Java C++"

print(text.split())
```

Output

```
['Python','Java','C++']
```

---

Custom Separator

```python
text = "A,B,C"

print(text.split(","))
```

Output

```
['A','B','C']
```

---

Maximum Split

```python
text = "a,b,c,d"

print(text.split(",",2))
```

Output

```
['a','b','c,d']
```

---

### Return Type

```
list
```

---

### Complexity

```
O(n)
```

---

# join()

One of the most important interview methods.

Joins an iterable into one string.

```python
words = ["Python","Java","C++"]

print(" ".join(words))
```

Output

```
Python Java C++
```

---

Comma

```python
print(",".join(words))
```

Output

```
Python,Java,C++
```

---

### Why join()?

Never do

```python
result = ""

for word in words:
    result += word
```

Because

```
+=

↓

Creates new string

↓

Every iteration
```

Time Complexity

```
O(n²)
```

Instead

```python
result = "".join(words)
```

Complexity

```
O(n)
```

Huge interview question.

---

# find()

Returns the first index.

```python
text = "Python"

print(text.find("t"))
```

Output

```
2
```

---

Not Found

```python
print(text.find("x"))
```

Output

```
-1
```

---

# index()

Looks similar to `find()`.

```python
print(text.index("t"))
```

Output

```
2
```

But

```python
print(text.index("x"))
```

Output

```
ValueError
```

---

### find() vs index()

| find() | index() |
|---------|----------|
| Returns -1 | Raises Exception |
| Safer | Use when substring must exist |

---

# count()

Counts occurrences.

```python
text = "banana"

print(text.count("a"))
```

Output

```
3
```

Complexity

```
O(n)
```

---

# startswith()

```python
text = "Python"

print(text.startswith("Py"))
```

Output

```
True
```

---

# endswith()

```python
print(text.endswith("on"))
```

Output

```
True
```

---

# isalpha()

Checks whether every character is alphabetic.

```python
print("Python".isalpha())
```

Output

```
True
```

---

# isdigit()

```python
print("123".isdigit())
```

Output

```
True
```

---

# isalnum()

Letters or digits.

```python
print("Python123".isalnum())
```

Output

```
True
```

---

# isspace()

```python
print("   ".isspace())
```

Output

```
True
```

---

# islower()

```python
print("python".islower())
```

Output

```
True
```

---

# isupper()

```python
print("PYTHON".isupper())
```

Output

```
True
```

---

# String Method Summary

| Method | In-place? | Return Type | Complexity |
|---------|-----------|-------------|------------|
| upper() | ❌ | str | O(n) |
| lower() | ❌ | str | O(n) |
| strip() | ❌ | str | O(n) |
| replace() | ❌ | str | O(n) |
| split() | ❌ | list | O(n) |
| join() | ❌ | str | O(n) |
| find() | ❌ | int | O(n) |
| index() | ❌ | int | O(n) |
| count() | ❌ | int | O(n) |
| startswith() | ❌ | bool | O(k) |
| endswith() | ❌ | bool | O(k) |

---

# 💡 Best Practices

✅ Prefer `join()` over repeated `+` inside loops.

✅ Use `find()` if the substring may not exist.

✅ Use `index()` only when you're sure the substring exists.

✅ Remember every string method returns a new string.

---

# ⚠️ Common Mistakes

❌

```python
text.upper()

print(text)
```

Output

```
python
```

Because

`upper()` returns a new string.

Correct

```python
text = text.upper()
```

---

❌

```python
"abc".split("")
```

Raises

```
ValueError
```

The separator cannot be an empty string.

---

# 🧠 DSA Tips

- `split()` is commonly used to parse input.
- `join()` is essential for efficient string construction.
- `find()` is useful when `-1` is easier to handle than exceptions.
- Avoid repeated string concatenation in loops.

---

# 💼 Interview Questions

1. Why are string methods not in-place?
2. Difference between `find()` and `index()`?
3. Why is `join()` faster than repeated `+`?
4. Which method removes whitespace?
5. Difference between `strip()` and `replace()`?
6. Does `upper()` modify the original string?
7. What does `split()` return?
8. Which method is used to combine a list of strings?