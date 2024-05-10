"""
Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
"""
group = int(input("Informe valores entre 0 e 1000. "))

while group < 0 or group > 1000:
    group = int(input("Informe um conjunto entre 0 e 1000. "))

min_value = 0
max_value = 0
values = 0
count = 0
sum = 0
while count < group:
    while True:
        values = int(input(f"{count+1}º valor: "))
        if values > 0 and values < 1000:
            break
        else:
            print("Valor inválido. Tente novamente.")

    if count == 1:
        min_value = values
    if values >= max_value:
        max_value = values
    if values < min_value:
        min_value = values
    sum += values
    count += 1
print(f"Tamanho do conjunto {group}")
print(f"Menor valor {min_value}.")
print(f"Maior valor {max_value}.")
print(f"Soma dos valores {sum}.")
