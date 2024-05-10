""" 
Em uma eleição presidencial existem quatro candidatos. 
Os votos são informados por meio de código. Os códigos utilizados são:
1 , 2, 3, 4  - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.
"""
candidates = {1: 'Candidato 1', 2: 'Candidato 2', 3: 'Candidato 3', 4: 'Candidato 4', 5: 'Nulo', 6: 'Branco'}
votes = []

while True:
    vote = int(input("Digite o seu voto (0 para sair): "))
    if vote == 0:
        break
    elif vote not in candidates:
        print("[Voto invalido.]")
        continue
    votes.append(vote)

print("\n" * 2)
for candidate_code, candidate_name in candidates.items():
    print(f"Votos para {candidate_name}: {votes.count(candidate_code)}")

total_votes = len(votes)
percentage_null = (votes.count(5) / total_votes) * 100
percentage_white = (votes.count(6) / total_votes) * 100

print(f"\nPorcentagem Nulos: {round(percentage_null, 2)}%")
print(f"Porcentagem Brancos: {round(percentage_white, 2)}%")
