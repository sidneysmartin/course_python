"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu
peso ideal, utilizando as seguintes fórmulas:
. Para homens: (72.7*h) - 58
a. Para mulheres: (62.1*h) - 44.7
"""
height = float(input("Informe a altura .......: "))
weightM = (72.7 * height) - 58
weightW = (62.1 * height) - 44.7
print(f"Altura......................: {height}")
print(f"Peso ideal para homens......: {weightM} kg")
print(f"Peso ideal para mulheres....: {weightW} kg")