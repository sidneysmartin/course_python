"""
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, 
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
o Média de Aproveitamento Conceito
o Entre 9.0 e 10.0    A 
o Entre 7.5 e 9.0     B 
o Entre 6.0 e 7.5     C 
o Entre 4.0 e 6.0     D
o Entre 4.0 e zero    E
"""
grade1 = float(input("Digite a primeira nota: "))
grade2 = float(input("Digite a segunda nota: "))
average = (grade1 + grade2) / 2
print("A sua média foi de {:.1f}".format(average))

conceito = {
  9.0 : "A",
  7.5 : "B",
  6.0 : "C",
  4.0 : "D",
  0.0 : "E"
}

if average >= 9.0:
  print("Seu conceito é {}".format(conceito[9.0]))
elif average >= 7.5:
  print("Seu conceito é {}".format(conceito[7.5]))
elif average >= 6.0:
  print("Seu conceito é {}".format(conceito[6.0]))
elif average >= 4.0:
  print("Seu conceito é {}".format(conceito[4.0]))
else:
  print("Seu conceito é {}".format(conceito[0.0]))
