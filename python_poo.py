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