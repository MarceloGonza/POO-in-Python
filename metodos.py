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