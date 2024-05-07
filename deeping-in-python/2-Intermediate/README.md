# Lists?

### A list is a data structure that can store a collection of items. It is one of the built-in data types and is commonly used to hold an ordered sequence of elements. Lists can contain elements of different data types, including numbers, strings, and even other lists.

## Key features of lists

#### 👉 Lists maintain the order of elements as they are inserted, allowing you to access elements by their index.

#### 👉 You can modify the contents of a list by adding or removing elements.

#### 👉 Lists can grow or shrink in size as needed. You can add or remove elements without specifying the size beforehand.

## Creating Lists

```py
# Creating a list of numbers
numbers = [1, 2, 3, 4, 5]

# Creating a list of strings
fruits = ["apple", "orange", "banana", "grape"]

# Creating a mixed-type list
mixed_list = [1, "hello", 3.14, True]

# Accessing elements of a list
print(numbers[0])   # 1
print(fruits[2])    # banana
print(mixed_list[1])  # hello
```
# Accessing Items
#### List are zero index based
```
#py
my_list = ["apple", "banana", "orange"]
# Accessing items from the list using indexing
print(my_list[0])  # Output: apple
print(my_list[1])  # Output: banana

# Negative indexing can be used to access items from the end of the list
print(my_list[-1])  # Output: orange
print(my_list[-2])  # Output: banana

```
# Using Slices

### slicing is a wat to extract a portion of a list (or any iterable) by specifying a range of indices. The basic syntax for slicing is star:stop:step


#### 👉 start: is the index of the first element you want to include (inclusive).

#### 👉 stop is the index of the first element you want to exclude (exclusive).

#### 👉 step is the number of indices between elements (defaults to 1 if not specified).

```py
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

subset = my_list[2:6]  # Gets elements at index 2, 3, 4, 5
print(subset)  # [2, 3, 4, 5]

# Omitting start and stop indices
subset = my_list[:5]  # Gets elements at index 0, 1, 2, 3, 4
print(subset)  # [0, 1, 2, 3, 4]

subset = my_list[5:]  # Gets elements at index 5, 6, 7, 8, 9
print(subset)  # [5, 6, 7, 8, 9]

# Using negative indices
subset = my_list[-3:]  # Gets the last 3 elements
print(subset)  # [7, 8, 9]

# Using step
subset = my_list[1:9:2]  # Gets elements at index 1, 3, 5, 7
print(subset)  # [1, 3, 5, 7]
```

# Updating Items

#### Lists in Python are mutable, meaning you can modify their elements.

#### If you want to update any item in list, First you'll have to select the item using [index] and then change the value inside that.

```py
my_list = [1, 2, 3, 4, 5]

# Update the item at index 2
my_list[2] = 10

print(my_list)
```
# Removing / Deleting Items

#### We can delete an item from a list using the del statement or the remove() method

## Using del

```py
my_list = [1, 2, 3, 4, 5]

# Deleting the item at index 2
del my_list[2]
print(my_list)
```

## Using remove() method

```py
my_list = [1, 2, 3, 4, 5]

# Removing the value 3 from the list
my_list.remove(3)
print(my_list)
```

# Matrix 2D List

#### A list is a versatile data structure that can store multiple elements. Lists can be one-dimensional (1D), two-dimensional (2D), or even higher-dimensional.

## 1D List

#### A one-dimensional list is a simple list that contains elements in a linear sequence.

```py
my_list = [1, 2, 3, 4, 5]
```

## 2D List

#### A two-dimensional list is essentially a list of lists. Each element in the outer list is itself a list.

