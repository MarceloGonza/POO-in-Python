#significa quela clase superios defina comportamientos diferentes
# Es la capacidad que tiene los objetos en diferentes clases para usar
#un comportamiento o atributo del mismo nombre pero con diferente valor.

#class Auto:
    #rueda = 4
    #def desplazameinto(self): #metodo
        #print('El auto se desplaza sobre 4 ruedas')

#class Moto:
    #rueda = 2 #mismo objeto 'rueda', con diferentes valores
    #def desplazamiento(self):
        #print('La moto se desplaza en 2 ruedas')

#Polimorfismo y Herencia

class Animales:
    def __init__(self, nombre):
        self.nombre = nombre
    def tipo_animal(self):
        pass

class Leon(Animales):
    def tipo_animal(self):
        print('animal salvaje')
class Perro(Animales):
    def tipo_animal(self):
        print('animal domestico')

nuevo_animal = Leon('Simba')
nuevo_animal.tipo_animal()

nuevo_animal2 = Perro('Rex')
nuevo_animal2.tipo_animal()
