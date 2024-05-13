# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

numbers = []
for i in range(10):
    numbers.append(float(input(f"Digite o {i+1}º valor: ")))

for i in range(len(numbers) - 1, -1, -1):
    print(f"{i+1}º valor: {numbers[i]}")
