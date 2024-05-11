# Using Square Brackets
my_dict = {"name": "Naruto", "age": 17,
           "clan": "Uzumaki", "city": "Konoha", "rank": "Genin"}

# print(my_dict["name"])  # Output: Naruto
# print(my_dict["rank"])  # Output: Genin
# Using the get() Method
# print(my_dict.get("clan"))  # Output: Uzumaki
# print(my_dict.get("hokage", "Não é o Hokage ainda."))  # Output: None

# Iterating Through Keys
"""
for key in my_dict:
    print(f"{key}: {my_dict[key]}")
"""

# Iterating Through Items (Key Value Pairs)
for key, value in my_dict.items():
    print(f"{key}: {value}")
