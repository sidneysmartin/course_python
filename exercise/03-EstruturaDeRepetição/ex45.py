""" 
Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões,
o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar 
com o gabarito da prova e assim calcular o total de acertos e a nota 
(atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser 
feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem 
respondido informar:
a - Maior e Menor Acerto;
b - Total de Alunos que utilizaram o sistema;
c - A Média das Notas da Turma.
Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A
Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.
"""
answer_key = []
student_answers = []
scores = []

print("\nProfessor: ")
for i in range(10):
    print("Questões: ", i + 1)
    correct_answer = input("Escolha a resposta: ")
    answer_key.append(correct_answer)

student_number = 1
continue_input = 's'
while continue_input.lower() != 'n':
    print("\n" * 5)
    print("Número do estudante", student_number, ":")
    student_answers.clear()
    for i in range(10):
        print("Questões: ", i + 1)
        student_answer = input("Escola a resposta: ")
        student_answers.append(student_answer)
    score = sum([student_answer == correct_answer for student_answer,
                correct_answer in zip(student_answers, answer_key)])
    scores.append(score)
    continue_input = input("Deseja entrar outro estudante? [s/n] : ")
    student_number += 1

print(len(scores), "students used the system")
print("\nThe highest score was: ", max(scores))
print("The lowest score was: ", min(scores))
print("The average score of the class was:", sum(scores) / len(scores))
print(scores)
