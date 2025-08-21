
# Ejercicio Herencia
class culturistas:
    def __init__(self, nombreCulturista, categoria):
        self.nombreCulturista = nombreCulturista
        self.categoria = categoria
    def categoriaComp(self):
        return '{} es un culturista de la categoria {}'.format(self.nombreCulturista, self.categoria)
class cBum (culturistas):
    def peso (self, peso):
        return 'el culturista {} en competicion pesa: {}'.format(self.nombreCulturista, peso)
nuevoCulturista = cBum('CBum', 'Classic Physique',)
print(nuevoCulturista.categoriaComp())
print(nuevoCulturista.peso('100kg'))