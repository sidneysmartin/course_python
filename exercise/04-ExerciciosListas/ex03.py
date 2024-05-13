# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
grades = []
sum_grades = 0
avg_grades = 0
for i in range(4):
    grade = grades.append(float(input(f"Digite a {i+1}º nota: ")))
    sum_grades += grades[i]
avg_grades = sum_grades / len(grades)
j = 0
while j < len(grades):
    print(f"Nota {j+1}: {grades[j]}")
    j += 1

print(f"Média: {avg_grades:.2f}")
