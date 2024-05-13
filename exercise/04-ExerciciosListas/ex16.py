""" 
Utilize uma lista para resolver o problema a seguir. 
Uma empresa paga seus vendedores com base em comissões.
O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. 
Por exemplo, um vendedor que teve vendas brutas de $3000 em uma 
semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. 
Escreva um programa (usando um array de contadores) que determine quantos 
vendedores receberam salários nos seguintes intervalos de valores:
$200 - $299
$300 - $399
$400 - $499
$500 - $599
$600 - $699
$700 - $799
$800 - $899
$900 - $999
$1000 em diante
Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.
"""
sellers = [0] * 9  # Inicializa a lista de salários

for i in range(len(sellers)):
    sale = float(input('Digite o valor das vendas: '))
    salario = ((sale * 9)/ 100) + 200  # Calcula o salário

    # Calcula a posição na lista de salários
    if salario >= 1000:
        position = 8
    else:
        position = int((salario - 200) / 100)
    
    # Incrementa o contador na posição correspondente
    sellers[position] += 1

for i in range(8):
    print ('%d - %d : %d' % (i * 100 + 200, (i + 1) * 100 + 199, sellers[i]))
print("Salários maiores que R$1000:", sellers[8])
