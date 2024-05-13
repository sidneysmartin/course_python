""" 
Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
O resultado do atleta será determinado pela média dos cinco valores restantes. 
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas 
pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. 
O programa deve ser encerrado quando não for informado o nome do atleta. ,
A saída do programa deve ser conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo
 
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m
"""

athlete = input("Nome do atleta: ")
jumps = []

for i in range(5):
    slope = float(input(f"{i+1}° salto: "))
    jumps.append(slope)

average = sum(jumps) / len(jumps) if len(jumps) > 0 else 0

print(f"Resultados")
print(f"Atleta: {athlete}")
print(f"Saltos: {', '.join(map(str, jumps))}")
print(f"Média dos saltos: {average:.2f} m")
