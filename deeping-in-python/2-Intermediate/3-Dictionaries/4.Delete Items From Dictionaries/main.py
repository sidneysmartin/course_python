# del statement
my_dict = {'group': 'Justice League', 'hero': 'Batman',
           'rank': 2, 'city': 'Gotham',  'secret_identity': 'Bruce Wayne', 'ceo': 'Industries Wayne'}
# Output: {'group': 'Justice League', 'hero': 'Batman', 'rank': 2, 'city': 'Gotham', 'secret_identity': 'Bruce Wayne'}

del my_dict['secret_identity']
# Output: {'group': 'Justice League', 'hero': 'Batman', 'rank': 2, 'city': 'Gotham'}

# pop() method
my_dict.pop('ceo')
# Output: {'group': 'Justice League', 'hero': 'Batman', 'rank': 2, 'city': 'Gotham'}


# popitem() method to remove last inserted item
my_dict.popitem()
# Output: {'group': 'Justice League', 'hero': 'Batman', 'rank': 2, 'city': 'Gotham'}

# clear() method to remove all items
my_dict.clear()
print(my_dict)
