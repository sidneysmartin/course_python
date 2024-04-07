"""
limpar o terminal antes de exibir a mensagem

import os
 
# Clearing the Screen
os.system('cls')
"""
import os
 
# input permite a entrada de dados do usuário 
name = input("Qual seu nome? ")
altura = input("Qual sua altura? ")
peso = input("Qual seu peso? ")
os.system('clear')
imc = float(peso) / (float(altura) * float(altura))
if imc < 18.5:
  print("Abaixo do peso")
elif imc >= 18.5 and imc < 25:
  print("Peso normal")
elif imc >= 25 and imc < 30:
  print("Sobrepeso")
elif imc >= 30 and imc < 40:
  print("Obeso")
print(f"O IMC de {name} e {format(imc, '.2f')}")
print(f"{altura} de altura e {peso} kg")
