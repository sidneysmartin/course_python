"""
Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.
"""
base = int(input("Informe a base: "))
expo = int(input("Informe o expoente: "))


def calc_expo_for(b, e):
    if e == 0:
        return 1
    power = 1
    for i in range(e):
        power *= b
    return power
    print(f"{base}^{expo} = {power}")


def calc_expo_while(b, e):
    if e == 0:
        return 1
    power = 1
    count = 0
    while count < e:
        power *= b
        count += 1
    return power


result1 = calc_expo_for(base, expo)
result2 = calc_expo_while(base, expo)

print(f"{base}^{expo}={result1}")
print(f"{base}^{expo}={result2}")
