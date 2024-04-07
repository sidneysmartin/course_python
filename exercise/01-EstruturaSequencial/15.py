"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas
no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados
11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos
dê:
a. salário bruto.
b. quanto pagou ao INSS.
c. quanto pagou ao sindicato.
d. o salário líquido.
e. calcule os descontos e o salário líquido, conforme a tabela abaixo:
e. + Salário Bruto : R$
f. - IR (11%) : R$
g. - INSS (8%) : R$
h. - Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
"""

import locale

locale.setlocale(locale.LC_MONETARY, "pt_BR.UTF-8")
hourlyWage = float(input("Informe o valor da hora trabalhada: "))
hoursWorked = float(input("Informe o total de horas trabalhadas: "))
totalWage = hourlyWage * hoursWorked
incomeTax = totalWage * 0.11
inss = totalWage * 0.08
laborUnion = totalWage * 0.05
tax = incomeTax + inss + laborUnion
finalWage = totalWage - tax
print(f"Salário bruto....: R$ ", locale.currency(totalWage, grouping=True))
print(f"Imposto de Renda.: R$ ", locale.currency(incomeTax, grouping=True))
print(f"Imposto de INSS..: R$ ", locale.currency(inss, grouping=True))
print(f"Sindicato........: R$ ", locale.currency(laborUnion, grouping=True))
print(f"Descontos........: R$ ", locale.currency(tax, grouping=True))
print(f"Salário final....: R$ ", locale.currency(finalWage, grouping=True))


 