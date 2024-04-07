"""
Faça um Programa que calcule a área de um quadrado, 
em seguida mostre o dobro desta área para o usuário.
"""

side = float(input("Informe o lado do quadrado: "))

area = side * side
doubleArea = area * 2
print(f"O Lado é: {side}.")
print(f"A Área é: {area}.")
print(f"Dobro da area é: {doubleArea}.")
