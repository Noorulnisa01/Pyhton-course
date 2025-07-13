
# 🐍 Python Basics: Variables, Data Types, Type Casting, Input Function & Operators

---

## 📌 1. Variables in Python

### ✅ What is a Variable?

A variable is a name that refers to a value stored in memory. In Python, you don't need to declare the data type of a variable explicitly.

### ✅ Syntax

```python
variable_name = value
````

### 🧠 Rules for Naming Variables:

* Must begin with a letter or underscore `_`
* Cannot start with a digit
* Case-sensitive (`name` and `Name` are different)
* Cannot use reserved keywords like `if`, `else`, `while`, etc.

### 💡 Examples:

```python
x = 5
name = "Alice"
_pi = 3.14
Age = 20
```

---

## 📌 2. Data Types in Python

### ✅ Built-in Data Types:

| Type       | Description                   | Example           |
| ---------- | ----------------------------- | ----------------- |
| `int`      | Integer numbers               | `x = 10`          |
| `float`    | Floating-point numbers        | `pi = 3.14`       |
| `str`      | String (text)                 | `name = "Ali"`    |
| `bool`     | Boolean values                | `is_valid = True` |
| `list`     | Ordered, mutable collection   | `l = [1,2,3]`     |
| `tuple`    | Ordered, immutable collection | `t = (1,2,3)`     |
| `set`      | Unordered, unique items       | `s = {1,2,3}`     |
| `dict`     | Key-value pairs               | `d = {"a":1}`     |
| `NoneType` | Represents `None` or null     | `x = None`        |

### 🧠 Check Type:

```python
print(type(x))
```

---

## 📌 3. Type Casting (Type Conversion)

### ✅ What is Type Casting?

Changing the data type of a variable to another type.

### ✅ Types:

* `int()` – Converts to integer
* `float()` – Converts to float
* `str()` – Converts to string
* `bool()` – Converts to boolean
* `list()`, `tuple()`, `set()` – For collections

### 💡 Examples:

```python
x = "123"
y = int(x)       # 123 as integer
z = float(y)     # 123.0 as float
s = str(z)       # '123.0' as string
```

### ⚠️ Note:

* You can only cast valid strings to numbers.

```python
int("abc")  # ❌ Error
```

---

## 📌 4. `input()` Function

### ✅ What is `input()`?

It takes user input as a string.

### ✅ Syntax:

```python
variable = input("Enter something: ")
```

### 💡 Example:

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
```

### ⚠️ Tip:

Always cast `input()` to the appropriate type because it returns a string by default.

```python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Sum:", num1 + num2)
```

---

## 📌 5. Operators in Python

### ✅ Arithmetic Operators:

| Operator | Description    | Example  |
| -------- | -------------- | -------- |
| `+`      | Addition       | `a + b`  |
| `-`      | Subtraction    | `a - b`  |
| `*`      | Multiplication | `a * b`  |
| `/`      | Division       | `a / b`  |
| `//`     | Floor Division | `a // b` |
| `%`      | Modulus        | `a % b`  |
| `**`     | Exponent       | `a ** b` |

### ✅ Comparison Operators:

| Operator | Description      |
| -------- | ---------------- |
| `==`     | Equal to         |
| `!=`     | Not equal to     |
| `>`      | Greater than     |
| `<`      | Less than        |
| `>=`     | Greater or equal |
| `<=`     | Less or equal    |

### ✅ Logical Operators:

| Operator | Description | Example            |
| -------- | ----------- | ------------------ |
| `and`    | Logical AND | `a > 5 and a < 10` |
| `or`     | Logical OR  | `a < 5 or b < 10`  |
| `not`    | Logical NOT | `not(a > b)`       |

### ✅ Assignment Operators:

| Operator | Example | Equivalent to |
| -------- | ------- | ------------- |
| `=`      | x = 5   | x = 5         |
| `+=`     | x += 2  | x = x + 2     |
| `-=`     | x -= 3  | x = x - 3     |
| `*=`     | x \*= 4 | x = x \* 4    |
| `/=`     | x /= 5  | x = x / 5     |

### ✅ Membership Operators:

```python
"in"       # Returns True if value is in sequence
"not in"   # Returns True if value is NOT in sequence
```

### ✅ Identity Operators:

```python
is         # True if both refer to same object
is not     # True if both do NOT refer to same object
```

---

## 💡 Tips and Tricks

* 🔹 Use `type()` to debug variable types.
* 🔹 Use `isinstance()` to check type safely.
* 🔹 Chain operations:

```python
x += 5
x *= 2
```

* 🔹 Use `input()` wisely with type casting to avoid runtime errors.
* 🔹 Use `//` for integer division if you don’t want decimals.

---

## 📚 Example Program

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
year = 2025
print(f"Hello {name}, you will be {age + 1} in {year + 1}")
```

---

## 📎 Resources:

* [Official Python Docs](https://docs.python.org/3/)
* [W3Schools Python Tutorial](https://www.w3schools.com/python/)
* [Python Cheatsheet](https://www.pythoncheatsheet.org/)


