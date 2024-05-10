"""
Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar 
se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; 
e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
"""
people = int(input("Quantas pessoas deseja informar? "))
sum, avg = 0, 0
for i in range(people):
    age = int(input(f"{i+1}º pessoa: "))
    sum += age
avg = sum / people
if avg < 25:
    print(f"{avg:.2f} - Turma jovem")
elif avg < 60:
    print(f"{avg:.2f} - Turma adulta")
else:
    print(f"{avg:.2f} - Turma idosa")
