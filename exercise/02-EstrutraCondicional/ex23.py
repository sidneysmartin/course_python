"""
Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.
"""
value = float(input("Digite um número: "))

result = {
  value.is_integer(): "inteiro",
  not value.is_integer(): "decimal"
}

print(f"O número {value} é {result.get(True)}")