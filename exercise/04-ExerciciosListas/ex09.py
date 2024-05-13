"""
Faça um Programa que leia um vetor A com 10 números inteiros,
calcule e mostre a soma dos quadrados dos elementos do vetor.
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_squares = 0

for i in numbers:
    print(f"{i}² = {i**2}")
    sum_squares += i**2

print(f"Soma dos quadrados: {sum_squares}")
