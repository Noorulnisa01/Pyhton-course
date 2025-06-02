                        # -------------------- List Methods --------------------

# List methods are functions that can be applied to lists to perform various operations.



# Some of the common list methods include:

# 1. append(): Adds an element to the end of the list.
# 2. insert(): Inserts an element at a specific index in the list.
# 3. remove(): Removes an element from the list.
# 4. 4.pop(): Removes and returns the element at a specific index in the list.
# 5. clear(): Removes all elements from the list.
# 6. index(): Returns the index of the first occurrence of an element in the list.
# 7. count(): Returns the number of times an element appears in the list.
# 8. sort(): Sorts the elements of the list in ascending order.
# 9. reverse(): Reverses the order of the elements in the list.


                  # --------------------- Example of using list methods

# 1. append() method : It is used to add new element at the end of the list.

my_list = [1, "Ali", 2.2, 3]
my_list.append("Hello")
print(my_list) # Output: [1, 'Ali', 2.2, 3, 'Hello']


# 2. insert() method : It is used to add new element at the specific index of the list.
# syntax: list.insert(index, element)

my_list.insert(2, "World") # it means that insert "World" at index 2
print(my_list) # Output: [1, 'Ali', 'World', 2.2, 3, 'Hello']


# 3. remove() method : It is used to remove the first occurrence of the element from the list.
# syntax: list.remove(element)

my_list.remove(2.2) # it means that remove the first occurrence of 2.2 from the list
print(my_list) # Output: [1, 'Ali', 'World', 3, 'Hello']

# 4. pop() method : It is used to remove the element at the specific index from the list and return it.
# syntax: list.pop(index)

my_list.pop(1) # it means that remove the element at index 1 from the list and return it
print(my_list) # Output: [1, 'World', 3, 'Hello']


# 5. clear() method : It is used to remove all the elements from the list.
# syntax: list.clear()

my_list.clear() # it means that remove all the elements from the list
print(my_list) # Output: []

# 6. index() method : It is used to return the index of the first occurrence of the element in the list.
# syntax: list.index(element)

my_list = [1, "Ali", 2.2, 3, "Hello"]
index_of_hello = my_list.index("Hello")  # it means that return the index of "Hello" in the list
print(index_of_hello)  # Output: 4


# 7. count() method : It is used to return the number of occurrences of the element in the list.
# syntax: list.count(element)

my_list = [1, "Ali", 2.2, 3, "Hello", "Hello"]
count_of_hello = my_list.count("Hello")  # it means that return the number of occurrences of "Hello" in the list
print(count_of_hello)  # Output: 2

# 8. sort() method : It is used to sort the elements of the list in ascending order.
# syntax: list.sort()

my_list = [3, 1, 4, 2]
my_list.sort() # it means that sort the elements of the list in ascending order
print(my_list) # Output: [1, 2, 3, 4]

# 9. reverse() method : It is used to reverse the order of the elements in the list.
# syntax: list.reverse()

my_list = [3, 1, 4, 2]
my_list.reverse() # it means that reverse the order of the elements of the list
print(my_list) # Output: [2, 4, 1, 3]

# Note: The sort() and reverse() methods modify the list in place and do not return a new list.
# You can also use the sorted() function to sort a list without modifying the original list.

my_list = [3, 1, 4, 2]
sorted_list = sorted(my_list) # it means that sort the elements of the list in ascending order and return a new list
print(sorted_list) # Output: [1, 2, 3, 4]
print(my_list) # Output: [3, 1, 4, 2]



