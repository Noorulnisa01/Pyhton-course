# Operators:

# Operators are symbols that perform operations on variables and values.


#    Types of Operators:
        # 1. Arithmetic Operators
        # 2. Assignment Operators
        # 3. Comparison Operators
        # 4. Logical Operators
        # 5. Identity Operators
        

# 1. Arithmetic Operators:

#      Arithmetic operators are used to perform mathematical operations.
# For example: +, -, *, /, %, **, // a = 30;
a = 10;
b = 20;

print(a+b) # Addition
print(a-b) # Subtraction
print(a*b) # Multiplication
print(a/b) # Division
print(a%b) # Modulus
print(a**b) # Exponent


# Floor Division
print(a//b) # Floor Division (returns only integer part)
# Example:

a = 10
b = 3

result = a // b
print(result)  # Output: 3

# In this example, 10 // 3 equals 3, not 3.33, because // performs floor division

# 2. Assignment Operators:

#      Assignment operators are used to assign values to variables.
# For example: =, +=, -=, *=, /=, %=, != etc.

# Example:
a = 10      # Assign value 10 to variable a
print(a)

a += 5      # increment: Add 5 to variable a and assign the result to variable a
print(a)

a -= 5      # decrement: Subtract 5 from variable a and assign the result to variable a
print(a)

a *= 5      # multiplication: Multiply variable a by 5 and assign the result to variable a
print(a)

a /= 5      # division: Divide variable a by 5 and assign the result to variable a
print(a)

a %= 5      # modulus: Find the remainder of variable a divided by 5 and assign the result to variable a
print(a)



# 3. Comparison Operators:  

        # Comparison operators are used to compare two values.
# For example: ==, !=, >, <, >=, <= etc.

# Example:
a == 10     # equal to
print(a)

a != 10     # not equal to
print(a)

a > 10      # greater than
print(a)

a < 10      # less than
print(a)

a >= 10     # greater than or equal to
print(a)

a <= 10     # less than or equal to
print(a)


# 4. Logical Operators:

        # Logical operators are used to combine conditional statements.
# For example: and, or, not etc.

# Example:
a and b    # " and " means "both conditions should be true"
print(a)

a or b     # " or " means "at least one of the conditions should be true"
print(a)

not a      # " not " means "reverse the result, returns false if the result is true"
print(a)