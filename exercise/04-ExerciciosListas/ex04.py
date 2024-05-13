""" 
Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
"""
characters = []
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
              'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
count = 0

for i in range(10):
    characters.append(input(f"Digite o {i+1}º caractere: "))
    if characters[i].lower() in consonants:
        count += 1

for character in characters:
    if character.lower() in consonants:
        print(f"{character} e uma consoante.")

print(f"Foram lidas {count} consoantes.")
