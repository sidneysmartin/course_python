"""
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
"""
countryA = float(input("Informe a população do país A: "))
countryB = float(input("Informe a população do país B: "))
years = 0 

growthA = float(input("Informe a taxa de crescimento da população A em %: "))
growthB = float(input("Informe a taxa de crescimento da população B em %: "))

while countryA < countryB:
  countryA += countryA * (growthA * 100)
  countryB += countryB * (growthB * 100)
  years +=1
  
print(f"População país A - {round(countryA)} habitantes.")
print(f"População país B - {round(countryB)} habitantes.")
print(f"Levará {years} anos para a população A irá superar a população B")