""" 
Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, 
com a intenção de fazer um levantamento nas sucatas encontradas nesta área. 
A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, 
testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
Foi requisitado que você desenvolva um programa para registrar este levantamento. 
programa deverá receber um número indeterminado de entradas, cada uma contendo: 
um número de identificação do mouse o tipo de defeito:
necessita da esfera;
necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou 
inutilizado Uma identificação igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:
Quantidade de mouses: 100

Situação                        Quantidade              Percentual
1- necessita da esfera                  40                     40%
2- necessita de limpeza                 30                     30%
3- necessita troca do cabo ou conector  15                     15%
4- quebrado ou inutilizado              15                     15%
"""

def get_problem():
    while True:
        problem = int(input('Digite o número do problema: '))
        if 0 <= problem <= 4:
            return problem
        print('Número do problema inválido.')

def get_problems():
    problems = [0] * 4
    while True:
        identification = int(input('Identificação: '))
        if identification == 0:
            break
        problem = get_problem()
        problems[problem - 1] += 1
    return problems

def print_report(problems):
    print('Situação                        Quantidade              Percentual')
    total = sum(problems)
    situations = ['necessita da esfera', 'necessita de limpeza', 'necessita troca do cabo ou conector', 'quebrado ou inutilizado']
    for i, (situation, problem) in enumerate(zip(situations, problems), start=1):
        percentage = (100 * problem) / total
        print(f'{i} - {situation} - {problem} - {percentage:.2f}%')

def main():
    print('''1- necessita da esfera
    2- necessita de limpeza
    3- necessita troca do cabo ou conector
    4- quebrado ou inutilizado ''')
    problems = get_problems()
    print_report(problems)

if __name__ == "__main__":
    main()
