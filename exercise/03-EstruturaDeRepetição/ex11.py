"""
Altere o programa anterior para mostrar no final a soma dos números.
"""
num1 = int(input("Informe o 1º valor: "))
num2 = int(input("Informe o 2º valor: "))
sum = 0
count = 0

if num2 <= num1:
  count = num2
  while count <= num1:
    print(count)
    sum += count
    count += 1
elif num1 <= num2:
  count = num1
  while count <= num2:
    print(count)
    sum += count
    count += 1
print(f"A soma dos valores: {sum}")