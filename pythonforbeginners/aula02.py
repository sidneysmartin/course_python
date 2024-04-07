faturamento = 1200
custo = 500
novas_vendas = 300
faturamento = faturamento + novas_vendas
imposto = faturamento * 0.1
margem_lucro = faturamento * 0.2
restituicao = imposto * 0.1
lucro = faturamento - custo

tempo_em_meses = 160
tempo_em_anos = tempo_em_meses / 12

print("O faturamento foi de: ", faturamento)
print("O lucro foi de: ", lucro)
print("O custo foi de: ", margem_lucro  )
print("O custo foi de: ", custo)
print("O imposto foi de: ", imposto)
print("O tempo em anos foi de: ", tempo_em_anos)
print("O tempo em meses foi de: ", tempo_em_meses % 12)

exemple = 128_654_632 # edição visual da representação usando _
print(exemple)