                   # String function

       # 1. len() function
       # 2. lower() function
       # 3. upper() function
       # 4. title() function
       # 5. capitalize() function
       # 6. endswith() function
       # 7. startswith() function
       # 8. find() function
       # 9. replace() function
       # 10. split() function
       # 11. join() function

name = "Abdullah ahmad"
nick_name = "abdu"

# 1. len() function:
# The len() function returns the length of a string.

print(len(name))  # Output: 14 (length of the string)

# 2. lower() function:
# The lower() function converts all characters in a string to lowercase.

print(name.lower())  # Output: "abdullah ahmad"

# 3. upper() function:
# The upper() function converts all characters in a string to uppercase.

print(name.upper())  # Output: "ABDULLAH AHMAD"

# 4. title() function:
# The title() function converts the first character of each word to uppercase.

print(name.title())  # Output: "Abdullah Ahmad"

# 5. capitalize() function:
# The capitalize() function converts the first character of a string to uppercase.

print(name.capitalize())  # Output: "Abdullah ahmad"

# 6. endwith() function:
# The endswith() function checks if a string ends with a specified suffix.

print(name.endswith("ahmad"))  # Output: True

# 7. startswith() function:

# The startswith() function checks if a string starts with a specified prefix.

print(name.startswith("Abdullah"))  # Output: True

# 8. find() function:

# The find() function returns the index of the first occurrence of a that word in a string.
# find the string that start with this word and return the index of that string.

print(name.find("ahmad"))  # Output: 8 (index of the first occurrence of "ahmad")

# 9. replace() function:
# The replace() function replaces all occurrences of a specified substring with another substring.
# It means that if you want to replace a word with another word in a string, you can do it by using the replace() function.

print(name.replace("ahmad", "khan"))  # Output: "Abdullah khan"

# 10. split() function:
# The split() function splits a string into a list of substrings based on a specified separator.
# It means that if you want to split a string into a list of words, you can do it by using the split() function.

print(name.split(" "))  # Output: ["Abdullah", "ahmad"]
 
# 11. join() function:
# The join() function joins a list of strings into a single string with a specified separator.

print(" ".join(["Abdullah", "ahmad"]))  # Output: "Abdullah ahmad"