

## Variables
 
>A variable is a symbolic name that is used store and represent data values. 
>It is essentially a label or identifier for a memory location where a value is stored.

```
# Variable assignment
age = 

# Variable reference
print("My age is: ",age)
print ("I am " + str(age) + " years old")
print (f"I am {age} years old")
print("I am {} years old".format(age))
```
### Identifiers

Identifier is a name given to entities like variables, functions, classes, modules, etc. It helps to uniquely identify these entities in the program.

### Rules of identifiers
1. It must start with a letter (a-z, A-Z) or an underscore (_).
2. The remaining characters can be letters, underscores, or digits (0-9).
3. Python is case-sensitive, so variables and Variables are different identifiers.
4. Reserved keywords are not allowed as identifiers.

### Conventions for Naming Identifiers
1. Use descriptive names to make the code more readable.
2. Avoid using names that are too short or too cryptic.
3. Use underscores to separate words in a multo-word identifier (snake_case). For example, my_variable_name.
4. For constants, use all capital letters with underscores separating words (UPPER_CASE). For example, PI, MAX_VALUE.
 
### Numbers

Python provides various ways to work with numbers,
including integers, floating-point numbers, complex numbers, and more.

#### Basic Arithmetic Operations

```
# Addition
sum_result = 5 + 3
print(sum_result)  # 8

# Subtraction
difference = 7 - 4
print(difference)  # 3

# Multiplication
product = 2 * 6
print(product)     # 12

# Division
quotient = 10 / 2
print(quotient)    # 5.0 (even if the result is a whole number, division returns a float)
```

#### Exponentiation

```
# Exponentiation
power_result = 2 ** 3
print(power_result)  # 8
```

##### Working with Floats

```
# Floating-point numbers
float_num = 3.14

# Rounding
rounded_num = round(float_num, 2)
print(rounded_num)  # 3.14

# Conversion from int to float
int_to_float = float(5)
print(int_to_float)  # 5.0
```

### Input Function

input() function is used to take input from the user during the execution of a program. The input() function reads a line of text from the user as a "string" and returns that "string". It allows the user to provide input interactively.

- Getting input from the user
```
user_input = input("Enter something: ") # returns "string"
print("You entered:", user_input)
```
- Get user input as an integer
```
user_number = int(input("How old are you: "))
```
- Perform some operation with the input
```
result = user_number * 2
print("Twice the entered number:", result)
```
### Assignment Operators

#### Assignment (=)

- The basic assignment operator assigns the value on the right side to the variable on the left side.

```
    x = 10  # Assigns the value 10 to the variable x
```
#### Addition Assignment (+=)

- Adds the value on the right to the current value of the variable on the left and assigns the result to the variable.

```
y = 20
y -= 3  # Equivalent to y = y - 3
```

#### Subtraction Assignment (-=)

- Subtracts the value on the right from the current value of the variable on the left and assigns the result to the variable.

```
y = 20
y -= 3  # Equivalent to y = y - 3
```
#### Multiplication Assignment (*=)

- Multiplies the current value of the variable on the left by the value on the right and assigns the result to the variable.

```
z = 5
z *= 2  # Equivalent to z = z * 2
```
#### Division Assignment (/=)

- Divides the current value of the variable on the left by the value on the right and assigns the result to the variable.

```
a = 8
a /= 4  # Equivalent to a = a / 4
```

