""" 
Faça um Programa que peça as quatro notas de 10 alunos, 
calcule e armazene num vetor a média de cada aluno, 
imprima o número de alunos com média maior ou igual a 7.0.
"""
import os
students = {
    "name": [],
    "grades": [],
    "average": [],
}
total_students = 10

for i in range(total_students):
    os.system("clear")
    students["name"].append(input(f"Digite o {i+1}º nome: "))

    student_grades = []
    for j in range(4):
        student_grades.append(
            float(input(f"Informe a {j+1}º nota para ({students['name'][i]}): ")))

    average = sum(student_grades) / 4  # Calculo da media
    students["average"].append(average)  # Adiciona a média à lista
    students["grades"].append(student_grades)

# Correção: A contagem deve ser feita após todas as médias serem calculadas
count_passing = sum(1 for avg in students["average"] if avg >= 7)

print(f"Número de alunos com média maior ou igual a 7.0: {count_passing}")

# Correção: A verificação deve ser feita após todas as médias serem calculadas
for i in range(len(students["name"])):
    if students["average"][i] >= 7:
        print(f"Estudante: {students['name'][i]}, Notas: {
              students['grades'][i]}, Média: {students['average'][i]}")
