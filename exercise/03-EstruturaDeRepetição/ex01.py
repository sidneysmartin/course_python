"""
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
"""

grade = float(input("Insira uma nota entre 0 e 10: "))

while grade < 0 or grade > 10:
  print("Nota inválida!")
  grade = float(input("Insira uma nota entre 0 e 10: "))
  
print("Nota registrada com sucesso!")