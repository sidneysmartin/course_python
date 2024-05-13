""" 
Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
"""

import os
elements = 10
array1 = []
array2 = []
array3 = []
array4 = []

for i in range(elements):
    array1.append(int(input(f"1º array, Digite o {i+1}º valor: ")))
os.system("clear")
for i in range(elements):
    array2.append(int(input(f"2º array, Digite o {i+1}º valor: ")))
os.system("clear")
for i in range(elements):
    array3.append(int(input(f"3º array, Digite o {i+1}º valor: ")))
os.system("clear")


for i in range(elements):
    array4.append(array1[i])
    array4.append(array2[i])
    array4.append(array3[i])

print("Vetor intercalado com os valores do 1º e 2º  e 3º array.")
for i in range(len(array4)):
    print(f"{i+1}º valor: {array4[i]}")
