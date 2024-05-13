""" 
A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":
alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125

Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:
ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB
O arquivo de entrada deve ser lido uma única vez, 
e os dados armazenados em memória, caso sejam necessários,
de forma a agilizar a execução do programa. 
A conversão da espaço ocupado em disco, 
de bytes para megabytes deverá ser feita através de uma função separada,
que será chamada pelo programa principal. 
O cálculo do percentual de uso também deverá 
ser feito através de uma função, que será chamada 
pelo programa principal.
"""


def read_users():
    with open('usuarios.txt', 'r') as archive:
        lines = archive.readlines()
    users = []
    spaces = []
    for linha in lines:
        user, space = linha.split()
        users.append(user)
        spaces.append(int(space))
    return users, spaces


def calculate_percents(spaces):
    total = sum(spaces)
    percentuais = [space / total for space in spaces]
    return percentuais


def save_registers(users, spaces, percentuais):
    with open('registers.txt', 'w') as archive:
        archive.write(
            'ACME Inc.               Uso do espaço em disco pelos usuários\n')
        archive.write(
            '------------------------------------------------------------------------\n')
        archive.write('Nr.  Usuário        Espaço utilizado     %% do uso\n')
        for i, (user, space, percentual) in enumerate(zip(users, spaces, percentuais), start=1):
            space_mb = space / (1024.0 * 1024.0)
            archive.write(
                f'{i} - {user} - {space_mb:.2f} MB - {percentual * 100.0:.2f}%\n')
        total_mb = sum(spaces) / (1024.0 * 1024.0)
        avg_mg = total_mb / len(users)
        archive.write(f'Espaço total ocupado: {total_mb:.2f} MB\n')
        archive.write(f'Espaço médio ocupado: {avg_mg:.2f} MB\n')


def main():
    users, spaces = read_users()
    percentuais = calculate_percents(spaces)
    save_registers(users, spaces, percentuais)


if __name__ == "__main__":
    main()
