# HERENCIA
# Consiste en la posibilidad de crear una nueva clase a partir de una superior (base o padre) ya existente (clase derivada)

class pokemon: #clase superior
    def __init__(self, nombre_poke, tipo_poke):
        self.nombre_poke = nombre_poke
        self.tipo_poke = tipo_poke
    def descripcion(self):
        return '{} es un pokemon tipo: {}'.format(self.nombre_poke, self.tipo_poke)

class pikachu (pokemon): #le paso la clase padre como parametro
    def ataque (self, tipoataque):
        return 'el pokemon {} tiene como ataque: {}'.format(self.nombre_poke, tipoataque)

class charmander(pokemon):
    def ataque (self, tipoataque):
        return 'el pokemon {} tiene como ataque: {}'.format(self.nombre_poke, tipoataque)

nuevo_pokemon = pikachu('pika', 'electrico')
print(nuevo_pokemon.descripcion())
print(nuevo_pokemon.ataque('impact trueno'))
