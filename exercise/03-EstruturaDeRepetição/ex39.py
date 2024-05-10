"""
Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.
"""

students = {}

for i in range(10):
    print("\nDigitação número ", i + 1, " :")
    student_id = int(input("Digite o número do aluno: "))
    while student_id in students:
        print("[Este número ja foi digitado]")
        student_id = int(input("Digite outro número: "))
    student_height = float(input("Digite a altura do aluno: "))
    students[student_id] = student_height

# Obtém o id e a altura do aluno mais alto e mais baixo
id_lowest = min(students, key=students.get)
id_highest = max(students, key=students.get)

print("Aluno mais baixo \nNúmero: ", id_lowest, "\nAltura: ", students[id_lowest])
print("Aluno mais alto \nNúmero: ", id_highest, "\nAltura: ", students[id_highest])

