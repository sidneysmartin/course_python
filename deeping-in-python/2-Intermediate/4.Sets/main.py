# Exemple of Sets
my_set = {1, 2, 3, 4, 5}
# print(my_set)


# We can also create a set from a list using the set() constructor
my_list = [1, 2, 3, 3, 5, 5, 5, 7, 7, 7, 11, 13]
# print(my_list) # output: [1, 2, 3, 3, 5, 5, 5, 7, 7, 7, 11, 13]
converted_set = set(my_list)
# print(converted_set) # output: {1, 2, 3, 5, 7, 11, 13}

foods = ['rice', 'beans', "meat", "meat",
         'rice', 'eggs', 'onions', 'onions']
# print(foods)# output: ['rice', 'beans', 'meat', 'meat', 'rice', 'eggs', 'onions', 'onions']
converted_foods = set(foods)
print(converted_foods)
print(type(converted_foods))

# Add multiple items in a set
numbers = {1, 2, 3}
numbers.update([4, 5, 6])
print(numbers)
numbers.add(7)
print(numbers)

# delete element from a set
numbers.remove(1)
print(numbers)
# numbers.clear() # delete all elements


# iterating over a set
for number in numbers:
    print(number)
