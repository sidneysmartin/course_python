""" 
Faça um Programa que leia dois vetores com 10 elementos cada. 
Gere um terceiro vetor de 20 elementos, cujos valores deverão ser 
compostos pelos elementos intercalados dos dois outros vetores.
"""
import os
elements = 10
array1 = []
array2 = []
array3 = []

for i in range(elements):
    array1.append(int(input(f"1º array, Digite o {i+1}º valor: ")))
os.system("clear")
for i in range(elements):
    array2.append(int(input(f"2º array, Digite o {i+1}º valor: ")))
os.system("clear")


for i in range(len(array1)):
    array3.append(array1[i])
    array3.append(array2[i])

print("Vetor intercalado com os valores do 1º e 2º array.")
for i in range(len(array3)):
    print(f"{i+1}º valor: {array3[i]}")
