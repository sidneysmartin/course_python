"""
Faça um Programa para uma loja de tintas. 
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados 
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
o Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
o comprar apenas latas de 18 litros;
o comprar apenas galões de 3,6 litros;
o misturar latas e galões, de forma que o desperdício de tinta seja menor.
 Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""

tamanho = float(input('Entre com o tamanho da área: '))

litros = tamanho / 6
latas = litros / 18

if latas % 18 != 0:
    latas += 1
price = latas * 80

galoes = litros / 3.6
if galoes % 3.6 != 0:
    galoes += 1
price2 = galoes * 25

# mistura de latas e galoes
mistura_lata = int(litros / 18.0)
mistura_Gal = int((litros - (mistura_lata * 18)) / 3.6)

if litros - (mistura_lata * 18) % 3.6 != 0:
    mistura_Gal += 1

print('Apenas latas de 18 litros: %d' % latas, 'preço: %d' % price)
print('Apenas galões de 3.6 litros: %d' % galoes, 'preço: %d' % price2)
print('Mistura: %d latas e %d galoes = %.2f' % (
    mistura_lata, mistura_Gal, ((mistura_lata * 80) + (mistura_Gal * 25))))