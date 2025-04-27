from Atleta import *

class Ciclista(Atleta):
    def __init__(self, aposentado, peso):
        Atleta.__init__(self, aposentado, peso)

    def pedalar(self):
        print(f"{__name__} está pedalando")
