"""
Faça um Programa que peça a idade e a altura de 5 pessoas, 
armazene cada informação no seu respectivo vetor. 
Imprima a idade e a altura na ordem inversa a ordem lida
"""
import os
people = {
    "age": [],
    "height": []
}

for i in range(5):
    while True:
        try:
            age = int(input(f"Idade da {i+1}º pessoa: "))
            if 0 <= age <= 150:
                people["age"].append(age)
            else:
                raise ValueError("A idade deve estar entre 0 e 150.")

            height = float(input(f"Altura da {i+1}º pessoa: "))
            if 0.3 <= height <= 2.4:
                people["height"].append(height)
            else:
                raise ValueError("A altura deve estar entre 0.3m e 2.4m.")

            break
        except ValueError as e:
            print("Entrada inválida:", e)
os.system('clear')
for i in range(4, -1, -1):
    print(f"Idade da {i+1}º pessoa: {people['age'][i]}")
    print(f"Altura da {i+1}º pessoa: {people['height'][i]}")
