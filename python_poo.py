# CLASES
# Nombre con mayuscula

class Auto:
    #atributos de la clase
    marca = ""
    modelo = 0
    placa = ""

taxi = Auto()
print(taxi.modelo)

# clase y objetos II
class nombre:
    pass
# creo un objeto y lo asigno a la clase
victor = nombre()
maria = nombre()

#objeto.atributo = valor

victor.edad = 30
victor.sexo = "masculino"
victor.pais = "Chile"

maria.edad = 23
maria.sexo = "femenino"
maria.pais = "Colombia"


print(victor.edad)
print(maria.pais)

# METODOS
# cuando una funcion esta dentro de una clase se le llama metodo
# un metodo determina una accion o comportamiento de un objeto
# DEF nombre del metodo (self(referirnos al objeto)) SELF.nombre variable = algoritmo

class Matematica:
    def suma(self):
        self.n1 = 2
        self.n2 = 3

s = Matematica()
s.suma()
print(s.n1 + s.n2)

# __ini__(SELF) cumple funcion de constructor (INICIAR)

class Ropa:
    def __init__(self):
        self.marca = 'Nike'
        self.talla = 'M'
        self.color = 'Negro'

camisa = Ropa()
print(camisa.talla)
print(camisa.marca)

class Calculadora:
    def __init__(self, n1, n2):
        self.suma = n1 + n2
        self.resta = n1 - n2
        self.division = n1 / n2
        self.multiplicacion = n1 * n2

operacion = Calculadora(2,3)
print(operacion.suma)

# FUNCIONES CON ATRIBUTOS

class Persona:
    edad = 27
    nombre = "Ernesto"
    pais = "Brasil"

medico = Persona()
# print('la edad es: ', medico.edad)
# print('la edad es: ', getattr(medico, 'edad')) #mismo resultado, obtengo el valor de forma directa

print('el medico tiene edad?', hasattr(medico, 'edad')) # retorna True
print('Antes era: ', medico.nombre)
setattr(medico, 'nombre', 'Marcos') #se llama en comillas para que acceda al valor declarado
print('Ahora se llama: ', medico.nombre)
delattr(Persona, 'pais') #elimina el atributo

# CONSTRUCTOR

class Familiar:
    def __init__(self, nombre1, parentesco):
        self.nombre1 = nombre1
        self.parentesco = parentesco
    def descripcion(self):
        return ' {} tiene {} años'.format(self.nombre1, self.parentesco)

    def comentario(self, frase):
        return '{} dice: {}'.format(self.nombre1 , frase)

humano = Familiar('Maria', 23)
print(humano.descripcion())
print(humano.comentario('Hola que tal?'))

# MODIFICAR UN ATRIBUTO

class Email:
    def __init__(self):
        self.enviado = False
    def enviar_correo(self):
        self.enviado = True
mi_correo = Email()

#print(mi_correo.enviado)
mi_correo.enviar_correo() #Llamo al otro metodo
print(mi_correo.enviado)

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

# Ejercicio Herencia
class culturistas:
    def __init__(self, nombreCulturista, categoria):
        self.nombreCulturista = nombreCulturista
        self.categoria = categoria
    def categoriaComp(self):
        return '{} es un culturista de la categoria {}'.format(self.nombreCulturista, self.categoria)
class cBum (culturistas):
    def peso (self, peso):
        return 'el culturista {} en competicion pesa: {}'.format(self.nombreCulturista, peso)
nuevoCulturista = cBum('CBum', 'Classic Physique',)
print(nuevoCulturista.categoriaComp())
print(nuevoCulturista.peso('100kg'))