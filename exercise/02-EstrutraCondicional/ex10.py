"""
Faça um Programa que pergunte em que turno você estuda.
 Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""

turno = input("Em que turno você estuda? (M-matutino, V-vespertino, N-noturno): ")

if turno.upper() == "M":
  print("\nBom Dia!")
elif turno.upper() == "V":
  print("\nBoa Tarde!")
elif turno.upper() == "N":
  print("\nBoa Noite!")
else:
  print("\nHorário Inválido!")