""" 
Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média). Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são ordenados. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Melhor salto:  6.5 m
Pior salto: 5.3 m
Média dos demais saltos: 5.9 m

Resultado final:
Rodrigo Curvêllo: 5.9 m
"""
athlete_number = 1
while True:
    print("\n" * 5)
    print("Atleta n°", athlete_number)
    athlete_name = input("Digite o nome do atleta: ")
    if athlete_name == '':
        break

    jumps = []
    print("\n" * 3)
    for i in range(1, 6):
        print("Salto n° ", i)
        jump_distance = float(input("Digite a distancia do salto: "))
        jumps.append(jump_distance)

    print("Atleta: ", athlete_name)
    for i, jump in enumerate(jumps, start=1):
        print(i, "° salto : ", jump, " m")

    print("Melhor salto: ", max(jumps), " m")
    print("Pior salto: ", min(jumps), " m")

    jumps.remove(max(jumps))
    jumps.remove(min(jumps))
    average = sum(jumps) / len(jumps)
    print("Media dos demais saltos: ", round(average, 2))
    print("Resultado Final: \n", athlete_name, " : ", round(average, 2))
    athlete_number += 1
