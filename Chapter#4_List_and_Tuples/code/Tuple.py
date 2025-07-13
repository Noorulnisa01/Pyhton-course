                # --------------------- Tuple ---------------------

# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Tuples are created using round brackets ().

# Example of a tuple

fruits = ("apple", "banana", "cherry")
print(fruits)
# Accessing items in a tuple
print(fruits[1])  # Output: banana  

# Looping through a tuple
for fruit in fruits:
    print(fruit)
    
    #looping through a tuple means : you can iterate over each item in the tuple

# Checking if an item exists in a tuple
if "apple" in fruits:
    print("Apple is in the tuple")  # Output: Apple is in the tuple

# Tuple length
print(len(fruits))  # Output: 3

# ____________________Difference in Tuple and Lists _________________

# 1. Tuples are immutable, meaning they cannot be changed after creation.
# 2. Tuples are defined using parentheses (), while lists use square brackets [].
# 3. Tuples can be used as keys in dictionaries, while lists cannot.
# 4. Tuples are generally faster than lists for iteration due to their immutability.
# 5. Datatypes of items in tuples can be different, just like lists.