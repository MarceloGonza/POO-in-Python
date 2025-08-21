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
