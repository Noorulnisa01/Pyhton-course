
# 🐍 Python: Strings

## 📘 Table of Contents
1. [What is a String?](#what-is-a-string)
2. [Creating Strings](#creating-strings)
3. [Accessing Characters](#accessing-characters)
4. [String Slicing](#string-slicing)
5. [String Methods](#string-methods)
6. [String Formatting](#string-formatting)
7. [String Operations](#string-operations)
8. [Useful String Tricks](#useful-string-tricks)
9. [Escape Characters](#escape-characters)
10. [Conclusion](#conclusion)

---

## 📕 What is a String?

A **string** in Python is a sequence of **Unicode characters** enclosed in single, double, or triple quotes.

```python
s = "Hello, World!"
```

---

## 🧱 Creating Strings

```python
# Single and double quotes
a = 'Python'
b = "Programming"

# Triple quotes for multi-line strings
c = '''This is
a multi-line
string.'''
```

---

## 🔍 Accessing Characters

```python
text = "Python"

# Indexing
print(text[0])   # P
print(text[-1])  # n

# Looping through a string
for char in text:
    print(char)
```

---

## ✂️ String Slicing

```python
s = "Programming"

print(s[0:6])   # Progra
print(s[:6])    # Progra
print(s[3:])    # gramming
print(s[-3:])   # ing
```

---

## 🛠 String Methods

| Method               | Description                                 |
|----------------------|---------------------------------------------|
| `.lower()`           | Converts to lowercase                       |
| `.upper()`           | Converts to uppercase                       |
| `.capitalize()`      | Capitalizes first letter                    |
| `.title()`           | Capitalizes first letter of each word       |
| `.strip()`           | Removes whitespace from both ends           |
| `.lstrip()`          | Removes whitespace from the left            |
| `.rstrip()`          | Removes whitespace from the right           |
| `.replace(old, new)` | Replaces a substring                        |
| `.split(sep)`        | Splits string into a list                   |
| `.join(iterable)`    | Joins iterable into a string                |
| `.find(sub)`         | Returns first index of substring            |
| `.rfind(sub)`        | Returns last index of substring             |
| `.count(sub)`        | Counts occurrences of substring             |
| `.startswith(prefix)`| Checks if string starts with prefix         |
| `.endswith(suffix)`  | Checks if string ends with suffix           |
| `.isalpha()`         | Checks if all chars are letters             |
| `.isdigit()`         | Checks if all chars are digits              |
| `.isalnum()`         | Checks if all chars are alphanumeric        |

**Example:**
```python
s = " Hello Python "
print(s.strip().upper())  # HELLO PYTHON
```

---

## ✨ String Formatting

```python
name = "Alice"
age = 25

# f-string
print(f"My name is {name} and I am {age} years old.")

# format() method
print("My name is {} and I am {} years old.".format(name, age))

# Percentage formatting
print("My name is %s and I am %d years old." % (name, age))
```

---

## ➕ String Operations

```python
# Concatenation
s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)  # Hello World

# Repetition
print("Ha" * 3)  # HaHaHa

# Membership
print("Py" in "Python")  # True
print("Java" not in "Python")  # True

# Length
print(len("Python"))  # 6
```

---

## 💡 Useful String Tricks

```python
# Reverse a string
s = "hello"
print(s[::-1])  # olleh

# Palindrome check
s = "madam"
print(s == s[::-1])  # True

# Remove duplicates
print("".join(set("banana")))  # bna

# Count vowels
print(sum(1 for ch in "hello" if ch in "aeiou"))  # 2

# Swap case
print("HeLLo".swapcase())  # hEllO
```

---

## 🔁 Escape Characters

| Escape Code | Description         |
|-------------|---------------------|
| `\n`       | New line            |
| `\t`       | Tab                 |
| `\'`       | Single quote        |
| `\"`       | Double quote        |
| `\\`      | Backslash           |

```python
print("Hello\nWorld")  # Hello
                        # World
```

---

## ✅ Conclusion

- Strings are the core of text processing in Python.
- They are **immutable**, meaning any modification creates a new string.
- Using built-in methods and tricks can make string handling powerful and concise.

---

> 🚀 Strings are the foundation of data and communication in Python programming!
