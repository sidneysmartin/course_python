""" 
Faça um programa que calcule o mostre a média aritmética de N notas.
"""
number = int(input("Quantas notas deseja informar? "))
sum, avg = 0, 0
for i in range(number):
    value = float(input(f"{i+1}º valor: "))
    sum += value
avg = sum / number
print(f"Soma dos {number} valores informados: {
      sum:.2f}\nA média dos valores informados: {avg:.2f}")
