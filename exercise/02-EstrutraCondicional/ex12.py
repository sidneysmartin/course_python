"""
Faça um programa para o cálculo de uma folha de pagamento, 
sabendo que os descontos são do Imposto de Renda, 
que depende do salário bruto (conforme tabela abaixo) e 3% 
para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
 mas não é descontado (é a empresa que deposita).
O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

o Desconto do IR:
o Salário Bruto até 9000 (inclusive) - isento
o Salário Bruto até 15000 (inclusive) - desconto de 5%
o Salário Bruto até 25000 (inclusive) - desconto de 10%
o Salário Bruto acima de 25000 - desconto de 20% Imprima na tela as informações, 

"""
salary = float(input("Digite o valor do seu salário: "))
hours = float(input("Digite a quantidade de horas trabalhadas no mês: "))
grossSalary = salary * hours
syndicate = grossSalary * 0.03
calcFGTS = grossSalary * 0.11
def calculateIR(grossSalary):
  if grossSalary <= 900:
    salaryIR = 0
  elif grossSalary > 900 and grossSalary <= 1500:
    salaryIR = grossSalary * 0.05
  elif grossSalary > 1500 and grossSalary <= 2500:
    salaryIR = grossSalary * 0.1
  elif grossSalary > 2500:
    salaryIR = grossSalary * 0.2
  return salaryIR

salaryIR = calculateIR(grossSalary)
discount =  syndicate + calcFGTS + salaryIR
finalSalary = grossSalary - discount
print(f"\nSeu salário bruto é de R$ {grossSalary}.")
print(f"Seu sindicato é de R$ {syndicate}.")
print(f"Seu FGTS é de R$ {calcFGTS}.")
print(f"Seu imposto de renda é de R$ {salaryIR}.")
print(f"Seu salário liquido é de R$ {finalSalary}.")