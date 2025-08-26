#f-strings = formatear strings

#.format % (se usa % s para concatenar) (visto anteriormente)
#str.format() (visto anteriormente)

#nombre = 'Rafael'
#edad = 25

#print("hola soy, % s y tengo % s años." %(nombre,edad)) 
#print('hola que tal soy {} y mi edad es {} años.'.format(nombre,edad))

#con f-string: (mas recomendada y legible)
#print(f"hola soy {nombre} y mi edad es {edad} años.")

class Estudiante:

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    #def __str__(self): #metodo para visualizar directamente, informal
    def __repr__(self): #metodo mas formal, asimila los valores y mantiene la escencia del codigo
        return f" hola que tal soy {self.nombre} {self.apellido} y tengo {self.edad} años"

nuevo_estudiante = Estudiante('Jorge', 'Garcia', 21)
print(f"{nuevo_estudiante  !r}") 