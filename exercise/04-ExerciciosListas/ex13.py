""" 
Faça um programa que receba a temperatura média de cada mês do ano 
e armazene-as em uma lista. Após isto, calcule a média anual das 
temperaturas e mostre todas as temperaturas acima da média anual, 
e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
"""
import random
anual_temps = {
    'months': ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
    'temps': []
}
print("\n\nTemperaturas do ano:")

sum_temps = 0
for i in range(12):
    temp = random.uniform(0.0, 50.0)
    anual_temps['temps'].append(temp)
    sum_temps += temp

avg_temps = sum_temps / 12
for i in range(12):
    print(f"{anual_temps['months'][i]}: {anual_temps['temps'][i]:.2f}°C")
print(f"\nMedia anual: {
      avg_temps:.2f}°C\nTemperaturas acima da média anual: {avg_temps:.2f}°C")
for i in range(12):
    if anual_temps['temps'][i] > avg_temps:
        print(f"{anual_temps['months'][i]}: {anual_temps['temps'][i]:.2f}°C")
