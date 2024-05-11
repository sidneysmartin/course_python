my_dict = {'serie': 'The Lord of the Rings',
           'movie': 'The return of the King',
           'director': 'Peter Jackson',
           'year': 2003,
           'oscars': 11, }
# iterating through keys

"""
for key in my_dict:
    print(key)  # Output: serie, movie, director, year, oscars

"""
# iterating through values
"""
for value in my_dict.values():
    # Output: The Lord of the Rings, The return of the King, Peter Jackson, 2003, 11
    print(value)

"""
# Iterating through keys-values-pais
"""
while True:
    for key, value in my_dict.items():
        print(f"{key}: {value}")
    break
"""

# items() method

"""
for key, value in my_dict.items():
    print(f"{key}: {value}")
"""

# keys() method
"""
  for key in my_dict.keys():
      print(key)
"""
# values() method
for value in my_dict.values():
    print(value)
