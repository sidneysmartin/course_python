""" 
Faça um programa que simule um lançamento de dados.
Lance o dado 100 vezes e armazene os resultados 
em um vetor . 
Depois, mostre quantas vezes cada valor 
foi conseguido. 
Dica: use um vetor de contadores(1-6) 
e uma função para gerar números aleatórios, 
simulando os lançamentos dos dados.
"""
import random
numbers = [0] * 6
for i in range(1, 100):
    play = random.randint(1, 6)
    numbers[play - 1] = numbers[play - 1] + 1

count = 1
for play in numbers:
    print(f'{count} teve {play} lançamentos')
    count += 1
