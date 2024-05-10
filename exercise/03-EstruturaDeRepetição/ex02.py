"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
"""
name = input("Informe o nome: ")
passwd = input("Informe a senha: ")
while passwd == name:
  print("Senha inválida")
  passwd = input("Informe uma senha válida: ")

print("Cadastro realizado com sucesso.")