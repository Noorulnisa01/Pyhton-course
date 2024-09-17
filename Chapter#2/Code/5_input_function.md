> # ***Input Function in Python***

### ***input()*** function is used to ***take user input.***
> -  ***By default,*** it returns the ***user input*** in form of a ***string.***

## ***input() function syntax :***

```python
input(prompt)

a = input("Enter your 1st subject Marks: ")

b = input("Enter your 2nd subject Marks: ")

print("Total marks obtained = ", a + b)

```


# 💡***Did you Think ?***
> ## 📝 ***Question # 1:*** 
### ***Why + symbol is used in print function for print uers input ?***
```python
a = input("Your Name: ") 

b = input("Your Age: ") 

print(a + b)

```

> ## ***📢 Answer:***
- This **" + "** symbol shows the ***concatenation*** in the output.
- In C++, we use ***" , " symbol*** to print two variable in print function.
> ## ***Concatenation:***

- ***Concatenation*** means to j***oin two or more strings.***
- ***" + " symbol*** is used to join two or more strings because input function returns the ***user input*** in form of a ***string.***
- **Output print the input in one line.**
```python

a = input("Your Name: ") # Noor

b = input("Your Age: ") # 34

print(a + b)


# Output

Noor34
```



### If you want to **print in a new line** then we can use **" \n "**

```python
print(a + " \n " + b)

# Output

Noor
34
```

> ## 📝 ***Question # 2:*** 

### ***How does the input() function handle different data types? ?***


> ## ***📢 Answer:***

### By using ***typecasting*** we can convert any data type to another data type.

- The ***input()*** function always returns the user ***input as a string***, regardless of what the user types.
  
- However, If you need a ***different data type (like an integer or float)***, you have to ***convert it manually by using typecasting.***

```python

a = input("1st number: ") # a = 4

b = input("2nd number: ") # b = 6

print(a + b)

# Output

46 # ab 

# (here, a and b is a string and add two strings means that both strings print in one line )

```
# 🤔 ***Why answer is 46 ?***

## 👩🏻‍💻 ***Answer:*** The result is **46** ***because*** input function always print ***input in form of string*** and **" + "** symbol is used to join two or more strings.


> # ***Typecasting:***
- Input is a ***string*** and convert it into ***integer or float***.
- Type ***" int "*** before the input function.

```python

a = int input("1st number: ") # a = 4

b = int input("2nd number: ") # b = 6

print(a + b)

# Output

10  # a + b 

# (here, a and b is a integer and add two integers means sum of two integers )
```

> ## 📚 ***Key points:***
- Prompt is a ***string*** that will be displayed in the ***Terminal.***
- By default, it returns the ***user input*** in form of a ***string.***

- If any* user wants to ***take input as int or float***, we just need to **typecast it**.

```python
a = input("Enter your 1st subject Marks: ")
b = input("Enter your 2nd subject Marks: ")
print("Total marks obtained = ", a + b)

# typecasting
int(input(prompt))
float(input(prompt))
```