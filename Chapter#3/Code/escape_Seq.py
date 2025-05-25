                             # Escape Sequence
# Escape sequences are special characters in strings that are preceded by a backslash (\).


# \n: New line
# \t: Tab
# \\: Backslash
# \': Single quote
# \": Double quote
# \r: Carriage return
# \b: Backspace


                        # 1. Newline \n
# \n: Newline character, used to create a new line in a string.
# Example:


multiline_string = "Line 1\nLine 2"
print(multiline_string)
# Output:
# Line 1
# Line 2

                        # 2. Tab \t
                        # 3. Backslash \\
# \t : tab character, used to insert a horizontal tab in a string.

tab_string = "Column 1\tColumn 2"
print(tab_string)
# Output:
# Column 1    Column 2

                        # 4. Single quote \'
#\' : single quote character, used to include a single quote in a string without ending it.
# It means if you want to show the quoutation marks in a string, you can dot it by using \' character.

string = " My name is \'taha\' and I love programming."
print(string)
# Output: My name is "taha" and I love programming.


                        # 5. Double quote \"
# \" : double quote character, used to include a double quote in a string without ending it.

string_with_double_quote = "My name is \"taha\" and I love programming."
print(string_with_double_quote)
# Output: My name is "taha" and I love programming.

                        # 6. Carriage return \r
# \r : Carriage return character, used to move the words that are written after the \r to the beginning of the line
# The words replce with first word of string.
carriage_return_string = " World!\rPython"
print(carriage_return_string)
# Output: Python, World!


                        # 7. Backspace \b
# \b : Backspace character, used to remove the character before it.
backspace_string = "Hello \bbWorld"
print(backspace_string)
# Output: HelloWorld

                        # 8. Backslash \\
# \\ : Backslash character, used to include a backslash in a string.

string_with_backslash = "This is a backslash: \\"
print(string_with_backslash)
# Output: This is a backslash: \