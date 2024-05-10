""" 
Faça um programa que peça um numero inteiro positivo e em seguida 
mostre este numero invertido.
Exemplo:
  12376489
  => 98467321
"""
# Solicita um número inteiro positivo do usuário
num = int(input("Digite um número inteiro positivo: "))

# Converte o número para uma lista de caracteres
num_list = list(str(num))

# Inverte a lista usando um loop for
num_list_reversed = [num_list[i] for i in range(len(num_list)-1, -1, -1)]

# Junta a lista invertida em uma string e converte para um número
num_reversed = int(''.join(num_list_reversed))

# Imprime o número invertido
print("O número invertido é:", num_reversed)
