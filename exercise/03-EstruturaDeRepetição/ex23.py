"""
  Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
"""

n = int(input('Digite um numero: '))

amount = 0
for i in range(1, n + 1):
    cont = 0
    for y in range(1, i + 1):
        amount += 1
        if i % y == 0:
            cont += 1

    if cont <= 2:
        print('%d é um número primo' % i)

print('Quantidade de divisões %d' % amount)
