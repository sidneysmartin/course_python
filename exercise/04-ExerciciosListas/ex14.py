""" 
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
a-"Telefonou para a vítima?"
b-"Esteve no local do crime?"
c-"Mora perto da vítima?"
d-"Devia para a vítima?"
e-"Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação 
sobre a participação da pessoa no crime. Se a pessoa responder positivamente 
a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 
5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""

question = {
    1: "Telefonou para a vítima?",
    2: "Esteve no local do crime?",
    3: "Mora perto da vítima?",
    4: "Devia para a vítima?",
    5: "Já trabalhou com a vítima?"
}

count_answer = 0

for i in range(1, 6):
    answer = input(f"{question[i]} [S / N]: ").upper()
    if answer == "S":
        count_answer += 1
if count_answer < 2:
    print("Inocente")
elif count_answer == 2:
    print("Suspeita")
elif count_answer == 3 or count_answer == 4:
    print("Cúmplice")
elif count_answer == 5:
    print("Assassino")
