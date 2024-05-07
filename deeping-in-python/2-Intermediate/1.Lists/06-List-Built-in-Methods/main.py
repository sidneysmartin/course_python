# List built-in methods

my_list = [1, 2, 3]
# append() - adds an element at the end of the list
my_list.append(4)
print(my_list) # [1, 2, 3, 4]

# extend(iterable)
# Extends the list by appending elements from iterable

my_list.extend([4, 5, 6])
# Result: [1, 2, 3, 4, 5, 6]
print(my_list)

# insert(i, x)
# Inserts element x at the specified position i.
my_list.insert(1, 4)
# Result: [1, 4, 2, 3]
print(my_list)

# remove(x)
# Removes the first occurrence of element x.
my_list.remove(2)
# Result: [1, 3, 2]
print(my_list)

# pop([i])
# Removes and returns the element at the specified position i. If no index is provided, it removes and returns the last element.
popped_element = my_list.pop(1)
# Result: popped_element=2, my_list=[1, 3]
print(popped_element)

# count(x)
# Returns the number of occurrences of element x in the list.
count_of_2 = my_list.count(2)
# Result: count_of_2=2
print(count_of_2)

# sort(key=None, reverse=False)
# Sorts the elements of the list in ascending order. The key and reverse parameters are optional.
new_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
new_list.sort()
print(new_list)

# reverse()
# Reverses the elements of the list in place.
print(new_list.reverse())

# copy()
# Returns a shallow copy of the list.
original_list = [1, 2, 3]
copied_list = original_list.copy()
# Result: copied_list=[1, 2, 3]