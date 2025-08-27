#CLASE Y ESTATICO:
#instancia : Un objeto se crea usando el constructor de una clase.
    #Una vez que el objeto es creado, se le conoce como una instancia de la clase

#TIPOS DE METODOS: 
    #1 = Estáticos
    #2 = Clase
    #3 = Instancia

#metodos clase: palabra reservada @classmethod
    #este metodo puede ser llamado sin crear una instancia de la clase
    #este metodo no tiene acceso a atributos de instancia

class Pastel:
    def __init__(self, ingredientes ):
        self.ingredientes = ingredientes

    def __repr__(self):
        return f'pastel({self.ingredientes !r})'

    @classmethod #con este metodo se usa cls, no self
    def Pastel_chocolate(cls):
        return cls(['harina', 'leche', 'chocolate'])
    @classmethod
    def Pastel_vainilla(cls):
        return cls(['harina', 'leche', 'vainilla'])
print(Pastel.Pastel_chocolate())

#METODO ESTATICO:
#@staticmethod : pueden ser llamados sin tener una instancia de la clase,
    #ademas este tipo de metodos notiene acceso al exterior por lo cual
    #no pueden acceder a ningun otro atributo o llamar a ninguna otra
    #funcion dentro de la clase
import math
class Disco:
    def __init__(self, materiales, volumen):
        self.materiales = materiales
        self.volumen = volumen
    def __repr__(self):
        return (f'materiales({self.materiales}, 'f'{self.volumen})')
    def area(self):
        return self.volumen_area(self.volumen)
    @staticmethod #no es necesario self o cls
    def volumen_area(A):
        return A ** 2 * math.pi

nuevo_disco = Disco(['PVC', 'Cemento', 'Moldes'], 4)
print(nuevo_disco.volumen_area(12))