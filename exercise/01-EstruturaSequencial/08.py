"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas
no mês. Calcule e mostre o total do seu salário no referido mês.
"""
import locale

locale.setlocale(locale.LC_MONETARY, "pt_BR.UTF-8")
hourlyWage = float(input("Informe o valor da hora trabalhada: "))
hoursWorked = float(input("Informe o total de horas trabalhadas: "))
totalWage = hourlyWage * hoursWorked
print(f"O valor do salário é: R$ {totalWage}")
print(f"Horas trabalhadas: {hoursWorked}.")
print("O valor do salário é: R$", locale.currency(totalWage, grouping=True))
