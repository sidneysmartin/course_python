""" 
Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine
quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
"""
import random

students = {
    'age': [],
    'height': [],
    'names': ['João', 'Maria', 'Pedro', 'Ana', 'Carlos', 'Fernanda', 'Bruna'],
    'surnames': ['Silva', 'Santos', 'Oliveira', 'Pereira', 'Almeida', 'Martins']
}

for i in range(30):
    students['age'].append(random.randint(0, 25))
    students['height'].append(random.uniform(0.3, 2.4))
    students['names'].append(students['names'][random.randint(0, 6)])
    students['surnames'].append(students['surnames'][random.randint(0, 5)])

count_loss13 = 0

for i in range(30):
    print(f"{students['names'][i]} {students['surnames'][i]} Idade: {
          students['age'][i]} | Altura: {students['height'][i]:.2f}")

for i in range(30):
    if students['age'][i] > 13 and students['height'][i] < sum(students['height']) / 30:
        count_loss13 += 1

print(f"Alunos com mais de 13 anos e altura inferior a media: {count_loss13}")
