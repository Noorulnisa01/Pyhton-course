
# 🐍 Python: Tuples and Lists

## 📘 Table of Contents
1. [Lists](#lists)
    - [Definition](#definition)
    - [Why Use Lists?](#why-use-lists)
    - [Creating a List](#creating-a-list)
    - [Accessing List Items](#accessing-list-items)
    - [Modifying List Items](#modifying-list-items)
    - [List Methods](#list-methods)
2. [Tuples](#tuples)
    - [Definition](#definition-1)
    - [Why Use Tuples?](#why-use-tuples)
    - [Creating a Tuple](#creating-a-tuple)
    - [Accessing Tuple Items](#accessing-tuple-items)
    - [Tuple Methods](#tuple-methods)
3. [Comparison Table](#comparison-table)
4. [Conclusion](#conclusion)

---

## 📕 Lists

### 📌 Definition
A **list** in Python is an **ordered**, **mutable** collection of elements. It can contain items of different data types.

```python
my_list = [1, "hello", 3.14, True]
```

### ✅ Why Use Lists?
- Store multiple values in a single variable.
- Items can be modified, added, or removed.
- Supports indexing and slicing.

---

### 🔧 Creating a List

```python
# Using square brackets
fruits = ["apple", "banana", "cherry"]

# Using list() constructor
numbers = list([1, 2, 3, 4])
```

---

### 🔎 Accessing List Items

```python
# Indexing
print(fruits[1])  # banana

# Negative indexing
print(fruits[-1])  # cherry

# Slicing
print(fruits[0:2])  # ['apple', 'banana']
```

---

### ✏️ Modifying List Items

```python
# Change value
fruits[0] = "orange"

# Append item
fruits.append("mango")

# Insert item at specific index
fruits.insert(1, "grape")

# Remove item
fruits.remove("banana")

# Pop item by index
fruits.pop(1)

# Delete item by index
del fruits[0]

# Clear all items
fruits.clear()
```

---

### 🛠 List Methods

| Method              | Description                              |
|---------------------|------------------------------------------|
| `.append(x)`        | Adds an item to the end                  |
| `.insert(i, x)`     | Inserts item at given index              |
| `.remove(x)`        | Removes first item with value x          |
| `.pop(i)`           | Removes item at index i                  |
| `.clear()`          | Removes all items                        |
| `.index(x)`         | Returns index of first item with value x |
| `.count(x)`         | Returns number of occurrences of x       |
| `.sort()`           | Sorts list in place                      |
| `.reverse()`        | Reverses the list                        |
| `.copy()`           | Returns a shallow copy                   |
| `.extend(iterable)` | Adds elements from another iterable      |

---

## 📙 Tuples

### 📌 Definition
A **tuple** in Python is an **ordered**, **immutable** collection of elements. Like lists, it can contain mixed data types.

```python
my_tuple = (1, "hello", 3.14)
```

### ✅ Why Use Tuples?
- Protect data from accidental changes.
- More memory-efficient than lists.
- Can be used as dictionary keys.

---

### 🔧 Creating a Tuple

```python
# With parentheses
coordinates = (10, 20)

# Without parentheses (not recommended)
colors = "red", "green", "blue"

# Single item tuple (with comma)
single = ("only",)
```

---

### 🔎 Accessing Tuple Items

```python
# Indexing
print(coordinates[0])  # 10

# Slicing
print(colors[1:])  # ('green', 'blue')
```

---

### 🛠 Tuple Methods

| Method         | Description                                 |
|----------------|---------------------------------------------|
| `.count(x)`    | Returns number of occurrences of x          |
| `.index(x)`    | Returns index of first occurrence of x      |

---

## 🔄 Comparison Table

| Feature              | List                           | Tuple                         |
|----------------------|--------------------------------|-------------------------------|
| Ordered              | Yes                            | Yes                           |
| Mutable              | Yes                            | No                            |
| Allow duplicates     | Yes                            | Yes                           |
| Syntax               | `[1, 2, 3]`                    | `(1, 2, 3)`                   |
| Use case             | General-purpose collection     | Fixed data, keys, performance |
| Memory efficiency    | Less efficient                 | More efficient                |
| Methods              | Many                           | Few                           |

---

## ✅ Conclusion

- Use **Lists** when you need a **dynamic**, changeable collection.
- Use **Tuples** when your data should **not change** and you want faster performance.
- Understanding both helps you choose the right tool for your Python programs.

---

> 🚀 Lists and Tuples are fundamental to mastering Python data structures!
