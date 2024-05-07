# Removing Items
clothes = ["bag", "shoes", "shirt", "hat", "pants", "jacket","belt"]
# Using slicing

print(clothes[0:3])
print(clothes[4:])
print(clothes[:3])
print(clothes[0:7:2])

# using del
del clothes[5]
print(clothes)

my_list = [1, 2, 3, 4, 5]

# Deleting the item at index 2
del my_list[2]
print(my_list)

# using remove() method
clothes.remove("bag")
print(clothes)

my_list = [1, 2, 3, 4, 5]

# Removing the value 3 from the list
my_list.remove(3)
print(my_list)