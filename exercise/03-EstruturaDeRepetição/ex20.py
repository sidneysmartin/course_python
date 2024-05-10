"""
Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.
"""
amount = int(input('Digite a quantidade: '))

for i in range(1, amount + 1):

    while True:
        number = int(input('Digite o %dº número: ' % i))

        if number < 16:
            break
        else:
            print('Número inválido. Digito novamente.')

    count = 1
    factorial = 1
    while count <= number:
        factorial *= count
        count += 1

    print(f"{factorial}!")