```py
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

## 3D List

#### A three-dimensional list is a list of lists of lists. It can be thought of as a cube of elements, where each element is a list.

```py
cube = [
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ],
    [
        [10, 11, 12],
        [13, 14, 15],
        [16, 17, 18]
    ],
    [
        [19, 20, 21],
        [22, 23, 24],
        [25, 26, 27]
    ]
]
```

# Lists Built-In Methods

## append(x)

#### Adds element at the end of the list.

```py
my_list = [1, 2, 3]
my_list.append(4)
# Result: [1, 2, 3, 4]
```

## extend(iterable)

#### Extends the list by appending elements from the iterable.

```py
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
# Result: [1, 2, 3, 4, 5, 6]
```

## insert(i, x)

#### Inserts element x at the specified position i.

```py
my_list = [1, 2, 3]
my_list.insert(1, 4)
# Result: [1, 4, 2, 3]
```

## remove(x)

#### Removes the first occurrence of element x.

```py
my_list = [1, 2, 3, 2]
my_list.remove(2)
# Result: [1, 3, 2]
```

## pop([i])

#### Removes and returns the element at the specified position i. If no index is provided, it removes and returns the last element.

```py
my_list = [1, 2, 3]
popped_element = my_list.pop(1)
# Result: popped_element=2, my_list=[1, 3]
```

## count(x)

#### Returns the number of occurrences of element x in the list.

```py
my_list = [1, 2, 3, 2]
count_of_2 = my_list.count(2)
# Result: count_of_2=2
```

## sort(key=None, reverse=False)

#### Sorts the elements of the list in ascending order. The key and reverse parameters are optional.

```py
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
my_list.sort()
# Result: [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]
```

## reverse()

#### Reverses the elements of the list in place.

```py
my_list = [1, 2, 3]
my_list.reverse()
# Result: [3, 2, 1]
```

## copy()

#### Returns a shallow copy of the list.

```py
original_list = [1, 2, 3]
copied_list = original_list.copy()
# Result: copied_list=[1, 2, 3]
```

# In Operator

### The in operator is used to check if a specified value is present in a sequence, such as a string, list, tuple, or dictionary. The result is a boolean value (True or False). The in operator is often used in conditional statements and loops to test membership within a collection.

## In Strings

```py
text = "Hello, World!"
result = 'o' in text
print(result)  # Output: True
```

## In Lists

```py
numbers = [1, 2, 3, 4, 5]
result = 3 in numbers
print(result)  # Output: True
```

## In Tuples

```py
fruits = ('apple', 'banana', 'cherry')
result = 'banana' in fruits
print(result)  # Output: True
```

## In Dictionaries (Checking Keys)

```py
person = {'name': 'John', 'age': 30, 'city': 'New York'}
result = 'age' in person
print(result)  # Output: True

```

## In Sets

```py
colors = {'red', 'green', 'blue'}
result = 'yellow' in colors
print(result)  # Output: False
```

## In Substrings

```py
sentence = "Python is powerful"
result = "power" in sentence
print(result)  # Output: True
```

# List Unpacking

### List unpacking is a feature in Python that allows you to split the elements of a list into individual variables. It is a concise and convenient way to extract values from a list and assign them to multiple variables in a single line.

## Basic Unpacking

```py
my_list = [1, 2, 3]

# Unpacking the list into variables a, b, c
a, b, c = my_list

print(a)  # 1
print(b)  # 2
print(c)  # 3
```

## \*rest

```py
my_list = [1, 2, 3, 4, 5]

# Unpacking the first two elements, and collecting the rest into a variable
first, second, *rest = my_list

print(first) # 1
print(second) # 2
print(rest) # [3, 4, 5]
```
# In Operator

### The in operator is used to check if a specified value is present in a sequence, such as a string, list, tuple, or dictionary. The result is a boolean value (True or False). The in operator is often used in conditional statements and loops to test membership within a collection.

## In Strings

```py
text = "Hello, World!"
result = 'o' in text
print(result)  # Output: True
```

## In Lists

```py
numbers = [1, 2, 3, 4, 5]
result = 3 in numbers
print(result)  # Output: True
```

## In Tuples

```py
fruits = ('apple', 'banana', 'cherry')
result = 'banana' in fruits
print(result)  # Output: True
```

## In Dictionaries (Checking Keys)

```py
person = {'name': 'John', 'age': 30, 'city': 'New York'}
result = 'age' in person
print(result)  # Output: True

```

## In Sets

```py
colors = {'red', 'green', 'blue'}
result = 'yellow' in colors
print(result)  # Output: False
```

## In Substrings

```py
sentence = "Python is powerful"
result = "power" in sentence
print(result)  # Output: True
```

# List Unpacking

### List unpacking is a feature in Python that allows you to split the elements of a list into individual variables. It is a concise and convenient way to extract values from a list and assign them to multiple variables in a single line.

## Basic Unpacking

```py
my_list = [1, 2, 3]

