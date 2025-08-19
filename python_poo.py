# clase

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