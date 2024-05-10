"""
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
"""

countryA = 80000
countryB = 200000
growthA = 0.03
growthB = 0.015
years = 0

while countryA < countryB:
  countryA += (countryA * growthA) 
  countryB += (countryB * growthB) 
  years += 1

print("População País A ultrapassa o País B %d"%years + " anos.")