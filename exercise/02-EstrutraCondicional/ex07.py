# Faça um Programa que leia três números e mostre o maior e o menor deles.

num1 = int(input("Digite o 1º número: "))
num2 = int(input("Digite o 2º número: "))
num3 = int(input("Digite o 3º número: "))

if num1 < num2 and num2 < num3:
  print(f"O menor número é: {num1}\nO maior número é: {num3}")
elif num1 < num3 and num3 < num2:
  print(f"O menor número é: {num1}\nO maior número é: {num2}")
elif num2 < num1 and num1 < num3:
  print(f"O menor número é: {num2}\nO maior número é: {num3}")
elif num2 < num3 and num3 < num1:
  print(f"O menor número é: {num2}\nO maior número é: {num1}")
elif num3 < num1 and num1 < num2:
  print(f"O menor número é: {num3}\nO maior número é: {num2}")
elif num3 < num2 and num2 < num1:
  print(f"O menor número é: {num3}\nO maior número é: {num1}")
  