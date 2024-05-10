"""
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
"""

val = 0
count = 0
countEven = 0
countOdd = 0

for count in range(10):
    val = int(input(f"Informe 10 valores - {count + 1}º valor: "))
    if val % 2 == 0:
        countEven += 1
    if val % 2 == 1:
        countOdd += 1
print("Quantidade de pares....: ", countEven)
print("Quantidade de Ímpares..: ", countOdd)