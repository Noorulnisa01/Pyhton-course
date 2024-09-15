> # ***Type Casting*** 

### ***Type Casting*** means to ***convert one data type to another data type.***

> ## ***type() Function:***
- **type()** function is used to ***show the type/class of data*** that stored in a variable.

> ## ***Declare a type() function:***

 ### type(variable_name)

```python
x = 10
y = 20

print(type(x)) 

# class 'int' means class of x value is integer.
.
print(type(y))

 # class 'int' means class of y value is integer.
```
> # ***Type Casting:***

- Type casting is also known as ***Type Conversion.***
- We Can ***convert any data type*** to another data type by using ***"type casting"*** function.

> ## 📝 ***How to convert one data type to another data type?***
1. ***Write the data type*** in which do you want to convert your variable's data.
2. ***Type the variable next*** to the data type you want to convert.***e.g float x = 10.***

```python
x = 10
y = 20.478
z = "noor"

# converting integer to float.
a = float(x) 

# converting integer to string.
b = str(y)

# converting string to integer.
c = int(z)
```