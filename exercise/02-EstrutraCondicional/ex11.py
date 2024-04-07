"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus 
colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
o salários até R$ 2800,00 (incluindo) : aumento de 20%
o salários entre R$ 2800,00 e R$ 7000,00 : aumento de 15%
o salários entre R$ 7000,00 e R$ 15000,00 : aumento de 10%
o salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o o salário antes do reajuste;
o o percentual de aumento aplicado;
o o valor do aumento;
o o novo salário, após o aumento.

"""

salary = float(input("Digite o valor do seu salário: "))
newSalary = 0
percentIncrease = 0
if salary <= 2800:
  percentIncrease = 0.20
  newSalary = salary + (salary * percentIncrease)

elif salary > 2800 and salary <= 7000:
  percentIncrease = 0.15
  newSalary = salary + (salary * percentIncrease)
elif salary > 7000 and salary <= 15000:
  percentIncrease = 0.10
  newSalary = salary + (salary * percentIncrease) 
else:
  percentIncrease = 0.05
  newSalary = salary + (salary * percentIncrease)

print(f"\nSeu salário antes do reajuste é de R$ {salary}.")
print(f"O percentual de aumento aplicado foi de {percentIncrease * 100}%.")
print(f"O valor do aumento foi de R$ {salary * 0.20}.")
print(f"Seu novo salário é de R$ {newSalary}.")