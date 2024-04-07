"""
Funções em python-
São blocos reutilizáveis de código que realizam tarefas especificas
"""
import os
os.system('cls')
def calcSum(value1, value2):
  return value1 + value2

value1 = int(input("Digite 1º valor: "))
value2 = int(input("Digite 2º valor: "))

sum = calcSum(value1, value2)
print(f"A soma dos valores é: {sum}")