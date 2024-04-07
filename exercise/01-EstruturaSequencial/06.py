"""
Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
"""
import math

radius = float(input("Informe raio: "))

area = round( math.pi * (radius**2),2)
print(f"Raio é: {radius}.")
print(f"Área é: {area}.")