# Unpacking the list into variables a, b, c
a, b, c = my_list

print(a)  # 1
print(b)  # 2
print(c)  # 3
```

## \*rest

```py
my_list = [1, 2, 3, 4, 5]

# Unpacking the first two elements, and collecting the rest into a variable
first, second, *rest = my_list

print(first) # 1
print(second) # 2
print(rest) # [3, 4, 5]
```

# Tuples?

### Tuple is an ordered, immutable collection of elements. This means that once you create a tuple, you cannot modify its contents - you can't add, remove, or change elements in a tuple after it has been created. Tuples are defined by enclosing a comma-separated sequence of values in parentheses ()

### Basic Syntax

```py
my_tuple = (1, 2, 3, 'hello', 3.14)
print(my_tuple[0])  # Output: 1
print(my_tuple[3])  # Output: 'hello'
```

### Error

```py
my_tuple = (1, 2, 3, 'hello', 3.14)
# This will raise an error since tuples are immutable
# my_tuple[0] = 5

# Creating a new tuple with modified content
new_tuple = my_tuple + (5, 'world')
print(new_tuple)  # Output: (1, 2, 3, 'hello', 3.14, 5, 'world')
```
# Sets?

### A set is an unordered collection of unique elements. Sets are defined by enclosing a comma-separated sequence of values in curly braces {}. Unlike lists or tuples, sets do not allow duplicate elements, and the order of elements is not guaranteed.

## Example of set

```py
my_set = {1, 2, 3, 4, 5}
```

## We can also create a set from a list using the set() constructor

```py
my_list = [1, 2, 2, 3, 4, 4, 5]
converted_set = set(my_list)
print(converted_set)  # Output: {1, 2, 3, 4, 5}
```
# Functions?

### A function is a reusable block of code that performs a specific task or set of tasks, We can define a function by using the "def" keyword.

## Function Basic Syntax

```py
def greet():
    print("Hello From Function")

# Calling/Invoking/Executing the function
greet()
greet()
greet()
```

## Another Simple Example

```py
def printNumber():
  result = 2 + 4
  print(result)

printNumber()
```
# Function Parameter(s)

### Function parameters are values that are passed into a function when it is called. They allow functions to take input, making them more versatile and adaptable.

## Example 1

```py
# ------------- 👇 Parameters
def add_numbers(x, y):
    """This function adds two numbers and prints the result."""
    result = x + y
    print("Sum:", result)

# ----------👇 Arguments
add_numbers(3, 5)
```

## Example 2

```py
def greet_user(username):
  print(f"Hello {username}, How are you doing? ")

greet_user("HuXn")
greet_user("John")
greet_user("Jordan")
```
# Default Param Values

### You can also pass a default value for a parameter in a function. If a value is provided for that parameter when the function is called, it will use the provided value. If no value is provided, the function will use the default value.

## Example 1

```py
def greet_person(name, greeting="Hello"):
    """This function greets a person with a specified greeting (default is Hello)."""
    print(f"{greeting}, {name}!")

greet_person("HuXn") # Uses the default greeting ("Hello")
greet_person("Bob", "Hi there") # Overrides the default greeting with "Hi there"
```

## Example 2

```py
def print_message(message, num_exclamation_marks=3):
    """Print a message with a specified number of exclamation marks."""
    print(message + "!" * num_exclamation_marks)

# Calling the function with different arguments
print_message("Hello") # Prints "Hello!!!" using the default number of exclamation marks
print_message("Hi there", 5) # Prints "Hi there!!!!!" with the specified number of exclamation marks
print_message("Greetings", 10)
```
# Named Arguments

### Keyword arguments, aka named arguments, allow you to pass values to a function by explicitly specifying the parameter names along with their values. This can make function calls more readable and allow you to provide arguments in a different order than they appear in the function definition.

## Example 1

```py
def display_info(name, age, city):
    """Display information about a person."""
    print("Name:", name)
    print("Age:", age)
    print("City:", city)

