
class Calculadora:
    def __init__(self, numero):
        self.n = numero
        self.datos = [0 for i in range(numero)]

    def ingresarDato(self):
        self.datos = [int(input('ingresar datos: '+str(i+1)+ ' = ')) for i in range(self.n)]

class op_basicas(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,2)
    def suma(self):
        a,b, = self.datos
        s = a + b
        print('el resultado es: ' , s)

    def resta(self):
        a,b, = self.datos
        r = a - b
        print('el resultado es: ' , r)

class raiz(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,1)
    
    def cuadrada(self):
        import math
        a, = self.datos
        print('el resultado es: ', math.sqrt(a))

objeto =op_basicas()
#funcion integrada:
#verifica la herencia(si es correcto, devuelve true)
#dos paramentros: objeto y nombre de la clase

print(isinstance(objeto, raiz))

#verifica la herencia de clases
#clase padre mas una subclase
print(issubclass(op_basicas, Calculadora))