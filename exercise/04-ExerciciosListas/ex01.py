# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

numbers = []

for i in range(5):
    numbers.append(int(input(f"Digite o {i+1}º valor: ")))

for i in numbers:
    print(i)
