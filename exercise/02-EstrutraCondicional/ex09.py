# Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1 = int(input("Digite o 1º número: "))
num2 = int(input("Digite o 2º número: "))
num3 = int(input("Digite o 3º número: "))
print("\n")
if num1 > num2 and num1 > num3:
  if num2 > num3:
    print(f"{num1} - {num2} - {num3}")
  else:
    print(f"{num1} - {num3} - {num2}")
elif num2 > num1 and num2 > num3:
  if num1 > num3:
    print(f"{num2} - {num1} - {num3}")
  else:
    print(f"{num2} - {num3} - {num1}")
else:
  if num1 > num2:
    print(f"{num3} - {num1} - {num2}")
  else:
    print(f"{num3} - {num2} - {num1}")