Floor Division Assignment (//=)

- Performs floor division on the current value of the variable on the left by the value on the right and assigns the result to the variable.

```
b = 17
b //= 3  # Equivalent to b = b // 3
```
#### Exponentiation Assignment (**=)

- Performs floor division on the current value of the variable on the left by the value on the right and assigns the result to the variable.

```
c = 2
c **= 3  # Equivalent to c = c ** 3
```

#### Modulus Assignment (%=)

- Computes the modulus of the current value of the variable on the left divided by the value on the right and assigns the result to the variable.

```
d = 10
d %= 3  # Equivalent to d = d % 3
```
### Strings

- A string is a sequence of characters, and it is one of the fundamental data types used to represent textual data.
```
# Using single quotes
single_quoted_string = 'Hello, World!'

# Using double quotes
double_quoted_string = "Python Programming"

# Multiline string using triple quotes
multiline_string = '''This is a
multiline
string.'''
```
- Concatenation
```
str1 = "Hello"
str2 = "World"
concatenated_string = str1 + ", " + str2
print(concatenated_string)  # Hello, World
```
- String Length
```
string = "Python"
length = len(string)
print(length)  # 6

- String Formatting

```

```
name = "HuXn"
age = 20
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)
```
- Escape Characters

```
escaped_string = "This is a line.\nThis is a new line."
print(escaped_string)

```
### Booleans

- A boolean is a data type that represents one of two values: True or False.
```
x = True
y = False
```
### Type Casting
- Type casting refers to the process of converting one data type into another. Python provides several built-in functions for type casting, allowing you to convert variables from one type to another

- int() | Converts a value to an integer.

```
float_num = 3.14
int_num = int(float_num)
print(int_num)  # 3
```
- float() | Converts a value to a floating-point number.
```
int_num = 5
float_num = float(int_num)
print(float_num)  # 5.0
```
- str() | Converts a value to a string.

```
num = 42
str_num = str(num)
print(str_num)  # '42'
```
- bool() | Converts a value to a boolean
```
num = 0
bool_value = bool(num)
print(bool_value)  # False
```
#### String Methods
Strings in Python come with a variety of built-in methods that allow you to manipulate and work with them.

- str.upper() and str.lower()
- Converts all characters in a string to uppercase or lowercase.
```
text = "Hello, World!"
upper_text = text.upper()
lower_text = text.lower()
print(upper_text)  # HELLO, WORLD!
print(lower_text)  # hello, world!
```
- str.capitalize() and str.title()

capitalize() capitalizes the first letter of a string.
title() capitalizes the first letter of each word in a string.

```
phrase = "python programming is fun"
cap_phrase = phrase.capitalize()
title_phrase = phrase.title()
print(cap_phrase)   # Python programming is fun
print(title_phrase) # Python Programming Is Fun
```
> str.strip(), str.lstrip(), and str.rstrip()
> strip() removes leading and trailing whitespace.
> lstrip() removes leading whitespace.
> rstrip() removes trailing whitespace.

```
sentence = "   Python is fun!   "
stripped_sentence = sentence.strip()
print(stripped_sentence)  # Python is fun!
```
- str.startswith(prefix) and str.endswith(suffix)
- Checks if a string starts or ends with a specified prefix or suffix.

```
filename = "example.txt"
starts_with = filename.startswith("example")
ends_with = filename.endswith(".txt")
print(starts_with)  # True
print(ends_with)    # True
```
- str.replace(old, new)
- Replaces occurrences of a substring with another substring.
```
sentence = "I like programming in Java."
new_sentence = sentence.replace("Java", "Python")
print(new_sentence)  # I like programming in Python.
```
- str.find(substring) and str.index(substring)
find() returns the lowest index of the first occurrence of a substring.
index() also returns the index of the first occurrence but raises an error if the substring is not found.

```
phrase = "Python is powerful and Python is easy to learn."
index1 = phrase.find("Python")
index2 = phrase.index("Python")
print(index1)  # 0
print(index2)  # 0
```
- str.split(separator)
- Splits a string into a list of substrings based on a specified separator.
```
sentence = "Python is a powerful programming language"
words = sentence.split(" ")
print(words) # ['Python', 'is', 'a', 'powerful', 'programming', 'language']
```
- str.join(iterable)
Concatenates elements of an iterable (e.g., a list) into a string using the original string as a separator.

```
words = ['Python', 'is', 'awesome']
sentence = ' '.join(words)
print(sentence)  # Python is awesome
```
- str.count(substring)
Returns the number of occurrences of a substring in the string.
```
sentence = "Python is easy. Python is fun. Python is powerful."
count_python = sentence.count("Python")
print(count_python)  # 3
```

#### Comparison Operators
Comparison operators are used to compare two values, expressions, or variables. These operators return a boolean value (True or False) based on the comparison result.

- Equality (==)
```
# Checks if the values on both sides are equal.
a = 5
b = 10
result = (a == b)  # Result is False
```
- Inequality (!=)
```
# Checks if the values on both sides are not equal.
a = 5
b = 10
result = (a != b)  # Result is True
```
- Greater Than (>)
```
# Checks if the value on the left is greater than the value on the right.
a = 5
b = 10
result = (a > b)  # Result is False
```
- Less Than (<)
```
# Checks if the value on the left is less than the value on the right.
a = 5
b = 10
result = (a < b)  # Result is True
```
- Greater Than or Equal To (>=)
```
# Checks if the value on the left is greater than or equal to the value on the right.
a = 5
b = 5
result = (a >= b)  # Result is True
```
- Less Than or Equal To (<=)
```
# Checks if the value on the left is less than or equal to the value on the right.
a = 5
b = 10
result = (a <= b)  # Result is True
```
### Equality Operators

Equality operators are used to compare two values for equality. They help determine whether the values on both sides are equal or not, and they return a boolean result (True or False).

- Equality (==)
```
# Checks if the values on both sides are equal.
a = 5
b = 5
result = (a == b)  # True
```
- Inequality (!=)
```
# Checks if the values on both sides are not equal.
a = 5
b = 10
result = (a != b)  # True
```
### Logical Operators
Logical operators are used to perform logical operations on boolean values. These operators allow you to combine or modify boolean values and make more complex decisions in your code.

- Logical AND (and)
The and operator returns True if both conditions on its left and right are True. Otherwise, it returns False.

```
x = True
y = False
result = x and y  # Result is False
```

- Logical OR (or)
The or operator returns True if at least one of the conditions on its left or right is True. If both conditions are False, it returns False.

```
x = True
y = False
result = x or y  # Result is True
```
- Logical NOT (not)
The not operator negates the boolean value. If the condition is True, it returns False. If the condition is False, it returns True.

```
x = True
result = not x  # Result is False
```
### Conditional Statements
Conditional statements are used to control the flow of a program based on certain conditions. They allow you to execute different blocks of code depending on whether a specified condition evaluates to True or False

- if Statement
- The if statement is used to execute a block of code only if a specified condition is True
```
x = 10

if x > 5:
    print("x is greater than 5")
```
- if-else Statement
- The if-else statement allows you to specify two blocks of code: one to be executed if the condition is True, and another if the condition is False.

```
x = 3

if x % 2 == 0:
    print("x is even")
else:
    print("x is odd")
```
- if-elif-else Statement
- The if-elif-else statement allows you to check multiple conditions sequentially. It executes the block of code associated with the first condition that is True.
```
x = 0

if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")
```

### Loops?

Loops allow us to repeatedly execute a block of code as long as a certain condition is met or iterate over a sequence of elements. Python supports two main types of loops: for loops and while loops.

#### for loop
A for loop is used to iterate over a sequence (such as a list, tuple, string, or other iterable objects) and execute a block of code for each element in the sequence.

#### range
range is a built-in function that generates a sequence of numbers within a specified range. It is commonly used with for loops to iterate over a sequence of numbers.

```
for i in range(5):
    print(i)
```
#### range(start, stop)
```
for i in range(2, 8):
    print(i)
```

#### range(start, stop, step)

range(1, 10, 2): This creates a sequence of numbers starting from 1 up to (but not including) 10, with a step of 2. So, the sequence generated is [1, 3, 5, 7, 9]

```
for i in range(1, 10, 2):
    print(i)
```

### while loop
A while loop is a control flow statement that allows a block of code to be executed repeatedly as long as a specified condition is true.

```
count = 1

while count <= 5:
    print(count)
    count += 1
```