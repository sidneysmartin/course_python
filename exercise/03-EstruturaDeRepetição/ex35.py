""" 
Encontrar números primos é uma tarefa difícil. 
Faça um programa que gera uma lista dos números primos 
existentes entre 1 e um número inteiro informado pelo usuário.
"""

number = int(input("\nDigite um número: "))
list = []

for i in range(number + 1):
    if i % 2 == 1 and i != 2:
        list.append(i)

print("Números primos: ", list)
