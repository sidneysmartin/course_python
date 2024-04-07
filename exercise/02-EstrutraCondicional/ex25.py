"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
. "Telefonou para a vítima?"
a. "Esteve no local do crime?"
b. "Mora perto da vítima?"
c. "Devia para a vítima?"
d. "Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação 
sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela
deve ser classificada como "Suspeita", 
entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
Caso contrário, ele será classificado como "Inocente".
"""
def main():
    questions = [
        "Telefonou para a vítima?",
        "Esteve no local do crime?",
        "Mora perto da vítima?",
        "Devia para a vítima?",
        "Já trabalhou com a vítima?"
    ]

    results = {
        2: "Suspeita",
        3: "Cúmplice",
        4: "Cúmplice",
        5: "Assassino"
    }

    counter = 0
    for i in range(len(questions)):
        answer = input(f"{questions[i]} [S / N]: ").upper()
        if answer == "S":
            counter += 1

    print(results.get(counter, "Inocente"))

if __name__ == "__main__":
    main()
