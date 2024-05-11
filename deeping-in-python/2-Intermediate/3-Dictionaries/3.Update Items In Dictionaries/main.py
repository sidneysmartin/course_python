# Adding a New Key-Value Pair
my_dict = {'warchief': 'Thrall', 'spec': 'Shaman'}
my_dict["city"] = 'Orgrimmar'
# print(my_dict) # Output: {'warchief': 'Thrall', 'spec': 'Shaman', 'city': 'Orgrimmar'}
# Modifying an existing value
my_dict['warchief'] = 'Thrall Go"el '
# print(my_dict) # Output: {'warchief': 'Thrall Go"el ', 'spec': 'Shaman', 'city': 'Orgrimmar'}

# Updating with Another Dictionary
updated_dict = {'raid': 'Blackwing Descent'}
my_dict.update(updated_dict)
print(my_dict)

# # Updating with keyword arguments
another_dict = {'king_of_alliance': "Varian Wrynn", 'race': 'human'}
another_dict.update(spec="Warrior", city="Stormwind")
print(another_dict)
# using setdefault() to add default values
another_dict.setdefault("king_of_alliance", "Varian Wrynn")
print(another_dict)
