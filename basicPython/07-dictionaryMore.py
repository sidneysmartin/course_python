import os
 
mensagens = []
nome = input("Nome: ")

while True:
  # limpar o terminal
  os.system('cls')
  if len(mensagens) > 0:
    for m in mensagens:
        print(m['nome'], '-', m['texto'])

  print("***************************")

  # obtendo texto
  texto = input("Mensagem: ")
  if texto == "fim":
   break


  # adicionando mensagem
  mensagens.append ({
      'nome': nome,
      'texto': texto  
  })