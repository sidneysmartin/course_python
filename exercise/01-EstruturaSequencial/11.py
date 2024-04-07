"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
. o produto do dobro do primeiro com metade do segundo .
a. a soma do triplo do primeiro com o terceiro.
b. o terceiro elevado ao cubo.
"""

first = int(input("1º valor: "))
second = int(input("2º valor: "))
thirty = float(input("3º valor: "))

result1 = (first * 2) * (second /2)
result2 = (first * 3) + thirty
result3  = thirty ** 3

print(f"O produto do dobro do {first} com metade do {second}...: {result1}")
print(f"A soma do triplo de {first} com o {thirty}.............: {result2}")
print(f"O cudo de {thirty}³....................................: {result3}")