"""
Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
"""

value1 = int(input("Informe o 1º valor do intervalo: "))
value2 = int(input("Informe o 2º valor do intervalo: "))
i = 0

if value1 >= value2: 
  for i in range(value2,value1+1):
    print(i)
else:
  for i in range(value1,value2+1):
    print(i)
 