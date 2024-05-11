#  Lambda Function  is a small Anonymous Function
# syntax  -lambda arguments: expression

add = lambda x, y: x+y
result = add(5,8)
print(result)

# Function that takes another function as an argument
def apply_operation(x, y, operation):
    return operation(x, y)

result_addition = apply_operation(5, 3, lambda a, b: a + b)
print("Result of addition:", result_addition)

result_multiplication = apply_operation(5, 3, lambda a, b: a * b)
print("Result of multiplication:", result_multiplication)