"""
Uma fruteira está vendendo frutas com a seguinte tabela de preços
                 Até 5 kg Acima de 5 kg
- Morango R$ 2,50 por kg R$ 2,20 por kg
- Maçã R$ 1,80 por kg R$ 1,50 por kg
Se o cliente comprar mais de 8 kg em frutas ou o valor total 
da compra ultrapassar R$ 25,00, receberá ainda um desconto 
de 10% sobre este total. Escreva um algoritmo para ler a 
quantidade (em kg) de morangos e a quantidade (em kg) 
de maças adquiridas e escreva o valor a ser pago pelo cliente.

"""
def calcular_valor_frutas(peso_morango, peso_maca):
    pr_morango_ate_5kg = 2.5
    pr_morango_acima_5kg = 2.2
    pr_maca_ate_5kg = 1.8
    pr_maca_acima_5kg = 1.5

    total_morango = pr_morango_ate_5kg * peso_morango if peso_morango <= 5 else pr_morango_acima_5kg * peso_morango
    total_maca = pr_maca_ate_5kg * peso_maca if peso_maca <= 5 else pr_maca_acima_5kg * peso_maca

    valor_total = total_morango + total_maca

    # Aplica desconto de 10% se necessário
    if peso_morango + peso_maca > 8 or valor_total > 25:
        return valor_total * 0.9

    return valor_total

# Exemplo de uso:
peso_morango_comprado = 4  # Peso em kg
peso_maca_comprada = 3  # Peso em kg

valor_a_pagar = calcular_valor_frutas(peso_morango_comprado, peso_maca_comprada)
print(f"Valor a ser pago pelo cliente: R$ {valor_a_pagar:.2f}")
