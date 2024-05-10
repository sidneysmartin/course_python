"""
Faça um programa que, dado um conjunto de N números, 
determine o menor valor, o maior valor e a
"""

group = int(input("Quantos números deseja informar? "))
max_value = 0
min_value = 0
sum = 0

for i in range(group):
    value = int(input(f"{i+1}º valor: "))
    if i == 0:
        max_value = value
        min_value = value
    else:
        if value > max_value:
            max_value = value
        if value < min_value:
            min_value = value

    sum += value

print(f"Menor valor informado: {min_value}")
print(f"Maior valor informado: {max_value}")
print(f"Soma dos valores informados: {sum}")
