""" 
Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
"""

numbers = []
sum = 0
product = 1
for i in range(5):
    numbers.append(int(input(f"Digite o {i+1}º valor: ")))
    sum += numbers[i]
    product *= numbers[i]

print(f"Numeros: {numbers}")
print(f"Soma: {sum}")
print(f"Multiplicação: {product}")
