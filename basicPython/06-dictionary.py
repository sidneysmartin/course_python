"""
Dictionary são uma estrutura de dados que armazena uma coleção de pares chave/valor
"""
player = {
  "name": "Zænd",
  "age": 21,
  "isMale": True,
  "Denominação": "Guerreiro",
  "level": 10,
  "power": 1500,
  "weapons": ["Espada", "Escudo", "Arco", "Adaga", "Besta"],
  "Atributes": ["Força", "Agilidade", "Vitalidade", "Resistência"],
  "isAlive": True
}

enemies = [
  {"name": "Dragão", "level": 100, "power": 5000, "isAlive": False},
  {"name": "Cavaleiro", "level": 50, "power": 2000, "isAlive": True},
  {"name": "Necromancer", "level": 80, "power": 3000, "isAlive": True},
  {"name": "Ladino", "level": 50, "power": 2000, "isAlive": True}
]

print(player)
print(enemies)
