"""
Faça um Programa que leia 2 números e em 
seguida pergunte ao usuário qual operação ele deseja realizar. 
O resultado da operação deve ser acompanhado de uma 
frase que diga se o número é:
a. par ou ímpar;
b. positivo ou negativo;
c. inteiro ou decimal
"""
def main():
    try:
        num1 = float(input("Digite o 1º valor: "))
        num2 = float(input("Digite o 2º valor: "))
        operation = input("Qual operação deseja fazer? (+, -, *, /): ")

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            result = num1 / num2
        else:
            print("Operação inválida. Escolha entre +, -, *, /")
            return

        print(f"O resultado da operação {operation} entre os números {num1} e {num2} é {result}")

        if result % 2 == 0:
            print("O número é par.")
        else:
            print("O número é ímpar.")

        if result > 0:
            print("O número é positivo.")
        elif result < 0:
            print("O número é negativo.")

        if result.is_integer():
            print("O número é inteiro.")
        else:
            print("O número é decimal.")
    except ValueError:
        print("Valores inválidos. Certifique-se de inserir números válidos.")

if __name__ == "__main__":
    main()
