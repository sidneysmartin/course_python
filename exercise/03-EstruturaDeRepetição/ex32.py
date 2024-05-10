"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120
"""

num = int(input("Digite um número: "))
numCalc = num
factorial = 1
print("Fatorial de:", num)

numbers = []

while (numCalc > 0):
    factorial = factorial * numCalc
    numbers.append(str(numCalc))  # Adiciona o número atual à lista
    numCalc = numCalc - 1

# Junta os números com ' . ' e imprime o cálculo factorial
print(num, '! = ' + ' . '.join(numbers) + ' = ' + str(factorial))
