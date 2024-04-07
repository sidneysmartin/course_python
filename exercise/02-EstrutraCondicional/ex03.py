# Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

gender = input("F - Feminino, M - Masculino, Sexo Inválido: ")

if gender.upper() == "F":
  print("F - Feminino")
elif gender == "M":
  print("M - Masculino")
else:
  print("Sexo Inválido")