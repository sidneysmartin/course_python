""" 
O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.
"""

group_amount = int(input("Quantas temperaturas deseja informar? "))

sum = 0
avg_tmp = 0
min_tmp = 0
max_tmp = 0

for i in range(group_amount):
    tmp = float(input(f"{i+1}º temperatura: "))
    sum += tmp
    if i == 0:
        max_tmp = tmp
        min_tmp = tmp
    else:
        if tmp > max_tmp:
            max_tmp = tmp
        if tmp < min_tmp:
            min_tmp = tmp

avg_tmp = sum / group_amount
print(f"Menor temperatura informada: {min_tmp:.2f}")
print(f"Maior temperatura informada: {max_tmp:.2f}")
print(f"Média das temperaturas informadas: {avg_tmp:.2f}")
