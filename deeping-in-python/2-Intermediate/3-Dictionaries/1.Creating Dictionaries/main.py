# Empty Dictionary
empty_dict = {}
# print(type(empty_dict))

# Dictionary with Key-Value Pairs
student_info = {'name': 'Ana Clara', 'code': 1223,
                'matter': 'physics', 'grade': 'B'}
# print(student_info)

# Using the dict() Constructor
dict_from_list = dict([('name', 'Ana Clara'), ('code', 1223),
                       ('matter', 'physics'), ('grade', 'B')])
# print(dict_from_list)

# Dictionary with Different Data Types
mixed_dict = {'name': 'Ana Clara', 'code': 1223,
              'matter': 'physics', 'grade': 'B', 'name': 'Ana Clara'}
print(mixed_dict)

# Nested Dictionary
nested_dict = {
    'person': {'name': 'Ana Clara', 'age': 10},
    'location': {'country': 'Brazil', 'city': 'Belo Horizonte'},
}
# print(nested_dict)

# Using a List of Tuples
tuple_list = [('name', 'Carlos Eduardo'), ('age', 3),
              ("city", "Belo Horizonte")]

from_tuple_dict = dict(tuple_list)
print(from_tuple_dict)
