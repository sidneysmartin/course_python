"""
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
Um número primo é aquele que é divisível somente por ele mesmo e por 1.
"""
number = int(input("Verifique se o número é primo: "))
cousin_number = 0
i = 1
while i <= number:
    if number % i == 0:
        cousin_number += 1
    i += 1
if cousin_number == 2:
    print(f"{number} e primo")
else:
    print(f"{number} não é primo")
