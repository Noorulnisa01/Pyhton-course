                       #---------------------  List  -------------------------

# List is a collection of items that can be of different data types.
# Lists are mutable, meaning you can change their content without changing their identity.
# Lists are created using square brackets [].

# Example of a list 
my_list = [1, 2, 3, 4, 5]
# Accessing elements in a list
print(my_list[0])  # Output: 1
print(my_list[2])  # Output: 3

                    # ------------------ Slicing a list ------------------

# Slicing a list allows you to extract a portion of a list.
# It means that if you want to write some characters and words from a list, you can do it by slicing.


# Slicing syntax: list[start:end] where start is inclusive and end is exclusive.
print(my_list[1:4])  # Output: [2, 3, 4]    



                    # ------------------ Difference B/w List and String ------------------

#        1. Lists are mutable, meaning you can change their content.
#           Strings are immutable, meaning you cannot change their content.

#        2. Lists can contain items of different data types.
#           Strings can only contain characters.

#        3. You can modify a list (add, remove, or change elements).
#           You cannot modify a string (you can only create a new string).

#       4. In Lists, you can use methods like append(), remove(), and pop() to modify the list.
#          In Strings, you can use methods like upper(), lower(), and replace() to create new strings.

                    
                    

# Modifying elements in a list
my_list[0] = 10
print(my_list)  # Output: [10, 2, 3, 4, 5]

# Adding elements to a list
my_list.append(6)
print(my_list)  # Output: [10, 2, 3, 4, 5, 6]

# Removing elements from a list
my_list.remove(2)
print(my_list)  # Output: [10, 3, 4, 5, 6]