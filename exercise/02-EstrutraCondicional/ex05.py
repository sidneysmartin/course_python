"""
Faça um programa para a leitura de duas notas parciais de um aluno. 
O programa deve calcular a média alcançada por aluno e apresentar:
 - A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
 - A mensagem "Reprovado", se a média for menor do que sete;
 - A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""
grade1 = float(input("Nota 1: "))
grade2 = float(input("Nota 2: "))

average = (grade1 + grade2) / 2

if average >= 7:
  if average == 10:
    print("Aprovado com Distinção")
  else:
    print("Aprovado")
else:
  print("Reprovado")
  