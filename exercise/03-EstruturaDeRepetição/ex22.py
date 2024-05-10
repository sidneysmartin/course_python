"""
Altere o programa de cálculo dos números primos, informando, 
caso o número não seja primo, por quais número ele é divisível.
"""
number = int(input("Verifique se o número é primo: "))
cousin_number = 0
i = 1
while i <= number:
    if number % i == 0:
        cousin_number += 1
    i += 1
if cousin_number == 2:
    print(f"{number} e primo")
else:
    print(f"{number} não é primo")
    print("Números divisíveis.")
    i = 1
    while i <= number:
        if number % i == 0:
            print(i)
        i += 1
