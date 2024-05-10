"""
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""
name = input("Informe o nome: ")
while len(name) < 3:
  print("Nome inválido, informe nome com mais de 3 caracteres")
  name = input("Informe o nome: ")

print(f'Nome informado: {name}')

wage = float(input("Informe um salário maior que 0: "))
while wage < 0:
  print("Valor inválido")
  wage = float(input("Informe o salário válido: "))
  

print(f"Salário: R$ {wage}".format(2))