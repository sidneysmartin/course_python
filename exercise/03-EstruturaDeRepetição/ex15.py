"""
    A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,... 
    Faça um programa capaz de gerar a série até o n−ésimo termo.
"""

n_terms = int(input("Informe um valor: "))
count = 0

f1, f2 = 0, 1

if n_terms <= 0:
    print("Informe valores positivos.")
elif n_terms == 1:
    print(f"Sequência fibonacci - {n_terms}")
    print(f1)
else:
    print("Sequência Fibonacci")
    while count < n_terms:
        print(f1)
        fib = f1 + f2
        f1 = f2
        f2 = fib
        count += 1
