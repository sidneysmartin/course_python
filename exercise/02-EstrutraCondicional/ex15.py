"""
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. 
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
- Dicas:
- Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
- Triângulo Equilátero: três lados iguais;
- Triângulo Isósceles: quaisquer dois lados iguais;
- Triângulo Escaleno: três lados diferentes;
"""
line1 = float(input("Lado 1: "))
line2 = float(input("Lado 2: "))
line3 = float(input("Lado 3: "))

triangle = {
  line1 == line2 == line3: "Equilátero",
  line1 == line2 or line1 == line3 or line2 == line3: "Isósceles",
  line1 != line2 != line3: "Escaleno"
}

print(f"O triângulo é {triangle.get(True)}")