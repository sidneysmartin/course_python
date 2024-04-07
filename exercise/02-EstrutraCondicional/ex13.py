# Faça um Programa que leia um número e exiba o dia correspondente da semana. 
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido. 

number = int(input("Digite um número de 1 a 7 e verifique o dia da semana: "))

daysOfWeek ={
  1 : "Domingo",
  2 : "Segunda-feira",
  3 : "Terça-feira",
  4 : "Quarta-feira",
  5 : "Quinta-feira",
  6 : "Sexta-feira",
  7 : "Sábado"
}

print(daysOfWeek.get(number, "Dia inválido"))