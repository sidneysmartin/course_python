"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
"""
n_terms = int(input("Calcule o fatorial de: "))
fat = 1
count = 1

if n_terms <= 2:
    fat = 1
    print(fat)
else:
    while count <= n_terms:
        fat *= count
        count += 1
    print(f"{n_terms}! = {fat}")
