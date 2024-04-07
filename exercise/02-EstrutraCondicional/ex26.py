"""
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
. Álcool:
a. até 20 litros, desconto de 3% por litro
b. acima de 20 litros, desconto de 5% por litro
c. Gasolina:
d. até 20 litros, desconto de 4% por litro
e. acima de 20 litros, desconto de 6% por litro 
Escreva um algoritmo que leia o número de litros vendidos, 
o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), 
calcule e imprima o valor a ser pago pelo cliente sabendo-se
 que o preço do litro da gasolina é R$ 2,50 o preço do 
 litro do álcool é R$ 1,90.
"""

def main():
    try:
        liters = float(input("Informe a quantidade que deseja abastecer: "))
        fuel = input("Combustível - (A - Álcool | G - Gasolina): ").upper()

        priceGas = 2.5
        priceAl = 1.9

        def calc_gasoline(liters):
            return 0.03 if liters < 20 else 0.05

        def calc_alcohol(liters):
            return 0.04 if liters < 20 else 0.06

        if fuel == "A":
            price_complete = liters * priceAl
            discount = calc_alcohol(liters)
            final_price = price_complete - price_complete * discount
            print("Álcool")
        elif fuel == "G":
            price_complete = liters * priceGas
            discount = calc_gasoline(liters)
            final_price = price_complete - price_complete * discount
            print("Gasolina")
        else:
            print("Informe um combustível válido.")
            return

        print(f"Total de Litros.....: {liters:.2f}l")
        print(f"Preço completo......: R$ {price_complete:.2f}")
        print(f"Preço c/ desconto...: R$ {final_price:.2f}")

    except ValueError:
        print("Informe uma quantidade válida.")

if __name__ == "__main__":
    main()
