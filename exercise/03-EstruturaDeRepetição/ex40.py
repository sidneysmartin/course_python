""" 
Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
a - Código da cidade
b - Número de veículos de passeio (em 1999);
c - Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
d - Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
e - Qual a média de veículos nas cinco cidades juntas;
f - Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
"""
city_codes = []
vehicle_numbers = []
accident_numbers = []
accidents_2000 = []

for i in range(5):
    print("\nCity number ", i + 1)
    city_code = int(input("Digite o código da Cidade: "))
    while city_code in city_codes:
        print("[Este código ja foi digitado]")
        city_code = int(input("Digite outro código: "))

    accident_number = int(input("Informe o número de acidentes: "))
    vehicle_number = int(input("Informe o número de veículos: "))

    if vehicle_number > 2000:
        accidents_2000.append(accident_number)
        accident_numbers.append(accident_number)
    else:
        accident_numbers.append(accident_number)

    vehicle_numbers.append(vehicle_number)
    city_codes.append(city_code)

index_least_accidents = accident_numbers.index(min(accident_numbers))
index_most_accidents = accident_numbers.index(max(accident_numbers))

print("\nMenos acidentes\nNúmeros de acidentes: ", min(accident_numbers),
      "\nCódigo da cidade: ", city_codes[index_least_accidents])
print("\nMais acidentes\nNúmeros de acidentes: ", max(accident_numbers),
      "\nCódigo da cidade: ", city_codes[index_most_accidents])

average_vehicles = sum(vehicle_numbers) / len(vehicle_numbers)
print("\nNúmero médio de veículos nas 5 cidades: ", average_vehicles)

average_accidents_2000 = sum(accidents_2000) / len(accidents_2000)
print("\nNúmero médio de acidentes em cidades com menos de 2.000 veículos: ",
      average_accidents_2000)
