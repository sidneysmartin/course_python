"""
Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores.
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
"""
import os
total_voter = int(input("Total de eleitores: "))
candidate_A = 0
candidate_B = 0
candidate_C = 0
discard = 0
white = 0
i = 0

while i <= total_voter:
    print("Candidato A: 1\nCandidato B: 2\nCandidato C: 3")
    vote = int(input(f'{i}º eleitor: '))
    if vote == 1:
        candidate_A += 1
    elif vote == 2:
        candidate_B += 1
    elif vote == 3:
        candidate_C += 1
    elif vote == 0:
        white += 1
    else:
        discard += 1
    i += 1
    os.system('clear')


if candidate_A > candidate_B and candidate_A > candidate_C:
    elected = "Candidato A"
elif candidate_B > candidate_A and candidate_B > candidate_C:
    elected = "Candidato B"
elif candidate_C > candidate_A and candidate_C > candidate_B:
    elected = "Candidato C"


print("* * * * Votos Totais * * * *")
print(f"Candidato A....: {candidate_A}")
print(f"Candidato B....: {candidate_B}")
print(f"Candidato C....: {candidate_C}")
print(f"Votos Brancos..: {white}")
print(f"Votos Nulos....: {discard}")
print(f"Eleito.........: {elected}")
