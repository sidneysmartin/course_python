# Complete Module
"""
import my_op_math

print(my_op_math.intro())
print(my_op_math.my_number)


print(my_op_math.add_to_number(5, 3))

print(my_op_math.sub_to_number(5, 3))

print(my_op_math.mult_to_number(5, 3))

print(my_op_math.div_to_number(15, 3))

print(my_op_math.exp_to_number(15, 3))
"""

# Import as alias
"""
import my_op_math as math
print(math.add_to_number(5, 3))

print(math.sub_to_number(5, 3))

print(math.mult_to_number(5, 3))

print(math.div_to_number(15, 3))

print(math.exp_to_number(15, 3))
"""

# Specific Item
"""
from my_op_math import (my_number, intro)
print(my_number)
intro()
"""

# Import Specific item from a module and provide alias to that
"""
from my_op_math import (
  my_number,
  intro,
  add_to_number as addition,
  sub_to_number as subtract,
  mult_to_number as multiply,
  div_to_number as divide,
  exp_to_number as exponent
)

print(my_number)
intro()
print(addition(6, 4))
print(subtract(6, 4))
print(multiply(6, 4))
print(divide(24, 3))
print(exponent(2, 3))
"""

# All Items

from my_op_math import *
print(my_number)
intro()
print(add_to_number(7, 5))
print(sub_to_number(7, 5))
print(mult_to_number(7, 5))
print(div_to_number(45, 5))
print(exp_to_number(5, 3))
