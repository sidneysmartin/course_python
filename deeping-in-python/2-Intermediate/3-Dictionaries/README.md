# Dictionaries?

### A dictionary is a built-in data type that represents a collection of key-value pairs. It is a highly flexible and efficient data structure used for mapping keys to values.

## Key features of dictionaries

#### 👉 Each element in a dictionary consists of a key and its corresponding value. The key is a unique identifier for the value.

#### 👉 Unlike lists, dictionaries are unordered collections, which means the order of elements is not guaranteed.

#### 👉 Dictionaries can be modified after creation. You can add, remove, or update key-value pairs.

#### 👉 Dictionaries can grow or shrink in size as needed.

#### 👉 Each key in a dictionary must be unique. If you try to add a key that already exists, the new value will overwrite the existing one.

## Empty Dictionary

```py
empty_dict = {}
```

## Dictionary with Key-Value Pairs

```py
student_info = {'name': 'Alice', 'age': 20, 'grade': 'A'}
```

## Using the dict() Constructor

```py
person = dict(name='Bob', age=25, city='London')
```

## Dictionary with Different Data Types

```py
mixed_dict = {'name': 'Charlie', 'age': 30, 'grades': [85, 90, 78], 'is_student': True}
```

## Nested Dictionary

```py
nested_dict = {'person': {'name': 'David', 'age': 22}, 'location': {'city': 'Paris', 'country': 'France'}}
```

## Using a List of Tuples

```py
tuple_list = [('name', 'Eva'), ('age', 28), ('city', 'Berlin')]
from_tuples_dict = dict(tuple_list)
```

# Accessing Items

### We can access items in dictionaries using their keys.

## Using Square Brackets

```py
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
print(my_dict['name'])  # John
print(my_dict['age'])   # 25
```

## Using the get() Method

```py
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
print(my_dict.get('name'))  # John
print(my_dict.get('grade', 'Not Available'))  # Not Available
```

## Iterating Through Keys

```py
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
for key in my_dict:
    print(f"{key}: {my_dict[key]}")
```

## Iterating Through Items (Key-Value Pairs)

```py
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
for key, value in my_dict.items():
    print(f"{key}: {value}")
```

# Updating Dictionaries?

### We can update dictionaries by adding, modifying, or removing key-value pairs.

## Adding a New Key-Value Pair

```py
my_dict = {'name': 'John', 'age': 25}
my_dict['city'] = 'New York'
```

## Modifying an Existing Value

```py
my_dict = {'name': 'John', 'age': 25}
my_dict['age'] = 26
```

## Updating with Another Dictionary

```py
my_dict = {'name': 'John', 'age': 25}
update_dict = {'age': 26, 'city': 'New York'}
my_dict.update(update_dict)
```

## Updating with Keyword Arguments

```py
my_dict = {'name': 'John', 'age': 25}
my_dict.update(age=26, city='New York')
```

## Using setdefault() to Add Default Values

```py
my_dict = {'name': 'John', 'age': 25}
my_dict.setdefault('city', 'New York')
```

# Deleting In Dictionaries

### We can delete items from dictionaries using the del statement or the pop() method.

## del Statement

```py
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
del my_dict['age']
```

## pop() Method

```py
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
my_dict.pop('age')
```

## popitem() Method

```py
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
my_dict.popitem()
```

## clear() Method to Remove All Items

```py
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
my_dict.clear()
```