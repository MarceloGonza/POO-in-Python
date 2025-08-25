# se refiere a la posibilidad de crear una clase a partir de múltiples clases superiores
# tambien se pueden heredar las clases derivadas, en la herencia multinivel, las
#características de la clase y la clase derivada se heredan en la nueva clase derivada

#Herencia multinivel ejemplo:
    #class Base:
        #pass
    #class Derivado_uno(Base):
        #pass
    #class Derivado_dos(Derivado_uno):
        #pass

class Telefono:
    def __init__(self):
        pass
    def llamar(self):
        print('Llamando...')
    def ocupado(self):
        print('Ocupado...')

class Camara:
    def __init__(self):
        pass
    def fotografia(self):
        print('Capturando fotos...')

class Reproduccion:
    def __init__(self):
        pass
    def reproduccion_musica(self):
        print('Reproduciendo musica...')
    def reproducir_video(self):
        print('Reproduciendo video')

class smartphone(Telefono, Camara, Reproduccion):
    def __del__(self): #del se usa para limpiar los recursos
        print('telefono apagado')
#objeto con clase enlazada
movil = smartphone()
print(movil.llamar())
#print(dir(movil)) #dir imprime directorio con acciones que se pueden aplicar al objeto