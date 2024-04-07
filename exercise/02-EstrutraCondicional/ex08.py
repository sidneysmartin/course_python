"""
Faça um programa que pergunte o preço de três produtos e informe qual 
produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
"""

price1 = float(input("Preço do 1º produto: R$ "))
price2 = float(input("Preço do 2º produto: R$ "))
price3 = float(input("Preço do 3º produto: R$ "))

if price1 < price2 and price2 < price3:
  print(f"\nO 1º produto é mais barato.\nSeu valor é: R$ {price1}")
elif price1 < price3 and price3 < price2:
  print(f"\nO 1º produto é mais barato.\nSeu valor é: R$ {price1}")
elif price2 < price1 and price1 < price3:
  print(f"\nO 2º produto é mais barato.\nSeu valor é: R$ {price2}")
elif price2 < price3 and price3 < price1:
  print(f"\nO 2º produto é mais barato.\nSeu valor é: R$ {price2}")
elif price3 < price1 and price1 < price2:
  print(f"\nO 3º produto é mais barato.\nSeu valor é: R$ {price3}")
elif price3 < price2 and price2 < price1:
  print(f"\nO 3º produto é mais barato.\nSeu valor é: R$ {price3}")