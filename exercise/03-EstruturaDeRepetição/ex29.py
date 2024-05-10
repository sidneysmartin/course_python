""" 
O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. 
Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu 
um tabela que contém o número de itens que o cliente comprou e ao lado o valor da conta. 
Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços. Você foi contratado para desenvolver o programa que monta esta tabela de preços, que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:
Lojas Quase Dois - Tabela de preços
1 - R$ 1.99
2 - R$ 3.98
...
50 - R$ 99.50
"""
import os

total_prods_sale = int(input("Total de produtos vendidos: "))

while total_prods_sale < 0 or total_prods_sale > 50:
    print("Informe uma quantidade entre 0 e 50")
    total_prods_sale = int(input("Total de produtos vendidos: "))
    os.system("clear")

prices = []
n_product = 1
count = 0
value_total = 0

for i in range(total_prods_sale):
    price = float(input(f"Preço do {n_product}º item: "))
    prices.append(price)
    value_total += price
    n_product += 1
    count += 1

for j in range(count):
    print(f"{j+1} - ********* R$ {prices[j]:.2f}")
    count += 1
    n_product += 1

print(f"Valor total...: R$ {value_total:.2f}")
