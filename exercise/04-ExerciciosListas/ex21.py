""" 
Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:
a-O modelo do carro mais econômico;
b-Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa.
Comparativo de Consumo de Combustível

Veículo 1
Nome: fusca
km por litro: 7
Veículo 2
Nome: gol
km por litro: 10
Veículo 3
Nome: uno
km por litro: 12.5
Veículo 4
Nome: Vectra
km por litro: 9
Veículo 5
Nome: Peugeout
km por litro: 14.5

Relatório Final
 1 - fusca           -    7.0 -  142.9 litros - R$ 321.43
 2 - gol             -   10.0 -  100.0 litros - R$ 225.00
 3 - uno             -   12.5 -   80.0 litros - R$ 180.00
 4 - vectra          -    9.0 -  111.1 litros - R$ 250.00
 5 - peugeout        -   14.5 -   69.0 litros - R$ 155.17
O menor consumo é do peugeout.
"""


def get_vehicle_info():
    models = []
    consumptions = []
    for i in range(1, 6):
        print(f'Veículo {i}')
        models.append(input('Nome: '))
        consumptions.append(float(input('km por litro: ')))
    return models, consumptions


def calculate_costs(models, consumptions):
    costs = [1000 / consumption for consumption in consumptions]
    spents = [cost * 2.25 for cost in costs]
    return costs, spents


def find_most_efficient(models, costs):
    min_cost = min(costs)
    min_index = costs.index(min_cost)
    return models[min_index]


def print_report(models, consumptions, costs, spents):
    print('Relatório Final')
    for model, consumption, cost, spent in zip(models, consumptions, costs, spents):
        print(f'{model} - {consumption:.1f} - {cost:.1f} litros - R$ {spent:.2f}')
    most_efficient = find_most_efficient(models, costs)
    print(f'O menor consumo é do {most_efficient}.')


def main():
    models, consumptions = get_vehicle_info()
    costs, spents = calculate_costs(models, consumptions)
    print_report(models, consumptions, costs, spents)


if __name__ == "__main__":
    main()
