""" 
Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.
"""
total_cd = int(input("Informe a quantidade de CDs: "))
value_cd = 0
sum_cd = 0
avg_value_cd = 0
for i in range(total_cd):
    value_cd = float(input(f"Informe o valor do {i + 1}º CD: "))
    print(f"O valor do {i + 1}º CD: {value_cd}")
    sum_cd += value_cd
avg_value_cd = sum_cd / total_cd
print(f"Total de CDs....: {total_cd}")
print(f"Valor total.....: {sum_cd:.2f}")
print(f"Média de valor..: {avg_value_cd:.2f}")
