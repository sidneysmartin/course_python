value1 = int(input("Digite 1º valor: "))
value2 = int(input("Digite 2º valor: "))

sum = value1 + value2
sub = value1 - value2
mult = value1 * value2
div = value1 / value2
expo = value1 ** value2
print(f"A soma dos valores é: {sum}")
print("A subtração dos valores é: ", sub)
print(f"A multiplicação dos valores é: {mult}")
print(f"A divisão dos valores é: {format(div, '.2f')}")
print(value1, " ** ", value2, " = ", expo)