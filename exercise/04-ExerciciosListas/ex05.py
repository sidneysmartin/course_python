""" 
Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. 
Imprima os três vetores.
"""

numbers = []


def is_even(number):
    return number % 2 == 0


def is_odd(number):
    return number % 2 != 0


check_numbers = {
    "even": [],
    "odd": []
}

for i in range(20):
    numbers.append(int(input(f"Digite o {i+1}º valor: ")))

for number in numbers:
    if is_even(number):
        check_numbers["even"].append(number)
    elif is_odd(number):
        check_numbers["odd"].append(number)

evens = check_numbers["even"]
odds = check_numbers["odd"]
print(f"Numeros pares: {evens}\nNumeros impares: {odds}")
