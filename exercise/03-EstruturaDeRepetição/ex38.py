""" 
Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
a - Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
b - Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
c - A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.
"""
from datetime import datetime

now = datetime.now()
year = now.year
wage = float(input("Salário inicial: "))
print(f"Salário inicial...: R$ {wage:.2f}")

percent_increase = 1.5 / 100  # Inicialmente 1.5%
for i in range(1996, year + 1):
    if i > 1996:
        percent_increase *= 2  # Dobra o percentual de aumento a cada ano após 1996
    wage += wage * percent_increase

print(f"Salário atual.....: R$ {wage:.2f}")
