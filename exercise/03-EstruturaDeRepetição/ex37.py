""" 
Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do cliente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes
"""

topmost = 0
lower = 0
heaviest = 0
lighter = 0
code_topmost = 0
code_lower = 0
code_heaviest = 0
code_lighter = 0
sum_weight = 0
sum_height = 0

total = int(input("Total de alunos: "))

for i in range(total):
    code = int(input("Código: "))

    height = float(input("Altura: "))
    while height < 1.4 or height > 2.2:
        print("Altura deve estar entre 1.40 e 2.20 m.")
        height = float(input("Altura: "))

    weight = float(input("Peso: "))
    while weight < 40 or weight > 220:
        print("Peso deve estar entre 40 e 220 kg.")
        weight = float(input("Peso: "))

    sum_height += height
    sum_weight += weight
    if height > topmost:
        topmost = height
        code_topmost = code
    if height < lower:
        lower = height
        code_lower = code
    if weight > heaviest:
        heaviest = weight
        code_heaviest = code
    if weight < lighter:
        lighter = weight
        code_lighter = code

avg_height = sum_height / total
avg_weight = sum_weight / total

print(f"Código mais alto....: {code_topmost} - altura = {topmost} m.")
print(f"Código mais baixo...: {code_lower} - altura = {lower} m.")
print(f"Código mais pesado..: {code_heaviest} - peso = {heaviest} kg.")
print(f"Código menor peso...: {code_lighter} - peso = {lighter} kg.")
print(f"Altura média.......: {avg_height} m")
print(f"Peso médio.........: {avg_weight} kg")
