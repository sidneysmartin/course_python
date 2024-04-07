"""
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                   Até 5 kg Acima de 5 kg
- File Duplo R$ 4,90 por kg R$ 5,80 por kg
- Alcatra R$ 5,90 por kg R$ 6,80 por kg 
- Picanha R$ 6,90 por kg R$ 7,80 por kg
Para atender a todos os clientes, cada cliente poderá levar
 apenas um dos tipos de carne da promoção, porém não há limites 
 para a quantidade de carne por cliente. Se compra for feita no 
 cartão Tabajara o cliente receberá ainda um desconto de 5% sobre 
 o total da compra. Escreva um programa que peça o tipo e a quantidade 
 de carne comprada pelo usuário e gere um cupom fiscal, 
 contendo as informações da compra: tipo e quantidade de carne, 
 preço total, tipo de pagamento, valor do desconto e valor a pagar.
"""
def calcular_valor_carne(tipo, quantidade, resposta):
    precos = {
        1: {"nome": "File Duplo", "ate_5kg": 4.9, "acima_5kg": 5.8},
        2: {"nome": "Alcatra", "ate_5kg": 5.9, "acima_5kg": 6.8},
        3: {"nome": "Picanha", "ate_5kg": 6.9, "acima_5kg": 7.8},
    }

    if tipo not in precos:
        print("Tipo de carne inválido. Escolha entre 1, 2 ou 3.")
        return

    carne = precos[tipo]
    price = carne["ate_5kg"] * quantidade if quantidade <= 5 else carne["acima_5kg"] * quantidade

    if resposta == 1:
        r = "SIM"
        desconto = (price * 5) / 100
        total = price - desconto
    else:
        r = "NÃO"
        total = price

    print("\n***************************CUPOM FISCAL**************************************")
    print(f"* Carne.......................................................... {carne['nome']}")
    print(f"* Quantidade..................................................... {quantidade} KG")
    print(f"* Preço......................................................... R$ {price:.2f}")
    print(f"* Cartão Tabajara................................................ {r}")
    print(f"* Total com desconto............................................ R$ {total:.2f}")
    print("******************************************************************************")

# Exemplo de uso:
tipo_carne_comprada = int(input("Digite o tipo (1-File Duplo, 2-Alcatra, 3-Picanha): "))
quantidade_comprada = float(input("Digite a quantidade comprada (em KG): "))
resposta_cartao = int(input("A compra será realizada com cartão Tabajara? (1 para SIM, 2 para NÃO): "))

calcular_valor_carne(tipo_carne_comprada, quantidade_comprada, resposta_cartao)
