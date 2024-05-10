"""
Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.
"""
import os
group_25 = []
group_50 = []
group_75 = []
group_100 = []
number = 0
while number >= 0 and number <= 100:
    number = float(input("Digite um valor entre 0 e 100: "))
    if number < 0 or number > 100:
        break
    if number >= 0 and number <= 25:
        group_25.append(number)
    elif number > 25 and number <= 50:
        group_50.append(number)
    elif number > 50 and number <= 75:
        group_75.append(number)
    elif number > 75 and number <= 100:
        group_100.append(number)
    os.system('clear')

print("\nValores entre [0, 25]: ", len(group_25))
print("Valores entre [26, 50]: ", len(group_50))
print("Valores entre [51, 75]: ", len(group_75))
print("Valores entre [76, 100]: ", len(group_100))
