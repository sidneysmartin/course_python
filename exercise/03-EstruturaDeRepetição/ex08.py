import os
"""
Faça um programa que leia 5 números e informe a soma e a média dos números.
"""
# https://wiki.python.org.br/EstruturaDeRepeticao

sum = 0
avg = 0
i = 0

while (i < 5):
  value = float(input(f"{i+1}º valor: "))
  sum += value
  i +=1
avg = sum / 5
print(f"Soma dos 5 valores informados: {sum:.2f}\nA média dos valores informados: {avg:.2f}")