"""
Faça um programa que mostre os n termos da Série a seguir:
  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
  Imprima no final a soma da série.
"""
numerator_list = list(range(1, 11))
denominator_list = list(range(1, 21, 2))

print("S = ", end = "")
for i in range(len(numerator_list) - 1):
    print(numerator_list[i], "/", denominator_list[i], " + ", end="")

print(numerator_list[-1], "/", denominator_list[-1], " = ", sum(numerator_list), "/", sum(denominator_list))
