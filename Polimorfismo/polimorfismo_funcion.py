#Polimorfismo por funcion
class Tomate:
    def tipo(self):
        print('Vegetal')
    def color(self):
        print('Rojo')

class Manzana:
    def tipo(self):
        print('Fruta')
    def color(self):
        print('Verde')

def funcion(objeto):
    objeto.tipo()
    objeto.color()

nuevo_tomate = Tomate()
funcion(nuevo_tomate)
nueva_manzana = Manzana()
funcion(nueva_manzana)

#Polimorfismo con metodo
#funciona bien cuando tenemos dos clases

class Colombia:
    def capital(self):
        print('Bogota')
    def idioma(self):
        print('español')
class Francia:
    def capital(self):
        print('Paris')
    def idioma(self):
        print('frances')

colombiano = Colombia()
frances = Francia()
for pais in (colombiano,frances):
    pais.capital()
    pais.idioma()

#Polimorfismo con Herencia
class Aves:
    def volar(self): #metodo que lleva el mismo nombre pero indica un sentido diferente
        print('la mayoria de las aves pueden volar')

class Aguila(Aves):
    def volar(self):
        print('las aguilas pueden volar')
class Gallina(Aves):
    def volar(self):
        print('La galllina no puede volar')

obj_ave = Aves()
obj_aguila = Aguila()
obj_gallina = Gallina()
obj_ave.volar()
obj_aguila.volar()
obj_gallina.volar()