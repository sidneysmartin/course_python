"""
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a
temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
"""
tempFahrenheit = float(input("Informe a temperatura em Fahrenheit: "))
tempCelsius = 5 * ((tempFahrenheit - 32) / 9)

print(f"A temperatura em Fahrenheit é {round(tempFahrenheit,2)}ºF")
print(f"A temperatura em Celsius é {round(tempCelsius,2)}ºC")
