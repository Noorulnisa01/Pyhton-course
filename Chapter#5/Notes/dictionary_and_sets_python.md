
# 🐍 Python: Dictionaries and Sets

## 📘 Table of Contents
1. [Dictionaries](#dictionaries)
    - [Definition](#definition)
    - [Why Use Dictionaries?](#why-use-dictionaries)
    - [Creating a Dictionary](#creating-a-dictionary)
    - [Accessing Items](#accessing-items)
    - [Modifying Items](#modifying-items)
    - [Dictionary Methods](#dictionary-methods)
2. [Sets](#sets)
    - [Definition](#definition-1)
    - [Why Use Sets?](#why-use-sets)
    - [Creating a Set](#creating-a-set)
    - [Set Operations](#set-operations)
    - [Set Methods](#set-methods)
3. [Comparison Table](#comparison-table)
4. [Conclusion](#conclusion)

---

## 📕 Dictionaries

### 📌 Definition
A **dictionary** in Python is an unordered, mutable collection of **key-value pairs**. Each key must be unique and immutable.

```python
my_dict = {"name": "Alice", "age": 25, "city": "Lahore"}
```

### ✅ Why Use Dictionaries?
- Fast lookup for data using keys.
- Store related data (like attributes of a person).
- Ideal for data mapping (e.g., user info, config settings).

---

### 🔧 Creating a Dictionary

```python
# Using curly braces
person = {"name": "Noor", "age": 22}

# Using dict() constructor
person = dict(name="Noor", age=22)
```

---

### 🔎 Accessing Items

```python
# Access value by key
print(person["name"])      # Noor

# Use get() method to avoid errors if key doesn't exist
print(person.get("city", "Not Found"))  # Not Found
```

---

### ✏️ Modifying Items

```python
# Change value
person["age"] = 23

# Add new key-value pair
person["city"] = "Karachi"

# Delete key-value pair
del person["city"]

# Clear all items
person.clear()
```

---

### 🛠 Dictionary Methods

| Method              | Description                                  |
|---------------------|----------------------------------------------|
| `.get(key, default)`| Returns value for key; returns default if not found |
| `.keys()`           | Returns a view of all keys                   |
| `.values()`         | Returns a view of all values                 |
| `.items()`          | Returns view of key-value pairs              |
| `.update(dict2)`    | Updates dictionary with another dictionary   |
| `.pop(key)`         | Removes and returns item with key            |
| `.popitem()`        | Removes and returns last inserted item       |
| `.clear()`          | Removes all items                            |
| `.copy()`           | Returns a shallow copy of dictionary         |
| `dict.fromkeys(seq, val)` | Creates dict from keys with same value |

**Example**:
```python
my_dict = {"a": 1, "b": 2}
print(my_dict.keys())        # dict_keys(['a', 'b'])
print(my_dict.items())       # dict_items([('a', 1), ('b', 2)])
```

---

## 📙 Sets

### 📌 Definition
A **set** in Python is an **unordered**, **mutable** collection of **unique elements**.

```python
my_set = {1, 2, 3, 4}
```

### ✅ Why Use Sets?
- Automatically removes duplicates.
- Fast membership testing.
- Useful for mathematical operations (union, intersection, etc.).

---

### 🔧 Creating a Set

```python
# Using curly braces
numbers = {1, 2, 3}

# Using set() constructor
letters = set(["a", "b", "c", "a"])  # Duplicates removed

print(letters)  # {'a', 'b', 'c'}
```

---

### 🔄 Set Operations

| Operation        | Symbol | Example                    | Result                     |
|------------------|--------|----------------------------|----------------------------|
| Union            | `|`    | A \| B                     | All unique elements        |
| Intersection     | `&`    | A & B                      | Common elements            |
| Difference       | `-`    | A - B                      | Elements in A not in B     |
| Symmetric Diff.  | `^`    | A ^ B                      | Elements in A or B, not both |

**Example**:
```python
A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)  # {1, 2, 3, 4, 5}
print(A & B)  # {3}
print(A - B)  # {1, 2}
print(A ^ B)  # {1, 2, 4, 5}
```

---

### 🛠 Set Methods

| Method            | Description                                  |
|-------------------|----------------------------------------------|
| `.add(item)`      | Adds an item                                 |
| `.update(iter)`   | Adds multiple items                          |
| `.remove(item)`   | Removes item (raises error if not found)     |
| `.discard(item)`  | Removes item (no error if not found)         |
| `.pop()`          | Removes and returns an arbitrary item        |
| `.clear()`        | Removes all items                            |
| `.copy()`         | Returns shallow copy                         |
| `.union(set)`     | Returns union of sets                        |
| `.intersection(set)` | Returns common elements                  |
| `.difference(set)`   | Returns difference                      |
| `.issubset(set)`     | Checks if all elements exist in other   |
| `.issuperset(set)`   | Checks if set contains another set      |
| `.isdisjoint(set)`   | Checks if sets have no elements in common |

**Example**:
```python
s = {1, 2}
s.add(3)
s.update([4, 5])
s.discard(2)
print(s)  # {1, 3, 4, 5}
```

---

## 🔄 Comparison Table

| Feature              | Dictionary                   | Set                          |
|----------------------|------------------------------|-------------------------------|
| Structure            | Key-value pairs              | Unique values only            |
| Ordering (Python 3.7+)| Maintains insertion order   | Unordered                     |
| Mutability           | Mutable                      | Mutable                       |
| Duplicates Allowed?  | No duplicate keys            | No duplicates                 |
| Indexed?             | No                           | No                            |
| Use Case             | Mapping data                 | Membership test, uniqueness   |

---

## ✅ Conclusion

- Use **Dictionaries** when you need to associate keys with values.
- Use **Sets** when you need to store **unique** items and perform **mathematical operations**.
- Both are powerful tools in Python for efficient data manipulation and organization.

---

> 🚀 Mastering dictionaries and sets gives you a strong foundation in Python for building fast and clean code!
