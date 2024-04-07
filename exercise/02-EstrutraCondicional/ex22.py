"""
Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).
"""

num = int(input("Digite um número inteiro: "))

result = {
  num % 2 == 0: "par",
  num % 2 != 0: "impar"
}

print(f"O número {num} é {result.get(True)}")