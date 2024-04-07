"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) 
e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo 
aproximado de download do arquivo usando este link (em minutos).
"""
sizeFile = float(input("Informe o tamanho do arquivo: "))
lan = float(input("Informe a velocidade da internet: "))
time = ((sizeFile * 8) / lan ) / 60

print(f"O tempo de download: {time:.2f} minutos")