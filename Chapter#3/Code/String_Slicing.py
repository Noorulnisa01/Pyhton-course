
#_______________________String slicing___________________________   

# String slicing allows you to extract a portion of a string using indexing.
# It means that if you want to write some characters and words from a string, you can do it by slicing.
# Syntax: string[index_start:index_end]
                # 1. positive slicing
                # 2. negative slicing
                # 3. reverse slicing

                  #__________indexing___________

# indexing means counting the characters in a string starting from 0.
# For example, in the string "Hello", 'H' is at index 0, 'e' is at index 1, and so on.
# indexing starts at 0 (if you start indexing from the left to right.)



#_____________Positive indexing_______________
# (indexing from left to right , indexing stats at 0)


# Example

my_string = "Hello, World!"

positive_string_slicing = my_string[1:4]  # Extracts characters from index 1 to 4

print(positive_string_slicing)  # Output: "ello"



                    ##_____________Negative indexing_______________
# Negative indexing allows you to access characters from the end of the string.
# (indexing from right to left, indexing starts at -1)

# Example of negative indexing
negative_string_slicing = my_string[-5:-2]  # Extracts characters from index -5 to -2
print(negative_string_slicing)  # Output: "Wor"




# Note: you can smiple convert the negative slicing into positive slicing and then slove the question.

# Scenario no. 1:

#if the index_start is missing and only index_end is written e.g. [ :5] ?

# Ans: Missing of index_START means here is 0 e.g [ :5] is same as [0:5]

# Example: 

My_name = "Abdullah"
print(My_name[:5]) # Output: "Abdull"


# Scenario no. 2:   
#if the index_end is missing and only index_start is written e.g. [5:] ?

# Ans: Missing of index_END means here is length of the string 
# e.g the length of string "Abdullah" is 7 e.g [5:] is same as [5:7]

# Example: 

My_name = "Abdullah"
print(My_name[5:]) # Output: "lah"

                # __________________reversing a string using slicing___________________________
# You can reverse a string using slicing by specifying a step of -1.
reversed_string = my_string[::-1]  # Reverses the string

print(reversed_string)  # Output: "!dlroW ,olleH"


# Example of reversing a string
my_string = "Hello, World!"
reversed_string = my_string[::-1]  # Reverses the string
print(reversed_string)  # Output: "!dlroW ,olleH"