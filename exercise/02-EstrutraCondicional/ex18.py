"""
Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
"""

def validar_data(data):
    """
    Validar a data informada no formato dd/mm/yyyy.
    Args:
        data (str): A data no formato dd/mm/yyyy.
    Returns:
        bool: True se a data for válida, False caso contrário.
    """
    try:
        day, month, year = map(int, data.split('/'))
        if 1 <= day <= 31 and 1 <= month <= 12 and 1000 <= year <= 9999:
            return True
        else:
            return False
    except ValueError:
        return False

def main():
    while True:
        input_data = input("Informe uma data (dd/mm/aaaa): ")
        if validar_data(input_data):
            print("Data válida!")
            break
        else:
            print("Formato inválido. Tente novamente.")

if __name__ == "__main__":
    main()
