# In Strings
text = "Hello, World!"
result = 'o' in text
print(result)  # Output: True
# In Lists
numbers = [1, 2, 3, 4, 5]
result = 3 in numbers
print(result)  # Output: True
# In Tuples
fruits = ('apple', 'banana', 'cherry')
result = 'banana' in fruits
print(result)  # Output: True
# In Dictionaries (Checking Keys)
person = {'name': 'John', 'age': 30, 'city': 'New York'}
result = 'age' in person
print(result)  # Output: True
# In Sets
colors = {'red', 'green', 'blue'}
result = 'yellow' in colors
print(result)  # Output: False
# In Substrings
sentence = "Python is powerful"
result = "power" in sentence
print(result)  # Output: True