# Using keyword arguments to call the function
display_info(name="HuXn", age=20, city="US")
```

## Example 2

```py
def calculate_rectangle_area(length, width):
    """Calculate the area of a rectangle."""
    area = length * width
    return area

# Using keyword arguments to call the function
area_result = calculate_rectangle_area(length=5, width=3)
print("Rectangle Area:", area_result)
```
# Return Statement

### The return statement is used within a function to send a value back to the caller. When a function is executed and encounters the return statement, it immediately stops executing, and the specified value is sent back to the caller.

## Example 1

```py
def add_numbers(x, y):
    """This function adds two numbers and returns the result."""
    result = x + y
    return result

# Calling the function and storing the returned result
sum_result = add_numbers(3, 5)
print("Sum:", sum_result)
```

## Example 2

```py
def square_and_cube(x):
    """This function returns both the square and cube of a number."""
    square = x ** 2
    cube = x ** 3
    return square, cube

# Calling the function and storing the returned values
square_result, cube_result = square_and_cube(2)

print("Square:", square_result)
print("Cube:", cube_result)
```
# Nested Functions

### A nested function refers to a function defined within another function.

```py
def outer_function(x):
    """Outer function with a nested function."""

    def inner_function(y):
        """Inner function."""
        return x + y

    result = inner_function(5)
    return result

# Calling the outer function
result_value = outer_function(10)
print("Result:", result_value)
```
# Lambda Function

### Lambda function is a small anonymous function defined using the lambda keyword. It is often referred to as a "lambda expression." Lambda functions are used when you need a simple function for a short period and don't want to formally define a full function using the def keyword.

```py
# lambda arguments: expression

add = lambda x, y: x + y
result = add(3, 5)
print(result)  # Output: 8
```

```py
# Function that takes another function as an argument
def apply_operation(x, y, operation):
    return operation(x, y)

result_addition = apply_operation(5, 3, lambda a, b: a + b)
print("Result of addition:", result_addition)

result_multiplication = apply_operation(5, 3, lambda a, b: a * b)
print("Result of multiplication:", result_multiplication)
```
# Lambda Function

### Lambda function is a small anonymous function defined using the lambda keyword. It is often referred to as a "lambda expression." Lambda functions are used when you need a simple function for a short period and don't want to formally define a full function using the def keyword.

```py
# lambda arguments: expression

add = lambda x, y: x + y
result = add(3, 5)
print(result)  # Output: 8
```

```py
# Function that takes another function as an argument
def apply_operation(x, y, operation):
    return operation(x, y)

result_addition = apply_operation(5, 3, lambda a, b: a + b)
print("Result of addition:", result_addition)

result_multiplication = apply_operation(5, 3, lambda a, b: a * b)
print("Result of multiplication:", result_multiplication)
```
# Scope?

### A scope refers to the region of a program where a particular variable can be accessed or modified. The scope of a variable is determined by where it is defined in the code, and it plays a crucial role in understanding how variables are accessed and manipulated within a program.

## There are two main types of scope in Python:

## 1️⃣ Global Scope

#### Variables defined at the top level are considered to be in the global scope.

#### Global variables can be accessed and modified from any part of the code, including within functions.

```py
global_variable = 10  # This is a global variable

def print_global_variable():
    print(global_variable)

print_global_variable()  # Outputs: 10
```

## 2️⃣ Local Scope

#### Variables defined within a function have local scope and are only accessible within that function.

#### Once the function execution is complete, local variables are typically destroyed, and their values are no longer accessible.

```py
def my_func():
    local_variable = 5  # This is a local variable
    print(local_variable)

my_func()  # Outputs: 5

# Attempting to access the local variable outside the function would result in an error
# print(local_variable)  # Raises a NameError
```

#### There's also another concept of nested scopes (not that much important). If a function is defined within another function, it creates a nested scope. Variables in the outer function can be accessed within the inner function, but not vice versa.

```py
def outer_function():
    outer_variable = "I'm in outer function"

    def inner_function():
        print(outer_variable)

    inner_function()

outer_function()  # Outputs: I'm in outer function
```