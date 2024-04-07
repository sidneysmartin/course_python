"""
FOR
Loop que percorre uma lista de valores definidos
"""
values = []

for i in range(1, 11):
  values.append(i)

print(values)

"""
WHILE
Loop que percorre uma lista de valores definidos enquanto uma condição for verdadeira (cuidado para o loop infinito)
"""
values = []

i = 1
while i  < 11:
  if i % 2 == 0:
    values.append(i)
  i += 1

print(values)