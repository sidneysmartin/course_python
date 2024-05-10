"""
    A série de Fibonacci é formada pela sequência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.
"""

first = 0
print(first)
second = 1

while second <= 500:
    print(second)
    third = first + second
    first, second = second, third
