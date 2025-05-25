#______________________Strings___________________________

# string are the most common data type in python and are used to store text data.
# They are immutable (unchangeable) - meaning once created, they cannot be changed.
# Strings can be created using single quotes, double quotes, or triple quotes for multi-line strings.


# Example of a string
name = "John"
print(name)  # Output: John


# Example of a multi-line string
message = """This is a multi-line string.
It can span multiple lines.
"""
print(message)


# Example of string slicing
text = "Hello, World!"
print(text[0:5])  # Output: Hello
# text[index_start:index_end]

# All string operations:

my_string = "Hello, World!"

# Extract "Hello"
substring1 = my_string[0:5]
print(substring1)  # Output: Hello

# Extract "World"
substring2 = my_string[7:12]
print(substring2)  # Output: World

# Extract every other character
substring3 = my_string[::2]
print(substring3)  # Output: Hlo ol!

# Reverse the string
reversed_string = my_string[::-1]
print(reversed_string)  # Output: !dlroW ,olleH

# Slice from a specific index to the end
substring4 = my_string[7:]
print(substring4) # Output: World!

# Slice from the beginning to a specific index
substring5 = my_string[:5]
print(substring5) # Output: Hello