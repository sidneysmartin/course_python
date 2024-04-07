# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
vowels = ["a","e", "i", "o","u"]
consents = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

letter = input("Digite uma letra: ")

if letter.lower() in vowels:
  print(f"{letter} e uma vogal.")
elif letter.lower() in consents:
  print(f"{letter} e uma consoante.")
else:
  print(f"{letter} não é uma letra")
