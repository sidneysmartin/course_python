""" 
Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:
Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----
Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
"""
def get_option():
    while True:
        option = int(input('Digite a opção: '))
        if 0 <= option <= 6:
            return option
        print('Opção inválida.')

def get_votes(options):
    votes = [0] * len(options)
    while True:
        option = get_option()
        if option == 0:
            break
        votes[option - 1] += 1
    return votes

def print_results(options, votes):
    total_votes = sum(votes)
    print('Sistema Operacional     Votos  %')
    print('----------------------------------')
    best_votes = 0
    best_option = ''
    for i, (option, vote) in enumerate(zip(options, votes), start=1):
        percentage = (vote * 100) / total_votes
        print(f'{option}   {vote}   {percentage:.2f}%')
        if vote > best_votes:
            best_votes = vote
            best_option = option
    print('----------------------------------')
    print(f'Total   {total_votes}')
    print(f'O Sistema Operacional mais votado foi o {best_option}, com {best_votes} votos, correspondendo a {percentage:.2f}% dos votos.')

def main():
    print('Qual o melhor Sistema Operacional para uso em servidores?')
    print('''1- Windows Server
    2- Unix
    3- Linux
    4- Netware
    5- Mac OS
    6- Outro''')
    options = ['Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro']
    votes = get_votes(options)
    print_results(options, votes)

if __name__ == "__main__":
    main()
