"""
Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
a. A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
b. A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
c. A mensagem "Aprovado com Distinção", se a média for igual a 10.
"""

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

average = (n1 + n2 + n3) / 3

result = {
  average >= 7 and average < 10: "Aprovado",
  average < 7: "Reprovado",
  average == 10: "Aprovado com Distinção"  
}
finalResult = result.get(True, "Ano inválido")

print(f"O aluno foi {finalResult} com uma media de {average:.1f}")