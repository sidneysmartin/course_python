"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros
quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário
a quantidades de latas de tinta a serem compradas e o preço total.
"""
import math
area = float(input("Informe o tamanho do da área: "))
litros = area / 3
priceT = 80.0
volume = 18

latas = math.ceil(litros / volume)
total = latas * priceT

print(f"Área m²..........: R$ {area}")
print(f"Total de latas...: {(latas)}")
print(f"Preço total......: R$ {(total)}")