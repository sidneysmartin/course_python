# return statement

def add_numbers(x, y):
    sum = x + y
    return sum


sum_result = add_numbers(9, 8)
print(sum_result)


# return double return
def square_and_cube(x):
    square = x ** 2
    cube = x ** 3
    return square, cube


value = 5
square_result, cube_result = square_and_cube(value)
print(f"Quadrado de {value} : {square_result}\nCubo de {value}: {cube_result}")
