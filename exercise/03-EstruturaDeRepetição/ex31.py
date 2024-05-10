""" 
O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:
Lojas Tabajara 
Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 9.00
Dinheiro: R$ 20.00
Troco: R$ 11.00
...
"""
import time

def calcular_compra():
    precos_produtos = []
    preco_produto = True
    n_produto = 1

    while preco_produto != 0:
        print(f"Produto n° {n_produto}")
        preco_produto = float(input("Digite o preço do produto: "))
        if preco_produto != 0:
            precos_produtos.append(preco_produto)
            n_produto += 1

    return precos_produtos

def receber_pagamento(total):
    print(f"Total: R$ {total}")
    dinheiro = float(input("Digite a quantia que irá pagar: "))

    while dinheiro < total:
        dinheiro = float(input(f"Digite a quantia que irá pagar [maior que o total da compra R$ {total}] : "))

    return dinheiro

def main():
    while True:
        precos_produtos = calcular_compra()
        total = sum(precos_produtos)
        dinheiro = receber_pagamento(total)

        print(f"Dinheiro: R$ {dinheiro}")
        print(f"Troco: R$ {dinheiro - total}")
        print("\nPróxima compra em 3 segundos...")
        time.sleep(3)
        print("\n" * 5)

if __name__ == "__main__":
    main()
