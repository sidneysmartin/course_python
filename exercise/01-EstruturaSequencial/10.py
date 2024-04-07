"""
Faça um Programa que peça a temperatura em graus Celsius, 
transforme e mostre em graus Fahrenheit.
F =((Cº * 9/5).
"""
tempCelsius = float(input("Informe a temperatura em Celsius: "))
tempFahrenheit = (tempCelsius * 9 / 5) + 32
print(f"A temperatura em Celsius é {round(tempCelsius,2)}ºC")
print(f"A temperatura em Fahrenheit é {round(tempFahrenheit,2)}ºF")
