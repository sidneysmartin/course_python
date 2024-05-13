""" 
As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado alcançado durante o ano que passou. Para isto contratou você para desenvolver a aplicação que servirá como uma projeção de quanto será gasto com o pagamento deste abono.
Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do sindicato laboral, chegou-se a seguinte forma de cálculo:
a.Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro; a.O piso do abono será de 100 reais, isto é, aqueles funcionários cujo salário for muito baixo, recebem este valor mínimo; Neste momento, não se deve ter nenhuma preocupação com colaboradores com tempo menor de casa, descontos, impostos ou outras particularidades. Seu programa deverá permitir a digitação do salário de um número indefinido (desconhecido) de salários. Um valor de salário igual a 0 (zero) encerra a digitação. Após a entrada de todos os dados o programa deverá calcular o valor do abono concedido a cada colaborador, de acordo com a regra definida acima. Ao final, o programa deverá apresentar:
O salário de cada funcionário, juntamente com o valor do abono;
O número total de funcionário processados;
O valor total a ser gasto com o pagamento do abono;
O número de funcionário que receberá o valor mínimo de 100 reais;
O higher valor pago como abono; A tela abaixo é um exemplo de execução do programa, apenas para fins ilustrativos. Os valores podem mudar a cada execução do programa.
Projeção de Gastos com Abono
============================ 
 
Salário: 1000
Salário: 300
Salário: 500
Salário: 100
Salário: 4500
Salário: 0
 
Salário    - Abono     
R$ 1000.00 - R$  200.00
R$  300.00 - R$  100.00
R$  500.00 - R$  100.00
R$  100.00 - R$  100.00
R$ 4500.00 - R$  900.00
 
Foram processados 5 colaboradores
Total gasto com discount: R$ 1400.00
Valor mínimo pago a 3 colaboradores
Maior valor de abono pago: R$ 900.00
"""


def get_wage():
    print('Digite 0 para encerrar o programa')
    wages = []
    while True:
        salario = float(input('Salário: '))
        if salario == 0:
            break
        wages.append(salario)
    return wages


def calcular_abonos(wages):
    discount, minimum = 0, 0
    higher = 0
    for s in wages:
        abono = (s * 20) / 100
        if abono < 100:
            abono = 100
            minimum += 1
        if abono > higher:
            higher = abono
        discount += abono
    return discount, minimum, higher


def print_abonos(wages, discount, minimum, higher):
    print('Projeção de Gastos com Abono')
    print('============================')
    print('Salário - Abono')
    for s in wages:
        abono = (s * 20) / 100
        if abono < 100:
            abono = 100
        print('R$ %.2f - R$ %.2f' % (s, abono))
    print('Foram processados %d colaboradores' % len(wages))
    print('Total gasto com discount: R$ %.2f' % discount)
    print('Valor mínimo pago a %d colaboradores' % minimum)
    print('Maior valor de abono pago: R$ %.2f' % higher)


def main():
    wages = get_wage()
    discount, minimum, higher = calcular_abonos(wages)
    print_abonos(wages, discount, minimum, higher)


if __name__ == "__main__":
    main()
