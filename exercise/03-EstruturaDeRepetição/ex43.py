""" 
O cardápio de uma lanchonete é o seguinte:
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburger   104     R$ 1,30
Refrigerante    105     R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. 
Considere que o cliente deve informar quando o pedido deve ser encerrado.
"""
menu = {
    100: {'item': 'Cachorro Quente', 'price': 1.20},
    101: {'item': 'Bauru Simples', 'price': 1.30},
    102: {'item': 'Bauru com ovo', 'price': 1.50},
    103: {'item': 'Hamburger', 'price': 1.20},
    104: {'item': 'CheeseBurger', 'price': 1.30},
    105: {'item': 'Refrigerante', 'price': 1.0}
}

orders = []
order_number = 1

while True:
    print("\nPedido n°", order_number)
    code = int(input("Digite o código do alimento: "))

    if code == 0:
        break
    elif code not in menu:
        print("[Este código não corresponde a nenhum alimento.]")
        continue

    quantity = int(input("Digite a quantidade: "))
    order_value = menu[code]['price'] * quantity
    orders.append(order_value)
    order_number += 1

print("\n" * 2)
for i, order in enumerate(orders, start=1):
    print(f"Pedido n° {i} = R$ {round(order, 2)}")
print("Total: R$ ", round(sum(orders), 2))
