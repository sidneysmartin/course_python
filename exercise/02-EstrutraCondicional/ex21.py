"""
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário 
a valor do saque e depois informar quantas notas de cada valor serão fornecidas. 
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. 
O programa não deve se preocupar com a quantidade de notas existentes na máquina.
a. Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
b. Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
"""

def sacar_notas(valor):
    """
    Calcula o número de cédulas para um valor de saque dado.
    Args:
        valor (int): O valor a ser sacado.
    Returns:
        str: Uma string formatada mostrando a quantidade de cada tipo de cédula.
    """
    cem = valor // 100
    valor -= cem * 100
    cinquenta = valor // 50
    valor -= cinquenta * 50
    dez = valor // 10
    valor -= dez * 10
    cinco = valor // 5
    valor -= cinco * 5
    um = valor

    result = ""
    if cem > 0:
        result += f"{cem} nota(s) de cem\n"
    if cinquenta > 0:
        result += f"{cinquenta} nota(s) de cinquenta\n"
    if dez > 0:
        result += f"{dez} nota(s) de dez\n"
    if cinco > 0:
        result += f"{cinco} nota(s) de cinco\n"
    if um > 0:
        result += f"{um} nota(s) de um\n"

    return result.strip()

def main():
    valor = int(input("Digite o valor a ser sacado (entre 10 e 600): "))
    if 10 <= valor <= 600:
        print(sacar_notas(valor))
    else:
        print("Valor inválido!")

if __name__ == "__main__":
    main()
