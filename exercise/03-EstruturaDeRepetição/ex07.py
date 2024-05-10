"""
Faça um programa que leia 5 números e informe o maior número.
"""
import os
print("Informe 5 valores")

i = 0
value = 0
 
valueMax = -float('inf')
valueMin = float('inf')

for i in range (5):
  os.system('clear')
  value = float(input(f"{i+1}º valor: "))  
  if value > valueMax: 
    valueMax = value
  if value < valueMin: 
    valueMin = value
   

print(f"Maior valor informado: {valueMax}")
print(f"Menor valor informado: {valueMin}")
print("Informe 5 valores")

i = 0
value = 0
 
valueMax = -float('inf')
valueMin = float('inf')

for i in range (5):
  value = float(input(f"{i+1}º valor: ")) 
  if value > valueMax: 
    valueMax = value
  if value < valueMin: 
    valueMin = value
  os.system('clear')

print(f"Maior valor informado: {round(valueMax)}")
print(f"Menor valor informado: {round(valueMin)}")