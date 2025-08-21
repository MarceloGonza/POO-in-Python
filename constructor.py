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