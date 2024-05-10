""" 
Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
Os juros e a quantidade de parcelas seguem a tabela abaixo:
Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
1       0
3       10
6       15
9       20
12      25
Exemplo de saída do programa:
Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
R$ 1.000,00     0               1                       R$  1.000,00
R$ 1.100,00     100             3                       R$    366,00
R$ 1.150,00     150             6                       R$    191,67
"""
print("\n" * 5)
debt = float(input("Digite o valor da divida: "))
installments = [1, 3, 6, 9, 12]
interest_rates = [1, 1.10, 1.15, 1.20, 1.25]

print("\n" * 5)
print("Valor da divida: ", end="  ")
print("Valor do juros: ", end="  ")
print("Quantidade de parcelas: ", end="  ")
print("Valor da parcela: ")

for i in range(5):
    interest = interest_rates[i]
    installment = installments[i]

    interest_value = debt * (interest - 1)
    debt_with_interest = debt * interest
    installment_value = debt_with_interest / installment

    print("R$", round(debt_with_interest, 2), end="            ")
    print(round(interest_value, 2), end="                  ")
    print(installment, end="                        ")
    print("R$ ", round(installment_value, 2))
