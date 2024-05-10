""" 
Faça um programa que mostre os n termos da Série a seguir:
S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
Imprima no final a soma da série.
"""
n_terms = int(input("Quantos termos? "))
sum = 0
divider = 1
for i in range(1, n_terms + 1):
    sum += 1 / divider
    divider += 2

print(f"S = {sum:.2f}")
