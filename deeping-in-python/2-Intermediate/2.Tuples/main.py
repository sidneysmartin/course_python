# Basic syntax

my_tuple = (1, 2, 3, 'hello', 3.14)
print(my_tuple[0])  # Output: 1
print(my_tuple[3])  # Output: 'hello'

# Erro
my_tuple = (1, 2, 3, 'hello', 3.14)
# This will raise an error since tuples are immutable
# my_tuple[0] = 5

# Creating a new tuple with modified content
new_tuple = my_tuple + (5, 'world')
print(new_tuple)  # Output: (1, 2, 3, 'hello', 3.14, 5, 'world')

# Weird things about tuple
values = 1,6,7,98,'Python','hello'
print(values, type(values))