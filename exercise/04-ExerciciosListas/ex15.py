"""
Faça um programa que leia um número indeterminado de valores, correspondentes a notas,
encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado).
Após esta entrada de dados, faça:
a-Mostre a quantidade de valores que foram lidos;
b-Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
c-Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
d-Calcule e mostre a soma dos valores;
e-Calcule e mostre a média dos valores;
f-Calcule e mostre a quantidade de valores acima da média calculada;
g-Calcule e mostre a quantidade de valores abaixo de sete;
h-Encerre o programa com uma mensagem;
"""

grades = []
grade = 0

while grade != -1:
    grade = float(input("Digite uma nota ou -1 para encerrar: "))
    if grade != -1:
        grades.append(grade)


amount = len(grades)
sum = sum()
avg_grades = sum / amount if amount > 0 else 0
higher_than_avg = len([x for x in grades if x > avg_grades])
lower_than_seven = len([x for x in grades if x < 7])

print(f"\nQuantidade de notas: {amount}")
print(f"b) Valores na ordem informada: {' '.join(map(str, grades))}")

print("c) Valores na ordem inversa: ")

for grade in range(len(grades) - 1, -1, -1):
    print(grades[grade])

print(f"d) Soma dos valores: {sum}")
print(f"e) Média dos valores: {avg_grades}")
print(f"f) Quantidade de valores acima da media {higher_than_avg}")
print(f"g) Quantidade de valores abaixo de 7: {lower_than_seven}")

print("h) Encerrando o programa...")
