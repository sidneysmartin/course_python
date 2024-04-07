"""
Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu
peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
"""
height = float(input("Informe a altura: "))
weight = (72.7 * height) - 58
print(f"Altura.....: {height}")
print(f"Peso.......: {weight}")