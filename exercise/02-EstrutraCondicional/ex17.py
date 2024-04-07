"""
Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
"""
year = int(input("Digite o ano: "))

leapYear = {
  year % 4 == 0 and year % 100 != 0 or year % 400 == 0: "bissexto",
  year % 4 != 0: "não bissexto"
}

checkYear = leapYear.get(True, "Ano inválido")

print(f"O ano {year} é {checkYear}")