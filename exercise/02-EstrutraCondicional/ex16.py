"""
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O
 programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
a. Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
b. Se o delta calculado for negativo, a equação não possui raízes reais. Informe ao usuário e encerre o programa;
c. Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
d. Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
"""
valueA = int(input("Digite o valor de A: "))
valueB = int(input("Digite o valor de B: "))
valueC = int(input("Digite o valor de C: "))

delta = valueB**2 - 4*valueA*valueC

if valueA == 0:
  print("A equação não é do segundo grau")
else:
  if delta < 0:
    print("A equação não possui raízes reais")
  elif delta == 0:
    print("A equação possui apenas uma raiz real")
  else:
    print("A equação possui duas raízes reais")